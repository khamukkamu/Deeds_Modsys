﻿import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *
from dac_mercenary_company import mercenary_company_troops

from compiler import *
####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

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

woman_face_1    = 0x000000000010000536db6db6db6db6db003b6db6db6db6db0000000000000000
woman_face_2    = 0x000000003f10600436db6db6db6db6db003b6db6db6db6db0000000000000000

swadian_woman_face_1 = 0x000000000010000536db6db6db6db6db003b6db6db6db6db0000000000000000
swadian_woman_face_2 = 0x000000003f10600436db6db6db6db6db003b6db6db6db6db0000000000000000

khergit_woman_face_1 = 0x000000000010000536db6db6db6db6db003b6db6db6db6db0000000000000000
khergit_woman_face_2 = 0x000000003f10600436db6db6db6db6db003b6db6db6db6db0000000000000000

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


troops = [
["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,[],str_4|agi_4|int_4|cha_4,wp(15),0,0x00000001bf00114d57237198fb66c55c00000000001cb52a0000000000000000],
["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],0,0,0,0x00000001bf00114d57237198fb66c55c00000000001cb52a0000000000000000],
["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,[itm_a_tabard,itm_b_high_boots_1],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_tutorial_club,itm_a_leather_jerkin,itm_b_turnshoes_1],str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,[itm_tutorial_short_bow,itm_tutorial_arrows,itm_a_leather_jerkin,itm_b_high_boots_1],str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_tutorial_sword,itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_1],str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1,mercenary_face_2],
["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,[itm_b_turnshoes_1],str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1,mercenary_face_2],
["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1,mercenary_face_2],

["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_b_turnshoes_1],str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1,mercenary_face_2],

["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
["farmer", "Farmer", "Farmers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_h_straw_hat,itm_a_farmer_tunic,itm_b_turnshoes_2,itm_a_commoner_apron,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_tunic,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_b_green,itm_h_felt_hat_b_brown,itm_w_spiked_club,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_03,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fork_1,itm_w_fork_2,itm_w_scythe_1], def_attrib, wp(60), knows_common_kham, swadian_face_young_1, swadian_face_old_2 ],
["townsman", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_h_woolen_cap_black,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_green,itm_h_woolen_cap_red,itm_h_woolen_cap_white,itm_h_woolen_cap_yellow,itm_h_felt_hat_b_black,itm_h_felt_hat_b_blue,itm_h_felt_hat_b_brown,itm_h_felt_hat_b_green,itm_h_felt_hat_b_red,itm_h_felt_hat_b_white,itm_h_felt_hat_b_yellow,itm_h_felt_hat_black,itm_h_felt_hat_blue,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_red,itm_h_felt_hat_white,itm_h_felt_hat_yellow,itm_h_highlander_beret_black,itm_h_highlander_beret_blue,itm_h_highlander_beret_brown,itm_h_highlander_beret_green,itm_h_highlander_beret_red,itm_h_highlander_beret_white,itm_h_highlander_beret_yellow,itm_a_peasant_man_custom,itm_a_peasant_coat,itm_a_peasant_cote_custom,itm_a_peasant_cote_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_noble_shirt_black,itm_a_noble_shirt_blue,itm_a_noble_shirt_green,itm_a_noble_shirt_red,itm_a_noble_shirt_white,itm_a_noble_shirt_green,itm_b_turnshoes_1,itm_b_turnshoes_2], def_attrib, wp(75), knows_warrior_basic, swadian_face_young_1, swadian_face_old_2 ],
#Farmer Troop Tree continues after mercenaries.

#Mercenaries Begin
############################################################################################################## DAC New mercenaries
### Generic Mercenaries
["watchman", "Watchman", "Watchmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,itm_h_skullcap_hood_liripipe_custom,itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark], 
level(10)|str_12|agi_12, wpex(120,80,80,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],
["caravan_guard", "Caravan_Guard", "Caravan_Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, 
[itm_h_skullcap_hood_liripipe_custom,itm_h_german_kettlehat_1_liripipe_hood_custom,itm_h_german_kettlehat_3_liripipe_hood_custom,itm_h_chapel_de_fer_liripipe_hood_custom,itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,itm_a_light_gambeson_long_sleeves_alt_custom,itm_g_leather_gauntlet,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_squire,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,itm_w_onehanded_war_axe_03,itm_w_onehanded_war_axe_03_brown,itm_w_onehanded_war_axe_03_red,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_mace_spiked_red,itm_w_spear_8,itm_w_spear_9,itm_w_spear_3,itm_w_spear_4,itm_s_heater_shield_breton_2,itm_s_heater_shield_breton_4,itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_english_1,itm_s_heater_shield_english_2,itm_s_heater_shield_english_6,itm_s_heater_shield_french_1,itm_s_heater_shield_french_2,itm_s_heater_shield_french_3], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],
["mercenary_swordsman", "Mercenary Swordsman", "Mercenary Swordsmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, 
[itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,itm_a_pistoia_mail_a_mail_sleeves_jackchains,itm_a_pistoia_mail_b_mail_sleeves_jackchains,itm_b_low_boots_1,itm_b_low_boots_2,itm_b_low_boots_3,itm_b_low_boots_4,itm_g_leather_gauntlet,itm_g_gauntlets_mailed,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_squire,itm_s_heater_shield_breton_2,itm_s_heater_shield_breton_4,itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_english_1,itm_s_heater_shield_english_2,itm_s_heater_shield_english_6,itm_s_heater_shield_french_1,itm_s_heater_shield_french_2,itm_s_heater_shield_french_3], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, 0x000000000710701036d26cbb59a5e6db00000000001db6db0000000000000000, 0x000000000710801236d26cbb59a5e6db00000000001db6db0000000000000000 ],
["hired_blade", "Hired Blade", "Hired Blades", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_commoners, 
[itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_mail_aventail,itm_h_sallet_mail_collar_bevor,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_sallet_curved_mail_collar_bevor,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_4,itm_g_demi_gauntlets,itm_g_finger_gauntlets,itm_a_corrazina_hohenaschau_custom,itm_a_churburg_13_asher_plain_custom,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_forsaken,itm_w_onehanded_sword_martyr,itm_s_heraldic_shield_french_1,itm_s_heraldic_shield_french_2,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_french_4,itm_s_heraldic_shield_english_1,itm_s_heraldic_shield_english_2,itm_s_heraldic_shield_english_3,itm_s_heraldic_shield_english_4,itm_s_heraldic_shield_english_7,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3,itm_s_heraldic_shield_burgundian_4,itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,itm_s_heraldic_shield_breton_5], 
level(25)|str_20|agi_20, wpex(200,100,100,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, mercenary_face_1, mercenary_face_2 ],

["mercenary_spearman", "Mercenary Spearman", "Mercenary Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_commoners, 
[itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_a_padded_over_mail_heavy_1_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_4_custom,itm_b_low_boots_1,itm_b_low_boots_2,itm_b_low_boots_3,itm_b_low_boots_4,itm_g_leather_gauntlet,itm_g_gauntlets_mailed,itm_w_spear_3,itm_w_spear_4,itm_w_spear_8,itm_w_spear_9,itm_s_heraldic_shield_pavise], 
level(20)|str_16|str_16, wpex(80,80,160,80,80,80), knows_ironflesh_4|knows_power_strike_4|knows_shield_2|knows_athletics_3|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],
["mercenary_pavise_spearman", "Mercenary Pavise Spearman", "Mercenary Pavise Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_commoners, 
[itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_mail_aventail,itm_h_sallet_mail_collar_bevor,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_sallet_curved_mail_collar_bevor,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_4,itm_g_demi_gauntlets,itm_g_finger_gauntlets,itm_a_brigandine_asher_mail_custom,itm_a_brigandine_asher_plate_1_custom,itm_a_brigandine_asher_plate_2_custom,itm_a_brigandine_asher_plate_3_custom,itm_w_spear_10,itm_w_spear_11,itm_w_spear_5,itm_w_spear_6,itm_s_heraldic_shield_pavise_native], 
level(25)|str_20|str_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_3|knows_weapon_master_2, 0x000000000710701036d26cbb59a5e6db00000000001db6db0000000000000000, 0x000000000710801236d26cbb59a5e6db00000000001db6db0000000000000000 ],

["mercenary_bowman", "Mercenary Bowman", "Mercenary Bowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners, 
[itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,itm_h_straw_hat,itm_a_peasant_man_custom,itm_a_peasant_cote_custom,itm_b_low_boots_1,itm_b_low_boots_2,itm_b_low_boots_3,itm_b_low_boots_4,itm_b_low_boots_9,(itm_w_dagger_quillon, imodbit_rusty),(itm_w_dagger_rondel, imodbit_rusty),(itm_w_dagger_baselard, imodbit_rusty),itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_hunting_bow_ash,itm_w_hunting_bow_elm,itm_w_hunting_bow_oak,itm_w_arrow_triangular], 
level(10)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, mercenary_face_1, mercenary_face_2 ],
["mercenary_archer", "Mercenary Archer", "Mercenary Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners, 
[itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_chapel_de_fer_liripipe_hood_custom,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,itm_h_arming_cap,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_9,itm_g_leather_gauntlet,itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,itm_w_dagger_baselard,itm_w_dagger_quillon,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,itm_w_war_bow_ash,itm_w_war_bow_elm,itm_w_war_bow_yew,itm_w_arrow_triangular_large], 
level(15)|str_12|agi_14, wpex(100,80,80,120,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, mercenary_face_1, mercenary_face_2 ],
["mercenary_longbowman", "Mercenary Longbowman", "Mercenary Longbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners, 
[itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_sallet_mail_aventail,itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_4,itm_b_high_boots_9,itm_g_leather_gauntlet,itm_a_padded_jack_custom,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_a,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_long_bow_ash,itm_w_long_bow_elm,itm_w_arrow_bodkin], 
level(20)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, mercenary_face_1, mercenary_face_2 ],

["mercenary_scout", "Mercenary Scout", "Mercenary Scouts", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_commoners, 
[
 itm_h_makeshift_kettle_strap,itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_shingle_helmet_strap,itm_h_rope_helmet_strap,itm_h_wicker_helmet_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_padded_over_mail_1_custom,itm_a_padded_over_mail_2_custom,itm_a_padded_over_mail_alt_1_custom,itm_a_padded_over_mail_alt_2_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_6,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_g_leather_gauntlet,
 itm_w_light_lance,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_horseman_axe_01,itm_w_onehanded_horseman_axe_01_brown,itm_w_onehanded_horseman_axe_01_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,
 itm_s_heater_shield_french_1,itm_s_heater_shield_french_2,itm_s_heater_shield_french_3,itm_s_heater_shield_french_4,itm_s_heater_shield_english_1,itm_s_heater_shield_english_2,itm_s_heater_shield_english_3,itm_s_heater_shield_english_4,itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_burgundian_3,itm_s_heater_shield_breton_1,itm_s_heater_shield_breton_2,itm_s_heater_shield_breton_4,
 itm_ho_sumpter_1,itm_ho_sumpter_2,itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(15)|str_16|agi_16, wp_melee(120), knows_ironflesh_3|knows_power_strike_3|knows_shield_1|knows_athletics_3|knows_weapon_master_3|knows_riding_2, mercenary_face_1, mercenary_face_2 ],
["mercenary_light_cavalry", "Mercenary Light Cavalry", "Mercenary Light Cavalries", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_commoners, 
[
 itm_h_makeshift_kettle_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_chapel_de_fer_mail_aventail,
 itm_a_padded_over_mail_3_custom,itm_a_padded_over_mail_alt_3_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_6,itm_b_high_boots_7,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_g_demi_gauntlets,
 itm_w_light_lance,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_warhammer_1_red,itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_warhammer_2_red,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_02_red,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_03_brown,itm_w_onehanded_horseman_axe_03_red,itm_w_onehanded_sword_squire,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,
 itm_s_heraldic_shield_french_1,itm_s_heraldic_shield_french_2,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_french_4,itm_s_heraldic_shield_english_1,itm_s_heraldic_shield_english_2,itm_s_heraldic_shield_english_3,itm_s_heraldic_shield_english_4,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3,itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,
 itm_ho_courser_1,itm_ho_courser_2,itm_ho_courser_3,itm_ho_courser_4,itm_ho_courser_5,itm_ho_courser_6,itm_ho_courser_7,itm_ho_courser_8,
], 
level(20)|str_18|agi_18, wp_melee(150), knows_ironflesh_4|knows_power_strike_4|knows_shield_2|knows_athletics_4|knows_weapon_master_4|knows_riding_3, mercenary_face_1, mercenary_face_2 ],
["mercenary_cavalry", "Mercenary Cavalry", "Mercenary Cavalries", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_commoners, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_3_visor_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_bascinet_4_visor_4_mail_aventail,itm_h_bascinet_4_visor_4_open_mail_aventail,
 itm_a_padded_over_mail_4_custom,itm_a_padded_over_mail_5_custom,itm_a_padded_over_mail_alt_4_custom,itm_a_padded_over_mail_alt_5_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_finger_gauntlets,
 itm_w_lance_1,itm_w_lance_2,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_ebony,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_ebony,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_ebony,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_ebony,
 itm_s_heraldic_shield_french_1,itm_s_heraldic_shield_french_2,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_french_4,itm_s_heraldic_shield_english_1,itm_s_heraldic_shield_english_2,itm_s_heraldic_shield_english_3,itm_s_heraldic_shield_english_4,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3,itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,
 itm_ho_horse_barded_black,itm_ho_horse_barded_blue,itm_ho_horse_barded_brown,itm_ho_horse_barded_green,itm_ho_horse_barded_red,itm_ho_horse_barded_white,
], 
level(25)|str_20|agi_20, wp_melee(180), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, mercenary_face_1, mercenary_face_2 ],

### Flemish
["flemish_peasant_crossbowman", "Flemish Camp Guard", "Flemish Camp Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_cervelliere_strap,itm_h_cervelliere_roundel_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_rope_helmet_strap,itm_h_wicker_helmet_strap,itm_h_arming_cap,itm_h_simple_coif,
 itm_a_peasant_cotehardie_custom,itm_a_tailored_cotehardie_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,
 itm_w_crossbow_hunting,itm_w_bolt_triangular,
 itm_w_dagger_quillon,itm_w_dagger_bollock,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
], 
level(12)|str_13|agi_12, wpex(80,80,80,80,100,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],
["flemish_militia_crossbowman", "Flemish Poor Crossbowman", "Flemish Poor Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_chapel_de_fer_liripipe_hood_custom,itm_h_german_kettlehat_1_liripipe_hood_custom,itm_h_german_kettlehat_2_liripipe_hood_custom,itm_h_german_kettlehat_3_liripipe_hood_custom,itm_h_german_kettlehat_4_liripipe_hood_custom,itm_h_german_kettlehat_5_liripipe_hood_custom,itm_h_german_kettlehat_6_liripipe_hood_custom,itm_h_german_kettlehat_7_liripipe_hood_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_2_strap,itm_h_german_kettlehat_3_strap,itm_h_german_kettlehat_4_strap,itm_h_german_kettlehat_5_strap,itm_h_german_kettlehat_6_strap,itm_h_german_kettlehat_7_strap,itm_h_cervelliere_strap,itm_h_cervelliere_roundel_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_shingle_helmet_strap,itm_h_rope_helmet_strap,itm_h_wicker_helmet_strap,
 itm_a_aketon_asher_dagged_thick_black_1,itm_a_aketon_asher_dagged_thick_black_2,itm_a_aketon_asher_dagged_thick_beige_1,itm_a_aketon_asher_dagged_thick_beige_2,itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_beige_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,
 itm_g_leather_gauntlet,
 itm_w_crossbow_light,itm_w_bolt_triangular,
 itm_w_goedendag,itm_w_dagger_quillon,itm_w_dagger_bollock,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,
], 
level(15)|str_15|agi_13, wpex(100,80,80,80,120,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_athletics_3|knows_weapon_master_2, swadian_face_young_1, swadian_face_old_2 ],
["flemish_crossbowman", "Flemish Crossbowman", "Flemish Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,
 itm_a_gambeson_asher_regular_custom,itm_a_gambeson_asher_belt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,
 itm_g_leather_gauntlet,
 itm_w_crossbow_medium,itm_w_bolt_triangular_large,
 itm_w_goedendag_burgundy,itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_messer,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_war_axe_04,itm_w_onehanded_war_axe_04_brown,itm_w_onehanded_war_axe_04_red,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_mace_spiked_red,
], 
level(20)|str_17|agi_15, wpex(120,80,80,80,140,80), knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_weapon_master_3|knows_athletics_3, swadian_face_young_1, swadian_face_old_2 ],
["flemish_heavy_crossbowman", "Flemish Rich Crossbowman", "Flemish Rich Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,
 itm_a_corrazina_hohenaschau_mail_custom,itm_a_churburg_13_asher_plain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,
 itm_g_demi_gauntlets,
 itm_w_goedendag_burgundy,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_messer,itm_w_onehanded_war_axe_04,itm_w_onehanded_war_axe_04_brown,itm_w_onehanded_war_axe_04_red,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_warhammer_1_red,
 itm_w_crossbow_heavy,itm_w_bolt_triangular_large,
], 
level(22)|str_18|agi_16, wpex(140,80,80,80,160,80), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_4, swadian_face_young_1, swadian_face_old_2 ],

["flemish_militia_pikeman", "Flemish Infantry", "Flemish Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_chapel_de_fer_liripipe_hood_custom,itm_h_german_kettlehat_1_liripipe_hood_custom,itm_h_german_kettlehat_2_liripipe_hood_custom,itm_h_german_kettlehat_3_liripipe_hood_custom,itm_h_german_kettlehat_4_liripipe_hood_custom,itm_h_german_kettlehat_5_liripipe_hood_custom,itm_h_german_kettlehat_6_liripipe_hood_custom,itm_h_german_kettlehat_7_liripipe_hood_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_2_strap,itm_h_german_kettlehat_3_strap,itm_h_german_kettlehat_4_strap,itm_h_german_kettlehat_5_strap,itm_h_german_kettlehat_6_strap,itm_h_german_kettlehat_7_strap,itm_h_cervelliere_strap,itm_h_cervelliere_roundel_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_shingle_helmet_strap,itm_h_rope_helmet_strap,itm_h_wicker_helmet_strap,
 itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,
 itm_g_leather_gauntlet,
 itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_awlpike_5,itm_w_awlpike_6,
]
, level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
["flemish_pikeman", "Flemish Pikeman", "Flemish Pikemen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,
 itm_a_brigandine_asher_a_custom,itm_a_brigandine_asher_b_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,
 itm_g_demi_gauntlets,
 itm_w_pike_1,itm_w_dagger_baselard,itm_w_dagger_pikeman,itm_w_dagger_quillon,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,
]
, level(15)|str_16|agi_12, wpex(120,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2|knows_shield_2, swadian_face_young_1, swadian_face_old_2 ],
["flemish_heavy_pikeman", "Flemish Heavy Pikeman", "Flemish Heavy Pikemen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_pike_swiss_1,itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_messer,itm_w_dagger_baselard,itm_w_dagger_rondel,itm_w_onehanded_falchion_a,
]
, level(20)|str_18|agi_15, wpex(140,100,180,100,100,100), knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3|knows_shield_3, swadian_face_young_1, swadian_face_old_2 ],

["flemish_halberdier", "Flemish Halberdier", "Flemish Halberdiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,
 itm_a_pistoia_mail_a_mail_sleeves_plate_1,itm_a_pistoia_mail_b_mail_sleeves_plate_1,itm_a_pistoia_mail_a_mail_sleeves_plate_2,itm_a_pistoia_mail_b_mail_sleeves_plate_2,itm_a_pistoia_mail_a_mail_sleeves_plate_3,itm_a_pistoia_mail_b_mail_sleeves_plate_3,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,
 itm_g_demi_gauntlets,
 itm_w_halberd_1,itm_w_halberd_1_alt,itm_w_halberd_1_brown_alt,itm_w_halberd_1_brown,itm_w_halberd_2,itm_w_halberd_2_alt,itm_w_halberd_2_brown_alt,itm_w_halberd_2_brown,itm_w_halberd_3,itm_w_halberd_3_brown,itm_w_halberd_3_alt,itm_w_halberd_3_brown_alt,
], 
level(15)|str_15|agi_13, wpex(100,100,160,100,100,100), knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_2, swadian_face_young_1, swadian_face_old_2 ],
["flemish_heavy_halberdier", "Flemish Heavy Halberdier", "Flemish Heavy Halberdiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,
 itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_mail_sleeves_jackchain,itm_a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_3,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_2,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_3,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_halberd_4,itm_w_halberd_4_brown,itm_w_halberd_4_alt,itm_w_halberd_4_brown_alt,itm_w_halberd_5,itm_w_halberd_5_alt,itm_w_halberd_5_brown_alt,itm_w_halberd_5_brown,itm_w_halberd_6,itm_w_halberd_6_brown,itm_w_halberd_6_alt,itm_w_halberd_6_brown_alt,
], 
level(20)|str_17|agi_16, wpex(100,100,190,100,100,100), knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_weapon_master_3, swadian_face_young_1, swadian_face_old_2 ],

["mercenary_german_knight", "German Knight", "German Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_pigface_klappvisor,itm_h_pigface_klappvisor_open,itm_h_zitta_bascinet,itm_h_zitta_bascinet_open,itm_h_wespe_bascinet_a,itm_h_wespe_bascinet_b,itm_h_wespe_bascinet_c,itm_h_wespe_bascinet_a_open,itm_h_wespe_bascinet_b_open,itm_h_wespe_bascinet_c_open,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,
 itm_g_gauntlets_segmented_a,
 itm_a_plate_german_covered_fauld_custom,itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,
 itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_1,itm_b_leg_harness_2,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_onehanded_sword_messer,itm_w_onehanded_sword_flemish,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_forsaken,itm_w_onehanded_sword_martyr,itm_w_onehanded_knight_axe_german_01,itm_w_onehanded_knight_axe_german_01_brown,itm_w_onehanded_knight_axe_german_01_ebony,itm_w_onehanded_knight_axe_german_02,itm_w_onehanded_knight_axe_german_02_brown,itm_w_onehanded_knight_axe_german_02_ebony,itm_w_mace_german,itm_w_mace_german_brown,itm_w_mace_german_ebony,itm_w_lance_6,itm_w_lance_5,
 itm_s_heraldic_shield_german_1,itm_s_heraldic_shield_german_2,itm_s_heraldic_shield_german_3,itm_s_heraldic_shield_german_4,itm_s_heraldic_shield_german_6,itm_s_heraldic_shield_german_7,
 itm_ho_horse_barded_black_chamfrom,itm_ho_horse_barded_brown_chamfrom,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_6, swadian_face_middle_1, swadian_face_older_2 ],
["mercenary_german_dismounted_knight", "German Dismounted Knight", "German Dismounted Knights", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_flemish_mercenaries, 
[
 itm_h_pigface_klappvisor,itm_h_pigface_klappvisor_open,itm_h_zitta_bascinet,itm_h_zitta_bascinet_open,itm_h_wespe_bascinet_a,itm_h_wespe_bascinet_b,itm_h_wespe_bascinet_c,itm_h_wespe_bascinet_a_open,itm_h_wespe_bascinet_b_open,itm_h_wespe_bascinet_c_open,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,
 itm_g_gauntlets_segmented_a,
 itm_a_plate_german_covered_fauld_custom,itm_a_corrazina_hohenaschau_custom,
 itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_1,itm_b_leg_harness_2,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_bastard_sword_german,itm_w_kriegshammer_ebony,itm_w_kriegshammer_alt_ebony,itm_w_pollaxe_blunt_08_brown,itm_w_pollaxe_blunt_12_brown,itm_w_pollaxe_cut_03_brown
],
 level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_7|knows_power_strike_7|knows_shield_4|knows_athletics_4|knows_weapon_master_6, swadian_face_middle_1, swadian_face_older_2 ],

############################################################################################################### DAC New Mercenaries End

["italian_light_infantry", "Italian Light Infantry", "Italian Light Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_neutral, 
[
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_hood_big_liripipe_full_custom,itm_h_chapel_de_fer_hood_custom,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,itm_h_arming_cap,itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_curved_mail_collar,itm_h_transitional_sallet_1_mail_collar,itm_h_transitional_sallet_2_mail_collar,itm_h_transitional_sallet_3_mail_collar,itm_h_barbuta_nooxy_1_mail_collar,itm_h_barbuta_nooxy_2_mail_collar,
 itm_a_peasant_cotehardie_custom,itm_a_tailored_cotehardie_custom,itm_a_gambeson_asher_belt_custom,itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_9,
 itm_w_dagger_italian,itm_w_onehanded_falchion_italian,itm_w_onehanded_sword_italian,itm_w_onehanded_sword_milanese,itm_w_onehanded_falchion_peasant,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_genoese_1,itm_s_tall_pavise_genoese_2,
], 
level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["italian_infantry", "Italian Infantry", "Italian Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, 
[
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_sallet_mail_aventail,itm_h_transitional_sallet_1_mail_aventail,itm_h_transitional_sallet_2_mail_aventail,itm_h_transitional_sallet_3_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_barbuta_1_mail_collar,itm_h_barbuta_1_nasal_mail_collar,itm_h_barbuta_2_mail_collar,itm_h_barbuta_2_nasal_mail_collar,itm_h_wespe_bascinet_c,itm_h_wespe_bascinet_c_open,itm_h_barbuta_nooxy_1_mail_collar,itm_h_barbuta_nooxy_2_mail_collar,itm_h_barbuta_nooxy_3,
 itm_a_brigandine_asher_custom,itm_a_brigandine_asher_custom,itm_a_pistoia_breastplate_half_mail_sleeves,itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,itm_a_pistoia_mail_a_mail_sleeves_jackchains,itm_a_pistoia_mail_b_mail_sleeves_jackchains,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_9,
 itm_w_onehanded_falchion_italian,itm_w_onehanded_sword_italian,itm_w_onehanded_sword_milanese,itm_w_onehanded_falchion_peasant,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_genoese_1,itm_s_tall_pavise_genoese_2,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["italian_heavy_infantry", "Italian Heavy Infantry", "Italian Heavy Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, 
[
 itm_h_chapel_de_fer_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_sallet_mail_aventail,itm_h_transitional_sallet_1_mail_aventail,itm_h_transitional_sallet_2_mail_aventail,itm_h_transitional_sallet_3_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_barbuta_1_mail_collar,itm_h_barbuta_1_nasal_mail_collar,itm_h_barbuta_2_mail_collar,itm_h_barbuta_2_nasal_mail_collar,itm_h_wespe_bascinet_c,itm_h_wespe_bascinet_c_open,itm_h_barbuta_nooxy_1_mail_collar,itm_h_barbuta_nooxy_2_mail_collar,itm_h_barbuta_nooxy_3,
 itm_a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,itm_a_brigandine_asher_mail_custom,itm_a_brigandine_asher_plate_1_custom,itm_a_corrazina_spina_custom,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_onehanded_falchion_italian,itm_w_onehanded_sword_italian,itm_w_onehanded_sword_milanese,itm_w_onehanded_falchion_peasant,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_genoese_1,itm_s_tall_pavise_genoese_2, 
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],


["genoese_crossbowman", "Genoese Crossbowman", "Genoese Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_neutral, 
[
 itm_h_barbuta_nooxy_1_mail_collar,itm_h_barbuta_nooxy_2_mail_collar,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,
 itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_beige_2,itm_a_aketon_asher_dagged_red_1,itm_a_aketon_asher_dagged_red_2,itm_a_aketon_asher_green_1,itm_a_aketon_asher_green_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_9,
 itm_w_dagger_italian,itm_w_dagger_quillon,itm_w_onehanded_falchion_italian,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_italian,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_crossbow_light,itm_w_bolt_triangular,
 itm_s_tall_pavise_genoese_1,itm_s_tall_pavise_genoese_2,
], 
level(22)|str_18|agi_16, wpex(140,80,80,80,180,80), knows_ironflesh_5|knows_power_strike_3|knows_shield_3|knows_athletics_3|knows_weapon_master_3, 0x000000000710a05236d26cbb59a5e6db00000000001db6db0000000000000000, 0x000000003e10b0d236d26cbb59a5e6db00000000001db6db0000000000000000 ],

["genoese_heavy_crossbowman", "Genoese Heavy Crossbowman", "Genoese Heavy Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_neutral, 
[
 itm_h_bascinet_2_mail_aventail,itm_h_barbuta_1_mail_collar,itm_h_barbuta_2_mail_collar,itm_h_sallet_mail_collar,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,
 itm_a_pistoia_breastplate_half_mail_sleeves,itm_a_pistoia_breastplate_mail_sleeves,itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,itm_a_pistoia_breastplate_mail_sleeves_jackchain,itm_a_corrazina_capwell_custom,itm_a_brigandine_asher_mail_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,itm_g_finger_gauntlets,
 itm_w_onehanded_falchion_italian,itm_w_onehanded_sword_italian,itm_w_onehanded_sword_milanese,
 itm_w_crossbow_heavy,itm_w_bolt_bodkin,
 itm_s_tall_pavise_genoese_1,itm_s_tall_pavise_genoese_2,], 
level(22)|str_18|agi_16, wpex(140,80,80,80,180,80), knows_ironflesh_5|knows_power_strike_3|knows_shield_3|knows_athletics_3|knows_weapon_master_3, 0x000000000710a05236d26cbb59a5e6db00000000001db6db0000000000000000, 0x000000003e10b0d236d26cbb59a5e6db00000000001db6db0000000000000000 ],

["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,[],def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
#Mercenaries END


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC FRENCH TROOPS ########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

##### Village Troops

### Ranged Line
["french_peasant_archer", "French Peasant Archer", "French Peasant Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, [
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif,itm_h_straw_hat,itm_h_woolen_cap_blue,itm_h_woolen_cap_white,itm_h_woolen_cap_brown,
 itm_a_peasant_cotehardie_custom,itm_a_peasant_cote_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_1,
 itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_short_bow_elm,itm_w_short_bow_oak,itm_w_arrow_triangular,itm_w_arrow_triangular,itm_w_arrow_triangular,
], 
level(8)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["french_poor_archer", "French Poor Archer", "French Poor Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, [
 itm_h_bycocket_1_custom,itm_h_bycocket_2_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_skullcap_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,
 itm_a_tailored_cotehardie_custom,itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,itm_g_leather_gauntlet,
 itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_dagger_quillon,itm_w_dagger_bollock,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_hunting_bow_ash,itm_w_hunting_bow_elm,itm_w_hunting_bow_yew,itm_w_arrow_triangular,itm_w_arrow_triangular,
], 
level(12)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["french_archer", "French Archer", "French Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, [
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,itm_g_leather_gauntlet,
 itm_w_dagger_baselard,itm_w_dagger_rondel,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,
 itm_w_war_bow_ash,itm_w_war_bow_elm,itm_w_arrow_triangular_large,itm_w_arrow_triangular_large,
], 
level(15)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],


### Infantry Line
["french_peasant_levy", "French Peasant Levy", "French Peasants Levies", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_1, [
itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_straw_hat_1,itm_h_simple_coif,itm_h_straw_hat,itm_h_arming_cap,
itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,
itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_fork_1,itm_w_fork_2,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
],
level(6)|str_10|agi_10,wpex(80,80,80,80,80,80),knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_athletics_2,french_face_young_1,french_face_middle_2],
["french_poor_spearman", "French Poor Spearman", "French Poor Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,
 itm_s_heater_shield_french_1,itm_s_heater_shield_french_2,itm_s_heater_shield_french_3,itm_s_heater_shield_french_4,itm_s_heater_shield_french_5,itm_s_heater_shield_french_6,itm_s_heater_shield_french_7,itm_s_heater_shield_french_8,
], 
level(10)|str_12|agi_12, wpex(120,80,80,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["french_spearman", "French Spearman", "French Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_mail_aventail,
 itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,itm_a_light_gambeson_long_sleeves_alt_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,
 itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_defiant,itm_w_onehanded_falchion_peasant,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_mace_spiked_red,
 itm_s_heater_shield_french_1,itm_s_heater_shield_french_2,itm_s_heater_shield_french_3,itm_s_heater_shield_french_4,itm_s_heater_shield_french_5,itm_s_heater_shield_french_6,itm_s_heater_shield_french_7,itm_s_heater_shield_french_8,
], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],
["french_vougier", "French Vougier", "French Vougier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_mail_aventail,
 itm_a_light_gambeson_long_sleeves_3_custom,itm_a_light_gambeson_long_sleeves_6_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,
 itm_w_glaive_1,itm_w_glaive_1_brown,itm_w_glaive_1_red,itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,
], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],


##### City Troops
### Ranged Line
["french_militia_crossbowman", "French Militia Crossbowman", "French Militia Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,itm_h_straw_hat,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_white,itm_h_skullcap_hood_liripipe_custom,itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,
 itm_a_aketon_asher_blue_1,itm_a_aketon_asher_blue_2,itm_a_aketon_asher_vandyked_blue_1,itm_a_aketon_asher_vandyked_blue_2,itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_beige_2,itm_a_aketon_asher_dagged_white_1,itm_a_aketon_asher_dagged_white_2,itm_a_aketon_asher_dagged_thick_beige_1,itm_a_aketon_asher_dagged_thick_beige_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,
 itm_w_crossbow_light,itm_w_bolt_triangular,
 itm_w_goedendag,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_dagger_baselard,itm_w_dagger_quillon,
], 
level(12)|str_13|agi_12, wpex(100,80,80,80,110,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["french_crossbowman", "French Crossbowman", "French Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,itm_h_shingle_helmet_strap,
 itm_a_gambeson_crossbowman_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_goedendag, 
 itm_w_crossbow_medium,itm_w_bolt_triangular_large,
], 
level(16)|str_15|agi_13, wpex(120,80,80,80,130,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["french_rich_crossbowman", "French Rich Crossbowman", "French Rich Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_gambeson_crossbowman_heavy_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_goedendag,
 itm_w_crossbow_heavy,itm_w_bolt_bodkin,
], 
level(22)|str_17|agi_15, wpex(140,80,80,80,150,80), knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_athletics_3|knows_weapon_master_3, french_face_middle_1, french_face_old_2 ],

### Infantry Line
["french_militia", "French Militia", "French Militia", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,
 itm_a_simple_gambeson_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,
 itm_s_heraldic_shield_french_1,itm_s_heraldic_shield_french_2,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_french_4,itm_s_heraldic_shield_french_5,itm_s_heraldic_shield_french_6,itm_s_heraldic_shield_french_7,
], 
level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["french_poor_pavoisier", "French Poor Pavoisier", "French Poor Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,itm_a_pistoia_mail_a_mail_sleeves_jackchains,itm_a_pistoia_mail_b_mail_sleeves_jackchains,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_leather_gauntlet,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_french_1,itm_s_tall_pavise_french_2,itm_s_tall_pavise_french_3,itm_s_tall_pavise_french_4,itm_s_tall_pavise_french_5,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["french_pavoisier", "French Pavoisier", "French Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_padded_over_mail_heavy_1_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_4_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_french_1,itm_s_tall_pavise_french_2,itm_s_tall_pavise_french_3,itm_s_tall_pavise_french_4,itm_s_tall_pavise_french_5,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["french_rich_pavoisier", "French Rich Pavoisier", "French Rich Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_french_1,itm_s_tall_pavise_french_2,itm_s_tall_pavise_french_3,itm_s_tall_pavise_french_4,itm_s_tall_pavise_french_5,
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],

["french_poor_guisarmier", "French Poor Guisarmier", "French Poor Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_brigandine_asher_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["french_guisarmier", "French Guisarmier", "French Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_brigandine_asher_a_mail_custom,itm_a_brigandine_asher_a_mail_jackchain_custom,itm_a_brigandine_asher_b_mail_custom,itm_a_brigandine_asher_b_mail_jackchain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["french_rich_guisarmier", "French Rich Guisarmier", "French Rich Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,
 itm_w_glaive_4,itm_w_glaive_4_brown,itm_w_glaive_4_ebony,itm_w_glaive_6,itm_w_glaive_6_brown,itm_w_glaive_6_red,
], 
level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_warrior_basic2|knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, french_face_middle_1, french_face_mature_2 ],
["french_sergeant", "French Sergeant", "French Sergeants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_3,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,
 itm_w_glaive_4,itm_w_glaive_4_brown,itm_w_glaive_4_ebony,itm_w_glaive_6,itm_w_glaive_6_brown,itm_w_glaive_6_red,
], 
level(25)|str_20|agi_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, french_face_mature_1, french_face_old_2 ],

##### Castle Troops
### Noble Line
["french_spearman_at_atms", "French Homme d'Armes à Pied", "French Hommes d'Armes à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,itm_a_corrazina_spina_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], 
level(25)|str_20|agi_20, wp_melee(160), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, french_face_young_1, french_face_mature_2 ],
["french_dismounted_squire", "French Écuyer à Pied", "French Écuyers à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], 
level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, french_face_young_1, french_face_mature_2 ],
["french_chevalier_a_pied", "French Chevalier à Pied", "French Chevaliers à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_great_bascinet_continental,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,itm_h_great_bascinet_continental_visor_c_gilded,itm_h_great_bascinet_continental_visor_c_gilded_open,itm_h_great_bascinet_continental_visor_c_strip,itm_h_great_bascinet_continental_visor_c_strip_open,itm_h_great_bascinet_continental_1430,itm_h_great_bascinet_continental_1430_visor,itm_h_great_bascinet_continental_1430_visor_open,
 itm_a_padded_over_plate_sleeved_1_custom,itm_a_padded_over_plate_sleeved_2_custom,itm_a_padded_over_plate_shortsleeved_1_custom,itm_a_padded_over_plate_shortsleeved_2_custom,itm_a_padded_over_plate_shortsleeved_3_custom,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_w_bardiche_7,itm_w_bardiche_7_brown,itm_w_bardiche_7_red,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_twohanded_knight_battle_axe_03,itm_w_twohanded_knight_battle_axe_03_brown,itm_w_twohanded_knight_battle_axe_03_ebony,itm_w_pollaxe_blunt_05_ash,itm_w_pollaxe_blunt_alt_05_ash,itm_w_pollaxe_blunt_05_brown,itm_w_pollaxe_blunt_alt_05_brown,itm_w_pollaxe_blunt_05_ebony,itm_w_pollaxe_blunt_alt_05_ebony,itm_w_pollaxe_blunt_08_ash,itm_w_pollaxe_blunt_alt_08_ash,itm_w_pollaxe_blunt_08_brown,itm_w_pollaxe_blunt_alt_08_brown,itm_w_pollaxe_cut_03_ash,itm_w_pollaxe_cut_alt_03_ash,itm_w_pollaxe_cut_03_brown,itm_w_pollaxe_cut_alt_03_brown,itm_w_pollaxe_cut_03_red_trim,itm_w_pollaxe_cut_alt_03_red_trim,
 itm_w_bastard_falchion,itm_w_bastard_sword_crecy,itm_w_bastard_sword_agincourt,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,
], level(30)|str_24|agi_24, 
wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6, french_face_middle_1, french_face_mature_2 ],

["french_man_at_arms", "French Homme d'Armes", "French Hommes d'Armes", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,itm_a_corrazina_spina_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_s_heater_shield_french_1,itm_s_heater_shield_french_2,itm_s_heater_shield_french_3,itm_s_heater_shield_french_4,itm_s_heater_shield_french_5,itm_s_heater_shield_french_6,itm_s_heater_shield_french_7,itm_s_heater_shield_french_8,itm_s_heraldic_shield_heater,
 itm_w_native_spear_b,itm_w_native_spear_b_custom,
 itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_squire,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,
 itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(25)|str_20|agi_20, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, french_face_young_1, french_face_middle_2 ],
["french_squire", "French Écuyer", "French Écuyers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_s_heraldic_shield_french_1,itm_s_heraldic_shield_french_2,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_french_4,itm_s_heraldic_shield_french_5,itm_s_heraldic_shield_french_6,itm_s_heraldic_shield_french_7,itm_s_heraldic_shield_leather,
 itm_w_native_spear_f,itm_w_native_spear_f_custom,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_poitiers,itm_w_onehanded_horseman_axe_01,itm_w_onehanded_horseman_axe_01_alt,itm_w_onehanded_horseman_axe_01_brown,itm_w_onehanded_horseman_axe_01_alt_brown,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_02_alt,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_02_alt_brown,itm_w_warhammer_1,itm_w_warhammer_1_alt,itm_w_warhammer_1_brown,itm_w_warhammer_1_alt_brown,itm_w_warhammer_2,itm_w_warhammer_2_alt,itm_w_warhammer_2_brown,itm_w_warhammer_2_alt_brown,
 itm_ho_courser_1,itm_ho_courser_2,itm_ho_courser_3,itm_ho_courser_4,itm_ho_courser_5,itm_ho_courser_6,itm_ho_courser_7,itm_ho_courser_8,
], 
level(28)|str_22|agi_22, wp_melee(200), knows_ironflesh_7|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],
["french_chevalier", "French Chevalier", "French Chevaliers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_great_bascinet_continental,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,itm_h_great_bascinet_continental_visor_c_gilded,itm_h_great_bascinet_continental_visor_c_gilded_open,itm_h_great_bascinet_continental_visor_c_strip,itm_h_great_bascinet_continental_visor_c_strip_open,itm_h_great_bascinet_continental_1430,itm_h_great_bascinet_continental_1430_visor,itm_h_great_bascinet_continental_1430_visor_open,
 itm_a_padded_over_plate_sleeved_1_custom,itm_a_padded_over_plate_sleeved_2_custom,itm_a_padded_over_plate_shortsleeved_1_custom,itm_a_padded_over_plate_shortsleeved_2_custom,itm_a_padded_over_plate_shortsleeved_3_custom,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_w_lance_colored_french_1_custom,itm_w_lance_colored_french_2_custom,itm_w_lance_colored_french_3_custom,
 itm_s_hand_pavise_french_1,itm_s_hand_pavise_french_2,itm_s_hand_pavise_french_3,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_alt_brown,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_alt_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
 itm_ho_horse_barded_blue,itm_ho_horse_barded_brown,itm_ho_horse_barded_green,itm_ho_horse_barded_white,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],

# Special Troops
["french_bannerman", "French Porteur d'Étandard à Pied", "French Porteurs d'Étandard à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_english_plate_1415_heraldic,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_heraldic_banner,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_alt_brown,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_alt_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
], 
level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6, french_face_middle_1, french_face_mature_2 ],
["french_bannerman_mounted", "French Porteur d'Étandard", "French Porteurs d'Étandard", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_english_plate_1415_heraldic,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_heraldic_banner,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_alt_brown,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_alt_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],

## END French Main Troops
["french_messenger", "French Messenger", "French Messengers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, 
[], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5, french_face_young_1, french_face_middle_2 ],
["french_deserter", "French Deserter", "French Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, 
[], def_attrib|level(14), wp(80), knows_common|knows_riding_2|knows_ironflesh_1, french_face_young_1, french_face_middle_2 ],
["french_prison_guard", "Prison Guard", "Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], def_attrib|level(25), wp(130), knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3, french_face_mature_1, french_face_old_2 ],
["french_castle_guard", "Castle Guard", "Castle Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], def_attrib|level(25), wp(130), knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3, french_face_mature_1, french_face_old_2 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC ENGLISH TROOPS ########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################


##### Village Troops

### Ranged Line
["english_communal_bowman", "English Communal Bowman", "English Communal Bowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_arming_cap,itm_h_straw_hat,itm_h_simple_coif,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_hunting_bow_ash,itm_w_hunting_bow_oak,itm_w_arrow_triangular,
], 
level(8)|str_10|agi_12, wpex(90,80,80,110,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, english_face_young_1, english_face_middle_2 ],
["english_communal_archer", "English Communal Archer", "English Communal Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_cervelliere_hood_custom,itm_h_simple_cervelliere_hood_custom,itm_h_skullcap_hood_custom,itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_rope_helmet_strap,
 itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_white_1,itm_a_aketon_asher_dagged_white_2,itm_a_aketon_asher_dagged_red_1,itm_a_aketon_asher_dagged_red_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,
 itm_w_arrow_triangular_large,itm_w_hunting_bow_elm,itm_w_hunting_bow_yew,
], 
level(12)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_young_1, english_face_middle_2 ],
["english_communal_veteran_archer", "English Communal Veteran Archer", "English Communal Veteran Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_skullcap_mail_aventail,
 itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_dagger_bollock,itm_w_dagger_baselard,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,
 itm_w_war_bow_oak,itm_w_war_bow_elm,itm_w_arrow_triangular_large,
], 
level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],

["english_garrison_crossbowman", "English Garrison Crossbowman", "English Garrison Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_skullcap_mail_aventail,
 itm_a_simple_gambeson_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_goedendag,itm_w_dagger_bollock,itm_w_dagger_baselard,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,
 itm_w_crossbow_medium,itm_w_bolt_triangular,

], 
level(12)|str_13|agi_12, wpex(100,80,80,80,130,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, english_face_young_1, english_face_middle_2 ],

### Infantry Line
["english_communal_levy", "English Communal Levy", "English Communal Levies", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_straw_hat,itm_h_straw_hat_1,itm_h_simple_coif,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_dagger_quillon,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_spiked_club,itm_w_spiked_club_dark,itm_w_fork_1,itm_w_fork_2,
], 
level(6)|str_10|agi_10, wpex(80,80,80,80,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_athletics_2, english_face_young_1, english_face_middle_2 ],
["english_communal_levy_footman", "English Communal Poor Footman", "English Communal Poor Footmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_cervelliere_hood_custom,itm_h_simple_cervelliere_hood_custom,itm_h_skullcap_hood_custom,itm_h_wicker_helmet_strap,itm_h_rope_helmet_strap,itm_h_shingle_helmet_strap,itm_h_skullcap_strap,itm_h_simple_cervelliere_2_strap,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_makeshift_kettle_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,
 itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_onehanded_sword_a,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_spear_3,itm_w_spear_8,
 itm_s_heater_shield_english_1,itm_s_heater_shield_english_2,itm_s_heater_shield_english_3,itm_s_heater_shield_english_4,itm_s_heater_shield_english_5,itm_s_heater_shield_english_6,itm_s_heater_shield_english_7,itm_s_heater_shield_english_8,
], 
level(10)|str_12|agi_12, wpex(100,80,120,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, english_face_young_1, english_face_middle_2 ],
["english_communal_footman", "English Communal Footman", "English Communal Footmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_makeshift_kettle_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_spear_4,itm_w_spear_5,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_onehanded_war_axe_03,itm_w_onehanded_war_axe_03_brown,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_laird,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_d,itm_w_onehanded_sword_c,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,
 itm_s_heraldic_shield_english_1,itm_s_heraldic_shield_english_2,itm_s_heraldic_shield_english_3,itm_s_heraldic_shield_english_4,itm_s_heraldic_shield_english_5,itm_s_heraldic_shield_english_6,itm_s_heraldic_shield_english_7,
], 
level(15)|str_14|agi_14, wpex(120,80,140,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, english_face_middle_1, english_face_mature_2 ],
["english_communal_vougier", "English Communal Vougier", "English Communal Vougiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_makeshift_kettle_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_simple_gambeson_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_awlpike_1,itm_w_awlpike_2,itm_w_fauchard_2,itm_w_fauchard_3,
], 
level(20)|str_16|agi_16, wpex(140,100,160,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],

##### Town Troops

### Infantry Line
["english_militia", "English Militia", "English Militia", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_wicker_helmet_strap,itm_h_rope_helmet_strap,itm_h_skullcap_strap,itm_h_simple_cervelliere_2_strap,itm_h_simple_cervelliere_strap,itm_h_makeshift_kettle_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,
 itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_3_custom,itm_a_light_gambeson_long_sleeves_6_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_fauchard_2,itm_w_fauchard_3,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, english_face_young_1, english_face_middle_2 ],
["english_footman", "English Poor Spearman", "English Poor Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_chapel_de_fer_strap,itm_h_makeshift_kettle_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_4_strap,itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,
 itm_a_padded_over_mail_4_custom,itm_a_padded_over_mail_5_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,
], 
level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_warrior_basic2|knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, english_face_middle_1, english_face_mature_2 ],
["english_heavy_footman", "English Spearman", "English Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_skullcap_mail_aventail,
 itm_a_brigandine_asher_a_custom,itm_a_brigandine_asher_b_custom,
 itm_g_demi_gauntlets,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_bill_1,itm_w_bill_4,
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],
["english_sergeant", "English Rich Spearman", "English Rich Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_bill_2,itm_w_bill_3,
], 
level(25)|str_20|agi_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, english_face_mature_1, english_face_old_2 ],

### Ranged Line
["english_yeoman_archer", "English Yeoman Archer", "English Yeomen Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_hood_big_liripipe_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_straw_hat,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,itm_h_wicker_helmet_strap,itm_h_rope_helmet_strap,
 itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_beige_2,itm_a_aketon_asher_dagged_red_1,itm_a_aketon_asher_dagged_green_1,itm_a_aketon_asher_dagged_green_2,itm_a_aketon_asher_vandyked_red_1,itm_a_aketon_asher_vandyked_red_2,itm_a_aketon_asher_green_1,itm_a_aketon_asher_green_2,itm_a_aketon_asher_dagged_thick_red_1,itm_a_aketon_asher_dagged_thick_red_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_long_bow_ash,itm_w_arrow_triangular,
 itm_w_dagger_baselard,itm_w_dagger_quillon,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_a,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
], 
level(8)|str_10|agi_12, wpex(90,80,80,110,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, english_face_young_1, english_face_middle_2 ],
["english_archer", "English Archer", "English Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_hood_big_liripipe_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,
 itm_a_gambeson_asher_regular_custom,itm_a_gambeson_asher_belt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_long_bow_elm,itm_w_arrow_triangular_large,
 itm_w_dagger_baselard,itm_w_dagger_quillon,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_a,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
], 
level(12)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_young_1, english_face_middle_2 ],
["english_retinue_archer", "English Retinue Archer", "English Retinue Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,
 itm_a_padded_jack_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_long_bow_yew,itm_w_arrow_bodkin,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,
 itm_s_steel_buckler,
], 
level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],


##### Castle Troops

### Dismounted
["english_footman_at_arms", "English Footman-at-Arms", "English Footmen-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_awlpike_1,itm_w_awlpike_5,itm_w_twohanded_knight_battle_axe_01,itm_w_twohanded_knight_battle_axe_01_brown,itm_w_twohanded_knight_battle_axe_01_ebony,
], 
level(25)|str_20|agi_20, wp_melee(180), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, english_face_young_1, english_face_mature_2 ],

["english_dismounted_squire", "English Dismounted Squire", "English Dismounted Squires", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_b_plate_1_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_twohanded_sword_talhoffer,itm_w_bastard_falchion,itm_w_bastard_sword_agincourt,itm_w_bastard_sword_english,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_knight_battle_axe_02,itm_w_twohanded_knight_battle_axe_02_brown,itm_w_twohanded_knight_battle_axe_02_ebony,itm_w_awlpike_5,itm_w_pollaxe_blunt_05_ash,itm_w_pollaxe_blunt_alt_05_ash,itm_w_pollaxe_blunt_05_brown,itm_w_pollaxe_blunt_alt_05_brown,itm_w_pollaxe_cut_09_ash,itm_w_pollaxe_cut_09_brown,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_7|knows_power_strike_7|knows_athletics_4|knows_shield_4|knows_weapon_master_6, english_face_middle_1, english_face_mature_2 ],

["english_dismounted_knight", "English Dismounted Knight", "English Dismounted Knights", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_great_bascinet_english_1410,itm_h_great_bascinet_english_1410_visor,itm_h_great_bascinet_english_1410_visor_open,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_english_plate_1415_a,itm_a_english_plate_1415_b,itm_a_english_plate_1415_a_besagews_round,itm_a_english_plate_1415_b_besagews_round,itm_a_english_plate_1415_a_besagews_square,itm_a_english_plate_1415_b_besagews_square,
 itm_b_leg_harness_english_1415,itm_b_leg_harness_english_1420,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_pollaxe_blunt_04_english_ash,itm_w_pollaxe_blunt_alt_04_english_ash,itm_w_pollaxe_blunt_04_english_red_trim,itm_w_pollaxe_blunt_alt_04_english_red_trim,itm_w_pollaxe_blunt_04_english_dark,itm_w_pollaxe_blunt_alt_04_english_dark,itm_w_pollaxe_cut_04_english_ash,itm_w_pollaxe_cut_alt_04_english_ash,itm_w_pollaxe_cut_04_english_ebony,itm_w_pollaxe_cut_alt_04_english_ebony,(itm_w_bastard_sword_english,imodbit_masterwork),(itm_w_bastard_sword_agincourt,imodbit_masterwork),itm_w_twohanded_sword_earl,itm_w_twohanded_knight_battle_axe_03,itm_w_twohanded_knight_battle_axe_03_brown,itm_w_twohanded_knight_battle_axe_03_ebony,itm_w_awlpike_4,
], 
level(35)|str_28|agi_28, wp_melee(260), knows_ironflesh_8|knows_power_strike_8|knows_shield_5|knows_athletics_4|knows_weapon_master_8, english_face_mature_1, english_face_old_2 ],

### Mounted
["english_man_at_arms", "English Man-at-Arms", "English Men-at-Arms", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_native_spear_b_custom,itm_w_native_spear_f_custom,itm_w_mace_english,itm_w_mace_english_brown,itm_w_mace_english_ebony,itm_w_onehanded_horseman_axe_01,itm_w_onehanded_horseman_axe_01_brown,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,
 itm_s_heraldic_shield_heater,
 itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(25)|str_20|agi_20, wp_melee(150), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_3, english_face_young_1, english_face_middle_2 ],
["english_squire", "English Squire", "English Squires", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_b_plate_1_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_lance_1_custom,itm_w_lance_2_custom,itm_w_lance_3_custom,itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_03_brown,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_d,
 itm_s_heraldic_shield_leather,
 itm_ho_horse_barded_brown,itm_ho_horse_barded_red,itm_ho_horse_barded_red,itm_ho_horse_barded_white,
], 
level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, english_face_middle_1, english_face_mature_2 ],
["english_knight", "English Knight", "English Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_great_bascinet_english_1410,itm_h_great_bascinet_english_1410_visor,itm_h_great_bascinet_english_1410_visor_open,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_english_plate_1415_a,itm_a_english_plate_1415_b,itm_a_english_plate_1415_a_besagews_round,itm_a_english_plate_1415_b_besagews_round,itm_a_english_plate_1415_a_besagews_square,itm_a_english_plate_1415_b_besagews_square,
 itm_b_leg_harness_english_1415,itm_b_leg_harness_english_1420,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_lance_colored_english_1_custom,itm_w_lance_colored_english_2_custom,itm_w_lance_colored_english_3_custom,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_ebony,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_ebony,itm_w_knight_warhammer_3,itm_w_knight_warhammer_3_ebony,itm_w_knight_flanged_mace,itm_w_knight_winged_mace,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_ebony,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_ebony,(itm_w_bastard_sword_agincourt,imodbit_masterwork),(itm_w_bastard_sword_english,imodbit_masterwork),(itm_w_bastard_sword_d,imodbit_masterwork),(itm_w_bastard_sword_c,imodbit_masterwork),
 itm_s_heraldic_shield_bouche,
 itm_ho_horse_barded_brown_chamfrom,itm_ho_horse_barded_red_chamfrom,itm_ho_horse_barded_red_chamfrom,itm_ho_horse_barded_white_chamfrom,
], 
level(35)|str_28|agi_28, wp_melee(250), knows_ironflesh_8|knows_power_strike_8|knows_shield_4|knows_athletics_4|knows_weapon_master_8|knows_riding_5, english_face_mature_1, english_face_old_2 ],

# Special Troops
["english_bannerman", "English Bannerman", "English Bannermen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_b_plate_1_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_03_brown,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_d,
 itm_heraldic_banner,
],
 level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_7|knows_power_strike_7|knows_athletics_4|knows_shield_4|knows_weapon_master_6, english_face_middle_1, english_face_mature_2 ],
["english_bannerman_mounted", "English Mounted Bannerman", "English Mounted Bannermen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_b_plate_1_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_03_brown,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_d,
 itm_heraldic_banner,
 itm_ho_horse_barded_brown,itm_ho_horse_barded_red,itm_ho_horse_barded_red,itm_ho_horse_barded_white,
],
 level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5, english_face_middle_1, english_face_mature_2 ],

## END English Main Troops
["english_messenger", "English_Messenger", "Vaegir Messengers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5, english_face_young_1, english_face_middle_2 ],
["english_deserter", "English_Deserter", "Vaegir Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[], def_attrib|str_10|level(14), wp(80), knows_ironflesh_1|knows_power_draw_1, english_face_young_1, english_face_middle_2 ],
["english_prison_guard", "Prison Guard", "Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_awlpike_1,itm_w_awlpike_5,itm_w_twohanded_knight_battle_axe_01,itm_w_twohanded_knight_battle_axe_01_brown,itm_w_twohanded_knight_battle_axe_01_ebony,
], def_attrib|level(24), wp(130), knows_athletics_3|knows_shield_2|knows_ironflesh_3, english_face_mature_1, english_face_old_2 ],
["english_castle_guard", "Castle Guard", "Castle Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_awlpike_1,itm_w_awlpike_5,itm_w_twohanded_knight_battle_axe_01,itm_w_twohanded_knight_battle_axe_01_brown,itm_w_twohanded_knight_battle_axe_01_ebony,
], def_attrib|level(24), wp(130), knows_athletics_3|knows_shield_2|knows_ironflesh_3, english_face_mature_1, english_face_old_2 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC BURGUNDIAN TROOPS #####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

##### Village Troops

### Ranged Line
["burgundian_peasant_bowman", "Burgundian Peasant Bowman", "Burgundian Peasant Bowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif,itm_h_straw_hat,itm_h_woolen_cap_blue,itm_h_woolen_cap_white,itm_h_woolen_cap_brown,
 itm_a_peasant_cotehardie_custom,itm_a_peasant_cote_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_1,
 itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_short_bow_elm,itm_w_short_bow_oak,itm_w_arrow_triangular,itm_w_arrow_triangular,itm_w_arrow_triangular,
], 
level(8)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_poor_bowman", "Burgundian Poor Bowman", "Burgundian Poor Bowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bycocket_1_custom,itm_h_bycocket_2_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_skullcap_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,
 itm_a_tailored_cotehardie_custom,itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,itm_g_leather_gauntlet,
 itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_dagger_quillon,itm_w_dagger_bollock,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_hunting_bow_ash,itm_w_hunting_bow_elm,itm_w_hunting_bow_yew,itm_w_arrow_triangular,itm_w_arrow_triangular,
], 
level(12)|str_12|agi_14, wpex(100,80,80,120,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_bowman", "Burgundian Bowman", "Burgundian Bowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,itm_g_leather_gauntlet,
 itm_w_dagger_baselard,itm_w_dagger_rondel,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,
 itm_w_war_bow_ash,itm_w_war_bow_elm,itm_w_arrow_triangular_large,itm_w_arrow_triangular_large,
], 
level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],

### Infantry Line
["burgundian_peasant", "Burgundian Peasant", "Burgundian Peasants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_straw_hat_1,itm_h_simple_coif,itm_h_straw_hat,itm_h_arming_cap,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_fork_1,itm_w_fork_2,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
], 
level(6)|str_10|agi_10, wpex(80,80,80,80,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_athletics_2, burgundian_face_young_1, burgundian_face_middle_2 ],

["burgundian_poor_spearman", "Burgundian Poor Spearman", "Burgundian Poor Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,
 itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_burgundian_3,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_burgundian_5,itm_s_heater_shield_burgundian_6,
], 
level(10)|str_12|agi_12, wpex(120,80,80,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_spearman", "Burgundian Spearman", "Burgundian Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_mail_aventail,
 itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,itm_a_light_gambeson_long_sleeves_alt_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_defiant,itm_w_onehanded_falchion_peasant,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_mace_spiked_red,
 itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_burgundian_3,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_burgundian_5,itm_s_heater_shield_burgundian_6,
], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, burgundian_face_middle_1, burgundian_face_mature_2 ],

["burgundian_poor_vougier", "Burgundian Poor Vougier", "Burgundian Poor Vougier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_glaive_2,itm_w_glaive_2_brown,itm_w_glaive_2_red,itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,
], 
level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_vougier", "Burgundian Vougier", "Burgundian Vougiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_mail_aventail,
 itm_a_light_gambeson_long_sleeves_3_custom,itm_a_light_gambeson_long_sleeves_6_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_glaive_1,itm_w_glaive_1_brown,itm_w_glaive_1_red,itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],

##### Town Troops

### Ranged Line

["burgundian_militia_archer", "Burgundian Militia Archer", "Burgundian Militia Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_arming_cap,itm_h_simple_coif,itm_h_wicker_helmet_strap,itm_h_rope_helmet_strap,itm_h_skullcap_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_cervelliere_strap,
 itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_beige_2,itm_a_aketon_asher_dagged_white_1,itm_a_aketon_asher_dagged_white_2,itm_a_aketon_asher_dagged_red_1,itm_a_aketon_asher_dagged_red_2,itm_a_aketon_asher_dagged_thick_black_1,itm_a_aketon_asher_dagged_thick_black_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_b,
 itm_w_hunting_bow_ash,itm_w_hunting_bow_elm,itm_w_hunting_bow_oak,itm_w_arrow_triangular,
 ], 
level(8)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_poor_archer", "Burgundian Poor Archer", "Burgundian Poor Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_war_bow_elm,itm_w_war_bow_oak,itm_w_arrow_triangular_large,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 ], 
level(12)|str_12|agi_14, wpex(100,80,80,120,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_archer", "Burgundian Archer", "Burgundian Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,
 itm_a_padded_jack_custom,
 itm_b_high_boots_lined_1,itm_b_high_boots_lined_2,itm_b_high_boots_lined_3,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_messer,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_sovereign,itm_w_onehanded_war_axe_04,itm_w_onehanded_war_axe_04_brown,itm_w_onehanded_war_axe_04_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,
 itm_w_long_bow_ash,itm_w_long_bow_elm,itm_w_arrow_bodkin,itm_w_arrow_bodkin,
], 
level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],

["burgundian_poor_crossbowman", "Burgundian Poor Crossbowman", "Burgundian Poor Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_2_strap,itm_h_german_kettlehat_3_strap,itm_h_german_kettlehat_4_strap,itm_h_german_kettlehat_5_strap,itm_h_german_kettlehat_6_strap,itm_h_german_kettlehat_7_strap,itm_h_sallet_curved_strap,itm_h_sallet_strap,itm_h_cervelliere_mail_aventail,itm_h_cervelliere_roundels_mail_aventail,
 itm_a_simple_gambeson_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_goedendag,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_crossbow_medium,itm_w_bolt_triangular,
 ], 
level(12)|str_13|agi_12, wpex(100,80,80,80,120,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_crossbowman", "Burgundian Crossbowman", "Burgundian Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,
 itm_a_gambeson_asher_regular_custom,itm_a_gambeson_asher_belt_custom,
 itm_b_high_boots_lined_1,itm_b_high_boots_lined_2,itm_b_high_boots_lined_3,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_messer,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_sovereign,itm_w_onehanded_war_axe_04,itm_w_onehanded_war_axe_04_brown,itm_w_onehanded_war_axe_04_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,itm_w_goedendag_burgundy,itm_w_goedendag,
 itm_w_crossbow_heavy,itm_w_bolt_triangular_large,
], 
level(16)|str_15|agi_13, wpex(120,80,80,80,150,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],

### Infantry Line
["burgundian_militia", "Burgundian Militia", "Burgundian Militias", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_wicker_helmet_strap,itm_h_rope_helmet_strap,itm_h_shingle_helmet_strap,itm_h_skullcap_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_cervelliere_strap,itm_h_makeshift_kettle_strap,
 itm_a_light_gambeson_long_sleeves_3_custom,itm_a_light_gambeson_long_sleeves_6_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_spear_8,itm_w_spear_9,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_dagger_quillon,itm_w_dagger_rondel,itm_w_dagger_baselard,
 itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_burgundian_3,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_burgundian_5,itm_s_heater_shield_burgundian_6,
 ], 
level(10)|str_12|agi_12, wpex(120,80,80,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],

["burgundian_poor_pavoisier", "Burgundian Poor Pavoisier", "Burgundian Poor Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_2_strap,itm_h_german_kettlehat_3_strap,itm_h_german_kettlehat_4_strap,itm_h_german_kettlehat_5_strap,itm_h_german_kettlehat_6_strap,itm_h_german_kettlehat_7_strap,
 itm_a_gambeson_asher_regular_custom,itm_a_gambeson_asher_belt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_spear_8,itm_w_spear_9,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_dagger_quillon,itm_w_dagger_rondel,itm_w_dagger_baselard,
 itm_s_pavise_burgundian_4,itm_s_pavise_burgundian_3,itm_s_pavise_burgundian_2,itm_s_pavise_burgundian_1,
], 
level(15)|str_15|agi_13, wpex(100,100,140,100,100,100), knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_pavoisier", "Burgundian Pavoisier", "Burgundian Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_2_strap,itm_h_german_kettlehat_3_strap,itm_h_german_kettlehat_4_strap,itm_h_german_kettlehat_5_strap,itm_h_german_kettlehat_6_strap,itm_h_german_kettlehat_7_strap,itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,
 itm_a_padded_over_mail_heavy_4_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_1_custom,
 itm_g_leather_gauntlet,itm_g_demi_gauntlets,
 itm_b_high_boots_lined_1,itm_b_high_boots_lined_2,itm_b_high_boots_lined_3,
 itm_w_spear_3,itm_w_spear_6,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,
 itm_s_pavise_burgundian_1,itm_s_pavise_burgundian_2,itm_s_pavise_burgundian_3,itm_s_pavise_burgundian_4,
], 
level(20)|str_17|agi_16, wpex(100,100,160,100,100,100), knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_rich_pavoisier", "Burgundian Rich Pavoisier", "Burgundian Rich Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_corrazina_hohenaschau_custom,itm_a_corrazina_hohenaschau_mail_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,itm_b_leg_harness_8,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_flemish,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_burgundian_5,itm_s_tall_pavise_burgundian_4,itm_s_tall_pavise_burgundian_3,itm_s_tall_pavise_burgundian_2,itm_s_tall_pavise_burgundian_1,
], 
level(25)|str_20|agi_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, burgundian_face_mature_1, burgundian_face_old_2 ],
["burgundian_sergeant_pavoisier", "Burgundian Sergeant Pavoisier", "Burgundian Sergeants Pavoisier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_pigface_klappvisor,itm_h_pigface_klappvisor_open,itm_h_zitta_bascinet,itm_h_zitta_bascinet_open,itm_h_wespe_bascinet_a,itm_h_wespe_bascinet_b,itm_h_wespe_bascinet_c,itm_h_wespe_bascinet_a_open,itm_h_wespe_bascinet_b_open,itm_h_wespe_bascinet_c_open,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,
 itm_a_pistoia_kastenbrust_a_mail_sleeves_jackchain,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_2,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_3,itm_a_pistoia_kastenbrust_b_mail_sleeves_jackchain,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_mail_sleeves_jackchain,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_3,
 itm_g_gauntlets_mailed,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,itm_b_leg_harness_8,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_messer,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_forsaken,itm_w_spear_9,itm_w_spear_10,itm_w_spear_11,
 itm_s_tall_pavise_burgundian_1,itm_s_tall_pavise_burgundian_2,itm_s_tall_pavise_burgundian_3,itm_s_tall_pavise_burgundian_4,itm_s_tall_pavise_burgundian_5,
], 
level(25)|str_20|agi_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, burgundian_face_mature_1, burgundian_face_old_2 ],

["burgundian_poor_guisarmier", "Burgundian Poor Guisarmier", "Burgundian Poor Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_2_strap,itm_h_german_kettlehat_3_strap,itm_h_german_kettlehat_4_strap,itm_h_german_kettlehat_5_strap,itm_h_german_kettlehat_6_strap,itm_h_german_kettlehat_7_strap,
 itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_4,itm_b_turnshoes_5,
 itm_w_fauchard_2,itm_w_fauchard_3,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_6,
], 
level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_guisarmier", "Burgundian Guisarmier", "Burgundian Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[ 
 itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_brigandine_asher_mail_custom,itm_a_brigandine_asher_custom,
 itm_b_high_boots_lined_1,itm_b_high_boots_lined_2,itm_b_high_boots_lined_3,
 itm_w_awlpike_7,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_1,itm_w_glaive_2,itm_w_glaive_3,itm_w_glaive_1_brown,itm_w_glaive_1_red,itm_w_glaive_2_brown,itm_w_glaive_2_red,itm_w_glaive_3_brown,itm_w_glaive_3_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_rich_guisarmier", "Burgundian Rich Guisarmier", "Burgundian Rich Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_2_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_4_mail_aventail,itm_h_german_kettlehat_5_mail_aventail,itm_h_german_kettlehat_6_mail_aventail,
 itm_a_brigandine_asher_plate_1_custom,itm_a_brigandine_asher_plate_2_custom,itm_a_brigandine_asher_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,itm_b_leg_harness_8,
 itm_w_awlpike_7,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_4,itm_w_glaive_4_brown,itm_w_glaive_4_ebony,itm_w_glaive_5,itm_w_glaive_5_red,itm_w_glaive_5_brown,itm_w_glaive_6,itm_w_glaive_6_brown,itm_w_glaive_6_red,
], 
level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],


##### Castle Troops

### Dismounted
["burgundian_footman_at_arms", "Burgundian Footman-at-Arms", "Burgundian Footmen-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_corrazina_capwell_custom,
 itm_g_gauntlets_mailed,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_sempach,itm_w_twohanded_war_axe_02,itm_w_twohanded_war_axe_02_brown,itm_w_twohanded_war_axe_02_red,itm_w_twohanded_war_axe_03,itm_w_twohanded_war_axe_03_brown,itm_w_twohanded_war_axe_03_red,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_4_red,itm_w_bardiche_7,itm_w_bardiche_7_brown,itm_w_bardiche_7_red,itm_w_kriegshammer,itm_w_kriegshammer_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,
], 
level(25)|str_20|agi_20, wp_melee(160), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_dismounted_squire", "Burgundian Dismounted Squire", "Burgundian Dismounted Squires", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,
 itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_german_covered_fauld_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_a,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_d,itm_w_bastard_sword_german,itm_w_bastard_sword_sempach,itm_w_bastard_sword_landgraf,itm_w_bastard_sword_baron,itm_w_twohanded_sword_messer,itm_w_twohanded_sword_messer_b,itm_w_twohanded_knight_battle_axe_01,itm_w_twohanded_knight_battle_axe_01_brown,itm_w_twohanded_knight_battle_axe_01_ebony,itm_w_bardiche_5,itm_w_bardiche_5_brown,itm_w_bardiche_5_red,itm_w_bardiche_6,itm_w_bardiche_6_brown,itm_w_bardiche_6_red,itm_w_kriegshammer_ebony,itm_w_awlpike_4,itm_w_awlpike_5,itm_w_pollaxe_blunt_03_ash,itm_w_pollaxe_blunt_03_brown,itm_w_pollaxe_blunt_03_ebony_trim,itm_w_pollaxe_blunt_03_red_trim,itm_w_pollaxe_blunt_05_ash,itm_w_pollaxe_blunt_05_brown,itm_w_pollaxe_blunt_05_ebony,itm_w_pollaxe_cut_01_burgundian_ash,itm_w_pollaxe_cut_01_burgundian_dark,itm_w_pollaxe_cut_01_burgundian_ebony_trim,
], 
level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_4|knows_athletics_4|knows_weapon_master_5, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_dismounted_knight", "Burgundian Dismounted Knight", "Burgundian Dismounted Knights", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_great_bascinet_continental,itm_h_great_bascinet_continental_roundels,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,
 itm_a_padded_over_plate_sleeved_1_custom,itm_a_padded_over_plate_sleeved_2_custom,itm_a_padded_over_plate_shortsleeved_1_custom,itm_a_padded_over_plate_shortsleeved_2_custom,itm_a_padded_over_plate_shortsleeved_3_custom,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_b_leg_harness_4,itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_w_bastard_sword_d,itm_w_bastard_sword_german,itm_w_bastard_sword_duke,itm_w_bastard_sword_landgraf,itm_w_bastard_sword_sempach,itm_w_bastard_falchion,itm_w_twohanded_sword_messer,itm_w_twohanded_sword_messer_b,itm_w_twohanded_sword_talhoffer,itm_w_twohanded_sword_talhoffer_mordhau,itm_w_twohanded_knight_battle_axe_02,itm_w_twohanded_knight_battle_axe_02_brown,itm_w_twohanded_knight_battle_axe_02_ebony,itm_w_twohanded_knight_battle_axe_03,itm_w_twohanded_knight_battle_axe_03_brown,itm_w_twohanded_knight_battle_axe_03_ebony,itm_w_bardiche_6,itm_w_bardiche_6_brown,itm_w_bardiche_6_red,itm_w_pollaxe_blunt_07_ash,itm_w_pollaxe_blunt_07_ebony,itm_w_pollaxe_blunt_12_ash,itm_w_pollaxe_blunt_12_brown,itm_w_pollaxe_cut_07_red,itm_w_pollaxe_cut_07_brown,itm_w_pollaxe_cut_07_ash,itm_w_pollaxe_cut_08_burgundian_ash,itm_w_pollaxe_cut_08_burgundian_brown,itm_w_pollaxe_cut_08_burgundian_red,
], 
level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5, burgundian_face_mature_1, burgundian_face_old_2 ],

### Mounted
["burgundian_man_at_arms", "Burgundian Man-at-Arms", "Burgundian Men-at-Arms", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_corrazina_capwell_custom,
 itm_g_gauntlets_mailed,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_squire,itm_w_onehanded_horseman_axe_01,itm_w_onehanded_horseman_axe_01_brown,itm_w_onehanded_horseman_axe_01_red,itm_w_mace_german,itm_w_mace_german_brown,itm_w_mace_german_ebony,itm_w_light_lance,itm_w_native_spear_b,
 itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_burgundian_3,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_burgundian_5,itm_s_heater_shield_burgundian_6,
 itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(25)|str_20|agi_20, wp_melee(170), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_3, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_squire", "Burgundian Squire", "Burgundian Squires", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,
 itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_german_covered_fauld_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_a,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_sword_martyr,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_02_red,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_03_brown,itm_w_onehanded_horseman_axe_03_red,itm_w_onehanded_knight_axe_german_02,itm_w_onehanded_knight_axe_german_02_ebony,itm_w_onehanded_knight_axe_german_02_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_lance_1,itm_w_lance_2,itm_w_lance_6,
 itm_s_hand_pavise_burgundian_1,itm_s_hand_pavise_burgundian_2,itm_s_hand_pavise_burgundian_3,
 itm_ho_horse_barded_black,itm_ho_horse_barded_blue,itm_ho_horse_barded_brown,itm_ho_horse_barded_red,
], 
level(28)|str_22|agi_22, wp_melee(190), knows_ironflesh_7|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_knight", "Burgundian Knight", "Burgundian Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_great_bascinet_continental,itm_h_great_bascinet_continental_roundels,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,
 itm_a_padded_over_plate_sleeved_1_custom,itm_a_padded_over_plate_sleeved_2_custom,itm_a_padded_over_plate_shortsleeved_1_custom,itm_a_padded_over_plate_shortsleeved_2_custom,itm_a_padded_over_plate_shortsleeved_3_custom,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_b_leg_harness_4,itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_sword_martyr,itm_w_onehanded_knight_axe_german_01,itm_w_onehanded_knight_axe_german_01_brown,itm_w_onehanded_knight_axe_german_01_ebony,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_ebony,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_ebony,itm_w_knight_warhammer_2_ebony,itm_w_knight_warhammer_2,itm_w_knight_flanged_mace,itm_w_lance_colored_english_1,itm_w_lance_colored_english_2,itm_w_lance_colored_english_3,
 itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3,itm_s_heraldic_shield_burgundian_4,itm_s_heraldic_shield_burgundian_5,itm_s_heraldic_shield_burgundian_6,itm_s_heraldic_shield_burgundian_7,
 itm_ho_horse_barded_black_chamfrom,itm_ho_horse_barded_blue_chamfrom,itm_ho_horse_barded_brown_chamfrom,itm_ho_horse_barded_red_chamfrom,
], 
level(30)|str_24|agi_24, wp_melee(215), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5, burgundian_face_middle_1, burgundian_face_mature_2 ],

# Special Troops
["burgundian_bannerman", "Burgundian Bannerman", "Burgundian Bannermen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,
 itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_german_covered_fauld_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_a,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_sword_martyr,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_02_red,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_03_brown,itm_w_onehanded_horseman_axe_03_red,itm_w_onehanded_knight_axe_german_02,itm_w_onehanded_knight_axe_german_02_ebony,itm_w_onehanded_knight_axe_german_02_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_warhammer_2,itm_w_warhammer_2_brown,
 itm_heraldic_banner,
], 
level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5, burgundian_face_mature_1, burgundian_face_old_2 ],
["burgundian_bannerman_mounted", "Burgundian Mounted Bannerman", "Burgundian Mounted Bannermen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,
 itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_german_covered_fauld_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_a,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_sword_martyr,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_02_red,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_03_brown,itm_w_onehanded_horseman_axe_03_red,itm_w_onehanded_knight_axe_german_02,itm_w_onehanded_knight_axe_german_02_ebony,itm_w_onehanded_knight_axe_german_02_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_warhammer_2,itm_w_warhammer_2_brown,
 itm_heraldic_banner,
 itm_ho_horse_barded_black,itm_ho_horse_barded_blue,itm_ho_horse_barded_brown,itm_ho_horse_barded_red,
], 
level(30)|str_24|agi_24, wp_melee(215), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5, burgundian_face_middle_1, burgundian_face_mature_2 ],

## END Burgundy Main Troops
["burgundian_messenger", "Burgundian Messenger", "Burgundian Messenger", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_deserter", "Burgundian Deserter", "Burgundian Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, 
[], def_attrib|str_10|level(14), wp(80), knows_ironflesh_1|knows_power_draw_1, burgundian_face_young_1, burgundian_face_middle_2 ],
["burgundian_prison_guard", "Burgundian Prison Guard", "Burgundian Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_corrazina_capwell_custom,
 itm_g_gauntlets_mailed,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_sempach,itm_w_twohanded_war_axe_02,itm_w_twohanded_war_axe_02_brown,itm_w_twohanded_war_axe_02_red,itm_w_twohanded_war_axe_03,itm_w_twohanded_war_axe_03_brown,itm_w_twohanded_war_axe_03_red,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_4_red,itm_w_bardiche_7,itm_w_bardiche_7_brown,itm_w_bardiche_7_red,itm_w_kriegshammer,itm_w_kriegshammer_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,
], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_2, burgundian_face_mature_1, burgundian_face_old_2 ],
["burgundian_castle_guard", "Burgundian Castle Guard", "Burgundian Castle Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_mail_collar,itm_h_sallet_curved_mail_collar,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,
 itm_a_corrazina_spina_custom,itm_a_corrazina_capwell_custom,
 itm_g_gauntlets_mailed,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_sempach,itm_w_twohanded_war_axe_02,itm_w_twohanded_war_axe_02_brown,itm_w_twohanded_war_axe_02_red,itm_w_twohanded_war_axe_03,itm_w_twohanded_war_axe_03_brown,itm_w_twohanded_war_axe_03_red,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_4_red,itm_w_bardiche_7,itm_w_bardiche_7_brown,itm_w_bardiche_7_red,itm_w_kriegshammer,itm_w_kriegshammer_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,
], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, burgundian_face_mature_1, burgundian_face_old_2 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC Breton TROOPS ########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

##### Village Troops

### Ranged Line
["breton_peasant_archer", "Breton Peasant Archer", "Breton Peasant Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, [
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif,itm_h_straw_hat,itm_h_woolen_cap_blue,itm_h_woolen_cap_white,itm_h_woolen_cap_brown,
 itm_a_peasant_cotehardie_custom,itm_a_peasant_cote_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_1,
 itm_w_dagger_quillon,itm_w_dagger_pikeman,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_short_bow_elm,itm_w_short_bow_oak,itm_w_arrow_triangular,itm_w_arrow_triangular,itm_w_arrow_triangular,
], 
level(8)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["breton_poor_archer_ordonnance", "Breton Poor Archer d'Ordonnance", "Breton Poor Archers d'Ordonnance", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, [
 itm_h_bycocket_1_custom,itm_h_bycocket_2_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_skullcap_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,
 itm_a_tailored_cotehardie_custom,itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_g_leather_gauntlet,
 itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_a,itm_w_onehanded_falchion_peasant,itm_w_dagger_quillon,itm_w_dagger_bollock,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_hunting_bow_ash,itm_w_hunting_bow_elm,itm_w_hunting_bow_yew,itm_w_arrow_triangular,itm_w_arrow_triangular,
], 
level(12)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["breton_archer_ordonnance", "Breton Archer d'Ordonnance", "Breton Archers d'Ordonnance", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, [
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_lined_1,itm_b_high_boots_lined_2,itm_g_leather_gauntlet,
 itm_w_dagger_baselard,itm_w_dagger_rondel,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,
 itm_w_war_bow_ash,itm_w_war_bow_elm,itm_w_arrow_triangular_large,itm_w_arrow_triangular_large,
], 
level(15)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],


### Infantry Line
["breton_peasant_levy", "Breton Peasant Levy", "Breton Peasants Levies", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_4, [
itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_straw_hat_1,itm_h_simple_coif,itm_h_straw_hat,itm_h_arming_cap,
itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,
itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_fork_1,itm_w_fork_2,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
],
level(6)|str_10|agi_10,wpex(80,80,80,80,80,80),knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_athletics_2,french_face_young_1,french_face_middle_2],
["breton_poor_spearman", "Breton Poor Pavoisier d'Ordonnance", "Breton Poor Pavoisiers d'Ordonnance", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, [
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_light_gambeson_short_sleeves_custom,itm_a_light_gambeson_short_sleeves_diamond_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,
 itm_s_pavise_breton_1,itm_s_pavise_breton_2,itm_s_pavise_breton_3,
], 
level(10)|str_12|agi_12, wpex(120,80,80,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["breton_spearman", "Breton Pavoisier d'Ordonnance", "Breton Pavoisiers d'Ordonnance", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, [
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_mail_aventail,
 itm_a_light_gambeson_long_sleeves_custom,itm_a_light_gambeson_long_sleeves_diamond_custom,itm_a_light_gambeson_long_sleeves_alt_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_defiant,itm_w_onehanded_falchion_peasant,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_spiked,itm_w_mace_spiked_brown,itm_w_mace_spiked_red,
 itm_s_pavise_breton_1,itm_s_pavise_breton_2,itm_s_pavise_breton_3,
], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],
["breton_vougier", "Breton Vougier", "Breton Vougier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, [
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_mail_aventail,
 itm_a_light_gambeson_long_sleeves_3_custom,itm_a_light_gambeson_long_sleeves_6_custom,
 itm_g_leather_gauntlet,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_glaive_1,itm_w_glaive_1_brown,itm_w_glaive_1_red,itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,
], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],


##### City Troops
### Ranged Line
["breton_militia_crossbowman", "Breton Militia Crossbowman", "Breton Militia Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_arming_cap,itm_h_simple_coif,itm_h_simple_coif_black,itm_h_simple_coif_brown,itm_h_straw_hat,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_white,itm_h_skullcap_hood_liripipe_custom,itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,
 itm_a_aketon_asher_blue_1,itm_a_aketon_asher_blue_2,itm_a_aketon_asher_vandyked_blue_1,itm_a_aketon_asher_vandyked_blue_2,itm_a_aketon_asher_dagged_beige_1,itm_a_aketon_asher_dagged_beige_2,itm_a_aketon_asher_dagged_white_1,itm_a_aketon_asher_dagged_white_2,itm_a_aketon_asher_dagged_thick_beige_1,itm_a_aketon_asher_dagged_thick_beige_2,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_crossbow_light,itm_w_bolt_triangular,
 itm_w_goedendag,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_dagger_baselard,itm_w_dagger_quillon,
], 
level(12)|str_13|agi_12, wpex(100,80,80,80,110,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["breton_poor_archer", "Breton Poor Archer", "Breton Poor Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_war_bow_elm,itm_w_war_bow_oak,itm_w_arrow_triangular_large,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 ], 
level(12)|str_12|agi_14, wpex(100,80,80,120,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, burgundian_face_young_1, burgundian_face_middle_2 ],
["breton_archer", "Breton Archer", "Breton Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,
 itm_a_padded_jack_custom,
 itm_b_high_boots_lined_1,itm_b_high_boots_lined_2,itm_b_high_boots_lined_3,
 itm_w_onehanded_sword_flemish,itm_w_onehanded_sword_messer,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_c,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_sovereign,itm_w_onehanded_war_axe_04,itm_w_onehanded_war_axe_04_brown,itm_w_onehanded_war_axe_04_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,
 itm_w_long_bow_ash,itm_w_long_bow_elm,itm_w_arrow_bodkin,itm_w_arrow_bodkin,
], 
level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],
["breton_poor_crossbowman", "Breton Poor Crossbowman", "Breton Poor Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,itm_h_shingle_helmet_strap,
 itm_a_gambeson_crossbowman_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_lined_2,itm_b_high_boots_lined_1,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_goedendag, 
 itm_w_crossbow_medium,itm_w_bolt_triangular_large,
], 
level(16)|str_15|agi_13, wpex(120,80,80,80,130,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["breton_crossbowman", "Breton Crossbowman", "Breton Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_german_kettlehat_7_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_gambeson_crossbowman_heavy_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_goedendag,
 itm_w_crossbow_heavy,itm_w_bolt_bodkin,
], 
level(22)|str_17|agi_15, wpex(140,80,80,80,150,80), knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_athletics_3|knows_weapon_master_3, french_face_middle_1, french_face_old_2 ],

### Infantry Line
["breton_militia", "Breton Militia", "Breton Militia", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,
 itm_a_simple_gambeson_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,itm_b_turnshoes_6,itm_b_turnshoes_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,
 itm_s_heraldic_shield_french_1,itm_s_heraldic_shield_french_2,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_french_4,itm_s_heraldic_shield_french_5,itm_s_heraldic_shield_french_6,itm_s_heraldic_shield_french_7,
], 
level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],
["breton_poor_pavoisier", "Breton Poor Pavoisier", "Breton Poor Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,itm_a_pistoia_mail_a_mail_sleeves_jackchains,itm_a_pistoia_mail_b_mail_sleeves_jackchains,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_leather_gauntlet,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_breton_3,itm_s_tall_pavise_breton_2,itm_s_tall_pavise_breton_1,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["breton_pavoisier", "Breton Pavoisier", "Breton Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_padded_over_mail_heavy_1_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_4_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_breton_1,itm_s_tall_pavise_breton_2,itm_s_tall_pavise_breton_3,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["breton_rich_pavoisier", "Breton Rich Pavoisier", "Breton Rich Pavoisiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,
 itm_s_tall_pavise_breton_1,itm_s_tall_pavise_breton_2,itm_s_tall_pavise_breton_3,
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],

["breton_poor_guisarmier", "Breton Poor Guisarmier", "Breton Poor Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_brigandine_asher_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["breton_guisarmier", "Breton Guisarmier", "Breton Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_brigandine_asher_a_mail_custom,itm_a_brigandine_asher_a_mail_jackchain_custom,itm_a_brigandine_asher_b_mail_custom,itm_a_brigandine_asher_b_mail_jackchain_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["breton_rich_guisarmier", "Breton Rich Guisarmier", "Breton Rich Guisarmiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,
 itm_w_glaive_4,itm_w_glaive_4_brown,itm_w_glaive_4_ebony,itm_w_glaive_6,itm_w_glaive_6_brown,itm_w_glaive_6_red,
], 
level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_warrior_basic2|knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, french_face_middle_1, french_face_mature_2 ],
["breton_sergeant", "Breton Sergeant", "Breton Sergeants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2,itm_a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_3,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_demi_gauntlets,
 itm_w_glaive_4,itm_w_glaive_4_brown,itm_w_glaive_4_ebony,itm_w_glaive_6,itm_w_glaive_6_brown,itm_w_glaive_6_red,
], 
level(25)|str_20|agi_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, french_face_mature_1, french_face_old_2 ],

##### Castle Troops
### Noble Line
["breton_footman_at_arms", "Breton Homme d'Armes à Pied", "Breton Hommes d'Armes à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,itm_a_corrazina_spina_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], 
level(25)|str_20|agi_20, wp_melee(160), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, french_face_young_1, french_face_mature_2 ],
["breton_dismounted_squire", "Breton Écuyer à Pied", "Breton Écuyers à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], 
level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, french_face_young_1, french_face_mature_2 ],
["breton_chevalier_a_pied", "Breton Chevalier à Pied", "Breton Chevaliers à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_great_bascinet_continental,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,itm_h_great_bascinet_continental_visor_c_gilded,itm_h_great_bascinet_continental_visor_c_gilded_open,itm_h_great_bascinet_continental_visor_c_strip,itm_h_great_bascinet_continental_visor_c_strip_open,itm_h_great_bascinet_continental_1430,itm_h_great_bascinet_continental_1430_visor,itm_h_great_bascinet_continental_1430_visor_open,
 itm_a_padded_over_plate_sleeved_1_custom,itm_a_padded_over_plate_sleeved_2_custom,itm_a_padded_over_plate_shortsleeved_1_custom,itm_a_padded_over_plate_shortsleeved_2_custom,itm_a_padded_over_plate_shortsleeved_3_custom,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_w_bardiche_7,itm_w_bardiche_7_brown,itm_w_bardiche_7_red,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_twohanded_knight_battle_axe_03,itm_w_twohanded_knight_battle_axe_03_brown,itm_w_twohanded_knight_battle_axe_03_ebony,itm_w_pollaxe_blunt_05_ash,itm_w_pollaxe_blunt_alt_05_ash,itm_w_pollaxe_blunt_05_brown,itm_w_pollaxe_blunt_alt_05_brown,itm_w_pollaxe_blunt_05_ebony,itm_w_pollaxe_blunt_alt_05_ebony,itm_w_pollaxe_blunt_08_ash,itm_w_pollaxe_blunt_alt_08_ash,itm_w_pollaxe_blunt_08_brown,itm_w_pollaxe_blunt_alt_08_brown,itm_w_pollaxe_cut_03_ash,itm_w_pollaxe_cut_alt_03_ash,itm_w_pollaxe_cut_03_brown,itm_w_pollaxe_cut_alt_03_brown,itm_w_pollaxe_cut_03_red_trim,itm_w_pollaxe_cut_alt_03_red_trim,
 itm_w_bastard_falchion,itm_w_bastard_sword_crecy,itm_w_bastard_sword_agincourt,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,
], level(30)|str_24|agi_24, 
wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6, french_face_middle_1, french_face_mature_2 ],

["breton_man_at_arms", "Breton Homme d'Armes", "Breton Hommes d'Armes", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,itm_a_corrazina_spina_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_s_heater_shield_breton_1,itm_s_heater_shield_breton_2,itm_s_heater_shield_breton_3,itm_s_heater_shield_breton_4,itm_s_heraldic_shield_heater,
 itm_w_native_spear_b,itm_w_native_spear_b_custom,
 itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_squire,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,
 itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(25)|str_20|agi_20, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, french_face_young_1, french_face_middle_2 ],
["breton_squire", "Breton Écuyer", "Breton Écuyers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_plate_kastenbrust_a,itm_a_plate_kastenbrust_b,itm_a_plate_kastenbrust_c,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,itm_s_heraldic_shield_breton_4,itm_s_heraldic_shield_breton_5,itm_s_heraldic_shield_breton_6,itm_s_heraldic_shield_breton_7,itm_s_heraldic_shield_leather,
 itm_w_native_spear_f,itm_w_native_spear_f_custom,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_poitiers,itm_w_onehanded_horseman_axe_01,itm_w_onehanded_horseman_axe_01_alt,itm_w_onehanded_horseman_axe_01_brown,itm_w_onehanded_horseman_axe_01_alt_brown,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_02_alt,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_02_alt_brown,itm_w_warhammer_1,itm_w_warhammer_1_alt,itm_w_warhammer_1_brown,itm_w_warhammer_1_alt_brown,itm_w_warhammer_2,itm_w_warhammer_2_alt,itm_w_warhammer_2_brown,itm_w_warhammer_2_alt_brown,
 itm_ho_courser_1,itm_ho_courser_2,itm_ho_courser_3,itm_ho_courser_4,itm_ho_courser_5,itm_ho_courser_6,itm_ho_courser_7,itm_ho_courser_8,
], 
level(28)|str_22|agi_22, wp_melee(200), knows_ironflesh_7|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],
["breton_chevalier", "Breton Chevalier", "Breton Chevaliers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_great_bascinet_continental,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,itm_h_great_bascinet_continental_visor_c_gilded,itm_h_great_bascinet_continental_visor_c_gilded_open,itm_h_great_bascinet_continental_visor_c_strip,itm_h_great_bascinet_continental_visor_c_strip_open,itm_h_great_bascinet_continental_1430,itm_h_great_bascinet_continental_1430_visor,itm_h_great_bascinet_continental_1430_visor_open,
 itm_a_padded_over_plate_sleeved_1_custom,itm_a_padded_over_plate_sleeved_2_custom,itm_a_padded_over_plate_shortsleeved_1_custom,itm_a_padded_over_plate_shortsleeved_2_custom,itm_a_padded_over_plate_shortsleeved_3_custom,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_w_lance_colored_french_1_custom,itm_w_lance_colored_french_2_custom,itm_w_lance_colored_french_3_custom,
 itm_s_hand_pavise_breton_1,itm_s_hand_pavise_breton_2,itm_s_hand_pavise_breton_3,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_alt_brown,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_alt_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
 itm_ho_horse_barded_blue,itm_ho_horse_barded_brown,itm_ho_horse_barded_green,itm_ho_horse_barded_white,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],

# Special Troops
["breton_bannerman", "Breton Porteur d'Étandard à Pied", "Breton Porteurs d'Étandard à Pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_english_plate_1415_heraldic,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_heraldic_banner,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_alt_brown,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_alt_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
], 
level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6, french_face_middle_1, french_face_mature_2 ],
["breton_bannerman_mounted", "Breton Porteur d'Étandard", "Breton Porteurs d'Étandard", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_english_plate_1415_heraldic,
 itm_b_leg_harness_7,itm_b_leg_harness_8,itm_b_leg_harness_9,itm_b_leg_harness_10,
 itm_g_gauntlets_segmented_a,
 itm_heraldic_banner,
 itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_onehanded_knight_axe_02_brown,itm_w_onehanded_knight_axe_02_alt_brown,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_1_alt_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],

## END Breton Main Troops
["breton_messenger", "Breton Messenger", "Breton Messenger", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5, breton_face_young_1, breton_face_middle_2 ],
["breton_deserter", "Breton Deserter", "Breton Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, 
[], def_attrib|str_10|level(14), wp(80), knows_ironflesh_1|knows_power_draw_1, breton_face_young_1, breton_face_middle_2 ],
["breton_prison_guard", "Prison Guard", "Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,itm_a_corrazina_spina_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_2, breton_face_mature_1, breton_face_old_2 ],
["breton_castle_guard", "Dungeon Guard", "Dungeon Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_1_raised_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_2_raised_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_raised_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_martinus_kettlehat_3_raised_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,
 itm_a_churburg_13_asher_plain_custom,itm_a_corrazina_spina_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_red,itm_w_twohanded_war_axe_01_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_bardiche_5,itm_w_bardiche_5_red,itm_w_bardiche_9,itm_w_kriegshammer,itm_w_kriegshammer_alt,itm_w_kriegshammer_brown,itm_w_kriegshammer_alt_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,itm_w_glaive_6,itm_w_glaive_6_brown,
], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, breton_face_mature_1, breton_face_old_2 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC BANDIT TROOPS #########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### Routiers
["routier_knight", "Routier Knight", "Routier Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_outlaws, 
[
 itm_h_great_bascinet_english_1430_visor,itm_h_great_bascinet_english_1430_visor_open,itm_h_great_bascinet_continental_visor_a,itm_h_great_bascinet_continental_visor_a_open,itm_h_great_bascinet_continental_visor_b,itm_h_great_bascinet_continental_visor_b_open,itm_h_great_bascinet_continental_visor_c,itm_h_great_bascinet_continental_visor_c_open,itm_h_great_bascinet_continental_visor_c_strip,itm_h_great_bascinet_continental_visor_c_strip_open,itm_h_great_bascinet_continental_1430,itm_h_great_bascinet_continental_1430_visor,itm_h_great_bascinet_continental_1430_visor_open,
 itm_a_continental_plate_a,itm_a_continental_plate_b,itm_a_continental_plate_c,itm_a_padded_over_mail_4_custom,itm_a_padded_over_mail_5_custom,itm_a_corrazina_hohenaschau_custom,itm_a_churburg_13_asher_plain_custom,itm_a_brigandine_asher_plate_1_custom,itm_a_english_plate_1415_b,itm_a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_3,
 itm_b_leg_harness_5,itm_b_leg_harness_7,itm_b_leg_harness_9,itm_b_leg_harness_10,itm_b_leg_harness_english_1415,
 itm_g_gauntlets_mailed,itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_lance_colored_french_1_custom,itm_w_lance_colored_french_2_custom,itm_w_lance_colored_french_3_custom,
 itm_s_heater_shield_breton_2,itm_s_heater_shield_burgundian_1,itm_s_heater_shield_english_1,itm_s_heater_shield_french_4,itm_s_heraldic_shield_english_2,itm_s_heraldic_shield_english_7,itm_s_heraldic_shield_french_3,itm_s_heraldic_shield_german_2,
 itm_w_onehanded_falchion_b,itm_w_onehanded_sword_defiant,itm_w_onehanded_sword_knight,itm_w_onehanded_sword_forsaken,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_alt,itm_w_onehanded_knight_axe_01_brown,itm_w_onehanded_knight_axe_01_alt_brown,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_alt,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_alt,itm_w_knight_warhammer_2_brown,itm_w_knight_warhammer_2_alt_brown,itm_w_knight_winged_mace,
 itm_ho_horse_barded_blue,itm_ho_horse_barded_brown,itm_ho_horse_barded_green,itm_ho_horse_barded_white,
], 
level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, french_face_mature_1, french_face_old_2 ],
["routier_mounted_sergeant", "Routier Mounted Sergeant", "Routier Mounted Sergeants", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,itm_a_churburg_13_asher_plain_custom,itm_a_pistoia_kastenbrust_a_mail_sleeves_jackchain,itm_a_brigandine_asher_custom,itm_a_brigandine_asher_mail_custom,itm_a_padded_over_mail_heavy_1_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_4_custom, 
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_s_heater_shield_breton_4,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_english_6,itm_s_heater_shield_french_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_german_3,
 itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_squire,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,itm_w_lance_1,itm_w_lance_2,
 itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(20)|str_18|agi_18, wp_melee(150), knows_ironflesh_4|knows_power_strike_4|knows_shield_2|knows_athletics_4|knows_weapon_master_4|knows_riding_3, french_face_middle_1, french_face_mature_2 ],
["routier_sergeant", "Routier Sergeant", "Routier Sergeants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,
 itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,itm_a_churburg_13_asher_plain_custom,itm_a_pistoia_kastenbrust_a_mail_sleeves_jackchain,itm_a_brigandine_asher_custom,itm_a_brigandine_asher_mail_custom,itm_a_padded_over_mail_heavy_1_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_4_custom, 
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_s_heater_shield_breton_4,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_english_6,itm_s_heater_shield_french_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_german_3,
 itm_w_onehanded_sword_a_long,itm_w_onehanded_sword_c_long,itm_w_onehanded_sword_d_long,itm_w_onehanded_sword_poitiers,itm_w_onehanded_sword_squire,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,
], 
level(18)|str_15|agi_15, wpex(140,80,160,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],
["routier_voulgier", "Routier Voulgier", "Routier Voulgiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_brigandine_asher_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_demi_gauntlets,
 itm_w_glaive_3,itm_w_glaive_3_brown,itm_w_glaive_3_red,itm_w_glaive_5,itm_w_glaive_5_brown,itm_w_glaive_5_red,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["routier_footman", "Routier Footman", "Routier Footmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_chapel_de_fer_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,
 itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,itm_a_pistoia_mail_a_mail_sleeves_jackchains,itm_a_pistoia_mail_b_mail_sleeves_jackchains,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_g_leather_gauntlet,
 itm_w_spear_3,itm_w_spear_4,itm_w_spear_5,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_a,
 itm_s_heater_shield_breton_4,itm_s_heater_shield_burgundian_4,itm_s_heater_shield_english_6,itm_s_heater_shield_french_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_german_3,
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["routier_crossbowman", "Routier Crossbowman", "Routier Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_outlaws, 
[
 itm_h_skullcap_hood_custom,itm_h_cervelliere_hood_custom,itm_h_german_kettlehat_1_hood_custom,itm_h_german_kettlehat_3_hood_custom,itm_h_martinus_kettlehat_1_hood_custom,itm_h_martinus_kettlehat_2_hood_custom,itm_h_oliphant_kettlehat_hood_custom,itm_h_chapel_de_fer_hood_custom,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,itm_h_shingle_helmet_strap,
 itm_a_gambeson_crossbowman_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_sword_poitiers,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_goedendag, 
 itm_w_crossbow_medium,itm_w_bolt_triangular_large,
], 
level(12)|str_13|agi_12, wpex(100,80,80,80,120,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, french_face_young_1, french_face_middle_2 ],

### Flayers
["flayer_captain", "Flayer Captain", "Flayer Captains", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_outlaws, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_1_visor_1_mail_aventail,itm_h_bascinet_1_visor_1_open_mail_aventail,itm_h_bascinet_1_visor_2_mail_aventail,itm_h_bascinet_1_visor_2_open_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_2_visor_5_mail_aventail,itm_h_bascinet_2_visor_5_open_mail_aventail,itm_h_bascinet_2_visor_6_mail_aventail,itm_h_bascinet_2_visor_6_open_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_d,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_02,itm_w_knight_winged_mace,itm_w_knight_flanged_mace,
 itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3, 
], 
level(25)|str_20|agi_20, wp_melee(160), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, french_face_mature_1, french_face_old_2 ],
["flayer_infantry", "Flayer Infantry", "Flayer Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,
 itm_a_pistoia_mail_a_mail_sleeves_short,itm_a_pistoia_mail_b_mail_sleeves_short,itm_a_pistoia_mail_a_mail_sleeves,itm_a_pistoia_mail_b_mail_sleeves,itm_a_pistoia_mail_a_mail_sleeves_jackchains,itm_a_pistoia_mail_b_mail_sleeves_jackchains,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_falchion_a,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,itm_w_spear_5,itm_w_spear_6,itm_w_mace_winged,itm_w_mace_winged_brown,
 itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3, 
], 
level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],
["flayer_fauchard", "Flayer Fauchard", "Flayer Fauchards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_outlaws, 
[
 itm_h_eyeslot_kettlehat_1_mail_aventail,itm_h_eyeslot_kettlehat_2_mail_aventail,itm_h_eyeslot_kettlehat_3_mail_aventail,itm_h_oliphant_eyeslot_kettlehat_mail_aventail,itm_h_martinus_kettlehat_3_mail_aventail,itm_h_oliphant_kettlehat_mail_aventail,itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,
 itm_a_brigandine_asher_custom,itm_a_corrazina_hohenaschau_mail_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bardiche_1,itm_w_bardiche_1_brown,itm_w_bardiche_2,itm_w_bardiche_2_brown,itm_w_bardiche_4,itm_w_bardiche_4_brown,itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_brown,itm_w_great_hammer,itm_w_great_hammer_brown,itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["flayer_archer", "Flayer Archer", "Flayer Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_outlaws, 
[
 itm_h_skullcap_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,itm_b_high_boots_6,itm_b_high_boots_7,itm_g_leather_gauntlet,
 itm_w_dagger_baselard,itm_w_dagger_rondel,itm_w_onehanded_falchion_peasant,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_02_brown,itm_w_onehanded_war_axe_02_red,
 itm_w_war_bow_ash,itm_w_war_bow_elm,itm_w_arrow_triangular_large,itm_w_arrow_triangular_large,
], 
level(12)|str_12|agi_14, wpex(100,80,80,120,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],

### Retondeurs
["retondeur_horseman", "Retondeur Horseman", "Retondeur Horsemen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_makeshift_kettle_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_cervelliere_roundels_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail, 
 itm_a_padded_over_mail_heavy_1_custom,itm_a_padded_over_mail_heavy_2_custom,itm_a_padded_over_mail_heavy_3_custom,itm_a_padded_over_mail_heavy_4_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_3,
 itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_warhammer_1_red,itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_warhammer_2_red,itm_w_light_lance,
 itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3,
 itm_ho_sumpter_1,itm_ho_sumpter_2,itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,
], 
level(15)|str_16|agi_16, wp_melee(120), knows_ironflesh_3|knows_power_strike_3|knows_shield_1|knows_athletics_3|knows_weapon_master_3|knows_riding_2, mercenary_face_1, mercenary_face_2 ],
["retondeur_maceman", "Retondeur Maceman", "Retondeur Macemen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_martinus_kettlehat_1_mail_aventail,itm_h_martinus_kettlehat_2_mail_aventail,itm_h_chapel_de_fer_mail_aventail,itm_h_german_kettlehat_1_mail_aventail,itm_h_german_kettlehat_3_mail_aventail,itm_h_makeshift_kettle_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_cervelliere_roundels_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,
 itm_a_padded_over_mail_1_custom,itm_a_padded_over_mail_2_custom,itm_a_padded_over_mail_alt_1_custom,itm_a_padded_over_mail_alt_2_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_mace_winged,itm_w_mace_winged_brown,itm_w_mace_winged_red,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,
 itm_s_heraldic_shield_breton_1,itm_s_heraldic_shield_breton_2,itm_s_heraldic_shield_breton_3,itm_s_heraldic_shield_burgundian_1,itm_s_heraldic_shield_burgundian_2,itm_s_heraldic_shield_burgundian_3,
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, mercenary_face_1, mercenary_face_2 ],
["retondeur_crossbowman", "Retondeur Crossbowman", "Retondeur Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_outlaws, 
[
 itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,itm_h_makeshift_kettle_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,
 itm_a_padded_over_mail_3_custom,itm_a_padded_over_mail_alt_3_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_goedendag,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
 itm_w_crossbow_light,itm_w_bolt_triangular,
], 
level(12)|str_13|agi_12, wpex(100,80,80,80,100,80), knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_3|knows_weapon_master_1, mercenary_face_1, mercenary_face_2 ],

### Tard-Venus
["tard_venu_militia", "Tard-Venu Militia", "Tard-Venu Militias", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_outlaws, 
[
 itm_h_makeshift_kettle_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_shingle_helmet_strap,itm_h_rope_helmet_strap,itm_h_wicker_helmet_strap,
 itm_a_light_gambeson_long_sleeves_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_d,itm_w_spear_1,itm_w_spear_3,
 itm_s_heater_shield_breton_1,itm_s_heater_shield_breton_2,itm_s_heater_shield_breton_4,itm_s_heater_shield_burgundian_1,itm_s_heater_shield_burgundian_2,itm_s_heater_shield_burgundian_4,
], 
level(10)|str_12|agi_12, wpex(120,80,80,80,80,80), knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_athletics_3|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],
["tard_venu_pikeman", "Tard-Venu Pikeman", "Tard-Venu Pikemen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_outlaws, 
[
 itm_h_makeshift_kettle_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_shingle_helmet_strap,itm_h_rope_helmet_strap,itm_h_wicker_helmet_strap,
 itm_a_light_gambeson_long_sleeves_alt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_awlpike_1,itm_w_awlpike_2,itm_w_awlpike_3,
], 
level(10)|str_14|agi_10, wpex(100,100,120,100,100,100), knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],
["tard_venu_archer", "Tard-Venu Archer", "Tard-Venu Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_outlaws, 
[
 itm_h_wicker_helmet_strap,itm_h_rope_helmet_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_arming_cap,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,itm_a_light_gambeson_short_sleeves_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_dagger_quillon,itm_w_dagger_bollock,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,
 itm_w_short_bow_oak,itm_w_short_bow_yew,itm_w_arrow_triangular,
], 
level(8)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],

### Angry plebs
["disgruntled_farmer", "Disgruntled Farmer", "Disgruntled Farmers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_outlaws, 
[
 itm_h_straw_hat_1,itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_simple_coif,itm_h_arming_cap,itm_h_felt_hat_b_brown,itm_h_felt_hat_b_green,itm_h_hood_big_liripipe_full_custom,itm_h_hood_square_full_custom,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_dagger_quillon,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_wooden_stick,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,itm_w_fork_1,itm_w_fork_2,
], 
def_attrib, wp(60), knows_common_kham, swadian_face_young_1, swadian_face_old_2 ],
["furious_lumberjack", "Furious Lumberjack", "Furious Lumberjacks", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_outlaws, 
[
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_woolen_cap_brown,itm_h_woolen_cap_green,itm_h_simple_coif,itm_h_arming_cap,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_twohanded_war_axe_01,itm_w_twohanded_war_axe_01_brown,itm_w_twohanded_war_axe_01_red,
], 
def_attrib, wp(60), knows_common_kham, swadian_face_young_1, swadian_face_old_2 ],
["irrate_hunter", "Irrate Hunter", "Irrate Hunters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_outlaws, 
[
 itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,
 itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_dagger_quillon,
 itm_w_hunting_bow_ash,itm_w_hunting_bow_elm,
 itm_w_arrow_triangular,
], 
level(8)|str_10|agi_12, wpex(90,80,80,100,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, swadian_face_young_1, swadian_face_old_2 ],


### Assorted Bandits
["looter", "Looter", "Looters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_outlaws, 
[
 itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_arming_cap,itm_h_simple_coif,itm_h_wicker_helmet_strap,itm_h_skullcap_strap,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 (itm_w_dagger_quillon,imodbit_rusty),(itm_w_onehanded_sword_a,imod_rusty),itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_spiked_club,itm_w_spiked_club_dark,itm_w_fork_1,itm_w_fork_2,itm_w_fauchard_3,
], 
def_attrib, wp(20), knows_common_kham, bandit_face1, bandit_face2 ],
["bandit", "Bandit", "Bandits", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_outlaws, 
[
 itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_arming_cap,itm_h_simple_coif,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 (itm_w_dagger_quillon,imodbit_rusty),(itm_w_onehanded_sword_a,imod_rusty),itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_spiked_club,itm_w_spiked_club_dark,itm_w_fork_1,itm_w_fork_2,itm_w_fauchard_3,
], 
def_attrib, wp(60), knows_warrior_basic, bandit_face1, bandit_face2 ],
["brigand", "Brigand", "Brigands", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac_outlaws, 
[
 itm_h_hood_square_full_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_big_liripipe_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_arming_cap,itm_h_simple_coif,
 itm_a_peasant_cote_custom,itm_a_peasant_cotehardie_custom,itm_a_hunter_coat_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_3,
 (itm_w_dagger_quillon,imodbit_rusty),(itm_w_onehanded_sword_a,imod_rusty),itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_spiked_club,itm_w_spiked_club_dark,itm_w_fork_1,itm_w_fork_2,itm_w_fauchard_3,
], 
def_attrib, wp(90), knows_warrior_basic, bandit_face1, bandit_face2 ],

["manhunter", "Manhunter", "Manhunters", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_manhunters, 
[], 
def_attrib, wp(50), knows_warrior_basic, bandit_face1, bandit_face2 ],


## Slave Driver
["slave_driver", "Slave Driver", "Slave Drivers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_slavers, 
[], def_attrib, wp(80), knows_warrior_normal, bandit_face1, bandit_face2 ],
["slave_hunter", "Slave Hunter", "Slave Hunters", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_slavers, 
[], def_attrib, wp(90), knows_warrior_normal, bandit_face1, bandit_face2 ],
["slave_crusher", "Slave Crusher", "Slave Crushers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_slavers, 
[], def_attrib, wp(110), knows_warrior_veteran, bandit_face1, bandit_face2 ],
["slaver_chief", "Slaver Chief", "Slaver Chiefs", tf_guarantee_all_wo_ranged|tf_mounted, no_scene, reserved, fac_slavers, 
[], def_attrib3, wp(130), knows_warrior_veteran, bandit_face1, bandit_face2 ],

# ["follower_woman", "Apprenti combattant", "Apprenti combattants", tf_female|tf_guarantee_armor, no_scene, reserved, fac_commoners, [], def_attrib, wp(70), knows_common_kham, 0x00000000140453c5275949b75566b56600000000001dc2da0000000000000000, man_face_young_2 ],
# ["hunter_woman", "deffenseur", "deffenseurs", tf_female|tf_guarantee_armor, no_scene, reserved, fac_commoners, [], def_attrib, wp(85), knows_warrior_basic, 0x000000003f04d14536db6db6db6db6db00000000000db6db0000000000000000, man_face_young_2 ],
# ["fighter_woman", "Vengeur", "Vengeurs", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [], def_attrib, wp(100), knows_warrior_basic2, 0x000000003f0404c5275949b75566356600000000001dc2da0000000000000000, man_face_young_2 ],
["sword_sister", "Female Warrior", "Female Warriors", tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, 
[], def_attrib, wp(140), knows_warrior_normal, 0x000000003f0414c5275949b75566356600000000001dc2da0000000000000000, man_face_young_2 ],


["refugee", "Refugee", "Refugees", tf_female|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_straw_hat,itm_a_farmer_tunic,itm_b_turnshoes_2,itm_a_commoner_apron,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_tunic,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_b_green,itm_h_felt_hat_b_brown,itm_w_spiked_club,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_03,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fork_1,itm_w_fork_2,itm_w_scythe_1], def_attrib|level(1), wp(45), knows_common, woman_face_1, woman_face_2 ],
["peasant_woman", "Peasant Woman", "Peasant Women", tf_female|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_straw_hat,itm_a_farmer_tunic,itm_b_turnshoes_2,itm_a_commoner_apron,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_tunic,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_b_green,itm_h_felt_hat_b_brown,itm_w_spiked_club,itm_w_onehanded_war_axe_02,itm_w_onehanded_war_axe_03,itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fork_1,itm_w_fork_2,itm_w_scythe_1], def_attrib|level(1), wp(40), knows_common, 0x0000000028043003475c7249aab12d1d002395288a463cdb0000000000000000 ],


["caravan_master", "Caravan Master", "Caravan Masters", tf_mounted|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac_commoners, 
[itm_h_highlander_beret_red_2,itm_a_merchant_outfit,itm_b_high_boots_1,itm_g_leather_gauntlet,itm_w_dagger_italian,itm_ho_courser_1], def_attrib|level(9), wp(100), knows_common|knows_riding_4|knows_ironflesh_3|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

["kidnapped_girl", "Kidnapped Girl", "Kidnapped Girls", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners, 
[itm_a_woman_common_dress_2_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, woman_face_1, woman_face_2 ],


#This troop is the troop marked as soldiers_end and town_walkers_begin
["town_walker_1", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_hood_custom,itm_h_felt_hat_b_black,itm_h_felt_hat_b_blue,itm_h_felt_hat_b_brown,itm_h_felt_hat_b_green,itm_h_felt_hat_b_red,itm_h_felt_hat_b_white,itm_h_felt_hat_b_yellow,itm_h_felt_hat_black,itm_h_felt_hat_blue,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_red,itm_h_felt_hat_white,itm_h_felt_hat_yellow,itm_h_straw_hat,itm_h_woolen_cap_black,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_green,itm_h_woolen_cap_red,itm_h_woolen_cap_white,itm_h_woolen_cap_yellow,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_cote_custom,itm_a_tavern_keeper_shirt,itm_a_noble_shirt_black,itm_a_noble_shirt_blue,itm_a_noble_shirt_brown,itm_a_noble_shirt_green,itm_a_noble_shirt_red,itm_b_high_boots_1,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,], def_attrib|level(4), wp(60), knows_common, 0x000000003f04018556db6d35244636db00000000001db69b0000000000000000, man_face_old_2 ],
["town_walker_2", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_court_wimple_1,itm_h_court_wimple_2,itm_h_court_lady_hood,itm_a_woman_common_dress_1_custom,itm_a_woman_common_dress_2_custom,itm_b_turnshoes_2,itm_b_turnshoes_1], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
["khergit_townsman", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_woolen_cap_black,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_green,itm_h_woolen_cap_red,itm_h_woolen_cap_white,itm_h_woolen_cap_yellow,itm_h_felt_hat_b_black,itm_h_felt_hat_b_blue,itm_h_felt_hat_b_brown,itm_h_felt_hat_b_green,itm_h_felt_hat_b_red,itm_h_felt_hat_b_white,itm_h_felt_hat_b_yellow,itm_h_felt_hat_black,itm_h_felt_hat_blue,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_red,itm_h_felt_hat_white,itm_h_felt_hat_yellow,itm_h_highlander_beret_black,itm_h_highlander_beret_blue,itm_h_highlander_beret_brown,itm_h_highlander_beret_green,itm_h_highlander_beret_red,itm_h_highlander_beret_white,itm_h_highlander_beret_yellow,itm_a_peasant_man_custom,itm_a_peasant_coat,itm_a_peasant_cote_custom,itm_a_peasant_cote_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_noble_shirt_black,itm_a_noble_shirt_blue,itm_a_noble_shirt_green,itm_a_noble_shirt_red,itm_a_noble_shirt_white,itm_a_noble_shirt_green,itm_b_turnshoes_1,itm_b_turnshoes_2], def_attrib|level(4), wp(60), knows_common, 0x000000003f04118756db6d35244636db00000000001db69b0000000000000000, 0x000000002404230d56db6d35244636db00000000001db69b0000000000000000 ],
["khergit_townswoman", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_court_wimple_1,itm_h_court_wimple_2,itm_h_court_lady_hood,itm_a_woman_common_dress_1_custom,itm_a_woman_common_dress_2_custom,itm_b_turnshoes_2,itm_b_turnshoes_1], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
["sarranid_townsman", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_woolen_cap_black,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_green,itm_h_woolen_cap_red,itm_h_woolen_cap_white,itm_h_woolen_cap_yellow,itm_h_felt_hat_b_black,itm_h_felt_hat_b_blue,itm_h_felt_hat_b_brown,itm_h_felt_hat_b_green,itm_h_felt_hat_b_red,itm_h_felt_hat_b_white,itm_h_felt_hat_b_yellow,itm_h_felt_hat_black,itm_h_felt_hat_blue,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_red,itm_h_felt_hat_white,itm_h_felt_hat_yellow,itm_h_highlander_beret_black,itm_h_highlander_beret_blue,itm_h_highlander_beret_brown,itm_h_highlander_beret_green,itm_h_highlander_beret_red,itm_h_highlander_beret_white,itm_h_highlander_beret_yellow,itm_a_peasant_man_custom,itm_a_peasant_coat,itm_a_peasant_cote_custom,itm_a_peasant_cote_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_noble_shirt_black,itm_a_noble_shirt_blue,itm_a_noble_shirt_green,itm_a_noble_shirt_red,itm_a_noble_shirt_white,itm_a_noble_shirt_green,itm_b_turnshoes_1,itm_b_turnshoes_2], def_attrib|level(4), wp(60), knows_common, swadian_face_younger_1, swadian_face_middle_2 ],
["sarranid_townswoman", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_court_wimple_1,itm_h_court_wimple_2,itm_h_court_lady_hood,itm_a_woman_common_dress_1_custom,itm_a_woman_common_dress_2_custom,itm_b_turnshoes_2,itm_b_turnshoes_1], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],

#This troop is the troop marked as town_walkers_end and village_walkers_begin
["village_walker_1", "Villager", "Villagers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_hood_custom,itm_h_felt_hat_b_black,itm_h_felt_hat_b_blue,itm_h_felt_hat_b_brown,itm_h_felt_hat_b_green,itm_h_felt_hat_b_red,itm_h_felt_hat_b_white,itm_h_felt_hat_b_yellow,itm_h_felt_hat_black,itm_h_felt_hat_blue,itm_h_felt_hat_brown,itm_h_felt_hat_green,itm_h_felt_hat_red,itm_h_felt_hat_white,itm_h_felt_hat_yellow,itm_h_straw_hat,itm_h_woolen_cap_black,itm_h_woolen_cap_blue,itm_h_woolen_cap_brown,itm_h_woolen_cap_green,itm_h_woolen_cap_red,itm_h_woolen_cap_white,itm_h_woolen_cap_yellow,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_cote_custom,itm_a_peasant_cote_custom,itm_a_tavern_keeper_shirt,itm_a_noble_shirt_black,itm_a_noble_shirt_blue,itm_a_noble_shirt_brown,itm_a_noble_shirt_green,itm_a_noble_shirt_red,itm_b_high_boots_1,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom,itm_a_peasant_man_custom], def_attrib|level(4), wp(60), knows_common, man_face_younger_1, man_face_older_2 ],
["village_walker_2", "Villager", "Villagers", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, 
[itm_h_court_wimple_1,itm_h_court_wimple_2,itm_h_court_lady_hood,itm_a_woman_common_dress_1_custom,itm_a_woman_common_dress_2_custom,itm_b_turnshoes_2,itm_b_turnshoes_1], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
["spy_walker_1", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, 
[itm_h_hood_custom,itm_a_leather_jerkin,itm_b_turnshoes_1], def_attrib|level(4), wp(60), knows_common, man_face_middle_1, man_face_old_2 ],
["spy_walker_2", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, 
[itm_h_hood_black,itm_a_leather_jerkin,itm_b_turnshoes_1], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
["tournament_master", "Tournament Master", "Tournament Master", tf_hero, scn_zendar_center|entry(1), reserved, fac_commoners, [], def_attrib|level(2), wp(20), knows_common, 0x000000002404530f56db6d35244636db00000000001db69b0000000000000000 ],
["trainer", "Trainer", "Trainer", tf_hero, scn_zendar_center|entry(2), reserved, fac_commoners, [], def_attrib|level(2), wp(20), knows_common, 0x0000000a240473cf56db6d35244636db00000000001db69b0000000000000000 ],
["Constable_Hareck", "Constable Hareck", "Constable Hareck", tf_hero, scn_zendar_center|entry(5), reserved, fac_commoners, [], def_attrib|level(5), wp(20), knows_common, 0x000000002404844f56db6d35244636db00000000001db69b0000000000000000 ],

# Ryan BEGIN
["Ramun_the_slave_trader", "Ramun, the slave trader", "Ramun, the slave trader", tf_hero, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, 0x000000002404a59056db6d35244636db00000000001db69b0000000000000000 ],

["guide", "Quick Jimmy", "Quick Jimmy", tf_hero, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000002404b59056db6d35244636db00000000001db69b0000000000000000 ],
# Ryan END

["Xerina", "Xerina", "Xerina", tf_female|tf_hero, scn_the_happy_boar|entry(5), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|str_15|agi_30|level(39), wp(312), knows_power_strike_5|knows_ironflesh_10|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_10, 0x0000000023102007408b49f95b48bb8c0000000000199ccb0000000000000000 ],
["Dranton", "Dranton", "Dranton", tf_hero, scn_the_happy_boar|entry(2), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|str_25|agi_20|level(42), wp(324), knows_power_strike_5|knows_ironflesh_10|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_10, 0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000 ],
["Kradus", "Kradus", "Kradus", tf_hero, scn_the_happy_boar|entry(3), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|str_30|agi_17|level(43), wp(270), knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3, 0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000 ],


#Tutorial
["tutorial_trainer", "Training Ground Master", "Training Ground Master", tf_hero, no_scene, reserved, fac_commoners, [], def_attrib|level(2), wp(20), knows_common, 0x000000003604c00f56db6d35244636db00000000001db69b0000000000000000 ],
["tutorial_student_1", "{!}tutorial_student_1", "{!}tutorial_student_1", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral, [], def_attrib|level(2), wp(20), knows_common, swadian_face_young_1, swadian_face_old_2 ],
["tutorial_student_2", "{!}tutorial_student_2", "{!}tutorial_student_2", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral, [], def_attrib|level(2), wp(20), knows_common, swadian_face_young_1, swadian_face_old_2 ],
["tutorial_student_3", "{!}tutorial_student_3", "{!}tutorial_student_3", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral, [], def_attrib|level(2), wp(20), knows_common, swadian_face_young_1, swadian_face_old_2 ],
["tutorial_student_4", "{!}tutorial_student_4", "{!}tutorial_student_4", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral, [], def_attrib|level(2), wp(20), knows_common, swadian_face_young_1, swadian_face_old_2 ],

#Salt mine
["Galeas", "Galeas", "Galeas", tf_hero, no_scene, reserved, fac_commoners, [], def_attrib|level(5), wp(20), knows_common, 0x000000003604d04f56db6d35244636db00000000001db69b0000000000000000 ],

#Dhorak keep

["farmer_from_bandit_village", "Farmer", "Farmers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_a_farmer_tunic,itm_b_turnshoes_2,itm_h_straw_hat], def_attrib|level(4), wp(60), knows_common, 0x000000003604004f56db6d35244636db00000000001db69b0000000000000000, man_face_older_2 ],

# Trainers
["trainer_1", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_1|entry(6), reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003604104f56db6d35244636db00000000001db69b0000000000000000 ],
["trainer_2", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_2|entry(6), reserved, fac_commoners, [itm_a_simple_gambeson_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000360420c956db6d35244636db00000000001db69b0000000000000000 ],
["trainer_3", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_3|entry(6), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003604818056db6e35244636db00000000001db69b0000000000000000 ],
["trainer_4", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_4|entry(6), reserved, fac_commoners, [itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000057604535356db6e35244636db00000000001db69b0000000000000000 ],
["trainer_5", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_5|entry(6), reserved, fac_commoners, [itm_h_cervelliere_mail_aventail,itm_a_light_gambeson_long_sleeves_custom,itm_b_high_boots_2], def_attrib|level(2), wp(20), knows_common, 0x000000037604839356db6e35244636db00000000001db69b0000000000000000 ],

# Ransom brokers.
["ransom_broker_1", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_2", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_3", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_blue,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_4", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_5", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_simple_gambeson_custom,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_noble_shirt_red,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_hunter_coat_custom,itm_b_turnshoes_1],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_11", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_12", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_13", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_blue,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_14", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_15", "Ransom_Broker", "Ransom_Broker", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["ransom_broker_16","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_simple_gambeson_custom,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_17","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_18","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
# ["ransom_broker_19","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_noble_shirt_red,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
# ["ransom_broker_20","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_a_hunter_coat_custom,itm_b_turnshoes_1],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
["tavern_traveler_1", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_2", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_3", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_hood_black,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_4", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_monk_robe_black,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_5", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_simple_gambeson_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_6", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_simple_coif,itm_a_light_gambeson_long_sleeves_custom,itm_b_high_boots_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_7", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_woolen_cap_brown,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_8", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_9", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_traveler_10", "Traveller", "Traveller", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_black,itm_h_highlander_beret_black_2,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],


# Tavern traveler.
["tavern_bookseller_1", "Book_Merchant", "Book_Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_1,itm_book_persuasion,itm_book_intelligence,itm_book_trade,itm_book_wound_treatment_reference,itm_book_surgery_reference,itm_a_surgeon_dress], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_bookseller_2", "Book_Merchant", "Book_Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_1,itm_book_tactics,itm_book_leadership,itm_book_weapon_mastery,itm_book_engineering,itm_book_training_reference], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],


# Tavern minstrel.
["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_h_highlander_beret_red_2,itm_a_noble_shirt_red, itm_b_high_boots_1, itm_lute, itm_dedal_lutnia],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_a_tabard, itm_b_turnshoes_2, itm_lyre, itm_dedal_lira],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_3","Wandering Musician","Musician",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_a_tabard, itm_b_turnshoes_2, itm_lute, itm_dedal_lutnia],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_4","Wandering Poet","Poet",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_a_tabard, itm_b_turnshoes_1, itm_lyre, itm_dedal_lira],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_5","Wandering Troubadour","Troubadour",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_h_highlander_beret_green_2,itm_a_noble_shirt_green, itm_b_turnshoes_1, itm_lute, itm_dedal_lutnia],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

#dedal
["musican_male","Musician","Musician",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_a_tabard,itm_b_turnshoes_2, itm_lute, itm_dedal_lutnia],def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2,itm_dedal_lutnia],
["musican_female","Musician","Musician",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_a_woman_common_dress_1_custom,itm_a_woman_common_dress_2_custom,itm_b_turnshoes_2,itm_h_court_wimple_1,itm_h_court_wimple_2, itm_dedal_lutnia],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["musicans_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],

["tavern_tailor_1", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_1,itm_a_surgeon_dress], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_2", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_black,itm_b_turnshoes_1,itm_h_leather_hat_d_black], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_3", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_4", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_5", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_leather_hat_c,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_6", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_leather_hat_b,itm_a_noble_shirt_blue,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_7", "Travelling Tailor", "Travelling Tailor", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_red,itm_a_noble_shirt_red,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_common, merchant_face_1, merchant_face_2 ],
["tavern_tailor_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],

#NPC system changes begin
#Companions
["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

#DAC - Replacement Companions Placeholders

#William Reynes english longbowman mounted archer/scout
["npc1", "William Reynes", "William Reynes", tf_hero|tf_mounted, no_scene, reserved, fac_kingdom_2,
[
 itm_h_skullcap_strap,itm_a_aketon_asher_dagged_red_1,itm_b_low_boots_1,itm_w_long_bow_ash,itm_w_arrow_triangular,itm_w_onehanded_sword_poitiers,
]
,level(18)|str_14|agi_16|int_8|cha_10,wpex(120,80,80,180,80,80),knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2|knows_riding_3,0x0000000500009004450d65aa627948d500000000001d44e50000000000000000],

# Frans Demaar Marchand Flamand de Bruges
["npc2", "Frans Demaar", "Frans Demaar", tf_hero, no_scene, reserved, fac_kingdom_3,
[
 itm_h_highlander_beret_red_2,itm_a_houpelande_decorated_a_3,itm_b_poulaines_lined_1,itm_w_dagger_italian,
]
,str_12|agi_9|int_6|cha_6|level(6),wp(100),knows_warrior_npc|knows_riding_3|knows_weapon_master_1|knows_ironflesh_1|knows_power_strike_2|knows_athletics_2|knows_tactics_1|knows_leadership_1,0x00000007c00064d131948255aa95a51a00000000001db6db0000000000000000],

#Morgane Lann guérisseuse herboriste/marchande bretonne
["npc3", "Morgane Lann", "Morgane Lann", tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_4,
[
 itm_a_woman_common_dress_1_custom,itm_b_turnshoes_2,itm_w_dagger_quillon,
]
,str_9|agi_9|int_12|cha_6|level(6),wp(70),knows_warrior_npc|knows_power_strike_1|knows_tactics_4|knows_first_aid_2|knows_athletics_1|knows_riding_2,0x00000004790c400147156b33ed29e3620000000000114b1b0000000000000000],

# Jean, bâtard du Guesclin Ecuyer/contrebandier/marchand à cheval/scout
["npc4", "Jean", "Jean", tf_hero, no_scene, reserved, fac_kingdom_4,
[
 itm_h_bascinet_3_mail_aventail,itm_a_pistoia_mail_b_mail_sleeves_jackchains,itm_b_high_boots_2,itm_w_onehanded_sword_squire,itm_w_light_lance,itm_ho_courser_1,itm_s_heraldic_shield_french_1,
]
,str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,0x000000043f0030045edb6dc59b4e5cd500000000001db6db0000000000000000],

# Josserand de Reulle (bourguignon) arbalétrier à cheval/Scout
["npc5", "Josserand de Reulle", "Josserand de Reulle", tf_hero, no_scene, reserved, fac_kingdom_3,
[
 itm_h_german_kettlehat_4_strap,itm_a_gambeson_asher_belt_custom,itm_b_high_boots_3,itm_ho_courser_6,itm_w_crossbow_light,itm_w_bolt_triangular,itm_w_onehanded_sword_a_long,
]
,str_9|agi_9|int_12|cha_7|level(5),wp(90),knows_warrior_npc|knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1|knows_trade_5,0x000000041410404057604acb2665bb2300000000001dc4dd0000000000000000],

#Louis le Barbier Chirurgien Bourguignon Dijon
["npc6", "Louis le Barbier", "Louis le Barbier", tf_hero, no_scene, reserved, fac_kingdom_3,
[
 itm_h_simple_coif,itm_a_surgeon_dress,itm_b_low_boots_2,itm_w_dagger_quillon,
]
,str_8|agi_7|int_13|cha_7|level(4),wp(30),knows_merchant_npc|knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,0x0000000fff089006389e52b7526d16f300000000001e92a20000000000000000],

#Diane du Bois rebelle française archère
["npc7", "Diane du Bois", "Diane du Bois", tf_hero|tf_female, no_scene, reserved, fac_kingdom_1,
[
 itm_a_leather_jerkin,itm_b_turnshoes_3,itm_h_hood_big_liripipe_full_custom,itm_w_hunting_bow_yew,itm_w_archer_hatchet_brown,itm_w_arrow_triangular_large,
]
,str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|knows_tracking_4|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2|knows_tracking_2,0x000000038308500736ed712323523ad300000000001cd2ec0000000000000000],

#Baudouin de Limoges marchand
["npc8", "Baudouin de Limoges", "Baudouin de Limoges", tf_hero, no_scene, reserved, fac_kingdom_1,
[
 itm_b_poulaines_9,itm_a_merchant_outfit,itm_h_highlander_beret_brown,itm_w_dagger_italian,
]
,str_17|agi_10|int_9|cha_10|level(9),wp(100),knows_warrior_npc|knows_weapon_master_3|knows_power_strike_2|knows_leadership_1|knows_athletics_4,0x0000000a400cb50b374346d654cdaa5d00000000001ebb140000000000000000],

#Philippe de Culant jeune noble Français écuyer 0rleans en 1429
["npc9", "Philippe de Culant", "Philippe de Culant", tf_hero, no_scene, reserved, fac_kingdom_1,
[
 itm_h_sallet_strap,itm_b_high_boots_2,itm_a_padded_over_mail_heavy_1_custom,itm_w_bastard_sword_a,itm_w_lance_1,itm_ho_courser_5,itm_s_heraldic_shield_leather,
]
,str_12|agi_12|int_7|cha_8|level(7),wp(100),knows_warrior_npc|knows_weapon_master_2|knows_riding_4|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_2,0x000000002208b00558d46a4cac6abab300000000001d38ca0000000000000000],

#Frère Hardouin du Puy Moine guérisseur
["npc10", "Frère Hardouin du Puy", "Frère Hardouin du Puy", tf_hero, no_scene, reserved, fac_kingdom_1,
[
 itm_a_priest_robe,itm_w_wooden_stick,
]
,str_12|agi_8|int_9|cha_11|level(9),wp(105),knows_warrior_npc|knows_weapon_master_3|knows_tactics_2|knows_leadership_1|knows_ironflesh_3|knows_trainer_3|knows_riding_2,0x000000097b10100a195c715a96a958aa00000000001dc8940000000000000000],

#Marguerite du Four Cuisinière/Marchande
["npc11", "Marguerite du Four", "Marguerite du Four", tf_hero|tf_female, no_scene, reserved, fac_kingdom_1,[
 itm_a_woman_common_dress_2_custom,itm_b_poulaines_2,itm_w_archers_maul_brown,
],str_8|agi_11|int_10|cha_10|level(8),wp(70),knows_merchant_npc|knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,0x00000003981030061c2372c0db46169300000000001da4990000000000000000],

#Michele Guistella Chirurgien Italien
["npc12", "Michele Guistella", "Michele Guistella", tf_hero, no_scene, reserved, fac_commoners,
[
 itm_a_tailored_cotehardie_custom,itm_b_poulaines_9,itm_w_dagger_italian,
]
,str_8|agi_7|int_13|cha_7|level(5),wp(70),knows_merchant_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_4|knows_inventory_management_3|knows_first_aid_3|knows_wound_treatment_2,0x00000000c400348b174a84c2db53331200000000001f34dc0000000000000000],

#Thomas Gower mounted squire mant at arms (Falaise)
["npc13", "Thomas Gower", "Thomas Gower", tf_hero, no_scene, reserved, fac_kingdom_2,
[
 itm_h_bascinet_1_mail_aventail,itm_a_brigandine_asher_a_custom,itm_b_leg_harness_1,itm_w_lance_2,itm_w_mace_english,itm_ho_courser_7,itm_s_heater_shield_english_1,
]
,str_9|agi_8|int_12|cha_8|level(3),wp(90),knows_warrior_npc|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,0x00000000f604018437534e375c98cb0a00000000001db2e30000000000000000],

#John Crichton noble écossais soldat veteran
["npc14", "John Crichton", "John Crichton", tf_hero, no_scene, reserved, fac_commoners,
[
 itm_h_eyeslot_kettlehat_1_mail_aventail,itm_a_pistoia_breastplate_half_mail_sleeves_jackchain,itm_b_leg_harness_3,itm_w_bardiche_4_brown,
]
,str_12|agi_10|int_9|cha_8|level(9),wp(100),knows_warrior_npc|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1|knows_inventory_management_3|knows_tactics_2|knows_ironflesh_3|knows_trainer_2,0x00000000d808a30746eb6e392ad23b9300000000001d4ae30000000000000000],

#Gaspard Bureau bourgeois Français de Paris Ingénieur
["npc15", "Gaspard Bureau", "Gaspard Bureau", tf_hero, no_scene, reserved, fac_kingdom_1,
[
 itm_a_tabard,itm_b_turnshoes_6,itm_w_dagger_pikeman,
]
,str_9|agi_9|int_12|cha_8|level(7),wp(40),knows_warrior_npc|knows_surgery_4|knows_trade_3|knows_spotting_1|knows_engineer_3|knows_tactics_1,0x00000000ca0824055ae399e91e6f47de00000000001e02e30000000000000000],

# Frère Martin d'Autun Moine Guérisseur
["npc16", "Frère Martin d'Autun", "Frère Martin d'Autun", tf_hero, no_scene, reserved, fac_kingdom_3,
[
 itm_a_monk_robe_brown,itm_b_turnshoes_1,
]
,str_7|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|knows_power_throw_3|knows_athletics_2|knows_power_strike_1|knows_surgery_8,0x00000000000040060558b239244d94d100000000001d98e30000000000000000],

#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
["kingdom_1_lord", "Charles_VII, Regent of France, le Dauphin", "Charles_VII", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_a_nobleman_court_outfit_custom,itm_b_turnshoes_1,itm_s_heraldic_shield_bouche,itm_w_bastard_sword_regent], king_attrib, wp(420), king_skills, 0x00000002fb1030055726767eab4d555c00000000001d34e50000000000000000, 0 ],

["kingdom_2_lord", "John_of_Lancaster, Duke of Bedford", "John_of_Lancaster", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_ho_horse_barded_red_chamfrom,itm_w_pollaxe_cut_04_english_ebony,itm_w_lance_colored_english_1,itm_h_great_bascinet_english_1430_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_10,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_nobleman_court_outfit_custom,itm_s_heraldic_shield_metal,(itm_w_bastard_sword_english, imodbit_masterwork),], king_attrib, wp(420), king_skills, 
0x00000006e910300c7774776e532d2cea00000000001dc6db0000000000000000, 0 ],

["kingdom_3_lord", "Philippe the Good, Duke of Burgundy", "Philippe the Good", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_ho_horse_barded_brown_chamfrom,itm_w_lance_3,itm_h_great_bascinet_english_1410_visor,itm_g_gauntlets_gilded_segmented_a,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_nobleman_court_outfit_custom,itm_s_heraldic_shield_bouche,itm_w_bastard_sword_duke], king_attrib, wp(420), king_skills, 0x00000004f810b0024caa6dd4fa90d6a200000000001c331a0000000000000000, 0 ],

["kingdom_4_lord", "Jean V de Montfort, Duke of Brittany", "Jean V de Montfort", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_ho_horse_barded_black_chamfrom,itm_w_lance_4,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_nobleman_court_outfit_custom,itm_s_heraldic_shield_metal,itm_w_bastard_sword_sempach], king_attrib, wp(420), king_skills, 0x00000007bb10b34b5b1b55077970594900000000001db7660000000000000000, 0 ],
# ["kingdom_5_lord",  "King Graveth",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_tabard,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_heraldic_mail_with_tabard,  itm_gauntlets,         itm_bastard_sword_b,         itm_s_heraldic_shield_metal,        itm_spiked_helmet],         knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
# ["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_warhorse_sarranid,     itm_mamluke_mail,          itm_sarranid_boots_c,       itm_sarranid_mail_coif,  itm_mail_mittens,      itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC FRENCH LORDS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["knight_1_1", "Jean II d'Alençon, Duc d'Alençon", "Jean d'Alençon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000002110c00b555b95c4a36ec68c00000000001e464c0000000000000000, 0x000000002110c00b555b95c4a36ec68c00000000001e464c0000000000000000 ],
["knight_1_2", "Étienne de Vignolles, Seigneur de Vignolles", "La Hire", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x000000003f10238364ec7b3afb2db76400000000001db6d30000000000000000, 0x000000003f10238364ec7b3afb2db76400000000001db6d30000000000000000 ],
["knight_1_3", "Gilles de Rais, Baron de Rais", "Gilles de Rais", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_a_tabard,itm_h_pigface_klappvisor_open,itm_b_leg_harness_10,itm_g_finger_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x00000001ff10110b456d8a875a69c6d300000000001e25220000000000000000, 0x00000001ff10110b456d8a875a69c6d300000000001e25220000000000000000 ],
["knight_1_4", "Charles II d'Albret, Sire d'Albret, Vicomte de Tartas", "Charles d'Albret", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x000000017404b00528cb772ae471a72300000000001db4db0000000000000000, 0x000000017404b00528cb772ae471a72300000000001db4db0000000000000000 ],
["knight_1_5", "Jeanne, La Pucelle d'Orléans", "Jeanne d'Arc", tf_hero|tf_female, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_white_chamfrom,itm_a_plate_joan,itm_h_great_bascinet_english_1410_visor,itm_g_gauntlets_segmented_b,itm_b_leg_harness_9,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000002d04000647136cc31b732a53003b0c98db6c45f10000000000000000, 0x000000002d04000647136cc31b732a53003b0c98db6c45f10000000000000000 ],
["knight_1_6", "Jean Poton de Xaintrailles, Seigneur de Xaintrailles", "Jean Poton de Xaintrailles", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x000000016904948164deb23b6b6d4adb00000000001da56c0000000000000000, 0x000000016904948164deb23b6b6d4adb00000000001da56c0000000000000000 ],
["knight_1_7", "Louis d'Amboise, Vicomte de Thouars", "Louis d'Amboise", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_sempach], lord_attrib, wp(380), knows_lord_1, 0x0000000616086004151c7ad66d6da8e300000000001d36d50000000000000000, 0x0000000616086004151c7ad66d6da8e300000000001d36d50000000000000000 ],
["knight_1_8", "Pierre d'Amboise, Seigneur de Chaumont", "Pierre d'Amboise", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000003508100b471a7ad66d6da8e300000000001d36dd0000000000000000, 0x000000003508100b471a7ad66d6da8e300000000001d36dd0000000000000000 ],
["knight_1_9", "Jean d'Orléans, Comte de Mortain, de Perigord et de Gien", "Jean d'Orléans", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x000000003508100d371a75586d6daacd00000000001d24d10000000000000000, 0x000000003508100d371a75586d6daacd00000000001d24d10000000000000000 ],
["knight_1_10", "Jean V de Bueil, Seigneur de Bueil", "Jean de Bueil", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x000000003f10000564db7ab09b6d3cd900000000001d32dd0000000000000000, 0x000000003f10000564db7ab09b6d3cd900000000001d32dd0000000000000000 ],

["knight_1_11", "Louis de Culant, Baron de Culant", "Louis de Culant", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x0000000fff10c00b5b6392db5d68badd00000000001d152d0000000000000000, 0x0000000fff10c00b5b6392db5d68badd00000000001d152d0000000000000000 ],
["knight_1_12", "Charles de Culant, Seigneur de la Crête", "Charles de Culant", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x000000013f10c00437a391cb5c71b6dd00000000001d951d0000000000000000, 0x000000013f10c00437a391cb5c71b6dd00000000001d951d0000000000000000 ],
["knight_1_13", "Raymond de Villars, Sénéchal de Beaucaire et de Nîmes", "Raymond de Villars", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000006cb1054d1591ba8a56449a8e600000000001d132a0000000000000000, 0x00000006cb1054d1591ba8a56449a8e600000000001d132a0000000000000000 ],
["knight_1_14", "Raoul VI de Gaucourt, Seigneur de Gaucourt", "Raoul de Gaucourt", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x0000000d01102011365b75ab1ba9a46500000000001dc48d0000000000000000, 0x0000000d01102011365b75ab1ba9a46500000000001dc48d0000000000000000 ],
["knight_1_15", "Jean de Brosse, Seigneur de Boussac", "Jean de Brosse", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_tabard,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x00000009ff10124b472c91c92371d75c00000000001ca48b0000000000000000, 0x00000009ff10124b472c91c92371d75c00000000001ca48b0000000000000000 ],
["knight_1_16", "Charles I de Bourbon, Duc de Bourbon et d'Auvergne", "Charles I de Bourbon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_sempach], lord_attrib, wp(380), knows_lord_1, 0x000000043f10800156e6d963b479c69c00000000001d268c0000000000000000, 0x000000043f10800156e6d963b479c69c00000000001d268c0000000000000000 ],
["knight_1_17", "Louis I de Bourbon, Comte de Clermont et de Sancerre", "Louis I de Bourbon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x000000006d10600422dd7143b479c69c00000000001d24890000000000000000, 0x000000006d10600422dd7143b479c69c00000000001d24890000000000000000 ],
["knight_1_18", "Arnault Guilhem de Barbazan, Seigneur de Barbazan", "Arnault Guilhem de Barbazan", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_s_heraldic_shield_metal,itm_w_lance_1_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000f2d106104531cb7cb614ca96100000000001da5520000000000000000, 0x0000000f2d106104531cb7cb614ca96100000000001da5520000000000000000 ],
["knight_1_19", "Jacques de Chabannes, Seigneur de La Palice", "Jacques de Chabannes", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000003ff10200b79349999a54d48de00000000001d211c0000000000000000, 0x00000003ff10200b79349999a54d48de00000000001d211c0000000000000000 ],
["knight_1_20", "Antoine de Chabannes, Seigneur de Charlus", "Antoine de Chabannes", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x000000013f10200b7d349f08e58d451600000000001d23190000000000000000, 0x000000013f10200b7d349f08e58d451600000000001d23190000000000000000 ],

["knight_1_21", "Pierre de Beauvau, Seigneur de Beauvau", "Pierre de Beauvau", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x0000000a78101002372e6e6333c51adb00000000001d26d40000000000000000, 0x0000000a78101002372e6e6333c51adb00000000001d26d40000000000000000 ],
["knight_1_22", "Jean IV d'Armagnac, Comte d'Armagnac", "Jean IV d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_tabard,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000057d00300b366c8ad954b5a0b400000000001ca2ed0000000000000000, 0x000000057d00300b366c8ad954b5a0b400000000001ca2ed0000000000000000 ],
["knight_1_23", "Bernard VIII d'Armagnac, Comte de Pardiac", "Bernard VIII d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000003bd00100d469c8cc92491a0b400000000001e44da0000000000000000, 0x00000003bd00100d469c8cc92491a0b400000000001e44da0000000000000000 ],
["knight_1_24", "Jean IV de Termes d'Armagnac, Seigneur de Termes", "Jean de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x0000000ee800400d469c8cc92491a8e600000000001d231a0000000000000000, 0x0000000ee800400d469c8cc92491a8e600000000001d231a0000000000000000 ],
["knight_1_25", "Géraud de Termes d'Armagnac", "Géraud de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x0000000768009002469c8cc92491a8e600000000001e33220000000000000000, 0x0000000768009002469c8cc92491a8e600000000001e33220000000000000000 ],
["knight_1_26", "Thilbault de Termes d'Armagnac", "Thilbault de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000034c00600b469c8ce92491a96f00000000001d23220000000000000000, 0x000000034c00600b469c8ce92491a96f00000000001d23220000000000000000 ],
["knight_1_27", "Renaud de Termes d'Armagnac", "Renaud de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_b], lord_attrib, wp(380), knows_lord_1, 0x000000005f003001449c8db95aa9a6cb00000000001c33120000000000000000, 0x000000005f003001449c8db95aa9a6cb00000000001c33120000000000000000 ],
["knight_1_28", "Jean de Murol, Seigneur de Murol", "Jean de Murol", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x000000096700324552647246a34acd5000000000001eb51a0000000000000000, 0x000000096700324552647246a34acd5000000000001eb51a0000000000000000 ],
["knight_1_29", "Hugues de Cubières du Cheylard, Seigneur de Cubières et du Cheylard", "Hugues de Cubières du Cheylard", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000002ff006005471b71565b8cb6a300000000001dc6eb0000000000000000, 0x00000002ff006005471b71565b8cb6a300000000001dc6eb0000000000000000 ],
["knight_1_30", "Christophe d'Harcourt, Baron D'Avrech", "Christophe d'Harcourt", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x000000092b086144179367531a6e18da00000000001c251d0000000000000000, 0x000000092b086144179367531a6e18da00000000001c251d0000000000000000 ],

["knight_1_31", "Charles II de Poitiers, Seigneur de Saint-Vallier", "Charles de Poitiers", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x0000000ab00c301128b5ad5763c4c86500000000001d351c0000000000000000, 0x0000000ab00c301128b5ad5763c4c86500000000001d351c0000000000000000 ],
["knight_1_32", "Pierre de Beaufort de Turenne, Comte de Beaufort, Vicomte de Turenne", "Pierre de Beaufort de Turenne", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x00000004ab04100b5ced48a91850b8de00000000001d369b0000000000000000, 0x00000004ab04100b5ced48a91850b8de00000000001d369b0000000000000000 ],
["knight_1_33", "Jacques II de Bourbon de Vendôme, Comte de la Marche et de Castres", "Jacques de Bourbon de Vendôme", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_tabard,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x0000000fc708c003335c97346c961b2a00000000001db5ed0000000000000000, 0x0000000fc708c003335c97346c961b2a00000000001db5ed0000000000000000 ],
["knight_1_34", "Louis I de Bourbon de Vendôme, Comte de Vendôme et de Chartres", "Louis de Bourbon de Vendôme", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_sempach], lord_attrib, wp(380), knows_lord_1, 0x0000000e60089000552599b8ac91a6e200000000001db5730000000000000000, 0x0000000e60089000552599b8ac91a6e200000000001db5730000000000000000 ],
["knight_1_35", "Jean de Lignières, Baron de Linières, Seigneur de Rezay, Thévé et Brécy", "Jean de Lignières", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x00000009700810024f119276f22d455300000000001d251a0000000000000000, 0x00000009700810024f119276f22d455300000000001d251a0000000000000000 ],
["knight_1_36", "Jean Malet de Graville, Seigneur de Graville, Grand Maître des Arbalétriers", "Jean Malet de Graville", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_tabard,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x00000007080c601126a2653d9d4d767400000000001da2b20000000000000000, 0x00000007080c601126a2653d9d4d767400000000001da2b20000000000000000 ],
["knight_1_37", "Louis III d'Anjou, Duc d'Anjou", "Louis III d'Anjou", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000005bc00824358d5324982a1bb0f00000000001e051d0000000000000000, 0x00000005bc00824358d5324982a1bb0f00000000001e051d0000000000000000 ],
["knight_1_38", "René d'Anjou, Comte de Provence", "René D'Anjou", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x00000005bc00600558d5324982a1bb7f00000000001e351d0000000000000000, 0x00000005bc00600558d5324982a1bb7f00000000001e351d0000000000000000 ],
["knight_1_39", "Guy XIV de Montfort de Laval, Baron de Laval", "Guy de Laval", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x000000010808300b2a9388d35cb0b72500000000001d24f30000000000000000, 0x000000010808300b2a9388d35cb0b72500000000001d24f30000000000000000 ],
["knight_1_40", "André de Montfort de Laval, Seigneur de Lohéac", "André de Lohéac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x00000000140800053a9388d35cd1271400000000001ca4d90000000000000000, 0x00000000140800053a9388d35cd1271400000000001ca4d90000000000000000 ],

["knight_1_41", "Guy III de Chauvigny, Baron de Châteauroux", "Guy de Chauvigny", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x000000003f08c0043b0c6dd72d8e555400000000001da4dc0000000000000000, 0x000000003f08c0043b0c6dd72d8e555400000000001da4dc0000000000000000 ],
["knight_1_42", "Gilbert Motier de la Fayette, Seigneur de la Fayette", "Gilbert Motier de la Fayette", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_tabard,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000087f0031053a6d66c96a31a46c00000000001e971b0000000000000000, 0x000000087f0031053a6d66c96a31a46c00000000001e971b0000000000000000 ],
["knight_1_43", "Bertrand V de la Tour d'Auvergne, Baron de la Tour", "Bertrand de la Tour d'Auvergne", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x00000005a008600b2b24935b344dbcde00000000001d25620000000000000000, 0x00000005a008600b2b24935b344dbcde00000000001d25620000000000000000 ],
["knight_1_44", "Ambroise de Loré, Capitaine de Sainte-Suzanne", "Ambroise de Loré", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x00000004f20c100d575d6948946ec65300000000001da5210000000000000000, 0x00000004f20c100d575d6948946ec65300000000001da5210000000000000000 ],
["knight_1_45", "Georges de La Trémoille, Grand Chambellan de France", "Georges de La Trémoille", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000003d30024cb369da9bd34ee271400000000001e37210000000000000000, 0x00000003d30024cb369da9bd34ee271400000000001e37210000000000000000 ],
["knight_1_46", "Jean I de Foix, Comte de Foix et de Bigorre","Jean de Foix", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x00000008f508b58738debd5894c9571500000000001dd5290000000000000000, 0x00000008f508b58738debd5894c9571500000000001dd5290000000000000000 ],
["knight_1_47", "Girault de la Paillière", "Girault de la Paillière", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x00000003ff04600d2aa252b9548a4b1900000000001cc28d0000000000000000, 0x00000003ff04600d2aa252b9548a4b1900000000001cc28d0000000000000000 ],
["knight_1_48", "Guillaume II de Gamaches, Seigneur de Gamaches", "Guillaume de Gamaches", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000007910c62912add3939626db6dc00000000001d455b0000000000000000, 0x00000007910c62912add3939626db6dc00000000001d455b0000000000000000 ],
["knight_1_49", "Jean de Gamaches, Seigneur de Rosemont et La Guerche", "Jean de Gamaches", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000004510c60032add3939626dbadb00000000001cb55b0000000000000000, 0x00000004510c60032add3939626dbadb00000000001cb55b0000000000000000 ],
["knight_1_50", "Louis d'Estouteville, Seigneur d'Estouteville et de Valmont", "Louis d'Estouteville", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x000000046d043011439a56352392d75c00000000001dc2a10000000000000000, 0x000000046d043011439a56352392d75c00000000001dc2a10000000000000000 ],

["knight_1_51", "André de Rambures, Seigneur de Rambures", "André de Rambures", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x000000047208100448e68898db3536d900000000001d329b0000000000000000, 0x000000047208100448e68898db3536d900000000001d329b0000000000000000 ],
["knight_1_52", "Denis de Chailly, Seigneur de Chailly", "Denis de Chailly", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x000000063f04600244eb6ee6d8ae229100000000001d13190000000000000000, 0x000000063f04600244eb6ee6d8ae229100000000001d13190000000000000000 ],
["knight_1_53", "Louis-Armand XII de Chalençon-Polignac, Vicomte de Polignac, Baron de Chalençon", "Louis-Armand de Polignac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000610042241370bb0a3a16d955500000000001ea4690000000000000000, 0x0000000610042241370bb0a3a16d955500000000001ea4690000000000000000 ],
["knight_1_54", "Nicolas de Giresme, Chevalier Hospitalier de Rhodes, Commandeur de la Croix-en-Brie", "Nicolas de Giresme", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1_heraldic,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_sempach], lord_attrib, wp(380), knows_lord_1, 0x00000004ff08100554da6656a26d293300000000001ea36b0000000000000000, 0x00000004ff08100554da6656a26d293300000000001ea36b0000000000000000 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC ENGLISH LORDS #########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["knight_2_1", "John Talbot, Baron Talbot and Furnival", "John Talbot", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x000000093108100239a1723b6c826b6700000000001d47210000000000000000, 0x000000093108100239a1723b6c826b6700000000001d47210000000000000000 ],
["knight_2_2", "John Fastolf, Lieutenant-general of Normandy", "John Fastolf", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000b3f0000044b1297cb926d371200000000001e48660000000000000000, 0x0000000b3f0000044b1297cb926d371200000000001e48660000000000000000 ],
["knight_2_3", "William de la Pole, Earl of Suffolk", "William de la Pole", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000001db08024b39e1723769823ffa00000000001d34ed0000000000000000, 0x00000001db08024b39e1723769823ffa00000000001d34ed0000000000000000 ],
["knight_2_4", "Thomas de Scales, Baron de Scales", "Thomas de Scales", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000049608700565247a3b5ba5c99900000000001e47090000000000000000, 0x000000049608700565247a3b5ba5c99900000000001e47090000000000000000 ],
["knight_2_5", "John Tiptoft, Baron Tiptoft", "John Tiptoft", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_tabard,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x000000097710100b189badaba949d29c00000000001ea5740000000000000000, 0x000000097710100b189badaba949d29c00000000001ea5740000000000000000 ],
["knight_2_6", "Thomas Rempston, Baron Rempston and Gacé", "Thomas Rempston", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000006ae08608428d2699b1eb5c8dd00000000001db09a0000000000000000, 0x00000006ae08608428d2699b1eb5c8dd00000000001db09a0000000000000000 ],
["knight_2_7", "Thomas Beaufort, Count of Perche", "Thomas Beaufort", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000001f504b004571c6ad8a27134ea00000000001d37730000000000000000, 0x00000001f504b004571c6ad8a27134ea00000000001d37730000000000000000 ],
["knight_2_8", "Edmund Beaufort, Count of Mortain", "Edmund Beaufort", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000001d704600b371c6ad8a269b6dc00000000001d275b0000000000000000, 0x00000001d704600b371c6ad8a269b6dc00000000001d275b0000000000000000 ],
["knight_2_9", "John Mowbray, Earl of Norfolk", "John Mowbray", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x00000008340460063b1c6e468229b6d100000000001d255b0000000000000000, 0x00000008340460063b1c6e468229b6d100000000001d255b0000000000000000 ],
["knight_2_10", "Richard Beauchamp, Earl of Warwick", "Richard de Beauchamp", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x0000000aff0800023cd275a4fa25232500000000001c42630000000000000000, 0x0000000aff0800023cd275a4fa25232500000000001c42630000000000000000 ],

["knight_2_11", "Humphrey Stafford, Earl of Stafford", "Humphrey Stafford", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000077404b184579b6ec7bb6db6db00000000001c96db0000000000000000, 0x000000077404b184579b6ec7bb6db6db00000000001c96db0000000000000000 ],
["knight_2_12", "Richard le Strange, Baron Strange","Richard le Strange",  tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000009a50c7011351c51a2948a279c00000000001d911c0000000000000000, 0x00000009a50c7011351c51a2948a279c00000000001d911c0000000000000000 ],
["knight_2_13", "Reginald Grey, Baron Grey de Ruthyn", "Reginald Grey", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x0000000fff04340f78646a4ae569e6ec00000000001dd71b0000000000000000, 0x0000000fff04340f78646a4ae569e6ec00000000001dd71b0000000000000000 ],
["knight_2_14", "John Grey, Lord Grey de Ruthyn", "John Grey", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x0000000b3f04300168646a4ae569b6dc00000000001d351b0000000000000000, 0x0000000b3f04300168646a4ae569b6dc00000000001d351b0000000000000000 ],
["knight_2_15", "William Harington, Baron Harington", "William Harington", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000009bf04210168646a4ae549b75c00000000001db51b0000000000000000, 0x00000009bf04210168646a4ae549b75c00000000001db51b0000000000000000 ],
["knight_2_16", "John Radcliffe, Seneschal of Guyenne, Captain of Fronsac", "John Radcliffe", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000aba08600d3d656ec35c74d76b00000000001db51b0000000000000000, 0x0000000aba08600d3d656ec35c74d76b00000000001db51b0000000000000000 ],
["knight_2_17", "Sir Thomas Radcliffe", "Thomas Radcliffe", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x00000003ff0800023ae36ed95c74d76b00000000001db51b0000000000000000, 0x00000003ff0800023ae36ed95c74d76b00000000001db51b0000000000000000 ],
["knight_2_18", "Sir Walter Hungerford", "Walter Hungerford", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000002d50424c2445d85b962ad18e600000000001d15690000000000000000, 0x00000002d50424c2445d85b962ad18e600000000001d15690000000000000000 ],
["knight_2_19", "Sir Robert Hungerford", "Robert Hungerford", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000002f7043006445d85b762ad18e600000000001d14d20000000000000000, 0x00000002f7043006445d85b762ad18e600000000001d14d20000000000000000 ],
["knight_2_20", "Sir Edmund Hungerford", "Edmund Hungerford", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x000000017f04000b265d853762ad190c00000000001d34cb0000000000000000, 0x000000017f04000b265d853762ad190c00000000001d34cb0000000000000000 ],

["knight_2_21", "Richard Woodville, Baron Woodville", "Richard Woodville", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_sempach], lord_attrib, wp(380), knows_lord_1, 0x000000087f10900444664586cc66369300000000001d14d90000000000000000, 0x000000087f10900444664586cc66369300000000001d14d90000000000000000 ],
["knight_2_22", "Sir Richard II Woodville", "Richard Woodville, the young", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x000000027710c00d44664586cc66369300000000001e34d90000000000000000, 0x000000027710c00d44664586cc66369300000000001e34d90000000000000000 ],
["knight_2_23", "James Tuchet, Baron Tuchet", "James Tuchet", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x000000050b08144b472b6e4ee94e38fa00000000001e23690000000000000000, 0x000000050b08144b472b6e4ee94e38fa00000000001e23690000000000000000 ],
["knight_2_24", "Sir William Glasdale", "William Glasdale", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_b], lord_attrib, wp(380), knows_lord_1, 0x000000097f0410023999d4b954c9392500000000001e46760000000000000000, 0x000000097f0410023999d4b954c9392500000000001e46760000000000000000 ],
["knight_2_25", "Sir Thomas Kyriell", "Thomas Kyriell", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_a], lord_attrib, wp(380), knows_lord_1, 0x00000008fc04b00d1a6269d8abaeb6e400000000001f44a40000000000000000, 0x00000008fc04b00d1a6269d8abaeb6e400000000001f44a40000000000000000 ],
["knight_2_26", "Sir James Fiennes", "James Fiennes", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x00000008380c6001551aaa491a2d36e300000000001da96b0000000000000000, 0x00000008380c6001551aaa491a2d36e300000000001da96b0000000000000000 ],
["knight_2_27", "Sir William Oldhall", "William Oldhall", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_tabard,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x00000008b210918b672c3598dba9471300000000001db6d30000000000000000, 0x00000008b210918b672c3598dba9471300000000001db6d30000000000000000 ],
["knight_2_28", "John Holland, Earl of Huntingdon, Amiral", "John Holland", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x00000006900462d12ae48929954897e400000000001d225a0000000000000000, 0x00000006900462d12ae48929954897e400000000001d225a0000000000000000 ],
["knight_2_29", "William Bonville, Baron Bonville", "William Bonville", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x00000008690c15042a63af6aa3a9a2ab00000000001e386d0000000000000000, 0x00000008690c15042a63af6aa3a9a2ab00000000001e386d0000000000000000 ],
["knight_2_30", "Sir Robert Harling", "Robert Harling", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000001f110c011485969390c95d52400000000001d249b0000000000000000, 0x00000001f110c011485969390c95d52400000000001d249b0000000000000000 ],

["knight_2_31", "Sir Matthew Gough", "Matthew Gough", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_w_bastard_sword_agincourt,itm_a_tabard], lord_attrib, wp(380), knows_lord_1, 0x000000096010a243488b523864b9d76400000000001e389a0000000000000000, 0x000000096010a243488b523864b9d76400000000001e389a0000000000000000 ],
["knight_2_32", "John Salvayn, Lord of Croxdale", "John Salvayn", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x00000006eb04100b385289671b4dd71300000000001db5550000000000000000, 0x00000006eb04100b385289671b4dd71300000000001db5550000000000000000 ],
["knight_2_33", "Sir Thomas Blount", "Thomas Blount", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000008bf041002390b75a76a6938cc00000000001db3930000000000000000, 0x00000008bf041002390b75a76a6938cc00000000001db3930000000000000000 ],
["knight_2_34", "Robert Willoughby, Lord Willoughby of Eresby", "Robert Willoughby", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000008bf101001331a75d824aa172300000000001dc9640000000000000000, 0x00000008bf101001331a75d824aa172300000000001dc9640000000000000000 ],
["knight_2_35", "John Beauchamp, Baron Beauchamp", "John Beauchamp", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x00000000f604114446626e36962ea51c00000000001db6cc0000000000000000, 0x00000000f604114446626e36962ea51c00000000001db6cc0000000000000000 ],
["knight_2_36", "Sir Robert Howard of Tendring", "Robert Howard of Tendring", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor_open,itm_a_tabard,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x00000008c90420064ca3adaada91259b00000000001d34a50000000000000000, 0x00000008c90420064ca3adaada91259b00000000001d34a50000000000000000 ],
["knight_2_37", "Ralph Boteler, Baron Sudeley", "Ralph Boteler", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x000000069d0c6006641332d92a32399a00000000001e34e30000000000000000, 0x000000069d0c6006641332d92a32399a00000000001e34e30000000000000000 ],
["knight_2_38", "John Fitzalan, Earl of Arundel", "John Fitzalan", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x000000007704900532adf646cc6b365e00000000001db29b0000000000000000, 0x000000007704900532adf646cc6b365e00000000001db29b0000000000000000 ],
["knight_2_39", "Henry Bourchier, Count of Eu", "Henry Bourchier", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000002fc0030022951b1d9644a49b300000000001f47a30000000000000000, 0x00000002fc0030022951b1d9644a49b300000000001f47a30000000000000000 ],
["knight_2_40", "John Robessart, Lord of Escaillon and Bruille", "John Robessart", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x0000000abd0434912ba23254da6d249400000000000cc6e30000000000000000, 0x0000000abd0434912ba23254da6d249400000000000cc6e30000000000000000 ],

["knight_2_41", "Sir Lewis Robessart", "Lewis Robessart", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000005fd0420032ba25254da6d127400000000001cc4a30000000000000000, 0x00000005fd0420032ba25254da6d127400000000001cc4a30000000000000000 ],
["knight_2_42", "Bertrand III de Montferrand, Baron de Guyenne", "Bertrand de Montferrand", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x0000000a5d04700042d24548ebc9e6b200000000001d28a20000000000000000, 0x0000000a5d04700042d24548ebc9e6b200000000001d28a20000000000000000 ],
["knight_2_43", "François de Montferrand, Gouverneur de Dax, Sénéchal des Lannes", "François de Montferrand", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x000000075d04818432d24548eb69372b00000000001e28a20000000000000000, 0x000000075d04818432d24548eb69372b00000000001e28a20000000000000000 ],
["knight_2_44", "Jean de Montferrand, Seigneur de Langoiran", "Jean de Montferrand", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x000000014204800236d24548eb69372b00000000001e24a20000000000000000, 0x000000014204800236d24548eb69372b00000000001e24a20000000000000000 ],
["knight_2_45", "Jean-Gaillard de Durfort, Seigneur de Duras, Prévôt de Bayonne", "Jean-Gaillard de Durfort",  tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000009a704900d4b5b6de919d52b9500000000001d46490000000000000000, 0x00000009a704900d4b5b6de919d52b9500000000001d46490000000000000000 ],
["knight_2_46", "Sir Robert de Vere", "Robert de Vere", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_tabard,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x000000020710300d29136e596c70c89e00000000001d36d30000000000000000, 0x000000020710300d29136e596c70c89e00000000001d36d30000000000000000 ],
["knight_2_47", "Sir Richard de Vere", "Richard de Vere", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x000000020710000329136db4e470c89500000000001c15230000000000000000, 0x000000020710000329136db4e470c89500000000001c15230000000000000000 ],
["knight_2_48", "Sir John de la Pole", "John de la Pole", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_tabard,itm_b_high_boots_2,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x00000005ea08324d469b91b2f5514ad300000000001eb8e30000000000000000, 0x00000005ea08324d469b91b2f5514ad300000000001eb8e30000000000000000 ],
["knight_2_49", "Sir Alexander de la Pole", "Alexander de la Pole", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x00000005ea081004469b91b2db4d36d300000000001d44e30000000000000000, 0x00000005ea081004469b91b2db4d36d300000000001d44e30000000000000000 ],
["knight_2_50", "Sir Thomas de la Pole", "Thomas de la Pole", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x00000005fa080006392491b8db4d26d300000000001ca4c90000000000000000, 0x00000005fa080006392491b8db4d26d300000000001ca4c90000000000000000 ],

["knight_2_51", "Lawrence Warren, Lord of Poynton and Stockport", "Lawrence Warren", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_1_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x00000008ac08428d59628e976b88a4dd00000000001e94e30000000000000000, 0x00000008ac08428d59628e976b88a4dd00000000001e94e30000000000000000 ],
["knight_2_52", "Sir Richard Hankford", "Richard Hankford", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3_heraldic,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000005bc00100438f3319a8c5464e100000000001e44e30000000000000000, 0x00000005bc00100438f3319a8c5464e100000000001e44e30000000000000000 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC BURGUNDIAN LORDS ######################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["knight_3_1", "Antoine de Toulongeon, Seigneur de Buxy, La Bastie, Montrichard et de Traves", "Antoine de Toulongeon", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_2_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000a3f0c600b54db6fb4db46524200000000001da35d0000000000000000, 0x0000000a3f0c600b54db6fb4db46524200000000001da35d0000000000000000 ],
["knight_3_2", "André de Toulongeon, Seigneur de Mornay", "André de Toulongeon", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x0000000a3f0cb00b559491b4db46549000000000001da3630000000000000000, 0x0000000a3f0cb00b559491b4db46549000000000001da3630000000000000000 ],
["knight_3_3", "Guy de Bourgogne, Comte de Rethel", "Guy de Bourgogne", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_6_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x00000007a008600444c24e59196934ab00000000001cc6e50000000000000000, 0x00000007a008600444c24e59196934ab00000000001cc6e50000000000000000 ],
["knight_3_4", "Pierre I de Luxembourg, Comte de Brienne", "Pierre de Luxembourg", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_1_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000008ff08c00b351b6f39236db75800000000001dc4d20000000000000000, 0x00000008ff08c00b351b6f39236db75800000000001dc4d20000000000000000 ],
["knight_3_5", "Jean II de Luxembourg, Comte de Guise", "Jean II de Luxembourg", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_2_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_duke], lord_attrib, wp(380), knows_lord_1, 0x00000007a408200b471b6e0b234dbd5900000000001dc4d20000000000000000, 0x00000007a408200b471b6e0b234dbd5900000000001dc4d20000000000000000 ],
["knight_3_6", "Jean de Luxembourg, Seigneur d'Haubourdin et d'Ailly", "Jean de Luxembourg", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x00000006ff00100229588d3cde89555c00000000001d251c0000000000000000, 0x00000006ff00100229588d3cde89555c00000000001d251c0000000000000000 ],
["knight_3_7", "Baudot de Noyelles, Seigneur de Noyelles", "Baudot de Noyelles", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_baron], lord_attrib, wp(380), knows_lord_1, 0x00000006fb1010115923ada8238eb8d000000000001e26cc0000000000000000, 0x00000006fb1010115923ada8238eb8d000000000001e26cc0000000000000000 ],
["knight_3_8", "Pierre de Bauffremont, Comte de Charny et Seigneur de Montfort", "Pierre de Bauffremont", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000006ea00324d36936d96daa6591e00000000001da90c0000000000000000, 0x00000006ea00324d36936d96daa6591e00000000001da90c0000000000000000 ],
["knight_3_9", "Régnier Pot, Seigneur de la Prugne", "Régnier Pot", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_6_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_pigface_klappvisor_open,itm_a_tabard,itm_g_finger_gauntlets,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x0000000f3f0011422b269a2adc8ad99200000000001ed15c0000000000000000, 0x0000000f3f0011422b269a2adc8ad99200000000001ed15c0000000000000000 ],
["knight_3_10", "Jean de Villiers de l'Isle-Adam, Seigneur de L'Isle-Adam", "Jean de Villiers de l'Isle-Adam", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000097208121144a65a345c764d1900000000001d45230000000000000000, 0x000000097208121144a65a345c764d1900000000001d45230000000000000000 ],

["knight_3_11", "David de Brimeu, Seigneur de Ligny", "David de Brimeu", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000009be0c14cd151449276b52d51a00000000001d351b0000000000000000, 0x00000009be0c14cd151449276b52d51a00000000001d351b0000000000000000 ],
["knight_3_12", "Jacques de Brimeu, Seigneur de Grigny", "Jacques de Brimeu", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x00000009be0c300914d449449349b51a00000000001e351b0000000000000000, 0x00000009be0c300914d449449349b51a00000000001e351b0000000000000000 ],
["knight_3_13", "Jean de La Trémoille, Seigneur de Jonvelle", "Jean de La Trémoille", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_2_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000b2a04248216dcb226e57268d500000000001e37250000000000000000, 0x0000000b2a04248216dcb226e57268d500000000001e37250000000000000000 ],
["knight_3_14", "Antoine de Vergy, Comte de Dammartin", "Antoine de Vergy", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_6_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x0000000b3c04300422dcb2aaa57268d500000000001e272a0000000000000000, 0x0000000b3c04300422dcb2aaa57268d500000000001e272a0000000000000000 ],
["knight_3_15", "Jean IV de Vergy, Seigneur de Fouvent-Saint-Andoche", "Jean de Vergy", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x0000000b3c043151249cb2aaa57268d500000000001db72a0000000000000000, 0x0000000b3c043151249cb2aaa57268d500000000001db72a0000000000000000 ],
["knight_3_16", "Guillaume IV de Vienne, Seigneur de Saint-Georges et de Sainte-Croix", "Guillaume de Vienne", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x0000000fc010750f435a7866d349392400000000001eb2b20000000000000000, 0x0000000fc010750f435a7866d349392400000000001eb2b20000000000000000 ],
["knight_3_17", "Antoine I de Croÿ, Seigneur de Croÿ", "Antoine de Croÿ", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x0000000a2e08100136d986536457565e00000000001cb6990000000000000000, 0x0000000a2e08100136d986536457565e00000000001cb6990000000000000000 ],
["knight_3_18", "Jean II de Croÿ, Seigneur de Chimay", "Jean de Croÿ", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x00000006ae08c00128d96dd3644e365300000000001da4910000000000000000, 0x00000006ae08c00128d96dd3644e365300000000001da4910000000000000000 ],
["knight_3_19", "Roland d'Uytkerke, Seigneur d'Uytkerke", "Roland d'Uytkerke", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000093404c00b54e2cdc929764a5a00000000001dd4a30000000000000000, 0x000000093404c00b54e2cdc929764a5a00000000001dd4a30000000000000000 ],
["knight_3_20", "Thibaud VI de Rougemont, Vicomte de Besançon, Seigneur de Rougemont", "Thibaud VI de Rougemont", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x000000055604108d49237ab8ec70c55b00000000001d36590000000000000000, 0x000000055604108d49237ab8ec70c55b00000000001d36590000000000000000 ],

["knight_3_21", "Claude de Beauvoir, Seigneur de Chastellux", "Claude de Beauvoir", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x0000000c5f04904b1aebae7eed6f572400000000001caab40000000000000000, 0x0000000c5f04904b1aebae7eed6f572400000000001caab40000000000000000 ],
["knight_3_22", "Jean des Mazis, Capitaine d'Etampes et Dourdan", "Jean des Mazis", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x0000000c5f04904b1aebae7eed6f572400000000001caab40000000000000000, 0x000000075c0882913ae1ae470a71456400000000001cc4990000000000000000 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC BRETON LORDS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["knight_4_1", "Arthur de Richemont, Connétable de Richemont", "Arthur de Richemont", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_1_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000c560430004d0b2e7a5e8c1da400000000001eb7620000000000000000, 0x0000000c560430004d0b2e7a5e8c1da400000000001eb7620000000000000000 ],
["knight_4_2", "Richard de Montfort, Comte d'Étampes, Seigneur de Clisson", "Richard de Montfort", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_1_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000006bf041006490b6e389b6d27a400000000001d25620000000000000000, 0x00000006bf041006490b6e389b6d27a400000000001d25620000000000000000 ],
["knight_4_3", "Jean de Penhoët, Seigneur de Penhoët", "Jean de Penhoët", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000ff60822445996366baa74d69a00000000001e48ca0000000000000000, 0x0000000ff60822445996366baa74d69a00000000001e48ca0000000000000000 ],
["knight_4_4", "Tanneguy III du Chastel, Seigneur Du Chastel", "Tanneguy du Chastel", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x0000000b7500224434cdcec7b16aa6d300000000001d48ea0000000000000000, 0x0000000b7500224434cdcec7b16aa6d300000000001d48ea0000000000000000 ],
["knight_4_5", "Prigent VII de Coëtivy, Seigneur de Coëtivy", "Prigent de Coëtivy", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_1_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000077704c00b1491923654adb76200000000001d35120000000000000000, 0x000000077704c00b1491923654adb76200000000001d35120000000000000000 ],
["knight_4_6", "Tugdual de Kermoysan, Seigneur de Kermoysan et de Goasmap", "Tugdual de Kermoysan", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_2_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_b], lord_attrib, wp(380), knows_lord_1, 0x000000093f043306445c6eb92b93285400000000001db4db0000000000000000, 0x000000093f043306445c6eb92b93285400000000001db4db0000000000000000 ],
["knight_4_7", "Henri Penmarc'h, Seigneur de Penmarc'h", "Henri Penmarc'h", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_c], lord_attrib, wp(380), knows_lord_1, 0x0000000cb70c700f6add56aaa24db6eb00000000001ca69c0000000000000000, 0x0000000cb70c700f6add56aaa24db6eb00000000001ca69c0000000000000000 ],
["knight_4_8", "Sire Alain Penmarc'h", "Alain Penmarc'h", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x00000006370c10026add56aaa24db6eb00000000001db6da0000000000000000, 0x00000006370c10026add56aaa24db6eb00000000001db6da0000000000000000 ],
["knight_4_9", "Alain IX de Rohan, Vicomte de Rohan", "Alain IX de Rohan", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x0000000bb70c10046add56a6e34dbaeb00000000001eb75a0000000000000000, 0x0000000bb70c10046add56a6e34dbaeb00000000001eb75a0000000000000000 ],
["knight_4_10", "Alain X de Rohan, Vicomte de Léon", "Alain de Rohan", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x00000003b500300b272372e90c4db69300000000001d26d20000000000000000, 0x00000003b500300b272372e90c4db69300000000001d26d20000000000000000 ],

["knight_4_11", "Charles de Rohan-Guéméné, Seigneur de Guéméné", "Charles de Rohan-Guéméné", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x0000000da90c734436d295469b71276200000000001d34da0000000000000000, 0x0000000da90c734436d295469b71276200000000001d34da0000000000000000 ],
["knight_4_12", "Louis de Rohan-Guéméné", "Louis de Rohan-Guéméné", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_5_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent], lord_attrib, wp(380), knows_lord_1, 0x000000020b0c800936d295469b91269a00000000001d34920000000000000000, 0x000000020b0c800936d295469b91269a00000000001d34920000000000000000 ],
["knight_4_13", "Guillaume de Rosmadec, Baron de Rosmadec", "Guillaume de Rosmadec", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor,itm_a_tabard,itm_b_leg_harness_7,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000081b0c554454cb9e156365286400000000001ca4e30000000000000000, 0x000000081b0c554454cb9e156365286400000000001ca4e30000000000000000 ],
["knight_4_14", "Pierre de Rochefort, Seigneur de Rieux et de Rochefort", "Pierre de Rochefort", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_2_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x000000081b0c748536db6db6db594d2400000000001ed4db0000000000000000, 0x000000081b0c748536db6db6db594d2400000000001ed4db0000000000000000 ],
["knight_4_15", "Bertrand de Dinan, Seigneur de Châteaubriant", "Bertrand de Dinan", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_3_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x000000052a089191438db6a8a351d75b00000000001db71b0000000000000000, 0x000000052a089191438db6a8a351d75b00000000001db71b0000000000000000 ],
["knight_4_16", "Jacques de Dinan, Seigneur de Beaumanoir", "Jacques de Dinan", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_4_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_sempach], lord_attrib, wp(380), knows_lord_1, 0x000000032a081002438db6a89b51b6db00000000001db71b0000000000000000, 0x000000032a081002438db6a89b51b6db00000000001db71b0000000000000000 ],
["knight_4_17", "Raoul V de Coëtquen, Seigneur de Coëtquen", "Raoul de Coëtquen", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_6_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_pigface_klappvisor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x0000000f7f0cb50b2ae671c75265996000000000001e44f40000000000000000, 0x0000000f7f0cb50b2ae671c75265996000000000001e44f40000000000000000 ],
["knight_4_18", "Rolland III de Coëtmen, Seigneur de Tonquédec, Comte de Trégor et Goëlo", "Rolland de Coëtmen", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_1_heraldic,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_tabard,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x00000006bc04101125a3972ae46f3ce300000000001d38f20000000000000000, 0x00000006bc04101125a3972ae46f3ce300000000001d38f20000000000000000 ],


# ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

# ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

["kingdom_3_pretender",  "Philippe de Saint-Pol",  "Philippe de Saint-Pol",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_s_heraldic_shield_metal,itm_w_lance_4,itm_ho_horse_barded_brown_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_churburg_13_asher_plain_custom,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_regent],      lord_attrib,wp(220),knight_skills_5, 0x00000006b30c900c7c5bd13920b124f100000000001da8ca0000000000000000, 0x00000006b30c900c7c5bd13920b124f100000000001da8ca0000000000000000],
#of the family

["kingdom_4_pretender",  "Olivier de Blois",   "Olivier de Blois",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_s_heraldic_shield_metal,itm_w_lance_1,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_churburg_13_asher_plain_custom,itm_b_leg_harness_7,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy],            lord_attrib,wp(220),knight_skills_5, 0x0000000ffd08024446ca55cb6caeba9b00000000001db3500000000000000000, 0x0000000ffd08024446ca55cb6caeba9b00000000001db3500000000000000000],
#dispossessed and wronged

# ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
# republican

# ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

["knight_1_1_wife", "Error - knight_1_1_wife should not appear in game", "knight_1_1_wife", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners, [], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC FRENCH LADIES ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["kingdom_1_lady_1", "Jeanne d'Orléans", "Jeanne d'Orléans", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002f0c40024b246ab55389a713003a21202816b71a0000000000000000 ],
["kingdom_1_lady_2", "Marie d'Anjou", "Marie d'Anjou", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001f40460045d444b3561d71e84003d5806ed90d56b0000000000000000 ],
["kingdom_1_lady_3", "Catherine de Thouars", "Catherine de Thouars", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000080001371aaa4564d2352d0038000020114b560000000000000000 ],
["kingdom_1_lady_4", "Anne d'Armagnac", "Anne d'Armagnac", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002b80c300457894653e28a384c0038000a21b104e20000000000000000 ],
["kingdom_1_lady_5", "Jacqueline de Montaigu", "Jacqueline de Montaigu", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000054f004004478dd14aa3d0c72c001491db6549af5b0000000000000000 ],
["kingdom_1_lady_6", "Marguerite de Savoie", "Marguerite de Savoie", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_6], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002be0c100627a38ec9ab97195d000b24e72a71938a0000000000000000 ],
["kingdom_1_lady_7", "Louise-Marie de Rieux", "Louise-Marie de Rieux", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_6], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003210400664f2703b6292b89300384e491b72d80e0000000000000000 ],
["kingdom_1_lady_8", "Agnès de Bueil", "Agnès de Bueil", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a0c50025d7c951b6b721b6b00332abaeaba57630000000000000000 ],
["kingdom_1_lady_9", "Isabelle de Lorraine", "Isabelle de Lorraine", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000e0040053aac9137548ab894003b4a99626a25090000000000000000 ],
["kingdom_1_lady_10", "Jeanne de Montjean", "Jeanne de Montjean", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a006006552386e72d530b20003b85ba5d7138dc0000000000000000 ],

["kingdom_1_lady_11", "Jeanne de Châtillon", "Jeanne de Châtillon", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000fbd045001475cda276991d8d5002491c64c6abb0e0000000000000000 ],
["kingdom_1_lady_12", "Catherine de Laval", "Catherine de Laval", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000051050045b4c96badb9658eb00380000001118e50000000000000000 ],
["kingdom_1_lady_13", "Marie d'Armagnac", "Marie d'Armagnac", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_6], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000cf81000053cb545ad1c4db763003b98d91c7a3bb50000000000000000 ],
["kingdom_1_lady_14", "Jeanne de Preuilly", "Jeanne de Preuilly", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000005ec081004750ab7c2918e3b9a003a2eb66b9633210000000000000000 ],
["kingdom_1_lady_15", "Jeanne de Naillac", "Jeanne de Naillac", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000684006004691d81d77e7624f4003929b2a476270c0000000000000000 ],
["kingdom_1_lady_16", "Agnès de Bourgogne", "Agnès de Bourgogne", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a08100544096d4b24860734003c4a4f1b4e53090000000000000000 ],
["kingdom_1_lady_17", "Jeanne de Clermont", "Jeanne de Clermont", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000b04100238654d54e26da8d2003b6128652ea4e30000000000000000 ],
["kingdom_1_lady_18", "Sybille de Montaut", "Sybille de Montaut", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000b6908400228a352b95d6db72500380000100ca8d10000000000000000 ],
["kingdom_1_lady_19", "Anne de Launay", "Anne de Launay", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000e10400336db6db6db6db6db003b6db6db6db6db0000000000000000 ],
["kingdom_1_lady_20", "Jeanne de Joyeuse", "Jeanne de Joyeuse", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000370030023aac9137548ab894003b4a99626a25490000000000000000 ],

["kingdom_1_lady_21", "Jacquette du Peschin", "Jacquette du Peschin", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000030c500228e489b5638d86ac003985c8626e575c0000000000000000 ],
["kingdom_1_lady_22", "Isabelle de Navarre", "Isabelle de Navarre", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000537104004389d76371b71c8a9003800001009a72b0000000000000000 ],
["kingdom_1_lady_23", "Eléonore de Bourbon", "Eléonore de Bourbon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000040040064d6469d44c925093003caad76c98b51d0000000000000000 ],
["kingdom_1_lady_24", "Eyquem de Tasque", "Eyquem de Tasque", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000d80102002196b89c352a636a1003e7236b570b76a0000000000000000 ],
["kingdom_1_lady_25", "Guilhelma d'Urgosse", "Guilhelma d'Urgosse", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003f0c100528e489b5638d86ac003985c8626e575c0000000000000000 ],
["kingdom_1_lady_26", "Catherine de Marcilly", "Catherine de Marcilly", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000a00200234cc8d54a22ed66c003c74cada69ec990000000000000000 ],
["kingdom_1_lady_27", "Jeanne d'Albret", "Jeanne d'Albret", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001ab0810046b53524ae599c524003c8146d5a2b9190000000000000000 ],
["kingdom_1_lady_28", "Gabrielle de Lastic", "Gabrielle de Lastic", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001b710600458628d12d5aa32db003a66bd2a7165110000000000000000 ],
["kingdom_1_lady_29", "Cécile d'Altier", "Cécile d'Altier", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000a35006005568d72569a8d3995003a5236f25636e30000000000000000 ],
["kingdom_1_lady_30", "Marguerite de Corbie", "Marguerite de Corbie", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000101004371a6a4a63314554003d51a8dd9246910000000000000000 ],

["kingdom_1_lady_31", "Anne de Montlaur", "Anne de Montlaur", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000180c100628e489b5638d86ac003985c8626e575c0000000000000000 ],
["kingdom_1_lady_32", "Blanche de Gimel", "Blanche de Gimel", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001810840043ad28dbbb4ca5756003645d661b5254c0000000000000000 ],
["kingdom_1_lady_33", "Isabeau de Lignières", "Isabeau de Lignières", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000026a10000353898987a55624e5003d80c72af0c36a0000000000000000 ],
["kingdom_1_lady_34", "Jeanne de Laval", "Jeanne de Laval", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001b61040013314722cda72a4f5003d9abcdd4a34a50000000000000000 ],
["kingdom_1_lady_35", "Jacqueline de Chambly", "Jacqueline de Chambly", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000006fc00600646d2463b6d52b650003b3532e591c8e20000000000000000 ],
["kingdom_1_lady_36", "Jeanne Paynel", "Jeanne Paynel", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000391060052b8c86557252849a0039254ce3a587200000000000000000 ],
["kingdom_1_lady_37", "Péronne de Créquy", "Péronne de Créquy", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000004330c600337114a4b185328db003c52599371bb630000000000000000 ],
["kingdom_1_lady_38", "Denise Pisdoë", "Denise Pisdoë", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000005fa0840045cdb764698921616001bc947249948d50000000000000000 ],
["kingdom_1_lady_39", "Isabeau de la Tour d'Auvergne", "Isabeau de la Tour d'Auvergne", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000047c084005045b6dcb1a8a66c3003dd3dc5ca4d5590000000000000000 ],
["kingdom_1_lady_40", "Bonne d'Armagnac", "Bonne d'Armagnac", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000004781030054d5bd2b8d36ab91b003b41b72390988a0000000000000000 ],

["kingdom_1_lady_41", "Corneille de Barbazan", "Corneille de Barbazan", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000016e0000064593292662912b93003c50b3648e39a20000000000000000 ],
["kingdom_1_lady_42", "Jeanne de Chailly", "Jeanne de Chailly", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002c006003446284b0eb75c6940011ce356bc5375c0000000000000000 ],
["kingdom_1_lady_43", "Blanche de Gamaches", "Blanche de Gamaches", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003508500427517a6a9d72a8e9003ca726d16db3a40000000000000000 ],
["kingdom_1_lady_44", "Marie Malet de Graville", "Marie Malet de Graville", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000340c6004391b7238ed8da934003db5bae591aa9b0000000000000000 ],
["kingdom_1_lady_45", "Johannetta de Termes d'Armagnac", "Johannetta de Termes d'Armagnac", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003804500457a34519a4adb923003b99476475cf2e0000000000000000 ],
["kingdom_1_lady_46", "Marguerite de Brosse", "Marguerite de Brosse", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000341000013b24aac2f38eec6b0024463bb3f539610000000000000000 ],
["kingdom_1_lady_47", "Aenor de Culant", "Aenor de Culant", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001800400014b1a4ab4eaa5b2dc003932d7e517255e0000000000000000 ],
["kingdom_1_lady_48", "Jehannette de Bourbon", "Jehannette de Bourbon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002890c300536db6db6db6db6db003b6db6de61b6eb0000000000000000 ],
["kingdom_1_lady_49", "Johaneta de Foix", "Johaneta de Foix", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000006908200136d36dc4dc8ae72a003966b6d52db2aa0000000000000000 ],
["kingdom_1_lady_50", "Jacqueline de Lignières", "Jacqueline de Lignières", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002b044005444ba16aa556085a003e65b36da962e30000000000000000 ],

["kingdom_1_lady_51", "Jeanne de Poitiers", "Jeanne de Poitiers", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002e1030027b0aacb8d56d94eb003d75455b9006a90000000000000000 ],
["kingdom_1_lady_52", "Marguerite d'Harcourt", "Marguerite d'Harcourt", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003100100448a80d92ed8da543003e8a296db1559c0000000000000000 ],
["kingdom_1_lady_53", "Dauphine de Murol", "Dauphine de Murol", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a08100544096d4b24860734003c4a4f1b4e53090000000000000000 ],
["kingdom_1_lady_54", "Louise de Chalençon-Polignac", "Louise de Chalençon-Polignac", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000028104005216512296a9ab6d5003d75a4e17037640000000000000000 ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC ENGLISH LADIES ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["kingdom_2_lady_1", "Margareth Beauchamp", "Margareth Beauchamp", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002550c600232db6db6986db6db003b6eb75b6d36c30000000000000000 ],
["kingdom_2_lady_2", "Millicent Tibetot", "Millicent Tibetot", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000df10440013665a6591c9b1922003d82351929291c0000000000000000 ],
["kingdom_2_lady_3", "Alice Chaucer", "Alice Chaucer", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_6], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002cd0030013ae2adbb5429dae2003b55449e8aab130000000000000000 ],
["kingdom_2_lady_4", "Ismayne Whalesburgh", "Ismayne Whalesburgh", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_6], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002260c300359a4adeaeb921d0e003d752bac32e4dd0000000000000000 ],
["kingdom_2_lady_5", "Joyce Charlton", "Joyce Charlton", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000021b0c4005356431358a522699003800001010b92a0000000000000000 ],
["kingdom_2_lady_6", "Alice Beckering", "Alice Beckering", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002ce0c60016b63c946c6722b6c003e89a719295cd40000000000000000 ],
["kingdom_2_lady_7", "Joan Fastolf", "Joan Fastolf", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001110500166d445e311b2591a003c260b629356d60000000000000000 ],
["kingdom_2_lady_8", "Eleanor Beauchamp", "Eleanor Beauchamp", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002804400158f969991991d81a003a5ab0d4e916e20000000000000000 ],
["kingdom_2_lady_9", "Katherine Neville", "Katherine Neville", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000003fd0450062893523a5ba9c7a3003a45249a71f7730000000000000000 ],
["kingdom_2_lady_10", "Elizabeth Grey", "Elizabeth Grey", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001c204500266ab89549d96c8da003da598e6b5a95b0000000000000000 ],

["kingdom_2_lady_11", "Anne Neville", "Anne Neville", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003500500228ecba16a3c9c514003b2d452c35c3740000000000000000 ],
["kingdom_2_lady_12", "Joan Grey", "Joan Grey", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000002e90020041d51a930d22ac6a9003b88c914d6946b0000000000000000 ],
["kingdom_2_lady_13", "Joan de Astley", "Joan de Astley", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000bbc04100214a5adb6b22aa4e2003dadc74a7959130000000000000000 ],
["kingdom_2_lady_14", "Constance Holland", "Constance Holland", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000082a0060024513719af66ec6db001a4d255a91c9510000000000000000 ],
["kingdom_2_lady_15", "Margaret Neville", "Margaret Neville", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000072d005006351f4d34dd72d2ca00380000000ead0c0000000000000000 ],
["kingdom_2_lady_16", "Katherine Burnell", "Katherine Burnell", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_6], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000003240450045975f90dadaa18e2003ba5c7229640e40000000000000000 ],
["kingdom_2_lady_17", "Eleanor Grey", "Eleanor Grey", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000022c00200166dcc634a28a2713003a5a296aa6b8620000000000000000 ],
["kingdom_2_lady_18", "Fynette Radcliffe ", "Fynette Radcliffe ", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_2], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000120000044905cd170c56c963003e5135552dd3640000000000000000 ],
["kingdom_2_lady_19", "Elizabeth Woodville", "Elizabeth Woodville", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000171084001691945c7aa76191a003800000009631d0000000000000000 ],
["kingdom_2_lady_20", "Joan Woodville", "Joan Woodville",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000034106001060daa34f43f9b7800398f6ee2ace8c60000000000000000],

["kingdom_2_lady_21","Joan Bittlesgate","Joan Bittlesgate",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058d0420064c1e0f370c75c6dc003c6d3a5b3b97340000000000000000],
["kingdom_2_lady_22","Mary Oldhall","Mary Oldhall",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002f005002585c7a475c6257490034f238db5127220000000000000000],
["kingdom_2_lady_23","Eleanor Holland","Eleanor Holland",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000016d005004189495a99c9e975100029254a266b9290000000000000000],
["kingdom_2_lady_24","Elizabeth Blount","Elizabeth Blount",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a08100544096d4b24860734003c4a4f1b4e53090000000000000000],
["kingdom_2_lady_25","Joan Willoughby","Joan Willoughby",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000210c200454d63740f5d258dc00038dccea88e6e40000000000000000],
["kingdom_2_lady_26","Emmeline Fiennes","Emmeline Fiennes",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003fe08300634930f58d42db69600380dca1c5546730000000000000000],
["kingdom_2_lady_27","Mary Willoughby","Mary Willoughby",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008740c20064573261a636d396400000000000eb2dc0000000000000000],
["kingdom_2_lady_28","Anne Stafford","Anne Stafford",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000014210100454b5b357143228dc001c6d268baae91b0000000000000000],
["kingdom_2_lady_29","Elizabeth Courtenay","Elizabeth Courtenay",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000f500100622e2521563b312eb0038000a180d3b740000000000000000],
["kingdom_2_lady_30","Jane Gonville","Jane Gonville",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000020c400258958e4ada8656d3003baaeaa470b31c0000000000000000],

["kingdom_2_lady_31","Margareth Moythe","Margareth Moythe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000025f0030045b2277455a9338a2000a92c94e92250b0000000000000000],
["kingdom_2_lady_32","Katherine Howard of Trending","Katherine Howard of Trending",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000c103002575d6848e129bb1b003cb60a9c8d291b0000000000000000],
["kingdom_2_lady_33","Margery Gresley","Margery Gresley",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000009820c40024451d528666f4b6a003ca988de89a9240000000000000000],
["kingdom_2_lady_34","Elizabeth Montacute","Elizabeth Montacute",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000d4508400329146db512adc71a003bd145366d55330000000000000000],
["kingdom_2_lady_35","Isabeau de Montferrand","Isabeau de Montferrand",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003710000626446e36f349a96b0039166ae58ed69c0000000000000000],
["kingdom_2_lady_36","Margaret Mowbray","Margaret Mowbray",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000010c5005391b7238ed8da934003db5bae591aa9b0000000000000000],
["kingdom_2_lady_37","Elizabeth Boteler","Elizabeth Boteler",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000010c4002391b7238ed8da9340025b5bae591aa9b0000000000000000],
["kingdom_2_lady_38","Maud Lovell","Maud Lovell",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000900500337257aa963c94a2a000d4d34a1aee3550000000000000000],
["kingdom_2_lady_39","Isabel of Cambridge of York","Isabel of Cambridge of York",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000290800044d2daad6da91a6aa003dc1a513b1c6e50000000000000000],
["kingdom_2_lady_40","Jane Kerdeston","Jane Kerdeston",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000147083004146545a974ca972500380004635507240000000000000000],

["kingdom_2_lady_41","Elizabeth Bourchier","Elizabeth Bourchier",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000036d041006369ca9cab4324720001b6628ddb0d8620000000000000000],
["kingdom_2_lady_42","Isabeau de Preissac","Isabeau de Preissac",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008b4006002471a99c82374c56c003e48ba528ec89a0000000000000000],
["kingdom_2_lady_43","Jouyne de Pommiers","Jouyne de Pommiers",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000072b0c400236aca5c8e44e92eb003399d2d498a7630000000000000000],
["kingdom_2_lady_44","Johaneta de Durfort","Johaneta de Durfort",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a10200136db6db6db6db6db003b6db6db6db6db0000000000000000],
["kingdom_2_lady_45","Judiote de la Lande","Judiote de la Lande",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000037c0c4005344636491c719cd9003800069b69c72a0000000000000000],
["kingdom_2_lady_46","Joan Courtenay","Joan Courtenay",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007071030054cac8616536a359b003a8eb8e46da95b0000000000000000],
["kingdom_2_lady_47","Johaneta de Montferrand","Johaneta de Montferrand",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000371030056accaa575b6a4a8b00380000000e64db0000000000000000],
["kingdom_2_lady_48","Judiote de Durfort","Judiote de Durfort",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000035001004569db5b6a5d2b11d003800042b6924e30000000000000000],
["kingdom_2_lady_49","Margaret Warren","Margaret Warren",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a084004172c49b8ec8e549e001cb658a36abaa80000000000000000],
["kingdom_2_lady_50","Joan Warren","Joan Warren",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a084004172c51b8ec8e5d5c003cb658a396baa80000000000000000],

["kingdom_2_lady_51","Margery de Bulkeley","Margery de Bulkeley",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000009ad10500656e971379a7539a40038000018123ab50000000000000000],
["kingdom_2_lady_52","Anne Montacute","Anne Montacute",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e800c400217294aa89cb1a6ed003ba5451592149c0000000000000000],
["kingdom_2_lady_53","Anne de Bourgogne","Anne de Bourgogne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001820c50013acd66369d76d91b003b89925b6e36e30000000000000000],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC BURGUNDIAN LADIES ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["kingdom_3_lady_1","Béatrice de Saint-Chéron","Béatrice de Saint-Chéron",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_2 ],    def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006f10c10044973a69d6e8b40e200000000180e3adc0000000000000000],
["kingdom_3_lady_2","Corneille de Bourgogne","Corneille de Bourgogne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_3 ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000006081002269a76b771da1d63000ab248606a365f0000000000000000],
["kingdom_3_lady_3","Jeanne de Toulongeon","Jeanne de Toulongeon",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_b_turnshoes_1,itm_a_woman_court_dress_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000037f0440045754935ad4863654003b4d971d06239c0000000000000000],
["kingdom_3_lady_4","Marguerite des Baux","Marguerite des Baux",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [itm_b_turnshoes_1,itm_a_woman_court_dress_5 ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000067010600128e2ae56e9ada4ad0039491165eeb4ab0000000000000000],
["kingdom_3_lady_5","Jeanne de Béthune","Jeanne de Béthune",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_b_turnshoes_1,itm_a_woman_court_dress_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001410500436db6db6db6db6db001b6db6db6db6db0000000000000000],
["kingdom_3_lady_6","Jacqueline de Luxembourg","Jacqueline de Luxembourg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_b_turnshoes_1,itm_a_woman_court_dress_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000c00200347617538736a3472003dade29e7115220000000000000000],
["kingdom_3_lady_7","Marie de Hangest","Marie de Hangest",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_2 ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000040410044c947596d4caaa53003a76796b51c5250000000000000000],
["kingdom_3_lady_8","Agnès de Saulx ","Agnès de Saulx ",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_3], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003008000232c3c6a8628f48a3003b4f5f5a2837140000000000000000],
["kingdom_3_lady_9","Catherine d'Anguissola","Catherine d'Anguissola",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_b_turnshoes_1,itm_a_woman_court_dress_3 ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000f7500500344ecaa34db75b962000000001808b9530000000000000000],
["kingdom_3_lady_10","Jeanne de Vallangoujard","Jeanne de Vallangoujard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_b_turnshoes_1,itm_a_woman_court_dress_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006ec10600148636eb33c35590a003c8cc925b1e6dc0000000000000000],

["kingdom_3_lady_11","Marie-Marguerite de Montagu","Marie-Marguerite de Montagu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [itm_b_turnshoes_1,itm_a_woman_court_dress_1 ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000e08000232c3c6a8628f48a3003b4f5f5a2837140000000000000000],
["kingdom_3_lady_12","Marie du Bois","Marie du Bois",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_2],   def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e4d083001373366653579bd09003d75569d52dacf0000000000000000],
["kingdom_3_lady_13","Jacqueline d'Amboise","Jacqueline d'Amboise",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_3 ],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004b90c4001379dd64924b6d6dc0038012a180ed51a0000000000000000],
["kingdom_3_lady_14","Guillemette de Vienne","Guillemette de Vienne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_4 ],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001a0c4006376d8e3ae2a9cb1c003bb2e5542dc96d0000000000000000],
["kingdom_3_lady_15","Pernelle de Villiers de L'Isle-Adam","Pernelle de Villiers de L'Isle-Adam",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_6],   def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003d10100537238ec6e3b5c8e6003a8c552b6e56d30000000000000000],
["kingdom_3_lady_16","Marie d'Auvergne", "Marie d'Auvergne", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_5], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000cc3105002349cb69a9352d4eb00358eaf1cab44e30000000000000000 ],
["kingdom_3_lady_17","Marie de Roubaix", "Marie de Roubaix",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_b_turnshoes_1,itm_a_woman_court_dress_4 ],       def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000aa600400238cdadb8d456a2da003b32db65b1c6bb0000000000000000],
["kingdom_3_lady_18","Marie de Lalaing","Marie de Lalaing",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_b_turnshoes_1,itm_a_woman_court_dress_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007730810022b0c89a8eace2b22003e9194d650c6fa0000000000000000],
["kingdom_3_lady_19","Margaretha van der Clite","Margaretha van der Clite",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_1],   def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005ea0c000238dccd88a49a3adb00299364b371bca20000000000000000],
["kingdom_3_lady_20","Ermengarde de Rougemont","Ermengarde de Rougemont",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_2],   def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001c041001271d4517018dbae600238daaa2798aaa0000000000000000],

["kingdom_3_lady_21","Marianne de Brimeu","Marianne de Brimeu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_2],   def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010100516526cb7514e12da003a322f1dacb6e80000000000000000],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC BRETON LADIES ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["kingdom_4_lady_1","Marguerite de Bourgogne","Marguerite de Bourgogne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [  itm_b_turnshoes_1,itm_a_woman_court_dress_1     ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000062f084001679c71ace4664b25003a6c98aa8d390c0000000000000000],
["kingdom_4_lady_2","Marguerite d'Orléans","Marguerite d'Orléans",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [  itm_b_turnshoes_1,itm_a_woman_court_dress_2     ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000014c1020022935656b62ae4ced003d51576b6ca90a0000000000000000],
["kingdom_4_lady_3","Marguerite de Malestroit","Marguerite de Malestroit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_3    ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000a660410033452cd2b254626a5003c6538e492b5130000000000000000],
["kingdom_4_lady_4","Sibylle le Voyer","Sibylle le Voyer",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_b_turnshoes_1,itm_a_woman_court_dress_4  ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ba300200247204acaeb6a1b1200000000001236620000000000000000],
["kingdom_4_lady_5","Jeanne de France","Jeanne de France",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [   itm_b_turnshoes_1,itm_a_woman_court_dress_5    ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000280840023b0b6dc6b2cdb2bc00398db8647d96d30000000000000000],
["kingdom_4_lady_6","Jeanne de Rohan","Jeanne de Rohan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [     itm_b_turnshoes_1,itm_a_woman_court_dress_6  ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000280840023b0b6dc6b2cdb28c00398db8647d96d30000000000000000],
["kingdom_4_lady_7","Plézan Taupin","Plézan Taupin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_b_turnshoes_1,itm_a_woman_court_dress_5  ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008d70c4004296d72e3636a457400135657ad79c69d0000000000000000],
["kingdom_4_lady_8","Isabelle de Bretagne","Isabelle de Bretagne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [  itm_b_turnshoes_1,itm_a_woman_court_dress_2    ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000c0c400224db354491663a8b003d9144d3a649250000000000000000],
["kingdom_4_lady_9","Jacquette de Bretagne","Jacquette de Bretagne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [  itm_b_turnshoes_1,itm_a_woman_court_dress_1    ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002b0c40011921c5c71a4e1d1e003f48a6d18d28e20000000000000000],
["kingdom_4_lady_10","Katell Penmarc'h","Katell Penmarc'h",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_b_turnshoes_1,itm_a_woman_court_dress_2 ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001800c100458da85925ac5b532003a55b5245a1b500000000000000000],

["kingdom_4_lady_11","Catherine du Guesclin","Catherine du Guesclin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_3     ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000d3a1020035911a9171a6b548c003d5a36d355b9150000000000000000],
["kingdom_4_lady_12","Gwendoline de Coëtquen","Gwendoline de Coëtquen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [   itm_b_turnshoes_1,itm_a_woman_court_dress_4   ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000222105005384bb4d8917529a2003b523b616db9e30000000000000000],
["kingdom_4_lady_13","Jeanne de Lespervez","Jeanne de Lespervez",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [    itm_b_turnshoes_1,itm_a_woman_court_dress_5   ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005b10000014ae245c7236a68e2003c91bc9caa692b0000000000000000],
["kingdom_4_lady_14","Marie de Bretagne","Marie de Bretagne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [   itm_b_turnshoes_1,itm_a_woman_court_dress_6    ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000080410035b238d535629d86a003b51a84b769b1d0000000000000000],
["kingdom_4_lady_15","Marie de Surgères","Marie de Surgères",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001711020065b0c6dbb224e42e3003b4da7126e231b0000000000000000],
["kingdom_4_lady_16","Catherine de Rohan","Catherine de Rohan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [ itm_b_turnshoes_1,itm_a_woman_court_dress_2     ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000070c600536db6db6db6db6db001b6db6db6db6db0000000000000000],
["kingdom_4_lady_17","Marguerite de Châteaugiron-Malestroit","Marguerite de Châteaugiron-Malestroit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [       itm_b_turnshoes_1,itm_a_woman_court_dress_3 ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000009f11010032cab7147239322a2001a6ac8f491d3130000000000000000],
["kingdom_4_lady_18","Jeanne du Plessis-Anger","Jeanne du Plessis-Anger",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [       itm_b_turnshoes_1,itm_a_woman_court_dress_3],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000027c0c100258dbb12d23865b16003e892aaf452acc0000000000000000],

["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],


#Seneschals
["french_town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00159222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00259222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003f0025c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000400246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000410146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000810146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000910146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000a0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000b0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000e0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000100c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901110146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901210146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900114046da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900214146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900218146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900318146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900418246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900518346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900818346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190081c436db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_23_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00159222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_24_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00259222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_25_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003f0025c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_26_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000400246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_27_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000410146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_28_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000810146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["french_town_29_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000910146da8e3b1c81b91b00000000001db6db0000000000000000 ],

["english_town_1_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000a0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_2_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000b0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_3_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000e0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_4_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000100c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_5_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901110146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_6_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901210146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_7_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900114046da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_8_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900214146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_9_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900218146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_10_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900318146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_11_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900418246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_12_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900518346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_13_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900818346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_14_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190081c436db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_15_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_16_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00159222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_17_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00259222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_18_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003f0025c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_19_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000400246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_20_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000410146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_21_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000810146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["english_town_22_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000910146da8e3b1c81b91b00000000001db6db0000000000000000 ],

["burgundian_town_1_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000a0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_2_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000b0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_3_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000e0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_4_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000100c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_5_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901110146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_6_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901210146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_7_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900114046da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_8_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900214146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_9_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900218146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_10_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900318146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_11_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900418246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_12_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900518346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_13_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900818346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_14_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00159222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["burgundian_town_15_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00159222da8e3b1c81b91b00000000001db6db0000000000000000 ],

["breton_town_1_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00259222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_2_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003f0025c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_3_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000400246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_4_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000410146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_5_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000810146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_6_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000910146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_7_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000a0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["breton_town_8_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000000000b0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],

# Castle Seneschals
["french_castle_1_seneschal",  "{!}Castle Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_2_seneschal",  "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900920536db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_3_seneschal",  "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900a20536db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_4_seneschal",  "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900b20546db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_5_seneschal",  "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900c24546db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_6_seneschal",  "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900e24646db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_7_seneschal",  "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901028646db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_8_seneschal",  "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901128746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_9_seneschal",  "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_10_seneschal", "{!}Castle Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190012c746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_11_seneschal", "{!}Castle Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190022c746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_12_seneschal", "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190032c746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_13_seneschal", "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190042c746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_14_seneschal", "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190052c746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_15_seneschal", "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900630746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_16_seneschal", "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_17_seneschal", "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900930746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_18_seneschal", "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900a30746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_19_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900b30746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_20_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900c30746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_21_seneschal", "{!}Castle Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900e34746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_22_seneschal", "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901034746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_23_seneschal", "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901134746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_24_seneschal", "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901234746db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_25_seneschal", "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_26_seneschal", "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_27_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_28_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_29_seneschal", "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_30_seneschal", "{!}Castle Seneschal", "{!}Castle 30 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_31_seneschal", "{!}Castle Seneschal", "{!}Castle 31 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["french_castle_32_seneschal", "{!}Castle Seneschal", "{!}Castle 32 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],

["english_castle_1_seneschal",  "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900238846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_2_seneschal",  "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900338846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_3_seneschal",  "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900438846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_4_seneschal",  "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900538846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_5_seneschal",  "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900838846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_6_seneschal",  "{!}Castle Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900938846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_7_seneschal",  "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900a38846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_8_seneschal",  "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900b38846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_9_seneschal",  "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900c38846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_10_seneschal", "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900e38846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_11_seneschal", "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000001038846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_12_seneschal", "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000001138846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_13_seneschal", "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000001238846db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_14_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000013cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_15_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000023cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_16_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000033cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_17_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000043cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_18_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000053cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_19_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000083cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_20_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000093cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_21_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000a3cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_22_seneschal", "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000a3cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_23_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_24_seneschal", "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],
["english_castle_25_seneschal", "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],

["burgundian_castle_1_seneschal",  "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000b3cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_2_seneschal",  "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000000000c3cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_3_seneschal",  "{!}Castle Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_4_seneschal",  "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900920536db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_5_seneschal",  "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900a20536db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_6_seneschal",  "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900b20546db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_7_seneschal",  "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900c24546db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_8_seneschal",  "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900e24646db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_9_seneschal",  "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901028646db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_10_seneschal", "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901128746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_11_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_12_seneschal", "{!}Castle Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190012c746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_13_seneschal", "{!}Castle Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190022c746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_14_seneschal", "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190032c746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_15_seneschal", "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190042c746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_16_seneschal", "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190052c746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_17_seneschal", "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900630746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_18_seneschal", "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_19_seneschal", "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_20_seneschal", "{!}Castle Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_21_seneschal", "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_castle_22_seneschal", "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],

["breton_castle_1_seneschal",  "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900930746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_2_seneschal",  "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900a30746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_3_seneschal",  "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900b30746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_4_seneschal",  "{!}Castle Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900c30746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_5_seneschal",  "{!}Castle Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900e34746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_6_seneschal",  "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901034746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_7_seneschal",  "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901134746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_8_seneschal",  "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901234746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_9_seneschal",  "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_10_seneschal", "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900238846db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_11_seneschal", "{!}Castle Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_12_seneschal", "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900920536db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_13_seneschal", "{!}Castle Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900a20536db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_14_seneschal", "{!}Castle Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900b20546db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_15_seneschal", "{!}Castle Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900c24546db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_16_seneschal", "{!}Castle Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001900e24646db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_17_seneschal", "{!}Castle Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901028646db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_18_seneschal", "{!}Castle Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901128746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_19_seneschal", "{!}Castle Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_20_seneschal", "{!}Castle Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190012c746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_21_seneschal", "{!}Castle Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190022c746db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_castle_22_seneschal", "{!}Castle Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000190032c746db6db6db6db6db00000000001db6db0000000000000000 ],

#Arena Masters
["french_town_1_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_1_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901044b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_2_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_2_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_3_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_3_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_4_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_4_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901148b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_5_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_5_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_6_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_6_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000003900148d46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_7_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_7_arena|entry(52),reserved,   fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_8_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_8_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000044cf46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_9_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_9_arena|entry(52),reserved,   fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_10_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_10_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000054d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_11_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_11_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_12_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_12_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_13_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_13_arena|entry(52),reserved,  fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_14_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_14_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_15_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_15_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_16_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_16_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1 ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_17_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_17_arena|entry(52),reserved,  fac_commoners,[itm_a_commoner_apron,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_18_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_18_arena|entry(52),reserved,  fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_19_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_19_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["french_town_20_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_20_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000000000084c046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_21_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_21_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_22_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_22_arena|entry(52), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_23_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_23_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901044b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_24_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_24_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_25_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_25_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_26_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_26_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901148b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_27_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_27_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["french_town_28_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_28_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000003900148d46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_29_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_french_town_29_arena|entry(52),reserved,   fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],

["english_town_1_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_1_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000044cf46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_2_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_2_arena|entry(52),reserved,   fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_3_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_3_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000054d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_4_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_4_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_5_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_5_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_6_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_6_arena|entry(52),reserved,  fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_7_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_7_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_8_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_8_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_9_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_9_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1 ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_10_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_10_arena|entry(52),reserved,  fac_commoners,[itm_a_commoner_apron,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_11_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_11_arena|entry(52),reserved,  fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_12_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_12_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["english_town_13_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_13_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000000000084c046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_14_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_14_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["english_town_15_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_15_arena|entry(52), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["english_town_16_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_16_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901044b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_17_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_17_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["english_town_18_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_18_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["english_town_19_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_19_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901148b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_20_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_20_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["english_town_21_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_21_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000003900148d46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_22_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_english_town_22_arena|entry(52),reserved,   fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],

["burgundian_town_1_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_1_arena|entry(52),reserved,   fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_2_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_2_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000054d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_3_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_3_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_4_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_4_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_5_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_5_arena|entry(52),reserved,  fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_6_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_6_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_7_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_7_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_8_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_8_arena|entry(52),reserved,  fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1 ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_9_arena_master",  "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_9_arena|entry(52),reserved,  fac_commoners,[itm_a_commoner_apron,itm_b_high_boots_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_10_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_10_arena|entry(52),reserved,  fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_11_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_11_arena|entry(52),reserved,  fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["burgundian_town_12_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_12_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000000000084c046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_13_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_13_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901044b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_14_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_14_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000044cf46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_15_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_burgundian_town_14_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000044cf46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],

["breton_town_1_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_1_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["breton_town_2_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_2_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["breton_town_3_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_3_arena|entry(52), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003901148b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_4_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_4_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["breton_town_5_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_5_arena|entry(52), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000003900148d46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_6_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_6_arena|entry(52),reserved,   fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["breton_town_7_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_7_arena|entry(52), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000000000044cf46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_8_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_breton_town_8_arena|entry(52),reserved,   fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_b_turnshoes_1          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_b_turnshoes_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_b_turnshoes_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_b_turnshoes_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_b_turnshoes_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
#arena_masters_end = zendar_armorer

["french_town_1_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000094c046db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_2_armorer",  "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000002b04400204d4b114ddae4515003b92aa9d89a9220000000000000000, 0x000000002b04400204d4b114ddae4515003b92aa9d89a9220000000000000000 ],
["french_town_3_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_4_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1,itm_h_highlander_beret_brown], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0114c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_5_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_hunter_coat_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_6_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0124c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_7_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_8_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_coat], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0014c246db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_9_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_10_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_1,itm_a_commoner_apron], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_11_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_12_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1,itm_h_highlander_beret_black], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00850346db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_13_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_14_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_15_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_16_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_17_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_18_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000000220c200738548c559dad196c00339959646f4cd40000000000000000, 0x00000000220c200738548c559dad196c00339959646f4cd40000000000000000 ],
["french_town_19_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_20_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_white,itm_h_highlander_beret_white,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_21_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00950446db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_22_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0c60035b2ed2c6dc5218dd003ba6389230b3540000000000000000, 0x000000003f0c60035b2ed2c6dc5218dd003ba6389230b3540000000000000000 ],
["french_town_23_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000094c046db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_24_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000370840024713ba48ac2dd86c000c71aed3d6b8e90000000000000000, 0x00000000370840024713ba48ac2dd86c000c71aed3d6b8e90000000000000000 ],
["french_town_25_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_26_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1,itm_h_highlander_beret_brown], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0114c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_27_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_hunter_coat_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_28_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0124c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_29_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

["english_town_1_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_coat], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0014c246db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_2_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_3_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_1,itm_a_commoner_apron], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_4_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_5_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1,itm_h_highlander_beret_black], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00850346db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_6_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_7_armorer",  "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_8_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_9_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_10_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_11_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000000370840024713ba48ac2dd86c000c71aed3d6b8e90000000000000000, 0x00000000370840024713ba48ac2dd86c000c71aed3d6b8e90000000000000000 ],
["english_town_12_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_13_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_white,itm_h_highlander_beret_white,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_14_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00950446db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_15_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006a8085003689e4a52e345d6dc003a53468465dc090000000000000000, 0x00000006a8085003689e4a52e345d6dc003a53468465dc090000000000000000 ],
["english_town_16_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000094c046db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_17_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000069d04400118dd85c9b35b5912001a3138a169d30c0000000000000000, 0x000000069d04400118dd85c9b35b5912001a3138a169d30c0000000000000000 ],
["english_town_18_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_19_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1,itm_h_highlander_beret_brown], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0114c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_20_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_hunter_coat_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_21_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0124c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_22_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

["burgundian_town_1_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_coat], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0014c246db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_2_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_3_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_1,itm_a_commoner_apron], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_4_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_5_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1,itm_h_highlander_beret_black], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00850346db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_6_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_7_armorer",  "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_8_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_9_armorer",  "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_10_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_11_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000069e00100228cb8ea99c32c75a001bb2a70a6537210000000000000000, 0x000000069e00100228cb8ea99c32c75a001bb2a70a6537210000000000000000 ],
["burgundian_town_12_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_light_gambeson_long_sleeves_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_13_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_noble_shirt_white,itm_h_highlander_beret_white,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_14_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000094c046db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_15_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000094c046db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["breton_town_1_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_man_custom], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000006bb08300128ac76bae265a72c003c9636a484d7340000000000000000, 0x00000006bb08300128ac76bae265a72c003c9636a484d7340000000000000000 ],
["breton_town_2_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_3_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_high_boots_1,itm_h_highlander_beret_brown], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0114c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_4_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_hunter_coat_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_5_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0124c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_6_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_7_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_b_turnshoes_2,itm_a_peasant_coat], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0014c246db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_8_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

# Weapon merchants

["french_town_1_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_2_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00c00546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_3_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00e08546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_4_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_5_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_6_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_7_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00f18546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_8_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006b5081005352b72c70dcab993003b25131d51475c0000000000000000, 0x00000006b5081005352b72c70dcab993003b25131d51475c0000000000000000 ],
["french_town_9_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_10_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_11_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_12_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_13_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_14_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_15_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_16_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000043f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_17_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_18_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_19_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_20_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_21_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_22_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_23_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_24_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00c00546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_25_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00e08546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_26_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_27_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_28_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_29_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00f18546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["english_town_1_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006800c5002125bb9c30cae5b5c003c91165650b6e00000000000000000, 0x00000006800c5002125bb9c30cae5b5c003c91165650b6e00000000000000000 ],
["english_town_2_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_3_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_4_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_5_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_6_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_7_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_8_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_9_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000043f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_10_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_11_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_12_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_13_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_14_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_15_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_16_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_17_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00c00546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_18_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00e08546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_19_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_20_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_21_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_22_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00f18546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["burgundian_town_1_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006b700300426966a53ac4a4669001349d624914b420000000000000000, 0x00000006b700300426966a53ac4a4669001349d624914b420000000000000000 ],
["burgundian_town_2_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_3_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_4_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_5_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_6_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_7_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_8_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_9_weaponsmith",  "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000043f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_10_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_11_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_12_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_13_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_14_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_15_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_white,itm_a_peasant_coat,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],

["breton_town_1_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00c00546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_2_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00e08546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_3_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_4_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_5_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_6_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00f18546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_7_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006af08600238936f475cb148db001d84c4f285325a0000000000000000, 0x00000006af08600238936f475cb148db001d84c4f285325a0000000000000000 ],
["breton_town_8_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

#Tavern keepers
["french_town_1_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_1_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_2_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_2_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01114546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_3_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_3_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006a50860052a5e6db6dbaeb523001b89c91c564acc0000000000000000, 0x00000006a50860052a5e6db6dbaeb523001b89c91c564acc0000000000000000 ],
["french_town_4_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_4_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0120c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_5_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_5_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_6_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_6_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000069f0840072c754ab6aa9a971800194dc6616d355c0000000000000000, 0x000000069f0840072c754ab6aa9a971800194dc6616d355c0000000000000000 ],
["french_town_7_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_7_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006a500100524e4ef2b9375b79c000570c3138f2b4a0000000000000000, 0x00000006a500100524e4ef2b9375b79c000570c3138f2b4a0000000000000000 ],
["french_town_8_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_8_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0010c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_9_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_9_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_10_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_10_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000068b086001149666397175aee4001a92251455a8690000000000000000, 0x000000068b086001149666397175aee4001a92251455a8690000000000000000 ],
["french_town_11_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_11_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000068708500516e3cf13a34a2ae2002d55b69b8eaad10000000000000000, 0x000000068708500516e3cf13a34a2ae2002d55b69b8eaad10000000000000000 ],
["french_town_12_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_12_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_13_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_13_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006ab00000324d9b139a189a9d2000bd936e58dd8ea0000000000000000, 0x00000006ab00000324d9b139a189a9d2000bd936e58dd8ea0000000000000000 ],
["french_town_14_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_14_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0111cd46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_15_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_15_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_16_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_16_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_17_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_17_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_18_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_18_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0121cf46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_19_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_19_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006bd10300518bc99b936764913001d89291a8ca6940000000000000000, 0x00000006bd10300518bc99b936764913001d89291a8ca6940000000000000000 ],
["french_town_20_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_20_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_21_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_21_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_22_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_22_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_23_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_23_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_24_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_24_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01114546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_25_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_25_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006b708100236636ca6b37298a300249986c632251b0000000000000000, 0x00000006b708100236636ca6b37298a300249986c632251b0000000000000000 ],
["french_town_26_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_26_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0120c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_27_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_french_town_27_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["french_town_28_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_28_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000069600400248b38b5c9349b6f4001c5a56a44d32a70000000000000000, 0x000000069600400248b38b5c9349b6f4001c5a56a44d32a70000000000000000 ],
["french_town_29_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_french_town_29_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006bd0c400458c291c7256a4311001bb0dd746b299a0000000000000000, 0x00000006bd0c400458c291c7256a4311001bb0dd746b299a0000000000000000 ],

["english_town_1_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,            scn_english_town_1_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0010c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_2_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_english_town_2_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_3_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_english_town_3_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000068c045007232b7e672ed24aa2002b5a50913279280000000000000000, 0x000000068c045007232b7e672ed24aa2002b5a50913279280000000000000000 ],
["english_town_4_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_english_town_4_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006b810500138d0549b11d13acb002b72629379a4d90000000000000000, 0x00000006b810500138d0549b11d13acb002b72629379a4d90000000000000000 ],
["english_town_5_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,            scn_english_town_5_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_6_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_english_town_6_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006940c00054afd2cb9324e385b000e72525c6ecadc0000000000000000, 0x00000006940c00054afd2cb9324e385b000e72525c6ecadc0000000000000000 ],
["english_town_7_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,            scn_english_town_7_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0111cd46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_8_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_english_town_8_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_9_tavernkeeper",  "Tavern_Keeper",  "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,            scn_english_town_9_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_10_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_english_town_10_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_11_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_11_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0121cf46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_12_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_english_town_12_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006910460074aa3c4c72c7a295e002e455712adba920000000000000000, 0x00000006910460074aa3c4c72c7a295e002e455712adba920000000000000000 ],
["english_town_13_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,             scn_english_town_13_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_14_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_english_town_14_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_15_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,             scn_english_town_15_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_16_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,             scn_english_town_16_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_17_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,             scn_english_town_17_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01114546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_18_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_english_town_18_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000068610400616db513551ad6ad400139128dcb9a89b0000000000000000, 0x000000068610400616db513551ad6ad400139128dcb9a89b0000000000000000 ],
["english_town_19_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,             scn_english_town_19_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0120c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_20_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,             scn_english_town_20_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["english_town_21_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_english_town_21_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000069104100446e5acd4e5c5a8a2002a8296645138cb0000000000000000, 0x000000069104100446e5acd4e5c5a8a2002a8296645138cb0000000000000000 ],
["english_town_22_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_english_town_22_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006be00200466935493328acd530033313c6d7239340000000000000000, 0x00000006be00200466935493328acd530033313c6d7239340000000000000000 ],

["burgundian_town_1_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_1_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0010c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_2_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_2_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_3_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_3_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006b61020055a5cb6a6f38e28a4002a921aa3b0c5750000000000000000, 0x00000006b61020055a5cb6a6f38e28a4002a921aa3b0c5750000000000000000 ],
["burgundian_town_4_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_4_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000068b1040023b226e386e6a575e0035ae472436d85c0000000000000000, 0x000000068b1040023b226e386e6a575e0035ae472436d85c0000000000000000 ],
["burgundian_town_5_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_5_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_6_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_6_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006b610300234b7ae58e36536da001e92c8d3adcae50000000000000000, 0x00000006b610300234b7ae58e36536da001e92c8d3adcae50000000000000000 ],
["burgundian_town_7_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_7_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0111cd46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_8_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_8_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_9_tavernkeeper",  "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_9_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_10_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_10_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_11_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_11_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0121cf46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_12_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,    scn_burgundian_town_12_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000069b1050044774a936a24e54d1001b9894547c87620000000000000000, 0x000000069b1050044774a936a24e54d1001b9894547c87620000000000000000 ],
["burgundian_town_13_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_13_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["burgundian_town_14_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_14_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_15_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,              scn_burgundian_town_14_tavern|entry(9), reserved, fac_commoners, [itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["breton_town_1_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,           scn_breton_town_1_tavern|entry(9), reserved, fac_commoners, [itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01114546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_2_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_breton_town_2_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006a6101005374495bb1b2d9cdc000d4a0162b985120000000000000000, 0x00000006a6101005374495bb1b2d9cdc000d4a0162b985120000000000000000 ],
["breton_town_3_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,           scn_breton_town_3_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0120c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_4_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,           scn_breton_town_4_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_black,itm_a_commoner_apron,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["breton_town_5_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_breton_town_5_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_tavern_keeper_shirt,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006bf002002451c46357537369d003badb96c4e171c0000000000000000, 0x00000006bf002002451c46357537369d003badb96c4e171c0000000000000000 ],
["breton_town_6_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_breton_town_6_tavern|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_peasant_cote_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006830000024f536b49a22524a5002191d664b1371d0000000000000000, 0x00000006830000024f536b49a22524a5002191d664b1371d0000000000000000 ],
["breton_town_7_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face,           scn_breton_town_7_tavern|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0010c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_8_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_breton_town_8_tavern|entry(9), reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],

#Goods Merchants
["french_town_1_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_1_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f01221046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_2_merchant",  "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_french_town_2_store|entry(9),0, fac_commoners,     [itm_a_merchant_outfit,itm_b_turnshoes_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_3_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_3_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_4_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_4_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f00125046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_5_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_5_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_6_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_6_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_7_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_7_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00229046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_8_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_8_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f0052d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_9_merchant",  "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_french_town_9_store|entry(9),0, fac_commoners,     [ itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_10_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_french_town_10_store|entry(9),0, fac_commoners,    [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_11_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_11_store|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00830146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_12_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_12_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_13_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_13_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_14_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_14_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00b34146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_15_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_15_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_16_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_16_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_17_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_17_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_18_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_18_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00c40146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_19_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_french_town_19_store|entry(9),0, fac_commoners,    [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_20_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_20_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_21_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_21_store|entry(9), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_22_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_22_store|entry(9), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00e44146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_23_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_23_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f01221046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_24_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_french_town_24_store|entry(9),0, fac_commoners,     [itm_a_merchant_outfit,itm_b_turnshoes_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_25_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_25_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_26_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_26_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f00125046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_27_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_27_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_28_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_french_town_28_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["french_town_29_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_french_town_29_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00229046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],

["english_town_1_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_1_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f0052d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_2_merchant",  "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,   scn_english_town_2_store|entry(9),0, fac_commoners,     [ itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_3_merchant",  "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,   scn_english_town_3_store|entry(9),0, fac_commoners,    [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_4_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_4_store|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00830146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_5_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_5_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_6_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_6_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_7_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_7_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00b34146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_8_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_8_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["english_town_9_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_9_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_10_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_10_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_11_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_11_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00c40146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_12_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,   scn_english_town_12_store|entry(9),0, fac_commoners,    [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_13_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_13_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_14_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_14_store|entry(9), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_15_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_15_store|entry(9), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00e44146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_16_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_16_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f01221046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_17_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,   scn_english_town_17_store|entry(9),0, fac_commoners,     [itm_a_merchant_outfit,itm_b_turnshoes_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_18_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_18_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_19_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_19_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f00125046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_20_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_20_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["english_town_21_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_english_town_21_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["english_town_22_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,           scn_english_town_22_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00229046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],

["burgundian_town_1_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_1_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f0052d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_2_merchant",  "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_burgundian_town_2_store|entry(9),0, fac_commoners,     [ itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_3_merchant",  "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_burgundian_town_3_store|entry(9),0, fac_commoners,    [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_4_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_4_store|entry(9), reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00830146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_5_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_burgundian_town_5_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_6_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_burgundian_town_6_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_brown,itm_a_noble_shirt_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_7_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_7_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00b34146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_8_merchant",  "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_8_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["burgundian_town_9_merchant",  "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_burgundian_town_9_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_10_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_burgundian_town_10_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_11_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_11_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00c40146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_12_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_burgundian_town_12_store|entry(9),0, fac_commoners,    [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_13_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,  scn_burgundian_town_13_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["burgundian_town_14_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_14_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f01221046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_15_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,            scn_burgundian_town_14_store|entry(9), reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f01221046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],

["breton_town_1_merchant", "Merchant", "{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_breton_town_1_store|entry(9),0, fac_commoners,     [itm_a_merchant_outfit,itm_b_turnshoes_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["breton_town_2_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_breton_town_2_store|entry(9), reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["breton_town_3_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,             scn_breton_town_3_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f00125046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_4_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,             scn_breton_town_4_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_green,itm_a_noble_shirt_green,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["breton_town_5_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face,   scn_breton_town_5_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["breton_town_6_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,             scn_breton_town_6_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00229046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_7_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face,             scn_breton_town_7_store|entry(9), reserved, fac_commoners, [itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f0052d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_8_merchant", "Merchant", "{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant,    scn_breton_town_8_store|entry(9),0, fac_commoners,     [ itm_h_highlander_beret_red,itm_a_noble_shirt_red,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

["salt_mine_merchant", "Barezan", "Barezan", tf_hero|tf_is_merchant, scn_salt_mine|entry(1), reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6 ],

# Horse Merchants

["french_town_1_horse_merchant",  "Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],   def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000006a41010012697a8b4abcde6b70034b6c842b6369e0000000000000000, 0x00000006a41010012697a8b4abcde6b70034b6c842b6369e0000000000000000],
["french_town_2_horse_merchant",  "Horse Merchant", "{!}Town 2 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00f44148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_3_horse_merchant",  "Horse Merchant", "{!}Town 3 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_4_horse_merchant",  "Horse Merchant", "{!}Town 4 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01044148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_5_horse_merchant",  "Horse Merchant", "{!}Town 5 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000683046006285bbad9659544ed002cd11ae54e452d0000000000000000, 0x0000000683046006285bbad9659544ed002cd11ae54e452d0000000000000000 ],
["french_town_6_horse_merchant",  "Horse Merchant", "{!}Town 6 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01148248db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_7_horse_merchant",  "Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_8_horse_merchant",  "Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_peasant_coat,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_9_horse_merchant",  "Horse Merchant", "{!}Town 9 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01248348db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_10_horse_merchant", "Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000006bd002007386a4d564c2d3499001d39b69a6cd4db0000000000000000, 0x00000006bd002007386a4d564c2d3499001d39b69a6cd4db0000000000000000],
["french_town_11_horse_merchant", "Horse Merchant", "{!}Town 11 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_12_horse_merchant", "Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_13_horse_merchant", "Horse Merchant", "{!}Town 13 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00148448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_14_horse_merchant", "Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["french_town_15_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff0025c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_16_horse_merchant", "Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_17_horse_merchant", "Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["french_town_18_horse_merchant", "Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2 ],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000006b80410035d6a79b6cbaa3ae1000db1364b99aa620000000000000000, 0x00000006b80410035d6a79b6cbaa3ae1000db1364b99aa620000000000000000],
["french_town_19_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000000000115c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_20_horse_merchant", "Horse Merchant", "{!}Town 16 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_21_horse_merchant", "Horse Merchant", "{!}Town 17 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_22_horse_merchant", "Horse Merchant", "{!}Town 18 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000068700500736cb4a9ca2adb71a002c9642fc2dd6640000000000000000, 0x000000068700500736cb4a9ca2adb71a002c9642fc2dd6640000000000000000 ],
["french_town_23_horse_merchant", "Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],   def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000006b70420013a6985464b6a2656000bd6595b6927490000000000000000, 0x00000006b70420013a6985464b6a2656000bd6595b6927490000000000000000],
["french_town_24_horse_merchant", "Horse Merchant", "{!}Town 2 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00f44148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_25_horse_merchant", "Horse Merchant", "{!}Town 3 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["french_town_26_horse_merchant", "Horse Merchant", "{!}Town 4 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01044148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_27_horse_merchant", "Horse Merchant", "{!}Town 5 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006bc04200614dd65969aaaa561003c2ea8e472a95d0000000000000000, 0x00000006bc04200614dd65969aaaa561003c2ea8e472a95d0000000000000000 ],
["french_town_28_horse_merchant", "Horse Merchant", "{!}Town 6 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01148248db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_town_29_horse_merchant", "Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

["english_town_1_horse_merchant",  "Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_peasant_coat,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_2_horse_merchant",  "Horse Merchant", "{!}Town 9 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01248348db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_3_horse_merchant",  "Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000006ab046006537569279275a8f3001a4a5512b5ab120000000000000000, 0x00000006ab046006537569279275a8f3001a4a5512b5ab120000000000000000],
["english_town_4_horse_merchant",  "Horse Merchant", "{!}Town 11 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["english_town_5_horse_merchant",  "Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_6_horse_merchant",  "Horse Merchant", "{!}Town 13 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00148448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_7_horse_merchant",  "Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["english_town_8_horse_merchant",  "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff0025c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_9_horse_merchant",  "Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_10_horse_merchant", "Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["english_town_11_horse_merchant", "Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2 ],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000006a6104007519d9158d449a4f20018d1c55a76349d0000000000000000, 0x00000006a6104007519d9158d449a4f20018d1c55a76349d0000000000000000],
["english_town_12_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000000000115c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_13_horse_merchant", "Horse Merchant", "{!}Town 16 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["english_town_14_horse_merchant", "Horse Merchant", "{!}Town 17 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["english_town_15_horse_merchant", "Horse Merchant", "{!}Town 18 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006a10c000218e4a9d50c86378a002d2a2cad65229c0000000000000000, 0x00000006a10c000218e4a9d50c86378a002d2a2cad65229c0000000000000000 ],
["english_town_16_horse_merchant", "Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],   def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000006a3005005326a8a3cdbaeb714002129b9dd6da6e30000000000000000, 0x00000006a3005005326a8a3cdbaeb714002129b9dd6da6e30000000000000000],
["english_town_17_horse_merchant", "Horse Merchant", "{!}Town 2 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00f44148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_18_horse_merchant", "Horse Merchant", "{!}Town 3 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["english_town_19_horse_merchant", "Horse Merchant", "{!}Town 4 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01044148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_20_horse_merchant", "Horse Merchant", "{!}Town 5 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006b40440014ac645a2f929485b001111c56256b6de0000000000000000, 0x00000006b40440014ac645a2f929485b001111c56256b6de0000000000000000 ],
["english_town_21_horse_merchant", "Horse Merchant", "{!}Town 6 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01148248db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_town_22_horse_merchant", "Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

["burgundian_town_1_horse_merchant",  "Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_peasant_coat,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_2_horse_merchant",  "Horse Merchant", "{!}Town 9 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01248348db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_3_horse_merchant",  "Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000691106006495b8dd2648a34b3002a6db2e446b90e0000000000000000, 0x0000000691106006495b8dd2648a34b3002a6db2e446b90e0000000000000000],
["burgundian_town_4_horse_merchant",  "Horse Merchant", "{!}Town 11 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["burgundian_town_5_horse_merchant",  "Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_6_horse_merchant",  "Horse Merchant", "{!}Town 13 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00148448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_7_horse_merchant",  "Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["burgundian_town_8_horse_merchant",  "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff0025c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_9_horse_merchant",  "Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_10_horse_merchant", "Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_h_highlander_beret_white,itm_a_noble_shirt_white,itm_b_turnshoes_2],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["burgundian_town_11_horse_merchant", "Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_turnshoes_2 ],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000693003001651db6a58d5246e3002d46ab5471b94a0000000000000000, 0x0000000693003001651db6a58d5246e3002d46ab5471b94a0000000000000000],
["burgundian_town_12_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000000000115c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_town_13_horse_merchant", "Horse Merchant", "{!}Town 16 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["burgundian_town_14_horse_merchant", "Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],   def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000006a4044003279287a2d22ec6630013b5c6db5a37950000000000000000, 0x00000006a4044003279287a2d22ec6630013b5c6db5a37950000000000000000],
["burgundian_town_15_horse_merchant", "Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],   def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000006a4044003279287a2d22ec6630013b5c6db5a37950000000000000000, 0x00000006a4044003279287a2d22ec6630013b5c6db5a37950000000000000000],

["breton_town_1_horse_merchant", "Horse Merchant", "{!}Town 2 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00f44148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_2_horse_merchant", "Horse Merchant", "{!}Town 3 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_commoner_apron,itm_b_high_boots_1], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["breton_town_3_horse_merchant", "Horse Merchant", "{!}Town 4 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01044148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_4_horse_merchant", "Horse Merchant", "{!}Town 5 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_coat,itm_b_turnshoes_1], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000069808400755626cad1d47366100347138e39936930000000000000000, 0x000000069808400755626cad1d47366100347138e39936930000000000000000 ],
["breton_town_5_horse_merchant", "Horse Merchant", "{!}Town 6 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01148248db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_town_6_horse_merchant", "Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_tabard,itm_b_turnshoes_2],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["breton_town_7_horse_merchant", "Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_a_peasant_coat,itm_b_turnshoes_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["breton_town_8_horse_merchant", "Horse Merchant", "{!}Town 9 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_h_felt_hat_b_brown,itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01248348db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],

#Town Mayors    #     itm_rich_outfit
["french_town_1_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de0115c448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_2_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e01208448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_3_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e00110548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_4_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00210748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_5_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00318748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_6_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008c000410648db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_7_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000010000918548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_8_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000001310cb0cc5664a943216a231a00000000001638660000000000000000, mercenary_face_2 ],
["french_town_9_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_white,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000011400e0c036db6db6db6db6db00000000000db6db0000000000000000, mercenary_face_2 ],
["french_town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000006000100c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_blue,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000006140110c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a5401218036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_red,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a540001c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a4000120036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000c4000220136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000084000328136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008760052c136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600830236db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600934336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600a38336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600b3c336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_white,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600e40536db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de0115c448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_24_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e01208448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_25_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e00110548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_26_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00210748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_27_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00318748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_28_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008c000410648db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["french_town_29_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000010000918548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["english_town_1_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000001310cb0cc5664a943216a231a00000000001638660000000000000000, mercenary_face_2 ],
["english_town_2_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_white,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000011400e0c036db6db6db6db6db00000000000db6db0000000000000000, mercenary_face_2 ],
["english_town_3_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000006000100c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_4_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_blue,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000006140110c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_5_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a5401218036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_6_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_red,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a540001c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_7_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a4000120036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_8_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000c4000220136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_9_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000084000328136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008760052c136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600830236db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600934336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600a38336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600b3c336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_white,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600e40536db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de0115c448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e01208448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e00110548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00210748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00318748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008c000410648db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["english_town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000010000918548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["burgundian_town_1_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000001310cb0cc5664a943216a231a00000000001638660000000000000000, mercenary_face_2 ],
["burgundian_town_2_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_white,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000011400e0c036db6db6db6db6db00000000000db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_3_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000006000100c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_4_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_blue,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000006140110c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_5_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a5401218036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_6_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_white_2,itm_a_noble_shirt_red,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a540001c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_7_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000a4000120036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_8_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000c4000220136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_9_mayor",  "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000084000328136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008760052c136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600830236db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600934336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000087600a38336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de0115c448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["burgundian_town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_black,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de0115c448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],

["breton_town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_white,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e01208448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_black_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e00110548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_black,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00210748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_brown_2,itm_a_noble_shirt_brown,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x00000008de00318748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_red_2,itm_a_noble_shirt_red,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000008c000410648db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_green_2,itm_a_noble_shirt_green,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000010000918548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["breton_town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000001310cb0cc5664a943216a231a00000000001638660000000000000000, mercenary_face_2 ],
["breton_town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_h_highlander_beret_blue_2,itm_a_noble_shirt_white,itm_b_turnshoes_1], def_attrib|level(2), wp(20), knows_common, 0x000000011400e0c036db6db6db6db6db00000000000db6db0000000000000000, mercenary_face_2 ],


#Village stores
["french_village_1_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff601040536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_2_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_3_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600140536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_4_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["french_village_5_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["french_village_6_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["french_village_7_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["french_village_8_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["french_village_9_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600250536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_10_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_11_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["french_village_12_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_13_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["french_village_14_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_15_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["french_village_16_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_17_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_18_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_19_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["french_village_20_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_21_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_22_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_23_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["french_village_24_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600354636db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_25_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["french_village_26_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_27_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["french_village_28_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_29_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["french_village_30_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_31_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600454636db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_32_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_33_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_34_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_35_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_36_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["french_village_37_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600458736db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_38_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["french_village_39_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["french_village_40_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_41_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["french_village_42_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_43_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_44_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_45_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_46_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff60045c836db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_47_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_48_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["french_village_49_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["french_village_50_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_51_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_52_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["french_village_53_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["french_village_54_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["french_village_55_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_56_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_57_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_58_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_59_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_60_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_61_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_62_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_63_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_64_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_65_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600400966db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_66_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_67_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_68_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_69_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_70_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_71_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_72_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_73_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600500966db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["french_village_74_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_75_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_76_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_77_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_78_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_79_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_80_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["french_village_81_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],

["english_village_1_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_2_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_3_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_4_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_5_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_6_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_7_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_8_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_9_elder", "Village_Elder",  "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_10_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_11_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_12_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_13_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_14_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_15_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600500b66db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_16_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["english_village_17_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["english_village_18_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["english_village_19_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_20_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_21_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_22_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_23_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600400c66db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_24_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_25_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_26_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_27_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_28_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_29_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600401266db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_30_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_31_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_32_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_33_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_34_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_35_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600701366db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_36_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff601040536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_37_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_38_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600140536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_39_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["english_village_40_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["english_village_41_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_42_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_43_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["english_village_44_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600250536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_45_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_46_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_47_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_48_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["english_village_49_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_50_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["english_village_51_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_52_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_53_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_54_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["english_village_55_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["english_village_56_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_57_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_58_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["english_village_59_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600354636db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_60_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["english_village_61_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_62_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["english_village_63_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_64_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_65_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_66_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600454636db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_67_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_68_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_69_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["english_village_70_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["english_village_71_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_72_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600458736db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["english_village_73_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_74_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_75_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_76_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["english_village_77_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],

["burgundian_village_1_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["burgundian_village_2_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["burgundian_village_3_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["burgundian_village_4_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["burgundian_village_5_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["burgundian_village_6_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["burgundian_village_7_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["burgundian_village_8_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff60045c836db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_village_9_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["burgundian_village_10_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["burgundian_village_11_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["burgundian_village_12_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["burgundian_village_13_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["burgundian_village_14_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["burgundian_village_15_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["burgundian_village_16_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["burgundian_village_17_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_18_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_19_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_20_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_21_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_22_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_23_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_24_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_25_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_26_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_27_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600400966db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_village_28_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_29_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_30_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_31_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_32_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_33_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_34_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_35_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600500966db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["burgundian_village_36_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_37_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_38_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_39_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_40_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_41_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_42_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_43_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_44_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_45_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_46_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_47_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_48_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_49_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_50_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_51_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["burgundian_village_52_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],

["breton_village_1_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_2_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["breton_village_3_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_4_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["breton_village_5_elder",  "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["breton_village_6_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600500b66db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_village_7_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["breton_village_8_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["breton_village_9_elder",  "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["breton_village_10_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["breton_village_11_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_12_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["breton_village_13_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_14_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600400c66db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_village_15_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["breton_village_16_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_17_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["breton_village_18_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_19_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["breton_village_20_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600401266db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_village_21_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_22_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["breton_village_23_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_24_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["breton_village_25_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["breton_village_26_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_a_peasant_man_custom,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600701366db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["breton_village_27_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["breton_village_28_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["breton_village_29_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["breton_village_30_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["breton_village_31_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["breton_village_32_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["breton_village_33_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["breton_village_34_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["breton_village_35_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["breton_village_36_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["breton_village_37_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["breton_village_38_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["breton_village_39_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],

# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

#Used for player enterprises
["french_town_1_master_craftsman",  "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600b01336db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_2_master_craftsman",  "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003600c01236db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_3_master_craftsman",  "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600e04130db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_4_master_craftsman",  "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f601008230db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_5_master_craftsman",  "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f601108230db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_6_master_craftsman",  "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f60110c338db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_7_master_craftsman",  "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f60120c338db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_8_master_craftsman",  "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f600114438db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_9_master_craftsman",  "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800214438db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800314438db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800514538db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_12_master_craftsman", "{!}Town 12 Craftsman", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800614638db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_13_master_craftsman", "{!}Town 13 Craftsman", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800714638db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_14_master_craftsman", "{!}Town 14 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800814738db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_15_master_craftsman", "{!}Town 15 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800914838db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_16_master_craftsman", "{!}Town 16 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800b14938db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800c18b38db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800e1cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000004e80101cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000004e801020f38db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000004e801120f38db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000004e801220f38db6db6db61b6db00000000001db6db0000000000000000 ],
["french_town_23_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600b01336db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_24_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003600c01236db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_25_master_craftsman", "{!}Town 25 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600e04130db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_26_master_craftsman", "{!}Town 26 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f601008230db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_27_master_craftsman", "{!}Town 27 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f601108230db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_28_master_craftsman", "{!}Town 28 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f60110c338db6db6db6db6db00000000001db6db0000000000000000 ],
["french_town_29_master_craftsman", "{!}Town 29 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f60120c338db6db6db6db6db00000000001db6db0000000000000000 ],

["english_town_1_master_craftsman",  "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f600114438db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_2_master_craftsman",  "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800214438db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_3_master_craftsman",  "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800314438db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_4_master_craftsman",  "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800514538db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_5_master_craftsman",  "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800614638db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_6_master_craftsman",  "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800714638db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_7_master_craftsman",  "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800814738db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_8_master_craftsman",  "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800914838db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_9_master_craftsman",  "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800b14938db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_10_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800c18b38db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_11_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800e1cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_12_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000004e80101cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_13_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000004e801020f38db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_14_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000004e801120f38db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_15_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000004e801220f38db6db6db61b6db00000000001db6db0000000000000000 ],
["english_town_16_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600b01336db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_17_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003600c01236db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_18_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600e04130db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_19_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f601008230db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_20_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f601108230db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_21_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f60110c338db6db6db6db6db00000000001db6db0000000000000000 ],
["english_town_22_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f60120c338db6db6db6db6db00000000001db6db0000000000000000 ],

["burgundian_town_1_master_craftsman",  "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f600114438db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_2_master_craftsman",  "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800214438db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_3_master_craftsman",  "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800314438db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_4_master_craftsman",  "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800514538db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_5_master_craftsman",  "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800614638db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_6_master_craftsman",  "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800714638db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_7_master_craftsman",  "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800814738db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_8_master_craftsman",  "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800914838db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_9_master_craftsman",  "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800b14938db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_10_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800c18b38db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_11_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007e800e1cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_12_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000004e80101cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_13_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000004e801020f38db6db6db61b6db00000000001db6db0000000000000000 ],
["burgundian_town_14_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600b01336db6db6db6db6db00000000001db6db0000000000000000 ],
["burgundian_town_15_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600b01336db6db6db6db6db00000000001db6db0000000000000000 ],

["breton_town_1_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000003600c01236db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_town_2_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x000000003600e04130db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_town_3_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f601008230db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_town_4_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f601108230db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_town_5_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f60110c338db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_town_6_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007f60120c338db6db6db6db6db00000000001db6db0000000000000000 ],
["breton_town_7_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_tabard,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x00000007f600114438db6db6db61b6db00000000001db6db0000000000000000 ],
["breton_town_8_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_a_leather_jerkin,itm_b_high_boots_1], def_attrib|level(2), wp(20), knows_common, 0x00000007e800214438db6db6db61b6db00000000001db6db0000000000000000 ],



# Chests
["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common,0],
["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
#SB : move samurai back to Rivacheg (other chests were inaccessible)
["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# These are used as arrays in the scripts. #SB : give full inventory
["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# DAC Kham - Extend so we can show another window for Custom Troops
["temp_array_d","{!}temp_array_d","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["temp_array_e","{!}temp_array_e","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["temp_array_f","{!}temp_array_f","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],


["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point

["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,[itm_practice_staff,itm_a_commoner_apron,itm_b_high_boots_1],def_attrib|level(4),wp(60),knows_common,vaegir_face1,vaegir_face2],
["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,[itm_h_leather_cap,itm_h_arming_cap,itm_h_simple_coif,itm_h_straw_hat,itm_a_farmer_tunic,itm_a_commoner_apron,itm_a_peasant_cote_custom,itm_a_peasant_cote_custom,itm_a_hunter_coat_custom,itm_a_peasant_coat,itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_2,itm_practice_staff],def_attrib|level(4),wp(60),knows_common,vaegir_face1,vaegir_face2],
["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_a_peasant_coat,itm_b_turnshoes_1,itm_throwing_daggers,itm_w_onehanded_sword_c],def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1,man_face_old_2],

["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_a_peasant_man_custom,itm_b_turnshoes_2,itm_w_onehanded_sword_c],def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,bandit_face1,bandit_face2],

["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, [itm_a_leather_jerkin,itm_b_high_boots_1,itm_w_onehanded_sword_a],def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,bandit_face1,bandit_face2],

["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_a_leather_jerkin,itm_b_high_boots_1],def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,bandit_face1,bandit_face2],



["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_a_tabard,itm_b_turnshoes_2],def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1,man_face_older_2],

["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_a_tabard,itm_b_turnshoes_2],def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1,vaegir_face2],


["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,[itm_a_woman_common_dress_1_custom,itm_b_turnshoes_2],def_attrib|level(4),wp(60),knows_common,0x0000000cbf105005531d51c2ec49c7db003f89846151b89a0000000000000000,0x0000000cbf105005531d51c2ec49c7db003f89846151b89a0000000000000000],
["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,[itm_a_merchant_outfit,itm_b_turnshoes_1],def_attrib|level(4),wp(60),knows_common,man_face_middle_1,man_face_older_2],



##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_a_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_a_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_b_turnshoes_1, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
["french_crossbowman_ai", "French Crossbowman", "French Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, [], level(16)|str_15|agi_13, wpex(120,80,80,80,130,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["french_infantry_ai", "French Infantry", "French Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [], level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],
["french_voulgier_ai", "French Voulgier", "French Voulgiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [], level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, french_face_young_1, french_face_mature_2 ],
["french_knight_bachelier_ai", "French Chevalier Bachelier", "French Chevaliers Bacheliers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_1, [], level(28)|str_22|agi_22, wp_melee(200), knows_ironflesh_7|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],

["english_longbowman_ai", "English Longbowman", "English Longbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, [], level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],
["english_spearman_ai", "English Spearman", "English Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, [], level(15)|str_14|agi_14, wpex(120,80,140,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, english_face_middle_1, english_face_mature_2 ],
["english_billman_ai", "English Billman", "English Billmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, [], level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_warrior_basic2|knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, english_face_middle_1, english_face_mature_2 ],
["english_knight_ai", "English Knight", "English Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, [], level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, english_face_middle_1, english_face_mature_2 ],

["burgundian_longbowman_ai", "Burgundian Longbowman", "Burgundian Longbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, [], level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_pikeman_ai", "Burgundian Pikeman", "Burgundian Pikemen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, [], level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_halberdier_ai", "Burgundian Halberdier", "Burgundian Halberdiers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, [], level(15)|str_15|agi_13, wpex(100,100,140,100,100,100), knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_knight_ai", "Burgundian Knight Bachelier", "Burgundian Knights Bachelier", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, [], level(28)|str_22|agi_22, wp_melee(190), knows_ironflesh_7|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, burgundian_face_middle_1, burgundian_face_mature_2 ],

["breton_crossbowman_ai", "Breton Crossbowman", "Breton Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, [], level(16)|str_15|agi_13, wpex(120,80,80,80,150,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, breton_face_middle_1, breton_face_mature_2 ],
["breton_infantry_ai", "Breton Infantry", "Breton Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, [], level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, breton_face_middle_1, breton_face_mature_2 ],
["breton_man_at_arms_ai", "Breton Man-at-Arms", "Breton Men-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_kingdom_4, [], level(15)|str_15|agi_13, wpex(100,140,100,100,100,100), knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_2, breton_face_middle_1, breton_face_mature_2 ],
["breton_knight_ai", "Breton Knight", "Breton Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_4, [], level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, breton_face_middle_1, breton_face_mature_2 ],


#Multiplayer troops (they must have the base items only, nothing else)
["french_crossbowman_multiplayer", "French Crossbowman", "French Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1, [], level(16)|str_15|agi_13, wpex(120,80,80,80,130,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["french_infantry_multiplayer", "French Infantry", "French Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [], level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, french_face_middle_1, french_face_mature_2 ],
["french_man_at_arms_multiplayer", "French Man-at-Arms", "French Men-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1, [], level(15)|str_15|agi_13, wpex(100,140,100,100,100,100), knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_2, french_face_middle_1, french_face_mature_2 ],
["french_chevalier_multiplayer", "French Chevalier", "French Chevaliers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_1, [], level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_5|knows_riding_5, french_face_middle_1, french_face_mature_2 ],

["english_longbowman_multiplayer", "English Longbowman", "English Longbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, [], level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],
["english_infantry_multiplayer", "English Infantry", "English Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, [], level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, english_face_middle_1, english_face_mature_2 ],
["english_man_at_arms_multiplayer", "English Man-at-Arms", "English Men-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, [], level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_warrior_basic2|knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, english_face_middle_1, english_face_mature_2 ],
["english_knight_multiplayer", "English Knight", "English Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, [], level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5, english_face_middle_1, english_face_mature_2 ],

["burgundian_longbowman_multiplayer", "Burgundian Longbowman", "Burgundian Longbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3, [], level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_infantry_multiplayer", "Burgundian Infantry", "Burgundian Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3, [], level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_man_at_arms_multiplayer", "Burgundian Man-at-Arms", "Burgundian Men-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, [], level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, burgundian_face_middle_1, burgundian_face_mature_2 ],
["burgundian_knight_multiplayer", "Burgundian Knight", "Burgundian Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_3, [], level(30)|str_24|agi_24, wp_melee(215), knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5, burgundian_face_middle_1, burgundian_face_mature_2 ],

["breton_crossbowman_multiplayer", "Breton Crossbowman", "Breton Crossbowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4, [], level(16)|str_15|agi_13, wpex(120,80,80,80,150,80), knows_ironflesh_3|knows_power_strike_2|knows_shield_2|knows_weapon_master_2, breton_face_middle_1, breton_face_mature_2 ],
["breton_pavoisier_multiplayer", "Breton Infantry", "Breton Infantries", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4, [], level(15)|str_14|agi_14, wpex(140,80,80,80,80,80), knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_athletics_3|knows_weapon_master_1, breton_face_middle_1, breton_face_mature_2 ],
["breton_man_at_arms_multiplayer", "Breton Man-at-Arms", "Breton Men-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_kingdom_4, [], level(15)|str_15|agi_13, wpex(100,140,100,100,100,100), knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_2, breton_face_middle_1, breton_face_mature_2 ],
["breton_chevalier_multiplayer", "Breton Knight", "Breton Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_4, [], level(30)|str_24|agi_24, wp_melee(200), knows_ironflesh_7|knows_power_strike_6|knows_shield_4|knows_athletics_4|knows_weapon_master_6|knows_riding_5, breton_face_middle_1, breton_face_mature_2 ],

["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_2, [], 0, 0, 0, 0, 0],

#Player history array
["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

["quick_battle_troop_1", "Charles_VII, Regent of France, le Dauphin", "Charles_VII", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_a_nobleman_court_outfit_custom,itm_b_turnshoes_1,itm_s_heraldic_shield_bouche,itm_w_bastard_sword_regent], king_attrib, wp(420), king_skills, 0x00000002fb1030055726767eab4d555c00000000001d34e50000000000000000, 0 ],
["quick_battle_troop_2", "John_of_Lancaster, Duke of Bedford", "John_of_Lancaster", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_ho_horse_barded_red_chamfrom,itm_w_lance_colored_english_1,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_nobleman_court_outfit_custom,itm_s_heraldic_shield_metal,itm_w_bastard_sword_english], king_attrib, wp(420), king_skills, 0x00000006e910300c7774776e532d2cea00000000001dc6db0000000000000000, 0 ],
["quick_battle_troop_3", "Philippe the Good, Duke of Burgundy", "Philippe the Good", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_ho_horse_barded_brown_chamfrom,itm_w_lance_3,itm_h_great_bascinet_english_1410_visor,itm_g_gauntlets_gilded_segmented_a,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_10,itm_b_turnshoes_1,itm_a_nobleman_court_outfit_custom,itm_s_heraldic_shield_metal,itm_w_bastard_sword_duke], king_attrib, wp(420), king_skills, 0x00000004f810b0024caa6dd4fa90d6a200000000001c331a0000000000000000, 0 ],
["quick_battle_troop_4", "Jean V de Montfort, Duke of Brittany", "Jean V de Montfort", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_ho_horse_barded_black_chamfrom,itm_w_lance_4,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_nobleman_court_outfit_custom,itm_s_heraldic_shield_metal,itm_w_bastard_sword_sempach], king_attrib, wp(420), king_skills, 0x00000007bb10b34b5b1b55077970594900000000001db7660000000000000000, 0 ],
["quick_battle_troop_5", "Étienne de Vignolles, Seigneur de Vignolles", "La Hire", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_pigface_klappvisor_open,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_b,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_count], lord_attrib, wp(380), knows_lord_1, 0x000000003f10238364ec7b3afb2db76400000000001db6d30000000000000000, 0x000000003f10238364ec7b3afb2db76400000000001db6d30000000000000000 ],
["quick_battle_troop_6", "Jeanne", "La Pucelle d'Orléans", tf_hero|tf_female, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_2,itm_s_heraldic_shield_metal,itm_ho_horse_barded_white_chamfrom,itm_a_plate_joan,itm_h_great_bascinet_english_1410_visor,itm_g_gauntlets_segmented_b,itm_b_leg_harness_9,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_agincourt], lord_attrib, wp(380), knows_lord_1, 0x000000002d04400739024d57618e9b53003955b4e4b1455a0000000000000000, 0x000000002d04400739024d57618e9b53003955b4e4b1455a0000000000000000 ],
["quick_battle_troop_7", "Jean Poton de Xaintrailles, Seigneur de Xaintrailles", "Jean Poton de Xaintrailles", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_3,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_mercenary], lord_attrib, wp(380), knows_lord_1, 0x000000016904948164deb23b6b6d4adb00000000001da56c0000000000000000, 0x000000016904948164deb23b6b6d4adb00000000001da56c0000000000000000 ],
["quick_battle_troop_8", "John Talbot, Baron Talbot and Furnival", "John Talbot", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_2,itm_ho_horse_barded_red_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_demi_gauntlets,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_english], lord_attrib, wp(380), knows_lord_1, 0x000000093108100239a1723b6c826b6700000000001d47210000000000000000, 0x000000093108100239a1723b6c826b6700000000001d47210000000000000000 ],
["quick_battle_troop_9", "John Fastolf, Lieutenant-general of Normandy", "John Fastolf", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_s_heraldic_shield_metal,itm_w_lance_colored_english_3,itm_ho_horse_barded_red_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_brigandine_asher_custom,itm_b_high_boots_1,itm_g_gauntlets_mailed,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000b3f0000044b1297cb926d371200000000001e48660000000000000000, 0x0000000b3f0000044b1297cb926d371200000000001e48660000000000000000 ],
["quick_battle_troop_10", "Arthur de Richemont, Connétable de Richemont", "Arthur de Richemont", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_1,itm_ho_horse_barded_black_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_d], lord_attrib, wp(380), knows_lord_1, 0x0000000c560430004d0b2e7a5e8c1da400000000001eb7620000000000000000, 0x0000000c560430004d0b2e7a5e8c1da400000000001eb7620000000000000000 ],
["quick_battle_troop_11", "Pierre de Rochefort, Seigneur de Rieux et de Rochefort", "Pierre de Rochefort", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_s_heraldic_shield_metal,itm_w_lance_2,itm_ho_horse_barded_black_chamfrom,itm_h_zitta_bascinet,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_9,itm_g_gauntlets_gilded_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_landgraf], lord_attrib, wp(380), knows_lord_1, 0x000000081b0c748536db6db6db594d2400000000001ed4db0000000000000000, 0x000000081b0c748536db6db6db594d2400000000001ed4db0000000000000000 ],
["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_2, [], 0, 0, 0, 0, 0],

["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000,vaegir_face_older_2],
["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000,vaegir_face_older_2],
["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[],def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000,vaegir_face_older_2],
["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[],def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000,vaegir_face_older_2],
["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,[],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1,vaegir_face_older_2],
["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,[],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000,vaegir_face_older_2],
["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,[],def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1,vaegir_face_older_2],
["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_2,[itm_s_heraldic_shield_leather],def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1,khergit_face_older_2],
["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,[],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000,vaegir_face_older_2],

["swadian_merchant", "Monk", "{!}Prominent", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_a_monk_robe_brown,itm_b_turnshoes_2], def_attrib|level(2), wp(20), knows_common, 0x000000099300500e36db6db6dbcdb6db00000000001e391b0000000000000000 ],
["vaegir_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_a_merchant_outfit,itm_b_turnshoes_1], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
# ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_a_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
# ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["sea_raider_leader","Sea Raider Captain","Sea Raider Captains",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,[],def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1,nord_face_old_2],

["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,[],def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000,bandit_face2],

["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,[],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000000320410022d2595495491afa400000000001d9ae30000000000000000,mercenary_face_2],

["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

##diplomacy begin
#SB : fixed plural name (hero name), TODO actually use name/gender in hiring dialogues
["dplmc_chamberlain","Chamberlain Aubrey de Vere", "Aubrey de Vere",tf_hero|tf_male,0,0,fac_commoners,[itm_a_tabard, itm_b_high_boots_1], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

["dplmc_constable","Constable Miles de Gloucester","Miles de Gloucester",tf_hero|tf_male,0,0,fac_commoners,[itm_a_noble_shirt_red, itm_b_high_boots_1],knight_attrib_4,wp_melee(200),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

["dplmc_chancellor","Chancellor Herfast","Herfast",tf_hero|tf_male,0,0,fac_commoners,[itm_a_noble_shirt_black, itm_b_high_boots_1],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1,itm_g_leather_gauntlet,itm_ho_courser_1,itm_w_onehanded_sword_squire],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_h_highlander_beret_blue_2,itm_a_noble_shirt_blue,itm_b_high_boots_1,itm_g_leather_gauntlet,itm_ho_courser_1,itm_w_onehanded_sword_squire],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
# recruiter kit begin
["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1,swadian_face_old_2],
# recruiter kit end
##diplomacy end

#Lumos List Troop
["upgrades", "{!}Upgrade list", "{!}List of available upgrades", tf_hero, no_scene, reserved, fac_neutral,[],level(60),wp(800),knows_lord_1,merchant_face_1, merchant_face_2],

# Bodysliding
["bodysliding_temp","_","_",tf_inactive,0,0,0,[],0,0,0,0],

# DAC Seek: dummy troops for item progression
["english_yeoman_archer_late", "English Yeoman Archer", "English Yeomen Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_hood_big_liripipe_full_custom,itm_h_skullcap_hood_liripipe_custom,itm_h_simple_cervelliere_hood_liripipe_custom,itm_h_hood_square_liripipe_full_custom,itm_h_hood_square_full_custom,itm_h_peasant_bycocket_1_custom,itm_h_peasant_bycocket_2_custom,itm_h_straw_hat,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_long_bow_ash,itm_w_arrow_triangular,
 itm_w_dagger_baselard,itm_w_dagger_quillon,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_a,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
], 
level(8)|str_10|agi_12, wpex(90,80,80,110,80,80), knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_athletics_4|knows_weapon_master_1, english_face_young_1, english_face_middle_2 ],
["english_archer_late", "English Archer", "English Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_gambeson_asher_regular_custom,itm_a_gambeson_asher_belt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_long_bow_elm,itm_w_arrow_triangular_large,
 itm_w_dagger_baselard,itm_w_dagger_quillon,itm_w_onehanded_falchion_peasant,itm_w_onehanded_falchion_peasant_b,itm_w_onehanded_sword_c_small,itm_w_onehanded_sword_a,itm_w_archer_hatchet,itm_w_archer_hatchet_brown,itm_w_archer_hatchet_red,itm_w_archers_maul,itm_w_archers_maul_brown,itm_w_archers_maul_red,itm_w_spiked_club,itm_w_spiked_club_brown,itm_w_spiked_club_dark,
], 
level(12)|str_12|agi_14, wpex(100,80,80,130,80,80), knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_young_1, english_face_middle_2 ],
["english_retinue_archer_late", "English Retinue Archer", "English Retinue Archers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_strap,itm_h_sallet_curved_strap,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_strap,itm_h_cervelliere_strap,itm_h_skullcap_strap,
 itm_a_padded_jack_cross_custom,itm_a_padded_jack_surcoat_custom,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_long_bow_yew,itm_w_arrow_bodkin,
 itm_w_onehanded_falchion_a,itm_w_onehanded_sword_longbowman,itm_w_onehanded_falchion_b,itm_w_onehanded_sword_a,itm_w_onehanded_sword_c,itm_w_onehanded_sword_c_small,itm_w_onehanded_war_axe_01,itm_w_onehanded_war_axe_01_brown,itm_w_onehanded_war_axe_01_red,itm_w_mace_knobbed,itm_w_mace_knobbed_brown,itm_w_mace_knobbed_red,
 itm_s_steel_buckler,
], 
level(18)|str_14|agi_16, wpex(120,80,80,150,80,80), knows_ironflesh_3|knows_power_draw_4|knows_power_strike_2|knows_athletics_4|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],

["english_militia_late", "English Militia", "English Militia", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_skullcap_strap,itm_h_simple_cervelliere_2_strap,itm_h_simple_cervelliere_strap,itm_h_makeshift_kettle_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_3_strap,itm_h_chapel_de_fer_strap,
 itm_a_light_gambeson_long_sleeves_8_custom,itm_a_light_gambeson_long_sleeves_8_alt_custom,
 itm_b_turnshoes_1,itm_b_turnshoes_2,itm_b_turnshoes_4,itm_b_turnshoes_5,itm_b_turnshoes_8,itm_b_turnshoes_9,
 itm_w_fauchard_1,itm_w_fauchard_2,itm_w_fauchard_3,
], 
level(15)|str_16|agi_12, wpex(100,100,150,100,100,100), knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_2, english_face_young_1, english_face_middle_2 ],
["english_footman_late", "English Poor Spearman", "English Poor Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_chapel_de_fer_strap,itm_h_makeshift_kettle_strap,itm_h_german_kettlehat_1_strap,itm_h_german_kettlehat_4_strap,itm_h_cervelliere_strap,itm_h_simple_cervelliere_strap,itm_h_simple_cervelliere_2_strap,itm_h_skullcap_strap,itm_h_transitional_sallet_1_strap,itm_h_transitional_sallet_2_strap,itm_h_transitional_sallet_3_strap,itm_h_sallet_strap,itm_h_sallet_curved_strap,
 itm_a_padded_jack_cross_custom,itm_a_padded_jack_surcoat_custom,
 itm_g_leather_gauntlet,
 itm_b_high_boots_1,itm_b_high_boots_2,itm_b_high_boots_4,itm_b_high_boots_5,itm_b_high_boots_8,itm_b_high_boots_9,
 itm_w_bill_1,itm_w_bill_4,
], 
level(20)|str_18|agi_15, wpex(100,100,180,100,100,100), knows_warrior_basic2|knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_3, english_face_middle_1, english_face_mature_2 ],
["english_heavy_footman_late", "English Spearman", "English Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_simple_cervelliere_mail_aventail,itm_h_simple_cervelliere_2_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_transitional_sallet_1_mail_aventail,itm_h_transitional_sallet_2_mail_aventail,itm_h_transitional_sallet_3_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,
 itm_a_brigandine_asher_a_custom,itm_a_brigandine_asher_b_custom,
 itm_g_demi_gauntlets,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_w_bill_1,itm_w_bill_4,
], 
level(20)|str_16|agi_16, wpex(160,100,100,100,100,100), knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3|knows_weapon_master_2, english_face_middle_1, english_face_mature_2 ],
["english_sergeant_late", "English Rich Spearman", "English Rich Spearmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_bascinet_1_mail_aventail,itm_h_bascinet_2_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_transitional_sallet_1_mail_aventail,itm_h_transitional_sallet_2_mail_aventail,itm_h_transitional_sallet_3_mail_aventail,itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,
 itm_a_brigandine_asher_a_plate_1_custom,itm_a_brigandine_asher_a_plate_2_custom,itm_a_brigandine_asher_a_plate_3_custom,itm_a_brigandine_asher_b_plate_1_custom,itm_a_brigandine_asher_b_plate_2_custom,itm_a_brigandine_asher_b_plate_3_custom,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_gauntlets_mailed,
 itm_w_bill_2,itm_w_bill_3,
], 
level(25)|str_20|agi_20, wpex(100,100,200,100,100,100), knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_4, english_face_mature_1, english_face_old_2 ],

["english_footman_at_arms_late", "English Footman-at-Arms", "English Footmen-at-Arms", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,
 itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_3,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_awlpike_1,itm_w_awlpike_5,itm_w_twohanded_knight_battle_axe_01,itm_w_twohanded_knight_battle_axe_01_brown,itm_w_twohanded_knight_battle_axe_01_ebony,
], 
level(25)|str_20|agi_20, wp_melee(180), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5, english_face_young_1, english_face_mature_2 ],

["english_dismounted_squire_late", "English Dismounted Squire", "English Dismounted Squires", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_3_visor_3_mail_aventail,itm_h_bascinet_3_visor_3_open_mail_aventail,itm_h_bascinet_3_visor_4_mail_aventail,itm_h_bascinet_3_visor_4_open_mail_aventail,itm_h_bascinet_3_visor_8_mail_aventail,itm_h_bascinet_3_visor_8_open_mail_aventail,itm_h_bascinet_3_visor_9_mail_aventail,itm_h_bascinet_3_visor_9_open_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_bascinet_4_visor_3_mail_aventail,itm_h_bascinet_4_visor_3_open_mail_aventail,itm_h_bascinet_4_visor_4_mail_aventail,itm_h_bascinet_4_visor_4_open_mail_aventail,itm_h_bascinet_4_visor_8_mail_aventail,itm_h_bascinet_4_visor_8_open_mail_aventail,itm_h_bascinet_4_visor_9_mail_aventail,itm_h_bascinet_4_visor_9_open_mail_aventail,
 itm_a_english_plate_1430_1445,
 itm_b_leg_harness_english_1420,itm_b_leg_harness_english_1430,
 itm_g_gauntlets_mailed,
 itm_w_twohanded_sword_talhoffer,itm_w_bastard_falchion,itm_w_bastard_sword_agincourt,itm_w_bastard_sword_english,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_twohanded_knight_battle_axe_02,itm_w_twohanded_knight_battle_axe_02_brown,itm_w_twohanded_knight_battle_axe_02_ebony,itm_w_awlpike_5,itm_w_pollaxe_blunt_05_ash,itm_w_pollaxe_blunt_alt_05_ash,itm_w_pollaxe_blunt_05_brown,itm_w_pollaxe_blunt_alt_05_brown,itm_w_pollaxe_cut_09_ash,itm_w_pollaxe_cut_09_brown,
], 
level(30)|str_24|agi_24, wp_melee(220), knows_ironflesh_7|knows_power_strike_7|knows_athletics_4|knows_shield_4|knows_weapon_master_6, english_face_middle_1, english_face_mature_2 ],

["english_dismounted_knight_late", "English Dismounted Knight", "English Dismounted Knights", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_great_bascinet_english_1430,itm_h_great_bascinet_english_1430_visor,itm_h_great_bascinet_english_1430_visor_open,itm_h_transitional_sallet_heavy,itm_h_transitional_sallet_heavy_frogmouth,itm_h_transitional_sallet_heavy_frogmouth_open, itm_h_great_bascinet_english_1410,itm_h_great_bascinet_english_1410_visor,itm_h_great_bascinet_english_1410_visor_open,
 itm_a_english_plate_1435_1450,
 itm_b_leg_harness_english_1430,itm_b_leg_harness_english_1435,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_pollaxe_blunt_04_english_ash,itm_w_pollaxe_blunt_alt_04_english_ash,itm_w_pollaxe_blunt_04_english_red_trim,itm_w_pollaxe_blunt_alt_04_english_red_trim,itm_w_pollaxe_blunt_04_english_dark,itm_w_pollaxe_blunt_alt_04_english_dark,itm_w_pollaxe_cut_04_english_ash,itm_w_pollaxe_cut_alt_04_english_ash,itm_w_pollaxe_cut_04_english_ebony,itm_w_pollaxe_cut_alt_04_english_ebony,(itm_w_bastard_sword_english,imodbit_masterwork),(itm_w_bastard_sword_agincourt,imodbit_masterwork),itm_w_twohanded_sword_earl,itm_w_twohanded_knight_battle_axe_03,itm_w_twohanded_knight_battle_axe_03_brown,itm_w_twohanded_knight_battle_axe_03_ebony,itm_w_awlpike_4,
], 
level(35)|str_28|agi_28, wp_melee(260), knows_ironflesh_8|knows_power_strike_8|knows_shield_5|knows_athletics_4|knows_weapon_master_8, english_face_mature_1, english_face_old_2 ],

### Mounted
["english_man_at_arms_late", "English Man-at-Arms", "English Men-at-Arms", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_cervelliere_mail_aventail,itm_h_skullcap_mail_aventail,itm_h_simple_cervelliere_mail_aventail,
 itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_1,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_2,itm_a_pistoia_breastplate_mail_sleeves_plate_spaulders_3,
 itm_b_leg_harness_1,itm_b_leg_harness_2,itm_b_leg_harness_3,
 itm_g_finger_gauntlets,itm_g_demi_gauntlets,
 itm_w_native_spear_b_custom,itm_w_native_spear_f_custom,itm_w_mace_english,itm_w_mace_english_brown,itm_w_mace_english_ebony,itm_w_onehanded_horseman_axe_01,itm_w_onehanded_horseman_axe_01_brown,itm_w_bastard_sword_a,itm_w_bastard_sword_b,itm_w_bastard_sword_c,
 itm_s_heraldic_shield_heater,
 itm_ho_rouncey_1,itm_ho_rouncey_2,itm_ho_rouncey_3,itm_ho_rouncey_4,itm_ho_rouncey_5,itm_ho_rouncey_6,
], 
level(25)|str_20|agi_20, wp_melee(150), knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_3, english_face_young_1, english_face_middle_2 ],
["english_squire_late", "English Squire", "English Squires", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_sallet_mail_aventail,itm_h_sallet_curved_mail_aventail,itm_h_bascinet_3_mail_aventail,itm_h_bascinet_3_visor_3_mail_aventail,itm_h_bascinet_3_visor_3_open_mail_aventail,itm_h_bascinet_3_visor_4_mail_aventail,itm_h_bascinet_3_visor_4_open_mail_aventail,itm_h_bascinet_3_visor_8_mail_aventail,itm_h_bascinet_3_visor_8_open_mail_aventail,itm_h_bascinet_3_visor_9_mail_aventail,itm_h_bascinet_3_visor_9_open_mail_aventail,itm_h_bascinet_4_mail_aventail,itm_h_bascinet_4_visor_3_mail_aventail,itm_h_bascinet_4_visor_3_open_mail_aventail,itm_h_bascinet_4_visor_4_mail_aventail,itm_h_bascinet_4_visor_4_open_mail_aventail,itm_h_bascinet_4_visor_8_mail_aventail,itm_h_bascinet_4_visor_8_open_mail_aventail,itm_h_bascinet_4_visor_9_mail_aventail,itm_h_bascinet_4_visor_9_open_mail_aventail,
 itm_a_english_plate_1430_1445,
 itm_b_leg_harness_english_1420,itm_b_leg_harness_english_1430,
 itm_g_gauntlets_mailed,
 itm_w_lance_1_custom,itm_w_lance_2_custom,itm_w_lance_3_custom,itm_w_warhammer_2,itm_w_warhammer_2_brown,itm_w_warhammer_1,itm_w_warhammer_1_brown,itm_w_onehanded_horseman_axe_02,itm_w_onehanded_horseman_axe_03,itm_w_onehanded_horseman_axe_02_brown,itm_w_onehanded_horseman_axe_03_brown,itm_w_bastard_sword_b,itm_w_bastard_sword_c,itm_w_bastard_sword_d,
 itm_s_heraldic_shield_leather,
 itm_ho_horse_barded_brown,itm_ho_horse_barded_red,itm_ho_horse_barded_red,itm_ho_horse_barded_white,
], 
level(28)|str_22|agi_22, wp_melee(180), knows_ironflesh_6|knows_power_strike_5|knows_shield_3|knows_athletics_4|knows_weapon_master_5|knows_riding_4, english_face_middle_1, english_face_mature_2 ],
["english_knight_late", "English Knight", "English Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_kingdom_2, 
[
 itm_h_great_bascinet_english_1430,itm_h_great_bascinet_english_1430_visor,itm_h_great_bascinet_english_1430_visor_open,itm_h_transitional_sallet_heavy,itm_h_transitional_sallet_heavy_frogmouth,itm_h_transitional_sallet_heavy_frogmouth_open, itm_h_great_bascinet_english_1410,itm_h_great_bascinet_english_1410_visor,itm_h_great_bascinet_english_1410_visor_open,
 itm_a_english_plate_1435_1450,
 itm_b_leg_harness_english_1430,itm_b_leg_harness_english_1435,
 itm_g_gauntlets_segmented_a,itm_g_gauntlets_segmented_b,
 itm_w_lance_colored_english_1_custom,itm_w_lance_colored_english_2_custom,itm_w_lance_colored_english_3_custom,itm_w_knight_warhammer_1,itm_w_knight_warhammer_1_ebony,itm_w_knight_warhammer_1_brown,itm_w_knight_warhammer_2,itm_w_knight_warhammer_2_ebony,itm_w_knight_warhammer_3,itm_w_knight_warhammer_3_ebony,itm_w_knight_flanged_mace,itm_w_knight_winged_mace,itm_w_onehanded_knight_axe_01,itm_w_onehanded_knight_axe_01_ebony,itm_w_onehanded_knight_axe_02,itm_w_onehanded_knight_axe_02_ebony,(itm_w_bastard_sword_agincourt,imodbit_masterwork),(itm_w_bastard_sword_english,imodbit_masterwork),(itm_w_bastard_sword_d,imodbit_masterwork),(itm_w_bastard_sword_c,imodbit_masterwork),
 itm_s_heraldic_shield_bouche,
 itm_ho_horse_barded_brown_chamfrom,itm_ho_horse_barded_red_chamfrom,itm_ho_horse_barded_red_chamfrom,itm_ho_horse_barded_white_chamfrom,
], 
level(35)|str_28|agi_28, wp_melee(250), knows_ironflesh_8|knows_power_strike_8|knows_shield_4|knows_athletics_4|knows_weapon_master_8|knows_riding_5, english_face_mature_1, english_face_old_2 ],


# EXTRA LORDS & LADIES FOR ARISTOCRACY - DAC
["extra_lady_1", "Yolande d'Aragon", "Yolande d'Aragon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_2", "Marie de Sully", "Marie de Sully", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_3", "Eléonore de Castille", "Eléonore de Castille", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_4", "Béatrice de Navarre", "Béatrice de Navarre", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_5", "Bonne de Berry", "Bonne de Berry", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_6", "Hélis de Bort", "Hélis de Bort", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_7", "Jeanne de Tigné", "Jeanne de Tigné", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_8", "Catherine de Vendôme", "Catherine de Vendôme", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_9", "Marie de Berry", "Marie de Berry", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_10", "Marie de Fécamp", "Marie de Fécamp", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_11", "Anne de Laval", "Anne de Laval", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_12", "Jeanne de Craon", "Jeanne de Craon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_13", "Marguerite d'Auvergne", "Marguerite d'Auvergne", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_14", "Isabel le Despenser", "Isabel le Despenser", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_15", "Katherine Stafford", "Katherine Stafford", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_16", "Margaret Holland", "Margaret Holland", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_17", "Katherine Peverell", "Katherine Peverell", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_18", "Jeanne d'Escaillon", "Jeanne d'Escaillon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_19", "Alice Sergeaux ", "Alice Sergeaux ", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_20", "Rose d'Albret", "Rose d'Albret", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_21", "Marguerite de Bavière", "Marguerite de Bavière", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_22", "Jeanne de Chalon-Arlay", "Jeanne de Chalon-Arlay", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_23", "Marguerite d'Enghien", "Marguerite d'Enghien", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_24", "Jeanne de Créquy", "Jeanne de Créquy", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_25", "Jeanne de Vergy", "Jeanne de Vergy", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_26", "Marguerite de Craon", "Marguerite de Craon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_27", "Jeanne de Navarre", "Jeanne de Navarre", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_28", "Jeanne de Beaumanoir", "Jeanne de Beaumanoir", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_29", "Isabeau de Brosse", "Isabeau de Brosse", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_30", "Marguerite de Sully", "Marguerite de Sully", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_31", "Jeanne de Rochefort", "Jeanne de Rochefort", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_32", "Béatrice de Montauban", "Béatrice de Montauban", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_33", "Agnès Trousseau", "Agnès Trousseau", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_34", "Elizabeth FitzAlan", "Elizabeth FitzAlan", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_35", "Elizabeth Plantagenêt", "Elizabeth Plantagenêt", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_36", "Valentine Visconti", "Valentine Visconti", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_37", "Isabelle de Valois", "Isabelle de Valois", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_38", "Lady Beatrice de Clisson", "Beatrice de Clisson", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_39", "Lady Beatrice de Clisson", "Beatrice de Clisson", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["extra_lady_40", "Lady Beatrice de Clisson", "Beatrice de Clisson", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],

["extra_lord_1", "Louis II d'Anjou", "Louis II d'Anjou", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_2", "Charles I d'Albret", "Charles I d'Albret", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_3", "Charles III de Navarre", "Charles III de Navarre", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_4", "Bernard VII d'Armagnac", "Bernard VII d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_5", "Robert de Chabannes", "Robert de Chabannes", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_6", "Jean III de Beauvau", "Jean III de Beauvau", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_7", "Jean de Bourbon", "Jean de Bourbon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_8", "Jean I de Bourbon", "Jean I de Bourbon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_9", "Guillaume I de Gamaches ", "Guillaume I de Gamaches ", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_10", "Guy XIII de Montfort-Laval", "Guy XIII de Montfort-Laval", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_11", "Ingelger II d'Amboise", "Ingelger II d'Amboise", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_12", "Jean IV de Bueil", "Jean IV de Bueil", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_13", "Michael de La Pole", "Michael de La Pole", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_14", "John Beaufort", "John Beaufort", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_15", "Walter Hungerford", "Walter Hungerford", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_16", "Thierry de Robersart", "Thierry de Robersart", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_17", "Richard de Vere", "Richard de Vere", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_18", "Bertrand II de Montferrand", "Bertrand II de Montferrand", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_19", "Jean de Bourgogne", "Jean de Bourgogne", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_20", "Tristan de Toulongeon", "Tristan de Toulongeon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_21", "Jean de Luxembourg", "Jean de Luxembourg", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_22", "Guillaume II de Brimeu", "Guillaume II de Brimeu", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_23", "Jean III de Vergy", "Jean III de Vergy", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_24", "Jean I de Croÿ", "Jean I de Croÿ", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_25", "Jean IV de Montfort", "Jean IV de Montfort", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_26", "Charles de Dinan", "Charles de Dinan", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_27", "Guichard de Culant", "Guichard de Culant", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_28", "Jean de Culant", "Jean de Culant", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_29", "Jean II de Rieux", "Jean II de Rieux", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_30", "Jean III de Rieux", "Jean III de Rieux", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_31", "Godemar II de Lignières", "Godemar II de Lignières", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_32", "Philippe de Lignières", "Philippe de Lignières", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_33", "Godemar III de Lignères", "Godemar III de Lignères", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_34", "Thomas Mowbray", "Thomas Mowbray", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_35", "John Holland of Exeter", "John Holland of Exeter", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_36", "Louis d'Orléans", "Louis d'Orléans", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_37", "Charles d'Orléans", "Charles d'Orléans", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_38", "Ayn Astir Farrow", "Ayn Astir Farrow", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], knight_attrib_4, wp(400), knight_skills_4, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_39", "Jean II d'Alençon, Duc d'Alençon", "Jean d'Alençon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_40", "Jean II d'Alençon, Duc d'Alençon", "Jean d'Alençon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],
["extra_lord_41", "Gui VI de La Trémoille", "Gui VI de La Trémoille", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_w_lance_colored_french_1,itm_s_heraldic_shield_metal,itm_ho_horse_barded_blue_chamfrom,itm_h_great_bascinet_english_1410_visor,itm_a_english_plate_1415_heraldic,itm_b_leg_harness_2,itm_g_gauntlets_segmented_a,itm_b_turnshoes_1,itm_a_tabard,itm_w_bastard_sword_crecy], lord_attrib, wp(380), knows_lord_1, 0x000000000000800f49255229948d172300000000001d551a0000000000000000, 0x000000000000800f49255229948d172300000000001d551a0000000000000000 ],

["female_face_keys", "{!}", "{!}", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners, [itm_b_turnshoes_1,itm_a_woman_court_dress_1], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000e10400336db6db6db6db6db003b6db6db6db6db0000000000000000, 0x000000000e10400336db6db6db6db6db003b6db6db6db6db0000000000000000 ],


# Mark7 arena spectators troops
 
# Arena Noble sit
["arena_1_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_poulaines_1], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],#
["arena_2_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_poulaines_2],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],#
["arena_3_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_a_merchant_outfit,itm_b_poulaines_3],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["arena_4_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_a_noble_shirt_green,itm_b_poulaines_4],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["arena_5_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_a_tabard,itm_b_high_boots_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["arena_6_noble","Warrior","Mercenary Crossbowmen",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
[itm_a_leather_jerkin,itm_a_leather_jerkin,itm_b_high_boots_2],def_attrib|level(19),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
["arena_7_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral, 
[itm_a_woman_court_dress_1,itm_b_turnshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
["arena_8_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_2,itm_b_turnshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["arena_9_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_3,itm_b_turnshoes_9], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
["arena_10_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_4,itm_b_turnshoes_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["arena_11_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_6,itm_b_turnshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["arena_12_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral, 
[itm_a_woman_court_dress_5,itm_b_turnshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
["arena_noble_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],

# Arena Noble sit
["arena_stand_1_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_h_highlander_beret_black,itm_a_noble_shirt_black,itm_b_poulaines_1], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],#
["arena_stand_2_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_h_highlander_beret_blue,itm_a_noble_shirt_blue,itm_b_poulaines_2],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],#
["arena_stand_3_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_a_merchant_outfit,itm_b_poulaines_3],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["arena_stand_4_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_a_noble_shirt_green,itm_b_poulaines_4],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["arena_stand_5_noble", "Noble", "{!}Noble", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,
[itm_a_tabard,itm_b_high_boots_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["arena_stand_6_noble","Warrior","Mercenary Crossbowmen",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
[itm_a_leather_jerkin,itm_a_leather_jerkin,itm_b_high_boots_2],def_attrib|level(19),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
["arena_stand_7_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral, 
[itm_a_woman_court_dress_1,itm_b_turnshoes_4],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
["arena_stand_8_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_2,itm_b_turnshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["arena_stand_9_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_3,itm_b_turnshoes_9], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
["arena_stand_10_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_4,itm_b_turnshoes_5], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["arena_stand_11_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral,  
[itm_a_woman_court_dress_6,itm_b_turnshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["arena_stand_12_noble","Noble Lady","Noble Lady",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_neutral, 
[itm_a_woman_court_dress_5,itm_b_turnshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
["arena_noble_stand_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],

# Arena commoner sit
["arena_stand_man_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_peasant_man_custom,itm_b_turnshoes_1],
def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
["arena_stand_man_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_woman_common_dress_1_custom,itm_b_turnshoes_1],
def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["arena_stand_man_3","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
[itm_a_peasant_man_custom,itm_b_turnshoes_2],
def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["arena_stand_man_4","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_woman_common_dress_1_custom, itm_b_turnshoes_3],
def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["arena_stand_man_5","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
[itm_a_peasant_man_custom,itm_b_turnshoes_9],
def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["arena_stand_man_6","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_woman_common_dress_2_custom,itm_b_turnshoes_4],
def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["arena_stand_man_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_tabard,itm_b_turnshoes_6],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_stand_man_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_hunter_coat_custom,itm_b_turnshoes_3],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_stand_man_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_light_gambeson_short_sleeves_custom,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_stand_man_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_peasant_man_custom,itm_b_turnshoes_3],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_stand_man_11","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_peasant_man_custom,itm_b_turnshoes_4],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_stand_man_12","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_peasant_cote_custom,itm_b_turnshoes_5],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["town_arena_stand_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],


# Arena commoner stand

["arena_sit_man_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_peasant_man_custom,itm_b_turnshoes_1],
def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
["arena_sit_man_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_woman_common_dress_1_custom,itm_b_turnshoes_1],
def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["arena_sit_man_3","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
[itm_a_peasant_man_custom,itm_b_turnshoes_2],
def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["arena_sit_man_4","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_woman_common_dress_1_custom, itm_b_turnshoes_3],
def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["arena_sit_man_5","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
[itm_a_peasant_man_custom,itm_b_turnshoes_9],
def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["arena_sit_man_6","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_a_woman_common_dress_2_custom,itm_b_turnshoes_4],
def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["arena_sit_man_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_tabard,itm_b_turnshoes_6],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_sit_man_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_hunter_coat_custom,itm_b_turnshoes_3],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_sit_man_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_light_gambeson_short_sleeves_custom,itm_b_turnshoes_2],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_sit_man_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_peasant_man_custom,itm_b_turnshoes_3],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_sit_man_11","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_peasant_man_custom,itm_b_turnshoes_4],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_sit_man_12","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
[itm_a_peasant_cote_custom,itm_b_turnshoes_5],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["arena_sit_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],


# Mark7 arena spectators troops END
] 
troops = troops + mercenary_company_troops

###################################################### FRENCH TROOPS
##### Village Troops
### Archer Line
upgrade(troops,"french_peasant_archer","french_poor_archer")
upgrade(troops,"french_poor_archer","french_archer")
### Infantry Line
upgrade(troops,"french_peasant_levy","french_poor_spearman")
upgrade2(troops,"french_poor_spearman","french_spearman","french_vougier")

##### City Troops
### Archer Line
upgrade(troops,"french_militia_crossbowman","french_crossbowman")
upgrade(troops,"french_crossbowman","french_rich_crossbowman")
### Infantry Line
upgrade2(troops,"french_militia","french_poor_pavoisier","french_poor_guisarmier")
upgrade(troops,"french_poor_pavoisier","french_pavoisier")
upgrade(troops,"french_pavoisier","french_rich_pavoisier")
upgrade(troops,"french_poor_guisarmier","french_guisarmier")
upgrade(troops,"french_guisarmier","french_rich_guisarmier")
upgrade(troops,"french_rich_guisarmier","french_sergeant")


## Noble Line
upgrade(troops,"french_spearman_at_atms","french_dismounted_squire")
upgrade(troops,"french_dismounted_squire","french_chevalier_a_pied") 

upgrade(troops,"french_man_at_arms","french_squire")
upgrade(troops,"french_squire","french_chevalier")

##################################################### ENGLISH TROOPS
## Archer Line
upgrade(troops,"english_communal_bowman","english_communal_archer")
upgrade2(troops,"english_communal_archer","english_communal_veteran_archer","english_garrison_crossbowman")

## Infantry Line
upgrade(troops,"english_communal_levy","english_communal_levy_footman")
upgrade2(troops,"english_communal_levy_footman","english_communal_footman","english_communal_vougier")

upgrade(troops,"english_militia","english_footman")
upgrade(troops,"english_footman","english_heavy_footman")
upgrade(troops,"english_heavy_footman","english_sergeant")

upgrade(troops,"english_yeoman_archer","english_archer")
upgrade(troops,"english_archer","english_retinue_archer")

## Noble Line
##English Noble Line
upgrade(troops,"english_footman_at_arms","english_dismounted_squire")
upgrade(troops,"english_dismounted_squire","english_dismounted_knight")

upgrade(troops,"english_man_at_arms","english_squire")
upgrade(troops,"english_squire","english_knight")


##################################################### BURGUNDIAN TROOPS
## Archer Line
upgrade(troops,"burgundian_peasant_bowman","burgundian_poor_bowman")
upgrade(troops,"burgundian_poor_bowman","burgundian_bowman")

upgrade2(troops,"burgundian_militia_archer","burgundian_poor_archer","burgundian_poor_crossbowman")
upgrade(troops,"burgundian_poor_archer","burgundian_archer")
upgrade(troops,"burgundian_poor_crossbowman","burgundian_crossbowman")

## Infantry Line
upgrade2(troops,"burgundian_peasant","burgundian_poor_spearman","burgundian_poor_vougier")
upgrade(troops,"burgundian_poor_spearman","burgundian_spearman")
upgrade(troops,"burgundian_poor_vougier","burgundian_vougier")

upgrade2(troops,"burgundian_militia","burgundian_poor_pavoisier","burgundian_poor_guisarmier")
upgrade(troops,"burgundian_poor_pavoisier","burgundian_pavoisier")
upgrade(troops,"burgundian_pavoisier","burgundian_rich_pavoisier")
upgrade(troops,"burgundian_rich_pavoisier","burgundian_sergeant_pavoisier")
upgrade(troops,"burgundian_poor_guisarmier","burgundian_guisarmier")
upgrade(troops,"burgundian_guisarmier","burgundian_rich_guisarmier")

## Noble Line
upgrade(troops,"burgundian_footman_at_arms","burgundian_dismounted_squire")
upgrade(troops,"burgundian_dismounted_squire","burgundian_dismounted_knight")

upgrade(troops,"burgundian_man_at_arms","burgundian_squire")
upgrade(troops,"burgundian_squire","burgundian_knight")


##################################################### BRETON TROOPS
## Archer Line
upgrade(troops,"breton_peasant_archer","breton_poor_archer_ordonnance")
upgrade(troops,"breton_poor_archer_ordonnance","breton_archer_ordonnance")

upgrade2(troops,"breton_militia_crossbowman","breton_poor_archer","breton_poor_crossbowman")
upgrade(troops,"breton_poor_archer","breton_archer")
upgrade(troops,"breton_poor_crossbowman","breton_crossbowman")

## Infantry Line
upgrade(troops,"breton_peasant_levy","breton_poor_spearman")
upgrade2(troops,"breton_poor_spearman","breton_spearman","breton_vougier")

upgrade2(troops,"breton_militia","breton_poor_pavoisier","breton_poor_guisarmier")
upgrade(troops,"breton_poor_pavoisier","breton_pavoisier")
upgrade(troops,"breton_pavoisier","breton_rich_pavoisier")
upgrade(troops,"breton_poor_guisarmier","breton_guisarmier")
upgrade(troops,"breton_guisarmier","breton_rich_guisarmier")
upgrade(troops,"breton_rich_guisarmier","breton_sergeant")

## Noble Line
upgrade(troops,"breton_footman_at_arms","breton_dismounted_squire")
upgrade(troops,"breton_dismounted_squire","breton_chevalier_a_pied")

upgrade(troops,"breton_man_at_arms","breton_squire")
upgrade(troops,"breton_squire","breton_chevalier")


##################################################### FLEMISH MERCENARIES
upgrade(troops,"flemish_peasant_crossbowman","flemish_militia_crossbowman")
upgrade(troops,"flemish_militia_crossbowman","flemish_crossbowman")
upgrade(troops,"flemish_crossbowman","flemish_heavy_crossbowman")

upgrade2(troops,"flemish_militia_pikeman","flemish_pikeman","flemish_halberdier")
upgrade(troops,"flemish_pikeman","flemish_heavy_pikeman")
upgrade(troops,"flemish_halberdier","flemish_heavy_halberdier")

##################################################### GENERIC MERCENARIES
upgrade2(troops,"watchman","caravan_guard","mercenary_spearman")
upgrade(troops,"mercenary_spearman","mercenary_pavise_spearman")
upgrade(troops,"caravan_guard","mercenary_swordsman")
upgrade(troops,"mercenary_swordsman","hired_blade")

upgrade(troops,"mercenary_bowman","mercenary_archer")
upgrade(troops,"mercenary_archer","mercenary_longbowman")

upgrade(troops,"mercenary_scout","mercenary_light_cavalry")
upgrade(troops,"mercenary_light_cavalry","mercenary_cavalry")

upgrade(troops,"genoese_crossbowman","genoese_heavy_crossbowman")

upgrade(troops,"italian_light_infantry","italian_infantry")
upgrade(troops,"italian_infantry","italian_heavy_infantry")

###################################################### CUSTOM TROOPS

upgrade(troops,"custom_merc_recruit","custom_merc_footman")
upgrade(troops,"custom_merc_footman","custom_merc_veteran")
upgrade(troops,"custom_merc_veteran","custom_merc_sergeant")

upgrade(troops,"custom_merc_skirmisher","custom_merc_ranger")
upgrade(troops,"custom_merc_ranger","custom_merc_marksman")

upgrade(troops,"custom_merc_scout","custom_merc_mounted_sergeant")
