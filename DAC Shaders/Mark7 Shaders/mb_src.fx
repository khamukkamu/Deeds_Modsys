///////////////////////////////////////////////////////////////////////////////////
//
// Mount&Blade Warband Shaders
// You can add edit main shaders and lighting system with this file.
// You cannot change fx_configuration.h file since it holds application dependent 
// configration parameters. Sorry its not well documented. 
// Please send your feedbacks to our forums.
//
// All rights reserved.
// www.taleworlds.com
//
//
///////////////////////////////////////////////////////////////////////////////////
// compile_fx.bat:
// ------------------------------
// @echo off
// fxc /D PS_2_X=ps_2_a /T fx_2_0 /Fo mb_2a.fxo mb.fx
// fxc /D PS_2_X=ps_2_b /T fx_2_0 /Fo mb_2b.fxo mb.fx
// pause>nul
///////////////////////////////////////////////////////////////////////////////////


#if !defined (PS_2_X)
	#error "define high quality shader profile: PS_2_X ( ps_2_b or ps_2_a )"
#endif

#include "fx_configuration.h"	// source code dependent configration definitions..

////////////////////////////////////////////////////////////////////////////////
//definitions: 
#define NUM_LIGHTS					10
#define NUM_SIMUL_LIGHTS			4
#define NUM_WORLD_MATRICES			32

#define PCF_NONE					0
#define PCF_DEFAULT					1
#define PCF_NVIDIA					2


#define INCLUDE_VERTEX_LIGHTING
#define VERTEX_LIGHTING_SCALER   1.0f	//used for diffuse calculation
#define VERTEX_LIGHTING_SPECULAR_SCALER   1.0f

#define USE_PRECOMPILED_SHADER_LISTS


//put this to un-reachable code blocks..
#define GIVE_ERROR_HERE {for(int i = 0; i < 1000; i++)		{Output.RGBColor *= Output.RGBColor;}}
#define GIVE_ERROR_HERE_VS {for(int i = 0; i < 1000; i++)		{Out.Pos *= Out.Pos;}}

//#define NO_GAMMA_CORRECTIONS

#ifdef NO_GAMMA_CORRECTIONS
#define INPUT_TEX_GAMMA(col_rgb) (col_rgb) = (col_rgb)
#define INPUT_OUTPUT_GAMMA(col_rgb) (col_rgb) = (col_rgb)
#define OUTPUT_GAMMA(col_rgb) (col_rgb) = (col_rgb)
#else
#define INPUT_TEX_GAMMA(col_rgb) (col_rgb) = pow((col_rgb), input_gamma.x) 
#define INPUT_OUTPUT_GAMMA(col_rgb) (col_rgb) = pow((col_rgb), output_gamma.x) 
#define OUTPUT_GAMMA(col_rgb) (col_rgb) = pow((col_rgb), output_gamma_inv.x) 
#endif
	
#ifdef DONT_INIT_OUTPUTS
	#pragma warning( disable : 4000)
#define INITIALIZE_OUTPUT(structure, var)	structure var;
#else
#define INITIALIZE_OUTPUT(structure, var)	structure var = (structure)0;
#endif

#pragma warning( disable : 3571)	//pow(f,e)


//Categories..
#define OUTPUT_STRUCTURES
#define FUNCTIONS

//Constant categories
#define PER_MESH_CONSTANTS
#define PER_FRAME_CONSTANTS
#define PER_SCENE_CONSTANTS
#define APPLICATION_CONSTANTS

//Shader categories
#define MISC_SHADERS
#define UI_SHADERS
#define SHADOW_RELATED_SHADERS
#define WATER_SHADERS
#define SKYBOX_SHADERS
#define HAIR_SHADERS
#define FACE_SHADERS
#define FLORA_SHADERS
#define MAP_SHADERS
#define SOFT_PARTICLE_SHADERS
#define STANDART_SHADERS
#define STANDART_RELATED_SHADER
#define OCEAN_SHADERS
#ifdef USE_NEW_TREE_SYSTEM
#define NEWTREE_SHADERS
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#ifdef PER_MESH_CONSTANTS

float4x4 matWorldViewProj;
float4x4 matWorldView;
float4x4 matWorld;

float4x4 matWaterWorldViewProj;
float4x4 matWorldArray[NUM_WORLD_MATRICES] : WORLDMATRIXARRAY;
	//float4   matBoneOriginArray[NUM_WORLD_MATRICES];

float4 vMaterialColor = float4(255.f / 255.f, 230.f / 255.f, 200.f / 255.f, 1.0f);
float4 vMaterialColor2;
float fMaterialPower = 16.f;
float4 vSpecularColor = float4(5, 5, 5, 5);
float4 texture_offset = { 0, 0, 0, 0 };

int iLightPointCount;
int iLightIndices[NUM_SIMUL_LIGHTS] = { 0, 1, 2, 3 };
	
bool bUseMotionBlur = false;
float4x4 matMotionBlur;
#endif

////////////////////////////////////////
#ifdef PER_FRAME_CONSTANTS
float time_var = 0.0f;
float4x4 matWaterViewProj;
#endif

////////////////////////////////////////
#ifdef PER_SCENE_CONSTANTS


float fFogDensity = 0.05f;

float3 vSkyLightDir;
float4 vSkyLightColor;
float3 vSunDir;
float4 vSunColor;
	
float4 vAmbientColor = float4(64.f / 255.f, 64.f / 255.f, 64.f / 255.f, 1.0f);
float4 vGroundAmbientColor = float4(84.f / 255.f, 44.f / 255.f, 54.f / 255.f, 1.0f);

float4 vCameraPos;
float4x4 matSunViewProj;
float4x4 matView;
float4x4 matViewProj;
	
float3 vLightPosDir[NUM_LIGHTS];
float4 vLightDiffuse[NUM_LIGHTS];
float4 vPointLightColor; //agerage color of lights
	
float reflection_factor;
#endif

////////////////////////////////////////
#ifdef APPLICATION_CONSTANTS
bool use_depth_effects = false;
float far_clip_Inv;
float4 vDepthRT_HalfPixel_ViewportSizeInv;

float fShadowMapNextPixel = 1.0f / 4096;
float fShadowMapSize = 4096;

static const float input_gamma = 2.62f;
float4 output_gamma = float4(2.62f, 2.62f, 2.62f, 2.62f); //STR: float4 yapyldy
float4 output_gamma_inv = float4(1.0f / 2.62f, 1.0f / 2.62f, 1.0f / 2.62f, 1.0f / 2.62f);

float4 debug_vector = { 0, 0, 0, 1 };
	
float spec_coef = 1.0f; //valid value after module_data!
	
	
static const float map_normal_detail_factor = 1.4f;
static const float uv_2_scale = 1.237;
//	static const float fShadowBias = 0.00002f;//-0.000002f;
static const float fShadowBias = 0.00000f; //-0.000002f;
	
#ifdef USE_NEW_TREE_SYSTEM
float flora_detail = 40.0f;
#define flora_detail_fade 		(flora_detail*FLORA_DETAIL_FADE_MUL)
#define flora_detail_fade_inv 	(flora_detail-flora_detail_fade)
#define flora_detail_clip 		(max(0,flora_detail_fade - 20.0f))
#endif

#endif

// Wind data inputs
float fWindDirectionX = 0.5; // Direction of the wind
float fWindDirectionZ = 0.5; // Direction of the wind
float fWindPower = 0.2; // Power of the wind
float fWaveFrequency = 0.5;
float fWaveSpeed = 1.4;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Texture&Samplers
#if defined(USE_SHARED_DIFFUSE_MAP) || !defined(USE_DEVICE_TEXTURE_ASSIGN)
texture diffuse_texture;
#endif

#ifndef USE_DEVICE_TEXTURE_ASSIGN
texture diffuse_texture_2;
texture specular_texture;
texture normal_texture;
texture env_texture;
texture shadowmap_texture;

texture cubic_texture;
	
texture depth_texture;
texture screen_texture;

#ifdef USE_REGISTERED_SAMPLERS
sampler ReflectionTextureSampler : register(fx_ReflectionTextureSampler_RegisterS) = sampler_state
{
    Texture = env_texture;
};
sampler EnvTextureSampler : register(fx_EnvTextureSampler_RegisterS) = sampler_state
{
    Texture = env_texture;
};
sampler Diffuse2Sampler : register(fx_Diffuse2Sampler_RegisterS) = sampler_state
{
    Texture = diffuse_texture_2;
};
sampler NormalTextureSampler : register(fx_NormalTextureSampler_RegisterS) = sampler_state
{
    Texture = normal_texture;
};
sampler SpecularTextureSampler : register(fx_SpecularTextureSampler_RegisterS) = sampler_state
{
    Texture = specular_texture;
};
sampler DepthTextureSampler : register(fx_DepthTextureSampler_RegisterS) = sampler_state
{
    Texture = depth_texture;
};
sampler CubicTextureSampler : register(fx_CubicTextureSampler_RegisterS) = sampler_state
{
    Texture = cubic_texture;
};
sampler ShadowmapTextureSampler : register(fx_ShadowmapTextureSampler_RegisterS) = sampler_state
{
    Texture = shadowmap_texture;
};
sampler ScreenTextureSampler : register(fx_ScreenTextureSampler_RegisterS) = sampler_state
{
    Texture = screen_texture;
};
sampler MeshTextureSampler : register(fx_MeshTextureSampler_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
sampler ClampedTextureSampler : register(fx_ClampedTextureSampler_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
sampler FontTextureSampler : register(fx_FontTextureSampler_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
sampler CharacterShadowTextureSampler : register(fx_CharacterShadowTextureSampler_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
sampler MeshTextureSamplerNoFilter : register(fx_MeshTextureSamplerNoFilter_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
sampler DiffuseTextureSamplerNoWrap : register(fx_DiffuseTextureSamplerNoWrap_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
sampler GrassTextureSampler : register(fx_GrassTextureSampler_RegisterS) = sampler_state
{
    Texture = diffuse_texture;
};
#else 
	
	
	sampler ReflectionTextureSampler 	= sampler_state	{  Texture = env_texture;		AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler EnvTextureSampler			= sampler_state	{  Texture = env_texture;		AddressU = WRAP;  AddressV = WRAP;  MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler Diffuse2Sampler 			= sampler_state	{  Texture = diffuse_texture_2;	AddressU = WRAP; AddressV = WRAP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler NormalTextureSampler		= sampler_state	{  Texture = normal_texture;	AddressU = WRAP; AddressV = WRAP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler SpecularTextureSampler 		= sampler_state	{  Texture = specular_texture;	AddressU = WRAP; AddressV = WRAP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler DepthTextureSampler 		= sampler_state	{  Texture = depth_texture;		AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;    }; 
	sampler CubicTextureSampler 		= sampler_state	{  Texture = cubic_texture;	 	AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;   }; 
	sampler ShadowmapTextureSampler 	= sampler_state	{  Texture = shadowmap_texture;	AddressU = CLAMP; AddressV = CLAMP; MinFilter = NONE; MagFilter = NONE;	};
	sampler ScreenTextureSampler 		= sampler_state	{  Texture = screen_texture;	AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	};
	sampler MeshTextureSampler 			= sampler_state	{  Texture = diffuse_texture;	AddressU = WRAP; AddressV = WRAP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler ClampedTextureSampler 		= sampler_state	{  Texture = diffuse_texture;	AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler FontTextureSampler 			= sampler_state	{  Texture = diffuse_texture;	AddressU = WRAP; AddressV = WRAP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler CharacterShadowTextureSampler= sampler_state	{  Texture = diffuse_texture;	AddressU = BORDER; AddressV = BORDER; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	sampler MeshTextureSamplerNoFilter 	= sampler_state	{  Texture = diffuse_texture;	AddressU = WRAP; AddressV = WRAP; MinFilter = NONE; MagFilter = NONE;	}; 
	sampler DiffuseTextureSamplerNoWrap = sampler_state	{  Texture = diffuse_texture;	AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	};
	sampler GrassTextureSampler 		= sampler_state	{  Texture = diffuse_texture;	AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR;	}; 
	
#endif
	
#else 

	sampler ReflectionTextureSampler 	: register(fx_ReflectionTextureSampler_RegisterS 		); 
	sampler EnvTextureSampler			: register(fx_EnvTextureSampler_RegisterS				); 
	sampler Diffuse2Sampler 			: register(fx_Diffuse2Sampler_RegisterS 				); 
	sampler NormalTextureSampler		: register(fx_NormalTextureSampler_RegisterS			); 
	sampler SpecularTextureSampler 		: register(fx_SpecularTextureSampler_RegisterS 			); 
	sampler DepthTextureSampler 		: register(fx_DepthTextureSampler_RegisterS 			);  
	sampler DepthTextureSampler 		: register(fx_CubicTextureSampler_RegisterS 			);
	sampler ShadowmapTextureSampler 	: register(fx_ShadowmapTextureSampler_RegisterS 		);
	sampler ScreenTextureSampler 		: register(fx_ScreenTextureSampler_RegisterS			);
		
#ifdef USE_SHARED_DIFFUSE_MAP
		sampler MeshTextureSampler 			: register(fx_MeshTextureSampler_RegisterS 				) = sampler_state	{  Texture = diffuse_texture;	}; 
		sampler ClampedTextureSampler 		: register(fx_ClampedTextureSampler_RegisterS 			) = sampler_state	{  Texture = diffuse_texture;	}; 
		sampler FontTextureSampler 			: register(fx_FontTextureSampler_RegisterS 				) = sampler_state	{  Texture = diffuse_texture;	}; 
		sampler CharacterShadowTextureSampler:register(fx_CharacterShadowTextureSampler_RegisterS	) = sampler_state	{  Texture = diffuse_texture;	}; 
		sampler MeshTextureSamplerNoFilter 	: register(fx_MeshTextureSamplerNoFilter_RegisterS 		) = sampler_state	{  Texture = diffuse_texture;	}; 
		sampler DiffuseTextureSamplerNoWrap : register(fx_DiffuseTextureSamplerNoWrap_RegisterS 	) = sampler_state	{  Texture = diffuse_texture;	};
		sampler GrassTextureSampler 		: register(fx_GrassTextureSampler_RegisterS 			) = sampler_state	{  Texture = diffuse_texture;	}; 
#else   
		sampler MeshTextureSampler 			: register(fx_MeshTextureSampler_RegisterS 				); 
		sampler ClampedTextureSampler 		: register(fx_ClampedTextureSampler_RegisterS 			); 
		sampler FontTextureSampler 			: register(fx_FontTextureSampler_RegisterS 				); 
		sampler CharacterShadowTextureSampler:register(fx_CharacterShadowTextureSampler_RegisterS	); 
		sampler MeshTextureSamplerNoFilter 	: register(fx_MeshTextureSamplerNoFilter_RegisterS 		); 
		sampler DiffuseTextureSamplerNoWrap : register(fx_DiffuseTextureSamplerNoWrap_RegisterS 	);
		sampler GrassTextureSampler 		: register(fx_GrassTextureSampler_RegisterS 			); 
#endif
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef OUTPUT_STRUCTURES

struct PS_OUTPUT
{
    float4 RGBColor : COLOR;
};

#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef FUNCTIONS
// Mark7 Sun Amount
float GetSunAmount(uniform const int PcfMode, float4 ShadowTexCoord, float2 ShadowTexelPos)
{
    float sun_amount;
    
    // Light and Shadows control Mark7
    const int NUM_SAMPLES = 16;
    float shadowSoftness = 0.000234;
    float shadowIntensity = 0.95; // Change as per your needs
    float shadowContrast = 0.95; // Change as per your needs
    
    float2 offsets[NUM_SAMPLES] =
    {
        float2(-1.5, -1.5), float2(-0.5, -1.5), float2(0.5, -1.5), float2(1.5, -1.5),
    float2(-1.5, -0.5), float2(-0.5, -0.5), float2(0.5, -0.5), float2(1.5, -0.5),
    float2(-1.5, 0.5), float2(-0.5, 0.5), float2(0.5, 0.5), float2(1.5, 0.5),
    float2(-1.5, 1.5), float2(-0.5, 1.5), float2(0.5, 1.5), float2(1.5, 1.5)
    };
    if (PcfMode == PCF_NVIDIA)
    {
        sun_amount = 0.0f;
        for (int i = 0; i < NUM_SAMPLES; ++i)
        {
            float2 offsetTexCoord = ShadowTexCoord.xy + offsets[i] * shadowSoftness;
            sun_amount += tex2Dproj(ShadowmapTextureSampler, float4(offsetTexCoord, ShadowTexCoord.z, ShadowTexCoord.w)).r;
        }
        sun_amount /= NUM_SAMPLES;
    }
    else
    {
        float2 lerps = frac(ShadowTexelPos);
		//read in bilerp stamp, doing the shadow checks
        float sourcevals[4];
        sourcevals[0] = (tex2D(ShadowmapTextureSampler, ShadowTexCoord).r < ShadowTexCoord.z) ? 0.0f : 1.0f;
        sourcevals[1] = (tex2D(ShadowmapTextureSampler, ShadowTexCoord + float2(fShadowMapNextPixel, 0)).r < ShadowTexCoord.z) ? 0.0f : 1.0f;
        sourcevals[2] = (tex2D(ShadowmapTextureSampler, ShadowTexCoord + float2(0, fShadowMapNextPixel)).r < ShadowTexCoord.z) ? 0.0f : 1.0f;
        sourcevals[3] = (tex2D(ShadowmapTextureSampler, ShadowTexCoord + float2(fShadowMapNextPixel, fShadowMapNextPixel)).r < ShadowTexCoord.z) ? 0.0f : 1.0f;

		// lerp between the shadow values to calculate our light amount
        sun_amount = lerp(lerp(sourcevals[0], sourcevals[1], lerps.x), lerp(sourcevals[2], sourcevals[3], lerps.x), lerps.y);
    }
    
    // After calculating sun_amount
    sun_amount *= shadowIntensity;
    sun_amount = saturate((sun_amount - 0.5f) * shadowContrast + 0.5); // Apply contrast

    return sun_amount;
}

////////////////////////////////////////
float get_fog_amount(float d)
{
	//return 1/(d * fFogDensity * 20);
	//   return saturate((fFogEnd - d) / (fFogEnd - fFogStart));
    return 1.0f / exp2(d * fFogDensity);
	//return 1.0f / exp ((d * fFogDensity) * (d * fFogDensity));
}

float get_fog_amount_new(float d, float wz)
{
	//you can implement world.z based algorithms here
    return get_fog_amount(d);
}

////////////////////////////////////////
static const float2 specularShift = float2(0.138 - 0.5, 0.254 - 0.5);
static const float2 specularExp = float2(256.0, 32.0) * 0.7;
static const float3 specularColor0 = float3(0.9, 1.0, 1.0) * 0.898 * 0.99;
static const float3 specularColor1 = float3(1.0, 0.9, 1.0) * 0.74 * 0.99;

float HairSingleSpecularTerm(float3 T, float3 H, float exponent)
{
    float dotTH = dot(T, H);
    float sinTH = sqrt(1.0 - dotTH * dotTH);
    return pow(sinTH, exponent);
}

float3 ShiftTangent(float3 T, float3 N, float shiftAmount)
{
    return normalize(T + shiftAmount * N);
}

// GGX & Calculations Mark7
float3 FresnelSchlick(float cosTheta, float3 F0)
{
    return F0 + (1.0 - F0) * pow(1.0 - cosTheta, 5.0);
}
float GGX_Distribution(float NdotH, float roughness)
{
    float alpha = roughness * roughness;
    float alphaSq = alpha * alpha;
    float denom = (NdotH * NdotH) * (alphaSq - 1.0) + 1.0;
    return alphaSq / (3.14 * denom * denom);
}

float Geometry_SchlickGGX(float NdotV, float roughness)
{
    float r = (roughness + 1.0);
    float k = (r * r) / 8.0; // This is an approximation by Epic for Unreal Engine 4
    float denom = NdotV * (1.0 - k) + k;
    return NdotV / denom;
}

float Geometry_Smith(float NdotL, float NdotV, float roughness)
{
    float ggx1 = Geometry_SchlickGGX(NdotL, roughness);
    float ggx2 = Geometry_SchlickGGX(NdotV, roughness);
    return ggx1 * ggx2;
}

float3 Fresnel_Schlick(float cosTheta, float3 F0)
{
    return F0 + (1.0 - F0) * pow(1.0 - cosTheta, 5.0);
}

float3 GGX_Specular(float3 lightVec, float3 viewVec, float3 normal, float roughness, float3 F0)
{
    float3 H = normalize(viewVec + lightVec);
    float NdotL = max(dot(normal, lightVec), 0.0);
    float NdotV = max(dot(normal, viewVec), 0.1);
    float NdotH = max(dot(normal, H), 0.0);
    float VdotH = max(dot(viewVec, H), 0.0);

    float D = GGX_Distribution(NdotH, roughness);
    float G = Geometry_Smith(NdotL, NdotV, roughness);
    float3 F = Fresnel_Schlick(VdotH, F0);

    return (D * G * F) / (4.0 * NdotL * NdotV);
}

// enchased spec hair calculations Mark7
float3 calculate_hair_specular(float3 normal, float3 tangent, float3 lightVec, float3 viewVec, float2 tc)
{
	// Shift tangents
    float shiftTex = tex2D(Diffuse2Sampler, tc).a;
	
    float3 T1 = ShiftTangent(tangent, normal, specularShift.x + shiftTex);
    float3 T2 = ShiftTangent(tangent, normal, specularShift.y + shiftTex);

    float3 H = normalize(lightVec + viewVec);
    float NdotH = max(dot(normal, H), 0.0);
    float NdotL = max(dot(normal, lightVec), 0.0);
    float NdotV = max(dot(normal, viewVec), 0.0);

    // Use Schlick's approximation for Fresnel
    float3 F0 = specularColor0 * specularColor0 * specularColor0; // Base reflectivity, you can set this per hair type or texture
    float3 fresnel = FresnelSchlick(NdotV, F0);

    // Calculate the specular term using a microfacet model
    float3 specular = vSunColor.rgb * fresnel * GGX_Specular(NdotH, NdotL, NdotV, 0.92, F0);

    // Modulate secondary specular term with noise, as before
    float specularMask = tex2D(Diffuse2Sampler, tc).a;
    specular *= specularMask;

    // Combine with secondary specular shifted tangent, as before
    float3 specular2 = vSunColor.rgb * specularColor1 * HairSingleSpecularTerm(T2, H, specularExp.y);
    specular2 *= specularMask;

    // Final specular combination
    float specularAttenuation = saturate(1.75 * NdotL + 0.25);
    float3 finalSpecular = (specular + specular2) * specularAttenuation;
    
    return finalSpecular;
}

float HairDiffuseTerm(float3 N, float3 L)
{
    return saturate(0.75 * dot(N, L) + 0.25);
}

float face_NdotL(float3 n, float3 l)
{

    float wNdotL = dot(n.xyz, l.xyz);
    return saturate(max(0.2f * (wNdotL + 0.9f), wNdotL));
}

// Improve diffuse point light Mark7
float4 calculate_point_lights_diffuse(const float3 vWorldPos, const float3 vWorldN, const bool face_like_NdotL, const bool exclude_0)
{
    const int exclude_index = 0;
    float4 total = 0;
    for (int j = 0; j < iLightPointCount; j++)
    {
        if (!exclude_0 || j != exclude_index)
        {
            int i = iLightIndices[j];
            float3 point_to_light = vLightPosDir[i] - vWorldPos;
            float distanceSquared = dot(point_to_light, point_to_light);
            float3 L = normalize(point_to_light);
            float NdotL = saturate(dot(vWorldN, L));
            
            // Attenuation factors
            float constant = 1.0f; // Consider making these shader constants or uniforms
            float lin = 0.7f;
            float quadratic = 1.8f;
            float attenuation = 2.8f / (constant + lin * sqrt(distanceSquared) + quadratic * distanceSquared);

            // Diffuse contribution
            float diffuseFactor = face_like_NdotL ? max(0.2f * (NdotL + 0.9f), NdotL) : NdotL;
            total += diffuseFactor * vLightDiffuse[i] * attenuation;
        }
    }
    return total;
}

// Improve spec point light Mark7
float4 calculate_point_lights_specular(const float3 vWorldPos, const float3 vWorldN, const float3 vWorldView, const bool exclude_0)
{
    const int exclude_index = 0;
    float4 total = 0;

    for (int i = 0; i < iLightPointCount; i++)
    {
        if (!exclude_0 || i != exclude_index)
        {
            float3 point_to_light = vLightPosDir[i] - vWorldPos;
            float distanceSquared = dot(point_to_light, point_to_light);
            float3 L = normalize(point_to_light);
            float3 V = normalize(vWorldView);
            float3 H = normalize(V + L);

            // Compute attenuation
            float constant = 1.0f; // These should be tweaked
            float lin = 0.7f;
            float quadratic = 1.8f;
            float attenuation = 2.8f / (constant +
            lin * sqrt
            (distanceSquared) + quadratic * distanceSquared);
            
            // Compute the specular term
            float specularCoefficient = pow(saturate(dot(vWorldN, H)), fMaterialPower);
            // Assuming vLightSpecular[i] is your light's specular color
            float4 specularColor = vLightDiffuse[i]; // Add this if you have a specular color for your lights

            // Apply the specular term to the total lighting
            total += attenuation * specularColor * specularCoefficient;
        }
    }

    return total;
}

// Improve ambient term Mark7

float4 get_ambientTerm(int ambientTermType, float3 normal, float3 DirToSky, float sun_amount)
{
    float4 ambientTerm;
    if (ambientTermType == 0)	//constant
    {
        ambientTerm = vAmbientColor;
    }
    else if (ambientTermType == 1)	//hemisphere
    {
        float4 g_vGroundColorTEMP = vGroundAmbientColor * sun_amount;
        float4 g_vSkyColorTEMP = vAmbientColor;
		
        float lerpFactor = (dot(normal, DirToSky) + 1.0f) * 0.5f;
		
        float4 hemiColor = lerp(g_vGroundColorTEMP, g_vSkyColorTEMP, lerpFactor);
        ambientTerm = hemiColor;
    }
    else //if(ambientTermType == 2)	//ambient cube 
    {
        float4 cubeColor = texCUBE(CubicTextureSampler, normal);
        ambientTerm = vAmbientColor * cubeColor;
    }
    return ambientTerm;
}


float4x4 build_instance_frame_matrix(float3 vInstanceData0, float3 vInstanceData1, float3 vInstanceData2, float3 vInstanceData3)
{
    const float3 position = vInstanceData0.xyz;
	//const float  scale = vInstanceData0.w;
	
	
    float3 frame_s = vInstanceData1;
    float3 frame_f = vInstanceData2;
    float3 frame_u = vInstanceData3; //cross(frame_s, frame_f);;
	
    float4x4 matWorldOfInstance =
    {
        float4(frame_s.x, frame_f.x, frame_u.x, position.x),
									float4(frame_s.y, frame_f.y, frame_u.y, position.y),
									float4(frame_s.z, frame_f.z, frame_u.z, position.z),
									float4(0.0f, 0.0f, 0.0f, 1.0f)
    };

    return matWorldOfInstance;
}


float4 skinning_deform(float4 vPosition, float4 vBlendWeights, float4 vBlendIndices)
{
    return mul(matWorldArray[vBlendIndices.x], vPosition /*- matBoneOriginArray[vBlendIndices.x]*/) * vBlendWeights.x
			+ mul(matWorldArray[vBlendIndices.y], vPosition /*- matBoneOriginArray[vBlendIndices.y]*/) * vBlendWeights.y
			+ mul(matWorldArray[vBlendIndices.z], vPosition /*- matBoneOriginArray[vBlendIndices.z]*/) * vBlendWeights.z
			+ mul(matWorldArray[vBlendIndices.w], vPosition /*- matBoneOriginArray[vBlendIndices.w]*/) * vBlendWeights.w;
}


#define DEFINE_TECHNIQUES(tech_name, vs_name, ps_name)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_name(PCF_NONE); \
							PixelShader = compile PS_2_X ps_name(PCF_NONE);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_name(PCF_DEFAULT); \
							PixelShader = compile PS_2_X ps_name(PCF_DEFAULT);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_name(PCF_NVIDIA); \
							PixelShader = compile ps_2_a ps_name(PCF_NVIDIA);} } 

#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#define	DEFINE_LIGHTING_TECHNIQUE(tech_name, use_dxt5, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)
							

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef MISC_SHADERS	//notexture, clear_floating_point_buffer, diffuse_no_shadow, simple_shading, simple_shading_no_filter, no_shading, no_shading_no_alpha

//shared vs_font
struct VS_OUTPUT_FONT
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
};
VS_OUTPUT_FONT vs_font(float4 vPosition : POSITION, float4 vColor : COLOR, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_FONT Out;

    Out.Pos = mul(matWorldViewProj, vPosition);

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;

	//apply fog
    float d = length(P);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}
VertexShader vs_font_compiled_2_0 = compile vs_2_0 vs_font();

//---
struct VS_OUTPUT_NOTEXTURE
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float Fog : FOG;
};
VS_OUTPUT_NOTEXTURE vs_main_notexture(float4 vPosition : POSITION, float4 vColor : COLOR)
{
    VS_OUTPUT_NOTEXTURE Out;

    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Color = vColor * vMaterialColor;
    float3 P = mul(matWorldView, vPosition); //position in view space
	//apply fog
    float d = length(P);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}
PS_OUTPUT ps_main_notexture(VS_OUTPUT_NOTEXTURE In)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
    return Output;
}
technique notexture
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_notexture();
        PixelShader = compile PS_2_X ps_main_notexture();
    }
}

//---
struct VS_OUTPUT_CLEAR_FLOATING_POINT_BUFFER
{
    float4 Pos : POSITION;
};
VS_OUTPUT_CLEAR_FLOATING_POINT_BUFFER vs_clear_floating_point_buffer(float4 vPosition : POSITION)
{
    VS_OUTPUT_CLEAR_FLOATING_POINT_BUFFER Out;

    Out.Pos = mul(matWorldViewProj, vPosition);

    return Out;
}
PS_OUTPUT ps_clear_floating_point_buffer()
{
    PS_OUTPUT Out;
    Out.RGBColor = float4(0.0f, 0.0f, 0.0f, 0.0f);
    return Out;
}
technique clear_floating_point_buffer
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_clear_floating_point_buffer();
        PixelShader = compile PS_2_X ps_clear_floating_point_buffer();
    }
}

//---
struct VS_OUTPUT_FONT_X
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float Fog : FOG;
};

VS_OUTPUT_FONT_X vs_main_no_shadow(float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
    VS_OUTPUT_FONT_X Out;

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor + vLightColor;
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;
    diffuse_light += saturate(dot(vWorldN, -vSunDir)) * vSunColor;
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//apply fog
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}
PS_OUTPUT ps_main_no_shadow(VS_OUTPUT_FONT_X In)
{
    PS_OUTPUT Output;
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);
    Output.RGBColor = In.Color * tex_col;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    return Output;
}
PS_OUTPUT ps_simple_no_filtering(VS_OUTPUT_FONT_X In)
{
    PS_OUTPUT Output;
    float4 tex_col = tex2D(MeshTextureSamplerNoFilter, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);
    Output.RGBColor = In.Color * tex_col;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    return Output;
}
PS_OUTPUT ps_no_shading(VS_OUTPUT_FONT In)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
	//Output.RGBColor *= tex2D(DiffuseTextureSamplerNoWrap, In.Tex0);
    Output.RGBColor *= tex2D(MeshTextureSampler, In.Tex0);
	
//	Output.RGBColor = float4(1,0,0,1);
    return Output;
}
PS_OUTPUT ps_no_shading_no_alpha(VS_OUTPUT_FONT In)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
    Output.RGBColor *= tex2D(MeshTextureSamplerNoFilter, In.Tex0);
    Output.RGBColor.a = 1.0f;
    return Output;
}

technique diffuse_no_shadow
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_no_shadow();
        PixelShader = compile PS_2_X ps_main_no_shadow();
    }
}
technique simple_shading //Uses gamma
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_main_no_shadow();
    }
}
technique simple_shading_no_filter //Uses gamma
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_simple_no_filtering();
    }
}
technique no_shading
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_no_shading();
    }
}
technique no_shading_no_alpha
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_no_shading_no_alpha();
    }
}

#endif

///////////////////////////////////////////////
#ifdef UI_SHADERS
PS_OUTPUT ps_font_uniform_color(VS_OUTPUT_FONT In)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
    Output.RGBColor.a *= tex2D(FontTextureSampler, In.Tex0).a;
    return Output;
}
PS_OUTPUT ps_font_background(VS_OUTPUT_FONT In)
{
    PS_OUTPUT Output;
    Output.RGBColor.a = 1.0f; //In.Color.a;
    Output.RGBColor.rgb = tex2D(FontTextureSampler, In.Tex0).rgb + In.Color.rgb;
	//	Output.RGBColor.rgb += 1.0f - In.Color.a;
	
    return Output;
}
PS_OUTPUT ps_font_outline(VS_OUTPUT_FONT In)
{
    float4 sample = tex2D(FontTextureSampler, In.Tex0);
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
    Output.RGBColor.a = (1.0f - sample.r) + sample.a;
	
    Output.RGBColor.rgb *= sample.a + 0.05f;
	
    Output.RGBColor = saturate(Output.RGBColor);
	
    return Output;
}

technique font_uniform_color
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_font_uniform_color();
    }
}
technique font_background
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_font_background();
    }
}
technique font_outline
{
    pass P0
    {
        VertexShader = vs_font_compiled_2_0;
        PixelShader = compile PS_2_X ps_font_outline();
    }
}

#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef SHADOW_RELATED_SHADERS

struct VS_OUTPUT_SHADOWMAP
{

    float4 Pos : POSITION;
    float2 Tex0 : TEXCOORD0;
    float Depth : TEXCOORD1;
};
VS_OUTPUT_SHADOWMAP vs_main_shadowmap_skin(float4 vPosition : POSITION, float2 tc : TEXCOORD0, float4 vBlendWeights : BLENDWEIGHT, float4 vBlendIndices : BLENDINDICES)
{
    VS_OUTPUT_SHADOWMAP Out;

    float4 vObjectPos = skinning_deform(vPosition, vBlendWeights, vBlendIndices);
	
    Out.Pos = mul(matWorldViewProj, vObjectPos);
    Out.Depth = Out.Pos.z / Out.Pos.w;
    Out.Tex0 = tc;

    return Out;
}
VS_OUTPUT_SHADOWMAP vs_main_shadowmap(float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_SHADOWMAP Out;
    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Depth = Out.Pos.z / Out.Pos.w;
	
    if (1)
    {
        float3 vScreenNormal = mul((float3x3) matWorldViewProj, vNormal); //normal in screen space
        Out.Depth -= vScreenNormal.z * (fShadowBias);
    }

    Out.Tex0 = tc;
    return Out;
}
VS_OUTPUT_SHADOWMAP vs_main_shadowmap_biased(float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_SHADOWMAP Out;
    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Depth = Out.Pos.z / Out.Pos.w;
	
    if (1)
    {
        float3 vScreenNormal = mul((float3x3) matWorldViewProj, vNormal); //normal in screen space
        Out.Depth -= vScreenNormal.z * (fShadowBias);
		
        Out.Pos.z += (0.0025f); //extra bias!
    }

    Out.Tex0 = tc;
    return Out;
}

PS_OUTPUT ps_main_shadowmap(VS_OUTPUT_SHADOWMAP In)
{
    PS_OUTPUT Output;
    Output.RGBColor.a = tex2D(MeshTextureSampler, In.Tex0).a;
    Output.RGBColor.a -= 0.5f;
    clip(Output.RGBColor.a);
	
    Output.RGBColor.rgb = In.Depth; // + fShadowBias;

    return Output;
}
VS_OUTPUT_SHADOWMAP vs_main_shadowmap_light(uniform const bool skinning, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0,
											float4 vBlendWeights : BLENDWEIGHT, float4 vBlendIndices : BLENDINDICES)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_SHADOWMAP, Out);

    return Out;
}
PS_OUTPUT ps_main_shadowmap_light(VS_OUTPUT_SHADOWMAP In)
{
    PS_OUTPUT Output;
	
    Output.RGBColor = float4(1, 0, 0, 1);
	
    return Output;
}
PS_OUTPUT ps_render_character_shadow(VS_OUTPUT_SHADOWMAP In)
{
    PS_OUTPUT Output;
    Output.RGBColor = 1.0f;
	//!! Output.RGBColor.rgb = In.Depth;
	//!! Output.RGBColor.a = 1.0f;
    return Output;
}

VertexShader vs_main_shadowmap_compiled = compile vs_2_0 vs_main_shadowmap();
VertexShader vs_main_shadowmap_skin_compiled = compile vs_2_0 vs_main_shadowmap_skin();

PixelShader ps_main_shadowmap_compiled = compile PS_2_X ps_main_shadowmap();
PixelShader ps_main_shadowmap_light_compiled = compile PS_2_X ps_main_shadowmap_light();
PixelShader ps_render_character_shadow_compiled = compile PS_2_X ps_render_character_shadow();


technique renderdepth
{
    pass P0
    {
        VertexShader = vs_main_shadowmap_compiled;
        PixelShader = ps_main_shadowmap_compiled;
    }
}
technique renderdepth_biased
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_shadowmap_biased();
        PixelShader = ps_main_shadowmap_compiled;
    }
}

technique renderdepthwithskin
{
    pass P0
    {
        VertexShader = vs_main_shadowmap_skin_compiled;
        PixelShader = ps_main_shadowmap_compiled;
    }
}
technique renderdepth_light
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_shadowmap_light(false);
        PixelShader = ps_main_shadowmap_light_compiled;
    }
}
technique renderdepthwithskin_light
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_shadowmap_light(true);
        PixelShader = ps_main_shadowmap_light_compiled;
    }
}

technique render_character_shadow
{
    pass P0
    {
        VertexShader = vs_main_shadowmap_compiled;
        PixelShader = ps_render_character_shadow_compiled;
    }
}
technique render_character_shadow_with_skin
{
    pass P0
    {
        VertexShader = vs_main_shadowmap_skin_compiled;
        PixelShader = ps_render_character_shadow_compiled;
    }
}

//--
float blurred_read_alpha(float2 texCoord)
{
    float3 sample_start = tex2D(CharacterShadowTextureSampler, texCoord).rgb;
	
    static const int SAMPLE_COUNT = 4;
    static const float2 offsets[SAMPLE_COUNT] =
    {
        -1, 1,
		 1, 1,
		0, 2,
		0, 3,
    };
	
    float blur_amount = saturate(1.0f - texCoord.y);
    blur_amount *= blur_amount;
    float sampleDist = (6.0f / 256.0f) * blur_amount;
    float sample = sample_start;
	
    for (int i = 0; i < SAMPLE_COUNT; i++)
    {
        float2 sample_pos = texCoord + sampleDist * offsets[i];
        float sample_here = tex2D(CharacterShadowTextureSampler, sample_pos).a;
        sample += sample_here;
    }

    sample /= SAMPLE_COUNT + 1;
    return sample;
}
struct VS_OUTPUT_CHARACTER_SHADOW
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float2 Tex0 : TEXCOORD0;
    float4 Color : COLOR0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
};
VS_OUTPUT_CHARACTER_SHADOW vs_character_shadow(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_CHARACTER_SHADOW, Out);
	
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    if (PcfMode != PCF_NONE)
    {
		//shadow mapping variables
        float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal));

        float wNdotSun = max(-0.0001, dot(vWorldN, -vSunDir));
        Out.SunLight = (wNdotSun) * vSunColor;

        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }

    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;
	
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}
PS_OUTPUT ps_character_shadow(uniform const int PcfMode, VS_OUTPUT_CHARACTER_SHADOW In)
{
    PS_OUTPUT Output;
	
    if (PcfMode == PCF_NONE)
    {
        Output.RGBColor.a = blurred_read_alpha(In.Tex0) * In.Color.a;
    }
    else
    {
        float sun_amount = 0.05f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        Output.RGBColor.a = saturate(blurred_read_alpha(In.Tex0) * In.Color.a * sun_amount);
    }
    Output.RGBColor.rgb = In.Color.rgb;
	//Output.RGBColor = float4(tex2D(CharacterShadowTextureSampler, In.Tex0).a, 0, 0, 1);

	//!! Output.RGBColor.a *= 0.1f;
    return Output;
}

DEFINE_TECHNIQUES(character_shadow, vs_character_shadow, ps_character_shadow)


PS_OUTPUT ps_character_shadow_new(uniform const int PcfMode, VS_OUTPUT_CHARACTER_SHADOW In)
{
    PS_OUTPUT Output;
	
    if (PcfMode == PCF_NONE)
    {
        Output.RGBColor.a = tex2D(CharacterShadowTextureSampler, In.Tex0).r * In.Color.a;
    }
    else
    {
        float sun_amount = 0.05f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        Output.RGBColor.a = saturate(tex2D(CharacterShadowTextureSampler, In.Tex0).r * In.Color.a * sun_amount);
    }
    Output.RGBColor.rgb = In.Color.rgb;
	//Output.RGBColor = float4(tex2D(CharacterShadowTextureSampler, In.Tex0).a, 0, 0, 1);
    return Output;
}

DEFINE_TECHNIQUES(character_shadow_new, vs_character_shadow, ps_character_shadow_new)

#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef WATER_SHADERS
// Mark7 Water

struct VS_OUTPUT_WATER
{
    float4 Pos : POSITION;
    float2 Tex0 : TEXCOORD0;
    float4 LightDir_Alpha : TEXCOORD1; //light direction for bump
    float4 LightDif : TEXCOORD2; //light diffuse for bump
    float3 CameraDir : TEXCOORD3; //camera direction for bump
    float4 PosWater : TEXCOORD4; //position according to the water camera
    float Fog : FOG;
	
    float4 projCoord : TEXCOORD5;
    float Depth : TEXCOORD6;
    float3 WorldPos : TEXCOORD7;

};
VS_OUTPUT_WATER vs_main_water(uniform const bool use_distort, float4 vPosition : POSITION, float3 vNormal : NORMAL, float4 vColor : COLOR, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL)
{
    VS_OUTPUT_WATER Out = (VS_OUTPUT_WATER) 0;

    Out.Pos = mul(matWorldViewProj, vPosition);
  
	//!Out.Pos = mul(matViewProj, vPosition);
	
    Out.PosWater = mul(matWaterWorldViewProj, vPosition);
  
    
    float3 vWorldPos = (float3) mul(matWorld, vPosition);
    float3 point_to_camera_normal = normalize(vCameraPos - vWorldPos);
    Out.WorldPos = vWorldPos;
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space
      
    if (use_distort)
    {
    // Apply wind-based vertex deformation
        float waveHeight = sin(dot(vPosition.xz, float2(fWindDirectionX, fWindDirectionZ) * vWorldPos.yz) * fWaveFrequency + time_var * fWaveSpeed) * fWindPower;
        Out.Pos.y += waveHeight;
    }
    
    float3 P = mul(matWorldView, vPosition); //position in view space

    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    Out.CameraDir = mul(TBNMatrix, point_to_camera_normal);

    Out.Tex0 = tc + texture_offset.xy;

    Out.LightDif = 0; //vAmbientColor;
    float totalLightPower = 0;

	//directional lights, compute diffuse color
    Out.LightDir_Alpha.xyz = mul(TBNMatrix, -vSunDir);
    Out.LightDif += vSunColor * vColor;
    totalLightPower += length(vSunColor.xyz);
	
    Out.LightDir_Alpha.a = vColor.a;

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
	
    if (use_depth_effects)
    {
        Out.projCoord.xy = (float2(Out.Pos.x, -Out.Pos.y) + Out.Pos.w) / 2;
        Out.projCoord.xy += (vDepthRT_HalfPixel_ViewportSizeInv.xy * Out.Pos.w);
        Out.projCoord.zw = Out.Pos.zw;
        Out.Depth = Out.Pos.z * far_clip_Inv;
    }

    return Out;
}
// Simple hash function to create pseudo-random values
float2 hash22(float2 p)
{
    float3 p3 = frac(float3(p.xyx) * 0.1031);
    p3 += dot(p3, p3.yzx + 33.33);
    return frac((p3.xx + p3.yz) * p3.zy);
}

// Noise function that uses the hash
float2 noise(float2 uv, float noiseScale)
{
    // Scale the input UVs and get the fractional part
    float2 p = frac(uv * noiseScale);
    // Get the integer part (the cell)
    float2 i = floor(uv * noiseScale);

    // Hash the corners of the cell
    float2 a = hash22(i);
    float2 b = hash22(i + float2(1.0, 0.0));
    float2 c = hash22(i + float2(0.0, 1.0));
    float2 d = hash22(i + float2(1.0, 1.0));

    // Bilinear interpolation to get the final value
    p = p * p * (3.0 - 2.0 * p); // Smootherstep
    float2 res = lerp(
        lerp(a, b, p.x),
        lerp(c, d, p.x),
        p.y
    );
    
    // Map from [0, 1] to [-1, 1]
    return res * 2.0 - 1.0;
}
float3 DesaturateColor(float3 color, float desaturationAmount)
{
    float luminance = dot(color, float3(0.299, 0.587, 0.114)); // Calculate luminance
    float3 grey = float3(luminance, luminance, luminance); // Grey color with the same luminance
    return lerp(color, grey, desaturationAmount); // Interpolate between color and grey
}

PS_OUTPUT ps_main_water(VS_OUTPUT_WATER In, uniform const bool use_high, uniform const bool apply_depth, uniform const bool mud_factor)
{
    PS_OUTPUT Output;
	
    const bool rgb_normalmap = false; //!apply_depth;
    float WaveScale1 = 0.5;
    float WaveScale2 = 1.75;
    float WaveScale3 = 8;
    float WaveOffset1 = 0;
    float WaveOffset2 = 64;
    //float WaveOffset3 = 0;
    float WaveStrength1 = 100; // Adjusted from 100 to 1
    float WaveStrength2 = 80; // Adjusted from 100 to 1

    float3 normal;
    float3 normalDistort;
    
    if (rgb_normalmap)
    {
        normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0).rgb - 1.0f);
    }
    else
    {
        float noiseScale = 1.25;
        float noiseStrenght = 0.1;
       // Using the noise function to perturb UVs
        float2 disturbedUV1 = In.Tex0 * WaveScale1 + WaveOffset1 + noise(In.Tex0, noiseScale) * noiseStrenght;
        float2 disturbedUV2 = In.Tex0 * WaveScale2 + WaveOffset2 + noise(In.Tex0, noiseScale) * noiseStrenght;
// You can use different noise strengths or even different noise textures for each UV set
// if you want a more complex or layered noise effect.

// Now sample the normal texture with the disturbed UVs
        float2 normal1GA = tex2D(NormalTextureSampler, disturbedUV1).ga * 2.0 - 1.0;
        float2 normal2GA = tex2D(NormalTextureSampler, disturbedUV2).ga * 2.0 - 1.0;
        //float2 normal3GA = tex2D(NormalTextureSampler, In.Tex0 * WaveScale3 + WaveOffset3).ga * 2.0 - 1.0;

// Reconstruct the Z component from the X and Y
        float normal1Z = sqrt(1.0f - clamp(dot(normal1GA, normal1GA), 0.0f, 1.0f));
        float normal2Z = sqrt(1.0f - clamp(dot(normal2GA, normal2GA), 0.0f, 1.0f));
        //float normal3Z = sqrt(1.0f - clamp(dot(normal3GA, normal3GA), 0.0f, 1.0f));

// Create the normal vectors using the X and Y from the texture, and the reconstructed Z
        float3 normal1 = pow(float3(normal1GA.y, normal1GA.x, normal1Z), 3);
        float3 normal2 = pow(float3(normal2GA.y, normal2GA.x, normal2Z), 3);
        //normalDistort = float3(normal3GA.y, normal3GA.x, normal3Z);
  
// Blend the normals
        normal = normalize(normal1 * WaveStrength1 + normal2 * WaveStrength2);
    }
	
    if (!apply_depth)
    {
        normal = float3(0, 0, 1);
    }
    
         // Foam Edge Calculations
    float depth = tex2Dproj(DepthTextureSampler, In.projCoord).r;
    float depthDiff = depth - In.Depth;
    float depthRange = 0.00062; // Depth range for transition
    float foamEdge = 1.0 - smoothstep(0.0, depthRange, depthDiff);
    float2 uv = In.Tex0; // Base texture coordinates

// Distortion parameters
    float noiseScale = 20; // Scale of the noise
    float secondNoiseScale = 20; // Scale of the noise
    float distortionScale = 1; // Scale of the distortion
    float distortionStrength = 0.025; // Strength of the distortion
    float foamSpeed = 0.1; // Speed of foam animation

// Sinusoidal movement parameters
    float sinSpeed = 0.5; // Speed of the sine movement
    float sinAmplitude = 1; // Amplitude of the sine movement
    float cosSpeed = 0.25; // Speed of the cosine movement
    float cosAmplitude = 1; // Amplitude of the cosine movement

// Calculate time-based offsets for sine and cosine
    float sinOffset = sin(time_var * sinSpeed) * sinAmplitude;
    float cosOffset = cos(time_var * cosSpeed) * cosAmplitude;

// Calculate distortion based on animated noise with sine and cosine offsets
    float2 timeOffsets = float2(sinOffset, cosOffset);
    float2 distortion = noise(uv * distortionScale + timeOffsets * foamSpeed, noiseScale) * distortionStrength;

// Apply the distortion to the UVs
    float2 distortedUV = uv + distortion;
    float2 noiseValue = noise(distortedUV, noiseScale);

    // Generate the secondary noise value
    float2 secondaryNoiseValue = noise(distortedUV * secondNoiseScale, noiseScale);
    
    float normalBlendIntencity = 0.15;
    // Combine with normals
    normal.x += (noiseValue * foamEdge) * normalBlendIntencity;
    normal.y += (secondaryNoiseValue * foamEdge) * normalBlendIntencity;
    
    // Blend the two noise values
    float blendFactor = 0.2; // Controls the influence of the second noise layer, adjust to taste
    float2 combinedNoiseValue = lerp(noiseValue, secondaryNoiseValue, blendFactor);
    
// Use the noise to modulate the foam edge
    float noiseStrength = 0.65; // How much the noise affects the foam
    foamEdge += noiseStrength * (combinedNoiseValue.x * 2.0 - 1.0) * foamEdge;

    
    float foamMultiplier = 6.75;
// Clamp foamEdge to [0, 1]
    foamEdge = clamp(foamEdge, 0.0, 1.0) * foamMultiplier;
	
    float NdotL = saturate(dot(normal, In.LightDir_Alpha.xyz)) * 0.5;
	//float NdotL = saturate(dot(detail_normal, In.LightDir));
	
	//float3 scaledNormal = normalize(normal * float3(0.2f, 0.2f, 1.0f));
	
    float3 vView = normalize(In.CameraDir);
		
    // Improved Fresnel effect with Schlick's approximation
    //float F0 = 0.02; // Base reflectivity at normal incidence
    //float fresnel = F0 + (1 - F0) * pow(1 - max(dot(vView, normal), 0), 5);
    
    // Calculate the Fresnel effect based on the view direction and normal
    float fresnelBias = 0.0462;
    float fresnelScale = 0.34;
    float fresnelPower = 3.2; // Controls the sharpness of the Fresnel effect
    float viewDotNormal = max(dot(normalize(vView), normalize(normal)), 0.0);
    float fresnel = fresnelBias + fresnelScale * pow(1.0 - viewDotNormal, fresnelPower);
    
    float4 tex;
    float3 viewDir = normalize(-In.CameraDir);
    float3 halfDir = normalize(viewDir + In.LightDir_Alpha.xyz);
    float fresnelFactor = pow(1.0 - max(dot(viewDir, normal), 0.0), 5.0);
    fresnelFactor *= fresnel; // Combining with your existing fresnel term

    //float causticsdepthRange = 0.005; // Depth range for transition
    //float causticsEdge = 1.0 - smoothstep(0, causticsdepthRange, depthDiff);
    //float causticsMask = Output.RGBColor.a * causticsEdge * 0.16;
    
    float2 skyUV = (normal.xy * (fresnelFactor * 3)) + float2(0.5f + 0.5f * (In.PosWater.x / In.PosWater.w), 0.5f - 0.5f * (In.PosWater.y / In.PosWater.w));
    if (apply_depth)
    {
        tex = tex2D(ReflectionTextureSampler, skyUV);
    }
    else
    {
		//for objects use env map (they use same texture register)
        tex = tex2D(EnvTextureSampler, (vView - normal).yx * 3.4f);
    }
	INPUT_OUTPUT_GAMMA(tex.rgb);
	
    Output.RGBColor = 0.001f * NdotL * In.LightDif;
    if (mud_factor)
    {
        Output.RGBColor *= 0.125f;
    }

    if (!apply_depth)
    {
        fresnel = min(fresnel, 0.01f);
    }
    else
    {
       // Define roughness - could also be sampled from a texture
        float roughness = 0.16f; // Vary this to simulate calmer or choppier water

        // Combine the reflection color with the Fresnel term, considering the roughness
        float3 reflectedColor = tex.rgb * fresnel;

        // Apply the roughness factor to the reflection (simulating blurriness in the reflection)
        float3 blurredReflection = lerp(reflectedColor, Output.RGBColor.rgb, roughness);

    // Add the blurred reflection to the output color
        Output.RGBColor.rgb += blurredReflection;
    }
    Output.RGBColor.a = 1.0f - 0.3f * In.CameraDir.z;
	
    float vertex_alpha = In.LightDir_Alpha.a;
    Output.RGBColor.a *= vertex_alpha;
	
    //if (mud_factor)
    //{
    //    Output.RGBColor.a = 1.0f;
    //}
    
	//static float3 g_cDownWaterColor = {12.0f/255.0f, 26.0f/255.0f, 36.0f/255.0f};
	//static float3 g_cUpWaterColor   = {33.0f/255.0f, 52.0f/255.0f, 77.0f/255.0f};
 
    // Define water colors with more green for muddy water
    const float3 g_cDownWaterColor = mud_factor ? float3(4.5f / 255.0f, 12.0f / 255.0f, 5.0f / 255.0f) : float3(1.0f / 255.0f, 10.0f / 255.0f, 5.0f / 255.0f);
    const float3 g_cUpWaterColor = mud_factor ? float3(5.0f / 255.0f, 14.0f / 255.0f, 5.0f / 255.0f) : float3(1.0f / 255.0f, 12.0f / 255.0f, 5.0f / 255.0f);

    // Define deep blue water colors
    const float3 g_cDownWaterColorBlue = float3(0.0f / 255.0f, 20.0f / 255.0f, 100.0f / 255.0f);
    const float3 g_cUpWaterColorBlue = float3(0.0f / 255.0f, 45.0f / 255.0f, 150.0f / 255.0f);
    
    float3 cWaterColor = lerp(g_cUpWaterColor, g_cDownWaterColor, saturate(dot(vView, normal)));
    float3 cWaterColorBlue = lerp(g_cUpWaterColorBlue, g_cDownWaterColorBlue, saturate(dot(vView, normal)));

    cWaterColor = lerp(cWaterColor, cWaterColorBlue, 0.075);
    if (!apply_depth)
    {
        cWaterColor = In.LightDif.xyz; // This could be modified if you want to affect the color when depth is not applied
    }

    float fog_fresnel_factor = saturate(dot(In.CameraDir, normal));
    //fog_fresnel_factor *= fog_fresnel_factor * fog_fresnel_factor; // Exponential increase for the fresnel factor

    if (!apply_depth)
    {
        fog_fresnel_factor *= 0.1f;
        fog_fresnel_factor += 0.05f;
    }
    float light_amount = (0.1f + NdotL) * 0.6f;
    
// Calculate the luminance using the Rec. 709 luminance formula
    float luminance = dot(cWaterColor, float3(0.2126, 0.7152, 0.0722));
// Create the grey color with the same luminance
    float3 grey = float3(luminance, luminance, luminance);
    
    Output.RGBColor.rgb *= DesaturateColor(lerp(tex.rgb * float3(0.105, 0.175, 0.160) * fresnel, tex.rgb, fresnel), 0.5);
    //Output.RGBColor.rgb += lerp(tex.rgb * float3(0.105, 0.175, 0.160) * fresnel, tex.rgb, fresnel) * 0.2;
    Output.RGBColor.rgb += (foamEdge * grey) * fog_fresnel_factor;
    Output.RGBColor.rgb += ((cWaterColor + cWaterColor) * light_amount) * fog_fresnel_factor;

// Adjust additional muddy color influence based on the view angle
    //if (mud_factor)
    //{
    //    Output.RGBColor.rgb += float3(0.022f, 0.03f, 0.005f) * (1.0f - saturate(dot(vView, normal))); // Increase green influence
    //}
	
    if (apply_depth && use_depth_effects)
    {
        float depth = tex2Dproj(DepthTextureSampler, In.projCoord).r;
	
        float alpha_factor;
        // Calculate the depth-based alpha factor with a smooth transition
        float depthDiff = depth - In.Depth;
        float depthRange = 0.028; // Adjust as needed to control the depth range for transition
        alpha_factor = 1.0 - smoothstep(0.0, depthRange, depthDiff);

        // Apply Fresnel effect to the alpha factor
        alpha_factor *= 1 - fresnel;
		
        Output.RGBColor.w *= alpha_factor;
		
		// Add additional alpha based on depth for underwater fog effect
        float fogFactor = 64; // Control how quickly the fog density increases with depth
        Output.RGBColor.w += saturate(depthDiff * fogFactor);
		
        static const bool use_refraction = true;
        
        if (use_refraction && use_high)
        {
            float refractionFactor = lerp(0, 1, fresnel);
            
            float4 coord_start = In.projCoord; //float2(0.5f + 0.5f * (In.PosWater.x / In.PosWater.w), 0.45 + 0.5f * (In.PosWater.y / In.PosWater.w));
            float4 coord_disto = coord_start;
            float2 distortion = (normal.xy * saturate(Output.RGBColor.w) * 30.185f);
            coord_disto.xy += distortion * refractionFactor;
            
            float depth_here = tex2D(DepthTextureSampler, coord_disto).r;
            float4 refraction;
            if (depth_here < depth)
                refraction = tex2Dproj(ScreenTextureSampler, coord_disto);
            else
                refraction = tex2Dproj(ScreenTextureSampler, coord_start);
			INPUT_OUTPUT_GAMMA(refraction.rgb);
            float3 surfaceMuddyColor = float3(0.8, 1.0, 0.6); // Soft brownish-green
            float3 deepMuddyColor = float3(0.6, 0.4, 0.2); // Darker brown
            float3 colorTint = lerp(surfaceMuddyColor, deepMuddyColor, In.Depth);

            // Apply the tint to the refracted color
            Output.RGBColor.rgb = lerp(Output.RGBColor.rgb, refraction.rgb * colorTint, saturate(1.0f - Output.RGBColor.w));
            
            if (Output.RGBColor.a > 0.1f)
            {
                Output.RGBColor.a *= 1.75f;
            }
            if (mud_factor)
            {
                Output.RGBColor.a *= 1.25f;
            }
            
        }
    }

       
    float edgeAlphaRange = 0.0002; // Depth range for transition
    float edgeALpha = 1.0 - smoothstep(0.0, edgeAlphaRange, depthDiff);
    edgeALpha = 1 - clamp(edgeALpha, 0, 1);
    
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    Output.RGBColor.a = saturate(Output.RGBColor.a) * edgeALpha;
    if (!apply_depth)
    {
        Output.RGBColor.a = 1.0f;
    }
    
    float3 cc = Output.RGBColor.rgb * (fresnel * 2) + (Output.RGBColor.rgb);
    Output.RGBColor.rgb = lerp(cc, Output.RGBColor.rgb, 0.75);
    
    // debug normals
    //Output.RGBColor.rgb = 0.5 * normal + 0.5; // This will visualize the normals
    //Output.RGBColor.a = 1.0f; // Opaque
    return Output;
}
technique watermap
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_water(false);
        PixelShader = compile PS_2_X ps_main_water(true, true, false);
    }
}
technique watermap_high
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_water(true);
        PixelShader = compile PS_2_X ps_main_water(true, true, false);
    }
}
technique watermap_mud
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_water(true);
        PixelShader = compile PS_2_X ps_main_water(false, true, true);
    }
}
technique watermap_mud_high
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_water(true);
        PixelShader = compile PS_2_X ps_main_water(true, true, true);
    }
}
/*technique watermap_for_objects
{
	pass P0
	{
		VertexShader = compile vs_2_0 vs_main_water();
		PixelShader = compile PS_2_X ps_main_water(true, false);
	}
}*/

#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef SKYBOX_SHADERS
PS_OUTPUT ps_skybox_shading(VS_OUTPUT_FONT In)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
    Output.RGBColor *= tex2D(MeshTextureSampler, In.Tex0);
	
    return Output;
}

PS_OUTPUT ps_skybox_shading_new(uniform bool use_hdr, VS_OUTPUT_FONT In)
{
    PS_OUTPUT Output;
	
    if (use_hdr)
    {
		
        Output.RGBColor = In.Color;
        Output.RGBColor *= tex2D(Diffuse2Sampler, In.Tex0);
		
		// expand to floating point.. (RGBE)
        float2 scaleBias = float2(vSpecularColor.x, vSpecularColor.y);
		
		//float exFactor16 = dot(tex2D(MeshTextureSampler, In.Tex0).rgb, 0.25);	//fake.
        float exFactor16 = tex2D(EnvTextureSampler, In.Tex0).r;
        float exFactor8 = floor(exFactor16 * 255) / 255;
        Output.RGBColor.rgb *= exp2(exFactor16 * scaleBias.x + scaleBias.y);
		
		//Output.RGBColor.rgb = tex2D(EnvTextureSampler, In.Tex0);
		
    }
    else
    {
		//switch to old style
        Output.RGBColor = In.Color;
        float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
		INPUT_TEX_GAMMA(tex_col.rgb);
        Output.RGBColor *= tex_col;
    }
	
    Output.RGBColor.a = 1;
	
	//gamma correct?
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    if (In.Color.a == 0.0f)
    {
        Output.RGBColor.rgb = saturate(Output.RGBColor.rgb);
    }
	
    return Output;
}

VS_OUTPUT_FONT vs_skybox(float4 vPosition : POSITION, float4 vColor : COLOR, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_FONT Out;

    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Pos.z = Out.Pos.w;

    float3 P = vPosition; //position in view space

    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;

	//apply fog
    P.z *= 0.2f;
    float d = length(P);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
	
    Out.Color.a = (vWorldPos.z < -10.0f) ? 0.0f : 1.0f;
	
    return Out;
}

VertexShader vs_skybox_compiled = compile vs_2_0 vs_skybox();

technique skybox
{
    pass P0
    {
        VertexShader = vs_skybox_compiled;
        PixelShader = compile PS_2_X ps_skybox_shading();
    }
}

technique skybox_new
{
    pass P0
    {
        VertexShader = vs_skybox_compiled;
        PixelShader = compile PS_2_X ps_skybox_shading_new(false);
    }
}

technique skybox_new_HDR
{
    pass P0
    {
        VertexShader = vs_skybox_compiled;
        PixelShader = compile PS_2_X ps_skybox_shading_new(true);
    }
}
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef STANDART_RELATED_SHADER //these are going to be same with standart!

struct VS_OUTPUT
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
};

VS_OUTPUT vs_main(uniform const int PcfMode, uniform const bool UseSecondLight, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space


    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);

    if (UseSecondLight)
    {
        diffuse_light += vLightColor;
    }

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
    float wNdotSun = saturate(dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}

VS_OUTPUT vs_main_Instanced(uniform const int PcfMode, uniform const bool UseSecondLight, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1,
							 //instance data:
						   float3 vInstanceData0 : TEXCOORD1,
						   float3 vInstanceData1 : TEXCOORD2,
						   float3 vInstanceData2 : TEXCOORD3,
						   float3 vInstanceData3 : TEXCOORD4)
{
	INITIALIZE_OUTPUT(VS_OUTPUT, Out);

    float4x4 matWorldOfInstance = build_instance_frame_matrix(vInstanceData0, vInstanceData1, vInstanceData2, vInstanceData3);
	
	//-- Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Pos = mul(matWorldOfInstance, float4(vPosition.xyz, 1.0f));
    Out.Pos = mul(matViewProj, Out.Pos);

    float4 vWorldPos = (float4) mul(matWorldOfInstance, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorldOfInstance, vNormal)); //normal in world space

    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);

    if (UseSecondLight)
    {
        diffuse_light += vLightColor;
    }

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
    float wNdotSun = saturate(dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float4 P = mul(matView, vWorldPos); //position in view space
    float d = length(P.xyz);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}


PS_OUTPUT ps_main(VS_OUTPUT In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);
	
    float sun_amount = 1.0f;
    if ((PcfMode != PCF_NONE))
    {
        sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }
    Output.RGBColor = tex_col * ((In.Color + In.SunLight * sun_amount));
	
	// gamma correct
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    return Output;
}

VertexShader vs_main_compiled_PCF_NONE_true = compile vs_2_0 vs_main(PCF_NONE, true);
VertexShader vs_main_compiled_PCF_DEFAULT_true = compile vs_2_0 vs_main(PCF_DEFAULT, true);
VertexShader vs_main_compiled_PCF_NVIDIA_true = compile vs_2_a vs_main(PCF_NVIDIA, true);

VertexShader vs_main_compiled_PCF_NONE_false = compile vs_2_0 vs_main(PCF_NONE, false);
VertexShader vs_main_compiled_PCF_DEFAULT_false = compile vs_2_0 vs_main(PCF_DEFAULT, false);
VertexShader vs_main_compiled_PCF_NVIDIA_false = compile vs_2_a vs_main(PCF_NVIDIA, false);

PixelShader ps_main_compiled_PCF_NONE = compile PS_2_X ps_main(PCF_NONE);
PixelShader ps_main_compiled_PCF_DEFAULT = compile PS_2_X ps_main(PCF_DEFAULT);
PixelShader ps_main_compiled_PCF_NVIDIA = compile ps_2_a ps_main(PCF_NVIDIA);


technique diffuse
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_NONE_true;
        PixelShader = ps_main_compiled_PCF_NONE;
    }
}
technique diffuse_SHDW
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_DEFAULT_true;
        PixelShader = ps_main_compiled_PCF_DEFAULT;
    }
}
technique diffuse_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_NVIDIA_true;
        PixelShader = ps_main_compiled_PCF_NVIDIA;
    }
}
DEFINE_LIGHTING_TECHNIQUE(diffuse, 0, 0, 0, 0, 0)    

technique diffuse_dynamic
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_NONE_false;
        PixelShader = ps_main_compiled_PCF_NONE;
    }
}
technique diffuse_dynamic_SHDW
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_DEFAULT_false;
        PixelShader = ps_main_compiled_PCF_DEFAULT;
    }
}
technique diffuse_dynamic_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_NVIDIA_false;
        PixelShader = ps_main_compiled_PCF_NVIDIA;
    }
}
DEFINE_LIGHTING_TECHNIQUE(diffuse_dynamic, 0, 0, 0, 0, 0)    


technique diffuse_dynamic_Instanced
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_Instanced(PCF_NONE, false);
        PixelShader = ps_main_compiled_PCF_NONE;
    }
}

technique diffuse_dynamic_Instanced_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_Instanced(PCF_DEFAULT, false);
        PixelShader = ps_main_compiled_PCF_DEFAULT;
    }
}

technique diffuse_dynamic_Instanced_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_Instanced(PCF_NVIDIA, false);
        PixelShader = ps_main_compiled_PCF_NVIDIA;
    }
}

technique envmap_metal
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_NONE_true;
        PixelShader = ps_main_compiled_PCF_NONE;
    }
}
technique envmap_metal_SHDW
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_DEFAULT_true;
        PixelShader = ps_main_compiled_PCF_DEFAULT;
    }
}
technique envmap_metal_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_compiled_PCF_NVIDIA_true;
        PixelShader = ps_main_compiled_PCF_NVIDIA;
    }
}
DEFINE_LIGHTING_TECHNIQUE(envmap_metal, 0, 0, 0, 0, 0)    

//-----
float3 calculate_wind_effect(int wind_type, float height, float3 position, float3 wPosition, float max_height)
{
    // Branches and Leaves
    if (wind_type == 1)
    {
        float leafWindStrength = 0.025; // Adjust for branches/leaves
        float leafWindSpeed = fWindPower*5; // Speed for branches/leaves

        // Swaying effect for branches and leaves
        float swayAngle = -sin(time_var * leafWindSpeed + wPosition.x) * leafWindStrength;
        float3x3 swayRotationMatrix = float3x3(cos(swayAngle), 0, sin(swayAngle),
                                               0, 1, 0,
                                               -sin(swayAngle), 0, cos(swayAngle));

        position = mul(swayRotationMatrix, position);

        //// Additional random movement for fluttering effect
        //position.xz += sin(time_var * leafWindSpeed  + wPosition.xz) * leafWindStrength;
        
         // Adding variability to leaf motion based on position
        float variability = noise(position.xy,5); // Replace with an appropriate noise function
        position.xz += sin(time_var * leafWindSpeed + wPosition.xy + variability) * leafWindStrength;
        
         // The pivot is at the top of the tree
        float3 pivot = float3(0, max_height, 0);
        position -= pivot;
        position = mul(swayRotationMatrix, position);
        position += pivot;
    }
    // Trunk
    else if (wind_type == 2)
    {
        float windStrength = 0.025; // Control the strength of the wind
        float windSpeed = fWindPower*5; // Control the speed of the wind

        // Calculate the bending angle based on height
        float angle = sin(time_var * windSpeed + wPosition.x) * windStrength * (1.0 - (height / max_height));

        // Create a rotation matrix around the Y-axis
        float3x3 rotationMatrix = float3x3(cos(angle), 0, sin(angle),
                                           0, 1, 0,
                                           -sin(angle), 0, cos(angle));

        // The pivot is at the top of the tree
        float3 pivot = float3(0, max_height, 0);
        position -= pivot;
        position = mul(rotationMatrix, position);
        position += pivot;
    }

    return position;
}


struct VS_OUTPUT_BUMP
{
    float4 Pos : POSITION;
    float4 VertexColor : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float3 SunLightDir : TEXCOORD1; //sun light dir in pixel coordinates
    float3 SkyLightDir : TEXCOORD2; //light diffuse for bump
    float4 PointLightDir : TEXCOORD3; //light ambient for bump
    float4 ShadowTexCoord : TEXCOORD4;
    float2 ShadowTexelPos : TEXCOORD5;
    float Fog : FOG;
	
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};
VS_OUTPUT_BUMP vs_main_bump(uniform const int PcfMode, uniform const bool is_windy_trunk, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL, float4 vVertexColor : COLOR0, float4 vPointLightDir : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_BUMP, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    
    //if (is_windy_trunk)
    //{
    //    float height = vPosition.y; // Assuming y is up, adjust if different
    //    float maxTreeHeight = height * 20.0; // Replace with your actual tree height
    //    float3 new_position = calculate_wind_effect(2, height, vPosition.xyz, vWorldPos.xyz,maxTreeHeight);
    //    Out.Pos = mul(matWorldViewProj, lerp(float4(new_position, 1.0), vPosition,0.8));
    //}
    //else
    //{
        Out.Pos = mul(matWorldViewProj, vPosition);
    //}

    
    Out.Tex0 = tc;
    
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }

    Out.SunLightDir = mul(TBNMatrix, -vSunDir);
    Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
	
#ifdef USE_LIGHTING_PASS
	Out.PointLightDir = vWorldPos;
#else
    Out.PointLightDir.rgb = 2.0f * vPointLightDir.rgb - 1.0f;
    Out.PointLightDir.a = vPointLightDir.a;
#endif
	
    Out.VertexColor = vVertexColor;
	
	//STR: note that these are not in TBN space.. (used for fresnel only..)
    Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz); //normalize(mul(TBNMatrix, (vCameraPos.xyz - vWorldPos.xyz) ));	// 
	//Out.ViewDir = mul(TBNMatrix, Out.ViewDir);

    Out.WorldNormal = vWorldN;
	//Out.WorldNormal = mul(TBNMatrix, Out.WorldNormal);

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

PS_OUTPUT ps_main_bump(VS_OUTPUT_BUMP In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 total_light = vAmbientColor; //In.LightAmbient;
	
    float3 normal;
    normal.xy = (2.0f * tex2D(NormalTextureSampler, In.Tex0).ag - 1.0f);
    normal.z = sqrt(1.0f - dot(normal.xy, normal.xy));
	
	/*
	const bool use_detail_normalmap = debug_vector.z > 1.0f;
	if(use_detail_normalmap)
	{
		float3 detail_normal = tex2D(Diffuse2Sampler, In.Tex0*debug_vector.y).rgb;
		//normal = lerp(normal, detail_normal, debug_vector.z);
		//normal = normalize(normal);
		
		float3x3 normal_frame; 
		normal_frame[2] = normal;
		normal_frame[1] = float3(0,1,0);
		normal_frame[0] = cross(normal_frame[1], normal_frame[2]);
		//normal_frame[0] = normalize(normal_frame[0]);
		normal_frame[1] = cross(normal_frame[2], normal_frame[0]);
		
		normal = mul(detail_normal, normal_frame);
	}
	*/

    if (PcfMode != PCF_NONE)
    {
        float sun_amount = 0.03f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        total_light += ((saturate(dot(In.SunLightDir.xyz, normal.xyz)) * (sun_amount))) * vSunColor;
    }
    else
    {
        total_light += saturate(dot(In.SunLightDir.xyz, normal.xyz)) * vSunColor;
    }
    total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
	
#ifndef USE_LIGHTING_PASS
    total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz)) * vPointLightColor;
#endif

    Output.RGBColor.rgb = total_light.rgb;
    Output.RGBColor.a = 1.0f;
    Output.RGBColor *= vMaterialColor;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
	
	//	Output.RGBColor = saturate(Output.RGBColor);
	OUTPUT_GAMMA(Output.RGBColor.rgb);

    return Output;
}
PS_OUTPUT ps_main_bump_simple(VS_OUTPUT_BUMP In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 total_light = vAmbientColor; //In.LightAmbient;
/*-	//Parallax mapping:
	//float viewVec_len = length(In.ViewDir);
	//float3 viewVec = In.ViewDir / viewVec_len;
	float3 viewVec = normalize(In.ViewDir);
	{
		float2 plxCoeffs = float2(0.04, -0.02) * debug_vector.w;
		float height = tex2D(NormalTextureSampler, In.Tex0).a;
		float offset = height * plxCoeffs.x + plxCoeffs.y;
		In.Tex0 = In.Tex0 + offset * viewVec.xy;
	}
*/
	
    float3 normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0).rgb - 1.0f);

    float sun_amount = 1.0f;
    if (PcfMode != PCF_NONE)
    {
        if (PcfMode == PCF_NVIDIA)
            sun_amount = saturate(0.15f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos));
        else
            sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos); //cannot fit 64 instruction
    }
    total_light += ((saturate(dot(In.SunLightDir.xyz, normal.xyz)) * (sun_amount * sun_amount))) * vSunColor;
	
    total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
#ifndef USE_LIGHTING_PASS
    total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz)) * vPointLightColor;
#endif

    Output.RGBColor.rgb = total_light.rgb;
    Output.RGBColor.a = 1.0f;
    Output.RGBColor *= vMaterialColor;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
	
	//	Output.RGBColor = saturate(Output.RGBColor);
	
	
    float fresnel = 1 - (saturate(dot(In.ViewDir, In.WorldNormal)));
	//-float fresnel = 1-(saturate(dot( viewVec, In.WorldNormal)));

	// Output.RGBColor.rgb *= fresnel; 
    Output.RGBColor.rgb *= max(0.6, fresnel * fresnel + 0.1);
	
    Output.RGBColor.rgb = OUTPUT_GAMMA(Output.RGBColor.rgb);


    return Output;
}
PS_OUTPUT ps_main_bump_simple_multitex(VS_OUTPUT_BUMP In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 total_light = vAmbientColor; //In.LightAmbient;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 tex_col2 = tex2D(Diffuse2Sampler, In.Tex0 * uv_2_scale);
	
    float4 multi_tex_col = tex_col;
    float inv_alpha = (1.0f - In.VertexColor.a);
    multi_tex_col.rgb *= inv_alpha;
    multi_tex_col.rgb += tex_col2.rgb * In.VertexColor.a;
	
	//!!
	INPUT_TEX_GAMMA(multi_tex_col.rgb);

    float3 normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0).rgb - 1.0f);

    float sun_amount = 1.0f;
    if (PcfMode != PCF_NONE)
    {
        if (PcfMode == PCF_NVIDIA)
            sun_amount = saturate(0.15f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos));
        else
            sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos); //cannot fit 64 instruction
    }
    total_light += (saturate(dot(In.SunLightDir.xyz, normal.xyz)) * (sun_amount)) * vSunColor;
	
    total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
#ifndef USE_LIGHTING_PASS
    total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz)) * vPointLightColor;
#endif

    Output.RGBColor.rgb = total_light.rgb;
    Output.RGBColor.a = 1.0f;
	//	Output.RGBColor *= vMaterialColor;
	

	
    Output.RGBColor *= multi_tex_col;
    Output.RGBColor.rgb *= In.VertexColor.rgb;
    Output.RGBColor.a *= In.PointLightDir.a;
	
	
    float fresnel = 1 - (saturate(dot(normalize(In.ViewDir), normalize(In.WorldNormal))));
	// Output.RGBColor.rgb *= fresnel; 
    Output.RGBColor.rgb *= max(0.6, fresnel * fresnel + 0.1);
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    return Output;
}

VertexShader vs_main_bump_compiled_PCF_NONE = compile vs_2_0 vs_main_bump(PCF_NONE, false);
VertexShader vs_main_bump_compiled_PCF_DEFAULT = compile vs_2_0 vs_main_bump(PCF_DEFAULT, false);
VertexShader vs_main_bump_compiled_PCF_NVIDIA = compile vs_2_a vs_main_bump(PCF_NVIDIA, false);


technique bumpmap
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_NONE;
        PixelShader = compile PS_2_X ps_main_bump(PCF_NONE);
    }
}
technique bumpmap_SHDW
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_DEFAULT;
        PixelShader = compile PS_2_X ps_main_bump(PCF_DEFAULT);
    }
}
technique bumpmap_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_NVIDIA;
        PixelShader = compile ps_2_a ps_main_bump(PCF_NVIDIA);
    }
}

VertexShader vs_main_bump_compiled_wind_PCF_NONE = compile vs_2_0 vs_main_bump(PCF_NONE, true);
VertexShader vs_main_bump_compiled_wind_PCF_DEFAULT = compile vs_2_0 vs_main_bump(PCF_DEFAULT, true);
VertexShader vs_main_bump_compiled_wind_PCF_NVIDIA = compile vs_2_a vs_main_bump(PCF_NVIDIA, true);


technique bumpmap_wind
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_wind_PCF_NONE;
        PixelShader = compile PS_2_X ps_main_bump(PCF_NONE);
    }
}
technique bumpmap_wind_SHDW
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_wind_PCF_DEFAULT;
        PixelShader = compile PS_2_X ps_main_bump(PCF_DEFAULT);
    }
}
technique bumpmap_wind_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_wind_PCF_NVIDIA;
        PixelShader = compile ps_2_a ps_main_bump(PCF_NVIDIA);
    }
}

DEFINE_LIGHTING_TECHNIQUE(bumpmap, 1, 1, 0, 0, 0)    

//-----
technique dot3
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_NONE;
        PixelShader = compile PS_2_X ps_main_bump_simple(PCF_NONE);
    }
}
technique dot3_SHDW
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_DEFAULT;
        PixelShader = compile PS_2_X ps_main_bump_simple(PCF_DEFAULT);
    }
}
technique dot3_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_NVIDIA;
        PixelShader = compile ps_2_a ps_main_bump_simple(PCF_NVIDIA);
    }
}
DEFINE_LIGHTING_TECHNIQUE(dot3, 0, 1, 0, 0, 0)    
//-----
technique dot3_multitex
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_NONE;
        PixelShader = compile PS_2_X ps_main_bump_simple_multitex(PCF_NONE);
    }
}
technique dot3_multitex_SHDW
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_DEFAULT;
        PixelShader = compile PS_2_X ps_main_bump_simple_multitex(PCF_DEFAULT);
    }
}
technique dot3_multitex_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_bump_compiled_PCF_NVIDIA;
        PixelShader = compile ps_2_a ps_main_bump_simple_multitex(PCF_NVIDIA);
    }
}
DEFINE_LIGHTING_TECHNIQUE(dot3_multitex, 0, 1, 0, 0, 0)    
//---
struct VS_OUTPUT_ENVMAP_SPECULAR
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float4 Color : COLOR0;
    float4 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
    float3 vSpecular : TEXCOORD4;
};
VS_OUTPUT_ENVMAP_SPECULAR vs_envmap_specular(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_ENVMAP_SPECULAR, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
	
    if (bUseMotionBlur)	//motion blur flag!?!
    {
        float4 vWorldPos1 = mul(matMotionBlur, vPosition);
        float3 delta_vector = vWorldPos1 - vWorldPos;
        float maxMoveLength = length(delta_vector);
        float3 moveDirection = delta_vector / maxMoveLength; //normalize(delta_vector);
		
        if (maxMoveLength > 0.25f)
        {
            maxMoveLength = 0.25f;
            vWorldPos1.xyz = vWorldPos.xyz + delta_vector * maxMoveLength;
        }
		
        float delta_coefficient_sharp = (dot(vWorldN, moveDirection) > 0.12f) ? 1 : 0;

        float y_factor = saturate(vPosition.y + 0.15);
        vWorldPos = lerp(vWorldPos, vWorldPos1, delta_coefficient_sharp * y_factor);

        float delta_coefficient_smooth = saturate(dot(vWorldN, moveDirection) + 0.5f);

        float extra_alpha = 0.1f;
        float start_alpha = (1.0f + extra_alpha);
        float end_alpha = start_alpha - 1.8f;
        float alpha = saturate(lerp(start_alpha, end_alpha, delta_coefficient_smooth));
        vColor.a = saturate(0.5f - vPosition.y) + alpha + 0.25;
		
        Out.Pos = mul(matViewProj, vWorldPos);
    }
    else
    {
        Out.Pos = mul(matWorldViewProj, vPosition);
    }

    Out.Tex0.xy = tc;

    float3 relative_cam_pos = normalize(vCameraPos - vWorldPos);
    float2 envpos;
    float3 tempvec = relative_cam_pos - vWorldN;
    float3 vHalf = normalize(relative_cam_pos - vSunDir);
    float3 fSpecular = spec_coef * vSunColor * vSpecularColor * pow(saturate(dot(vHalf, vWorldN)), fMaterialPower);
    Out.vSpecular = fSpecular;
    Out.vSpecular *= vColor.rgb;

    envpos.x = (tempvec.y); // + tempvec.x);
    envpos.y = tempvec.z;
    envpos += 1.0f;
	//   envpos *= 0.5f;

    Out.Tex0.zw = envpos;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);


	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);
	//shadow mapping variables
    float wNdotSun = max(-0.0001f, dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    Out.SunLight.a = vColor.a;

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}


VS_OUTPUT_ENVMAP_SPECULAR vs_envmap_specular_Instanced(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL,
														float2 tc : TEXCOORD0, float4 vColor : COLOR0,
														 //instance data:
													   float3 vInstanceData0 : TEXCOORD1, float3 vInstanceData1 : TEXCOORD2,
													   float3 vInstanceData2 : TEXCOORD3, float3 vInstanceData3 : TEXCOORD4)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_ENVMAP_SPECULAR, Out);

    float4x4 matWorldOfInstance = build_instance_frame_matrix(vInstanceData0, vInstanceData1, vInstanceData2, vInstanceData3);

    float4 vWorldPos = mul(matWorldOfInstance, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorldOfInstance, vNormal));
	
	
    if (bUseMotionBlur)	//motion blur flag!?!
    {
        float4 vWorldPos1;
        float3 moveDirection;
        if (true)	//instanced meshes dont have valid matMotionBlur!
        {
            const float blur_len = 0.2f;
            moveDirection = -normalize(float3(matWorldOfInstance[0][0], matWorldOfInstance[1][0], matWorldOfInstance[2][0])); //using x axis !
            moveDirection.y -= blur_len * 0.285; //low down blur for big blur_lens (show more like a spline)
            vWorldPos1 = vWorldPos + float4(moveDirection, 0) * blur_len;
        }
        else
        {
            vWorldPos1 = mul(matMotionBlur, vPosition);
            moveDirection = normalize(vWorldPos1 - vWorldPos);
        }
		
		   
        float delta_coefficient_sharp = (dot(vWorldN, moveDirection) > 0.12f) ? 1 : 0;

        float y_factor = saturate(vPosition.y + 0.15);
        vWorldPos = lerp(vWorldPos, vWorldPos1, delta_coefficient_sharp * y_factor);

        float delta_coefficient_smooth = saturate(dot(vWorldN, moveDirection) + 0.5f);

        float extra_alpha = 0.1f;
        float start_alpha = (1.0f + extra_alpha);
        float end_alpha = start_alpha - 1.8f;
        float alpha = saturate(lerp(start_alpha, end_alpha, delta_coefficient_smooth));
        vColor.a = saturate(0.5f - vPosition.y) + alpha + 0.25;
    }
	
    Out.Pos = mul(matViewProj, vWorldPos);

    Out.Tex0.xy = tc;

    float3 relative_cam_pos = normalize(vCameraPos - vWorldPos);
    float2 envpos;
	
    float3 tempvec = relative_cam_pos - vWorldN;
    float3 vHalf = normalize(relative_cam_pos - vSunDir);
    float3 fSpecular = spec_coef * vSunColor * vSpecularColor * pow(saturate(dot(vHalf, vWorldN)), fMaterialPower);
    Out.vSpecular = fSpecular;
    Out.vSpecular *= vColor.rgb;

    envpos.x = (tempvec.y); // + tempvec.x);
    envpos.y = tempvec.z;
    envpos += 1.0f;
	//   envpos *= 0.5f;

    Out.Tex0.zw = envpos;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);


	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);
	//shadow mapping variables
    float wNdotSun = max(-0.0001f, dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    Out.SunLight.a = vColor.a;

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float3 P = mul(matView, vWorldPos); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

PS_OUTPUT ps_envmap_specular(VS_OUTPUT_ENVMAP_SPECULAR In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
	// Compute half vector for specular lighting
	//   float3 vHalf = normalize(normalize(-ViewPos) + normalize(g_vLight - ViewPos));
    float4 texColor = tex2D(MeshTextureSampler, In.Tex0.xy);
	INPUT_TEX_GAMMA(texColor.rgb);
	
    float3 specTexture = tex2D(SpecularTextureSampler, In.Tex0.xy).rgb;
    float3 fSpecular = specTexture * In.vSpecular.rgb;
	
	//	float3 relative_cam_pos = normalize(vCameraPos - In.worldPos);
	//	float3 vHalf = normalize(relative_cam_pos - vSunDir);
	/*	
	float2 envpos;
	float3 tempvec =relative_cam_pos -  In.worldNormal ;
//	envpos.x = tempvec.x;
//	envpos.y = tempvec.z;
	envpos.xy = tempvec.xz;
	envpos += 1.0f;
	envpos *= 0.5f;
*/	
    float3 envColor = tex2D(EnvTextureSampler, In.Tex0.zw).rgb;
	
	// Compute normal dot half for specular light
	//	float4 fSpecular = 4.0f * specColor * vSpecularColor * pow( saturate( dot( vHalf, normalize( In.worldNormal) ) ), fMaterialPower);

	
    if ((PcfMode != PCF_NONE))
    {
		
        float sun_amount = 0.1f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        float4 vcol = In.Color;
        vcol.rgb += (In.SunLight.rgb + fSpecular) * sun_amount;
        Output.RGBColor = (texColor * vcol);
        Output.RGBColor.rgb += (In.SunLight * sun_amount + 0.3f) * (In.Color.rgb * envColor.rgb * specTexture);
    }
    else
    {
        float4 vcol = In.Color;
        vcol.rgb += (In.SunLight.rgb + fSpecular);
        Output.RGBColor = (texColor * vcol);
        Output.RGBColor.rgb += (In.SunLight + 0.3f) * (In.Color.rgb * envColor.rgb * specTexture);
    }

	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    Output.RGBColor.a = 1.0f;
	
    if (bUseMotionBlur)
        Output.RGBColor.a = In.SunLight.a;
		
    return Output;
}


PS_OUTPUT ps_envmap_specular_singlespec(VS_OUTPUT_ENVMAP_SPECULAR In, uniform const int PcfMode)	//only differs by black-white specular texture usage
{
    PS_OUTPUT Output;
	
	// Compute half vector for specular lighting
	
    float2 spectex_Col = tex2D(SpecularTextureSampler, In.Tex0.xy).ag;
    float specTexture = dot(spectex_Col, spectex_Col) * 0.5;
    float3 fSpecular = specTexture * In.vSpecular.rgb;
	
    float4 texColor = saturate((saturate(In.Color + 0.5f) * specTexture) * 2.0f + 0.25f);
	// INPUT_TEX_GAMMA(texColor.rgb);
	
	//	float3 relative_cam_pos = normalize(vCameraPos - In.worldPos);
	//	float3 vHalf = normalize(relative_cam_pos - vSunDir);
	/*	
	float2 envpos;
	float3 tempvec =relative_cam_pos -  In.worldNormal ;
//	envpos.x = tempvec.x;
//	envpos.y = tempvec.z;
	envpos.xy = tempvec.xz;
	envpos += 1.0f;
	envpos *= 0.5f;
*/	
    float3 envColor = tex2D(EnvTextureSampler, In.Tex0.zw).rgb;
	
	// Compute normal dot half for specular light
	//	float4 fSpecular = 4.0f * specColor * vSpecularColor * pow( saturate( dot( vHalf, normalize( In.worldNormal) ) ), fMaterialPower);

	
    if ((PcfMode != PCF_NONE))
    {
        float sun_amount = 0.1f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        float4 vcol = In.Color;
        vcol.rgb += (In.SunLight.rgb + fSpecular) * sun_amount;
        Output.RGBColor = (texColor * vcol);
        Output.RGBColor.rgb += (In.SunLight * sun_amount + 0.3f) * (In.Color.rgb * envColor.rgb * specTexture);
    }
    else
    {
        float4 vcol = In.Color;
        vcol.rgb += (In.SunLight.rgb + fSpecular);
        Output.RGBColor = (texColor * vcol);
        Output.RGBColor.rgb += (In.SunLight + 0.3f) * (In.Color.rgb * envColor.rgb * specTexture);
    }

	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    Output.RGBColor.a = 1.0f;
	/*
	if(bUseMotionBlur)
		Output.RGBColor.a = In.SunLight.a;
	*/
	
    return Output;
}

DEFINE_TECHNIQUES(envmap_specular_diffuse, vs_envmap_specular, ps_envmap_specular)
DEFINE_TECHNIQUES(envmap_specular_diffuse_Instanced, vs_envmap_specular_Instanced, ps_envmap_specular)
DEFINE_TECHNIQUES(watermap_for_objects, vs_envmap_specular, ps_envmap_specular_singlespec)

//---
struct VS_OUTPUT_BUMP_DYNAMIC
{
    float4 Pos : POSITION;
    float4 VertexColor : COLOR0;
    float2 Tex0 : TEXCOORD0;
#ifndef USE_LIGHTING_PASS
    float3 vec_to_light_0 : TEXCOORD1;
    float3 vec_to_light_1 : TEXCOORD2;
    float3 vec_to_light_2 : TEXCOORD3;
#endif
	//    float4 vec_to_light_3		: TEXCOORD4;
	//    float4 vec_to_light_4		: TEXCOORD5;
	//    float4 vec_to_light_5		: TEXCOORD6;
	//    float4 vec_to_light_6		: TEXCOORD7;
    float Fog : FOG;
};
VS_OUTPUT_BUMP_DYNAMIC vs_main_bump_interior(float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL, float4 vVertexColor : COLOR0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_BUMP_DYNAMIC, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Tex0 = tc;
   
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space


    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

#ifndef USE_LIGHTING_PASS
    float3 point_to_light = vLightPosDir[iLightIndices[0]] - vWorldPos.xyz;
    Out.vec_to_light_0.xyz = mul(TBNMatrix, point_to_light);
    point_to_light = vLightPosDir[iLightIndices[1]] - vWorldPos.xyz;
    Out.vec_to_light_1.xyz = mul(TBNMatrix, point_to_light);
    point_to_light = vLightPosDir[iLightIndices[2]] - vWorldPos.xyz;
    Out.vec_to_light_2.xyz = mul(TBNMatrix, point_to_light);
#endif
	
    Out.VertexColor = vVertexColor;

   //apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}
PS_OUTPUT ps_main_bump_interior(VS_OUTPUT_BUMP_DYNAMIC In)
{
    PS_OUTPUT Output;
    
    float4 total_light = vAmbientColor; //In.LightAmbient;
    

#ifndef USE_LIGHTING_PASS
    float3 normal;
    normal.xy = (2.0f * tex2D(NormalTextureSampler, In.Tex0).ag - 1.0f);
    normal.z = sqrt(1.0f - dot(normal.xy, normal.xy));
 
//	float3 abs_min_vec_to_light = float3(100000, 100000, 100000);
    
//	float LD = In.vec_to_light_0.w;
    float LD = dot(In.vec_to_light_0.xyz, In.vec_to_light_0.xyz);
    float3 L = normalize(In.vec_to_light_0.xyz);
    float wNdotL = dot(normal, L);
    total_light += saturate(wNdotL) * vLightDiffuse[iLightIndices[0]] / (LD);
	
//	LD = In.vec_to_light_1.w;
    LD = dot(In.vec_to_light_1.xyz, In.vec_to_light_1.xyz);
    L = normalize(In.vec_to_light_1.xyz);
    wNdotL = dot(normal, L);
    total_light += saturate(wNdotL) * vLightDiffuse[iLightIndices[1]] / (LD);

//	LD = In.vec_to_light_2.w;
    LD = dot(In.vec_to_light_2.xyz, In.vec_to_light_2.xyz);
    L = normalize(In.vec_to_light_2.xyz);
    wNdotL = dot(normal, L);
    total_light += saturate(wNdotL) * vLightDiffuse[iLightIndices[2]] / (LD);
#endif

//	Output.RGBColor = saturate(total_light * 0.6f) * 1.66f;
    Output.RGBColor = float4(total_light.rgb, 1.0);
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
	
//	Output.RGBColor = saturate(Output.RGBColor);
    Output.RGBColor.rgb = saturate(OUTPUT_GAMMA(Output.RGBColor.rgb));
    Output.RGBColor.a = In.VertexColor.a;

    return Output;
}

technique bumpmap_interior
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_bump_interior();
        PixelShader = compile PS_2_X ps_main_bump_interior();
    }
}

struct VS_OUTPUT_BUMP_DYNAMIC_NEW
{
    float4 Pos : POSITION;
    float4 VertexColor : COLOR0;
    float2 Tex0 : TEXCOORD0;
#ifndef USE_LIGHTING_PASS
    float3 vec_to_light_0 : TEXCOORD1;
    float3 vec_to_light_1 : TEXCOORD2;
    float3 vec_to_light_2 : TEXCOORD3;
#endif
    float3 ViewDir : TEXCOORD4;
	
    float Fog : FOG;
};


VS_OUTPUT_BUMP_DYNAMIC_NEW vs_main_bump_interior_new(float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL, float4 vVertexColor : COLOR0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_BUMP_DYNAMIC_NEW, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Tex0 = tc;

    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space


    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

#ifndef USE_LIGHTING_PASS
    float3 point_to_light = vLightPosDir[iLightIndices[0]] - vWorldPos.xyz;
    Out.vec_to_light_0.xyz = mul(TBNMatrix, point_to_light);
    point_to_light = vLightPosDir[iLightIndices[1]] - vWorldPos.xyz;
    Out.vec_to_light_1.xyz = mul(TBNMatrix, point_to_light);
    point_to_light = vLightPosDir[iLightIndices[2]] - vWorldPos.xyz;
    Out.vec_to_light_2.xyz = mul(TBNMatrix, point_to_light);
#endif
	
    Out.VertexColor = vVertexColor;
	
    float3 viewdir = normalize(vCameraPos.xyz - vWorldPos.xyz);
    Out.ViewDir = mul(TBNMatrix, viewdir);

	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}

//uses standart-style normal maps
PS_OUTPUT ps_main_bump_interior_new(VS_OUTPUT_BUMP_DYNAMIC_NEW In, uniform const bool use_specularmap) //ps_main_bump_interior with std normalmaps
{
    PS_OUTPUT Output;
	
    float4 total_light = vAmbientColor;

	// effective lights!?

#ifndef USE_LIGHTING_PASS
    float3 normal = 2.0f * tex2D(NormalTextureSampler, In.Tex0).rgb - 1.0f;
	
	
	//	float LD = In.vec_to_light_0.w;
    float LD_0 = saturate(1.0f / dot(In.vec_to_light_0.xyz, In.vec_to_light_0.xyz));
    float3 L_0 = normalize(In.vec_to_light_0.xyz);
    float wNdotL_0 = dot(normal, L_0);
    total_light += saturate(wNdotL_0) * vLightDiffuse[iLightIndices[0]] * (LD_0);

	//	LD = In.vec_to_light_1.w;
    float LD_1 = saturate(1.0f / dot(In.vec_to_light_1.xyz, In.vec_to_light_1.xyz));
    float3 L_1 = normalize(In.vec_to_light_1.xyz);
    float wNdotL_1 = dot(normal, L_1);
    total_light += saturate(wNdotL_1) * vLightDiffuse[iLightIndices[1]] * (LD_1);

	//	LD = In.vec_to_light_2.w;
    float LD_2 = saturate(1.0f / dot(In.vec_to_light_2.xyz, In.vec_to_light_2.xyz));
    float3 L_2 = normalize(In.vec_to_light_2.xyz);
    float wNdotL_2 = dot(normal, L_2);
    total_light += saturate(wNdotL_2) * vLightDiffuse[iLightIndices[2]] * (LD_2);
#endif
	
	//	Output.RGBColor = saturate(total_light * 0.6f) * 1.66f;
    Output.RGBColor = float4(total_light.rgb, 1.0);
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
	
    if (use_specularmap)
    {
        float4 fSpecular = 0;
		
		//light0 specular
        float4 light0_specColor = vLightDiffuse[iLightIndices[0]] * LD_0;
        float3 vHalf_0 = normalize(In.ViewDir + L_0);
        fSpecular = light0_specColor * pow(saturate(dot(vHalf_0, normal)), fMaterialPower);
		
		/* makes 65 instruction:
		//light1 specular
		float4 light1_specColor = vLightDiffuse[ iLightIndices[1] ] * LD_1;
		float3 vHalf_1 = normalize( In.ViewDir + L_1 );
		fSpecular += light1_specColor * pow( saturate(dot(vHalf_1, normal)), fMaterialPower);
		*/
		//light2 specular
		//float4 light2_specColor = vLightDiffuse[2] * LD_2;
		//float3 vHalf_2 = normalize( In.ViewDir + L_2 );
		//fSpecular += light2_specColor * pow( saturate(dot(vHalf_2, normal)), fMaterialPower);
		
        float4 specColor = 0.1 * spec_coef * vSpecularColor;
        float spec_tex_factor = dot(tex2D(SpecularTextureSampler, In.Tex0).rgb, 0.33); //get more precision from specularmap
        specColor *= spec_tex_factor;
		
        Output.RGBColor += specColor * fSpecular;
    }
	
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    Output.RGBColor = saturate(Output.RGBColor);
    Output.RGBColor.a = In.VertexColor.a;
	
    return Output;
}

technique bumpmap_interior_new
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_bump_interior_new();
        PixelShader = compile PS_2_X ps_main_bump_interior_new(false);
    }
}

technique bumpmap_interior_new_specmap
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_bump_interior_new();
        PixelShader = compile PS_2_X ps_main_bump_interior_new(true);
    }
}

DEFINE_LIGHTING_TECHNIQUE(bumpmap_interior, 1, 1, 0, 0, 0)    
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef STANDART_SHADERS


struct VS_OUTPUT_STANDART
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float4 VertexColor : COLOR0;
#ifdef INCLUDE_VERTEX_LIGHTING 
    float3 VertexLighting : COLOR1;
#endif
	
    float2 Tex0 : TEXCOORD0;
    float3 SunLightDir : TEXCOORD1;
    float3 SkyLightDir : TEXCOORD2;
#ifndef USE_LIGHTING_PASS 
    float4 PointLightDir : TEXCOORD3;
#endif
    float4 ShadowTexCoord : TEXCOORD4;
    float2 ShadowTexelPos : TEXCOORD5;
    float3 ViewDir : TEXCOORD6;
    float3 ReflectionUV : TEXCOORD7;
};

VS_OUTPUT_STANDART vs_main_standart(uniform const int PcfMode, uniform const bool use_bumpmap, uniform const bool use_skinning,
										float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL,
										float4 vVertexColor : COLOR0, float4 vBlendWeights : BLENDWEIGHT, float4 vBlendIndices : BLENDINDICES)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_STANDART, Out);
	
    float4 vObjectPos;
    float3 vObjectN, vObjectT, vObjectB;
	
    if (use_skinning)
    {
        vObjectPos = skinning_deform(vPosition, vBlendWeights, vBlendIndices);
		
        vObjectN = normalize(mul((float3x3) matWorldArray[vBlendIndices.x], vNormal) * vBlendWeights.x
									+ mul((float3x3) matWorldArray[vBlendIndices.y], vNormal) * vBlendWeights.y
									+ mul((float3x3) matWorldArray[vBlendIndices.z], vNormal) * vBlendWeights.z
									+ mul((float3x3) matWorldArray[vBlendIndices.w], vNormal) * vBlendWeights.w);
									
        if (use_bumpmap)
        {
            vObjectT = normalize(mul((float3x3) matWorldArray[vBlendIndices.x], vTangent) * vBlendWeights.x
										+ mul((float3x3) matWorldArray[vBlendIndices.y], vTangent) * vBlendWeights.y
										+ mul((float3x3) matWorldArray[vBlendIndices.z], vTangent) * vBlendWeights.z
										+ mul((float3x3) matWorldArray[vBlendIndices.w], vTangent) * vBlendWeights.w);
			
			// vObjectB = normalize(  mul((float3x3)matWorldArray[vBlendIndices.x], vBinormal) * vBlendWeights.x
			// 				+ mul((float3x3)matWorldArray[vBlendIndices.y], vBinormal) * vBlendWeights.y
			// 				+ mul((float3x3)matWorldArray[vBlendIndices.z], vBinormal) * vBlendWeights.z
			// 				+ mul((float3x3)matWorldArray[vBlendIndices.w], vBinormal) * vBlendWeights.w);
            vObjectB = /*normalize*/(cross(vObjectN, vObjectT));
            bool left_handed = (dot(cross(vNormal, vTangent), vBinormal) < 0.0f);
            if (left_handed)
            {
                vObjectB = -vObjectB;
            }
        }
    }
    else
    {
        vObjectPos = vPosition;
		
        vObjectN = vNormal;
									
        if (use_bumpmap)
        {
            vObjectT = vTangent;
            vObjectB = vBinormal;
        }
    }
	
    float4 vWorldPos = mul(matWorld, vObjectPos);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vObjectN));
	
    const bool use_motion_blur = bUseMotionBlur && (!use_skinning);
	
    if (use_motion_blur)	//motion blur flag!?!
    {
#ifdef STATIC_MOVEDIR //(used in instanced rendering )
			const float blur_len = 0.25f;
			float3 moveDirection = -normalize( float3(matWorld[0][0],matWorld[1][0],matWorld[2][0]) );
			moveDirection.y -= blur_len * 0.285;	//low down blur for big blur_lens (show more like a spline)
			float4 vWorldPos1 = vWorldPos + float4(moveDirection,0) * blur_len;
#else 
        float4 vWorldPos1 = mul(matMotionBlur, vObjectPos);
        float3 moveDirection = normalize(vWorldPos1 - vWorldPos);
#endif
		
		   
        float delta_coefficient_sharp = (dot(vWorldN, moveDirection) > 0.1f) ? 1 : 0;

        float y_factor = saturate(vObjectPos.y + 0.15);
        vWorldPos = lerp(vWorldPos, vWorldPos1, delta_coefficient_sharp * y_factor);

        float delta_coefficient_smooth = saturate(dot(vWorldN, moveDirection) + 0.5f);

        float extra_alpha = 0.1f;
        float start_alpha = (1.0f + extra_alpha);
        float end_alpha = start_alpha - 1.8f;
        float alpha = saturate(lerp(start_alpha, end_alpha, delta_coefficient_smooth));
        vVertexColor.a = saturate(0.5f - vObjectPos.y) + alpha + 0.25;
    }

    if (use_motion_blur)
    {
        Out.Pos = mul(matViewProj, vWorldPos);
    }
    else
    {
        Out.Pos = mul(matWorldViewProj, vObjectPos);
    }

    Out.Tex0 = tc;
	
    Out.ReflectionUV = reflect(normalize(vCameraPos.xyz - vWorldPos.xyz), vWorldN) * 0.5 + 0.5;
	
    Out.ReflectionUV.x = vSunColor.r > 0.1 ? Out.ReflectionUV.x * 0.5 : Out.ReflectionUV.x * 0.5 + 0.5;
	
	
    if (use_bumpmap)
    {
        float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vObjectB));
        float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vObjectT));
        float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

        Out.SunLightDir = normalize(mul(TBNMatrix, -vSunDir));
		//Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
        Out.SkyLightDir = mul(TBNMatrix, float3(0, 0, 1)); //STR_TEMP!?
        Out.VertexColor = vVertexColor;
		
		
		//point lights
#ifdef INCLUDE_VERTEX_LIGHTING
        Out.VertexLighting = calculate_point_lights_diffuse(vWorldPos, vWorldN, false, true);
#endif
		
#ifndef USE_LIGHTING_PASS 
        const int effective_light_index = iLightIndices[0];
        float3 point_to_light = vLightPosDir[effective_light_index] - vWorldPos.xyz;
        Out.PointLightDir.xyz = mul(TBNMatrix, normalize(point_to_light));
		
        float LD = dot(point_to_light, point_to_light);
        Out.PointLightDir.a = saturate(1.0f / LD); //prevent bloom for 1 meters
#endif
		
        float3 viewdir = normalize(vCameraPos.xyz - vWorldPos.xyz);
        Out.ViewDir = mul(TBNMatrix, viewdir);
		
#ifndef USE_LIGHTING_PASS
        if (PcfMode == PCF_NONE)
        {
            Out.ShadowTexCoord = calculate_point_lights_specular(vWorldPos, vWorldN, viewdir, true);
        }
#endif
    }
    else
    {

        Out.VertexColor = vVertexColor;
#ifdef INCLUDE_VERTEX_LIGHTING
        Out.VertexLighting = calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
		
        Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz);
		
        Out.SunLightDir = vWorldN;
#ifndef USE_LIGHTING_PASS
        Out.SkyLightDir = calculate_point_lights_specular(vWorldPos, vWorldN, Out.ViewDir, false);
#endif
    }
    Out.VertexColor.a *= vMaterialColor.a;

	

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float3 P = mul(matWorldView, vObjectPos); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
		
    return Out;
}


VS_OUTPUT_STANDART vs_main_standart_Instanced(uniform const int PcfMode, uniform const bool use_bumpmap, uniform const bool use_skinning,
										float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL,
										float4 vVertexColor : COLOR0, float4 vBlendWeights : BLENDWEIGHT, float4 vBlendIndices : BLENDINDICES,
									   //instance data:
									   float3 vInstanceData0 : TEXCOORD1, float3 vInstanceData1 : TEXCOORD2,
									   float3 vInstanceData2 : TEXCOORD3, float3 vInstanceData3 : TEXCOORD4)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_STANDART, Out);
	
    float4 vObjectPos;
    float3 vObjectN, vObjectT, vObjectB;
	
    if (use_skinning)
    {
		//no skinned instancing support yet!
		GIVE_ERROR_HERE_VS;
    }
    else
    {
        vObjectPos = vPosition;
		
        vObjectN = vNormal;
									
        if (use_bumpmap)
        {
            vObjectT = vTangent;
            vObjectB = vBinormal;
        }
    }
	
    float4x4 matWorldOfInstance = build_instance_frame_matrix(vInstanceData0, vInstanceData1, vInstanceData2, vInstanceData3);

    float4 vWorldPos = mul(matWorldOfInstance, vObjectPos);
    float3 vWorldN = normalize(mul((float3x3) matWorldOfInstance, vObjectN));
	
	
    const bool use_motion_blur = bUseMotionBlur && (!use_skinning);
	
    if (use_motion_blur)	//motion blur flag!?!
    {
        float4 vWorldPos1;
        float3 moveDirection;
        if (true)	//instanced meshes dont have valid matMotionBlur!
        {
            const float blur_len = 0.2f;
            moveDirection = -normalize(float3(matWorldOfInstance[0][0], matWorldOfInstance[1][0], matWorldOfInstance[2][0])); //using x axis !
            moveDirection.y -= blur_len * 0.285; //low down blur for big blur_lens (show more like a spline)
            vWorldPos1 = vWorldPos + float4(moveDirection, 0) * blur_len;
        }
        else
        {
            vWorldPos1 = mul(matMotionBlur, vObjectPos);
            moveDirection = normalize(vWorldPos1 - vWorldPos);
        }
		
		   
        float delta_coefficient_sharp = (dot(vWorldN, moveDirection) > 0.1f) ? 1 : 0;

        float y_factor = saturate(vObjectPos.y + 0.15);
        vWorldPos = lerp(vWorldPos, vWorldPos1, delta_coefficient_sharp * y_factor);

        float delta_coefficient_smooth = saturate(dot(vWorldN, moveDirection) + 0.5f);

        float extra_alpha = 0.1f;
        float start_alpha = (1.0f + extra_alpha);
        float end_alpha = start_alpha - 1.8f;
        float alpha = saturate(lerp(start_alpha, end_alpha, delta_coefficient_smooth));
        vVertexColor.a = saturate(0.5f - vObjectPos.y) + alpha + 0.25;
    }
	
	
	//-- Out.Pos = mul(matWorldViewProj, vObjectPos);
    Out.Pos = mul(matViewProj, vWorldPos);
	
    Out.Tex0 = tc;
	
	
    if (use_bumpmap)
    {
        float3 vWorld_binormal = normalize(mul((float3x3) matWorldOfInstance, vObjectB));
        float3 vWorld_tangent = normalize(mul((float3x3) matWorldOfInstance, vObjectT));
        float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

        Out.SunLightDir = normalize(mul(TBNMatrix, -vSunDir));
		//Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
        Out.SkyLightDir = mul(TBNMatrix, float3(0, 0, 1)); //STR_TEMP!?
        Out.VertexColor = vVertexColor;
		
		
		//point lights
#ifdef INCLUDE_VERTEX_LIGHTING
        Out.VertexLighting = calculate_point_lights_diffuse(vWorldPos, vWorldN, false, true);
#endif
		
#ifndef USE_LIGHTING_PASS 
        const int effective_light_index = iLightIndices[0];
        float3 point_to_light = vLightPosDir[effective_light_index] - vWorldPos.xyz;
        Out.PointLightDir.xyz = mul(TBNMatrix, normalize(point_to_light));
		
        float LD = dot(point_to_light, point_to_light);
        Out.PointLightDir.a = saturate(1.0f / LD); //prevent bloom for 1 meters
#endif
		
        float3 viewdir = normalize(vCameraPos.xyz - vWorldPos.xyz);
        Out.ViewDir = mul(TBNMatrix, viewdir);
		
#ifndef USE_LIGHTING_PASS
        if (PcfMode == PCF_NONE)
        {
            Out.ShadowTexCoord = calculate_point_lights_specular(vWorldPos, vWorldN, viewdir, true);
        }
#endif
    }
    else
    {

        Out.VertexColor = vVertexColor;
#ifdef INCLUDE_VERTEX_LIGHTING
        Out.VertexLighting = calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
		
        Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz);
		
        Out.SunLightDir = vWorldN;
#ifndef USE_LIGHTING_PASS
        Out.SkyLightDir = calculate_point_lights_specular(vWorldPos, vWorldN, Out.ViewDir, false);
#endif
    }

    Out.VertexColor.a *= vMaterialColor.a;
	

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float3 P = mul(matView, vWorldPos); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
	
    return Out;
}
float3 ToneMap_Reinhard(float3 color)
{
    return color / (color + 1.0);
}
// Mark7 Improved
PS_OUTPUT ps_main_standart(VS_OUTPUT_STANDART In, uniform const int PcfMode,
									uniform const bool use_bumpmap, uniform const bool use_specularfactor,
									uniform const bool use_specularmap, uniform const bool ps2x,
									uniform const bool use_aniso, uniform const bool terrain_color_ambient = true)
{
    PS_OUTPUT Output;

    float3 normal;
    if (use_bumpmap)
    {
        normal = normalize(2.0f * tex2D(NormalTextureSampler, In.Tex0) - 1.0f);
    }
    else
    {
        normal = In.SunLightDir;
    }
	
    float sun_amount = 1;
    if (PcfMode != PCF_NONE)
    {
        if ((PcfMode == PCF_NVIDIA) || ps2x)		//we have more ins count for shadow, add some ambient factor to sun amount
            sun_amount = 0.05f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        else
            sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }
		
	//define ambient term:
    const int ambientTermType = (terrain_color_ambient && (ps2x || !use_specularfactor)) ? 1 : 0;
    const float3 DirToSky = use_bumpmap ? In.SkyLightDir : float3(0.0f, 0.0f, 1.0f);
    float4 total_light = get_ambientTerm(ambientTermType, normal, DirToSky, sun_amount);
	
	
    float3 aniso_specular = 0;
    if (use_aniso)
    {
        if (!ps2x)
        {
			GIVE_ERROR_HERE;
        }
        float3 direction = float3(0, 1, 0);
        aniso_specular = calculate_hair_specular(normal, direction, ((use_bumpmap) ? In.SunLightDir : -vSunDir), In.ViewDir, In.Tex0);
    }
		
    if (use_bumpmap)
    {
        total_light.rgb += (saturate(dot(In.SunLightDir.xyz, normal.xyz)) + aniso_specular) * sun_amount * vSunColor;
	
        if (ps2x || !use_specularfactor)
        {
            total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
        }
#ifdef INCLUDE_VERTEX_LIGHTING
        if (ps2x || !use_specularfactor || (PcfMode == PCF_NONE))
        {
            total_light.rgb += In.VertexLighting;
        }
#endif
		
#ifndef USE_LIGHTING_PASS 
        float light_atten = In.PointLightDir.a;
        const int effective_light_index = iLightIndices[0];
        total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz) * vLightDiffuse[effective_light_index] * light_atten);
#endif
    }
    else
    {
        total_light.rgb += (saturate(dot(-vSunDir, normal.xyz)) + aniso_specular) * sun_amount * vSunColor;
		
        if (ambientTermType != 1 && !ps2x)
        {
            total_light += saturate(dot(-vSkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
        }
#ifdef INCLUDE_VERTEX_LIGHTING
        total_light.rgb += In.VertexLighting;
#endif
    }

    if (PcfMode != PCF_NONE)
        Output.RGBColor.rgb = total_light.rgb;
    else
        Output.RGBColor.rgb = min(total_light.rgb, 2.0f);
		
	// Output.RGBColor.rgb = total_light.rgb;	//saturate?
    Output.RGBColor.rgb *= vMaterialColor.rgb;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor.rgb *= tex_col.rgb;
    Output.RGBColor.rgb *= In.VertexColor.rgb;
	
	//add specular terms 
    if (use_specularfactor)
    {
        float4 fSpecular = 0;
		
        float4 specColor = 0.1 * spec_coef * vSpecularColor;
        if (use_specularmap)
        {
            float spec_tex_factor = dot(tex2D(SpecularTextureSampler, In.Tex0).rgb, 0.33); //get more precision from specularmap
            specColor *= spec_tex_factor;
        }
        else //if(use_specular_alpha)	//is that always true?
        {
            specColor *= tex_col.a;
        }

        float4 sun_specColor = specColor * vSunColor * sun_amount;
		
		//sun specular
        float3 vHalf = normalize(In.ViewDir + ((use_bumpmap) ? In.SunLightDir : -vSunDir));
        fSpecular = sun_specColor * pow(saturate(dot(vHalf, normal)), fMaterialPower);
        if (PcfMode != PCF_DEFAULT)	//we have 64 ins limit 
        {
            fSpecular *= In.VertexColor;
        }
		
        if (use_bumpmap)
        {
            if (PcfMode == PCF_NONE)	//add point lights' specular color for indoors
            {
                fSpecular.rgb += specColor * In.ShadowTexCoord.rgb; //ShadowTexCoord => point lights specular! (calculate_point_lights_specular)
            }
			
			//add more effects for ps2a version:
            if (ps2x || (PcfMode == PCF_NONE))
            {
			
#ifndef USE_LIGHTING_PASS 
				//effective point light specular
                float light_atten = In.PointLightDir.a;
                const int effective_light_index = iLightIndices[0];
                float4 light_specColor = specColor * vLightDiffuse[effective_light_index] * (light_atten * 0.5); //dec. spec term to remove "effective light change" artifacts
                vHalf = normalize(In.ViewDir + In.PointLightDir);
                fSpecular += light_specColor * pow(saturate(dot(vHalf, normal)), fMaterialPower);
#endif
            }
        }
        else
        {
            fSpecular.rgb += specColor * In.SkyLightDir * 0.1; //SkyLightDir-> holds lights specular color (calculate_point_lights_specular)
        }
		
        float fresnel = pow(1.0 - max(dot(normal, In.ViewDir), 0.0), 5.0);
        fSpecular *= fresnel;
        Output.RGBColor += fSpecular;
    }
    else if (use_specularmap)
    {
		GIVE_ERROR_HERE;
    }
	Output.RGBColor.rgb = ToneMap_Reinhard(Output.RGBColor.rgb);
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
	
	//if we dont use alpha channel for specular-> use it for alpha
    Output.RGBColor.a = In.VertexColor.a; //we dont control bUseMotionBlur to fit in 64 instruction
	
    if ((!use_specularfactor) || use_specularmap)
    {
        Output.RGBColor.a *= tex_col.a;
    }

    return Output;
}

// Schlick's approximation for Fresnel effect
float3 SchlickFresnel(float3 viewDir, float3 normal, float F0, float fresnelExponent)
{
    // Ensure the base reflectivity is clamped to reasonable physical values
    F0 = clamp(F0, 0.0, 1.0);

    // The dot product is clamped to avoid negative values, which have no physical meaning
    float viewDotNormal = max(dot(viewDir, normal), 0.0);

    // Calculate Fresnel term using the exponent for more artistic control
    float3 fresnel = F0 + (1 - F0) * pow(1 - viewDotNormal, fresnelExponent);

    return fresnel;
}

// Calculate environment reflection
float3 CalculateEnvironmentReflection(float3 normal, float3 viewDir, samplerCUBE envMapSampler)
{
    float3 reflection = reflect(-viewDir, normal); // Reflect view vector around normal
    float3 envMapColor = texCUBE(envMapSampler, reflection).rgb;
    return envMapColor;
}

// Combine base color with reflective color
float3 CombineBaseAndReflectiveColor(float3 baseColor, float3 reflectiveColor, float3 specularColor, float3 ambientColor)
{
    // Scale and mix the reflective color with the base color
    float3 combinedColor = lerp(baseColor, reflectiveColor, 0.5) + specularColor;

    // Add a subtle ambient term to simulate environmental lighting
    combinedColor += ambientColor * 0.012;

    return combinedColor;
}
float OverlayBlend(float base, float blend)
{
    return base < 0.5 ? (2.0 * base * blend) : (1.0 - 2.0 * (1.0 - base) * (1.0 - blend));
}

float3 OverlayBlendColor(float3 base, float3 blend)
{
    return float3(OverlayBlend(base.r, blend.r), OverlayBlend(base.g, blend.g), OverlayBlend(base.b, blend.b));
}

PS_OUTPUT ps_main_standart_fresnel(VS_OUTPUT_STANDART In, uniform const int PcfMode,
									uniform const bool use_bumpmap, uniform const bool use_specularfactor,
									uniform const bool use_specularmap, uniform const bool ps2x,
									uniform const bool use_aniso, uniform const bool terrain_color_ambient = true,
									uniform const bool use_envmap = true)
{
    PS_OUTPUT Output;

    float3 normal;
    if (use_bumpmap)
    {
        normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0) - 1.0f);
    }
    else
    {
        normal = In.SunLightDir;
    }
	
    float sun_amount = 1;
    if (PcfMode != PCF_NONE)
    {
        if ((PcfMode == PCF_NVIDIA) || ps2x)		//we have more ins count for shadow, add some ambient factor to sun amount
            sun_amount = 0.05f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        else
            sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 spec_col = tex2D(SpecularTextureSampler, In.Tex0);
	//define ambient term:
    const int ambientTermType = (terrain_color_ambient && (ps2x || !use_specularfactor)) ? 1 : 0;
    const float3 DirToSky = use_bumpmap ? In.SkyLightDir : float3(0.0f, 0.0f, 1.0f);
               
    // Normalize view vector for accurate angle calculations
    float3 vView = normalize(In.ViewDir);
    float lightFresnel = SchlickFresnel(vView, spec_col.g, 1, 5.0);

    float4 total_light = get_ambientTerm(ambientTermType, normal, DirToSky, sun_amount);
    //total_light = lerp(total_light, tex_col, lightFresnel) + pow((tex_col * spec_col), 4);
    
    float4 tint, envmap;
    float3 reflectionUV;
    tint = total_light;
    envmap = total_light;
    float3 refUV = clamp(spec_col.rgb +0.75,0,1) * In.ReflectionUV;
    if (use_envmap)
    {
		// reflectionUV	= reflect(In.ViewDir, normal);
		// reflectionUV.x = (1 + reflectionUV.x) * 0.5;
		// reflectionUV.y = (1 + reflectionUV.y) * -0.5;
		// envmap = tex2D(EnvTextureSampler, reflectionUV.xy);
		// reflectionUV.x = (1 + reflectionUV.x) * 0.5;
		// reflectionUV.z = (1 + reflectionUV.z) * -0.5;
        envmap = pow(tex2D(EnvTextureSampler, refUV.xz), 3);
        //envmap.rgb = OverlayBlendColor(envmap.rgb, float3(normal.r, normal.r, normal.r));
    }
    
    float3 aniso_specular = 0;
    if (use_aniso)
    {
        if (!ps2x)
        {
			GIVE_ERROR_HERE;
        }
        float3 direction = float3(0, 1, 0);
        aniso_specular = calculate_hair_specular(normal, direction, ((use_bumpmap) ? In.SunLightDir : -vSunDir), In.ViewDir, In.Tex0);
    }
		
    if (use_bumpmap)
    {
        total_light.rgb += (saturate(dot(In.SunLightDir.xyz, normal.xyz)) + aniso_specular) * sun_amount * vSunColor;
	
        if (ps2x || !use_specularfactor)
        {
            total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
        }
#ifdef INCLUDE_VERTEX_LIGHTING
        if (ps2x || !use_specularfactor || (PcfMode == PCF_NONE))
        {
            total_light.rgb += In.VertexLighting;
        }
#endif
		
#ifndef USE_LIGHTING_PASS 
        float light_atten = In.PointLightDir.a;
        const int effective_light_index = iLightIndices[0];
        total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz) * vLightDiffuse[effective_light_index] * light_atten);
#endif
    }
    else
    {
        total_light.rgb += (saturate(dot(-vSunDir, normal.xyz)) + aniso_specular) * sun_amount * vSunColor;
		
        if (ambientTermType != 1 && !ps2x)
        {
            total_light += saturate(dot(-vSkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
        }
#ifdef INCLUDE_VERTEX_LIGHTING
        total_light.rgb += In.VertexLighting;
#endif
    }
	
    if (use_envmap != true)
    {
		
        float3 vView = normalize(In.ViewDir);
        float3 specMap = tex2D(SpecularTextureSampler, In.Tex0);
        
        total_light.rgb += (0.020 * (total_light.rgb * SchlickFresnel(vView, normal, specMap.g, 5.0)));
        total_light = saturate(total_light);
    }

	
	

    if (PcfMode != PCF_NONE)
        Output.RGBColor.rgb = total_light.rgb;
    else
        Output.RGBColor.rgb = min(total_light.rgb, 2.0f);
		
	// Output.RGBColor.rgb = total_light.rgb;	//saturate?
    Output.RGBColor.rgb *= vMaterialColor.rgb;
	
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor.rgb *= tex_col.rgb;
    Output.RGBColor.rgb *= In.VertexColor.rgb;
	
	//add specular terms 
    if (use_specularfactor)
    {
        float4 fSpecular = 0;
		
        float4 specColor = 0.1 * spec_coef * vSpecularColor;
        if (use_specularmap)
        {
            float spec_tex_factor = dot(tex2D(SpecularTextureSampler, In.Tex0).rgb, 0.33); //get more precision from specularmap
            specColor *= spec_tex_factor;
        }
        else //if(use_specular_alpha)	//is that always true?
        {
            specColor *= tex_col.a;
        }
		
        float4 sun_specColor = specColor * vSunColor * sun_amount;
		
		//sun specular
        float3 vHalf = normalize(In.ViewDir + ((use_bumpmap) ? In.SunLightDir : -vSunDir));
        fSpecular = sun_specColor * pow(saturate(dot(vHalf, normal)), fMaterialPower);
        if (PcfMode != PCF_DEFAULT)	//we have 64 ins limit 
        {
            fSpecular *= In.VertexColor;
        }
		
        if (use_bumpmap)
        {
            if (PcfMode == PCF_NONE)	//add point lights' specular color for indoors
            {
                fSpecular.rgb += specColor * In.ShadowTexCoord.rgb; //ShadowTexCoord => point lights specular! (calculate_point_lights_specular)
            }
			
			//add more effects for ps2a version:
            if (ps2x || (PcfMode == PCF_NONE))
            {
			
#ifndef USE_LIGHTING_PASS 
				//effective point light specular
                float light_atten = In.PointLightDir.a;
                const int effective_light_index = iLightIndices[0];
                float4 light_specColor = specColor * vLightDiffuse[effective_light_index] * (light_atten * 0.5); //dec. spec term to remove "effective light change" artifacts
                vHalf = normalize(In.ViewDir + In.PointLightDir);
                fSpecular += light_specColor * pow(saturate(dot(vHalf, normal)), fMaterialPower);
#endif
            }
        }
        else
        {
            fSpecular.rgb += specColor * In.SkyLightDir * 0.1; //SkyLightDir-> holds lights specular color (calculate_point_lights_specular)
        }
		
        if (use_envmap)
        {
            // Reflection Special Mark7

		    // reflectionUV.x = (1 + reflectionUV.x) * 0.5;
		    // reflectionUV.z = (1 + reflectionUV.z) * -0.5;
            float3 reflectMap = tex2D(ReflectionTextureSampler, refUV.xz);
            float3 refCol = OverlayBlendColor(envmap, pow(reflectMap, 1));
            float3 finalCol = Output.RGBColor.rgb;
            float3 col = (finalCol * ((((tex_col.rgb * 1.8) + (tint.rgb * 1.8)) + (specColor * 1.5)) * specColor)) + (finalCol * pow(1 - specColor, 4));
            
            float sG = OverlayBlend(specColor.g, normal.g);
            float sR = OverlayBlend(specColor.r, normal.r);
            
            float S = lerp(sR, sG, 0.5);
            // Calculate Fresnel term using Schlick's approximation
            float3 fresnel = SchlickFresnel(vView, normal, lerp(pow(S, 4), fSpecular.g, 1), 5.0) * total_light.rgb;
            // Combine Fresnel term with environment map color and specular color
            float3 reflectiveColor = fresnel * specColor.rgb * refCol;

            float3 blendedColorG = OverlayBlendColor(reflectiveColor, float3(normal.g, normal.g, normal.g));
            float3 blendedColorR = OverlayBlendColor(reflectiveColor, float3(normal.r, normal.r, normal.r));
            reflectiveColor = ToneMap_Reinhard(reflectiveColor);
            reflectiveColor *= 3;
            finalCol = ToneMap_Reinhard(finalCol);
            col = ToneMap_Reinhard(col);
            
            //Output.RGBColor.rgb += reflectiveColor;
            Output.RGBColor.rgb = lerp(col, finalCol, 0.75) + (DesaturateColor(reflectiveColor, 0.5) * specColor + fSpecular * 0.012 * vGroundAmbientColor);
        }
        else
        {
    // If environment mapping is not used, fall back to regular specular highlight
            Output.RGBColor += fSpecular;
        }

		//Output.RGBColor = float4(fresnel, 1);
		//Output.RGBColor += fSpecular;
		
    }
    else if (use_specularmap)
    {
		GIVE_ERROR_HERE;
    }
    Output.RGBColor.rgb = ToneMap_Reinhard(Output.RGBColor.rgb);
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
	
	//if we dont use alpha channel for specular-> use it for alpha
    Output.RGBColor.a = In.VertexColor.a; //we dont control bUseMotionBlur to fit in 64 instruction
	
    if ((!use_specularfactor) || use_specularmap)
    {
        Output.RGBColor.a *= tex_col.a;
    }

    return Output;
}




PS_OUTPUT ps_main_standart_old_good(VS_OUTPUT_STANDART In, uniform const int PcfMode, uniform const bool use_specularmap, uniform const bool use_aniso)
{
    PS_OUTPUT Output;
	
	
    float sun_amount = 1;
    if (PcfMode != PCF_NONE)
    {
        sun_amount = 0.03f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }

    float3 normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0) - 1.0f);
	
	//define ambient term:
    static const int ambientTermType = 1;
    float3 DirToSky = In.SkyLightDir;
    float4 total_light = get_ambientTerm(ambientTermType, normal, DirToSky, sun_amount);
	
    float4 specColor = vSunColor * (vSpecularColor * 0.1);
    if (use_specularmap)
    {
        float spec_tex_factor = dot(tex2D(SpecularTextureSampler, In.Tex0).rgb, 0.33); //get more precision from specularmap
        specColor *= spec_tex_factor;
    }
	
    float3 vHalf = normalize(In.ViewDir + In.SunLightDir);
    float4 fSpecular = specColor * pow(saturate(dot(vHalf, normal)), fMaterialPower); // saturate(dot(In.SunLightDir, normal));
	
	
    if (use_aniso)
    {
        float3 tangent_ = float3(0, 1, 0);
        fSpecular.rgb += calculate_hair_specular(normal, tangent_, In.SunLightDir, In.ViewDir, In.Tex0);
    }
    else
    {
        fSpecular.rgb *= spec_coef;
    }
	
		
    total_light += (saturate(dot(In.SunLightDir.xyz, normal.xyz)) + fSpecular) * sun_amount * vSunColor;
    total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;
	
	
#ifndef USE_LIGHTING_PASS 
    float light_atten = In.PointLightDir.a;
    const int effective_light_index = iLightIndices[0];
    total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz)) * vLightDiffuse[effective_light_index] * light_atten;
#endif
	
#ifdef INCLUDE_VERTEX_LIGHTING
    total_light.rgb += In.VertexLighting;
#endif
	

    Output.RGBColor.rgb = total_light.rgb; //saturate(total_light.rgb);	//false!
    Output.RGBColor.a = 1.0f;
    Output.RGBColor *= vMaterialColor;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
	
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    Output.RGBColor.a = In.VertexColor.a * tex_col.a;

    return Output;
}

#ifdef USE_PRECOMPILED_SHADER_LISTS
																		//use_bumpmap, use_skinning, 
VertexShader standart_vs_noshadow[] =
{
    compile vs_2_0 vs_main_standart(PCF_NONE, 0, 0),
										compile vs_2_0 vs_main_standart(PCF_NONE, 0, 1),
										compile vs_2_0 vs_main_standart(PCF_NONE, 1, 0),
										compile vs_2_0 vs_main_standart(PCF_NONE, 1, 1)
};
										
VertexShader standart_vs_default[] =
{
    compile vs_2_0 vs_main_standart(PCF_DEFAULT, 0, 0),
										compile vs_2_0 vs_main_standart(PCF_DEFAULT, 0, 1),
										compile vs_2_0 vs_main_standart(PCF_DEFAULT, 1, 0),
										compile vs_2_0 vs_main_standart(PCF_DEFAULT, 1, 1)
};
										                            
VertexShader standart_vs_nvidia[] =
{
    compile vs_2_0 vs_main_standart(PCF_NVIDIA, 0, 0), //ps_main_standart compiled versions?!
										compile vs_2_0 vs_main_standart(PCF_NVIDIA, 0, 1),
										compile vs_2_0 vs_main_standart(PCF_NVIDIA, 1, 0),
										compile vs_2_0 vs_main_standart(PCF_NVIDIA, 1, 1)
};
										
#define DEFINE_STANDART_TECHNIQUE(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso, terraincolor)	\
				technique tech_name	\
				{ pass P0 { VertexShader = standart_vs_noshadow[(2*use_bumpmap) + use_skinning]; \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, false, use_aniso, terraincolor);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = standart_vs_default[(2*use_bumpmap) + use_skinning]; \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, false, use_aniso, terraincolor);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = standart_vs_nvidia[(2*use_bumpmap) + use_skinning]; \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} }  \
				DEFINE_LIGHTING_TECHNIQUE(tech_name, 0, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)

							
#define DEFINE_STANDART_TECHNIQUE_HIGH(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso, terraincolor)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} } \
				DEFINE_LIGHTING_TECHNIQUE(tech_name, 0, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)

////FRESNEL				
#define DEFINE_STANDART_TECHNIQUE_HIGH_FRESNEL(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso, terraincolor, use_envmap)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart_fresnel(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor, use_envmap);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart_fresnel(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor, use_envmap);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart_fresnel(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor, use_envmap);} } \
				DEFINE_LIGHTING_TECHNIQUE(tech_name, 0, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)
//////

#define DEFINE_STANDART_TECHNIQUE_INSTANCED(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso, terraincolor)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NONE, use_bumpmap, false); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_DEFAULT, use_bumpmap, false); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NVIDIA, use_bumpmap, false); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor);} } //lighting?
							
							
#define DEFINE_STANDART_TECHNIQUE_HIGH_INSTANCED(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } 
							
#else 

#define DEFINE_STANDART_TECHNIQUE(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, false, use_aniso);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, false, use_aniso);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} }  \
				DEFINE_LIGHTING_TECHNIQUE(tech_name, 0, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)

							

#define DEFINE_STANDART_TECHNIQUE_HIGH(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				DEFINE_LIGHTING_TECHNIQUE(tech_name, 0, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)

///FRESNEL				
#define DEFINE_STANDART_TECHNIQUE_HIGH_FRESNEL(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso, terraincolor, use_envmap)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart_fresnel(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor, use_envmap);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart_fresnel(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor, use_envmap);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart_fresnel(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso, terraincolor, use_envmap);} } \
				DEFINE_LIGHTING_TECHNIQUE(tech_name, 0, use_bumpmap, use_skinning, use_specularfactor, use_specularmap)
/////////////////	

#define DEFINE_STANDART_TECHNIQUE_INSTANCED(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NONE, use_bumpmap, false); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_DEFAULT, use_bumpmap, false); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NVIDIA, use_bumpmap, false); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } // lighting?
							
							
#define DEFINE_STANDART_TECHNIQUE_HIGH_INSTANCED(tech_name, use_bumpmap, use_skinning, use_specularfactor, use_specularmap, use_aniso)	\
				technique tech_name	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NONE, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDW	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_DEFAULT, use_bumpmap, use_skinning); \
							PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } \
				technique tech_name##_SHDWNVIDIA	\
				{ pass P0 { VertexShader = compile vs_2_0 vs_main_standart_Instanced(PCF_NVIDIA, use_bumpmap, use_skinning); \
							PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, use_bumpmap, use_specularfactor, use_specularmap, true, use_aniso);} } 

#endif //USE_PRECOMPILED_SHADER_LISTS


DEFINE_STANDART_TECHNIQUE(standart_noskin_bump_nospecmap, true, false, true, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_noskin_bump_specmap, true, false, true, true, false, true)
DEFINE_STANDART_TECHNIQUE(standart_skin_bump_nospecmap, true, true, true, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_skin_bump_specmap, true, true, true, true, false, true)
                        
//high versions: 
DEFINE_STANDART_TECHNIQUE_HIGH(standart_skin_bump_nospecmap_high, true, true, true, false, false, true)
DEFINE_STANDART_TECHNIQUE_HIGH(standart_skin_bump_specmap_high, true, true, true, true, false, true)

//fresnel
DEFINE_STANDART_TECHNIQUE_HIGH_FRESNEL(standart_skin_bump_specmap_high_fresnel, true, true, true, true, false, true, false)
DEFINE_STANDART_TECHNIQUE_HIGH_FRESNEL(standart_skin_bump_specmap_high_fresnel_envmap, true, true, true, true, false, true, true)
///

DEFINE_STANDART_TECHNIQUE_HIGH(standart_noskin_bump_nospecmap_high, true, false, true, false, false, true)
DEFINE_STANDART_TECHNIQUE_HIGH(standart_noskin_bump_specmap_high, true, false, true, true, false, true)
                                                                                      
//-----------------------------------------------
//nobump versions:
DEFINE_STANDART_TECHNIQUE(standart_noskin_nobump_nospecmap, false, false, true, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_noskin_nobump_specmap, false, false, true, true, false, true)
DEFINE_STANDART_TECHNIQUE(standart_skin_nobump_nospecmap, false, true, true, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_skin_nobump_specmap, false, true, true, true, false, true)
                                                                                        
//-----------------------------------------------
//nospec versions:
//
DEFINE_STANDART_TECHNIQUE(standart_noskin_nobump_nospec, false, false, false, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_noskin_bump_nospec, true, false, false, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_noskin_bump_nospec_noterraincolor, true, false, false, false, false, false)
DEFINE_STANDART_TECHNIQUE(standart_skin_nobump_nospec, false, true, false, false, false, true)
DEFINE_STANDART_TECHNIQUE(standart_skin_bump_nospec, true, true, false, false, false, true)
                                                                                         
//nospec_high
DEFINE_STANDART_TECHNIQUE_HIGH(standart_noskin_bump_nospec_high, true, false, false, false, false, true)
DEFINE_STANDART_TECHNIQUE_HIGH(standart_noskin_bump_nospec_high_noterraincolor, true, false, false, false, false, false)
DEFINE_STANDART_TECHNIQUE_HIGH(standart_skin_bump_nospec_high, true, true, false, false, false, true)


///--------
DEFINE_STANDART_TECHNIQUE_INSTANCED(standart_noskin_bump_nospecmap_Instanced, true, false, true, false, false, true)
DEFINE_STANDART_TECHNIQUE_INSTANCED(standart_noskin_nobump_specmap_Instanced, false, false, true, true, false, true)
DEFINE_STANDART_TECHNIQUE_INSTANCED(standart_noskin_bump_specmap_Instanced, true, false, true, true, false, true)
DEFINE_STANDART_TECHNIQUE_INSTANCED(standart_noskin_nobump_nospecmap_Instanced, false, false, true, false, false, true)
DEFINE_STANDART_TECHNIQUE_INSTANCED(standart_noskin_bump_nospec_high_Instanced, true, false, false, false, false, true)
DEFINE_STANDART_TECHNIQUE_INSTANCED(standart_noskin_bump_nospec_high_noterraincolor_Instanced, true, false, false, false, false, false)

DEFINE_STANDART_TECHNIQUE_HIGH_INSTANCED(standart_noskin_bump_specmap_high_Instanced, true, false, true, true, false)
DEFINE_STANDART_TECHNIQUE_HIGH_INSTANCED(standart_noskin_bump_nospecmap_high_Instanced, true, false, true, false, false)

//aniso versions:       
// technique nospecular_skin_bumpmap_high_aniso
technique standart_skin_bump_nospecmap_high_aniso
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, true, true);
		//PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, true, true, false, true, true);
        PixelShader = compile PS_2_X ps_main_standart_old_good(PCF_NONE, false, true);
    }
}
technique standart_skin_bump_nospecmap_high_aniso_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, true, true);
		//PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, true, true, false, true, true);
        PixelShader = compile PS_2_X ps_main_standart_old_good(PCF_DEFAULT, false, true);
    }
}
technique standart_skin_bump_nospecmap_high_aniso_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_main_standart(PCF_NVIDIA, true, true);
		//PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, true, true, false, true, true);
        PixelShader = compile ps_2_a ps_main_standart_old_good(PCF_NVIDIA, false, true);
    }
}

// technique specular_skin_bumpmap_high_aniso
technique standart_skin_bump_specmap_high_aniso
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart(PCF_NONE, true, true);
		//PixelShader = compile PS_2_X ps_main_standart(PCF_NONE, true, true, true, true, true);
        PixelShader = compile PS_2_X ps_main_standart_old_good(PCF_NONE, true, true);
    }
}
technique standart_skin_bump_specmap_high_aniso_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart(PCF_DEFAULT, true, true);
		//PixelShader = compile PS_2_X ps_main_standart(PCF_DEFAULT, true, true, true, true, true);
        PixelShader = compile PS_2_X ps_main_standart_old_good(PCF_DEFAULT, true, true);
    }
}
technique standart_skin_bump_specmap_high_aniso_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_main_standart(PCF_NVIDIA, true, true);
		//PixelShader = compile ps_2_a ps_main_standart(PCF_NVIDIA, true, true, true, true);
        PixelShader = compile ps_2_a ps_main_standart_old_good(PCF_NVIDIA, true, true);
    }
}


// !  technique specular_diffuse -> standart_noskin_nobump_specmap
// !  technique specular_diffuse_skin -> standart_skin_nobump_specmap
// !  technique specular_alpha -> standart_noskin_nobump_nospecmap
// !  technique specular_alpha_skin -> standart_skin_nobump_nospecmap
////////////////////////////
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef HAIR_SHADERS

struct VS_OUTPUT_SIMPLE_HAIR
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
    float Fog : FOG;
};

VS_OUTPUT_SIMPLE_HAIR vs_hair(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_SIMPLE_HAIR, Out);
	
    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, true, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = vColor * diffuse_light;

	//shadow mapping variables
    float wNdotSun = dot(vWorldN, -vSunDir);
    Out.SunLight = max(0.2f * (wNdotSun + 0.9f), wNdotSun) * vSunColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}
PS_OUTPUT ps_hair(VS_OUTPUT_SIMPLE_HAIR In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 tex1_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 tex2_col = tex2D(Diffuse2Sampler, In.Tex0);
	
    float4 final_col;
	
	INPUT_TEX_GAMMA(tex1_col.rgb);
	
    final_col = tex1_col * vMaterialColor;
	
    float alpha = saturate(((2.0f * vMaterialColor2.a) + tex2_col.a) - 1.9f);
    final_col.rgb *= (1.0f - alpha);
    final_col.rgb += tex2_col.rgb * alpha;
	
	//    tex_col = tex2_col * vMaterialColor2.a + tex1_col * (1.0f - vMaterialColor2.a);
	
	
    float4 total_light = In.Color;
    if ((PcfMode != PCF_NONE))
    {
        float sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        total_light.rgb += In.SunLight.rgb * sun_amount;
    }
    else
    {
        total_light.rgb += In.SunLight.rgb;
    }
    Output.RGBColor = final_col * total_light;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    return Output;
}

DEFINE_TECHNIQUES(hair_shader, vs_hair, ps_hair)


struct VS_INPUT_HAIR
{
    float4 vPosition : POSITION;
    float3 vNormal : NORMAL;
    float3 vTangent : BINORMAL;
	
    float2 tc : TEXCOORD0;
    float4 vColor : COLOR0;
};
struct VS_OUTPUT_HAIR
{
    float4 Pos : POSITION;
    float2 Tex0 : TEXCOORD0;
	
    float4 VertexLighting : TEXCOORD1;
	
    float3 viewVec : TEXCOORD2;
    float3 normal : TEXCOORD3;
    float3 tangent : TEXCOORD4;
    float4 VertexColor : COLOR0;
	
	
    float4 ShadowTexCoord : TEXCOORD6;
    float2 ShadowTexelPos : TEXCOORD7;
    float Fog : FOG;
};

VS_OUTPUT_HAIR vs_hair_aniso(uniform const int PcfMode, VS_INPUT_HAIR In)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_HAIR, Out);

    Out.Pos = mul(matWorldViewProj, In.vPosition);

    float4 vWorldPos = (float4) mul(matWorld, In.vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, In.vNormal)); //normal in world space

    float3 P = mul(matWorldView, In.vPosition); //position in view space

    Out.Tex0 = In.tc;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, true, false);
#endif
	
	//apply material color
    Out.VertexLighting = saturate(In.vColor * diffuse_light);
	
    Out.VertexColor = In.vColor;
	
    if (true)
    {
        float3 Pview = vCameraPos - vWorldPos;
        Out.normal = normalize(mul(matWorld, In.vNormal));
        Out.tangent = normalize(mul(matWorld, In.vTangent));
        Out.viewVec = normalize(Pview);
    }
	
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}

// Mark7 Hair calculations

// A simple Fresnel term calculation
float FresnelTerm(float3 viewDir, float3 hairNormal)
{
    return pow(1.0 - max(dot(viewDir, hairNormal), 0.0), 5.0);
}
float3 Desaturate(float3 color, float desaturation)
{
    // Compute the luminance using Rec. 709 luminance formula
    float luminance = dot(color, float3(0.2126, 0.7152, 0.0722));
    
    // Lerp between the original color and the luminance by the desaturation amount
    return lerp(color, float3(luminance, luminance, luminance), desaturation);
}
PS_OUTPUT ps_hair_aniso(VS_OUTPUT_HAIR In, uniform const int PcfMode)
{
    PS_OUTPUT Output;

    float3 lightDir = -vSunDir;
    float3 hairColor = vMaterialColor.rgb; // Base hair color from the material
    float4 nm = tex2D(NormalTextureSampler, In.Tex0);
	
    // Sample texture colors
    float4 tex1_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 tex2_col = tex2D(Diffuse2Sampler, In.Tex0);

    // Adjust the hair color based on the age of the character
    // Interpolate between the hair color and white as the character ages
    float ageFactor = vMaterialColor2.a; // Assuming this is a value between 0 and 1
    float3 ageColor = lerp(hairColor, tex2_col.rgb, ageFactor * 0.8); // Blend towards white with age

    // Compute diffuse term using your existing function or calculations
    float3 diffuse = ageColor * vSunColor.rgb * In.VertexColor.rgb * HairDiffuseTerm(In.normal, lightDir);

    // Adjusting alpha blending for texture interaction
    float alpha = saturate((2.0f * vMaterialColor2.a) + tex2_col.a - 1.0f);
    float3 final_col = lerp(tex1_col.rgb, tex2_col.rgb, alpha) * ageColor;

    // Compute specular term using your existing function
    float3 specular = calculate_hair_specular(In.normal, In.tangent, lightDir, In.viewVec, In.Tex0);

    // Calculate sun contribution
    float sun_amount = (PcfMode != PCF_NONE) ? GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos) : 1.0f;

    // Sum ambient, diffuse, and specular contributions
    float3 total_light = vAmbientColor.rgb + ((diffuse + specular) * (sun_amount * 0.5)) + (In.VertexLighting.rgb * 0.5) + specular;
    
    float3 des = Desaturate(tex1_col.rgb, 1);
    // Apply final color and lighting
    Output.RGBColor.rgb = total_light * final_col.rgb * (des * lerp(des, float3(1, 1, 1), 0.5));
    Output.RGBColor.a = tex1_col.a; // You can also use alpha here if needed

    // Gamma correction if necessary
    OUTPUT_GAMMA(Output.RGBColor.rgb);

    // Ensure the final color is within the valid range
    Output.RGBColor = saturate(Output.RGBColor);

    return Output;
}


technique hair_shader_aniso
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_hair_aniso(PCF_NONE);
        PixelShader = compile PS_2_X ps_hair_aniso(PCF_NONE);
    }
}
technique hair_shader_aniso_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_hair_aniso(PCF_DEFAULT);
        PixelShader = compile PS_2_X ps_hair_aniso(PCF_DEFAULT);
    }
}
technique hair_shader_aniso_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_hair_aniso(PCF_NVIDIA);
        PixelShader = compile ps_2_a ps_hair_aniso(PCF_NVIDIA);
    }
}

#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef FACE_SHADERS

struct VS_OUTPUT_SIMPLE_FACE
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
    float Fog : FOG;
};
VS_OUTPUT_SIMPLE_FACE vs_face(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_SIMPLE_FACE, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;
	//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, true, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = vMaterialColor * vColor * diffuse_light;

	//shadow mapping variables
    float wNdotSun = dot(vWorldN, -vSunDir);
    Out.SunLight = max(0.2f * (wNdotSun + 0.9f), wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}
PS_OUTPUT ps_face(VS_OUTPUT_SIMPLE_FACE In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 tex1_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 tex2_col = tex2D(Diffuse2Sampler, In.Tex0);
	
    float4 tex_col;
	
    tex_col = tex2_col * In.Color.a + tex1_col * (1.0f - In.Color.a);
	
	INPUT_TEX_GAMMA(tex_col.rgb);
	
    if ((PcfMode != PCF_NONE))
    {
        float sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        Output.RGBColor = tex_col * ((In.Color + In.SunLight * sun_amount));
    }
    else
    {
        Output.RGBColor = tex_col * (In.Color + In.SunLight);
    }
	// gamma correct
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    Output.RGBColor.a = vMaterialColor.a;
	
    return Output;
}

DEFINE_TECHNIQUES(face_shader, vs_face, ps_face)

DEFINE_LIGHTING_TECHNIQUE(face_shader, 0, 0, 0, 0, 0)    

////////////////////////////////////////


struct VS_INPUT_FACE
{
    float4 Position : POSITION;
    float2 TC : TEXCOORD0;
	
    float4 VertexColor : COLOR0;
	
    float3 Normal : NORMAL;
    float3 Tangent : TANGENT;
    float3 Binormal : BINORMAL;
};
struct VS_OUTPUT_FACE
{
    float4 Pos : POSITION;
    float Fog : FOG;

    float4 VertexColor : COLOR0;
    float2 Tex0 : TEXCOORD0;

    float3 WorldPos : TEXCOORD1;
    float3 ViewVec : TEXCOORD2;
	
    float3 SunLightDir : TEXCOORD3;
    float4 PointLightDir : TEXCOORD4;
	
    float4 ShadowTexCoord : TEXCOORD5;
    float2 ShadowTexelPos : TEXCOORD6;
#ifdef  INCLUDE_VERTEX_LIGHTING
    float3 VertexLighting : TEXCOORD7;
#endif
};

VS_OUTPUT_STANDART vs_main_standart_face_mod(uniform const int PcfMode,
										uniform const bool use_bumpmap,
										float4 vPosition : POSITION,
										float3 vNormal : NORMAL,
										float2 tc : TEXCOORD0,
										float3 vTangent : TANGENT,
										float3 vBinormal : BINORMAL,
										float4 vVertexColor : COLOR0,
										float4 vBlendWeights : BLENDWEIGHT,
										float4 vBlendIndices : BLENDINDICES)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_STANDART, Out);

	
    float4 vObjectPos;
    float3 vObjectN, vObjectT, vObjectB;
	
    vObjectPos = vPosition;
	
    vObjectN = vNormal;
    if (use_bumpmap)
    {
        vObjectT = vTangent;
        vObjectB = vBinormal;
    }
		
    float4 vWorldPos = mul(matWorld, vObjectPos);
    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Tex0 = tc;

	
    float3 vWorldN = normalize(mul((float3x3) matWorld, vObjectN));
	
    float3x3 TBNMatrix;
    if (use_bumpmap)
    {
        float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vObjectB));
        float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vObjectT));
        TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);
    }
	

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
    }

    if (use_bumpmap)
    {
        Out.SunLightDir = normalize(mul(TBNMatrix, -vSunDir));
        Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
    }
    else
    {
        Out.SunLightDir = vWorldN;
    }
    Out.VertexColor = vVertexColor;
	
	
	//point lights
#ifdef INCLUDE_VERTEX_LIGHTING
    Out.VertexLighting = calculate_point_lights_diffuse(vWorldPos, vWorldN, true, true);
#endif
	
	
#ifndef USE_LIGHTING_PASS 
    const int effective_light_index = iLightIndices[0];
    float3 point_to_light = vLightPosDir[effective_light_index] - vWorldPos.xyz;
    float LD = dot(point_to_light, point_to_light);
    Out.PointLightDir.a = saturate(1.0f / LD); //prevent bloom for 1 meters
	
    if (use_bumpmap)
    {
        Out.PointLightDir.xyz = mul(TBNMatrix, normalize(point_to_light));
    }
    else
    {
        Out.PointLightDir.xyz = normalize(point_to_light);
    }
#endif
	
	
    if (use_bumpmap)
    {
        Out.ViewDir = mul(TBNMatrix, normalize(vCameraPos.xyz - vWorldPos.xyz));
    }
    else
    {
        Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz);
    }
	
    float3 P = mul(matWorldView, vObjectPos); //position in view space
	
	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}
// Face Mark7
float3 SSS(float3 lightDir, float3 viewDir, float3 normal, float3 diffuseColor, float scale)
{
    float3 halfDir = normalize(lightDir + viewDir);
    float sssWeight = pow(1.0 - max(dot(halfDir, normal), 0.0), scale);
    return diffuseColor * sssWeight;
}

PS_OUTPUT ps_main_standart_face_mod(VS_OUTPUT_STANDART In, uniform const int PcfMode,
										uniform const bool use_bumpmap, uniform const bool use_ps2a)
{
    PS_OUTPUT Output;

    float4 total_light = vAmbientColor; //In.LightAmbient;

    float3 normal;
	
    if (use_bumpmap)
    {
        float3 tex1_norm, tex2_norm;
        tex1_norm = tex2D(NormalTextureSampler, In.Tex0);
		
        if (use_ps2a)
        { //add old's normal map with ps2a 
            tex2_norm = tex2D(SpecularTextureSampler, In.Tex0);
            normal = lerp(tex1_norm, tex2_norm, In.VertexColor.a); // blend normals different?
            normal = 2.0f * normal - 1.0f;
            normal = normalize(normal);
        }
        else
        {
            normal = (2 * tex1_norm - 1);
        }
    }
    else
    {
        normal = In.SunLightDir.xyz;
    }
	
    float sun_amount = 1;
    if (PcfMode != PCF_NONE)
    {
        sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }

    float NdotL_Sun = face_NdotL(In.SunLightDir.xyz, normal.xyz);
    float NdotL_Sky = face_NdotL(In.SkyLightDir.xyz, normal.xyz);

// Calculate Fresnel term using Schlick's approximation
    float fresnel = pow(1.0 - dot(In.ViewDir, normal), 5.0);
    fresnel = lerp(0.04, 1.0, fresnel); // Assuming 4% reflectivity at normal incidence
		
	
    float4 tex1_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 tex2_col = tex2D(Diffuse2Sampler, In.Tex0);
    //if (use_bumpmap)
    //{
    // Using a simple BRDF for specular (could be replaced with more complex model)
    float roughness = normal.x * 0.1; // Your roughness parameter
    float metallic = 0; // Your metallic parameter
    float3 brdfSpecular = GGX_Specular(In.SunLightDir.xyz, In.ViewDir, normal, roughness, metallic);

    total_light.rgb += NdotL_Sun * (sun_amount * 0.5) * vSunColor.rgb * (1.0 - metallic) + brdfSpecular;
    if (use_ps2a)
    {
        total_light += NdotL_Sky * vSkyLightColor * (1.0 - metallic);
    }
    //}
    //else
    //{
    //    total_light += NdotL_Sun * sun_amount * vSunColor;
    //    if (use_ps2a)
    //    {
    //        total_light += NdotL_Sky * vSkyLightColor;
    //    }
    //}
	
	
	// Mark7 SSS
    float3 viewDirection = normalize(In.ViewDir);
    float3 sssColor = SSS(normalize(In.SunLightDir), viewDirection, normalize(normal), tex2_col.rgb, 0.7);
    Output.RGBColor.rgb += sssColor;
	
    float3 point_lighting = 0;
#ifndef USE_LIGHTING_PASS 
    float light_atten = In.PointLightDir.a * 0.2f;
    const int effective_light_index = iLightIndices[0];
    point_lighting += light_atten * face_NdotL(In.PointLightDir.xyz, normal.xyz) * vLightDiffuse[effective_light_index];
#endif
	
#ifdef INCLUDE_VERTEX_LIGHTING
    if (use_ps2a)
    {
        point_lighting += In.VertexLighting;
    }
#endif
    total_light.rgb += point_lighting;

    if (PcfMode != PCF_NONE)
        Output.RGBColor.rgb = total_light.rgb;
    else
        Output.RGBColor.rgb = min(total_light.rgb, 2.0f);
		
	// Output.RGBColor.rgb = total_light.rgb;
	
	
    float4 tex_col = lerp(tex1_col, tex2_col, In.VertexColor.a);

    Output.RGBColor.rgb += sssColor * 0.025f;
	INPUT_TEX_GAMMA(tex_col.rgb);
	
    Output.RGBColor *= tex_col;
    Output.RGBColor.rgb *= (In.VertexColor.rgb * vMaterialColor.rgb);
	
    if (use_ps2a)
    {
        float fSpecular = 0;
		
        float4 specColor = vSpecularColor * vSunColor; //float4(1.0, 0.9, 0.8, 1.0) * 2;//
        if (false)
        { //we dont have specularmap yet-> used for normalmap2
            specColor *= tex2D(SpecularTextureSampler, In.Tex0);
        }
		
        float3 halfwayDir = normalize(In.ViewDir + In.SunLightDir);
        float specular = pow(saturate(dot(normal, halfwayDir)), fMaterialPower);
		
        float fresnel = pow(1.0 - dot(halfwayDir, normal), 5.0);
        Output.RGBColor += specular *= fresnel;
    }


	//Output.RGBColor = saturate(Output.RGBColor);
    Output.RGBColor.rgb = saturate(OUTPUT_GAMMA(Output.RGBColor.rgb)); //do not bloom!
    Output.RGBColor.a = vMaterialColor.a;
	////
	//Output.RGBColor = face_NdotL(In.PointLightDir.xyz, normal.xyz) * vLightDiffuse[effective_light_index] * In.PointLightDir.a;
	//Output.RGBColor.rgb += In.VertexLighting;
	//Output.RGBColor.a = 1;

    return Output;
}

////////////////////
technique face_shader_high
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart_face_mod(PCF_NONE, true);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_NONE, true, false);
    }
}
technique face_shader_high_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart_face_mod(PCF_DEFAULT, true);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_DEFAULT, true, false);

    }
}
technique face_shader_high_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_main_standart_face_mod(PCF_NVIDIA, true);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_NVIDIA, true, false);
    }
}

DEFINE_LIGHTING_TECHNIQUE(face_shader_high, 0, 1, 0, 0, 0)    	

////////////////////
technique faceshader_high_specular
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart_face_mod(PCF_NONE, true);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_NONE, true, true);
    }
}
technique faceshader_high_specular_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart_face_mod(PCF_DEFAULT, true);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_DEFAULT, true, true);

    }
}
technique faceshader_high_specular_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_main_standart_face_mod(PCF_NVIDIA, true);
        PixelShader = compile ps_2_a ps_main_standart_face_mod(PCF_NVIDIA, true, true);
    }
}

DEFINE_LIGHTING_TECHNIQUE(faceshader_high_specular, 0, 1, 0, 0, 0)    	


////////////////////
technique faceshader_simple
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart_face_mod(PCF_NONE, false);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_NONE, false, false);
    }
}
technique faceshader_simple_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_standart_face_mod(PCF_DEFAULT, false);
        PixelShader = compile PS_2_X ps_main_standart_face_mod(PCF_DEFAULT, false, false);

    }
}
technique faceshader_simple_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_main_standart_face_mod(PCF_NVIDIA, false);
        PixelShader = compile ps_2_a ps_main_standart_face_mod(PCF_NVIDIA, false, false);
    }
}

DEFINE_LIGHTING_TECHNIQUE(faceshader_high_specular, 0, 1, 0, 0, 0)    	

////////////////////////////////////////
VS_OUTPUT vs_main_skin(float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR, float4 vBlendWeights : BLENDWEIGHT, float4 vBlendIndices : BLENDINDICES, uniform const int PcfMode)
{
	INITIALIZE_OUTPUT(VS_OUTPUT, Out);

    float4 vObjectPos = skinning_deform(vPosition, vBlendWeights, vBlendIndices);
	
    float3 vObjectN = normalize(mul((float3x3) matWorldArray[vBlendIndices.x], vNormal) * vBlendWeights.x
								+ mul((float3x3) matWorldArray[vBlendIndices.y], vNormal) * vBlendWeights.y
								+ mul((float3x3) matWorldArray[vBlendIndices.z], vNormal) * vBlendWeights.z
								+ mul((float3x3) matWorldArray[vBlendIndices.w], vNormal) * vBlendWeights.w);

    float4 vWorldPos = mul(matWorld, vObjectPos);
    Out.Pos = mul(matWorldViewProj, vObjectPos);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vObjectN)); //normal in world space

    float3 P = mul(matView, vWorldPos); //position in view space

    Out.Tex0 = tc;

	//light computation
    Out.Color = vAmbientColor;
	//   Out.Color.rgb *= gradient_factor * (gradient_offset + vWorldN.z);

	//directional lights, compute diffuse color
    Out.Color += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
#ifndef USE_LIGHTING_PASS
    Out.Color += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif

	//apply material color
    Out.Color *= vMaterialColor * vColor;
    Out.Color = min(1, Out.Color);

	//shadow mapping variables
    float wNdotSun = saturate(dot(vWorldN, -vSunDir));
    Out.SunLight = wNdotSun * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

technique skin_diffuse
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_skin(PCF_NONE);
        PixelShader = ps_main_compiled_PCF_NONE;
    }
}
technique skin_diffuse_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_skin(PCF_DEFAULT);
        PixelShader = ps_main_compiled_PCF_DEFAULT;
    }
}
technique skin_diffuse_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_main_skin(PCF_NVIDIA);
        PixelShader = ps_main_compiled_PCF_NVIDIA;
    }
}

DEFINE_LIGHTING_TECHNIQUE(skin_diffuse, 0, 0, 1, 0, 0)    	


#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef FLORA_SHADERS

struct VS_OUTPUT_FLORA
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
};

struct VS_OUTPUT_FLORA_NO_SHADOW
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float Fog : FOG;
};

VS_OUTPUT_FLORA vs_flora(uniform const int PcfMode, float4 vPosition : POSITION, float4 vColor : COLOR0, float2 tc : TEXCOORD0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_FLORA, Out);

    //Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);

    //if (is_windy_trunk)
    //{
    //    float height = vPosition.y; 
    //    float maxTreeHeight = height * 10.0;
    //float3 new_position = calculate_wind_effect(1, height, vPosition.xyz, vWorldPos.xyz,maxTreeHeight);
    //    Out.Pos = mul(matWorldViewProj, lerp(float4(new_position, 1.0), vPosition, 0.8));
    //}
    //else
    //{
    Out.Pos = mul(matWorldViewProj, vPosition);
    //}

    Out.Tex0 = tc;
	//   Out.Color = vColor * vMaterialColor;
    Out.Color = vColor * (vAmbientColor + vSunColor * 0.06f); //add some sun color to simulate sun passing through leaves.
    Out.Color.a *= vMaterialColor.a;

	//   Out.Color = vColor * vMaterialColor * (vAmbientColor + vSunColor * 0.15f);
	//shadow mapping variables
    Out.SunLight = (vSunColor * 0.34f) * vMaterialColor * vColor;

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
    }
	//shadow mapping variables end
	
	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}


VS_OUTPUT_FLORA vs_flora_Instanced(uniform const int PcfMode, float4 vPosition : POSITION, float4 vColor : COLOR0, float2 tc : TEXCOORD0,
								   //instance data:
								   float3 vInstanceData0 : TEXCOORD1,
								   float3 vInstanceData1 : TEXCOORD2,
								   float3 vInstanceData2 : TEXCOORD3,
								   float3 vInstanceData3 : TEXCOORD4)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_FLORA, Out);
	
    float4x4 matWorldOfInstance = build_instance_frame_matrix(vInstanceData0, vInstanceData1, vInstanceData2, vInstanceData3);

    float4 vWorldPos = (float4) mul(matWorldOfInstance, vPosition);
    Out.Pos = mul(matViewProj, vWorldPos);

    Out.Tex0 = tc;
	//   Out.Color = vColor * vMaterialColor;
    Out.Color = vColor * (vAmbientColor + vSunColor * 0.06f); //add some sun color to simulate sun passing through leaves.
    Out.Color.a *= vMaterialColor.a;

	//   Out.Color = vColor * vMaterialColor * (vAmbientColor + vSunColor * 0.15f);
	//shadow mapping variables
    Out.SunLight = (vSunColor * 0.34f) * vMaterialColor * vColor;

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
    }
	//shadow mapping variables end
	
	//apply fog
    float3 P = mul(matView, vWorldPos); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

PS_OUTPUT ps_flora(VS_OUTPUT_FLORA In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    clip(tex_col.a - 0.05f);
	
	INPUT_TEX_GAMMA(tex_col.rgb);


    if (PcfMode != PCF_NONE)
    {
        float sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        Output.RGBColor = tex_col * ((In.Color + In.SunLight * sun_amount));
    }
    else
    {
        Output.RGBColor = tex_col * ((In.Color + In.SunLight));
    }

	//Output.RGBColor = tex_col * In.Color;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    return Output;
}

VS_OUTPUT_FLORA_NO_SHADOW vs_flora_no_shadow(float4 vPosition : POSITION, float4 vColor : COLOR0, float2 tc : TEXCOORD0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_FLORA_NO_SHADOW, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

PS_OUTPUT ps_flora_no_shadow(VS_OUTPUT_FLORA_NO_SHADOW In)
{
    PS_OUTPUT Output;
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    clip(tex_col.a - 0.05f);
	
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor = tex_col * In.Color;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    return Output;
}

VS_OUTPUT_FLORA vs_grass(uniform const int PcfMode, float4 vPosition : POSITION, float4 vColor : COLOR0, float2 tc : TEXCOORD0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_FLORA, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;
    Out.Color = vColor * vAmbientColor;

	//shadow mapping variables
    if (PcfMode != PCF_NONE)
    {
        Out.SunLight = (vSunColor * 0.55f) * vMaterialColor * vColor;
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
    }
    else
    {
        Out.SunLight = vSunColor * 0.5f * vColor;
    }
	//shadow mapping variables end
	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    Out.Color.a = min(1.0f, (1.0f - (d / 50.0f)) * 2.0f);

    return Out;
}

PS_OUTPUT ps_grass(VS_OUTPUT_FLORA In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
    float4 tex_col = tex2D(GrassTextureSampler, In.Tex0);
	
	//    clip(tex_col.a - 0.05f);
    clip(tex_col.a - 0.1f);
	
	INPUT_TEX_GAMMA(tex_col.rgb);

    if ((PcfMode != PCF_NONE))
    {
        float sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        Output.RGBColor = tex_col * ((In.Color + In.SunLight * sun_amount));
    }
    else
    {
        Output.RGBColor = tex_col * ((In.Color + In.SunLight));
    }

	//    	Output.RGBColor = tex_col * (In.Color + In.SunLight);
	//	Output.RGBColor = tex_col * In.Color;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    return Output;
}

VS_OUTPUT_FLORA_NO_SHADOW vs_grass_no_shadow(float4 vPosition : POSITION, float4 vColor : COLOR0, float2 tc : TEXCOORD0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_FLORA_NO_SHADOW, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    Out.Color.a = min(1.0f, (1.0f - (d / 50.0f)) * 2.0f);

    return Out;
}

PS_OUTPUT ps_grass_no_shadow(VS_OUTPUT_FLORA_NO_SHADOW In)
{
    PS_OUTPUT Output;
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	
    clip(tex_col.a - 0.1f);
	
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor = tex_col * In.Color;
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    return Output;
}

DEFINE_TECHNIQUES(flora, vs_flora, ps_flora)

technique flora_PRESHADED
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_flora_no_shadow();
        PixelShader = compile PS_2_X ps_flora_no_shadow();
    }
}
DEFINE_LIGHTING_TECHNIQUE(flora, 0, 0, 0, 0, 0)


DEFINE_TECHNIQUES(flora_Instanced, vs_flora_Instanced, ps_flora)


technique grass_no_shadow
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_grass_no_shadow();
        PixelShader = compile PS_2_X ps_grass_no_shadow();
    }
}

DEFINE_TECHNIQUES(grass, vs_grass, ps_grass)

technique grass_PRESHADED
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_grass_no_shadow();
        PixelShader = compile PS_2_X ps_grass_no_shadow();
    }
}
DEFINE_LIGHTING_TECHNIQUE(grass, 0, 0, 0, 0, 0)    
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef MAP_SHADERS

//---
struct VS_OUTPUT_MAP
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
    float Fog : FOG;
	
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};
VS_OUTPUT_MAP vs_main_map(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL,
							float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_MAP, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space


    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;

    if (true /*_UseSecondLight*/)
    {
        diffuse_light += vLightColor;
    }

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
    float wNdotSun = saturate(dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
    Out.ViewDir = normalize(vCameraPos - vWorldPos);
    Out.WorldNormal = vWorldN;
	
	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}
PS_OUTPUT ps_main_map(VS_OUTPUT_MAP In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);
	
    float sun_amount = 1;
    if ((PcfMode != PCF_NONE))
    {
        sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }
    Output.RGBColor = tex_col * ((In.Color + In.SunLight * sun_amount));
	
	
	//add fresnel term
	{
        float fresnel = 1 - (saturate(dot(normalize(In.ViewDir), normalize(In.WorldNormal))));
        fresnel *= fresnel;
        Output.RGBColor.rgb *= max(0.6, fresnel + 0.1);
    }
	// gamma correct
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    return Output;
}

DEFINE_TECHNIQUES(diffuse_map, vs_main_map, ps_main_map) //diffuse shader with fresnel effect

//---
struct VS_OUTPUT_MAP_BUMP
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
	//float4 SunLight				: TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
    float Fog : FOG;
	
    float3 SunLightDir : TEXCOORD4;
    float3 SkyLightDir : TEXCOORD5;
	
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};
VS_OUTPUT_MAP_BUMP vs_main_map_bump(uniform const int PcfMode, float4 vPosition : POSITION,
									float3 vNormal : NORMAL, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL,
									float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_MAP_BUMP, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
	
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space
    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);
	
    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;

    if (true /*_UseSecondLight*/)
    {
        diffuse_light += vLightColor;
    }

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;
	
	//point lights
#ifndef USE_LIGHTING_PASS
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
#endif
	
	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables

	//move sun light to pixel shader
	//float wNdotSun = saturate(dot(vWorldN, -vSunDir));
	//Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    Out.SunLightDir = normalize(mul(TBNMatrix, -vSunDir));
	
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
    Out.ViewDir = normalize(vCameraPos - vWorldPos);
    Out.WorldNormal = vWorldN;
	
	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}
PS_OUTPUT ps_main_map_bump(VS_OUTPUT_MAP_BUMP In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);
	
	
    float3 normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0 * map_normal_detail_factor).rgb - 1.0f);
	
	//float wNdotSun = saturate(dot(vWorldN, -vSunDir));
	//Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    float4 In_SunLight = saturate(dot(normal, In.SunLightDir)) * vSunColor * vMaterialColor; // * vColor;  vertex color needed??
	
    float sun_amount = 1;
    if ((PcfMode != PCF_NONE))
    {
        sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }
    Output.RGBColor = tex_col * ((In.Color + In_SunLight * sun_amount));
	
	
	//add fresnel term
	{
        float fresnel = 1 - (saturate(dot(normalize(In.ViewDir), normalize(In.WorldNormal))));
        fresnel *= fresnel;
        Output.RGBColor.rgb *= max(0.6, fresnel + 0.1);
    }
	// gamma correct
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
    //Output.RGBColor.rgb = float4(0, 0, 0, 1);
    //Output.RGBColor.r *= tex_col.a;
    return Output;
}

DEFINE_TECHNIQUES(diffuse_map_bump, vs_main_map_bump, ps_main_map_bump) //diffuse shader with fresnel effect + bumpmapping(if shader_quality medium)..

//---
struct VS_OUTPUT_MAP_MOUNTAIN
{
    float4 Pos : POSITION;
    float Fog : FOG;
	
    float4 Color : COLOR0;
    float3 Tex0 : TEXCOORD0;
    float4 SunLight : TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
	
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};

VS_OUTPUT_MAP_MOUNTAIN vs_map_mountain(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL,
										float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_MAP_MOUNTAIN, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0.xy = tc;
    Out.Tex0.z = /*saturate*/(0.7f * (vWorldPos.z - 3.2f));

    float4 diffuse_light = vAmbientColor;
    if (true /*_UseSecondLight*/)
    {
        diffuse_light += vLightColor;
    }

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
    float wNdotSun = saturate(dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	
    Out.ViewDir = normalize(vCameraPos - vWorldPos);
    Out.WorldNormal = vWorldN;
	
	
	//apply fog
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}

PS_OUTPUT ps_map_mountain(VS_OUTPUT_MAP_MOUNTAIN In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0.xy);
	INPUT_TEX_GAMMA(tex_col.rgb);
	
    tex_col.rgb += saturate(In.Tex0.z * (tex_col.a) - 3.2f);
    tex_col.a = 1.0f;
	
    if ((PcfMode != PCF_NONE))
    {
        float sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        Output.RGBColor = saturate(tex_col) * ((In.Color + In.SunLight * sun_amount));
    }
    else
    {
        Output.RGBColor = saturate(tex_col) * (In.Color + In.SunLight);
    }
	
	{
        float fresnel = 1 - (saturate(dot(In.ViewDir, In.WorldNormal)));
	//	fresnel *= fresnel;
        Output.RGBColor.rgb *= max(0.6, fresnel + 0.1);
    }
	
	
	// gamma correct
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
	
    return Output;
}

DEFINE_TECHNIQUES(map_mountain, vs_map_mountain, ps_map_mountain)


//---
struct VS_OUTPUT_MAP_MOUNTAIN_BUMP
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float3 Tex0 : TEXCOORD0;
	//float4 SunLight				: TEXCOORD1;
    float4 ShadowTexCoord : TEXCOORD2;
    float2 ShadowTexelPos : TEXCOORD3;
    float Fog : FOG;
	
    float3 SunLightDir : TEXCOORD4;
    float3 SkyLightDir : TEXCOORD5;
	
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};
VS_OUTPUT_MAP_MOUNTAIN_BUMP vs_map_mountain_bump(uniform const int PcfMode, float4 vPosition : POSITION,
												float3 vNormal : NORMAL, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL,
												float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_MAP_MOUNTAIN_BUMP, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space
    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0.xy = tc;
    Out.Tex0.z = /*saturate*/(0.7f * (vWorldPos.z - 3.2f));

    float4 diffuse_light = vAmbientColor;
    if (true /*_UseSecondLight*/)
    {
        diffuse_light += vLightColor;
    }

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
	//float wNdotSun = saturate(dot(vWorldN, -vSunDir));
	//Out.SunLight = (wNdotSun) * vSunColor;
    Out.SunLightDir = normalize(mul(TBNMatrix, -vSunDir));
			
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	
    Out.ViewDir = normalize(vCameraPos - vWorldPos);
    Out.WorldNormal = vWorldN;
	
	
	//apply fog
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}
PS_OUTPUT ps_map_mountain_bump(VS_OUTPUT_MAP_MOUNTAIN_BUMP In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 sample_col = tex2D(MeshTextureSampler, In.Tex0.xy);
	
	INPUT_TEX_GAMMA(sample_col.rgb);
    float4 tex_col = sample_col;
	
    tex_col.rgb += saturate(In.Tex0.z * (sample_col.a) - 3.2f);
    tex_col.a = 1.0f;
	/*    
	float snow = In.Tex0.z * (0.1f + sample_col.a) - 3.2f;
	if (snow > 0.5f)
	{
		tex_col = float4(1.0f,1.0f,1.0f,1.0f);
	}
*/    

	
    float3 normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0 * map_normal_detail_factor).rgb - 1.0f);
	
	//float wNdotSun = saturate(dot(vWorldN, -vSunDir));
	//Out.SunLight = (wNdotSun) * vSunColor;
    float4 In_SunLight = saturate(dot(normal, In.SunLightDir)) * vSunColor;
	

    if ((PcfMode != PCF_NONE))
    {
        float sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
		//		sun_amount *= sun_amount;
        Output.RGBColor = saturate(tex_col) * ((In.Color + In_SunLight * sun_amount));
    }
    else
    {
        Output.RGBColor = saturate(tex_col) * (In.Color + In_SunLight);
    }
	
	{
        float fresnel = 1 - (saturate(dot(In.ViewDir, In.WorldNormal)));
	//	fresnel *= fresnel;
        Output.RGBColor.rgb *= max(0.6, fresnel + 0.1);
    }
	
	
	// gamma correct
	OUTPUT_GAMMA(Output.RGBColor.rgb);
	
	
    return Output;
}

DEFINE_TECHNIQUES(map_mountain_bump, vs_map_mountain_bump, ps_map_mountain_bump)

//---
  //float2 worldpos = vWorldPos.xy ;
  //  worldpos.x /= 762.25;
  //  worldpos.y /= 711.2;
  //  worldpos.x -= 0.57175;
  //  worldpos.y += 0.5936;
	
  //  worldpos.x *= 1.;
  //  worldpos.y *= -1.;
  //  //worldpos.y *= 1.003;
  //  //worldpos.x *= 1.003;
    
  //  //worldpos.x *= -1.;
  //  Out.WPos = worldpos;

struct VS_OUTPUT_MAP_WATER
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float3 LightDir : TEXCOORD1; //light direction for bump
    float3 CameraDir : TEXCOORD3; //camera direction for bump
    float4 PosWater : TEXCOORD4; //position according to the water camera
    float Fog : FOG;
    float2 WPos : TEXCOORD7;
};
VS_OUTPUT_MAP_WATER vs_map_water(uniform const bool reflections, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_MAP_WATER, Out);

    Out.Pos = mul(matWorldViewProj, vPosition);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    Out.Tex0 = tc - texture_offset.xy;

    //float2 worldpos = vWorldPos.xy / 748;
    //worldpos.x -= 0.470;
    //worldpos.y += 0.65;
    
    float2 worldpos = vWorldPos.xy;
    worldpos.x /= 762.25;
    worldpos.y /= 711.2;
    worldpos.x -= 0.57175;
    worldpos.y += 0.5936;
	
    worldpos.y *= -1;
    Out.WPos = worldpos;

    float4 diffuse_light = vAmbientColor + vLightColor;

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

    float wNdotSun = max(-0.0001f, dot(vWorldN, -vSunDir));
    diffuse_light += (wNdotSun) * vSunColor;

	//apply material color
	//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor) * diffuse_light;
	
	
    if (reflections)
    {
        float4 water_pos = mul(matWaterViewProj, vWorldPos);
        Out.PosWater.xy = (float2(water_pos.x, -water_pos.y) + water_pos.w) / 2;
        Out.PosWater.xy += (vDepthRT_HalfPixel_ViewportSizeInv.xy * water_pos.w);
        Out.PosWater.zw = water_pos.zw;
    }
	
	{
        float3 vWorldN = float3(0, 0, 1); //vNormal; //normalize(mul((float3x3)matWorld, vNormal)); //normal in world space
        float3 vWorld_tangent = float3(1, 0, 0); //normalize(mul((float3x3)matWorld, vTangent)); //normal in world space
        float3 vWorld_binormal = float3(0, 1, 0); //normalize(cross(vWorld_tangent, vNormal)); //normalize(mul((float3x3)matWorld, vBinormal)); //normal in world space

        float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

        float3 point_to_camera_normal = normalize(vCameraPos.xyz - vWorldPos.xyz);
        Out.CameraDir = mul(TBNMatrix, -point_to_camera_normal);
        Out.LightDir = mul(TBNMatrix, -vSunDir);
    }
    
	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
	
    return Out;
}
PS_OUTPUT ps_map_water(uniform const bool reflections, VS_OUTPUT_MAP_WATER In)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color;
    float4 mask = tex2D(SpecularTextureSampler, In.WPos);
	
	/////////////////////
//    const bool rgb_normalmap = false; //!apply_depth;
    float WaveScale1 = 10;
    float WaveScale2 = 15;
    float WaveScale3 = 8;
    float WaveOffset1 = 0;
    float WaveOffset2 = 64;
    //float WaveOffset3 = 0;
    float WaveStrength1 = 100; // Adjusted from 100 to 1
    float WaveStrength2 = 80; // Adjusted from 100 to 1

    float3 normal;
    float3 normalDistort;
    
    float noiseScale = 800;
    float noiseStrenght = 0.1;
       // Using the noise function to perturb UVs
    float noiseDist = noise(In.WPos, noiseScale) + ((1 - mask.a) * 0.3) + ((1 - In.Color.a) * 0.3);
    float2 disturbedUV1 = In.Tex0 * WaveScale1 + WaveOffset1 + noiseDist * noiseStrenght;
    float2 disturbedUV2 = In.Tex0 * WaveScale2 + WaveOffset2 + noiseDist * noiseStrenght;
// You can use different noise strengths or even different noise textures for each UV set
// if you want a more complex or layered noise effect.

// Now sample the normal texture with the disturbed UVs
    float2 normal1GA = tex2D(NormalTextureSampler, disturbedUV1).ga * 2.0 - 1.0;
    float2 normal2GA = tex2D(NormalTextureSampler, disturbedUV2).ga * 2.0 - 1.0;
        //float2 normal3GA = tex2D(NormalTextureSampler, In.Tex0 * WaveScale3 + WaveOffset3).ga * 2.0 - 1.0;

// Reconstruct the Z component from the X and Y
    float normal1Z = sqrt(1.0f - clamp(dot(normal1GA, normal1GA), 0.0f, 1.0f));
    float normal2Z = sqrt(1.0f - clamp(dot(normal2GA, normal2GA), 0.0f, 1.0f));
        //float normal3Z = sqrt(1.0f - clamp(dot(normal3GA, normal3GA), 0.0f, 1.0f));

// Create the normal vectors using the X and Y from the texture, and the reconstructed Z
    float3 normal1 = float3(normal1GA.y, normal1GA.x, normal1Z);
    float3 normal2 = float3(normal2GA.y, normal2GA.x, normal2Z);
        //normalDistort = float3(normal3GA.y, normal3GA.x, normal3Z);
  
// Blend the normals
    normal = normalize(normal1 * WaveStrength1 + normal2 * WaveStrength2);
	
    float mainScale = 2;
    float mainOffset = 0;
    float mainNoiseStrenght = 0.5;
    float2 disturbedUVMain = In.Tex0 * mainScale + mainOffset + noise(In.Tex0, 8) * mainNoiseStrenght;
    
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);
    
    //float3 normal;
    //normal.xy = (2.0f * tex2D(NormalTextureSampler, In.Tex0 * 8).ag - 1.0f);
    //normal.z = sqrt(1.0f - dot(normal.xy, normal.xy));
	
    float NdotL = saturate(dot(normal, In.LightDir));
    float3 vView = normalize(In.CameraDir);

	// Fresnel term
    //float fresnel = 1 - (saturate(dot(vView, normal)));
    //fresnel = 0.0204f + 0.9796 * (fresnel * fresnel * fresnel * fresnel * fresnel);
    //Output.RGBColor.rgb += fresnel * In.Color.rgb;
	/////////////////////


    
    float3 riverColor = lerp(float3(0.20, 0.55, 0.60), tex_col.rgb, 0.3);
    float alpha = pow(1 - mask.a, 1.7);
    float3 nmCol = pow(float3(normal.r, normal.r, normal.r), 0.1);
    //Output.RGBColor.rgb = riverColor * alpha;
    float3 final_color = OverlayBlendColor(pow(riverColor, 2), nmCol) * alpha;
	
    float fresnel = ((SchlickFresnel(vView, pow(nmCol, 2), 0.1, 5) * In.Color.rgb) * mask.a);
    Output.RGBColor.rgb = final_color * (fresnel * 2) + (final_color * 0.35);
    float refFoam = pow(1 - clamp((nmCol * (pow(nmCol, 4) * 0.5)), 0, 1), 10);
    //Output.RGBColor.rgb += pow(1 - clamp((nmCol * (pow(nmCol, 4) * 0.5)), 0, 1), 50) * riverColor;
    
    		
  //  if (reflections)
  //  {
    //Output.RGBColor.rgb = w.b;
    
    In.PosWater.xy += 0.35f * normal.xy;
    float4 tex = tex2Dproj(ReflectionTextureSampler, In.PosWater);
		INPUT_OUTPUT_GAMMA(tex.rgb);
    tex.rgb = min(tex.rgb, 4.0f);
		
    float3 refColor = (NdotL * lerp(tex_col.rgb, tex.rgb, reflection_factor));
    Output.RGBColor.rgb += refFoam * refColor;
  //  }
  //  else
  //  {
  //      Output.RGBColor.rgb *= tex_col.rgb;
  //  }
    
    OUTPUT_GAMMA(Output.RGBColor.rgb); //0.5 * normal + 0.5; //
    //Output.RGBColor.rgb = In.Color.rgb;
    Output.RGBColor.a = In.Color.a * tex_col.a;
	
    //    // Foam Edge Calculations
//    float depth = tex2Dproj(DepthTextureSampler, In.projCoord).r;
//    float depthDiff = depth - In.Depth;
//    float depthRange = 0.001; // Depth range for transition
//    float foamEdge = 1.0 - smoothstep(0.0, depthRange, depthDiff);
//    // Use the noise to modulate the foam edge
//    float noiseStrength = 0.65; // How much the noise affects the foam
//    foamEdge += noiseStrength * (noise(In.Tex0, 2048).x * 2.0 - 1.0) * foamEdge;
//    float foamMultiplier = 6.75;
//// Clamp foamEdge to [0, 1]
//    foamEdge = clamp(foamEdge, 0.0, 1.0) * foamMultiplier;
    
  
    return Output;

}

technique map_water
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_map_water(false);
        PixelShader = compile PS_2_X ps_map_water(false);
    }
}
technique map_water_high
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_map_water(true);
        PixelShader = compile PS_2_X ps_map_water(true);
    }
}
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef SOFT_PARTICLE_SHADERS
struct VS_DEPTHED_FLARE
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float Fog : FOG;
	
    float4 projCoord : TEXCOORD1;
    float Depth : TEXCOORD2;
};

VS_DEPTHED_FLARE vs_main_depthed_flare(float4 vPosition : POSITION, float4 vColor : COLOR, float2 tc : TEXCOORD0)
{
    VS_DEPTHED_FLARE Out;

    Out.Pos = mul(matWorldViewProj, vPosition);


    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;
	
	
    if (use_depth_effects)
    {
        Out.projCoord.xy = (float2(Out.Pos.x, -Out.Pos.y) + Out.Pos.w) / 2;
        Out.projCoord.xy += (vDepthRT_HalfPixel_ViewportSizeInv.xy * Out.Pos.w);
        Out.projCoord.zw = Out.Pos.zw;
        Out.Depth = Out.Pos.z * far_clip_Inv;
    }

	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

// Improved soft particles Mark7
PS_OUTPUT ps_main_depthed_flare(VS_DEPTHED_FLARE In, uniform const bool sun_like, uniform const bool blend_adding)
{
    PS_OUTPUT Output;
    Output.RGBColor = In.Color * tex2D(MeshTextureSampler, In.Tex0); // Texture color blending

    // Gamma correction if not blending
    if (!blend_adding)
    {
        OUTPUT_GAMMA(Output.RGBColor.rgb);
    }
    
    if (use_depth_effects)
    {
        float sceneDepth = tex2Dproj(DepthTextureSampler, In.projCoord).r;
        float particleDepth = In.Depth;
        
        // Improved soft edge calculation
        float SoftEdgeIntensity = 0.5;
        float depthDifference = sceneDepth - particleDepth;
        float softEdgeFactor = saturate(1.0f - depthDifference * SoftEdgeIntensity);

        // Optional: Sun-like glow effect
        if (sun_like)
        {
            // Add sun-like glow effect here
            // E.g., based on angle to the camera, distance, etc.
        }

        // Blend mode handling
        if (blend_adding)
        {
            Output.RGBColor.rgb *= softEdgeFactor;
        }
        else
        {
            Output.RGBColor.a *= softEdgeFactor;
        }
    }

    return Output;
}


VertexShader vs_main_depthed_flare_compiled = compile vs_2_0 vs_main_depthed_flare();

technique soft_sunflare
{
    pass P0
    {
        VertexShader = vs_main_depthed_flare_compiled;
        PixelShader = compile PS_2_X ps_main_depthed_flare(true, true);
    }
}


technique soft_particle_add
{
    pass P0
    {
        VertexShader = vs_main_depthed_flare_compiled;
        PixelShader = compile PS_2_X ps_main_depthed_flare(false, true);
    }
}

technique soft_particle_modulate
{
    pass P0
    {
        VertexShader = vs_main_depthed_flare_compiled;
        PixelShader = compile PS_2_X ps_main_depthed_flare(false, false);
    }
}
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef OCEAN_SHADERS

struct VS_OUTPUT_OCEAN
{
    float4 Pos : POSITION;
    float2 Tex0 : TEXCOORD0;
    float3 LightDir : TEXCOORD1;
    float4 LightDif : TEXCOORD2; //light diffuse for bump
    float3 CameraDir : TEXCOORD3;
    float4 PosWater : TEXCOORD4; //position according to the water camera
	
    float Fog : FOG;
};

inline float get_wave_height_temp(const float pos[2], const float coef, const float freq1, const float freq2, const float time)
{
    return coef * sin((pos[0] + pos[1]) * freq1 + time) * cos((pos[0] - pos[1]) * freq2 + (time + 4)); // + (coef * 0.05 * sin( (pos[0]*pos[1]) * (freq1 * 200 * time) + time));
}
VS_OUTPUT_OCEAN vs_main_ocean(float4 vPosition : POSITION, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_OCEAN Out = (VS_OUTPUT_OCEAN) 0;

    float4 vWorldPos = mul(matWorld, vPosition);
	
    float3 viewVec = vCameraPos.xyz - vWorldPos.xyz;
    float wave_distance_factor = (1.0f - saturate(length(viewVec) * 0.01)); //no wave after 100 meters
	
    float pos_vector[2] = { vWorldPos.x, vWorldPos.y };
    vWorldPos.z += get_wave_height_temp(pos_vector, debug_vector.z, debug_vector.x, debug_vector.y, time_var) * wave_distance_factor;

    Out.Pos = mul(matViewProj, vWorldPos);
	
    Out.PosWater = mul(matWaterViewProj, vWorldPos);

	
	//calculate new normal:
    float3 vNormal;
    if (wave_distance_factor > 0.0f)
    {
        float3 near_wave_heights[2];
        near_wave_heights[0].xy = vWorldPos.xy + float2(0.1f, 0.0f);
        near_wave_heights[1].xy = vWorldPos.xy + float2(0.0f, 1.0f);
		
        float pos_vector0[2] = { near_wave_heights[0].x, near_wave_heights[0].y };
        near_wave_heights[0].z = get_wave_height_temp(pos_vector0, debug_vector.z, debug_vector.x, debug_vector.y, time_var);
        float pos_vector1[2] = { near_wave_heights[1].x, near_wave_heights[1].y };
        near_wave_heights[1].z = get_wave_height_temp(pos_vector1, debug_vector.z, debug_vector.x, debug_vector.y, time_var);
		
        float3 v0 = normalize(near_wave_heights[0] - vWorldPos.xyz);
        float3 v1 = normalize(near_wave_heights[1] - vWorldPos.xyz);
		
        vNormal = cross(v0, v1);
    }
    else
    {
        vNormal = float3(0, 0, 1);
    }
	
	
    float3 vWorldN = vNormal; //float3(0,0,1); //normalize(mul((float3x3)matWorld, vNormal)); //normal in world space
    float3 vWorld_tangent = float3(1, 0, 0); //normalize(mul((float3x3)matWorld, vTangent)); //normal in world space
    float3 vWorld_binormal = normalize(cross(vWorld_tangent, vNormal)); //float3(0,1,0); //normalize(mul((float3x3)matWorld, vBinormal)); //normal in world space

    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    float3 point_to_camera_normal = normalize(vCameraPos.xyz - vWorldPos.xyz);
    Out.CameraDir = mul(TBNMatrix, point_to_camera_normal);

    Out.Tex0 = vWorldPos.xy; //tc + texture_offset.xy;	

    Out.LightDir = 0;
    Out.LightDif = vAmbientColor;

	//directional lights, compute diffuse color
    Out.LightDir += mul(TBNMatrix, -vSunDir);
    Out.LightDif += vSunColor;
    Out.LightDir = normalize(Out.LightDir);

	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
	
	
	//Out.PosWater.xyz = vNormal;
	
    return Out;
}
PS_OUTPUT ps_main_ocean(VS_OUTPUT_OCEAN In)
{
    PS_OUTPUT Output;
	
    const float texture_factor = 1.0f;
	
    float3 normal;
    normal.xy = (2.0f * tex2D(NormalTextureSampler, In.Tex0 * texture_factor).ag - 1.0f);
    normal.z = sqrt(1.0f - dot(normal.xy, normal.xy));
	
	
    static const float detail_factor = 16 * texture_factor;
    float3 detail_normal;
    detail_normal.xy = (2.0f * tex2D(NormalTextureSampler, In.Tex0 * detail_factor).ag - 1.0f);
    detail_normal.z = sqrt(1.0f - dot(normal.xy, normal.xy));
	
    float NdotL = saturate(dot(normal, In.LightDir));
	
	
    float4 tex = tex2D(ReflectionTextureSampler, 0.5f * normal.xy + float2(0.5f + 0.5f * (In.PosWater.x / In.PosWater.w), 0.5f - 0.5f * (In.PosWater.y / In.PosWater.w)));
	INPUT_OUTPUT_GAMMA(tex.rgb);
	
    Output.RGBColor = 0.01f * NdotL * In.LightDif;
	
    float3 vView = normalize(In.CameraDir);

	// Fresnel term
    float fresnel = 1 - (saturate(dot(vView, normal)));
    fresnel = 0.0204f + 0.9796 * (fresnel * fresnel * fresnel * fresnel * fresnel);

    Output.RGBColor.rgb += (tex.rgb * fresnel);
    Output.RGBColor.w = 1.0f - 0.3f * In.CameraDir.z;
	
    float3 cWaterColor = 2 * float3(20.0f / 255.0f, 45.0f / 255.0f, 100.0f / 255.0f) * vSunColor;
	//float3 cWaterColor = lerp( g_cUpWaterColor, g_cDownWaterColor,  saturate(dot(vView, normal)));
	
    float fog_fresnel_factor = saturate(dot(In.CameraDir, normal));
    fog_fresnel_factor *= fog_fresnel_factor;
    fog_fresnel_factor *= fog_fresnel_factor;
    Output.RGBColor.rgb += cWaterColor * fog_fresnel_factor;
	
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    Output.RGBColor.a = 1;
	
	
	//Output.RGBColor.rgb = dot(In.PosWater.xyz, float3(0,0,1));
	//Output.RGBColor.rgb = NdotL * vSunColor;
	
    return Output;
}
technique simple_ocean
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_main_ocean();
        PixelShader = compile PS_2_X ps_main_ocean();
    }
}
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef NEWTREE_SHADERS


VS_OUTPUT_FLORA vs_flora_billboards(uniform const int PcfMode,
												float4 vPosition : POSITION,
												float3 vNormal : NORMAL,
												float2 tc : TEXCOORD0,
												float4 vColor : COLOR0)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_FLORA, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
	
    float3 view_vec = (vCameraPos.xyz - vWorldPos.xyz);
    float dist_to_vertex = length(view_vec);
	
	/*if(dist_to_vertex < flora_detail_clip)
	{
		//Out.Pos = float4(0,0,-1,1);	// str: we can just blend but "more vs instruction" generates less pixel to process, so faster
		Out.Color.a = 0.0f;
		//return Out;
	}*/
	
    float alpha_val = saturate(0.5f + ((dist_to_vertex - flora_detail_fade) / flora_detail_fade_inv));
	 
	
    Out.Pos = mul(matWorldViewProj, vPosition);
	
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
	

    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;

	//directional lights, compute diffuse color
    diffuse_light += saturate(dot(vWorldN, -vSkyLightDir)) * vSkyLightColor;

	//point lights
    diffuse_light += calculate_point_lights_diffuse(vWorldPos, vWorldN, false, false);
	
	//apply material color
    Out.Color = (vMaterialColor * vColor * diffuse_light);
    Out.Color.a *= alpha_val;

	//shadow mapping variables
    float wNdotSun = saturate(dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
	//apply fog
    float3 P = mul(matWorldView, vPosition); //position in view space
    float d = length(P);

    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}


DEFINE_TECHNIQUES(tree_billboards_flora, vs_flora_billboards, ps_flora)

VS_OUTPUT_BUMP vs_main_bump_billboards(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL, float4 vVertexColor : COLOR0, float4 vPointLightDir : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_BUMP, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
	
    float3 view_vec = (vCameraPos.xyz - vWorldPos.xyz);
    float dist_to_vertex = length(view_vec);
	
    if (dist_to_vertex < flora_detail_clip)
    {
        Out.Pos = float4(0, 0, -1, 1); // str: we can just blend but "more vs instruction" generates less pixel to process, so faster
        return Out;
    }
	
    float alpha_val = saturate(0.5f + ((dist_to_vertex - flora_detail_fade) / flora_detail_fade_inv));
	 

    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Tex0 = tc;


    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }

    Out.SunLightDir = mul(TBNMatrix, -vSunDir);
    Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
	
#ifdef USE_LIGHTING_PASS
	Out.PointLightDir = vWorldPos;
#else
    Out.PointLightDir.rgb = 2.0f * vPointLightDir.rgb - 1.0f;
    Out.PointLightDir.a = vPointLightDir.a;
#endif
	
    Out.VertexColor = vVertexColor;
    Out.VertexColor.a *= alpha_val;
	
	//STR: note that these are not in TBN space.. (used for fresnel only..)
    Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz); //normalize(mul(TBNMatrix, (vCameraPos.xyz - vWorldPos.xyz) ));	// 
    Out.WorldNormal = vWorldN;

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

DEFINE_TECHNIQUES(tree_billboards_dot3_alpha, vs_main_bump_billboards, ps_main_bump_simple)


#endif

// Mark7 Shaders
struct VS_OUTPUT_GLASS_SHADER
{
    float4 Pos : POSITION;
    float4 Color : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float4 projCoord : TEXCOORD1;
    float3 SunLightDir : TEXCOORD2; //sun light dir in pixel coordinates
    float3 SunLight : TEXCOORD3; //sun light dir in pixel coordinates
    float4 ShadowTexCoord : TEXCOORD4; //sun light dir in pixel coordinates
    float2 ShadowTexelPos : TEXCOORD5; //sun light dir in pixel coordinates
    float Fog : FOG;
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};

VS_OUTPUT_GLASS_SHADER vs_glass(uniform const int PcfMode, uniform const bool UseSecondLight, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL)
{

    INITIALIZE_OUTPUT(VS_OUTPUT_GLASS_SHADER, Out);

    float4 vObjectPos = vPosition;
    float3 vObjectN = vNormal;

    Out.Pos = mul(matWorldViewProj, vObjectPos);

    float4 vWorldPos = (float4) mul(matWorld, vObjectPos);
    
    float3 vWorldN = normalize(mul((float3x3) matWorld, vObjectN)); //normal in world space
     float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal.xyz)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent.xyz)); //normal in world space
    float3 P = mul(matWorldView, vObjectPos); //position in view space

    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;
//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);
   
    if (UseSecondLight)
    {
        diffuse_light += vLightColor;
    }
   
	//directional lights, compute diffuse color
    float dp = dot(vWorldN, -vSkyLightDir);
    diffuse_light += max(0, dp) * vSkyLightColor;

	//point lights
    for (int j = 0; j < iLightPointCount; j++)
    {
        int i = iLightIndices[j];
        float3 point_to_light = vLightPosDir[i] - vWorldPos.xyz;
        float LD = length(point_to_light);
        float3 L = normalize(point_to_light);
        float wNdotL = dot(vWorldN, L);
		
        float fAtten = 1.0f / (LD * LD); // + 0.9f / (LD * LD);
		//compute diffuse color
        diffuse_light += max(0, wNdotL) * vLightDiffuse[i] * fAtten;
    }
   //apply material color
//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
    float wNdotSun = max(0.0f, dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
   
      
    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    Out.SunLightDir = mul(TBNMatrix, -vSunDir);
    
    //apply fog
    float d = length(P);
    Out.ViewDir = normalize(vCameraPos - vWorldPos);
    Out.WorldNormal = vWorldN;
    if (use_depth_effects)
    {
        Out.projCoord.xy = (float2(Out.Pos.x, -Out.Pos.y) + Out.Pos.w) / 2.0f;
        Out.projCoord.xy += (vDepthRT_HalfPixel_ViewportSizeInv.xy * Out.Pos.w);
        Out.projCoord.zw = Out.Pos.zw;
    }
  
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);
    return Out;
}

PS_OUTPUT ps_glass(VS_OUTPUT_GLASS_SHADER In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
    float3 glassColor = pow(float3(0.15, 0.4, 0.35), 2.5); // Slight blue tint
    float3 glassColor_light = pow(float3(0.2, 0.3, 0.6), 2); // Slight blue tint
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    float4 normal = tex2D(NormalTextureSampler, In.Tex0);
    INPUT_TEX_GAMMA(tex_col.rgb);
    //tex_col.rgb *= glassColor;
    float3 total_light = ((saturate(dot(In.SunLightDir.xyz, normal.xyz)) * (0.5))) * vSunColor;
    float fresnelPower = 2.0; // Adjust for desired effect
    float refractionFactor = 0.3; // Adjust for strength of refraction
    // Fresnel term calculation for reflectivity
    float fresnelTerm = pow(1.0 - max(dot(In.ViewDir, In.WorldNormal), 0.0), fresnelPower);
    float fresnel = fresnelTerm * tex_col.g;
    // Simple refraction logic (can be more complex with actual refraction maps)
    float2 skyUV = (normal.xy * pow(tex_col.a,3)) + float2(0.5f + 0.5f * (In.projCoord.x / In.projCoord.w), 0.5f - 0.5f * (In.projCoord.y / In.projCoord.w));
    float3 refractedColor = tex2D(ReflectionTextureSampler, skyUV);
    
    // Blend the texture color with the refracted color based on Fresnel term
    //Output.RGBColor = lerp(tex_col, refractedColor, fresnelTerm) * In.Color.r;
    float sun_amount = 1.0f;
    if ((PcfMode != PCF_NONE))
    {
        sun_amount = GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
    }
    
    float3 blendedColor = OverlayBlendColor(OverlayBlendColor(lerp(glassColor, glassColor_light, fresnel), lerp(refractedColor, 1, 0.1)) + ((pow(refractedColor, 4) * 10) * pow(tex_col.rgb, 2)), tex_col.rgb) + (fresnel * 0.025);
    Output.RGBColor.rgb = blendedColor * ((In.Color.rgb + In.SunLight * sun_amount));
    //Output.RGBColor.rgb = blendedColor;
    //Output.RGBColor = tex2Dproj(ReflectionTextureSampler, In.projCoord);
    Output.RGBColor.a = 1; // You might want to adjust alpha based on the angle

    OUTPUT_GAMMA(Output.RGBColor.rgb);
    return Output;
}

technique standartGlass
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_glass(PCF_NONE, true);
        PixelShader = compile PS_2_X ps_glass(PCF_NONE);
    }
}

technique standartGlass_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_glass(PCF_DEFAULT, true);
        PixelShader = compile PS_2_X ps_glass(PCF_DEFAULT);
    }
}

technique standartGlass_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_glass(PCF_NVIDIA, true);
        PixelShader = compile PS_2_X ps_glass(PCF_NVIDIA);
    }
}

struct VS_OUTPUT_BUMP_PARALLAX
{
    float4 Pos : POSITION;
    float4 VertexColor : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float3 SunLightDir : TEXCOORD1; //sun light dir in pixel coordinates
    float3 SkyLightDir : TEXCOORD2; //light diffuse for bump
    float4 PointLightDir : TEXCOORD3; //light ambient for bump
    float4 ShadowTexCoord : TEXCOORD4;
    float2 ShadowTexelPos : TEXCOORD5;
    float Fog : FOG;
	
    float3 ViewDir : TEXCOORD6;
    float4 WorldNormal : TEXCOORD7;
};
VS_OUTPUT_BUMP_PARALLAX vs_main_parallax(uniform const int PcfMode, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL, float4 vVertexColor : COLOR0, float4 vPointLightDir : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_BUMP_PARALLAX, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    
    Out.Pos = mul(matWorldViewProj, vPosition);
    Out.Tex0 = tc;
    
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }

    Out.SunLightDir = mul(TBNMatrix, -vSunDir);
    Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
	
#ifdef USE_LIGHTING_PASS
	Out.PointLightDir = vWorldPos;
#else
    Out.PointLightDir.rgb = 2.0f * vPointLightDir.rgb - 1.0f;
    Out.PointLightDir.a = vPointLightDir.a;
#endif
	
    Out.VertexColor = vVertexColor;
	
	//STR: note that these are not in TBN space.. (used for fresnel only..)
	Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz); //normalize(mul(TBNMatrix, (vCameraPos.xyz - vWorldPos.xyz) ));	// It now is in TBN space so that probabaly messed up the fresnel stuff somewhere else....
	Out.ViewDir = mul(TBNMatrix, Out.ViewDir);

	float d = length(P);
	Out.WorldNormal = float4(vWorldN,saturate(.75*d-0.5)); //to reduce silly stretching artefacts when up close (not too sure about this)
	
	//Out.WorldNormal = mul(TBNMatrix, Out.WorldNormal);

	//apply fog
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

PS_OUTPUT ps_main_parallax(VS_OUTPUT_BUMP_PARALLAX In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
	
    float parallaxScale = 0.075; // Control the depth effect
   
    float height = tex2D(SpecularTextureSampler, In.Tex0).g;

    float heightmap = 0.5 - height;
    In.Tex0 -= parallaxScale * heightmap * In.ViewDir.xy * In.WorldNormal.w;

    float3 normal = normalize((2.0f * tex2D(NormalTextureSampler, In.Tex0) - 1.0f));

   // Improved stepping with shadowing in parallax mapping
    float startoffset = parallaxScale * In.SunLightDir.xy / max(0.2, In.SunLightDir.z);
    int numsteps = 20; // Increased steps for smoother parallax effect
    float shadowStrength = 0.0f; // Shadow strength within the parallax mapping
    float step = heightmap * float(1.0 / numsteps);
    float currentHeight = 1.0f;
    //[unroll]
    for (int i = 0; i < numsteps; ++i)
    {
        if (PcfMode != PCF_NONE)
        {
            float stepHeight = 1.0f - i * step;
            float sampleHeight = tex2D(SpecularTextureSampler, In.Tex0 + startoffset * (stepHeight - heightmap)).g;
            if (stepHeight <= sampleHeight)
            {
                shadowStrength = max(shadowStrength, (sampleHeight - stepHeight) * 8); // Enhanced shadow strength
                break;
            }
        }
        else
        {
            break;
        }
    }
    if (saturate(currentHeight) < height)
        Output.RGBColor.rgb *= 0.5 * (height - heightmap) + 0.5;

    
    float AOMap = tex2D(SpecularTextureSampler, In.Tex0).b;
    float smoothnessMap = tex2D(SpecularTextureSampler, In.Tex0).r;
    float edgeMap = tex2D(SpecularTextureSampler, In.Tex0).a;
    float edgeEnhancement = 1 + pow(edgeMap,3) * 2; // Increase 0.5 to make edges more pronounced
    float4 sunCol = vSunColor * edgeEnhancement; // Increase 0.5 to make edges more pronounced
    float4 total_light = vAmbientColor * edgeEnhancement; //In.LightAmbient;
    
	/*
	const bool use_detail_normalmap = debug_vector.z > 1.0f;
	if(use_detail_normalmap)
	{
		float3 detail_normal = tex2D(Diffuse2Sampler, In.Tex0*debug_vector.y).rgb;
		//normal = lerp(normal, detail_normal, debug_vector.z);
		//normal = normalize(normal);
		
		float3x3 normal_frame; 
		normal_frame[2] = normal;
		normal_frame[1] = float3(0,1,0);
		normal_frame[0] = cross(normal_frame[1], normal_frame[2]);
		//normal_frame[0] = normalize(normal_frame[0]);
		normal_frame[1] = cross(normal_frame[2], normal_frame[0]);
		
		normal = mul(detail_normal, normal_frame);
	}
	*/
    float parallax_shadow = 1;
    if (PcfMode != PCF_NONE)
    {
        parallax_shadow = 1.0f - shadowStrength;
        float sun_amount = 0.03f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos) * AOMap * parallax_shadow;
        total_light += ((saturate(dot(In.SunLightDir.xyz, normal.xyz)) * (sun_amount))) * sunCol;
        float sunSpecular = pow(saturate(dot(reflect(-In.SunLightDir, normal), In.ViewDir)), 1 - smoothnessMap); // specular exponent modulated by smoothness
        float shw = sun_amount  * pow(AOMap, 3) * parallax_shadow;
        total_light += ((sunSpecular * sunCol) * shw) * 0.33f;
    }
    else
    {
        total_light += saturate(dot(In.SunLightDir.xyz, normal.xyz)) * vSunColor;
    }
    total_light += saturate(dot(In.SkyLightDir.xyz, normal.xyz)) * vSkyLightColor;


#ifndef USE_LIGHTING_PASS
    total_light += saturate(dot(In.PointLightDir.xyz, normal.xyz)) * vPointLightColor;
#endif
    
    Output.RGBColor.rgb = total_light.rgb;
    Output.RGBColor.a = 1.0f;
    
    Output.RGBColor *= vMaterialColor;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
    Output.RGBColor.rgb *= AOMap;
    Output.RGBColor.rgb *= parallax_shadow;
	
	//	Output.RGBColor = saturate(Output.RGBColor);
	OUTPUT_GAMMA(Output.RGBColor.rgb);
    return Output;
}

VertexShader vs_main_parallax_compiled_PCF_NONE = compile vs_2_0 vs_main_parallax(PCF_NONE);
VertexShader vs_main_parallax_compiled_PCF_DEFAULT = compile vs_2_0 vs_main_parallax(PCF_DEFAULT);
VertexShader vs_main_parallax_compiled_PCF_NVIDIA = compile vs_2_a vs_main_parallax(PCF_NVIDIA);


technique bumpmap_parallax
{
    pass P0
    {
        VertexShader = vs_main_parallax_compiled_PCF_NONE;
        PixelShader = compile PS_2_X ps_main_parallax(PCF_NONE);
    }
}
technique bumpmap_parallax_SHDW
{
    pass P0
    {
        VertexShader = vs_main_parallax_compiled_PCF_DEFAULT;
        PixelShader = compile PS_2_X ps_main_parallax(PCF_DEFAULT);
    }
}
technique bumpmap_parallax_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_main_parallax_compiled_PCF_NVIDIA;
        PixelShader = compile ps_2_a ps_main_parallax(PCF_NVIDIA);
    }
}

float4 blowing_flag(float4 vPosition)
{
    float angle = time_var * 2.65 + matWorld;
    float windPower = fWindPower *2;

    // Define thresholds for the non-moving parts
    float leftThreshold = 1.8; // Replace [some_value] with the appropriate value
    float topThreshold = -0.1; // Replace [some_value] with the appropriate value

    // Calculate factors for waving based on position
    float xFactor = max(0.0f, (leftThreshold - vPosition.x ) / leftThreshold);
    float yFactor = max(0.0f, (vPosition.z -topThreshold ) / topThreshold);

    // Apply waving effect scaled by factors
    float waveEffectY = sin((vPosition.x + angle) * 4.5) * (vPosition.z * 0.24) * vPosition.x * (windPower * 0.33 + 2) * 0.08
                      + cos((vPosition.z + angle) * 4.5) * (vPosition.x * 0.1) * (windPower * 0.33 + 2) * 0.08
                      + cos((vPosition.z + angle) * 1.6) * 0.5 * vPosition.x * 0.3;

    float invertedWindPower = 6.0 / (windPower * 0.33 / 5 + 4) - 1;
    float bending = -(windPower * 0.33 * 0.01 + windPower * 0.33 * 0.092 * (sin(angle * windPower * 0.33 / 3) * cos(angle * windPower * 0.33 / 3 * 0.39)) + 0.4) * vPosition.x * (invertedWindPower - 0.1);
    
    float bendingX = vPosition.x * cos(bending) - vPosition.z * sin(bending);
    float bendingZ = vPosition.x * sin(bending) + vPosition.z * cos(bending);

    // Apply the effect based on the factors
    vPosition.y += waveEffectY * yFactor * xFactor;
    vPosition.x = lerp(vPosition.x, bendingX, xFactor);
    //vPosition.z = lerp(vPosition.z, bendingZ, xFactor);

    return vPosition;
}

struct VS_OUTPUT_WAVING_BANNER
{
    float4 Pos : POSITION;
    float4 VertexColor : COLOR0;
    float2 Tex0 : TEXCOORD0;
    float3 SunLightDir : TEXCOORD1; //sun light dir in pixel coordinates
    float3 SkyLightDir : TEXCOORD2; //light diffuse for bump
    float4 PointLightDir : TEXCOORD3; //light ambient for bump
    float4 ShadowTexCoord : TEXCOORD4;
    float2 ShadowTexelPos : TEXCOORD5;
    float Fog : FOG;
	
    float3 ViewDir : TEXCOORD6;
    float3 WorldNormal : TEXCOORD7;
};
VS_OUTPUT_WAVING_BANNER vs_waving_banner(uniform const int PcfMode, uniform const bool is_windy_trunk, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float3 vTangent : TANGENT, float3 vBinormal : BINORMAL, float4 vVertexColor : COLOR0, float4 vPointLightDir : COLOR1)
{
	INITIALIZE_OUTPUT(VS_OUTPUT_WAVING_BANNER, Out);

    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    
    vPosition = blowing_flag(vPosition);

        // Recalculate world position and output position
    vWorldPos = (float4) mul(matWorld, vPosition);
    Out.Pos = mul(matWorldViewProj, vPosition);
    
    Out.Tex0 = tc;
    
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
    float3 vWorld_binormal = normalize(mul((float3x3) matWorld, vBinormal)); //normal in world space
    float3 vWorld_tangent = normalize(mul((float3x3) matWorld, vTangent)); //normal in world space

    float3 P = mul(matWorldView, vPosition); //position in view space

    float3x3 TBNMatrix = float3x3(vWorld_tangent, vWorld_binormal, vWorldN);

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }

    Out.SunLightDir = mul(TBNMatrix, -vSunDir);
    Out.SkyLightDir = mul(TBNMatrix, -vSkyLightDir);
	
#ifdef USE_LIGHTING_PASS
	Out.PointLightDir = vWorldPos;
#else
    Out.PointLightDir.rgb = 2.0f * vPointLightDir.rgb - 1.0f;
    Out.PointLightDir.a = vPointLightDir.a;
#endif
	
    Out.VertexColor = vVertexColor;
	
	//STR: note that these are not in TBN space.. (used for fresnel only..)
    Out.ViewDir = normalize(vCameraPos.xyz - vWorldPos.xyz); //normalize(mul(TBNMatrix, (vCameraPos.xyz - vWorldPos.xyz) ));	// 
	//Out.ViewDir = mul(TBNMatrix, Out.ViewDir);

    Out.WorldNormal = vWorldN;
	//Out.WorldNormal = mul(TBNMatrix, Out.WorldNormal);

	//apply fog
    float d = length(P);
    Out.Fog = get_fog_amount_new(d, vWorldPos.z);

    return Out;
}

PS_OUTPUT ps_waving_banner(VS_OUTPUT_WAVING_BANNER In, uniform const int PcfMode)
{
    PS_OUTPUT Output;
	
    float4 total_light = vAmbientColor; //In.LightAmbient;
	
    float3 normal = (2.0f * tex2D(NormalTextureSampler, In.Tex0).rgb - 1.0f);

    if (PcfMode != PCF_NONE)
    {
        float sun_amount = 0.03f + GetSunAmount(PcfMode, In.ShadowTexCoord, In.ShadowTexelPos);
        total_light += ((saturate(dot(In.SunLightDir.xyz, normal)) * (sun_amount))) * vSunColor;
    }
    else
    {
        total_light += saturate(dot(In.SunLightDir.xyz, normal)) * vSunColor;
    }
    total_light += saturate(dot(In.SkyLightDir.xyz, normal)) * vSkyLightColor;
	
#ifndef USE_LIGHTING_PASS
    total_light += saturate(dot(In.PointLightDir.xyz, normal)) * vPointLightColor;
#endif

    Output.RGBColor.rgb = total_light.rgb;
    Output.RGBColor.a = 1.0f;
    Output.RGBColor *= vMaterialColor;
	
    float4 tex_col = tex2D(MeshTextureSampler, In.Tex0);
    float3 col = OverlayBlendColor(tex_col.rgb, float3(normal.x,normal.y,normal.x));
    tex_col.rgb = lerp(col, tex_col.rgb, 0.5) + (tex_col.rgb * 0.5);
	INPUT_TEX_GAMMA(tex_col.rgb);

    Output.RGBColor *= tex_col;
    Output.RGBColor *= In.VertexColor;
	
	//	Output.RGBColor = saturate(Output.RGBColor);
	OUTPUT_GAMMA(Output.RGBColor.rgb);

    return Output;
}


VertexShader vs_waving_banner_compiled_PCF_NONE = compile vs_2_0 vs_waving_banner(PCF_NONE, false);
VertexShader vs_waving_banner_compiled_PCF_DEFAULT = compile vs_2_0 vs_waving_banner(PCF_DEFAULT, false);
VertexShader vs_waving_banner_compiled_PCF_NVIDIA = compile vs_2_a vs_waving_banner(PCF_NVIDIA, false);


technique waving_banner
{
    pass P0
    {
        VertexShader = vs_waving_banner_compiled_PCF_NONE;
        PixelShader = compile PS_2_X ps_waving_banner(PCF_NONE);
    }
}
technique waving_banner_SHDW
{
    pass P0
    {
        VertexShader = vs_waving_banner_compiled_PCF_DEFAULT;
        PixelShader = compile PS_2_X ps_waving_banner(PCF_DEFAULT);
    }
}
technique waving_banner_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = vs_waving_banner_compiled_PCF_NVIDIA;
        PixelShader = compile ps_2_a ps_waving_banner(PCF_NVIDIA);
    }
}

// WAVING STANDARD
/////////////////////

VS_OUTPUT vs_mtarini_standart(uniform const int PcfMode, uniform const bool UseSecondLight, float4 vPosition : POSITION, float3 vNormal : NORMAL, float2 tc : TEXCOORD0, float4 vColor : COLOR0, float4 vLightColor : COLOR1)
{
    VS_OUTPUT Out = (VS_OUTPUT) 0;
   
   // WAVING...
    float4 vPositionNew = vPosition;
    float3 vNormalNew;

    float time = -2.5 * time_var;
   //time = sin(time*5.0);

    float atten = 1.0, wavel = 1.0 + tc.y * 0.8, angle;
	
    float fluidity = max(abs(vPosition.z * 1.5) - 0.05f, 0); // Essentially, the further from z = 0, the more the banner can move. Maybe subtract tc.y from vPos.z?

    atten = min(tc.y * fluidity * 2.0f, 1.0f);
    angle = time + fluidity * 4.0 * wavel;
  
    vPositionNew.x += (sin(angle) * (atten * 0.065));
   
    vPositionNew.y += (cos(angle) * (atten * 0.05)) /* max(fluidity - 0.25, 0)*/;
	
    vPositionNew.z += (sin(angle) * (atten * 0.025)) * fluidity;
   

    vNormalNew.z = cos(angle) * atten * fluidity;
    vNormalNew.y = vNormalNew.z * tc.y * 0.1;
    vNormalNew.x = -sqrt(1.0 - vNormalNew.z * vNormalNew.z);

   // revert all in not waving parts
    vPositionNew = (tc.x > 0.751) ? vPosition : vPositionNew;
    vPosition = (vAmbientColor > 0.85) ? vPosition : vPositionNew;
    vNormal = (tc.x > 0.75) ? vNormal : vNormalNew;
 
    Out.Pos = mul(matWorldViewProj, vPosition);
   
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 vWorldN = normalize(mul((float3x3) matWorld, vNormal)); //normal in world space
   
    float3 P = mul(matWorldView, vPosition); //position in view space
   
    Out.Tex0 = tc;

    float4 diffuse_light = vAmbientColor;
//   diffuse_light.rgb *= gradient_factor * (gradient_offset + vWorldN.z);
   
    if (UseSecondLight)
    {
        diffuse_light += vLightColor;
    }
   
	//directional lights, compute diffuse color
    float dp = dot(vWorldN, -vSkyLightDir);
    diffuse_light += max(0, dp) * vSkyLightColor;

	//point lights
    for (int j = 0; j < iLightPointCount; j++)
    {
        int i = iLightIndices[j];
        float3 point_to_light = vLightPosDir[i] - vWorldPos;
        float LD = length(point_to_light);
        float3 L = normalize(point_to_light);
        float wNdotL = dot(vWorldN, L);
		
        float fAtten = 1.0f / (LD * LD); // + 0.9f / (LD * LD);
		//compute diffuse color
        diffuse_light += max(0, wNdotL) * vLightDiffuse[i] * fAtten;
    }
   //apply material color
//	Out.Color = min(1, vMaterialColor * vColor * diffuse_light);
    Out.Color = (vMaterialColor * vColor * diffuse_light);

	//shadow mapping variables
    float wNdotSun = max(0.0f, dot(vWorldN, -vSunDir));
    Out.SunLight = (wNdotSun) * vSunColor * vMaterialColor * vColor;
    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
		//shadow mapping variables end
    }
	
   //apply fog
    float d = length(P);
   
    Out.Fog = get_fog_amount(d);
    return Out;
}

technique mtarini_standart_shader
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_standart(PCF_NONE, true);
        PixelShader = compile PS_2_X ps_main(PCF_NONE);
    }
}

technique mtarini_standart_shader_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_standart(PCF_DEFAULT, true);
        PixelShader = compile PS_2_X ps_main(PCF_DEFAULT);
    }
}

technique mtarini_standart_shader_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_standart(PCF_NVIDIA, true);
        PixelShader = compile PS_2_X ps_main(PCF_NVIDIA);
    }
}


// WIND THOUGH LEAVES
/////////////////////////

VS_OUTPUT_FLORA vs_mtarini_windy_flora(uniform const int PcfMode, uniform const float windSTR, uniform const int UseUV, float4 vPosition : POSITION, float3 norm : NORMAL, float4 vColor : COLOR, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_FLORA Out = (VS_OUTPUT_FLORA) 0;

    float2 treePos = float2(matWorld._m03, matWorld._m23);
    float windAmount = sin(time_var * 0.1014) + cos(time_var * 0.1413);
    windAmount *= windAmount;
    windAmount += 0.2;
    float t2 = time_var + dot(treePos, float2(2.5, 1.5)) + dot(norm, float3(7.1, 0.4, 3.2));
    float windPhase = sin(t2 * 3.9) * cos(t2 * 2.3);
    if (UseUV == 1)
    {
        vPosition.xyz += norm * (tc.x - 0.5) * (tc.y - 0.5) * windPhase * windAmount * windSTR;
    }
    else
    {
        vPosition.xyz += norm * windPhase * windAmount * windSTR;
    }
   
    Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
   
    float3 P = mul(matWorldView, vPosition); //position in view space
   
    Out.Tex0 = tc;
    Out.Color = vColor * (vAmbientColor + vSunColor * 0.06f); //add some sun color to simulate sun passing through leaves.
   
   	//shadow mapping variables
    Out.SunLight = (vSunColor * 0.34f) * vMaterialColor * vColor;

    if (PcfMode != PCF_NONE)
    {
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
    }
	//shadow mapping variables end
   
   //apply fog
    float d = length(P);
    Out.Fog = get_fog_amount(d);

    return Out;
}

VS_OUTPUT_FLORA vs_mtarini_windy_grass(uniform const int PcfMode, float4 vPosition : POSITION, float4 vColor : COLOR, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_FLORA Out = (VS_OUTPUT_FLORA) 0;
	
    float windAmount = sin(time_var * 0.1014) + cos(time_var * 0.1413);
    windAmount *= windAmount;
    float2 treePos = //float2 (matWorld._m03, matWorld._m13) + 
                    vPosition.xy;
    float t2 = time_var + dot(treePos, float2(6.5, 4.5));
    float windPhase = sin(t2 * 3.9) * cos(t2 * 2.3);
    vPosition.xy += float2(0.018, 0.018) // *(vPosition.z+50.0)
				    * windPhase * (windAmount + 0.2)
                   * vColor.w; // distance from ground stored in alpha channes with openbrf easteregg! ;)
   
    Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
    float3 P = mul(matWorldView, vPosition); //position in view space
    Out.Tex0 = tc;
	
    Out.Color = vColor * vAmbientColor;
  
    if (PcfMode != PCF_NONE)
    {
        Out.SunLight = (vSunColor * 0.55f) * vMaterialColor * vColor;
        float4 ShadowPos = mul(matSunViewProj, vWorldPos);
        Out.ShadowTexCoord = ShadowPos;
        Out.ShadowTexCoord.z /= ShadowPos.w;
        Out.ShadowTexCoord.w = 1.0f;
        Out.ShadowTexelPos = Out.ShadowTexCoord * fShadowMapSize;
    }
    else
    {
        Out.SunLight = vSunColor * 0.5f * vColor;
    }
	//shadow mapping variables end
   //apply fog
    float d = length(P);
    Out.Fog = get_fog_amount(d);
   
    Out.Color.a = min(1.0f, (1.0f - (d / 50.0f)) * 2.0f);

    return Out;
}

VS_OUTPUT_FLORA_NO_SHADOW vs_mtarini_windy_grass_no_shadow(float4 vPosition : POSITION, float4 vColor : COLOR, float2 tc : TEXCOORD0)
{
    VS_OUTPUT_FLORA_NO_SHADOW Out = (VS_OUTPUT_FLORA_NO_SHADOW) 0;

    float windAmount = sin(time_var * 0.1014) + cos(time_var * 0.1413);
    windAmount *= windAmount;
    float2 treePos = float2(matWorld._m03, matWorld._m13) + vPosition.xy;
    float t2 = time_var + dot(treePos, float2(2.5, 1.5));
    float windPhase = sin(t2 * 3.9) * cos(t2 * 2.3);
    vPosition.xy += float2(0.018, 0.018) // *(vPosition.z+50.0)
				    * windPhase * (windAmount + 0.2)
                   * vColor.w; // distance from ground stored in alpha channes with openbrf easteregg! ;)
   	
	
    Out.Pos = mul(matWorldViewProj, vPosition);
    float4 vWorldPos = (float4) mul(matWorld, vPosition);
  
    float3 P = mul(matWorldView, vPosition); //position in view space
   
    Out.Tex0 = tc;
    Out.Color = vColor * vMaterialColor;
   
   //apply fog
    float d = length(P);
    Out.Fog = get_fog_amount(d);
   
    Out.Color.a = min(1.0f, (1.0f - (d / 50.0f)) * 2.0f);
   //Out.Color.r = 1; Out.Color.g = Out.Color.b = 1.0-vColor.w;

    return Out;
}


technique mtarini_windy_flora
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NONE, 0.18, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_NONE);
    }
}

technique mtarini_windy_flora_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_DEFAULT, 0.18, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_DEFAULT);
    }
}

technique mtarini_windy_flora_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NVIDIA, 0.18, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_NVIDIA);
    }
}

technique mtarini_windy_flora_PRESHADED
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NONE, 0.18, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_NONE);
    }
}

technique mtarini_windy_flora_mild_one_sheet
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NONE, 0.1, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_NONE);
    }
}

technique mtarini_windy_flora_mild_one_sheet_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_DEFAULT, 0.1, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_DEFAULT);
    }
}

technique mtarini_windy_flora_mild_one_sheet_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NVIDIA, 0.1, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_NVIDIA);
    }
}

technique mtarini_windy_flora_mild_one_sheet_PRESHADED
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NONE, 0.1, 1);
        PixelShader = compile PS_2_X ps_flora(PCF_NONE);
    }
}

technique mtarini_windy_flora_mild
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NONE, 0.00625, 0);
        PixelShader = compile PS_2_X ps_flora(PCF_NONE);
    }
}
technique mtarini_windy_flora_mild_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_DEFAULT, 0.00625, 0);
        PixelShader = compile PS_2_X ps_flora(PCF_DEFAULT);
    }
}
technique mtarini_windy_flora_mild_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NVIDIA, 0.00625, 0);
        PixelShader = compile PS_2_X ps_flora(PCF_NVIDIA);
    }
}
technique mtarini_windy_flora_mild_PRESHADED
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_flora(PCF_NONE, 0.00625, 0);
        PixelShader = compile PS_2_X ps_flora(PCF_NONE);
    }
}


technique mtarini_windy_grass
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_grass(PCF_NONE);
        PixelShader = compile PS_2_X ps_grass(PCF_NONE);
    }
}

technique mtarini_windy_grass_SHDW
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_grass(PCF_DEFAULT);
        PixelShader = compile PS_2_X ps_grass(PCF_DEFAULT);
    }
}

technique mtarini_windy_grass_SHDWNVIDIA
{
    pass P0
    {
        VertexShader = compile vs_2_a vs_mtarini_windy_grass(PCF_NVIDIA);
        PixelShader = compile ps_2_a ps_grass(PCF_NVIDIA);
    }
}

technique mtarini_windy_grass_PRESHADED
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_grass(PCF_NONE);
        PixelShader = compile PS_2_X ps_grass(PCF_NONE);
      //VertexShader = compile vs_2_0 vs_mtarini_windy_grass_no_shadow();
      //PixelShader = compile PS_2_X ps_grass_no_shadow();
    }
}

technique mtarini_windy_grass_no_shadow
{
    pass P0
    {
        VertexShader = compile vs_2_0 vs_mtarini_windy_grass_no_shadow();
        PixelShader = compile PS_2_X ps_grass_no_shadow();
    }
}

