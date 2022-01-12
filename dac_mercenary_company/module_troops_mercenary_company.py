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
  
  ["custom_merc_recruit_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_hood_custom,
    # itm_h_hood_fi_custom,
    # itm_h_simple_coif,
    # itm_h_simple_coif_brown,
    # itm_h_leather_hat_d,
    # itm_h_leather_hat_d_black,
    # itm_h_leather_hat_b,
    
    # itm_a_peasant_man_custom,
    # itm_a_peasant_shirt_custom,
    
    # itm_b_hosen_shoes_custom,
    # itm_b_hosen_poulaines_custom,
    # itm_b_wrapping_boots,
    
    # itm_w_dagger_pikeman,
    # itm_w_archer_hatchet,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_c_small,
    # itm_w_onehanded_sword_c,
    # itm_w_spiked_club,
    # itm_w_mace_knobbed,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_recruit_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_hood_custom,
    # itm_h_hood_fi_custom,
    # itm_h_simple_coif,
    # itm_h_simple_coif_brown,
    # itm_h_leather_hat_d,
    # itm_h_leather_hat_d_black,
    # itm_h_leather_hat_b,
    
    # itm_a_peasant_man_custom,
    # itm_a_peasant_shirt_custom,
    
    # itm_b_hosen_shoes_custom,
    # itm_b_hosen_poulaines_custom,
    # itm_b_wrapping_boots,
    
    # itm_w_dagger_pikeman,
    # itm_w_archer_hatchet,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_c_small,
    # itm_w_onehanded_sword_c,
    # itm_w_spiked_club,
    # itm_w_mace_knobbed,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],

# Tier 2 #

  ["custom_merc_footman","Company Footman","Company Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(15)|str_14|agi_14, 
    wp_melee(140), 
    knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1,
    vaegir_face_old_1, vaegir_face_old_2],
  
  ["custom_merc_footman_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_mail_coif,
    # itm_h_pot_helmet_hood_custom,
    
    # itm_a_gambeson_custom,
    # itm_a_padded_armor_custom,
    # itm_a_padded_cloth_custom,
    
    # itm_b_leather_boots,
    # itm_b_hosen_shoes_custom,
    # itm_b_hosen_poulaines_custom,
    # itm_b_wrapping_boots,
    
    # itm_g_leather_gauntlet,
    
    # itm_s_heraldic_shield_heater,
    
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_c_small,
    # itm_w_onehanded_sword_c,
    # itm_w_mace_spiked,
    # itm_w_spear_4,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_footman_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_mail_coif,
    # itm_h_mail_coif_balaclava,
    # itm_h_pot_helmet_hood_custom,
    # itm_h_pot_helmet_padded,
    
    # itm_a_gambeson_custom,
    # itm_a_padded_armor_custom,
    # itm_a_padded_cloth_custom,
    
    # itm_b_leather_boots,
    # itm_b_hosen_shoes_custom,
    # itm_b_hosen_poulaines_custom,
    # itm_b_wrapping_boots,
    
    # itm_g_leather_gauntlet,
    
    # itm_s_heraldic_shield_heater,
    # itm_s_heater_shield_french_1,
    # itm_s_heater_shield_french_2,
    # itm_s_heater_shield_french_3,
    # itm_s_heater_shield_french_4,
    # itm_s_heater_shield_english_1,
    # itm_s_heater_shield_english_2,
    # itm_s_heater_shield_english_3,
    # itm_s_heater_shield_english_4,
    # itm_s_heater_shield_english_6,
    # itm_s_heater_shield_burgundian_1,
    # itm_s_heater_shield_burgundian_2,
    # itm_s_heater_shield_burgundian_3,
    # itm_s_heater_shield_burgundian_4,
    # itm_s_heater_shield_breton_1,
    # itm_s_heater_shield_breton_2,
    # itm_s_heater_shield_breton_4,
    
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_c_small,
    # itm_w_onehanded_sword_c,
    # itm_w_mace_spiked,
    # itm_w_mace_winged,
    # itm_w_spear_7,
    # itm_w_spear_6,
    # itm_w_spear_4,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],

# Tier 3 #

  ["custom_merc_veteran","Company Veteran","Company Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(20)|str_16|agi_16, 
    wp_melee(160), 
    knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2,
    mercenary_face_1, mercenary_face_2],
  
  ["custom_merc_veteran_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_pot_helmet_mail,
    # itm_h_cerveliere_hood_custom,
    # itm_h_sallet_hood_custom,
    
    # itm_a_aketon_narf_custom,
    # itm_a_aketon_jackchain_narf_custom,
    
    # itm_b_leather_boots,
    
    # itm_g_leather_gauntlet,
    # itm_g_mail_gauntlets,
    # itm_g_demi_gauntlets,
    
    # itm_w_onehanded_war_axe_01,
    # itm_w_onehanded_war_axe_02,
    # itm_w_mace_winged,
    # itm_w_spear_1,
    # itm_w_spear_8,
    
    # itm_w_onehanded_sword_a_long,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_d,
    # itm_w_onehanded_sword_d_long,
    
    # itm_s_heraldic_shield_leather,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_veteran_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_pot_helmet_mail,
    # itm_h_cerveliere_hood_custom,
    # itm_h_sallet_hood_custom,
    # itm_h_chapel_de_fer_1_hood_custom,
    # itm_h_chapel_de_fer_2_hood_custom,
    # itm_h_chapel_de_fer_3_hood_custom,
    # itm_h_chapel_de_fer_4_hood_custom,
    # itm_h_kettlehat_hood_custom,
    # itm_h_kettlehat_2_hood_custom,
    # itm_h_kettlehat_3_hood_custom,
    # itm_h_kettlehat_4_hood_custom,
    
    # itm_a_aketon_narf_custom,
    # itm_a_aketon_jackchain_narf_custom,
    # itm_a_mail_shirt_custom,
    # itm_a_gambeson_narf_breastplate_custom,
    
    # itm_b_leather_boots,
    # itm_b_mail_chausses,
    # itm_b_mail_boots,
    
    # itm_g_leather_gauntlet,
    # itm_g_mail_gauntlets,
    # itm_g_demi_gauntlets,
    
    # itm_w_onehanded_war_axe_01,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_war_axe_04,
    # itm_w_mace_winged,
    # itm_w_warhammer_1,
    # itm_w_warhammer_1_alt,
    # itm_w_spear_1,
    # itm_w_spear_8,
    
    # itm_w_onehanded_sword_forsaken,
    # itm_w_onehanded_sword_squire,
    # itm_w_onehanded_sword_a_long,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_d,
    # itm_w_onehanded_sword_d_long,
    
    # itm_s_heraldic_shield_leather,
    # itm_s_heraldic_shield_french_1,
    # itm_s_heraldic_shield_french_2,
    # itm_s_heraldic_shield_french_3,
    # itm_s_heraldic_shield_french_4,
    # itm_s_heraldic_shield_english_1,
    # itm_s_heraldic_shield_english_2,
    # itm_s_heraldic_shield_english_3,
    # itm_s_heraldic_shield_english_4,
    # itm_s_heraldic_shield_burgundian_1,
    # itm_s_heraldic_shield_burgundian_2,
    # itm_s_heraldic_shield_burgundian_3,
    # itm_s_heraldic_shield_burgundian_4,
    # itm_s_heraldic_shield_burgundian_7,
    # itm_s_heraldic_shield_breton_1,
    # itm_s_heraldic_shield_breton_2,
    # itm_s_heraldic_shield_breton_3,
    
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],

# Tier 4 #

  ["custom_merc_sergeant","Company Sergeant","Company Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20, 
    wp_melee(180), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5,
    mercenary_face_1, mercenary_face_2],
  
  ["custom_merc_sergeant_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_bascinet_fi_padded,
    # itm_h_bascinet_fi_mail,
    # itm_h_kettlehat_eyeslot_padded,
    # itm_h_kettlehat_eyeslot_mail,
    # itm_h_sallet_mail,
    # itm_h_cerveliere_mail,
    
    # itm_a_padded_over_mail_custom,
    # itm_a_brigandine_narf_padded_jackchain_custom,
    # itm_a_brigandine_narf_padded_jackchain_plate_hose_custom,
    
    # itm_b_mail_boots,
    
    # itm_g_demi_gauntlets,
    # itm_g_finger_gauntlets,
    
    # itm_w_onehanded_war_axe_01,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_war_axe_04,
    # itm_w_warhammer_1,
    # itm_w_warhammer_1_alt,
    # itm_w_warhammer_2,
    # itm_w_warhammer_2_alt,
    # itm_w_spear_4,
    # itm_w_spear_5,

    # itm_w_onehanded_sword_monarch,
    # itm_w_onehanded_sword_forsaken,
    
    # itm_s_heraldic_shield_pavise,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_sergeant_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_bascinet_fi_padded,
    # itm_h_bascinet_fi_mail,
    # itm_h_kettlehat_eyeslot_padded,
    # itm_h_kettlehat_eyeslot_mail,
    # itm_h_sallet_mail,
    # itm_h_cerveliere_mail,
    
    # itm_a_hauberk_narf,
    # itm_a_hauberk_narf_plate_hose,
    # itm_a_hauberk_narf_jackchain,
    # itm_a_hauberk_narf_jackchain_plate_hose,
    # itm_a_padded_over_mail_custom,
    # itm_a_brigandine_narf_padded_jackchain_custom,
    # itm_a_brigandine_narf_padded_jackchain_plate_hose_custom,
    
    # itm_b_mail_boots,
    # itm_b_steel_greaves,
    
    # itm_g_demi_gauntlets,
    # itm_g_finger_gauntlets,
    
    # itm_w_onehanded_war_axe_01,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_war_axe_04,
    # itm_w_warhammer_1,
    # itm_w_warhammer_1_alt,
    # itm_w_warhammer_2,
    # itm_w_warhammer_2_alt,
    # itm_w_spear_4,
    # itm_w_spear_5,

    # itm_w_onehanded_sword_monarch,
    # itm_w_bastard_sword_a,
    # itm_w_bastard_sword_b,
    # itm_w_onehanded_sword_forsaken,
    
    # itm_s_heraldic_shield_pavise,
    # itm_s_pavise_french_1,
    # itm_s_pavise_french_2,
    # itm_s_pavise_french_3,
    # itm_s_pavise_french_4,
    # itm_s_pavise_burgundian_1,
    # itm_s_pavise_burgundian_2,
    # itm_s_pavise_burgundian_3,
    # itm_s_pavise_burgundian_4,
    # itm_s_pavise_breton_1,
    # itm_s_pavise_breton_2,
    # itm_s_pavise_breton_3,
    # itm_s_pavise_flemish_1,
    # itm_s_pavise_flemish_2,
    # itm_s_pavise_flemish_3,
    # itm_s_pavise_flemish_4,

    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0],
    
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS RANGED ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["custom_merc_skirmisher","Company Skirmisher","Company Skirmishers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_player_faction,[],
    level(8)|str_10|agi_12,  
    wpex(90,90,90,100,100,100), 
    knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_skirmisher_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_hood_custom,
    # itm_h_hood_fi_custom,
    # itm_h_simple_coif,
    # itm_h_simple_coif_brown,
    # itm_h_leather_hat_d,
    # itm_h_leather_hat_d_black,
    # itm_h_leather_hat_b,
    
    # itm_a_peasant_man_custom,
    # itm_a_peasant_shirt_custom,
    
    # itm_b_hosen_shoes_custom,
    # itm_b_hosen_poulaines_custom,
    # itm_b_wrapping_boots,
    
    # itm_w_short_bow_elm,
    # itm_w_short_bow_oak,
    # itm_w_short_bow_ash,
    
    # itm_w_arrow_triangular,
    # itm_w_arrow_triangular,
    
    # itm_w_dagger_pikeman,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_spiked_club,
    # itm_w_mace_knobbed,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_skirmisher_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_hood_custom,
    # itm_h_hood_fi_custom,
    # itm_h_simple_coif,
    # itm_h_simple_coif_brown,
    # itm_h_leather_hat_d,
    # itm_h_leather_hat_d_black,
    # itm_h_leather_hat_b,
    
    # itm_a_peasant_man_custom,
    # itm_a_peasant_shirt_custom,
    
    # itm_b_hosen_shoes_custom,
    # itm_b_hosen_poulaines_custom,
    # itm_b_wrapping_boots,
    
    # itm_w_short_bow_elm,
    # itm_w_short_bow_oak,
    # itm_w_short_bow_ash,
    
    # itm_w_arrow_triangular,
    # itm_w_arrow_triangular,
    
    # itm_w_dagger_pikeman,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_spiked_club,
    # itm_w_mace_knobbed,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_ranger","Company Ranger","Company Rangers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_player_faction,[],
    level(12)|str_12|agi_14,  
    wpex(100,100,100,120,120,120), 
    knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2,
    mercenary_face_1, mercenary_face_2],
 
  ["custom_merc_ranger_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_pot_helmet_hood_custom,
    # itm_h_round_kettlehat_hood_custom,
    # itm_h_kettlehat_hood_custom,
    
    # itm_a_gambeson_custom,
    # itm_a_padded_armor_custom,
    # itm_a_padded_cloth_custom,
    
    # itm_b_ankle_boots,
    # itm_b_leather_boots,
    
    # itm_g_leather_gauntlet,
    
    # itm_w_war_bow_ash,
    # itm_w_war_bow_elm,
    # itm_w_arrow_triangular,
    
    # itm_w_crossbow_light,
    # itm_w_bolt_triangular,
    
    # itm_w_spiked_club,
    # itm_w_mace_knobbed,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_sword_c_small,
    # itm_w_onehanded_sword_a,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_ranger_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_pot_helmet_hood_custom,
    # itm_h_round_kettlehat_hood_custom,
    # itm_h_kettlehat_hood_custom,
    # itm_h_kettlehat_2_hood_custom,
    # itm_h_kettlehat_3_hood_custom,
    # itm_h_kettlehat_4_hood_custom,
    # itm_h_chapel_de_fer_1_hood_custom,
    # itm_h_chapel_de_fer_2_hood_custom,
    # itm_h_chapel_de_fer_3_hood_custom,
    # itm_h_chapel_de_fer_4_hood_custom,
    # itm_h_pot_helmet_padded,
    # itm_h_pot_helmet_mail,
    
    # itm_a_gambeson_custom,
    # itm_a_padded_armor_custom,
    # itm_a_padded_cloth_custom,
    # itm_a_leather_vest_custom,
    # itm_a_leather_armor_custom,
    
    # itm_b_ankle_boots,
    # itm_b_leather_boots,
    
    # itm_g_leather_gauntlet,
    
    # itm_w_war_bow_ash,
    # itm_w_war_bow_elm,
    # itm_w_arrow_triangular,
    
    # itm_w_crossbow_light,
    # itm_w_bolt_triangular,
    
    # itm_w_spiked_club,
    # itm_w_mace_knobbed,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_sword_c_small,
    # itm_w_onehanded_sword_a,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_marksman","Company Marksman","Company Marksmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_player_faction,[],
    level(18)|str_14|agi_16,  
    wpex(120,120,120,150,150,150), 
    knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3,
    mercenary_face_1, mercenary_face_2],
   
  ["custom_merc_marksman_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_round_kettlehat_padded,
    # itm_h_kettlehat_padded,
    
    # itm_a_aketon_narf_custom,
    # itm_a_aketon_jackchain_narf_custom,
    
    # itm_b_leather_boots,
    
    # itm_g_leather_gauntlet,
    # itm_g_demi_gauntlets,
    
    # itm_w_long_bow_ash,
    # itm_w_long_bow_elm,
    # itm_w_arrow_triangular,
    
    # itm_w_crossbow_medium,
    # itm_w_bolt_triangular,
    
    # itm_w_mace_spiked,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_sword_c,
    # itm_w_onehanded_sword_c_small,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_marksman_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_bascinet_fi_hood_custom,
    # itm_h_cerveliere_hood_custom,
    # itm_h_round_kettlehat_padded,
    # itm_h_sallet_hood_custom,
    # itm_h_kettlehat_padded,
    # itm_h_kettlehat_2_padded,
    # itm_h_kettlehat_3_padded,
    # itm_h_kettlehat_4_padded,
    # itm_h_chapel_de_fer_1_padded,
    # itm_h_chapel_de_fer_2_padded,
    # itm_h_chapel_de_fer_3_padded,
    # itm_h_chapel_de_fer_4_padded,
    
    # itm_a_aketon_narf_custom,
    # itm_a_aketon_jackchain_narf_custom,
    
    # itm_b_leather_boots,
    
    # itm_g_leather_gauntlet,
    # itm_g_demi_gauntlets,
    
    # itm_w_long_bow_ash,
    # itm_w_long_bow_elm,
    # itm_w_arrow_triangular,
    
    # itm_w_crossbow_medium,
    # itm_w_bolt_triangular,
    
    # itm_w_mace_spiked,
    # itm_w_onehanded_war_axe_02,
    # itm_w_onehanded_war_axe_03,
    # itm_w_onehanded_sword_c,
    # itm_w_onehanded_sword_c_small,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
 

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS CAVALRY ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["custom_merc_scout","Company Scout","Company Scouts", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(15)|str_16|agi_16,  
    wp_melee(120), 
    knows_ironflesh_3|knows_power_strike_3|knows_shield_1|knows_athletics_3|knows_weapon_master_3|knows_riding_2,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_scout_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_pot_helmet_mail,
    # itm_h_cerveliere_hood_custom,
    # itm_h_sallet_hood_custom,
    
    # itm_a_aketon_narf_custom,
    # itm_a_aketon_jackchain_narf_custom,
    
    # itm_b_mail_chausses,
    
    # itm_g_leather_gauntlet,
    # itm_g_mail_gauntlets,
    # itm_g_demi_gauntlets,
    
    # itm_w_mace_winged,
    # itm_w_native_spear_b,
    # itm_w_native_spear_f,
    # itm_w_native_spear_b_custom,
    # itm_w_native_spear_f_custom,
    
    # itm_w_onehanded_sword_squire,
    # itm_w_onehanded_sword_a_long,
    # itm_w_onehanded_sword_d_long,
    
    # itm_s_heraldic_shield_heater,
    
    # itm_ho_courser_1,
    # itm_ho_courser_2,
    # itm_ho_courser_3,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_scout_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_pot_helmet_mail,
    # itm_h_cerveliere_hood_custom,
    # itm_h_sallet_hood_custom,
    # itm_h_chapel_de_fer_1_hood_custom,
    # itm_h_chapel_de_fer_2_hood_custom,
    # itm_h_chapel_de_fer_3_hood_custom,
    # itm_h_chapel_de_fer_4_hood_custom,
    # itm_h_kettlehat_hood_custom,
    # itm_h_kettlehat_2_hood_custom,
    # itm_h_kettlehat_3_hood_custom,
    # itm_h_kettlehat_4_hood_custom,
    
    # itm_a_aketon_narf_custom,
    # itm_a_aketon_jackchain_narf_custom,
    # itm_a_mail_shirt_custom,
    # itm_a_gambeson_narf_breastplate_custom,
    
    # itm_b_leather_boots,
    # itm_b_mail_chausses,
    # itm_b_mail_boots,
    
    # itm_g_leather_gauntlet,
    # itm_g_mail_gauntlets,
    # itm_g_demi_gauntlets,
    
    # itm_w_mace_winged,
    # itm_w_native_spear_b,
    # itm_w_native_spear_f,
    # itm_w_native_spear_b_custom,
    # itm_w_native_spear_f_custom,
    
    # itm_w_onehanded_sword_forsaken,
    # itm_w_onehanded_sword_squire,
    # itm_w_onehanded_sword_a_long,
    # itm_w_onehanded_sword_a,
    # itm_w_onehanded_sword_d,
    # itm_w_onehanded_sword_d_long,
    
    # itm_s_heraldic_shield_heater,
    # itm_s_heater_shield_french_1,
    # itm_s_heater_shield_french_2,
    # itm_s_heater_shield_french_3,
    # itm_s_heater_shield_french_4,
    # itm_s_heater_shield_english_1,
    # itm_s_heater_shield_english_2,
    # itm_s_heater_shield_english_3,
    # itm_s_heater_shield_english_4,
    # itm_s_heater_shield_english_6,
    # itm_s_heater_shield_burgundian_1,
    # itm_s_heater_shield_burgundian_2,
    # itm_s_heater_shield_burgundian_3,
    # itm_s_heater_shield_burgundian_4,
    # itm_s_heater_shield_breton_1,
    # itm_s_heater_shield_breton_2,
    # itm_s_heater_shield_breton_4,
    
    # itm_ho_courser_1,
    # itm_ho_courser_2,
    # itm_ho_courser_3,
    # itm_ho_courser_4,
    # itm_ho_courser_5,
    # itm_ho_courser_6,
    # itm_ho_courser_7,
    # itm_ho_courser_8,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_mounted_sergeant","Company Mounted Sergeant","Company Mounted Sergeants", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20,  
    wp_melee(180), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_mounted_sergeant_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_bascinet_fi_padded,
    # itm_h_bascinet_fi_mail,
    # itm_h_sallet_mail,
    # itm_h_cerveliere_mail,
    
    # itm_a_padded_over_mail_custom,
    # itm_a_brigandine_narf_padded_jackchain_custom,
    # itm_a_brigandine_narf_padded_jackchain_plate_hose_custom,
    
    # itm_b_mail_boots,
    # itm_b_steel_greaves,
    
    # itm_g_demi_gauntlets,
    # itm_g_finger_gauntlets,
    
    # itm_w_native_spear_b,
    # itm_w_native_spear_f,
    # itm_w_native_spear_b_custom,
    # itm_w_native_spear_f_custom,

    # itm_w_onehanded_sword_monarch,
    # itm_w_onehanded_sword_forsaken,
    
    # itm_s_heraldic_shield_heater,
    
    # itm_ho_rouncey_1,
    # itm_ho_rouncey_2,
    # itm_ho_rouncey_3,
    # itm_ho_rouncey_4,
    # itm_ho_rouncey_5,
    # itm_ho_rouncey_6,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_mounted_sergeant_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_bascinet_fi_padded,
    # itm_h_bascinet_fi_mail,
    # itm_h_sallet_mail,
    # itm_h_cerveliere_mail,
    
    # itm_a_hauberk_narf,
    # itm_a_hauberk_narf_plate_hose,
    # itm_a_hauberk_narf_jackchain,
    # itm_a_hauberk_narf_jackchain_plate_hose,
    # itm_a_padded_over_mail_custom,
    # itm_a_brigandine_narf_padded_jackchain_custom,
    # itm_a_brigandine_narf_padded_jackchain_plate_hose_custom,
    
    # itm_b_mail_boots,
    # itm_b_steel_greaves,
    
    # itm_g_demi_gauntlets,
    # itm_g_finger_gauntlets,
    
    # itm_w_native_spear_b,
    # itm_w_native_spear_f,
    # itm_w_native_spear_b_custom,
    # itm_w_native_spear_f_custom,

    # itm_w_onehanded_sword_monarch,
    # itm_w_bastard_sword_a,
    # itm_w_bastard_sword_b,
    # itm_w_onehanded_sword_forsaken,
    
    # itm_s_heraldic_shield_heater,
    # itm_s_heater_shield_french_1,
    # itm_s_heater_shield_french_2,
    # itm_s_heater_shield_french_3,
    # itm_s_heater_shield_french_4,
    # itm_s_heater_shield_english_1,
    # itm_s_heater_shield_english_2,
    # itm_s_heater_shield_english_3,
    # itm_s_heater_shield_english_4,
    # itm_s_heater_shield_english_6,
    # itm_s_heater_shield_burgundian_1,
    # itm_s_heater_shield_burgundian_2,
    # itm_s_heater_shield_burgundian_3,
    # itm_s_heater_shield_burgundian_4,
    # itm_s_heater_shield_breton_1,
    # itm_s_heater_shield_breton_2,
    # itm_s_heater_shield_breton_4,
    
    # itm_ho_rouncey_1,
    # itm_ho_rouncey_2,
    # itm_ho_rouncey_3,
    # itm_ho_rouncey_4,
    # itm_ho_rouncey_5,
    # itm_ho_rouncey_6,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS DISMOUNTED KNIGHTS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["custom_merc_foot_squire","Company Foot Squire","Company Foot Squires", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20,  
    wp_melee(150), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_foot_squire_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_sallet_mail,
    # itm_h_chapel_de_fer_1_mail,
    # itm_h_chapel_de_fer_2_mail,
    # itm_h_chapel_de_fer_3_mail,
    # itm_h_kettlehat_mail,
    # itm_h_kettlehat_painted_mail,
    
    # itm_a_churburg_narf_custom,
    # itm_a_churburg_brass_narf_custom,
    
    # itm_b_steel_greaves,
    
    # itm_g_mail_gauntlets,
    # itm_g_demi_gauntlets,
    
    # itm_w_bastard_sword_a,
    # itm_w_bastard_sword_b,
    # itm_w_bastard_sword_c,
    
    # itm_w_warhammer_2,
    # itm_w_warhammer_1,
    # itm_w_mace_winged,
    
    # itm_w_ranseur_1,
    # itm_w_ranseur_2,
    
    # itm_s_heraldic_shield_heater,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_foot_squire_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_sallet_mail,
    # itm_h_chapel_de_fer_1_mail,
    # itm_h_chapel_de_fer_2_mail,
    # itm_h_chapel_de_fer_3_mail,
    # itm_h_kettlehat_mail,
    # itm_h_kettlehat_painted_mail,
    # itm_h_bascinet_oniontop,
    # itm_h_zitta_bascinet_novisor,
    
    # itm_a_churburg_narf_custom,
    # itm_a_churburg_brass_narf_custom,
    
    # itm_b_steel_greaves,
    
    # itm_g_mail_gauntlets,
    # itm_g_demi_gauntlets,
    
    # itm_w_bastard_sword_a,
    # itm_w_bastard_sword_b,
    # itm_w_bastard_sword_c,
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_agincourt,
    # itm_w_bastard_sword_baron,
    # itm_w_bastard_sword_mercenary,
    
    # itm_w_warhammer_2,
    # itm_w_warhammer_1,
    # itm_w_mace_winged,
    
    # itm_w_ranseur_1,
    # itm_w_ranseur_2,
    
    # itm_s_heraldic_shield_heater,
    # itm_s_heater_shield_french_1,
    # itm_s_heater_shield_french_2,
    # itm_s_heater_shield_french_3,
    # itm_s_heater_shield_french_4,
    # itm_s_heater_shield_english_1,
    # itm_s_heater_shield_english_2,
    # itm_s_heater_shield_english_3,
    # itm_s_heater_shield_english_4,
    # itm_s_heater_shield_english_6,
    # itm_s_heater_shield_burgundian_1,
    # itm_s_heater_shield_burgundian_2,
    # itm_s_heater_shield_burgundian_3,
    # itm_s_heater_shield_burgundian_4,
    # itm_s_heater_shield_breton_1,
    # itm_s_heater_shield_breton_2,
    # itm_s_heater_shield_breton_4,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_footman_at_arms","Company Footman-At-Arms","Company Footmen-At-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(28)|str_22|agi_22,  
    wp_melee(180), 
    knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_footman_at_arms_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_zitta_bascinet_novisor,
    # itm_h_bascinet_oniontop,
    # itm_h_klappvisier_pigface_open,
    # itm_h_klappvisier_pigface,
    
    # itm_a_corrazina_narf_custom,
    # itm_a_corrazina_leather_custom,
    
    # itm_b_steel_greaves,
    # itm_b_steel_greaves_full,
    
    # itm_g_finger_gauntlets,
    # itm_g_wisby_gauntlets_black,
    # itm_g_wisby_gauntlets_red,
    
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_c,
    
    # itm_s_heraldic_shield_leather,
    
    # itm_w_twohanded_knight_battle_axe_01,
    # itm_w_knight_winged_mace,
    # itm_w_polehammer_1,
    # itm_w_polehammer_2,
    # itm_w_poleaxe_3,
    # itm_w_poleaxe_2,
    # itm_w_poleaxe_1
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_footman_at_arms_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_zitta_bascinet_novisor,
    # itm_h_bascinet_oniontop,
    # itm_h_klappvisier_pigface_open,
    # itm_h_klappvisier_pigface,
    
    # itm_a_corrazina_narf_custom,
    # itm_a_corrazina_leather_custom,
    
    # itm_b_steel_greaves,
    # itm_b_steel_greaves_full,
    
    # itm_g_finger_gauntlets,
    # itm_g_wisby_gauntlets_black,
    # itm_g_wisby_gauntlets_red,
    
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_c,
    # itm_w_bastard_sword_agincourt,
    # itm_w_bastard_sword_crecy,
    # itm_w_bastard_sword_duke,
    
    # itm_s_heraldic_shield_leather,
    # itm_s_heraldic_shield_french_1,
    # itm_s_heraldic_shield_french_2,
    # itm_s_heraldic_shield_french_3,
    # itm_s_heraldic_shield_french_4,
    # itm_s_heraldic_shield_english_1,
    # itm_s_heraldic_shield_english_2,
    # itm_s_heraldic_shield_english_3,
    # itm_s_heraldic_shield_english_4,
    # itm_s_heraldic_shield_burgundian_1,
    # itm_s_heraldic_shield_burgundian_2,
    # itm_s_heraldic_shield_burgundian_3,
    # itm_s_heraldic_shield_burgundian_4,
    # itm_s_heraldic_shield_burgundian_7,
    # itm_s_heraldic_shield_breton_1,
    # itm_s_heraldic_shield_breton_2,
    # itm_s_heraldic_shield_breton_3,
    
    # itm_w_twohanded_knight_battle_axe_01,
    # itm_w_knight_winged_mace,
    # itm_w_polehammer_1,
    # itm_w_polehammer_2,
    # itm_w_poleaxe_3,
    # itm_w_poleaxe_2,
    # itm_w_poleaxe_1,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_dismounted_knight","Company Dismounted Knight","Company Dismounted Knights", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(30)|str_24|agi_24,  
    wp_melee(200), 
    knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_dismounted_knight_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_bascinet_great,
    # itm_h_zitta_bascinet,
    # itm_h_hounskull_narf,
    # itm_h_klappvisier_pigface,
    # itm_h_bascinet_great_fi,
    
    # itm_a_plate_harness_1,
    # itm_a_plate_harness_2,
    
    # itm_b_shynbaulds,
    
    # itm_g_hourglass_gauntlets,
    # itm_g_hourglass_gauntlets_ornate,
    
    # itm_s_heraldic_shield_metal,
    
    # itm_w_twohanded_knight_battle_axe_01,
    # itm_w_knight_winged_mace,
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_c,
    
    # itm_w_twohanded_war_axe_03,
    # itm_w_twohanded_sword_talhoffer,
    # itm_w_twohanded_sword_steward,
    # itm_w_poleaxe_3,
    # itm_w_poleaxe_2,
    # itm_w_poleaxe_1,
    # itm_w_polehammer_2,
    # itm_w_polehammer_1,
    # itm_w_bec_de_corbin,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_dismounted_knight_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_bascinet_great,
    # itm_h_zitta_bascinet,
    # itm_h_hounskull_narf,
    # itm_h_klappvisier_pigface,
    # itm_h_bascinet_great_fi,
    
    # itm_a_plate_harness_1,
    # itm_a_plate_harness_2,
    
    # itm_b_shynbaulds,
    
    # itm_g_hourglass_gauntlets,
    # itm_g_hourglass_gauntlets_ornate,
    
    # itm_s_heraldic_shield_metal,
    # itm_s_heraldic_shield_french_1,
    # itm_s_heraldic_shield_french_2,
    # itm_s_heraldic_shield_french_3,
    # itm_s_heraldic_shield_french_4,
    # itm_s_heraldic_shield_english_1,
    # itm_s_heraldic_shield_english_2,
    # itm_s_heraldic_shield_english_3,
    # itm_s_heraldic_shield_english_4,
    # itm_s_heraldic_shield_burgundian_1,
    # itm_s_heraldic_shield_burgundian_2,
    # itm_s_heraldic_shield_burgundian_3,
    # itm_s_heraldic_shield_burgundian_4,
    # itm_s_heraldic_shield_burgundian_7,
    # itm_s_heraldic_shield_breton_1,
    # itm_s_heraldic_shield_breton_2,
    # itm_s_heraldic_shield_breton_3,
    
    # itm_w_twohanded_knight_battle_axe_01,
    # itm_w_knight_winged_mace,
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_c,
    
    # itm_w_twohanded_war_axe_03,
    # itm_w_twohanded_sword_talhoffer,
    # itm_w_twohanded_sword_steward,
    # itm_w_poleaxe_3,
    # itm_w_poleaxe_2,
    # itm_w_poleaxe_1,
    # itm_w_polehammer_2,
    # itm_w_polehammer_1,
    # itm_w_bec_de_corbin,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS KNIGHTS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["custom_merc_squire","Company Squire","Company Squires", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(25)|str_20|agi_20,  
    wp_melee(150), 
    knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_squire_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_mail_coif,
    # itm_h_mail_coif_balaclava,
    # itm_h_kettlehat_painted_hood_custom,
    # itm_h_kettlehat_hood_custom,
    # itm_h_bascinet_fi_hood_custom,
    
    # itm_heraldic_tunic_new,
    # itm_heraldic_mail_tabard,
    
    # itm_b_mail_chausses,
    
    # itm_g_mail_gauntlets,
    
    # itm_w_onehanded_sword_d_long,
    # itm_w_onehanded_sword_c_long,
    # itm_w_onehanded_sword_a_long,
    
    # itm_w_native_spear_b_heraldic,
    # itm_w_native_spear_f_heraldic,
    
    # itm_w_onehanded_horseman_axe_01,
    # itm_w_mace_winged,
    # itm_w_mace_spiked,
    
    # itm_s_heraldic_shield_heater,
    
    # itm_ho_rouncey_1,
    # itm_ho_rouncey_2,
    # itm_ho_rouncey_3,
    # itm_ho_rouncey_4,
    # itm_ho_rouncey_5,
    # itm_ho_rouncey_6,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_squire_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_mail_coif,
    # itm_h_mail_coif_balaclava,
    # itm_h_kettlehat_painted_hood_custom,
    # itm_h_kettlehat_hood_custom,
    # itm_h_bascinet_fi_hood_custom,
    
    # itm_heraldic_tunic_new,
    # itm_heraldic_mail_tabard,
    # itm_heraldic_brigandine_narf_padded_full_plate_hose_custom,
    # itm_heraldic_brigandine_narf_padded_jackchain_full_plate_hose_custom,
    
    # itm_b_mail_boots,
    # itm_b_mail_chausses,
    
    # itm_g_mail_gauntlets,
    
    # itm_w_onehanded_sword_squire,
    # itm_w_onehanded_sword_martyr,
    # itm_w_onehanded_sword_defiant,
    # itm_w_onehanded_sword_d_long,
    # itm_w_onehanded_sword_c_long,
    # itm_w_onehanded_sword_a_long,
    
    # itm_w_light_lance_heraldic,
    # itm_w_native_spear_b_heraldic,
    # itm_w_native_spear_f_heraldic,
    
    # itm_w_onehanded_horseman_axe_01,
    # itm_w_mace_winged,
    # itm_w_mace_spiked,
    
    # itm_s_heraldic_shield_heater,
    # itm_s_heater_shield_french_1,
    # itm_s_heater_shield_french_2,
    # itm_s_heater_shield_french_3,
    # itm_s_heater_shield_french_4,
    # itm_s_heater_shield_english_1,
    # itm_s_heater_shield_english_2,
    # itm_s_heater_shield_english_3,
    # itm_s_heater_shield_english_4,
    # itm_s_heater_shield_english_6,
    # itm_s_heater_shield_burgundian_1,
    # itm_s_heater_shield_burgundian_2,
    # itm_s_heater_shield_burgundian_3,
    # itm_s_heater_shield_burgundian_4,
    # itm_s_heater_shield_breton_1,
    # itm_s_heater_shield_breton_2,
    # itm_s_heater_shield_breton_4,
    
    # itm_ho_rouncey_1,
    # itm_ho_rouncey_2,
    # itm_ho_rouncey_3,
    # itm_ho_rouncey_4,
    # itm_ho_rouncey_5,
    # itm_ho_rouncey_6,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_man_at_arms","Company Man-At-Arms","Company Men-At-Arms", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(30)|str_24|agi_24,  
    wp_melee(200), 
    knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_man_at_arms_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_bascinet_fi_noseguard,
    # itm_h_zitta_bascinet_novisor,
    # itm_h_bascinet_oniontop,
    # itm_h_bascinet_fi_mail,
    # itm_h_houndskull_fi,
    
    # itm_a_brigandine_narf_padded_plate_disc_plate_hose_custom,
    # itm_a_brigandine_narf_mail_plate_hose_custom,
    
    # itm_b_mail_boots,
    # itm_b_mail_chausses,
    
    # itm_g_mail_gauntlets,
    
    # itm_w_onehanded_sword_knight,
    # itm_w_onehanded_sword_squire,
    # itm_w_onehanded_sword_laird,
    # itm_w_onehanded_horseman_axe_01,
    # itm_w_onehanded_horseman_axe_02,
    # itm_w_knight_warhammer_1,
    # itm_w_knight_winged_mace,
    # itm_w_knight_warhammer_2,
    # itm_w_lance_1_custom,
    # itm_w_lance_2_custom,
    # itm_w_lance_3_custom,
    
    # itm_ho_courser_1,
    # itm_ho_courser_2,
    # itm_ho_courser_3,
    # itm_ho_courser_4,
    # itm_ho_courser_5,
    
    # itm_s_heraldic_shield_leather,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_man_at_arms_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_bascinet_fi_noseguard,
    # itm_h_zitta_bascinet_novisor,
    # itm_h_bascinet_oniontop,
    # itm_h_bascinet_fi_mail,
    # itm_h_houndskull_fi,
    # itm_h_klappvisier_pigface_open,
    # itm_h_klappvisier_pigface,
    # itm_h_hounskull_narf,
    
    # itm_a_brigandine_narf_padded_plate_disc_plate_hose_custom,
    # itm_a_brigandine_narf_mail_plate_hose_custom,
    
    # itm_b_mail_boots,
    # itm_b_mail_chausses,
    
    # itm_g_mail_gauntlets,
    
    # itm_w_onehanded_sword_knight,
    # itm_w_onehanded_sword_squire,
    # itm_w_onehanded_sword_laird,
    # itm_w_onehanded_sword_poitiers,
    # itm_w_onehanded_horseman_axe_01,
    # itm_w_onehanded_horseman_axe_02,
    # itm_w_onehanded_horseman_axe_03,
    # itm_w_knight_warhammer_1,
    # itm_w_knight_winged_mace,
    # itm_w_knight_warhammer_2,
    # itm_w_lance_1_custom,
    # itm_w_lance_2_custom,
    # itm_w_lance_3_custom,
    # itm_w_lance_4_custom,
    # itm_w_lance_5_custom,
    # itm_w_lance_6_custom,
    
    # itm_ho_courser_1,
    # itm_ho_courser_2,
    # itm_ho_courser_3,
    # itm_ho_courser_4,
    # itm_ho_courser_5,
    # itm_ho_courser_6,
    # itm_ho_courser_7,
    # itm_ho_courser_8,
    
    # itm_s_heraldic_shield_leather,
    # itm_s_heraldic_shield_french_1,
    # itm_s_heraldic_shield_french_2,
    # itm_s_heraldic_shield_french_3,
    # itm_s_heraldic_shield_french_4,
    # itm_s_heraldic_shield_english_1,
    # itm_s_heraldic_shield_english_2,
    # itm_s_heraldic_shield_english_3,
    # itm_s_heraldic_shield_english_4,
    # itm_s_heraldic_shield_burgundian_1,
    # itm_s_heraldic_shield_burgundian_2,
    # itm_s_heraldic_shield_burgundian_3,
    # itm_s_heraldic_shield_burgundian_4,
    # itm_s_heraldic_shield_burgundian_7,
    # itm_s_heraldic_shield_breton_1,
    # itm_s_heraldic_shield_breton_2,
    # itm_s_heraldic_shield_breton_3,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    
  ["custom_merc_knight","Company Knight","Company Knights", tf_guarantee_all|tf_mounted|tf_guarantee_polearm,0,0,fac_player_faction,[],
    level(35)|str_28|agi_28,  
    wp_melee(250), 
    knows_ironflesh_8|knows_power_strike_8|knows_shield_4|knows_athletics_4|knows_weapon_master_8|knows_riding_5,
    mercenary_face_1, mercenary_face_2],
    
  ["custom_merc_knight_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
   # Inventory Matters here. This is what they will be carrying first if not yet customized / given a weapon.
   [ 
    # itm_h_bascinet_great,
    # itm_h_bascinet_great_fi,
    # itm_h_hounskull_narf,
    # itm_h_klappvisier_pigface,
    # itm_h_houndskull_fi,
    
    # itm_heraldic_plate,
    # itm_heraldic_jupon,
    
    # itm_g_plate_mittens,
    
    # itm_b_steel_greaves_full,
    # itm_b_shynbaulds,
    
    # itm_w_lance_6_heraldic,
    # itm_w_lance_6_custom,
    
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_c,
    # itm_w_onehanded_horseman_axe_02,
    # itm_w_onehanded_horseman_axe_03,
    # itm_w_twohanded_knight_battle_axe_01,
    # itm_w_knight_warhammer_2,
    # itm_w_knight_warhammer_1,
    # itm_w_knight_winged_mace,
    
    # itm_s_heraldic_shield_bouche,
    
    # itm_ho_war_horse_blue,
    # itm_ho_war_horse_black,
    # itm_ho_war_horse_brown,
    # itm_ho_war_horse_green,
    # itm_ho_war_horse_red,
    # itm_ho_war_horse_blue,
   ], def_attrib|level(1), wp(60),knows_common,0
  ],
  
  ["custom_merc_knight_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_player_faction,
    [ #Inventory Matters here. This is what they CAN BE ASKED to equip. Our system gives this troop weapons through dialogues.
    # itm_h_bascinet_great,
    # itm_h_bascinet_great_fi,
    # itm_h_hounskull_narf,
    # itm_h_klappvisier_pigface,
    # itm_h_houndskull_fi,
    
    # itm_heraldic_plate,
    # itm_heraldic_jupon,
    
    # itm_g_plate_mittens,
    
    # itm_b_steel_greaves_full,
    # itm_b_shynbaulds,
    
    # itm_w_lance_6_heraldic,
    # itm_w_lance_6_custom,
    # itm_w_lance_colored_french_1_custom,
    # itm_w_lance_colored_french_2_custom,
    # itm_w_lance_colored_french_3_custom,
    # itm_w_lance_colored_french_1_heraldic,
    # itm_w_lance_colored_french_2_heraldic,
    # itm_w_lance_colored_french_3_heraldic,
    # itm_w_lance_colored_english_1_custom,
    # itm_w_lance_colored_english_2_custom,
    # itm_w_lance_colored_english_3_custom,
    # itm_w_lance_colored_english_1_heraldic,
    # itm_w_lance_colored_english_2_heraldic,
    # itm_w_lance_colored_english_3_heraldic,
    
    # itm_w_bastard_sword_d,
    # itm_w_bastard_sword_c,
    # itm_w_bastard_sword_agincourt,
    # itm_w_bastard_sword_landgraf,
    # itm_w_bastard_sword_sempach,
    # itm_w_bastard_sword_crecy,
    # itm_w_onehanded_horseman_axe_02,
    # itm_w_onehanded_horseman_axe_03,
    # itm_w_twohanded_knight_battle_axe_01,
    # itm_w_knight_warhammer_2,
    # itm_w_knight_warhammer_1,
    # itm_w_knight_winged_mace,
    
    # itm_s_heraldic_shield_bouche,
    
    # itm_ho_war_horse_blue,
    # itm_ho_war_horse_black,
    # itm_ho_war_horse_brown,
    # itm_ho_war_horse_green,
    # itm_ho_war_horse_red,
    # itm_ho_war_horse_blue,
    ], def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,0], 
    

  ["custom_mercs_end","{!}na","{!}na",0,0,0,fac_player_faction,[itm_velvet],def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,swadian_face_middle_1, swadian_face_older_2],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CUSTOM TROOPS NPCS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ["merc_company_quartermaster","Quartermaster Godefroy de Papincourt","Quartermaster Godefroy de Papincourt",tf_hero|tf_unmoveable_in_party_window,scn_player_camp|entry(2),0,fac_commoners,
   [
   # itm_w_lance_colored_french_2_heraldic,itm_ho_horse_barded_blue_chamfrom,itm_h_klappvisier_pigface_open,itm_heraldic_churburg_13_tabard,itm_b_shynbaulds,itm_g_plate_mittens,itm_b_hosen_shoes_custom,itm_a_tabard_heraldic,itm_w_bastard_sword_count
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x000000063f0011425723719b326ec55c00000000001cb72a0000000000000000],
   
  ["merc_company_smith","Henri the Smith","Henri the Smith",tf_hero|tf_unmoveable_in_party_window,scn_player_camp|entry(3),0,fac_commoners,
   [
   # itm_h_arming_cap,itm_a_commoner_apron,itm_b_ankle_boots
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x00000003bf100144266b7339a169555100000000001db7090000000000000000],

  ["merc_company_merchant","Guy the Merchant","Guy the Merchant",tf_hero|tf_is_merchant|tf_unmoveable_in_party_window,scn_player_camp|entry(4),0,fac_commoners,
   [
   # itm_h_highlander_beret_red_2,itm_a_merchant_outfit,itm_b_leather_boots
   ],
   def_attrib|level(20),wp(120),knows_common|knows_inventory_management_10, 0x00000001840834485914d426156ab55400000000000d35240000000000000000],

  ["inventory_backup","{!}Inventory","{!}Inventory",tf_hero|tf_inactive,0,reserved,fac_player_faction,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],
  
  ["merc_company_name","Mercenary Company","Mercenary Company",tf_hero|tf_inactive,0,reserved,fac_player_faction,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],

## DAC Custom Troops (Merc System) End

]