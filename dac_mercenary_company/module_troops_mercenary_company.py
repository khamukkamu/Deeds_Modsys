from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *
# from module_troops import *

from compiler import *

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

 #Troop Skills Templates
#lvl12
knows_common_kham = knows_weapon_master_5|knows_ironflesh_4|knows_athletics_5|knows_power_strike_3|knows_shield_1|knows_inventory_management_2|knows_power_throw_3|knows_power_draw_3 #40+12 / 2
#lvl18
knows_warrior_basic = knows_weapon_master_6|knows_ironflesh_5|knows_athletics_5|knows_riding_2|knows_power_strike_3|knows_shield_2|knows_inventory_management_4|knows_power_throw_3|knows_power_draw_3 #40+18 / 2 +2
#lvl23
knows_warrior_basic2 = knows_weapon_master_7|knows_ironflesh_7|knows_athletics_5|knows_riding_3|knows_power_strike_5|knows_shield_4|knows_inventory_management_4|knows_power_throw_3|knows_power_draw_3  #40+24 / 2 +4
#lvl26
knows_warrior_normal = knows_weapon_master_8|knows_ironflesh_8|knows_athletics_5|knows_riding_5|knows_power_strike_5|knows_shield_4|knows_inventory_management_5|knows_power_throw_4|knows_power_draw_4 #40+26 / 2 +6
#lvl29
knows_warrior_veteran = knows_weapon_master_9|knows_ironflesh_9|knows_athletics_5|knows_riding_6|knows_power_strike_7|knows_shield_6|knows_inventory_management_5|knows_power_throw_4|knows_power_draw_4 ##40+30 / 2 +8
#lvl31
knows_warrior_elite = knows_weapon_master_10|knows_ironflesh_10|knows_athletics_5|knows_riding_7|knows_power_strike_8|knows_shield_6|knows_inventory_management_6|knows_power_throw_4|knows_power_draw_4 ###40+32 / 2 +12

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30
knows_archer_basic = knows_weapon_master_3|knows_ironflesh_6|knows_athletics_5|knows_riding_3|knows_power_strike_2|knows_shield_2|knows_inventory_management_4|knows_power_throw_4|knows_power_draw_4 #cambiado chief

#Attributes Templates
def_attrib =    str_16 | agi_8 | int_12 | cha_12|level(12)   #basic points 55
def_attrib_b =  str_16 | agi_8 | int_12 | cha_12|level(18) #basic points 55

def_attrib2 =   str_18 | agi_8 | int_12 | cha_12|level(23)   #+3 level med
def_attrib2_b = str_18 | agi_8 | int_12 | cha_12|level(26) #+3 level med

def_attrib3 =   str_20 | agi_8 | int_12 | cha_12|level(29)   #+5 level max
def_attrib3_b = str_20 | agi_8 | int_12 | cha_12|level(31)   #+5 level max

### Kings & Lords Template New System BEGIN
king_attrib = str_20|agi_19|int_18|cha_20|level(40)

king_skills = knows_weapon_master_10|knows_trainer_5|knows_riding_4|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_shield_3|knows_tactics_10|knows_prisoner_management_9|knows_leadership_10|knows_wound_treatment_9|knows_first_aid_8|knows_surgery_8|knows_power_throw_5|knows_power_draw_6|knows_spotting_6|knows_pathfinding_5|knows_inventory_management_4|knows_persuasion_6|knows_engineer_6


knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

### New Faces
# French
french_face_young_1 =  0x000000000800b14d37a472292d963ad300000000001da5220000000000000000
french_face_young_2 =  0x000000003800100457237198fb66c54b00000000001da32a0000000000000000 

french_face_middle_1 = 0x00000006b400324d37a472292d963ad300000000001d25220000000000000000
french_face_middle_2 = 0x00000006bc00204537a472292d963ad300000000001d25220000000000000000

french_face_mature_1 = 0x0000000d550c81914b15aa592449652500000000001da4f10000000000000000
french_face_mature_2 = 0x0000000d6e04200619746e450d6a670b00000000001d42c90000000000000000

french_face_old_1 =  0x0000000e7c0052c537a472292d963ad300000000001d25220000000000000000
french_face_old_2 = 0x0000000ff30c500f4b15aa592449652500000000001da4f10000000000000000

# English
english_face_young_1 =  0x000000028b10000436db6dbaeb61a55d00000000001da6db0000000000000000
english_face_young_2 =  0x00000002a008618928db7238e12944eb00000000001e44e30000000000000000 

english_face_middle_1 = 0x000000068010620146e95f3c73d1b71100000000001dd6a50000000000000000
english_face_middle_2 = 0x00000006a3102406381975b6eb3d296500000000001e46d20000000000000000

english_face_mature_1 = 0x0000000a9504b304285a38a4b28ec8ac00000000001fb7080000000000000000
english_face_mature_2 = 0x0000000aa800600336db6db6db6db6db00000000000db6db0000000000000000

english_face_old_1 =  0x0000000ec210410467a68b5b1a71469b00000000001ec49e0000000000000000
english_face_old_2 = 0x0000000ecc10800d38e222e4d8ce1d2400000000001dc9250000000000000000

# Burgundian
burgundian_face_young_1 =  0x00000000e200350d3ae28dd6eb23255300000000001d26ec0000000000000000
burgundian_face_young_2 =  0x00000000ca0c100446b3b1556196aacb00000000001db6690000000000000000

burgundian_face_middle_1 = 0x00000004a70091836314731cd5b9969500000000001e251a0000000000000000
burgundian_face_middle_2 = 0x00000004890c3441276488c79b62ab5900000000001e48580000000000000000

burgundian_face_mature_1 = 0x00000009380c754d36528b27194ec2cc00000000001cb4990000000000000000
burgundian_face_mature_2 = 0x000000090100c591492c3096a162b93500000000001d44ca0000000000000000

burgundian_face_old_1 =  0x0000000f2404924d650b72a68b8949a300000000000926940000000000000000
burgundian_face_old_2 = 0x0000000f2204810f48edc9e7219092d100000000001a326d0000000000000000

# Breton
breton_face_young_1 =  0x000000000c04b0034c548ac0d42d932300000000001db44c0000000000000000
breton_face_young_2 =  0x000000002408718438dc49dd1b17371c00000000001d97120000000000000000

breton_face_middle_1 = 0x000000045f00514346feadb89cc8b25900000000001e48730000000000000000
breton_face_middle_2 = 0x000000045400a2c463132e4ad2b1a4e500000000001e57a50000000000000000

breton_face_mature_1 = 0x0000000a2408708b2693ae3d1ada38db00000000001da29d0000000000000000
breton_face_mature_2 = 0x0000000a0610a2463b092d44e1359aa200000000001eb8de0000000000000000

breton_face_old_1 =  0x0000000f700452d134d58d9cde30e90b00000000001de2d90000000000000000
breton_face_old_2 = 0x0000000f65086542471baa388a91a12500000000001654e30000000000000000

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

mercenary_company_troops = [

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################


# FORMAT:
# 1. Regular troop: this is the actual troop entry used for the troop. Ignore the equipment list, you can leave it blank.
# 2. Equip troop: shows what the troop will be carrying when the game first starts. This is later used for saving the troop's custom selection
# 3. Troop equipment selection: List of what is available to select during the customization phase. Can have up to around 80 items max, but recommended is maybe 50 max (to leave room so you can remove items from the current selection).

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS INFANTRY ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

## Tier 1 ##

  ["custom_merc_recruit","Company Recruit","Company Recruits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(10)|str_12|agi_12, 
    wp_melee(120), 
    knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1,
    vaegir_face_young_1, vaegir_face_young_2],
  
  ["custom_merc_recruit_equip","Company Recruit","Company Recruits",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_arming_cap,
    itm_h_simple_coif,
    itm_h_peasant_bycocket_1_custom,
    itm_h_peasant_bycocket_2_custom,
    
    itm_a_peasant_cote_custom,
    itm_a_peasant_cotehardie_custom,
    itm_a_noble_shirt_custom,
    
    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    
    itm_w_dagger_pikeman,
    itm_w_archer_hatchet,
    itm_w_onehanded_sword_c_small,
    itm_w_spiked_club,
    itm_w_mace_knobbed,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_recruit_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_arming_cap,
    itm_h_simple_coif,
    itm_h_peasant_bycocket_1_custom,
    itm_h_peasant_bycocket_2_custom,
    itm_h_hood_square_full_custom,
    itm_h_hood_square_liripipe_full_custom,
    itm_h_hood_big_liripipe_full_custom,
    itm_h_skullcap_strap,
    itm_h_rope_helmet_strap,
    itm_h_wicker_helmet_strap,
    
    itm_a_peasant_cote_custom,
    itm_a_peasant_cotehardie_custom,
    itm_a_noble_shirt_custom,
    
    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    itm_b_turnshoes_4,
    itm_b_turnshoes_5,
    itm_b_turnshoes_6,
    itm_b_turnshoes_7,
    itm_b_turnshoes_8,
    itm_b_turnshoes_9,
    
    itm_w_dagger_pikeman,
    itm_w_dagger_quillon,
    itm_w_archer_hatchet,
    itm_w_archer_hatchet_brown,
    itm_w_archer_hatchet_red,
    itm_w_onehanded_sword_a,
    itm_w_onehanded_sword_c_small,
    itm_w_onehanded_sword_c,
    itm_w_spiked_club,
    itm_w_spiked_club_brown,
    itm_w_spiked_club_dark,
    itm_w_mace_knobbed,
    itm_w_mace_knobbed_brown,
    itm_w_mace_knobbed_red,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],

# Tier 2 #

  ["custom_merc_footman","Company Footman","Company Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(15)|str_14|agi_14, 
    wp_melee(140), 
    knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1,
    vaegir_face_old_1, vaegir_face_old_2],
  
  ["custom_merc_footman_equip","Company Footman","Company Footmen",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_simple_cervelliere_hood_liripipe_custom,
    itm_h_skullcap_hood_liripipe_custom,
    itm_h_cervelliere_hood_custom,
    itm_h_simple_cervelliere_hood_custom,
    itm_h_skullcap_hood_custom,
    
    itm_a_aketon_asher_blue_1,
    itm_a_aketon_asher_green_1,
    itm_a_aketon_asher_vandyked_blue_1,
    itm_a_aketon_asher_vandyked_red_1,
    itm_a_aketon_asher_dagged_beige_1,
    itm_a_aketon_asher_dagged_white_1,
    
    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    
    itm_w_spear_2,
    itm_w_spear_3,
    itm_w_spear_4,
    itm_w_mace_winged,
    itm_w_onehanded_war_axe_02,
    itm_w_onehanded_falchion_peasant,
    itm_w_onehanded_falchion_peasant_b,
    
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_footman_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    
    itm_h_german_kettlehat_1_strap,
    itm_h_german_kettlehat_2_strap,
    itm_h_german_kettlehat_3_strap,
    itm_h_german_kettlehat_4_strap,
    itm_h_german_kettlehat_5_strap,
    itm_h_german_kettlehat_6_strap,
    itm_h_german_kettlehat_7_strap,
    itm_h_makeshift_kettle_strap,
    itm_h_cervelliere_strap,
    itm_h_cervelliere_roundel_strap,
    itm_h_simple_cervelliere_strap,
    itm_h_simple_cervelliere_2_strap,
    itm_h_shingle_helmet_strap,
    itm_h_simple_cervelliere_hood_liripipe_custom,
    itm_h_skullcap_hood_liripipe_custom,
    itm_h_cervelliere_hood_custom,
    itm_h_simple_cervelliere_hood_custom,
    itm_h_skullcap_hood_custom,
    
    itm_a_aketon_asher_blue_1,
    itm_a_aketon_asher_green_1,
    itm_a_aketon_asher_vandyked_blue_1,
    itm_a_aketon_asher_vandyked_red_1,
    itm_a_aketon_asher_dagged_beige_1,
    itm_a_aketon_asher_dagged_white_1,
    itm_a_light_gambeson_short_sleeves_custom,
    itm_a_light_gambeson_short_sleeves_diamond_custom,
    itm_a_light_gambeson_long_sleeves_custom,
    itm_a_light_gambeson_long_sleeves_diamond_custom,
    itm_a_gambeson_grande_assiette_custom,
    
    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    itm_b_turnshoes_4,
    itm_b_turnshoes_5,
    itm_b_turnshoes_6,
    itm_b_turnshoes_7,
    itm_b_turnshoes_8,
    itm_b_turnshoes_9,
    
    itm_w_spear_2,
    itm_w_spear_3,
    itm_w_spear_4,
    itm_w_mace_winged,
    itm_w_mace_winged_brown,
    itm_w_mace_winged_red,
    itm_w_onehanded_war_axe_02,
    itm_w_onehanded_war_axe_02_brown,
    itm_w_onehanded_falchion_peasant,
    itm_w_onehanded_falchion_peasant_b,
    itm_w_onehanded_sword_a,
    itm_w_onehanded_sword_c,
    itm_w_onehanded_sword_d,
    
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_french_3,
    itm_s_heater_shield_french_4,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_english_3,
    itm_s_heater_shield_english_4,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_burgundian_3,
    itm_s_heater_shield_burgundian_4,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
    
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],

# Tier 3 #

  ["custom_merc_veteran","Company Veteran","Company Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(20)|str_16|agi_16, 
    wp_melee(160), 
    knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2,
    mercenary_face_1, mercenary_face_2],
  
  ["custom_merc_veteran_equip","Company Veteran","Company Veterans",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_transitional_sallet_1_strap,
    itm_h_transitional_sallet_2_strap,
    itm_h_transitional_sallet_3_strap,
    itm_h_german_kettlehat_1_mail_aventail,
    itm_h_german_kettlehat_2_mail_aventail,
    itm_h_german_kettlehat_3_mail_aventail,
    itm_h_chapel_de_fer_mail_aventail,
    itm_h_martinus_kettlehat_1_mail_aventail,
    itm_h_martinus_kettlehat_2_mail_aventail,

    itm_a_pistoia_mail_a_mail_sleeves_short,
    itm_a_pistoia_mail_b_mail_sleeves_short,

    itm_b_high_boots_1,
    itm_b_high_boots_2,
    itm_b_high_boots_3,
    
    itm_w_spear_2,
    itm_w_spear_3,
    itm_w_spear_4,
    itm_w_spear_5,
    itm_w_warhammer_1,
    itm_w_warhammer_2,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_veteran_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.

    itm_h_transitional_sallet_1_strap,
    itm_h_transitional_sallet_2_strap,
    itm_h_transitional_sallet_3_strap,
    itm_h_german_kettlehat_1_mail_aventail,
    itm_h_german_kettlehat_2_mail_aventail,
    itm_h_german_kettlehat_3_mail_aventail,
    itm_h_german_kettlehat_4_mail_aventail,
    itm_h_german_kettlehat_5_mail_aventail,
    itm_h_german_kettlehat_6_mail_aventail,
    itm_h_german_kettlehat_7_mail_aventail,
    itm_h_chapel_de_fer_mail_aventail,
    itm_h_martinus_kettlehat_1_mail_aventail,
    itm_h_martinus_kettlehat_2_mail_aventail,

    itm_a_pistoia_mail_a_mail_sleeves_short,
    itm_a_pistoia_mail_b_mail_sleeves_short,
    itm_a_pistoia_mail_a_mail_sleeves,
    itm_a_pistoia_mail_b_mail_sleeves,
    itm_a_pistoia_mail_a_mail_sleeves_jackchains,
    itm_a_pistoia_mail_b_mail_sleeves_jackchains,

    itm_b_high_boots_1,
    itm_b_high_boots_2,
    itm_b_high_boots_3,
    itm_b_high_boots_4,
    itm_b_high_boots_5,
    itm_b_high_boots_6,
    itm_b_high_boots_7,
    itm_b_high_boots_8,
    itm_b_high_boots_9,
    
    itm_w_spear_2,
    itm_w_spear_3,
    itm_w_spear_4,
    itm_w_spear_5,
    itm_w_warhammer_1,
    itm_w_warhammer_1_brown,
    itm_w_warhammer_1_red,
    itm_w_warhammer_2,
    itm_w_warhammer_2_brown,
    itm_w_warhammer_2_red,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_french_3,
    itm_s_heater_shield_french_4,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_english_3,
    itm_s_heater_shield_english_4,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_burgundian_3,
    itm_s_heater_shield_burgundian_4,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
    
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],

# Tier 4 #

  ["custom_merc_sergeant","Company Sergeant","Company Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20, 
    wp_melee(180), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5,
    mercenary_face_1, mercenary_face_2],
  
  ["custom_merc_sergeant_equip","Company Sergeant","Company Sergeants",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_transitional_sallet_1_mail_aventail,
    itm_h_transitional_sallet_2_mail_aventail,
    itm_h_transitional_sallet_3_mail_aventail,
    
    itm_a_pistoia_breastplate_half_mail_sleeves,
    itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_spear_2,
    itm_w_spear_3,
    itm_w_warhammer_1,
    itm_w_warhammer_2,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    itm_w_onehanded_sword_defiant,
    
    itm_s_heraldic_shield_french_1,
    itm_s_heraldic_shield_french_2,
    itm_s_heraldic_shield_english_1,
    itm_s_heraldic_shield_english_2,
    itm_s_heraldic_shield_burgundian_1,
    itm_s_heraldic_shield_burgundian_2,
    itm_s_heraldic_shield_breton_1,
    itm_s_heraldic_shield_breton_2,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_sergeant_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.

    itm_h_transitional_sallet_1_mail_aventail,
    itm_h_transitional_sallet_2_mail_aventail,
    itm_h_transitional_sallet_3_mail_aventail,
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_eyeslot_kettlehat_1_mail_aventail,
    itm_h_eyeslot_kettlehat_2_mail_aventail,
    itm_h_eyeslot_kettlehat_3_mail_aventail,
    itm_h_oliphant_eyeslot_kettlehat_mail_aventail,
    itm_h_martinus_kettlehat_3_mail_aventail,
    
    itm_a_pistoia_mail_a_mail_sleeves_plate_spaulders_1,
    itm_a_pistoia_mail_b_mail_sleeves_plate_spaulders_1,
    itm_a_pistoia_mail_a_mail_sleeves_plate_spaulders_2,
    itm_a_pistoia_mail_b_mail_sleeves_plate_spaulders_2,
    itm_a_pistoia_mail_a_mail_sleeves_plate_spaulders_3,
    itm_a_pistoia_mail_b_mail_sleeves_plate_spaulders_3,
    itm_a_pistoia_breastplate_half_mail_sleeves,
    itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_spear_2,
    itm_w_spear_3,
    itm_w_spear_4,
    itm_w_spear_5,
    itm_w_warhammer_1,
    itm_w_warhammer_1_brown,
    itm_w_warhammer_1_red,
    itm_w_warhammer_2,
    itm_w_warhammer_2_brown,
    itm_w_warhammer_2_red,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heraldic_shield_french_1,
    itm_s_heraldic_shield_french_2,
    itm_s_heraldic_shield_french_3,
    itm_s_heraldic_shield_french_4,
    itm_s_heraldic_shield_english_1,
    itm_s_heraldic_shield_english_2,
    itm_s_heraldic_shield_english_3,
    itm_s_heraldic_shield_english_4,
    itm_s_heraldic_shield_burgundian_1,
    itm_s_heraldic_shield_burgundian_2,
    itm_s_heraldic_shield_burgundian_3,
    itm_s_heraldic_shield_burgundian_4,
    itm_s_heraldic_shield_breton_1,
    itm_s_heraldic_shield_breton_2,
    itm_s_heraldic_shield_breton_3,
    
    
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],
    
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS RANGED ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["custom_merc_skirmisher","Company Skirmisher","Company Skirmishers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_player_faction,[],
    level(8)|str_10|agi_12,  
    wpex(90,90,90,100,100,100), 
    knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_skirmisher_equip","Company Skirmisher","Company Skirmishers",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_hood_big_liripipe_full_custom,
    itm_h_arming_cap,
    itm_h_simple_coif,
    itm_h_straw_hat,
    itm_h_peasant_bycocket_1_custom,
    
    itm_a_peasant_cote_custom,
    itm_a_hunter_coat_custom,
    
    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    
    itm_w_dagger_quillon,
    itm_w_archer_hatchet,
    itm_w_archers_maul,
    
    itm_w_short_bow_ash,
    itm_w_short_bow_elm,
    
    itm_w_arrow_triangular,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_skirmisher_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.

    itm_h_hood_square_full_custom,
    itm_h_hood_square_liripipe_full_custom,
    itm_h_hood_big_liripipe_full_custom,
    itm_h_arming_cap,
    itm_h_simple_coif,
    itm_h_straw_hat,
    itm_h_peasant_bycocket_1_custom,
    itm_h_peasant_bycocket_2_custom,
    itm_h_wicker_helmet_strap,
    itm_h_rope_helmet_strap,
    itm_h_skullcap_strap,
    
    itm_a_peasant_man_custom,
    itm_a_peasant_cote_custom,
    itm_a_peasant_cotehardie_custom,
    itm_a_hunter_coat_custom,
    itm_a_noble_shirt_custom,
    itm_a_light_gambeson_short_sleeves_custom,
    itm_a_light_gambeson_short_sleeves_diamond_custom,
    
    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    itm_b_turnshoes_4,
    itm_b_turnshoes_5,
    itm_b_turnshoes_6,
    itm_b_turnshoes_7,
    itm_b_turnshoes_8,
    itm_b_turnshoes_9,
    
    itm_w_dagger_italian,
    itm_w_dagger_pikeman,
    itm_w_dagger_quillon,
    itm_w_archer_hatchet,
    itm_w_archer_hatchet_brown,
    itm_w_archer_hatchet_red,
    itm_w_archers_maul,
    itm_w_archers_maul_brown,
    itm_w_archers_maul_red,
    
    itm_w_short_bow_ash,
    itm_w_short_bow_elm,
    itm_w_short_bow_oak,
    itm_w_crossbow_hunting,
    itm_w_crossbow_light,
    
    itm_w_arrow_triangular,
    itm_w_bolt_triangular,

    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_ranger","Company Ranger","Company Rangers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_player_faction,[],
    level(12)|str_12|agi_14,  
    wpex(100,100,100,120,120,120), 
    knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2,
    mercenary_face_1, mercenary_face_2],
 
  ["custom_merc_ranger_equip","Company Ranger","Company Rangers",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_skullcap_hood_liripipe_custom,
    itm_h_simple_cervelliere_hood_liripipe_custom,
    itm_h_simple_cervelliere_strap,
    itm_h_simple_cervelliere_2_strap,

    itm_a_light_gambeson_long_sleeves_custom,
    itm_a_light_gambeson_long_sleeves_diamond_custom,

    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    
    itm_w_spiked_club,
    itm_w_onehanded_war_axe_02,
    itm_w_onehanded_falchion_peasant,
    itm_w_onehanded_falchion_peasant_b,
    itm_w_dagger_baselard,
    itm_w_dagger_rondel,

    itm_w_hunting_bow_ash,
    itm_w_hunting_bow_elm,

    itm_w_arrow_triangular,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_ranger_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_skullcap_hood_liripipe_custom,
    itm_h_simple_cervelliere_hood_liripipe_custom,
    itm_h_simple_cervelliere_strap,
    itm_h_simple_cervelliere_2_strap,
    itm_h_cervelliere_roundel_strap,
    itm_h_makeshift_kettle_strap,
    itm_h_chapel_de_fer_strap,
    itm_h_german_kettlehat_1_strap,
    itm_h_german_kettlehat_2_strap,
    itm_h_german_kettlehat_3_strap,

    itm_a_light_gambeson_altichiero_nooxy_custom,
    itm_a_light_gambeson_altichiero_nooxy_alt_custom,
    itm_a_light_gambeson_long_sleeves_custom,
    itm_a_light_gambeson_long_sleeves_diamond_custom,
    itm_a_gambeson_grande_assiette_custom,
    itm_a_simple_gambeson_custom,

    itm_b_turnshoes_1,
    itm_b_turnshoes_2,
    itm_b_turnshoes_3,
    itm_b_turnshoes_4,
    itm_b_turnshoes_5,
    itm_b_turnshoes_6,
    itm_b_turnshoes_7,
    itm_b_turnshoes_8,
    itm_b_turnshoes_9,
    
    itm_w_goedendag,
    itm_w_spiked_club,
    itm_w_spiked_club_brown,
    itm_w_spiked_club_dark,
    itm_w_onehanded_war_axe_02,
    itm_w_onehanded_war_axe_02_brown,
    itm_w_onehanded_war_axe_02_red,
    itm_w_onehanded_sword_a,
    itm_w_onehanded_sword_c,
    itm_w_onehanded_sword_d,
    itm_w_onehanded_falchion_peasant,
    itm_w_onehanded_falchion_peasant_b,
    itm_w_dagger_baselard,
    itm_w_dagger_rondel,

    itm_w_hunting_bow_ash,
    itm_w_hunting_bow_elm,
    itm_w_hunting_bow_oak,
    itm_w_crossbow_cavalry,
    itm_w_crossbow_medium,

    itm_w_arrow_triangular,
    itm_w_bolt_triangular,
    
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_marksman","Company Marksman","Company Marksmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_player_faction,[],
    level(18)|str_14|agi_16,  
    wpex(120,120,120,150,150,150), 
    knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3,
    mercenary_face_1, mercenary_face_2],
   
  ["custom_merc_marksman_equip","Company Marksman","Company Marksmen",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_cervelliere_mail_aventail,
    itm_h_cervelliere_roundels_mail_aventail,
    itm_h_makeshift_kettle_mail_aventail,
    
    itm_a_gambeson_asher_regular_custom,
    itm_a_gambeson_asher_belt_custom,
    
    itm_b_high_boots_1,
    itm_b_high_boots_2,
    itm_b_high_boots_3,
    
    itm_w_mace_winged,
    itm_w_onehanded_war_axe_01,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    
    itm_w_war_bow_ash,
    itm_w_war_bow_elm,
    itm_w_war_bow_oak,

    itm_w_arrow_triangular_large,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_marksman_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_cervelliere_mail_aventail,
    itm_h_cervelliere_roundels_mail_aventail,
    itm_h_makeshift_kettle_mail_aventail,
    itm_h_german_kettlehat_1_mail_aventail,
    itm_h_german_kettlehat_2_mail_aventail,
    itm_h_german_kettlehat_3_mail_aventail,
    itm_h_chapel_de_fer_mail_aventail,
    itm_h_sallet_curved_mail_aventail,
    itm_h_sallet_curved_mail_collar_bevor,
    
    itm_a_pistoia_mail_a_mail_sleeves_short,
    itm_a_pistoia_mail_b_mail_sleeves_short,
    itm_a_gambeson_crossbowman_custom,
    itm_a_gambeson_asher_regular_custom,
    itm_a_gambeson_asher_belt_custom,
    
    itm_b_high_boots_1,
    itm_b_high_boots_2,
    itm_b_high_boots_3,
    itm_b_high_boots_4,
    itm_b_high_boots_5,
    itm_b_high_boots_6,
    itm_b_high_boots_7,
    itm_b_high_boots_8,
    itm_b_high_boots_9,
    
    itm_w_goedendag,
    itm_w_goedendag_burgundy,
    itm_w_mace_winged,
    itm_w_mace_winged_brown,
    itm_w_mace_winged_red,
    itm_w_onehanded_war_axe_01,
    itm_w_onehanded_war_axe_01_brown,
    itm_w_onehanded_war_axe_01_red,
    itm_w_onehanded_sword_squire,
    itm_w_onehanded_sword_martyr,
    itm_w_onehanded_sword_laird,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    
    itm_w_crossbow_heavy,
    itm_w_war_bow_ash,
    itm_w_war_bow_elm,
    itm_w_war_bow_oak,
    
    itm_w_bolt_triangular_large,
    itm_w_bolt_broadhead,
    itm_w_arrow_triangular_large,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
 

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS CAVALRY ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### Tier 3
  ["custom_merc_scout","Company Scout","Company Scouts", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(15)|str_16|agi_16,  
    wp_melee(120), 
    knows_ironflesh_3|knows_power_strike_3|knows_shield_1|knows_athletics_3|knows_weapon_master_3|knows_riding_2,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_scout_equip","Company Scout","Company Scouts",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_transitional_sallet_1_strap,
    itm_h_german_kettlehat_1_mail_aventail,
    itm_h_german_kettlehat_2_mail_aventail,
    itm_h_german_kettlehat_3_mail_aventail,
    itm_h_chapel_de_fer_mail_aventail,
    itm_h_martinus_kettlehat_1_mail_aventail,

    itm_a_pistoia_mail_a_mail_sleeves_short,
    itm_a_pistoia_mail_b_mail_sleeves_short,

    itm_b_high_boots_1,
    itm_b_high_boots_2,
    itm_b_high_boots_3,
    
    itm_w_native_spear_b,
    itm_w_native_spear_f,
    itm_w_warhammer_1_red,
    itm_w_warhammer_2_red,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
    
    itm_ho_rouncey_1,
    itm_ho_rouncey_2,
    itm_ho_rouncey_3,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_scout_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_transitional_sallet_1_strap,
    itm_h_transitional_sallet_2_strap,
    itm_h_transitional_sallet_3_strap,
    itm_h_german_kettlehat_1_mail_aventail,
    itm_h_german_kettlehat_2_mail_aventail,
    itm_h_german_kettlehat_3_mail_aventail,
    itm_h_german_kettlehat_4_mail_aventail,
    itm_h_german_kettlehat_5_mail_aventail,
    itm_h_german_kettlehat_6_mail_aventail,
    itm_h_german_kettlehat_7_mail_aventail,
    itm_h_chapel_de_fer_mail_aventail,
    itm_h_martinus_kettlehat_1_mail_aventail,
    itm_h_martinus_kettlehat_2_mail_aventail,

    itm_a_pistoia_mail_a_mail_sleeves_short,
    itm_a_pistoia_mail_b_mail_sleeves_short,
    itm_a_pistoia_mail_a_mail_sleeves,
    itm_a_pistoia_mail_b_mail_sleeves,
    itm_a_pistoia_mail_a_mail_sleeves_jackchains,
    itm_a_pistoia_mail_b_mail_sleeves_jackchains,

    itm_b_high_boots_1,
    itm_b_high_boots_2,
    itm_b_high_boots_3,
    itm_b_high_boots_4,
    itm_b_high_boots_5,
    itm_b_high_boots_6,
    itm_b_high_boots_7,
    itm_b_high_boots_8,
    itm_b_high_boots_9,
    
    itm_w_native_spear_b,
    itm_w_native_spear_f,
    itm_w_warhammer_1,
    itm_w_warhammer_1_brown,
    itm_w_warhammer_1_red,
    itm_w_warhammer_2,
    itm_w_warhammer_2_brown,
    itm_w_warhammer_2_red,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_french_3,
    itm_s_heater_shield_french_4,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_english_3,
    itm_s_heater_shield_english_4,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_burgundian_3,
    itm_s_heater_shield_burgundian_4,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
    
    itm_ho_rouncey_1,
    itm_ho_rouncey_2,
    itm_ho_rouncey_3,
    itm_ho_rouncey_4,
    itm_ho_rouncey_5,
    itm_ho_rouncey_6,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_mounted_sergeant","Company Mounted Sergeant","Company Mounted Sergeants", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20,  
    wp_melee(180), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_mounted_sergeant_equip","Company Mounted Sergeant","Company Mounted Sergeants",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    
    itm_a_padded_over_mail_3_custom,
    itm_a_padded_over_mail_4_custom,
    itm_a_padded_over_mail_5_custom,
    itm_a_padded_over_mail_alt_3_custom,
    itm_a_padded_over_mail_alt_4_custom,
    itm_a_padded_over_mail_alt_5_custom,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_light_lance,
    itm_w_warhammer_1_red,
    itm_w_warhammer_2_red,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heraldic_shield_french_1,
    itm_s_heraldic_shield_french_2,
    itm_s_heraldic_shield_english_1,
    itm_s_heraldic_shield_english_2,
    itm_s_heraldic_shield_burgundian_1,
    itm_s_heraldic_shield_burgundian_2,
    itm_s_heraldic_shield_breton_1,
    itm_s_heraldic_shield_breton_2,
    
    itm_ho_courser_1,
    itm_ho_courser_2,
    itm_ho_courser_3,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_mounted_sergeant_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_transitional_sallet_1_mail_aventail,
    itm_h_transitional_sallet_2_mail_aventail,
    itm_h_transitional_sallet_3_mail_aventail,
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_eyeslot_kettlehat_1_mail_aventail,
    itm_h_eyeslot_kettlehat_2_mail_aventail,
    itm_h_eyeslot_kettlehat_3_mail_aventail,
    itm_h_oliphant_eyeslot_kettlehat_mail_aventail,
    itm_h_martinus_kettlehat_3_mail_aventail,
    
    itm_a_brigandine_asher_custom,
    itm_a_brigandine_asher_mail_custom,
    itm_a_brigandine_asher_a_custom,
    itm_a_brigandine_asher_b_custom,
    itm_a_padded_over_mail_3_custom,
    itm_a_padded_over_mail_4_custom,
    itm_a_padded_over_mail_5_custom,
    itm_a_padded_over_mail_alt_3_custom,
    itm_a_padded_over_mail_alt_4_custom,
    itm_a_padded_over_mail_alt_5_custom,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_light_lance,
    itm_w_native_spear_b,
    itm_w_native_spear_f,
    itm_w_warhammer_1,
    itm_w_warhammer_1_brown,
    itm_w_warhammer_1_red,
    itm_w_warhammer_2,
    itm_w_warhammer_2_brown,
    itm_w_warhammer_2_red,
    itm_w_onehanded_falchion_a,
    itm_w_onehanded_falchion_b,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_s_heraldic_shield_french_1,
    itm_s_heraldic_shield_french_2,
    itm_s_heraldic_shield_french_3,
    itm_s_heraldic_shield_french_4,
    itm_s_heraldic_shield_english_1,
    itm_s_heraldic_shield_english_2,
    itm_s_heraldic_shield_english_3,
    itm_s_heraldic_shield_english_4,
    itm_s_heraldic_shield_burgundian_1,
    itm_s_heraldic_shield_burgundian_2,
    itm_s_heraldic_shield_burgundian_3,
    itm_s_heraldic_shield_burgundian_4,
    itm_s_heraldic_shield_breton_1,
    itm_s_heraldic_shield_breton_2,
    itm_s_heraldic_shield_breton_3,
    
    itm_ho_courser_1,
    itm_ho_courser_2,
    itm_ho_courser_3,
    itm_ho_courser_4,
    itm_ho_courser_5,
    itm_ho_courser_6,
    itm_ho_courser_7,
    itm_ho_courser_8,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS DISMOUNTED KNIGHTS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### Tier 4

  ["custom_merc_foot_squire","Company Foot Squire","Company Foot Squires", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20,  
    wp_melee(150), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_foot_squire_equip","Company Foot Squire","Company Foot Squires",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_sallet_mail_aventail,
    itm_h_sallet_curved_mail_aventail,
    itm_h_eyeslot_kettlehat_1_mail_aventail,
    itm_h_eyeslot_kettlehat_2_mail_aventail,
    itm_h_eyeslot_kettlehat_3_mail_aventail,

    itm_a_churburg_13_asher_plain_custom,
    itm_a_churburg_13_asher_brass_custom,
    
    itm_g_gauntlets_mailed,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_bastard_sword_a,
    itm_w_bastard_sword_b,
    
    itm_w_twohanded_war_axe_01,
    itm_w_twohanded_war_axe_02,
    
    itm_w_bardiche_4,
    itm_w_bardiche_5,
    itm_w_bardiche_7,
    itm_w_kriegshammer,
    itm_w_awlpike_1,
    itm_w_awlpike_2,
    itm_w_awlpike_3,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_foot_squire_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_sallet_mail_aventail,
    itm_h_sallet_curved_mail_aventail,
    itm_h_transitional_sallet_1_mail_aventail,
    itm_h_transitional_sallet_2_mail_aventail,
    itm_h_transitional_sallet_3_mail_aventail,
    itm_h_eyeslot_kettlehat_1_mail_aventail,
    itm_h_eyeslot_kettlehat_2_mail_aventail,
    itm_h_eyeslot_kettlehat_3_mail_aventail,

    itm_a_churburg_13_asher_plain_custom,
    itm_a_churburg_13_asher_brass_custom,
    itm_a_brigandine_asher_a_mail_custom,
    itm_a_brigandine_asher_b_mail_custom,
    
    itm_g_gauntlets_mailed,
    itm_g_gauntlets_gilded_mailed,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_bastard_sword_a,
    itm_w_bastard_sword_b,
    itm_w_bastard_sword_c,
    itm_w_bastard_sword_d,
    itm_w_bastard_sword_italian,
    itm_w_bastard_sword_agincourt,
    itm_w_bastard_sword_crecy,
    
    itm_w_twohanded_war_axe_01,
    itm_w_twohanded_war_axe_01_brown,
    itm_w_twohanded_war_axe_01_red,
    itm_w_twohanded_war_axe_02,
    itm_w_twohanded_war_axe_02_brown,
    itm_w_twohanded_war_axe_02_red,    
    
    itm_w_bardiche_4,
    itm_w_bardiche_5,
    itm_w_bardiche_7,
    itm_w_kriegshammer,
    itm_w_kriegshammer_brown,
    itm_w_kriegshammer_ebony,
    itm_w_awlpike_1,
    itm_w_awlpike_2,
    itm_w_awlpike_3,

    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_footman_at_arms","Company Footman-At-Arms","Company Footmen-At-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(28)|str_22|agi_22,  
    wp_melee(180), 
    knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_footman_at_arms_equip","Company Footman-At-Arms","Company Footmen-At-Arms",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_1_visor_1_mail_aventail,
    itm_h_bascinet_1_visor_2_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_2_visor_5_mail_aventail,
    itm_h_bascinet_2_visor_6_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_3_visor_3_mail_aventail,
    itm_h_bascinet_3_visor_4_mail_aventail,
    itm_h_bascinet_3_visor_8_mail_aventail,
    itm_h_bascinet_3_visor_9_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_bascinet_4_visor_3_mail_aventail,
    itm_h_bascinet_4_visor_4_mail_aventail,
    itm_h_bascinet_4_visor_8_mail_aventail,
    itm_h_bascinet_4_visor_9_mail_aventail,
    
    itm_a_continental_plate_mail_short_a,
    itm_a_continental_plate_mail_short_b,
    itm_a_continental_plate_mail_short_c,

    itm_g_gauntlets_segmented_a,

    itm_b_leg_harness_5,
    itm_b_leg_harness_6,
    itm_b_leg_harness_8,
    
    itm_w_bastard_sword_english,
    itm_w_bastard_sword_german,
    itm_w_bastard_sword_italian,
    itm_w_bastard_falchion,
    
    itm_w_kriegshammer,
    
    itm_w_bardiche_1,
    itm_w_bardiche_2,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_footman_at_arms_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_1_visor_1_mail_aventail,
    itm_h_bascinet_1_visor_1_open_mail_aventail,
    itm_h_bascinet_1_visor_2_mail_aventail,
    itm_h_bascinet_1_visor_2_open_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_2_visor_5_mail_aventail,
    itm_h_bascinet_2_visor_5_open_mail_aventail,
    itm_h_bascinet_2_visor_6_mail_aventail,
    itm_h_bascinet_2_visor_6_open_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_3_visor_3_mail_aventail,
    itm_h_bascinet_3_visor_3_open_mail_aventail,
    itm_h_bascinet_3_visor_4_mail_aventail,
    itm_h_bascinet_3_visor_4_open_mail_aventail,
    itm_h_bascinet_3_visor_8_mail_aventail,
    itm_h_bascinet_3_visor_8_open_mail_aventail,
    itm_h_bascinet_3_visor_9_mail_aventail,
    itm_h_bascinet_3_visor_9_open_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_bascinet_4_visor_3_mail_aventail,
    itm_h_bascinet_4_visor_3_open_mail_aventail,
    itm_h_bascinet_4_visor_4_mail_aventail,
    itm_h_bascinet_4_visor_4_open_mail_aventail,
    itm_h_bascinet_4_visor_8_mail_aventail,
    itm_h_bascinet_4_visor_8_open_mail_aventail,
    itm_h_bascinet_4_visor_9_mail_aventail,
    itm_h_bascinet_4_visor_9_open_mail_aventail,
    
    itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1,
    itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_2,
    itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_3,
    itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,
    itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2,
    itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,
    itm_a_continental_plate_mail_short_a,
    itm_a_continental_plate_mail_short_b,
    itm_a_continental_plate_mail_short_c,

    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,

    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    itm_b_leg_harness_5,
    itm_b_leg_harness_6,
    itm_b_leg_harness_8,
    
    itm_w_bastard_sword_english,
    itm_w_bastard_sword_german,
    itm_w_bastard_sword_italian,
    itm_w_bastard_falchion,
    
    itm_w_kriegshammer,
    itm_w_kriegshammer_brown,
    itm_w_kriegshammer_ebony,
    
    itm_w_bardiche_1,
    itm_w_bardiche_2,
    itm_w_bardiche_3,
    itm_w_pollaxe_blunt_05_ash,
    itm_w_pollaxe_blunt_08_ash,
    itm_w_pollaxe_cut_03_ash,
    itm_w_pollaxe_cut_05_ash,

    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_dismounted_knight","Company Dismounted Knight","Company Dismounted Knights", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(30)|str_24|agi_24,  
    wp_melee(200), 
    knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_dismounted_knight_equip","Company Dismounted Knight","Company Dismounted Knights",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_great_bascinet_continental,
    itm_h_great_bascinet_continental_visor_a,
    itm_h_great_bascinet_continental_visor_b,
    itm_h_great_bascinet_continental_visor_c,

    itm_a_plate_kastenbrust_a,
    itm_a_plate_kastenbrust_b,
    itm_a_plate_kastenbrust_c,
    itm_a_english_plate_1415_heraldic,
    
    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,
    
    itm_b_leg_harness_4,
    itm_b_leg_harness_7,
    itm_b_leg_harness_9,
    itm_b_leg_harness_10,
    
    itm_w_twohanded_sword_steward,
    itm_w_twohanded_sword_talhoffer,
    itm_w_twohanded_sword_earl,
    
    itm_w_twohanded_knight_battle_axe_01,
    itm_w_twohanded_knight_battle_axe_02,
    
    itm_w_pollaxe_blunt_03_ash,
    itm_w_pollaxe_cut_03_ash,
    itm_w_pollaxe_cut_05_ash,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_dismounted_knight_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_great_bascinet_continental,
    itm_h_great_bascinet_continental_roundels,
    itm_h_great_bascinet_continental_visor_a,
    itm_h_great_bascinet_continental_visor_a_open,
    itm_h_great_bascinet_continental_visor_b,
    itm_h_great_bascinet_continental_visor_b_open,
    itm_h_great_bascinet_continental_visor_c,
    itm_h_great_bascinet_continental_visor_c_open,

    itm_a_plate_kastenbrust_a,
    itm_a_plate_kastenbrust_b,
    itm_a_plate_kastenbrust_c,
    itm_a_english_plate_1415_heraldic,
    itm_a_jupon_heraldic,
    itm_a_jupon_heraldic_belt_1,
    itm_a_jupon_heraldic_belt_2,
    itm_a_jupon_heraldic_belt_3,
    itm_a_jupon_heraldic_belt_4,
    
    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,
    
    itm_b_leg_harness_4,
    itm_b_leg_harness_7,
    itm_b_leg_harness_9,
    itm_b_leg_harness_10,
    
    itm_w_twohanded_sword_messer,
    itm_w_twohanded_sword_messer_b,
    itm_w_twohanded_sword_steward,
    itm_w_twohanded_sword_talhoffer,
    itm_w_twohanded_sword_earl,
    
    itm_w_twohanded_knight_battle_axe_01,
    itm_w_twohanded_knight_battle_axe_02,
    itm_w_twohanded_knight_battle_axe_03,
    
    itm_w_pollaxe_blunt_01_french_ash,
    itm_w_pollaxe_blunt_02_french_ash,
    itm_w_pollaxe_blunt_03_ash,
    itm_w_pollaxe_blunt_04_english_ash,
    itm_w_pollaxe_cut_01_burgundian_ash,
    itm_w_pollaxe_cut_02_french_ash,
    itm_w_pollaxe_cut_03_ash,
    itm_w_pollaxe_cut_05_ash,

    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS KNIGHTS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["custom_merc_squire","Company Squire","Company Squires", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20,  
    wp_melee(150), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_squire_equip","Company Squire","Company Squires",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_sallet_mail_aventail,
    itm_h_sallet_curved_mail_aventail,
    itm_h_transitional_sallet_1_mail_aventail,
    itm_h_transitional_sallet_2_mail_aventail,
    itm_h_transitional_sallet_3_mail_aventail,

    itm_a_churburg_13_asher_plain_custom,
    itm_a_churburg_13_asher_brass_custom,
    
    itm_g_gauntlets_mailed,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_onehanded_sword_c_long,
    itm_w_onehanded_sword_d_long,
    
    itm_w_onehanded_horseman_axe_02,
    itm_w_mace_winged,
    itm_w_warhammer_1,
    itm_w_warhammer_2,
    
    itm_w_native_spear_b,
    itm_w_native_spear_f,
    
    itm_s_heraldic_shield_heater,
    
    itm_ho_courser_1,
    itm_ho_courser_2,
    itm_ho_courser_3,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_squire_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_sallet_mail_aventail,
    itm_h_sallet_curved_mail_aventail,
    itm_h_transitional_sallet_1_mail_aventail,
    itm_h_transitional_sallet_2_mail_aventail,
    itm_h_transitional_sallet_3_mail_aventail,
    itm_h_eyeslot_kettlehat_1_mail_aventail,
    itm_h_eyeslot_kettlehat_2_mail_aventail,
    itm_h_eyeslot_kettlehat_3_mail_aventail,

    itm_a_churburg_13_asher_plain_custom,
    itm_a_churburg_13_asher_brass_custom,
    itm_a_brigandine_asher_a_mail_custom,
    itm_a_brigandine_asher_b_mail_custom,
    
    itm_g_gauntlets_mailed,
    itm_g_gauntlets_gilded_mailed,
    
    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    
    itm_w_onehanded_sword_squire,
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_c_long,
    itm_w_onehanded_sword_d_long,
    
    itm_w_onehanded_horseman_axe_02,
    itm_w_mace_winged,
    itm_w_warhammer_1,
    itm_w_warhammer_2,
    
    itm_w_native_spear_b,
    itm_w_native_spear_f,
    
    itm_s_heraldic_shield_heater,
    itm_s_heater_shield_french_1,
    itm_s_heater_shield_french_2,
    itm_s_heater_shield_french_3,
    itm_s_heater_shield_french_4,
    itm_s_heater_shield_english_1,
    itm_s_heater_shield_english_2,
    itm_s_heater_shield_english_3,
    itm_s_heater_shield_english_4,
    itm_s_heater_shield_burgundian_1,
    itm_s_heater_shield_burgundian_2,
    itm_s_heater_shield_burgundian_3,
    itm_s_heater_shield_burgundian_4,
    itm_s_heater_shield_breton_1,
    itm_s_heater_shield_breton_2,
    
    itm_ho_courser_1,
    itm_ho_courser_2,
    itm_ho_courser_3,
    itm_ho_courser_4,
    itm_ho_courser_5,
    itm_ho_courser_6,
    itm_ho_courser_7,
    itm_ho_courser_8,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_man_at_arms","Company Man-At-Arms","Company Men-At-Arms", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(30)|str_24|agi_24,  
    wp_melee(200), 
    knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_man_at_arms_equip","Company Man-At-Arms","Company Men-At-Arms",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_1_visor_1_mail_aventail,
    itm_h_bascinet_1_visor_1_open_mail_aventail,
    itm_h_bascinet_1_visor_2_mail_aventail,
    itm_h_bascinet_1_visor_2_open_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_2_visor_5_mail_aventail,
    itm_h_bascinet_2_visor_5_open_mail_aventail,
    itm_h_bascinet_2_visor_6_mail_aventail,
    itm_h_bascinet_2_visor_6_open_mail_aventail,
    
    itm_a_continental_plate_mail_short_a,
    itm_a_continental_plate_mail_short_b,
    itm_a_continental_plate_mail_short_c,

    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,

    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    itm_b_leg_harness_5,
    itm_b_leg_harness_6,
    itm_b_leg_harness_8,
    
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_knight,
    
    itm_w_onehanded_horseman_axe_01,
    itm_w_onehanded_horseman_axe_03,
    
    itm_w_lance_1,
    
    itm_s_heraldic_shield_leather,
    
    itm_ho_horse_barded_black,
    itm_ho_horse_barded_blue,
    itm_ho_horse_barded_brown,
    itm_ho_horse_barded_green,
    itm_ho_horse_barded_red,
    itm_ho_horse_barded_white,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_man_at_arms_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_bascinet_1_mail_aventail,
    itm_h_bascinet_1_visor_1_mail_aventail,
    itm_h_bascinet_1_visor_1_open_mail_aventail,
    itm_h_bascinet_1_visor_2_mail_aventail,
    itm_h_bascinet_1_visor_2_open_mail_aventail,
    itm_h_bascinet_2_mail_aventail,
    itm_h_bascinet_2_visor_5_mail_aventail,
    itm_h_bascinet_2_visor_5_open_mail_aventail,
    itm_h_bascinet_2_visor_6_mail_aventail,
    itm_h_bascinet_2_visor_6_open_mail_aventail,
    itm_h_bascinet_3_mail_aventail,
    itm_h_bascinet_3_visor_3_mail_aventail,
    itm_h_bascinet_3_visor_3_open_mail_aventail,
    itm_h_bascinet_3_visor_4_mail_aventail,
    itm_h_bascinet_3_visor_4_open_mail_aventail,
    itm_h_bascinet_3_visor_8_mail_aventail,
    itm_h_bascinet_3_visor_8_open_mail_aventail,
    itm_h_bascinet_3_visor_9_mail_aventail,
    itm_h_bascinet_3_visor_9_open_mail_aventail,
    itm_h_bascinet_4_mail_aventail,
    itm_h_bascinet_4_visor_3_mail_aventail,
    itm_h_bascinet_4_visor_3_open_mail_aventail,
    itm_h_bascinet_4_visor_4_mail_aventail,
    itm_h_bascinet_4_visor_4_open_mail_aventail,
    itm_h_bascinet_4_visor_8_mail_aventail,
    itm_h_bascinet_4_visor_8_open_mail_aventail,
    itm_h_bascinet_4_visor_9_mail_aventail,
    itm_h_bascinet_4_visor_9_open_mail_aventail,
    
    itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1,
    itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_2,
    itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_3,
    itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,
    itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2,
    itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,
    itm_a_continental_plate_mail_short_a,
    itm_a_continental_plate_mail_short_b,
    itm_a_continental_plate_mail_short_c,

    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,

    itm_b_leg_harness_1,
    itm_b_leg_harness_2,
    itm_b_leg_harness_3,
    itm_b_leg_harness_5,
    itm_b_leg_harness_6,
    itm_b_leg_harness_8,
    
    itm_w_onehanded_sword_defiant,
    itm_w_onehanded_sword_knight,
    itm_w_onehanded_sword_forsaken,
    itm_w_onehanded_sword_martyr,
    
    itm_w_onehanded_horseman_axe_01,
    itm_w_onehanded_horseman_axe_03,
    itm_w_knight_warhammer_1,
    itm_w_knight_warhammer_2,
    itm_w_knight_warhammer_3,
    
    itm_w_lance_1,
    itm_w_lance_2,
    itm_w_lance_3,
    
    itm_s_heraldic_shield_leather,
    itm_s_heraldic_shield_french_1,
    itm_s_heraldic_shield_french_2,
    itm_s_heraldic_shield_french_3,
    itm_s_heraldic_shield_french_4,
    itm_s_heraldic_shield_english_1,
    itm_s_heraldic_shield_english_2,
    itm_s_heraldic_shield_english_3,
    itm_s_heraldic_shield_english_4,
    itm_s_heraldic_shield_burgundian_1,
    itm_s_heraldic_shield_burgundian_2,
    itm_s_heraldic_shield_burgundian_3,
    itm_s_heraldic_shield_burgundian_4,
    itm_s_heraldic_shield_breton_1,
    itm_s_heraldic_shield_breton_2,
    itm_s_heraldic_shield_breton_3,
    
    itm_ho_horse_barded_black,
    itm_ho_horse_barded_blue,
    itm_ho_horse_barded_brown,
    itm_ho_horse_barded_green,
    itm_ho_horse_barded_red,
    itm_ho_horse_barded_white,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_knight","Company Knight","Company Knights", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(35)|str_28|agi_28,  
    wp_melee(250), 
    knows_ironflesh_8|knows_power_strike_8|knows_shield_4|knows_athletics_4|knows_weapon_master_8|knows_riding_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_knight_equip","Company Knight","Company Knights",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    itm_h_great_bascinet_continental,
    itm_h_great_bascinet_continental_visor_a,
    itm_h_great_bascinet_continental_visor_b,
    itm_h_great_bascinet_continental_visor_c,

    itm_a_plate_kastenbrust_a,
    itm_a_plate_kastenbrust_b,
    itm_a_plate_kastenbrust_c,
    itm_a_english_plate_1415_heraldic,
    
    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,
    
    itm_b_leg_harness_4,
    itm_b_leg_harness_7,
    itm_b_leg_harness_9,
    itm_b_leg_harness_10,
    
    itm_s_heraldic_shield_bouche,
    
    itm_w_lance_4_custom,
    
    itm_w_knight_winged_mace,
    itm_w_onehanded_knight_axe_01,
    
    (itm_w_bastard_sword_a,imodbit_masterwork),
    (itm_w_bastard_sword_b,imodbit_masterwork),
    (itm_w_bastard_sword_c,imodbit_masterwork),
    (itm_w_bastard_sword_d,imodbit_masterwork),
    
    itm_ho_horse_barded_black_chamfrom,
    itm_ho_horse_barded_blue_chamfrom,
    itm_ho_horse_barded_brown_chamfrom,
    itm_ho_horse_barded_green_chamfrom,
    itm_ho_horse_barded_red_chamfrom,
    itm_ho_horse_barded_white_chamfrom,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_knight_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    itm_h_great_bascinet_continental,
    itm_h_great_bascinet_continental_roundels,
    itm_h_great_bascinet_continental_visor_a,
    itm_h_great_bascinet_continental_visor_a_open,
    itm_h_great_bascinet_continental_visor_b,
    itm_h_great_bascinet_continental_visor_b_open,
    itm_h_great_bascinet_continental_visor_c,
    itm_h_great_bascinet_continental_visor_c_open,

    itm_a_plate_kastenbrust_a,
    itm_a_plate_kastenbrust_b,
    itm_a_plate_kastenbrust_c,
    itm_a_english_plate_1415_heraldic,
    itm_a_jupon_heraldic,
    itm_a_jupon_heraldic_belt_1,
    itm_a_jupon_heraldic_belt_2,
    itm_a_jupon_heraldic_belt_3,
    itm_a_jupon_heraldic_belt_4,
    
    itm_g_gauntlets_segmented_a,
    itm_g_gauntlets_segmented_b,
    
    itm_b_leg_harness_4,
    itm_b_leg_harness_7,
    itm_b_leg_harness_9,
    itm_b_leg_harness_10,
    
    itm_s_heraldic_shield_bouche,
    
    itm_w_lance_4_custom,
    itm_w_lance_5_custom,
    itm_w_lance_6_custom,
    
    itm_w_knight_winged_mace,
    itm_w_knight_flanged_mace,
    itm_w_onehanded_knight_axe_01,
    itm_w_onehanded_knight_axe_02,
    
    (itm_w_bastard_sword_a,imodbit_masterwork),
    (itm_w_bastard_sword_b,imodbit_masterwork),
    (itm_w_bastard_sword_c,imodbit_masterwork),
    (itm_w_bastard_sword_d,imodbit_masterwork),
    (itm_w_bastard_sword_english,imodbit_masterwork),
    (itm_w_bastard_sword_italian,imodbit_masterwork),
    (itm_w_bastard_sword_german,imodbit_masterwork),
    (itm_w_bastard_sword_agincourt,imodbit_masterwork),
    
    itm_ho_horse_barded_black_chamfrom,
    itm_ho_horse_barded_blue_chamfrom,
    itm_ho_horse_barded_brown_chamfrom,
    itm_ho_horse_barded_green_chamfrom,
    itm_ho_horse_barded_red_chamfrom,
    itm_ho_horse_barded_white_chamfrom,
    
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    

  ["custom_mercs_end","{!}na","{!}na",0,0,0,fac_player_faction,[itm_velvet],def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,swadian_face_middle_1, swadian_face_older_2],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS NPCS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["merc_company_quartermaster","Quartermaster Godefroy de Papincourt","Quartermaster Godefroy de Papincourt",tf_hero|tf_is_merchant|tf_unmoveable_in_party_window,scn_player_camp|entry(2),0,fac_commoners,
   [
   itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,itm_b_leg_harness_8,
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x00000008ff10c002586deeb88a61c50800000000001c56150000000000000000],
   
  ["merc_company_smith","Henri the Smith","Henri the Smith",tf_hero|tf_unmoveable_in_party_window,scn_player_camp|entry(3),0,fac_commoners,
   [
   itm_a_commoner_apron,itm_b_turnshoes_1,
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x00000004bf10b14d5d11ee17d88cc19800000000001cd6820000000000000000],

  ["merc_company_merchant","Harry Ricksson the Merchant","Harry Ricksson the Merchant",tf_hero|tf_is_merchant|tf_unmoveable_in_party_window,scn_player_camp|entry(4),0,fac_commoners,
   [
   itm_h_highlander_beret_red_2,itm_a_huque_2,itm_b_high_boots_1,
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x0000000e3610a4c03f48800102611a8000000000001d40090000000000000000],

  ["merc_company_ransom_broker","Numar the Ransom Broker","Numar the Ransom Broker",tf_hero|tf_is_merchant|tf_unmoveable_in_party_window,scn_player_camp|entry(5),0,fac_commoners,
   [
   itm_a_noble_tunic_custom,itm_b_poulaines_lined_1,
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x0000000eff00854f57237198fb66c55c00000000001cb52a0000000000000000],
   
  ["inventory_backup","{!}Inventory","{!}Inventory",tf_hero|tf_inactive,0,reserved,fac_player_faction,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],
  
  ["merc_company_name","Mercenary Company","Mercenary Company",tf_hero|tf_inactive,0,reserved,fac_player_faction,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],

## DAC Custom Troops (Merc System) End

]