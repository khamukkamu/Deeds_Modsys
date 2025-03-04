////////////////////////////////////////////////////////////////////////////////////
//POST EFFECT SHADERS........ 

#include "fx_configuration.h"

//#define ENABLE_EDITOR
//#define USE_CHARACTER_SHADOW_MERGE

float4 output_gamma;	// vectorize?
float4 output_gamma_inv;

static const float3 LUMINANCE_WEIGHTS = float3(0.299f, 0.587f, 0.114f);
static const float min_exposure = 0.15f;
static const float max_exposure = 3.0f;

#pragma warning(disable: 3571)		//pow(f,e) warning!

#define ERROR_OUT(c) c = float4(texCoord.x * 10 - floor(texCoord.x * 10) > 0.5, texCoord.y * 10 - floor(texCoord.y * 10) > 0.5, 0, 1)

// use postFX_sampler4 for point sampling
#if defined(USE_FX_STATE_MANAGER) && !defined(USE_DEVICE_TEXTURE_ASSIGN)	//else we can use direct device access with sampler indexes...
	texture postFX_texture0, postFX_texture1, postFX_texture2, postFX_texture3, postFX_texture4;

	//non-srgb samplers
	sampler postFX_sampler0 : register(s0) = sampler_state	{  Texture = postFX_texture0;  };	//linear clamp
	sampler postFX_sampler1 : register(s1) = sampler_state	{  Texture = postFX_texture1;  };	//linear clamp
	sampler postFX_sampler2 : register(s2) = sampler_state	{  Texture = postFX_texture2;  };	//linear clamp
	sampler postFX_sampler3 : register(s3) = sampler_state	{  Texture = postFX_texture3;  };	//linear clamp
	sampler postFX_sampler4 : register(s4) = sampler_state	{  Texture = postFX_texture4;  };	//linear clamp
	sampler postFX_sampler5 : register(s5); // depth
	sampler postFX_sampler16 : register(s0); // ref
	
#else 

	#ifdef USE_REGISTERED_SAMPLERS
	sampler postFX_sampler0 : register(s0);	//linear clamp
	sampler postFX_sampler1 : register(s1);	//linear clamp
	sampler postFX_sampler2 : register(s2);	//linear clamp
	sampler postFX_sampler3 : register(s3);	//linear clamp
	sampler postFX_sampler4 : register(s4);	//linear clamp
	#else
	sampler postFX_sampler0 : register(s0) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	 };	//linear clamp
	sampler postFX_sampler1 : register(s1) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	 };	//linear clamp
	sampler postFX_sampler2 : register(s2) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	 };	//linear clamp
	sampler postFX_sampler3 : register(s3) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	 };	//linear clamp
	sampler postFX_sampler4 : register(s4) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	 };	//linear clamp
	#endif

#endif
                                                                            
static const float BlurPixelWeight[8] = { 0.256, 0.240, 0.144, 0.135, 0.120, 0.065, 0.030, 0.010 };
//static const float BlurPixelWeight[8] = { 0.35537, 0.34185, 0.23821, 0.125861, 0.0813562, 0.04862, 0.025, 0.012552 };
//static const float BlurPixelWeight[8] = { 0.5537, 0.4185, 0.3821, 0.25861, 0.13562, 0.0862, 0.05, 0.02552 };
//static const float BlurPixelWeight[8] = { 0.2537, 0.2185, 0.1821, 0.15861, 0.082, 0.062, 0.03, 0.01552 };

bool showing_ranged_data = false;

float4 g_HalfPixel_ViewportSizeInv;
float  g_HDR_frameTime;	

float g_DOF_Focus = -0.005;
float g_DOF_Range = 5.19876;

#ifndef PS_2_X
	#define PS_2_X ps_2_b
#endif

#ifdef ENABLE_EDITOR
	//
	//postFX0- x:blurStr, y:exposure, z:range, w:temp
	//postFX1- brightness
	//postFX2- constrast
	//postFX3- saturation

	float4 postfx_editor_vector[4];
	
	#undef postfxTonemapOp
	#undef postfxParams1
	#undef postfxParams2
	#undef postfxParams3
	
	#define postfxTonemapOp		( int(postfx_editor_vector[0].x) )
	#define postfxParams1		float4(postfx_editor_vector[1].x, postfx_editor_vector[1].y, postfx_editor_vector[1].z, postfx_editor_vector[1].w)
	#define postfxParams2		float4(postfx_editor_vector[2].x, postfx_editor_vector[2].y, postfx_editor_vector[2].z, postfx_editor_vector[2].w)
	#define postfxParams3		float4(postfx_editor_vector[3].x, postfx_editor_vector[3].y, postfx_editor_vector[3].z, postfx_editor_vector[3].w)
	                                                                                                                                      
	#define RELATIVE_PS_TARGET PS_2_X	//we need more instruction_count to edit things dynamically
#else 
	//COMPILE_TIME_POSTFX_CONSTANTS
	// constants are defined from application to reduce inst. #
	//--#define 	postfxTonemapOp ((int)0)
	//--#define 	postfxParams1 (float4(16.0f, 1.0f, 1.0f, 1.0f))
	//--#define 	postfxParams2 (float4( 1.0f, 1.0f, 1.0f, 1.0f))
	
	#define RELATIVE_PS_TARGET ps_2_0
#endif

#define HDRRange 				(postfxParams1.x)
#define HDRExposureScaler 		(postfxParams1.y)
#define LuminanceAverageScaler 	(postfxParams1.z)
#define LuminanceMaxScaler 		(postfxParams1.w)

#define BrightpassTreshold 	(postfxParams2.x)
#define BrightpassPostPower (postfxParams2.y)
#define BlurStrenght 		(postfxParams2.z)
#define BlurAmount 			(postfxParams2.w)


#define HDRRangeInv 		(1.0f / HDRRange)

float CalculateWignette(float2 tc) {
	tc = tc - 0.5; // [-1/2, 1/2]
	return pow(1-dot(tc,tc), 4);
}
float4 radial(sampler2D tex, float2 texcoord, int samples, float startScale = 1.0, float scaleMul = 0.9){
    float4 c = 0;
    float scale = startScale;
    for(int i=0; i<samples; i++) {
        float2 uv = ((texcoord-0.5)*scale)+0.5;
        float4 s = tex2D(tex, uv);
        c += s;
        scale *= scaleMul;
    }
    c /= samples;
    return c;
}
float vignette(float2 pos, float inner, float outer){
  //float r = length(pos); //orj
  float r = dot(pos,pos);
  r = 1.0 - smoothstep(inner, outer, r);
  return r;
}
// Halton sequence generator for index i and base p
//float Halton(int i, int p)
//{
//    float h = 0.0;
//    float f = 1.0 / float(p);
//    int iH = i;
//    while (iH > 0)
//    {
//        h += f * float(iH % p);
//        iH = iH / p;
//        f = f / float(p);
//    }
//    return h;
//}

//// Improved hash function
//float2 hash22(float2 p)
//{
//    p = float2(dot(p, float2(127.1, 311.7)),
//               dot(p, float2(269.5, 183.3)));
//    return -1.0 + 2.0 * frac(sin(p) * 43758.5453123);
//}

//// Improved random normal function
//float3 randomNormal(float2 tex, int index)
//{
//    float z = Halton(index, 2); // Use Halton sequence for the z component
//    float2 xy = hash22(tex * 4.0); // Hash function for the angle
//    float angle = 6.28318530718 * xy.x; // 2*PI times the x component from hash
    
//    // Compute the normal from the spherical coordinates
//    float r = sqrt(1.0 - z * z);
//    return float3(r * cos(angle), r * sin(angle), z);
//}
float3 randomNormal(float2 tex)
{
    float z = frac(sin(dot(tex, float2(12.9898, 78.233))) * 43758.5453);
    float angle = z * 6.28318530718; // 2*PI
    return float3(cos(angle), sin(angle), sqrt(1.0 - z * z));
}

float3 normal_from_depth(float depth, float2 texcoords)
{
  
    const float2 offset1 = float2(0.0, 0.001);
    const float2 offset2 = float2(0.001, 0.0);
  
    float depth1 = tex2D(postFX_sampler5, texcoords + offset1).r;
    float depth2 = tex2D(postFX_sampler5, texcoords + offset2).r;
  
    float3 p1 = float3(offset1, depth1 - depth);
    float3 p2 = float3(offset2, depth2 - depth);
  
    float3 normal = cross(p1, p2);
    normal.z = -normal.z;
  
    return normalize(normal);
}

float ComputeSSAO(float2 texCoords)
{
    const float total_strength = 0.51;
    const float base = 0.3;
  
    const float area = 0.1175;
    const float falloff = 0.000001;
  
    const float radius = 0.001;
  
    const int samples = 16;
    float3 sample_sphere[samples] =
    {
        float3(0.5381, 0.1856, -0.4319), float3(0.1379, 0.2486, 0.4430),
      float3(0.3371, 0.5679, -0.0057), float3(-0.6999, -0.0451, -0.0019),
      float3(0.0689, -0.1598, -0.8547), float3(0.0560, 0.0069, -0.1843),
      float3(-0.0146, 0.1402, 0.0762), float3(0.0100, -0.1924, -0.0344),
      float3(-0.3577, -0.5301, -0.4358), float3(-0.3169, 0.1063, 0.0158),
      float3(0.0103, -0.5869, 0.0046), float3(-0.0897, -0.4940, 0.3287),
      float3(0.7119, -0.0154, -0.0918), float3(-0.0533, 0.0596, -0.5411),
      float3(0.0352, -0.0631, 0.5460), float3(-0.4776, 0.2847, -0.0271)
    };
    
    float3 random = normalize(randomNormal(texCoords * 4.0));
    float depth = tex2D(postFX_sampler5, texCoords).r;

    float3 position = float3(texCoords, depth);
    float3 normal = normal_from_depth(depth, texCoords);

    float radius_depth = radius / depth;
    float occlusion = 0.0;

	
    for (int i = 0; i < samples; i++)
    {
        float3 ray = radius_depth * reflect(sample_sphere[i], random);
        float3 hemi_ray = position + sign(dot(ray, normal)) * ray;
    
        float occ_depth = tex2D(postFX_sampler5, saturate(hemi_ray.xy)).r;
        float difference = depth - occ_depth;
    
        occlusion += step(falloff, difference) * (1.0 - smoothstep(falloff, area, difference));
    }
  
    float ao = 1.0 - total_strength * occlusion * (1.0 / samples);
    return saturate(ao + base);
}
float3 AdjustSaturation(float3 color, float saturation)
{
    // Gray-scale value of the color
    float gray = dot(color, float3(0.299, 0.587, 0.114));
    return lerp(float3(gray, gray, gray), color, saturation);
}
float3 SimpleColorGrade(float3 color, float contrast, float3 bias, float3 tint)
{
    color = color * contrast + 0.5 * (1.0 - contrast);
    color += bias;
    color = lerp(color, tint, 0.1); // blend a little bit of the tint color
    return color;
}
float3 LiftGammaGain(float3 color, float3 lift, float3 gamma, float3 gain)
{
    color = color * gain;
    color = pow(color, gamma);
    color = color + lift;
    return color;
}
float3 FilmicToneMapping(float3 x)
{
     float A = 0.15;
     float B = 0.50;
     float C = 0.10;
     float D = 0.20;
     float E = 0.02;
     float F = 0.30;

    return ((x * (A * x + C * B) + D * E) / (x * (A * x + B) + D * F)) - E / F;
}
float3 EnhanceContrast(float3 color, float contrast)
{
    return (color - 0.5) * contrast + 0.5;
}
float3 Desaturate(float3 color, float amount)
{
    float grayscale = dot(color, float3(0.299, 0.587, 0.114));
    return lerp(float3(grayscale, grayscale, grayscale), color, amount);
}
float3 tonemapping(const float3 scene_color, const float2 luminanceAvgMax, const int tonemapOp)
{
	
    float lum_avg = luminanceAvgMax.x * LuminanceAverageScaler;
    float lum_max = luminanceAvgMax.y * LuminanceMaxScaler;
    float saturation_level = 1.2;
	
    static const float MiddleValue = 0.85f;
	//float exposure = 1.4427 / (0.5 + lum_avg);
    float exposure = MiddleValue / (0.00001 + lum_avg);
    exposure = clamp(exposure * HDRExposureScaler, min_exposure, max_exposure);
	
    float3 scene_color_exposed = scene_color * (exposure * 1.5);
	
    float Lp = clamp(exposure / lum_avg, 0, 1) * max(scene_color_exposed.r, max(scene_color_exposed.g, scene_color_exposed.b));
    float3 final_color = 1.0 - exp2(-scene_color_exposed);

    final_color = LiftGammaGain(final_color, float3(0.024, 0.024, 0.044), float3(1, 1, 1), float3(1, 1, 1));
    final_color = SimpleColorGrade(final_color, 1.24, float3(-0.02, -0.02, -0.02), float3(0.95, 0.98, 1.05));
	
    final_color = AdjustSaturation(final_color, saturation_level);

    return lerp(scene_color_exposed, final_color, 0.5);
}

/////////////////////////////////////////////////////////////////////////////////////
struct VS_OUT_POSTFX
{
	float4 Pos:	POSITION;
	float2 Tex:	TEXCOORD0;
};
VS_OUT_POSTFX vs_main_postFX(float4 pos: POSITION){
	VS_OUT_POSTFX Out;

	Out.Pos = pos;
	Out.Tex = (float2(pos.x, -pos.y) * 0.5f + 0.5f) + g_HalfPixel_ViewportSizeInv.xy;
	
	return Out;
}
VertexShader vs_main_postFX_compiled = compile vs_2_0 vs_main_postFX();

/////////////////////////////////////////////////////////////////////////////////////
//float4 ps_main_postFX_Show(float2 texCoord: TEXCOORD0) : COLOR {

//	float4 color = tex2D(postFX_sampler0, texCoord);
	
//	if(showing_ranged_data) 
//	{
//		color.rgb *= HDRRange;
//		color.rgb = pow(color.rgb, output_gamma_inv);
//	}
//	return color;
//}
//technique postFX_Show
//{
//	pass P0
//	{
//		VertexShader = vs_main_postFX_compiled;
//		PixelShader = compile ps_2_0 ps_main_postFX_Show();
//	}
//}

/////////////////////////////////////////////////////////////////////////////////////
#ifdef USE_CHARACTER_SHADOW_MERGE


float4 ps_main_postFX_Shadowmap(float2 texCoord: TEXCOORD0) : COLOR {

	float original_shadowmap = tex2D(postFX_sampler0, texCoord).r;
	
	float character_shadow = tex2D(postFX_sampler1, texCoord).r;
	
	return min(original_shadowmap, character_shadow);
}
technique shadowmap_updater
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_postFX_Shadowmap();
	}
}
#endif
/////////////////////////////////////////////////////////////////////////////////////
//float4 color_value;

//float4 ps_main_postFX_TrueColor(float2 texCoord: TEXCOORD0) : COLOR
//{
//	const bool use_vignette = true;
	
//	float4 ret = color_value;
//	if(use_vignette)
//	{
//		ret.a = saturate(ret.a + ret.a * (1.0f - vignette(float2(texCoord.x*2-1, texCoord.y*2-1)*0.5f, 0.015f, 1.25f)) );	//remove blur from center
//	}
//	return ret;
//}
//technique postFX_TrueColor
//{
//	pass P0
//	{
//		VertexShader = vs_main_postFX_compiled;
//		PixelShader = compile ps_2_0 ps_main_postFX_TrueColor();
//	}
//}

/////////////////////////////////////////////////////////////////////////////////////


float4 ps_main_brightPass(uniform const bool with_luminance, float2 inTex: TEXCOORD0 ) : COLOR0 {

	float3 color = tex2D( postFX_sampler0, inTex );
	
	//get real-range
	color *= HDRRange;
		
	//bright pass 
	if(with_luminance)	//use luminance information to calculate exposure factor to be applied on blur rt
	{
		float2 lum_avgmax = tex2D( postFX_sampler4, float2(0.5f, 0.5f) ).rg;
		//color.rgb = tonemapping(color.rgb, lum_avgmax,0);//get exposed color
		
			static const float MiddleValue = 0.85f; 
			//float exposure = 1.4427 / (0.5 + lum_avg);
			float exposure_factor = MiddleValue / (0.00001 + lum_avgmax.x);	
			float exposure = 0.85 + exposure_factor * 0.15; 
			exposure = clamp(exposure*HDRExposureScaler, min_exposure, max_exposure);
			
			color.rgb = color.rgb * exposure;
		
		color.rgb = max(0.0f, color.rgb - BrightpassTreshold);
		/*color.rgb = pow(color.rgb, BrightpassPostPower);
		*/
		float intensity = dot(color.rgb, float3(.5f, .5f, .5f));
		float bloom_intensity = pow(intensity, BrightpassPostPower);
		color.rgb = color.rgb * ( bloom_intensity/intensity );
	}
	else 
	{
		color.rgb = max(0.0f, color.rgb - BrightpassTreshold);
		color.rgb = pow(color.rgb, BrightpassPostPower);
	}
	
	//we use interger format, turn back to normalized range
	color *= HDRRangeInv;
    return float4(color, 1);
}
technique postFX_brightPass
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile PS_2_X ps_main_brightPass(false);
	}
}
technique postFX_brightPass_WithLuminance
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
        PixelShader = compile PS_2_X ps_main_brightPass(true);
    }
}

/////////////////////////////////////////////////////////////////////////////////////

float4 ps_main_blurX( float2 inTex: TEXCOORD0 ) : COLOR0 {

	float2 BlurOffsetX = float2(g_HalfPixel_ViewportSizeInv.z,0);
	float4 color = 0;
	
	for( int i = 0; i < 8; i++ )
	{
		color += tex2D( postFX_sampler0, inTex + ( BlurOffsetX * i ) ) * BlurPixelWeight[i];
		color += tex2D( postFX_sampler0, inTex - ( BlurOffsetX * i ) ) * BlurPixelWeight[i];
	}
	
	return color;
}
float4 ps_main_blurY( float2 inTex: TEXCOORD0 ) : COLOR0 {
	float4 color = 0;//tex2D( postFX_sampler0, inTex ) ;

	float2 BlurOffsetY = float2(0, g_HalfPixel_ViewportSizeInv.w);
	
	for( int i = 0; i < 8; i++ )
	{
		color += tex2D( postFX_sampler0, inTex + ( BlurOffsetY * i ) ) * BlurPixelWeight[i];
		color += tex2D( postFX_sampler0, inTex - ( BlurOffsetY * i ) ) * BlurPixelWeight[i];
	}
	
	return color;
}
technique postFX_blurX
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_blurX();
	}
}
technique postFX_blurY
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_blurY();
	}
}

/////////////////////////////////////////////////////////////////////////////////////
//initial luminance calculation step
float4 ps_main_postFX_Average(float2 texCoord: TEXCOORD0) : COLOR {	

	static const float Offsets[4] = {-1.5f, -0.5f, 0.5f, 1.5f};
			
	float _max = 0;
	float _log_sum = 0;
	
	for (int x = 0; x < 4; x++)
	{
		for (int y = 0; y < 4; y++)
		{
			float2 vOffset = float2(Offsets[x], Offsets[y]) * float2(g_HalfPixel_ViewportSizeInv.y, g_HalfPixel_ViewportSizeInv.w);
			float3 color_here = tex2D(postFX_sampler0, texCoord + vOffset).rgb;
			float lum_here = dot(color_here * HDRRange, LUMINANCE_WEIGHTS);
			
			_log_sum += /*log*/(lum_here/*+ 0.0000001f*/);
			_max = max(_max, lum_here);
		}
	}
	
    return float4(_log_sum / 16, _max, 0, 1);
}
technique postFX_Average
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile PS_2_X ps_main_postFX_Average();
	}
}

float4 ps_main_postFX_AverageAvgMax(float2 texCoord: TEXCOORD0, uniform const bool smooth) : COLOR {

	static const float Offsets[4] = {-1.5f, -0.5f, 0.5f, 1.5f};
			
	float _max = 0;
	float _sum = 0;
	
	//downsample and find avg-max luminance
	for (int x = 0; x < 4; x++)
	{
		for (int y = 0; y < 4; y++)
		{
			float2 vOffset = float2(Offsets[x], Offsets[y]) * float2(g_HalfPixel_ViewportSizeInv.y, g_HalfPixel_ViewportSizeInv.w);
			float2 lumAvgMax_here = tex2D(postFX_sampler0, texCoord + vOffset).rg;
			

			_sum += lumAvgMax_here.r * lumAvgMax_here.r;
			_max = max(_max, lumAvgMax_here.g);
		}
	}
	float _avg = _sum / 16; 
	
	float4 new_ret = float4(sqrt(_avg), _max, 0, 1);
	
	if(smooth)
	{
		//last step,  finish average luminance calculation
		new_ret.r = /*exp*/(new_ret.r);
		
		float2 prev_avgmax = tex2D(postFX_sampler4, float2(0.5f, 0.5f)).rg;
		
		//new_ret.xy = lerp(prev_avgmax, new_ret, /*1.0f); //*/g_HDR_frameTime );/***/
		new_ret.x = lerp(prev_avgmax.x, new_ret.x, g_HDR_frameTime );
		new_ret.y = max(0.1f, lerp(prev_avgmax.y, new_ret.y, g_HDR_frameTime ) );
	}
	
	return new_ret;
}
technique postFX_AverageAvgMax
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile PS_2_X ps_main_postFX_AverageAvgMax(false);
	}
}
technique postFX_AverageAvgMax_Smooth
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile PS_2_X ps_main_postFX_AverageAvgMax(true);
	}
}

/////////////////////////////////////////////////////////////////////////////////////
struct VsOut_Convert_FP2I 
{
	float4 Pos:			POSITION;
	float2 texCoord0:	TEXCOORD0;
	float2 texCoord1:	TEXCOORD1;
	float2 texCoord2:	TEXCOORD2;
	float2 texCoord3:	TEXCOORD3;
};
VsOut_Convert_FP2I vs_main_postFX_Convert_FP2I(float4 pos: POSITION){
	VsOut_Convert_FP2I Out;

	Out.Pos = pos;

	// Texture coordinates
	float2 texCoord = (float2(pos.x, -pos.y) * 0.5f + 0.5f) + g_HalfPixel_ViewportSizeInv.xy;
	
	Out.texCoord0 = texCoord + float2(-1.0,  1.0) * g_HalfPixel_ViewportSizeInv.xy;
	Out.texCoord1 = texCoord + float2( 1.0,  1.0) * g_HalfPixel_ViewportSizeInv.xy;
	Out.texCoord2 = texCoord + float2( 1.0, -1.0) * g_HalfPixel_ViewportSizeInv.xy;
	Out.texCoord3 = texCoord + float2(-1.0, -1.0) * g_HalfPixel_ViewportSizeInv.xy;
	
	return Out;
}
float4 ps_main_postFX_Convert_FP2I(float2 texCoord0: TEXCOORD0, float2 texCoord1: TEXCOORD1, float2 texCoord2: TEXCOORD2, float2 texCoord3: TEXCOORD3) : COLOR0 {

	float3 rt;
	
#define gamma_corrected_input
#ifdef gamma_corrected_input
	rt  = tex2D(postFX_sampler4, texCoord0).rgb;
	rt += tex2D(postFX_sampler4, texCoord1).rgb;
	rt += tex2D(postFX_sampler4, texCoord2).rgb;
	rt += tex2D(postFX_sampler4, texCoord3).rgb;
#else

	rt  = pow(tex2D(postFX_sampler4, texCoord0).rgb, output_gamma);
	rt += pow(tex2D(postFX_sampler4, texCoord1).rgb, output_gamma);
	rt += pow(tex2D(postFX_sampler4, texCoord2).rgb, output_gamma);
	rt += pow(tex2D(postFX_sampler4, texCoord3).rgb, output_gamma);
#endif
	rt *= 0.25;
	//rt = BrightPass(rt);
	rt *= HDRRangeInv;
	
	return float4(rt.rgb,1);
}
technique postFX_Convert_FP2I
{
	pass P0
	{
		VertexShader = compile vs_2_0 vs_main_postFX_Convert_FP2I();
		PixelShader = compile ps_2_0 ps_main_postFX_Convert_FP2I();
	}
}

/////////////////////////////////////////////////////////////////////////////////////
float4 ps_main_postFX_DofBlur(uniform const bool using_hdr, uniform const bool using_depth, float2 texCoord: TEXCOORD0) : COLOR {

	float3 sample_start = tex2D(postFX_sampler0, texCoord).rgb;
	float depth_start;
	if(using_depth)
	{
		depth_start = tex2D(postFX_sampler1, texCoord).rgb;
	}
	
	static const int SAMPLE_COUNT = 8;
	static const float2 offsets[SAMPLE_COUNT] = {
		-1, -1,
		  0, -1,
		  1, -1,
		 -1,  0,
		  1,  0,
		 -1,  1,
		  0,  1,
		  1,  1,
	};
	
	float sampleDist = g_HalfPixel_ViewportSizeInv.x * 3.14f;
	float3 sample = sample_start;
	
	for (int i = 0; i < SAMPLE_COUNT; i++) {
	
		float2 sample_pos = texCoord + sampleDist * offsets[i];
		
		// !using_hdr -> non-lineer gamma!
		float3 sample_here;
		if(using_depth) {	
			float depth_here = tex2D(postFX_sampler1, sample_pos).r;
			if(depth_here < depth_start) 
			{
				sample_here = sample_start;
			}
			else {
				sample_here = tex2D(postFX_sampler0, sample_pos).rgb;
			}
		}
		else {
			sample_here = tex2D(postFX_sampler0, sample_pos).rgb;
		}
		
		sample += sample_here;
	}

	sample /= SAMPLE_COUNT+1;
	
	//sample.rgb =  pow(sample, input_gamma); 
	//sample.rgb = pow(sample.rgb, output_gamma_inv);
	
	
	//return pow(tex2D(postFX_sampler0, texCoord), input_gamma);
	return float4(sample.rgb, 1);
}
technique postFX_DofBlurHDR
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_postFX_DofBlur(true, false);
	}
}
technique postFX_DofBlurLDR
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_postFX_DofBlur(false, false);
	}
}
technique postFX_DofBlurHDR_Depth
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_postFX_DofBlur(true, true);
	}
}
technique postFX_DofBlurLDR_Depth
{
	pass P0
	{
		VertexShader = vs_main_postFX_compiled;
		PixelShader = compile ps_2_0 ps_main_postFX_DofBlur(false, true);
	}
}

/////////////////////////////////////////////////////////////////////////////////////
float OverlayBlend(float base, float blend)
{
    return base < 0.5 ? (2.0 * base * blend) : (1.0 - 2.0 * (1.0 - base) * (1.0 - blend));
}
float4 FinalScenePassPS(uniform const bool use_dof, uniform const int use_hdr, uniform const bool use_auto_exp, float2 texCoord: TEXCOORD0) : COLOR {
		
	// Sample the scene
    float4 scene = tex2D(postFX_sampler0, texCoord);
	scene.rgb  = pow(scene.rgb, output_gamma);
    float ssao = ComputeSSAO(texCoord);
    scene.rg *= pow(OverlayBlend(ssao, ssao),10);
    scene.b *= pow(OverlayBlend(ssao, ssao), 5);
	
	#ifndef ENABLE_EDITOR	//we disable dof in editor mode so that we can fit in ps 2.0
	if(use_dof) {
		float  pixelDepth = tex2D(postFX_sampler4, texCoord).r;
		
		float focus_factor01 = abs(g_DOF_Focus - pixelDepth);
		
		// static const bool use_depthRT_focus = false; 
		// if(use_depthRT_focus) {
		// 	focus_factor01 = tex2D(postFX_samplerX, texCoord).r;
		// }
		
		float lerp_factor = min(saturate(g_DOF_Range * focus_factor01), 0.62);
		//float lerp_factor = saturate(5 * focus_factor01);
		
		
		static const bool use_wignette = true;
		if(use_wignette) {
			lerp_factor *= 1 - vignette(float2(texCoord.x*2-1, texCoord.y-0.6), 0.015, 0.5);	//remove blur from center
		}

		float4 dofColor = tex2D(postFX_sampler3, texCoord);
		if(use_hdr) {
			dofColor *= HDRRange;
		}
		dofColor.rgb  = pow(dofColor.rgb, output_gamma);
		
		scene = lerp(scene, dofColor, lerp_factor);
	}
	#endif
	
	float4 color, blur;
	
	if(use_hdr > 0) {
		blur  = tex2D(postFX_sampler1,  texCoord);
		blur.rgb = pow(blur.rgb, BlurStrenght);
		
		blur.rgb *= HDRRange;
			
		float2 luminanceAvgMax;
		if(use_auto_exp) {
			luminanceAvgMax = tex2D(postFX_sampler2, float2(0.5f, 0.5f)).rg;
		}
		else {
			luminanceAvgMax = float2(0.5, 10.2);
		}
		
		// tonemap.. 
		color = scene; 
		
		color += blur * BlurAmount;
		color.rgb = tonemapping(color.rgb, luminanceAvgMax, postfxTonemapOp);
	}
	else {
		color = scene;
	}
	//gamma correction
	color.rgb = pow(color.rgb, output_gamma_inv);
    return color;
}

//postFX_final_[dof]_[hdr_quality]_[auto_exposure]
technique postFX_final_0_0_0{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS( false, 0, false);	} }
technique postFX_final_0_1_0{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS( false, 1, false);	} }
technique postFX_final_0_2_0{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS( false, 2, false);	} }
technique postFX_final_0_1_1{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS( false, 1, true);	} }
technique postFX_final_0_2_1{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS( false, 2, true);	} }
technique postFX_final_1_0_0{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS(  true, 0, false);	} }
technique postFX_final_1_1_0{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS(  true, 1, false);	} }
technique postFX_final_1_2_0{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS(  true, 2, false);	} }
technique postFX_final_1_1_1{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS(  true, 1, true);	} }
technique postFX_final_1_2_1{	pass P0	{   VertexShader = vs_main_postFX_compiled;		PixelShader = compile PS_2_X FinalScenePassPS(  true, 2, true);	} }
                                                                                                                                                 

//Recycle Bin: 