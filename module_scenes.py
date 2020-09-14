from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

from compiler import *
####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

## CC
open_field_small       = "0x00000002296028000005415000003efe00004b34000059be"     #  336*336
open_field_normal      = "0x0000000229602800000691a400003efe00004b34000059be"     #  420*420
open_field_large       = "0x00000002296028000009da7600003efe00004b34000059be"     #  630*630
open_field_extra_large = "0x0000000229602800000d234800003efe00004b34000059be"     #  840*840

forest_small       = "0x30002800000320c80000034e00004b34000059be"     #  200*200
forest_normal      = "0x300028000003e8fa0000034e00004b34000059be"     #  250*250
forest_large       = "0x300028000005dd770000034e00004b34000059be"     #  375*375
forest_extra_large = "0x300028000007D1F40000034e00004b34000059be"     #  500*500
## CC


scenes = [

  ## CC
  ("random_scene_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,forest_small, [],[]),
  ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_normal, [],[]),
  ("random_scene_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_large, [],[]), 
  ("random_scene_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_extra_large, [],[]), 
  ## CC


  ("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),


 ## CC
  # open_field
  ("random_scene_steppe_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_small, [],[], "outer_terrain_steppe"),
  ("random_scene_steppe",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_normal, [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_large, [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_extra_large, [],[], "outer_terrain_steppe"),
  
  ("random_scene_plain_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_small, [],[], "outer_terrain_plain"),
  ("random_scene_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_normal, [],[], "outer_terrain_plain"),
  ("random_scene_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_large, [],[], "outer_terrain_plain"), 
  ("random_scene_plain_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_extra_large, [],[], "outer_terrain_plain"), 
    
  ("random_scene_snow_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_small, [],[], "outer_terrain_snow"),
  ("random_scene_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_normal, [],[], "outer_terrain_snow"),
  ("random_scene_snow_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_large, [],[], "outer_terrain_snow"), 
  ("random_scene_snow_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_extra_large, [],[], "outer_terrain_snow"), 
    
  ("random_scene_desert_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_small, [],[], "outer_terrain_desert_b"),
  ("random_scene_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_normal, [],[], "outer_terrain_desert_b"),
  ("random_scene_desert_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_large, [],[], "outer_terrain_desert_b"), 
  ("random_scene_desert_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, open_field_extra_large, [],[], "outer_terrain_desert_b"), 

  # forest
  ("random_scene_steppe_forest_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_small, [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_normal, [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_forest_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_large, [],[], "outer_terrain_steppe"), 
  ("random_scene_steppe_forest_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_extra_large, [],[], "outer_terrain_steppe"), 
    
  ("random_scene_plain_forest_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_small, [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_normal, [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_large, [],[], "outer_terrain_plain"), 
  ("random_scene_plain_forest_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_extra_large, [],[], "outer_terrain_plain"), 
    
  ("random_scene_snow_forest_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_small, [],[], "outer_terrain_snow"),
  ("random_scene_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_normal, [],[], "outer_terrain_snow"),
  ("random_scene_snow_forest_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_large, [],[], "outer_terrain_snow"), 
  ("random_scene_snow_forest_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_extra_large, [],[], "outer_terrain_snow"), 
    
  ("random_scene_desert_forest_small",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_small, [],[], "outer_terrain_desert"),
  ("random_scene_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_normal, [],[], "outer_terrain_desert"),
  ("random_scene_desert_forest_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_large, [],[], "outer_terrain_desert"), 
  ("random_scene_desert_forest_extra_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, forest_extra_large, [],[], "outer_terrain_desert"), 
  ## CC
  

  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_town_thir_1"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),
  ("quick_battle_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30401ee300059966000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x4c6024e3000691a400001b7c0000591500007b52", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00001d63c005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a078bb2000589630000667200002fb90000179c", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("salt_mine",sf_generate,"none", "none", (-200,-200),(200,200),-100,"0x2a07b23200025896000023ee00007f9c000022a8",  
    [],[], "outer_terrain_steppe"),
  ("novice_ground",sf_indoors,"training_house_a", "bo_training_house_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("zendar_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[], "outer_terrain_plain"),
  ("dhorak_keep",sf_generate,"none", "none", (0,0),(120,120),-100,"0x33a7946000028ca300007f4a0000479400161992",
    ["exit"],[]),
  ("reserved4",sf_generate,"none", "none", (0,0),(120,120),-100,"28791",
    [],[]),
  ("reserved5",sf_generate,"none", "none", (0,0),(120,120),-100,"117828",
    [],[]),
  ("reserved6",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved7",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved8",sf_generate,"none", "none", (0,0),(100,100),-100,"13278",
    [],[]),
  ("reserved9",sf_indoors,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved10",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved11",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved12",sf_indoors,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain"),
  ("tutorial_1",sf_indoors,"tutorial_1_scene", "bo_tutorial_1_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
##  ("tutorial_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003a04ce140005e17a000030030000780e00006979",
##    [],[], "outer_terrain_plain"),
  ("tutorial_2",sf_indoors,"tutorial_2_scene", "bo_tutorial_2_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_3",sf_indoors,"tutorial_3_scene", "bo_tutorial_3_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
  ("tutorial_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),


  ("training_ground_horse_track_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000337553240004d53700000c0500002a0f80006267",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000301553240004d5370000466000002a0f800073f1",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_horse_track_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000400c12b2000515470000216b0000485e00006928",
    [],[], "outer_terrain_plain"),
  #Steppe
  ("training_ground_horse_track_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000200b60320004a5290000180d0000452f00000e90",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001350455c20005194a000041cb00005ae800000ff5",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000532c8dccb0005194a000041cb00005ae800001bdd",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_ranged_melee_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000054327dcba0005194a00001b1d00005ae800004d63",
    [],[], "outer_terrain_plain"),
  #Steppe
  ("training_ground_ranged_melee_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000012247dcba0005194a000041ef00005ae8000050af",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_ranged_melee_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("zendar_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    ["the_happy_boar","","zendar_merchant"],[], "outer_terrain_plain"),
#  ("zendar_center",0,"sargoth_square", "bo_sargoth_square", (-24,-22),(21,13),-100,"0",
#    ["the_happy_boar","","zendar_merchant"],[]),
  ("the_happy_boar",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["zendar_center"],["zendar_chest"]),
  ("zendar_merchant",sf_indoors,"interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    [],[]),

# Tvern names:
  #the shy monkey
  #the singing pumpkin
  #three swords
  #red stag
  #the bard's corner


#interior_tavern_a
#  town_1   Sargoth     #plain
#  town_2   Tihr        #plain
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain  
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe

### DAC French Towns  
# Bourges - BM's Suno
  ("town_1_center", sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

# Orleans - BM's Uxkhal
  ("town_2_center",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

### Tours - BM's Uxkhal
  ("town_3_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

# Poitiers - BM's De-snowed A
  ("town_4_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

# La Rochelle - BM's Praven
  ("town_5_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_beach"),

# Clermont - BM's De-snowed A	
  ("town_6_center", sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

# Moulins - Rus' Wenden
  ("town_7_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300798b2000380e3000037960000573900003f48",
    [],[],"outer_terrain_plain"),

### Aurillac
  ("town_8_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x3000148000025896000074e600006c260000125a",
    [],[],"outer_terrain_plain"),

# Lyon - Rus' Sandomierz
  ("town_9_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",
    [], [], "outer_terrain_steppe"),

### Le Puy
  ("town_10_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),
### Cahors 	
  ("town_11_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
### Rodez	
  ("town_12_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),

#Lectoure - BM's Reyvadin
  ("town_13_center",sf_generate|sf_muddy_water,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

### Tarbes	
  ("town_14_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),


#Toulouse - Rus' Wroclaw
  ("town_15_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000330078adc0005896200003c0800001a3200006859",[], ["town_20_master_craftsman"], "outer_terrain_plain"),

#Carcassonne - BM's Dhirim
  ("town_16_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  # Montpellier - Bowman's Rivacheg
  ("town_17_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
  [],["bonus_chest_1"],"outer_terrain_beach"),
  
# Valence - BM's De-snowed B
  ("town_18_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
	
### Thouars	
  ("town_19_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
    [],[],"outer_terrain_plain"),

  # Tournai - Rus' Riga
  ("town_20_center",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002300785550003c0f30000658f00005ca100003384",
    [], [], "outer_terrain_plain"),
  
### Gien  
  ("town_21_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
    [],[],"outer_terrain_plain"),
### Montargis-le-Franc	
  ("town_22_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x3000148000025896000074e600006c260000125a",
    [],[],"outer_terrain_plain"),

# DAC Town Dupes

# Center

#Albret - BM's Reyvadin
("town_23_center",sf_generate|sf_muddy_water,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),

### Bergerac
("town_24_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
  [],["bonus_chest_3"],"outer_terrain_town_thir_1"),
### Periguex  
("town_25_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),
### Angoulême
("town_26_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
  [],[],"outer_terrain_plain"),


#Limoges - BM's Suno
("town_27_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),

#Angers - Rigo
("town_28_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000330000500000d2348000010610000490600002ff9",[], [], "outer_terrain_steppe"),

### Foix
("town_29_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),

 ### DAC English Towns
#Paris - BM's Uxkhal   
("town_30_center",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),


("town_31_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),

("town_32_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
  [],[],"outer_terrain_plain"),

#Laval - Native Uxkhal
("town_33_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),
#Le Mans - Native Suno
("town_34_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
  [],[],"outer_terrain_town_thir_1"),


#Bordeaux - BM's Praven 
("town_35_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_beach"),

# Chartres - BM's Suno
("town_36_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),

#Rouen - Rus' Sandomierz
("town_37_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",[], [], "outer_terrain_steppe"),


# Caen - Rus' Wenden
("town_38_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300798b2000380e3000037960000573900003f48",
  [], [], "outer_terrain_plain"),

#Harfleur - BM's Praven 
("town_39_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_beach"),

# Cherbourg - BM's Rivacheg
("town_40_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000033000124c000acab40000280700000c9f00000ab5",
  [],["bonus_chest_1"],"outer_terrain_beach_roto"),

("town_41_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
  [],[],"outer_terrain_plain"),

# Calais - BM's Rivacheg
("town_42_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
  [],["bonus_chest_1"],"outer_terrain_beach"),


("town_43_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),

("town_44_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),

# Tartas - Native Rivacheg
("town_45_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300416a600035cd600007ee80000012100003fbc",
    [],["bonus_chest_3"],"outer_terrain_town_thir_1"),


#Dax - BM's Reyvadin 
("town_46_center",sf_generate|sf_muddy_water,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),


# Libourne - Native Suno
("town_47_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
  [],[],"outer_terrain_plain"),
("town_48_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
  [],[],"outer_terrain_plain"),

# Eu - Native Uxkhal
("town_49_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],["bonus_chest_2"],"outer_terrain_plain"),
("town_50_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
  [],[],"outer_terrain_plain"),
("town_51_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),

# Dijon - Rigo
("town_52_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030000500000b26c4000077c40000755f000036f6",[], [], "outer_terrain_plain"),


# Besancon - BM's Suno
("town_53_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),

# Nevers - Rus' Posnan
("town_54_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003b00787520004dd3d000072a000003c780000409f",
  [], [], "outer_terrain_plain"),


("town_55_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
  [],[],"outer_terrain_plain"),

# Troyes - Native Praven
("town_56_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
  [],[],"outer_terrain_town_thir_1"),

# Compiegne - BM's Dhirim
("town_57_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),

# Bruges - BM's Uxkhal
("town_58_center",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),

# Gand - BM's De-snowed A
("town_59_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
  [],[],"outer_terrain_plain"),

# Malines - BM's Reyvadin
("town_60_center",sf_generate|sf_muddy_water,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),


# Boulogne - DNO's Town 8
("town_61_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000124c000acab40000280700000c9f00000ab5",
  [],[],"outer_terrain_beach_roto"),


("town_62_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x3000148000025896000074e600006c260000125a",
    [],[],"outer_terrain_plain"),

# Reims - Rus' Krakow
("town_63_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000230078563000541320000775f000047e900002417",
  [], [], "outer_terrain_plain"),

# Amiens - BM's De-snowed B
("town_64_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
	
("town_65_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
  [],[],"outer_terrain_plain"),

# Rennes - BM's Uxkhal
("town_66_center",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_plain"),
  
# Nantes - BM's Praven 
("town_67_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
  [],[],"outer_terrain_beach"),

# Vannes
("town_68_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300790b20002c8b0000050d500006f8c00006dbd",
  [],["bonus_chest_3"],"outer_terrain_beach"),


# Kemper - Rus' Plock
("town_69_center", sf_generate, "none", "none", (0, 0), (180, 180), -100, "0x30050d0d0002d4b300000e2f000027d200005f66",[], [], "outer_terrain_steppe"),

# Saint Malo - BM's Rivacheg
("town_70_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
  [],["bonus_chest_1"],"outer_terrain_beach"),

# St-Brieuc
("town_71_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300790b20002c8b0000050d500006f8c00006dbd",
  [],["bonus_chest_2"],"outer_terrain_plain"),
("town_72_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
  [],[],"outer_terrain_plain"),


# Rohan - Rus' Gdansk
("town_73_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000002005591e00040506000059a100002cd500005052",[], [], "outer_terrain_steppe"),


# Bourges - BM's Suno
  ("town_1_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_1_seneschal"]),

# Orleans - BM's Uxkhal
  ("town_2_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_2_seneschal"]),


  ("town_3_castle",sf_indoors,"interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_3_seneschal"]),

# Poitiers - BM's De-snowed A	
  ("town_4_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_4_seneschal"]),

# La Rochelle - BM's Praven
  ("town_5_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_5_seneschal"]),

# Clermont - BM's De-snowed A
  ("town_6_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_6_seneschal"]),

# Moulins - Rus' Wenden
  ("town_7_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_7_seneschal"]),

  ("town_8_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_8_seneschal"]),

# Lyon - Rus' Sandomierz
  ("town_9_castle",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",
   ["exit"], ["town_9_seneschal"]),

  ("town_10_castle",sf_indoors,"interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_10_seneschal"]),
  ("town_11_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_11_seneschal"]),
  ("town_12_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_12_seneschal"]),

#Lectoure - BM's Reyvadin
  ("town_13_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_13_seneschal"]),


  ("town_14_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_14_seneschal"]),

#Toulouse - Rus' Wroclaw
  ("town_15_castle", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["town_15_seneschal"]),

#Carcassonne - BM's Dhirim
  ("town_16_castle",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
   ["exit"],["town_16_seneschal"]),

  # Montpellier - Replaced with Bowman's Rivacheg
  ("town_17_castle",0, "none", "none", (-100,-100),(100,100),-100,"0",
  ["exit"],["town_17_seneschal"]),
  
# Valence - BM's De-snowed B 
 ("town_18_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_18_seneschal"]),
	
  ("town_19_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_19_seneschal"]),

  # Tournai - Rus' Riga
  ("town_20_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["town_20_seneschal"]),
  
  ("town_21_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_21_seneschal"]),
  ("town_22_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_22_seneschal"]),

# Town Castle Dupes 

# Albret - BM's Reyvadin
  ("town_23_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_23_seneschal"]),


  ("town_24_castle",sf_indoors,"interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_24_seneschal"]),
  ("town_25_castle",sf_indoors,"interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_25_seneschal"]),
  ("town_26_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_26_seneschal"]),

#Limoges - BM's Suno
  ("town_27_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_27_seneschal"]),


#Angers - Rus' Poznan
  ("town_28_castle", sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["town_28_seneschal"]),

  ("town_29_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_29_seneschal"]),


#Paris - BM's Uxkhal   
  ("town_30_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_30_seneschal"]),


  ("town_31_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_31_seneschal"]),
  
  ("town_32_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_32_seneschal"]),

  ("town_33_castle",sf_indoors,"interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_33_seneschal"]),
  ("town_34_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_34_seneschal"]),


#Bordeaux - BM's Praven 
  ("town_35_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_35_seneschal"]),

  # Chatres - BM's Suno
  ("town_36_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_36_seneschal"]),
  
#Rouen - Rus' Sandomierz
  ("town_37_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["town_37_seneschal"]),


  # Caen - Rus' Wenden
  ("town_38_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_38_seneschal"]),
  
#Harfleur - BM's Praven 
  ("town_39_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_39_seneschal"]),

  # Cherbourg - BM's Rivacheg
  ("town_40_castle",0, "none", "none", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_40_seneschal"]),
  
  ("town_41_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_41_seneschal"]),

  # Calais - BM's Rivacheg
  ("town_42_castle",0, "none", "none", (-100,-100),(100,100),-100,"0",
   ["exit"],["town_42_seneschal"]),
  
  ("town_43_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_43_seneschal"]),

  ("town_44_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_44_seneschal"]),

  ("town_45_castle",sf_indoors,"interior_castle_b", "bo_interior_castle_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_45_seneschal"]),

#Dax - BM's Reyvadin 
  ("town_46_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_46_seneschal"]),

  ("town_47_castle",sf_indoors,"interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_47_seneschal"]),
  ("town_48_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_48_seneschal"]),
  ("town_49_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_49_seneschal"]),
  ("town_50_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_50_seneschal"]),
  ("town_51_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_51_seneschal"]),

# Dijon - Rigo
  ("town_52_castle", sf_indoors, "interior_castle_x", "bo_interior_castle_x", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["town_52_seneschal"]),

# Besancon - BM's Suno
  ("town_53_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_53_seneschal"]),

  # Nevers - Rus' Poznan
  ("town_54_castle", sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_54_seneschal"]),
  

  ("town_55_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_55_seneschal"]),
  ("town_56_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_56_seneschal"]),

# Compiegne - BM's Dhirim
  ("town_57_castle",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_57_seneschal"]),
  
  # Bruges - BM's Uxkhal
  ("town_58_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_58_seneschal"]),
  
# Gand - BM's De-snowed A
  ("town_59_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_59_seneschal"]),

  # Malines - BM's Reyvadin
  ("town_60_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_60_seneschal"]),
  

  ("town_61_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_61_seneschal"]),
  ("town_62_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_62_seneschal"]),
  
  # Reims - Rus' Krakow
  ("town_63_castle",sf_indoors, "interior_castle_x", "bo_interior_castle_x", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_63_seneschal"]),
  
# Amiens - BM's De-snowed B
  ("town_64_castle",sf_indoors,"interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_64_seneschal"]),
	
  ("town_65_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_65_seneschal"]),

  # Rennes - BM's Uxkhal
  ("town_66_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_66_seneschal"]),


# Nantes - BM's Praven 
  ("town_67_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_67_seneschal"]),


  ("town_68_castle",sf_indoors,"interior_castle_g", "bo_interior_castle_g", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_68_seneschal"]),

# Kemper - Rus' Plock
  ("town_69_castle", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["town_69_seneschal"]),


# Saint Malo - BM's Rivacheg
  ("town_70_castle",0, "none", "none", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_70_seneschal"]),
  
  ("town_71_castle",sf_indoors, "interior_castle_i", "bo_interior_castle_i", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_71_seneschal"]),
  ("town_72_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_72_seneschal"]),

# Rohan - Rus' Gdansk
  ("town_73_castle", sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100, -100), (100, 100), -100, "0",
  ["exit"], ["castle_73_seneschal"]),

  

# Bourges - BM's Suno
  ("town_1_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Orleans - BM's Uxkhal
  ("town_2_tavern",sf_indoors, "interior_tavern_d", "bo_interior_tavern_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_3_tavern",sf_indoors,"interior_tavern_d", "bo_interior_tavern_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Poitiers - BM's De-snowed A		
  ("town_4_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# La Rochelle - BM's Praven
  ("town_5_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Clermont - BM's De-snowed A
  ("town_6_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Moulins - Rus' Wenden
  ("town_7_tavern", sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),


  ("town_8_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Lyon - Rus' Sandomierz
  ("town_9_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",
   ["exit"], []),


  ("town_10_tavern",sf_indoors,"interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Lectoure - BM's Reyvadin
  ("town_13_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
  ["exit"],[]),


  ("town_14_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Toulouse - Rus' Wroclaw
  ("town_15_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100, -100), (100, 100), -100, "0",["exit"], []),

#Carcassonne - BM's Dhirim
  ("town_16_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
   ["exit"],[]),

  # Montpellier - Replaced by Bowman's Rivacheg
  ("town_17_tavern",sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100,-100),(100,100),-100,"0",
  ["exit"],[]),

# Valence - BM's De-snowed B  
  ("town_18_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	
  ("town_19_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Tournai - Rus' Riga
  ("town_20_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
 
  ("town_21_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Town Taverns

# Albret - BM's Reyvadin
  ("town_23_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_24_tavern",sf_indoors,"interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[],"outer_terrain_town_thir_1"),
  ("town_25_tavern",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_26_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Limoges - BM's Suno
  ("town_27_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Angers - Rus' Poznan
  ("town_28_tavern", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("town_29_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


#Paris - BM's Uxkhal   
  ("town_30_tavern",sf_indoors, "interior_tavern_d", "bo_interior_tavern_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_31_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_32_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_33_tavern",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_34_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Bordeaux - BM's Praven 
  ("town_35_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Chatres - BM's Suno
  ("town_36_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
#Rouen - Rus' Sandomierz
  ("town_37_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",["exit"], []),


  # Caen - Rus' Wenden
  ("town_38_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
#Harfleur - BM's Praven 
  ("town_39_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Cherbourg - BM's Rivacheg
  ("town_40_tavern",sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_41_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Calais - BM's Rivacheg
  ("town_42_tavern",sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_43_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_44_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_45_tavern",sf_indoors,"interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


#Dax - BM's Reyvadin 
("town_46_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
  ["exit"],[]),

  ("town_47_tavern",sf_indoors,"interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_48_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_49_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_50_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_51_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Dijon - Rigo
  ("town_52_tavern", sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100, -100), (100, 100), -100, "0",["exit"], []),

# Besancon - BM's Suno
  ("town_53_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Nevers - Rus' Poznan
  ("town_54_tavern",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100, -100), (100, 100), -100, "0",
   ["exit"], []),
  

  ("town_55_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_56_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Compiegne - BM's Dhirim
  ("town_57_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Bruges - BM's Uxkhal
  ("town_58_tavern",sf_indoors, "interior_tavern_d", "bo_interior_tavern_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Gand - BM's De-snowed A	
  ("town_59_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Malines - BM's Reyvadin
  ("town_60_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  

# Boulogne - DNO's Town 8
  ("town_61_tavern", sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("town_62_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Reims - Rus' Krakow
  ("town_63_tavern",sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
# Amiens - BM's De-snowed B
  ("town_64_tavern",sf_indoors,"interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	
  ("town_65_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Rennes - BM's Uxkhal
  ("town_66_tavern",sf_indoors, "interior_tavern_d", "bo_interior_tavern_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Nantes - BM's Praven 
  ("town_67_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_68_tavern",sf_indoors,"interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[],"outer_terrain_town_thir_1"),

# Kemper - Rus' Plock
  ("town_69_tavern", sf_indoors, "interior_tavern_d", "bo_interior_tavern_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

# Saint Malo - BM's Rivacheg
  ("town_70_tavern",sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_71_tavern",sf_indoors, "interior_tavern_c", "bo_interior_tavern_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_72_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Rohan - Rus' Gdansk
  ("town_73_tavern", sf_indoors, "interior_tavern_c", "bo_interior_tavern_c", (-100, -100), (100, 100), -100, "0",["exit"], []),


# Bourges - BM's Suno
  ("town_1_store",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Orleans - BM's Uxkhal
  ("town_2_store",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_3_store",sf_indoors,"interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	
# Poitiers - BM's De-snowed A	
  ("town_4_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# La Rochelle - BM's Praven
  ("town_5_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Clermont - BM's De-snowed A
  ("town_6_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Moulins - Rus' Wenden
  ("town_7_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),


  ("town_8_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Lyon - Rus' Sandomierz
  ("town_9_store",sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),


  ("town_10_store",sf_indoors,"interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Lectoure - BM's Reyvadin
  ("town_13_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_14_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Toulouse - Rus' Wroclaw
  ("town_15_store", sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100, -100), (100, 100), -100, "0",["exit"], []),

#Carcassonne - BM's Dhirim
  ("town_16_store",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  # Montpellier - Replaced by Bowman's Rivacheg
  ("town_17_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Valence - BM's De-snowed B  
  ("town_18_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	
  ("town_19_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Tournai - Rus' Riga
  ("town_20_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
  ("town_21_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Town Stores

# Albret - BM's Reyvadin
  ("town_23_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_24_store",sf_indoors,"interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_25_store",sf_indoors,"interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_26_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#Limoges - BM's Suno
  ("town_27_store",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Angers - Rus' Poznan
  ("town_28_store", sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("town_29_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


#Paris - BM's Uxkhal   
  ("town_30_store",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_31_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_32_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_33_store",sf_indoors,"interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_34_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


#Bordeaux - BM's Praven 
  ("town_35_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Chatres - BM's Suno
  ("town_36_store",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
#Rouen - Rus' Sandomierz
  ("town_37_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",["exit"], []),


  # Caen - Rus' Wenden
  ("town_38_store", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
#Harfleur - BM's Praven 
  ("town_39_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Cherbourg - BM's Rivacheg
  ("town_40_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_41_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Calais - BM's Rivacheg
  ("town_42_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_43_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_44_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_45_store",sf_indoors,"interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Dax - BM's Reyvadin 
  ("town_46_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_47_store",sf_indoors,"interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_48_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_49_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_50_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_51_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Dijon - Rigo
  ("town_52_store", sf_indoors, "interior_house_a", "bo_interior_house_a", (-100, -100), (100, 100), -100, "0",["exit"], []),

# Besancon - BM's Suno
  ("town_53_store",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Nevers - Rus' Poznan
  ("town_54_store", sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),


  ("town_55_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_56_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Compiegne - BM's Dhirim
  ("town_57_store",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  #  Bruges - BM's Uxkhal
  ("town_58_store", sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Gand - BM's De-snowed A	
  ("town_59_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Malines - BM's Reyvadin
  ("town_60_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  

  ("town_61_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_62_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Reims - Rus' Krakow
  ("town_63_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
# Amiens - BM's De-snowed B
  ("town_64_store",sf_indoors,"interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	
  ("town_65_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Rennes - BM's Uxkhal
  ("town_66_store", sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  

# Nantes - BM's Praven 
  ("town_67_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_68_store",sf_indoors,"interior_tavern_a", "bo_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Kemper - Rus' Plock
  ("town_69_store", sf_indoors, "interior_town_house_c", "bo_interior_town_house_c", (-100, -100), (100, 100), -100, "0",["exit"], []),

# Saint Malo - BM's Rivacheg
  ("town_70_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_71_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_72_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Rohan - Rus' Gdansk
  ("town_73_store", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100, -100), (100, 100), -100, "0",["exit"], []),

  
# Bourges - BM's Suno
  ("town_1_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Orleans - BM's Uxkhal
  ("town_2_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),


  ("town_3_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
	
# Poitiers - BM De-snowed A		
  ("town_4_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

# La Rochelle - BM's Praven
  ("town_5_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Clermont - BM's De-snowed A
  ("town_6_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Moulins - Rus' Wenden
  ("town_7_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300798b2000380e3000037960000573900003f48",
  [], [], "outer_terrain_steppe"),


  ("town_8_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Lyon - Rus' Sandomierz
  ("town_9_arena",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",
    [], [], "outer_terrain_plain"),


  ("town_10_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  ("town_11_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_12_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),

#Lectoure - BM's Reyvadin
  ("town_13_arena",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_14_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
#Toulouse - Rus' Wroclaw
  ("town_15_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], []),

#Carcassonne - BM's Dhirim
  ("town_16_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  # Montpellier - Replaced by Bowman's Rivacheg
  ("town_17_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
  [],[]),
 
# Valence - BM's De-snowed B 
  ("town_18_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_19_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  # Tournai - Rus' Riga
  ("town_20_arena",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",
    [], [], "outer_terrain_plain"),
  
  ("town_21_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_22_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
 

# Town Arenas

# Albret - BM's Reyvadin
  ("town_23_arena",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_24_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),
  ("town_25_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  ("town_26_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

#Limoges - BM's Suno
  ("town_27_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

#Angers - Rus' Poznan
  ("town_28_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002200005000005f57b00005885000046bd00006d9c",[], [], "outer_terrain_steppe"),

  ("town_29_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),


#Paris - BM's Uxkhal   
  ("town_30_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),


  ("town_31_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_32_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
  ("town_33_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  ("town_34_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),


#Bordeaux - BM's Praven 
  ("town_35_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),



  # Chatres - BM's Suno
  ("town_36_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
#Rouen - Rus' Sandomierz
  ("town_37_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",[], [], "outer_terrain_plain"),


  # Caen - Rus' Wenden
  ("town_38_arena",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300798b2000380e3000037960000573900003f48",
    [], [], "outer_terrain_steppe"),
  
#Harfleur - BM's Praven 
  ("town_39_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  # Cherbourg - BM's Rivacheg
  ("town_40_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  
  ("town_41_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
  # Calais - BM's Rivacheg
  ("town_42_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  
  ("town_43_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_44_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_45_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

#Dax - BM's Reyvadin 
  ("town_46_arena",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  

  ("town_47_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  ("town_48_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_49_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_50_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_51_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Dijon - Rigo
  ("town_52_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_town_thir_1"),


# Besancon - BM's Suno
  ("town_53_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  # Nevers - Rus' Poznan
  ("town_54_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002200005000005f57b00005885000046bd00006d9c",
    [], [], "outer_terrain_plain"),
  

  ("town_55_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_56_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),

# Compiegne - BM's Dhirim
  ("town_57_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
  # Bruges - BM's Uxkhal
  ("town_58_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
# Gand - BM's De-snowed A	
  ("town_59_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),
  
  # Malines - BM's Reyvadin
  ("town_60_arena",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  

  ("town_61_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_beach"),
  ("town_62_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
  # Reims - Rus' Krakow
  ("town_63_arena",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",
    [], [], "outer_terrain_town_thir_1"),
  
# Amiens - BM's De-snowed B
  ("town_64_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
	
  ("town_65_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  # Rennes - BM's Uxkhal
  ("town_66_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Nantes - BM's Praven 

  ("town_67_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_68_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),

# Kemper - Rus' Plock
  ("town_69_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x30050d0d0002d4b300000e2f000027d200005f66",[], [], "outer_terrain_plain"),

# Saint Malo - BM's Rivacheg
  ("town_70_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  
  ("town_71_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_72_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

# Rohan - Rus' Gdansk
  ("town_73_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000002005591e00040506000059a100002cd500005052",[], [], "outer_terrain_steppe"),



# Bourges - BM's Suno
  ("town_1_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),

# Orleans - BM's Uxkhal
  ("town_2_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_3_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
	
# Poitiers - BM's De-snowed A		
  ("town_4_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),

# La Rochelle - BM's Praven
  ("town_5_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_6_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Moulins - Rus' Wenden
  ("town_7_prison",sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),


  ("town_8_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Lyon - Rus' Sandomierz
  ("town_9_prison",sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
  ("town_10_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_11_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_12_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#Lectoure - BM's Reyvadin
  ("town_13_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_14_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),

  #Toulouse - Rus' Wroclaw
  ("town_15_prison", sf_indoors, "interior_prison_a", "bo_interior_prison_a", (-100, -100), (100, 100), -100, "0",["exit"], []),

#Carcassonne - BM's Dhirim
  ("town_16_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  #Montpellier - Replaced by Bowman's Rivacheg
  ("town_17_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Valence - BM's De-snowed B  
  ("town_18_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_20_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_21_prison", sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Town Prisons

# Albret - BM's Reyvadin
  ("town_23_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_24_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_25_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_26_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),

#Limoges - BM's Suno
  ("town_27_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  
#Angers - Rus' Poznan
  ("town_28_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("town_29_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


#Paris - BM's Uxkhal   
  ("town_30_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_31_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_32_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("town_33_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_34_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


#Bordeaux - BM's Praven 
  ("town_35_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Chartres - BM's Suno
  ("town_36_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
   [],[]),
  
#Rouen - Rus' Sandomierz
  ("town_37_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100, -100), (100, 100), -100, "0",["exit"], []),


  # Caen - Rus' Wenden
  ("town_38_prison",sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),

#Harfleur - BM's Praven 
  ("town_39_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Cherbourg - BM's Rivacheg
  ("town_40_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  

  ("town_41_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Calais - BM's Rivacheg
  ("town_42_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  

  ("town_43_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_44_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_45_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

#Dax - BM's Reyvadin 
  ("town_46_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_47_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_48_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_49_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_50_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_51_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Dijon - Rigo
  ("town_52_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

# Besancon - BM's Suno
  ("town_53_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),

  # Nevers - Rus' Posnan
  ("town_54_prison",sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  

  ("town_55_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_56_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Compiegne - BM's Dhirim
  ("town_57_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Bruges - BM's Uxkhal
  ("town_58_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Gand - BM's De-snowed A	
  ("town_59_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Malines - BM's Reyvadin
  ("town_60_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  

  ("town_61_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_62_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  # Reims - Rus' Krakow
  ("town_63_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",
    ["exit"], []),
  
# Amiens - BM's De-snowed B
  ("town_64_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("town_65_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  # Rennes - BM's Uxkhal
  ("town_66_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Nantes - BM's Praven 
  ("town_67_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_68_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

# Kemper - Rus' Plock
  ("town_69_prison", sf_indoors, "interior_prison_f", "bo_interior_prison_f", (-100, -100), (100, 100), -100, "0",["exit"], []),

# Saint Malo - BM's Rivacheg
  ("town_70_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_71_prison",sf_indoors,"dungeon_a", "bo_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_72_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
# Rohan - Rus' Gdansk
  ("town_73_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",["exit"], []),



# Bourges - BM's Suno
  ("town_1_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
   [],[],"outer_terrain_plain"),

# Orleans - BM's Uxkhal
  ("town_2_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),


  ("town_3_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

# Poitiers - BM's De-snowed A		
  ("town_4_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

# La Rochelle - BM's Praven
  ("town_5_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

# Clermont - BM's De-snowed A
  ("town_6_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"sea_outer_terrain_1"),

# Moulins - Rus' Wenden
  ("town_7_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300798b2000380e3000037960000573900003f48",[], [], "outer_terrain_plain"),
  

  ("town_8_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  
# Lyon - Rus' Sandomierz
  ("town_9_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",[], [], "outer_terrain_steppe"),
  

  ("town_10_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_plain"),
  ("town_11_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_12_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),

#Lectoure - BM's Reyvadin
  ("town_13_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  ("town_14_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),

#Toulouse - Rus' Wroclaw
  ("town_15_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000330078adc0005896200003c0800001a3200006859",[], [], "outer_terrain_plain"),

#Carcassonne - BM's Dhirim
  ("town_16_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

  # Montpellier - Replaced by Bowman's Rivacheg
  ("town_17_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
    [],[],"outer_terrain_beach"),

# Valence - BM's De-snowed B	
  ("town_18_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
	
  ("town_19_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),

  # Tournai - Rus' Riga
  ("town_20_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002300785550003c0f30000658f00005ca100003384",
    [], [], "outer_terrain_plain"),
  
  ("town_21_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  ("town_22_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  

# Town Walls

# Albret - BM's Reyvadin
  ("town_23_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

  ("town_24_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_25_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  ("town_26_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),

#Limoges - BM's Suno
  ("town_27_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  #Angers - Rus' Poznan
  ("town_28_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003b00787520004dd3d000072a000003c780000409f",[], [], "outer_terrain_steppe"),

  ("town_29_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),


#Paris - iJustWant2bPure   
  ("town_30_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000230000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),


  ("town_31_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),

  ("town_32_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  
  ("town_33_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  ("town_34_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),


#Bordeaux - BM's Praven 
  ("town_35_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

  # Chartres - BM's Suno
  ("town_36_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
#Rouen - Rus' Sandomierz
  ("town_37_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130001887000334d0000073ed00004f1a00007a35",[], [], "outer_terrain_steppe"),


  # Caen - Rus' Wenden
  ("town_38_walls",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300798b2000380e3000037960000573900003f48",
    [], [], "outer_terrain_plain"),
  
#Harfleur - BM's Praven 
  ("town_39_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

  # Cherbourg - BM's Rivacheg
  ("town_40_walls", sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000124c000acab40000280700000c9f00000ab5",
    [],[],"outer_terrain_beach_roto"),
  

  ("town_41_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300015e300063d8800002757000055df00001b08",
    [],[],"sea_outer_terrain_1"),
  
  # Calais - BM's Rivacheg
  ("town_42_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
    [],[],"outer_terrain_beach"),
  

  ("town_43_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),

  ("town_44_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),

  ("town_45_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130028e320005e17b00004a14000006d70000019d",
    [],[],"outer_terrain_plain"),


#Dax - BM's Reyvadin 
  ("town_46_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),


  ("town_47_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_48_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_49_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  ("town_50_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300015e300063d8800002757000055df00001b08",
    [],[],"sea_outer_terrain_1"),
  ("town_51_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),

# Dijon - Rigo
  ("town_52_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030000500000b26c4000077c40000755f000036f6",[], [], "outer_terrain_plain"),

# Besancon - BM's Suno
  ("town_53_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

  # Nevers - Rus' Posnan
  ("town_54_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003b00787520004dd3d000072a000003c780000409f",
  [], [], "outer_terrain_plain"),
  

  ("town_55_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300015e300063d8800002757000055df00001b08",
    [],[],"sea_outer_terrain_1"),
  ("town_56_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300015e300063d8800002757000055df00001b08",
    [],[],"outer_terrain_plain"),

# Compiegne - BM's Dhirim
  ("town_57_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  # Bruges - BM's Uxkhal
  ("town_58_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
# Gand - BM's De-snowed A	
  ("town_59_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

  # Malines - BM's Reyvadin
  ("town_60_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
# Boulogne - DNO's Town 8
  ("town_61_walls",sf_generate,"none", "none", (0,0),(300,300),-100,"0x000000033000124c000acab40000280700000c9f00000ab5",
    [],[],"outer_terrain_beach_roto"),
  
  ("town_62_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  
  # Reims - Rus' Krakow
  ("town_63_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000230078563000541320000775f000047e900002417",
    [], [], "outer_terrain_plain"),
  
# Amiens - BM's De-snowed B
  ("town_64_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("town_65_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),


  # Rennes - BM's Uxkhal
  ("town_66_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

# Nantes - BM's Praven 

  ("town_67_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),
  
  ("town_68_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_plain"),

# Kemper - Rus' Plock
  ("town_69_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x30050d0d0002d4b300000e2f000027d200005f66",[], [], "outer_terrain_steppe"),

# Saint Malo - BM's Rivacheg
  ("town_70_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
    [],[],"outer_terrain_beach"),
  
  ("town_71_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_plain"),
  ("town_72_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300015e300063d8800002757000055df00001b08",
    [],[],"sea_outer_terrain_1"),

# Rohan - Rus' Gdansk
  ("town_73_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000002005591e00040506000059a100002cd500005052",[], [], "outer_terrain_steppe"),

   

# Bourges - BM's Suno
  ("town_1_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

# Orleans - BM's Uxkhal
  ("town_2_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),


  ("town_3_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[]),
	
# Poitiers - BM De-snowed A		
  ("town_4_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

# La Rochelle - BM's Praven
  ("town_5_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

# Clermont - BM's De-snowed A
  ("town_6_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_plain"),

# Moulins - Rus' Wenden
  ("town_7_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300798b2000380e3000037960000573900003f48",[], [], "outer_terrain_plain"), 


  ("town_8_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),

# Lyon - Rus' Sandomierz
  ("town_9_alley",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",[], [], "outer_terrain_steppe"),


  ("town_10_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_11_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_12_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),

#Lectoure - BM's Reyvadin
  ("town_13_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  ("town_14_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
 #Toulouse - Rus' Wroclaw
  ("town_15_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",[], []),
 
 #Carcassonne - BM's Dhirim
  ("town_16_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  # Montpellier - Replaced by Bowman's Rivacheg
  ("town_17_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
    [],[],"outer_terrain_beach"),
  
# Valence - BM's De-snowed B	  
  ("town_18_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
	
  ("town_19_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),

  # Tournai - Rus' Riga
  ("town_20_alley",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",
  [], [], "outer_terrain_plain"),
  
  ("town_21_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),
  ("town_22_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),

# Town Alleys

# Albret - BM's Reyvadin
  ("town_23_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  ("town_24_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),
  ("town_25_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[]),
  ("town_26_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),

#Limoges - BM's Suno
  ("town_27_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
#Angers - Rus' Poznan
  ("town_28_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000420000500000334ce00001d1100003d0600000d27",[], [], "outer_terrain_steppe"),
  

  ("town_29_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),


#Paris - BM's Uxkhal   
  ("town_30_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),


  ("town_31_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),

  ("town_32_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  
  ("town_33_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[]),
  ("town_34_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),

#Bordeaux - BM's Praven 
  ("town_35_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

  # Chartres - BM's Suno
  ("town_36_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
#Rouen - Rus' Sandomierz
  ("town_37_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",[], [], "outer_terrain_steppe"),


  # Caen - Rus' Wenden
  ("town_38_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000420000500000334ce00001d1100003d0600000d27",
    [], [], "outer_terrain_plain"), 
  
#Harfleur - BM's Praven 
  ("town_39_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

  # Cherbourg - BM's Rivacheg
  ("town_40_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000124c000acab40000280700000c9f00000ab5",
    [],[],"outer_terrain_beach"),
  

  ("town_41_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  
  # Calais - BM's Rivacheg
  ("town_42_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
   [],[],"outer_terrain_beach"),
  

  ("town_43_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),

  ("town_44_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),

  ("town_45_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
#Dax - BM's Reyvadin 
  ("town_46_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

  ("town_47_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_48_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_49_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),
  ("town_50_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_51_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),

# Dijon - Rigo
  ("town_52_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",[], [], "outer_terrain_town_thir_1"),

# Besancon - BM's Suno
  ("town_53_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

  # Nevers - Rus' Posnan
  ("town_54_alley",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000420000500000334ce00001d1100003d0600000d27",
    [], [], "outer_terrain_plain"),
  

  ("town_55_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_56_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),

# Compiegne - BM's Dhirim
  ("town_57_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
  # Bruges - BM's Uxkhal
  ("town_58_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  
# Gand - BM's De-snowed A	
  ("town_59_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d234800005e0c0000699d00000b23",
    [],[],"outer_terrain_steppe"),

  # Malines - BM's Reyvadin
  ("town_60_alley", sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),
  

# Boulogne - DNO's Town 8
  ("town_61_alley",sf_generate,"none", "none", (0,0),(300,300),-100,"0x000000033000124c000acab40000280700000c9f00000ab5",
    [],[],"outer_terrain_beach"),

  ("town_62_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  
  # Reims - Rus' Krakow
  ("town_63_alley",sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",
    [], [], "outer_terrain_town_thir_1"),
  
# Amiens - BM's De-snowed B
  ("town_64_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000fffff000041ef00005ae800003c55",
    [],[]),
  ("town_65_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),

  # Rennes - BM's Uxkhal
  ("town_66_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_plain"),

# Nantes - BM's Praven 
  ("town_67_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c4000053ae00001d83",
    [],[],"outer_terrain_beach"),

  ("town_68_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300790b20002c8b0000050d500006f8c00006dbd",
    [],[],"outer_terrain_beach"),

# Kemper - Rus' Plock
  ("town_69_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",[], [], "outer_terrain_steppe"),

# Saint Malo - BM's Rivacheg
  ("town_70_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000d2348000030c40000061200007962",
    [],[],"outer_terrain_beach"),

  ("town_71_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300790b20002c8b0000050d500006f8c00006dbd",
    [],[],"outer_terrain_plain"),
  ("town_72_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),

# Rohan - Rus' Gdansk
  ("town_73_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000420000500000334ce00001d1100003d0600000d27",[], [], "outer_terrain_steppe"),



# DAC Town Dupes END

#0x30054d228004050000005a768000688400002e3b
#0x30054da28004050000005a76800022aa00002e3b
#Castles:

#       1 Steppe
  ("castle_1_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("castle_1_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_1_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#       2 Plain
  ("castle_2_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000018000055d4a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_2_interior",sf_indoors, "interior_castle_u", "bo_interior_castle_u", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_2_seneschal"]),
  ("castle_2_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",#### B bkullanilmayacak
    [],[]),
#       3 Plain
  ("castle_3_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_3_interior",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_3_seneschal"]),
  ("castle_3_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       4 Plain
  ("castle_4_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300032630004d53700003e24000029a300001809",
    [],[],"outer_terrain_plain"),
  ("castle_4_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_4_seneschal"]),
  ("castle_4_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       5 Plain
  ("castle_5_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300730ba00064d93000039c100002d9600004ced",
    [],[],"outer_terrain_plain"),
  ("castle_5_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_5_seneschal"]),
  ("castle_5_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       6 Plain
  ("castle_6_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b009723200059d6800005f4f0000757f000069cd",
    [],[],"outer_terrain_plain"),
  ("castle_6_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_6_seneschal"]),
  ("castle_6_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       7 Snow
  ("castle_7_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000c007a56300047d1e00006c9100002859000028bc",
    [],[],"outer_terrain_plain"),
  ("castle_7_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_7_seneschal"]),
  ("castle_7_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#       8 Plain
  ("castle_8_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("castle_8_interior",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_8_seneschal"]),
  ("castle_8_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       9 Steppe
  ("castle_9_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002000050000085a110000330d00000b4e00007893",
    [],[],"outer_terrain_steppe"),
  ("castle_9_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_9_seneschal"]),
  ("castle_9_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),
#       10 Steppe  
  ("castle_10_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005a16d000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_10_interior",sf_indoors, "interior_castle_g", "bo_interior_castle_g", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_10_seneschal"]),
  ("castle_10_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),
#       11 Plain
  ("castle_11_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_11_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_11_seneschal"]),
  ("castle_11_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_12_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_town_thir_1"),
  ("castle_12_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_12_seneschal"]),
  ("castle_12_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_13_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_plain"),
  ("castle_13_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_13_seneschal"]),
  ("castle_13_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_14_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025b8d0006459400006a3700002adb00007091",
    [],[],"outer_terrain_plain"),
  ("castle_14_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y" , (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_14_seneschal"]),
  ("castle_14_prison",sf_indoors,"interior_prison_m", "bo_interior_prison_m", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_15_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007941f0005415000007e650000225f00003b3e",
    [],[],"outer_terrain_plain"),
  ("castle_15_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_15_seneschal"]),
  ("castle_15_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_16_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0064a008006bdb9000052f500004725000020c7",
    [],[],"outer_terrain_plain"),
  ("castle_16_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_16_seneschal"]),
  ("castle_16_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Steppe
  ("castle_17_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300399c5000fffff0000290a0000409c00000c49",
    [],[],"outer_terrain_beach"),
  ("castle_17_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_17_seneschal"]),
  ("castle_17_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#      Snow
  ("castle_18_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240079f9e0005695a0000035f00003ef400004aa8",
    [],[],"outer_terrain_plain"),
  ("castle_18_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_18_seneschal"]),
  ("castle_18_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Snow
  ("castle_19_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("castle_19_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_19_seneschal"]),
  ("castle_19_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_20_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
    [],[],"outer_terrain_plain"),
  ("castle_20_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_20_seneschal"]),
  ("castle_20_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_21_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230011ab20005d57800003a2600004b7a000071ef",
    [],[],"outer_terrain_plain"),
  ("castle_21_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_21_seneschal"]),
  ("castle_21_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_22_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_plain"),
  ("castle_22_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_22_seneschal"]),
  ("castle_22_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  
  ("castle_23_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079f9e0005695a0000035f00003ef400004aa8",
    [],[], "outer_terrain_castle_9"),
  ("castle_23_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_23_seneschal"]),
  ("castle_23_prison",sf_indoors,"interior_prison_b", "bo_interior_prison_b", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_24_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000001500062183000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_24_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_24_seneschal"]),
  ("castle_24_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_25_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_plain"),
  ("castle_25_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_25_seneschal"]),
  ("castle_25_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_26_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300730ba00064d93000039c100002d9600004ced",
    [],[],"outer_terrain_plain"),
  ("castle_26_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_26_seneschal"]),
  ("castle_26_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_27_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0064a008006bdb9000052f500004725000020c7",
    [],[],"outer_terrain_plain"),
  ("castle_27_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_27_seneschal"]),
  ("castle_27_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_28_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000018000055d4a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_28_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_28_seneschal"]),
  ("castle_28_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_29_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006400796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_snow"),
  ("castle_29_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_29_seneschal"]),
  ("castle_29_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_30_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230011ab20005d57800003a2600004b7a000071ef",
    [],[],"outer_terrain_plain"),
  ("castle_30_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_30_seneschal"]),
  ("castle_30_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_31_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025b8d0006459400006a3700002adb00007091",
    [],[],"outer_terrain_plain"),
  ("castle_31_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_31_seneschal"]),
  ("castle_31_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_32_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002000050000085a110000330d00000b4e00007893",
    [],[],"outer_terrain_plain"),
  ("castle_32_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_32_seneschal"]),
  ("castle_32_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_33_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006f9bc000011c5000035d100000e36",
    [],[],"outer_terrain_plain"),
  ("castle_33_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_33_seneschal"]),
  ("castle_33_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_34_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b007b232000715c50000084c00001b5b00006580",
    [],[],"outer_terrain_plain"),
  ("castle_34_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_34_seneschal"]),
  ("castle_34_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_35_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_beach"),
  ("castle_35_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_35_seneschal"]),
  ("castle_35_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

# iJustWant2bPure's Château de Verneuil
  ("castle_36_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230000500000d234800000f570000698500002872",
    [],[],"outer_terrain_plain"),
  ("castle_36_interior",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_36_seneschal"]),
  ("castle_36_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_37_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_plain"),
  ("castle_37_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_37_seneschal"]),
  ("castle_37_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_38_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_steppe"),
  ("castle_38_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_38_seneschal"]),
  ("castle_38_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_39_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_39_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_39_seneschal"]),
  ("castle_39_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_40_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000000000047919000041ef00005ae800003c55",
    [],[],"outer_terrain_steppe"),
  ("castle_40_interior",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_40_seneschal"]),
  ("castle_40_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

#SB : fix seneschal references 
# DAC - Replaced 41 - 48 with castles 2, 3, 20, 23 - 27
  #       2 Plain
  ("castle_41_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[],"outer_terrain_plain"),
  ("castle_41_interior",sf_indoors, "interior_castle_u", "bo_interior_castle_u", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_2_seneschal"]),
  ("castle_41_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",#### B bkullanilmayacak
    [],[]),
#       3 Plain
  ("castle_42_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_beach"),
  ("castle_42_interior",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_3_seneschal"]),
  ("castle_42_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),

#       Plain
  ("castle_43_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
    [],[],"outer_terrain_plain"),
  ("castle_43_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_20_seneschal"]),
  ("castle_43_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),


  ("castle_44_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300005000005795e0000339200006c3400004937",
    [],[], "outer_terrain_plain"),
  ("castle_44_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_23_seneschal"]),
  ("castle_44_prison",sf_indoors,"interior_prison_b", "bo_interior_prison_b", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_45_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000000000047919000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_45_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_24_seneschal"]),
  ("castle_45_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_46_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230000500000d234800007e3e00004fd900006cf1",
    [],[],"outer_terrain_plain"),
  ("castle_46_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_25_seneschal"]),
  ("castle_46_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_47_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[],"outer_terrain_plain"),
  ("castle_47_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_26_seneschal"]),
  ("castle_47_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_48_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230000500000d234800007e3e00004fd900006cf1",
    [],[],"outer_terrain_plain"),
  ("castle_48_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_27_seneschal"]),
  ("castle_48_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

# DAC Castle Dupes Begin

#       1 Steppe
  ("castle_49_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("castle_49_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_49_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#       2 Plain
  ("castle_50_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000001500062183000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_50_interior",sf_indoors, "interior_castle_u", "bo_interior_castle_u", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_2_seneschal"]),
  ("castle_50_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",#### B bkullanilmayacak
    [],[]),
#       3 Plain
  ("castle_51_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_51_interior",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_3_seneschal"]),
  ("castle_51_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       4 Plain
  ("castle_52_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_plain"),
  ("castle_52_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_4_seneschal"]),
  ("castle_52_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       5 Plain
  ("castle_53_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d81100057963000062ce0000255800004c09",
    [],[],"outer_terrain_plain"),
  ("castle_53_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_5_seneschal"]),
  ("castle_53_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       6 Plain
  ("castle_54_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b009723200059d6800005f4f0000757f000069cd",
    [],[],"outer_terrain_plain"),
  ("castle_54_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_6_seneschal"]),
  ("castle_54_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       7 Snow
  ("castle_55_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300032630004d53700003e24000029a300001809",
    [],[],"outer_terrain_plain"),
  ("castle_55_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_7_seneschal"]),
  ("castle_55_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#       8 Plain
  ("castle_56_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("castle_56_interior",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_8_seneschal"]),
  ("castle_56_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       9 Steppe
  ("castle_57_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003007a56300047d1e00006c9100002859000028bc",
    [],[],"outer_terrain_steppe"),
  ("castle_57_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_9_seneschal"]),
  ("castle_57_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#       10 Steppe  
  ("castle_58_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000018000055d4a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_58_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_10_seneschal"]),
  ("castle_58_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       11 Plain
  ("castle_59_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_59_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_11_seneschal"]),
  ("castle_59_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_60_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_town_thir_1"),
  ("castle_60_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_12_seneschal"]),
  ("castle_60_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_61_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_plain"),
  ("castle_61_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_13_seneschal"]),
  ("castle_61_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_62_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
    [],[],"outer_terrain_plain"),
  ("castle_62_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y" , (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_14_seneschal"]),
  ("castle_62_prison",sf_indoors,"interior_prison_m", "bo_interior_prison_m", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_63_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_plain"),
  ("castle_63_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_15_seneschal"]),
  ("castle_63_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_64_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0064a008006bdb9000052f500004725000020c7",
    [],[],"outer_terrain_plain"),
  ("castle_64_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_16_seneschal"]),
  ("castle_64_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Steppe
  ("castle_65_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000ad340004d537000024650000253c00000461",
    [],[],"outer_terrain_steppe"),
  ("castle_65_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_17_seneschal"]),
  ("castle_65_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#      Snow
  ("castle_66_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("castle_66_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_18_seneschal"]),
  ("castle_66_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Snow
  ("castle_67_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[],"outer_terrain_plain"),
  ("castle_67_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_19_seneschal"]),
  ("castle_67_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),

# iJustWant2bPure's Château de Clisson
  ("castle_68_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002cf05800465160000251900001eee0000306a",
    [],[],"outer_terrain_plain"),
  ("castle_68_interior",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_20_seneschal"]),
  ("castle_68_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_69_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230011ab20005d57800003a2600004b7a000071ef",
    [],[],"outer_terrain_plain"),
  ("castle_69_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_21_seneschal"]),
  ("castle_69_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_70_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0064a008006bdb9000052f500004725000020c7",
    [],[],"outer_terrain_plain"),
  ("castle_70_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_22_seneschal"]),
  ("castle_70_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  
  ("castle_71_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[], "outer_terrain_plain"),
  ("castle_71_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_23_seneschal"]),
  ("castle_71_prison",sf_indoors,"interior_prison_b", "bo_interior_prison_b", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_72_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000001500062183000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_72_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_24_seneschal"]),
  ("castle_72_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

# iJustWant2bPure's Château de Tonquédec
  ("castle_73_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000761da00003e3f000034b400002490",
    [],[],"outer_terrain_plain"),
  ("castle_73_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_25_seneschal"]),
  ("castle_73_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_74_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005a16d000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_74_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_26_seneschal"]),
  ("castle_74_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_75_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_plain"),
  ("castle_75_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_27_seneschal"]),
  ("castle_75_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

# iJustWant2bPure's Château de Trémazan
  ("castle_76_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000a0748000042490000478a00006309",
    [],[],"outer_terrain_beach"),
  ("castle_76_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_28_seneschal"]),
  ("castle_76_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_77_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230011ab20005d57800003a2600004b7a000071ef",
    [],[],"outer_terrain_plain"),
  ("castle_77_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_29_seneschal"]),
  ("castle_77_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_78_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_plain"),
  ("castle_78_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_30_seneschal"]),
  ("castle_78_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_79_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_plain"),
  ("castle_79_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_31_seneschal"]),
  ("castle_79_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_80_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005a16d000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_80_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_32_seneschal"]),
  ("castle_80_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_81_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029cb2000709c200003c9500004b9b00002f4d",
    [],[],"outer_terrain_plain"),
  ("castle_81_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_33_seneschal"]),
  ("castle_81_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_82_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b007b232000715c50000084c00001b5b00006580",
    [],[],"outer_terrain_plain"),
  ("castle_82_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_34_seneschal"]),
  ("castle_82_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_83_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300009838009024000002b0f0000336a00007686",
    [],[],"outer_terrain_plain"),
  ("castle_83_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_35_seneschal"]),
  ("castle_83_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

# iJustWant2bPure's Suscinio
  ("castle_84_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000094a52000025d20000002400005ffc",
    [],[],"outer_terrain_plain"),
  ("castle_84_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_25_seneschal"]),
  ("castle_84_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

# Castle 85 - 86 replaced with castle 25 - 27
  ("castle_85_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_plain"),
  ("castle_85_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_26_seneschal"]),
  ("castle_85_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_86_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005a16d000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("castle_86_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_27_seneschal"]),
  ("castle_86_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
# DAC Castle Dupes END



#!!Villages !!#
  ("village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030081763000589620000338e00004f2c00005cfb",
    [],[],"outer_terrain_plain"),
  ("village_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003007a21c0003ecfe000001f0000073b100000fd2",
    [],[],"outer_terrain_plain"),
  ("village_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023003dc4e0006118b000029f8000034670000105f",
    [],[],"outer_terrain_plain"),
  ("village_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079732000651a00000044c0000177200000234",
    [],[],"outer_terrain_plain"),
  ("village_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003001ce100006097d0000134c000016d8000042a2",
    [],[],"outer_terrain_plain"),
  ("village_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230035598000761df000058ea000006f3000005e7",
    [],[],"outer_terrain_plain"),
  ("village_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000031059a0d0004792000005c3a00004df500000dbc",
    [],[],"outer_terrain_plain"),
  ("village_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300798320006499200002acc000040d70000421d",
    [],[],"outer_terrain_plain"),
  ("village_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000004300005008005b57000004e31800017d80000754b",
    [],[],"outer_terrain_plain"),
  ("village_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4",
    [],[],"outer_terrain_plain"),
  ("village_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220029c4400077de100002dcc00002edf00003925",
    [],[],"outer_terrain_steppe"),
  ("village_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200213e300077ddf000019d3000034520000626e",
    [],[],"outer_terrain_steppe"),
  ("village_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300265e3400691a400005e4d80006dfa00003bc8",
    [],[], "outer_terrain_plain"),
  ("village_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029ce30004912400002acc000040d7000077db",
    [],[], "outer_terrain_plain"),
  ("village_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300029d4000691a4000015148000335800004190",
    [],[],"outer_terrain_plain"),
  ("village_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240031a0f0006b9ae00006e1b00006e9000007281",
    [],[],"outer_terrain_plain"),
  ("village_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002c003131700066da00000484c000008630000613d",
    [],[],),
  ("village_18",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003561a00070dbe000016f8000010ca000069f8",
    [],[],"outer_terrain_plain"),
  ("village_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003991e0006f1bc000055cc0000085600001563",
    [],[],"outer_terrain_plain"),
  ("village_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_plain"),
  ("village_21",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240024d3800074dcc0000488b0000016100002047",
    [],[],"outer_terrain_plain"),
  ("village_22",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_plain"),
  ("village_23",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300415380007b5e600005f7b00000a9200001615",
    [],[],),
  ("village_24",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002e1ad00048924000031e70000677500002a0c",
    [],[],"outer_terrain_plain"),
  ("village_25",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002d0021ede000775dd000032670000173700007c40",
    [],[],"outer_terrain_steppe"),
  ("village_26",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230020a008005294c000063fc0000771c0000216f",
    [],[],"outer_terrain_plain"),
  ("village_27",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001b2320004a52900004d390000518c00001ab1",
    [],[],"outer_terrain_plain"),
  ("village_28",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022002de4c00077ddd00007e1300000af400006de1",
    [],[],"outer_terrain_steppe"),
  ("village_29",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b2320004f93c000023ed000053e500002949",
    [],[],"outer_terrain_plain"),
  ("village_30",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025e0a0004dd3700004822000032ea0000011b",
    [],[],"outer_terrain_plain"),
  ("village_31",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300619e38003a8ec00004c8380005c6600001cb5", ##0x00000001300619e30003a8ec00004c8380007de100001cb5",
    [],[],"outer_terrain_plain"),
  ("village_32",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300619e30003a8ec00004c8380007de100001cb5",
    [],[],"outer_terrain_plain"),
  ("village_33",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001700000649920000423900007768000062c3",
    [],[],"outer_terrain_plain"),
  ("village_34",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300323e3000611860000392d00005c05000067e1",
    [],[],"outer_terrain_plain"),
  ("village_35",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079cb20005394e00001ef90000753000000731",
    [],[],"outer_terrain_plain"),
  ("village_36",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003a1560006118d00003ce300004123000043b2",
    [],[],"outer_terrain_plain"),
  ("village_37",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022004d36300077dd600002e08000036ab00004651",
    [],[],"outer_terrain_steppe"),
  ("village_38",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e21e0005fd7f000028920000650500005c53",
    [],[],"outer_terrain_plain"),
  ("village_39",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e5990005fd78000069670000446c00007476",
    [],[],"outer_terrain_plain"),
  ("village_40",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220031f6300076dda000056f100004f6d000070b3",
    [],[],"outer_terrain_steppe"),

  ("village_41",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000a3e300062d8d0000444e0000276e00006eb1",
    [],[],"outer_terrain_steppe"),
  ("village_42",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022007b23200062d8d000060b900003b8b00006c93",
    [],[],"outer_terrain_steppe"),
  ("village_43",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000320e0005856300001d770000792700002aa1",
    [],[],"outer_terrain_steppe"),
  ("village_44",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200020200005c574000075480000002d00004be7",
    [],[],"outer_terrain_steppe"),
  ("village_45",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a3df0004e52b0000167700005180000051ea",
    [],[],"outer_terrain_steppe"),
  ("village_46",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a03200061184000058d20000717a00001af0",
    [],[],"outer_terrain_plain"),
  ("village_47",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300621b100051d47000034e300007926000048d3",
    [],[],"outer_terrain_plain"),
  ("village_48",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001b0051ebc00062d8b0000570d00005b3900001ae1",
    [],[],"outer_terrain_plain"),
  ("village_49",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_plain"),
  ("village_50",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_plain"),
  ("village_51",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002b0e30006a5a90000722700002f5200005e2b",
    [],[],"outer_terrain_plain"),
  ("village_52",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220011de30005655900002c2300003b2400000d47",
    [],[],"outer_terrain_steppe"),
  ("village_53",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dd19000691a40000566a000012a000001037",
    [],[],"outer_terrain_plain"),
  ("village_54",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300032300005c5740000243e000056aa00003a7a",
    [],[],"outer_terrain_plain"),
  ("village_55",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300019500006c1b4000065c700002bea0000154e",
    [],[],"outer_terrain_plain"),
  ("village_56",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300296320006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_town_thir_1"),
  ("village_57",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300027b200065d9700004dcf0000212800001bf0",
    [],[],"outer_terrain_plain"),
  ("village_58",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300018e38005e58300000376000027e70000015c",
    [],[],"outer_terrain_plain"),
  ("village_59",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_60",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_61",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300325350006659e0000603500006b0200005676",
    [],[],"outer_terrain_plain"),
  ("village_62",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000143c08f060004e53a00000a500000187700007c9b",
    [],[],"outer_terrain_plain"),
  ("village_63",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a6b20006258b00006bb8000074df00002f18",
    [],[],"outer_terrain_plain"),
  ("village_64",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
  ("village_65",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d8320006358b00006d2b000005d5000023e5",
    [],[],"outer_terrain_plain"),
  ("village_66",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a2b20006097f00001342000050d900003545",
    [],[],"outer_terrain_town_thir_1"),
  ("village_67",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e02d0005ed7800002c2e0000688800005fe4",
    [],[],"outer_terrain_plain"),
  ("village_68",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130079a3200062d8b0000297c00000def000067b7",
    [],[],"outer_terrain_plain"),
  ("village_69",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_70",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_71",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000630079ab20005fd7f0000687300007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_72",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006300654ac00062d910000635800007c9600005d35",
    [],[],"outer_terrain_plain"),
  ("village_73",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079db200050d4500001b4b00007cf400001973",
    [],[],"outer_terrain_plain"),
  ("village_74",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300794320005f17c00003187000051540000350a",
    [],[],"outer_terrain_plain"),
  ("village_75",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002400798b20005ed7b000019160000650f000072d2",
    [],[],"outer_terrain_plain"),
  ("village_76",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022007a7b200045d19000004920000076d00003b0a",
    [],[],"outer_terrain_steppe"),
  ("village_77",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023009629a0005615800005564000023590000579e",
    [],[],"outer_terrain_plain"),
  ("village_78",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023004561e00069da700000f490000256b000058b5",
    [],[],"outer_terrain_plain"),
  ("village_79",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230084fac00057d5f00002ba900004a7a000060be",
    [],[],"outer_terrain_plain"),
  ("village_80",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001b21e0004f13e000042b2000058e400007fce",
    [],[],"outer_terrain_plain"),
  #################### Yeni koyler ######################
  ("village_81",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079ab20005fd7f0000621700007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_82",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002541c00062d8b00000a01000068cb00006d9b",
    [],[],"outer_terrain_plain"),
  ("village_83",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b2320005956300001e640000462c00003a51",
    [],[],"outer_terrain_plain"),
  ("village_84",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130069b270004dd390000689b00002d3b00001876",
    [],[],"outer_terrain_plain"),
  ("village_85",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
    [],[],"outer_terrain_plain"),
  ("village_86",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
    [],[],"outer_terrain_plain"),
  ("village_87",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98a0004dd3000001a5e00005c6200001ec9",
    [],[],"outer_terrain_plain"),
  ("village_88",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a83200049924000049bd00001f7a00006c57",
    [],[],"outer_terrain_steppe"),
  ("village_89",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001200513940005314c00001f6d00006d7700006698",
    [],[],"outer_terrain_steppe"),
  ("village_90",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002cd900005314c00001f6d00006d7700003493",
    [],[],"outer_terrain_steppe"),
	
 # Sarranid Villages 91 - 110 replaced by Village 53 - 72 

  ("village_91",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dd19000691a40000566a000012a000001037",
    [],[],"outer_terrain_plain"),
  ("village_92",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300032300005c5740000243e000056aa00003a7a",
    [],[],"outer_terrain_plain"),
  ("village_93",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300019500006c1b4000065c700002bea0000154e",
    [],[],"outer_terrain_plain"),
  ("village_94",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300296320006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_town_thir_1"),
  ("village_95",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300027b200065d9700004dcf0000212800001bf0",
    [],[],"outer_terrain_plain"),
# Lion D'Angers - Rigo
  ("village_96",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004fd4500006fed000029db00001edd",
    [],[],"outer_terrain_plain"),
  ("village_97",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_98",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_99",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300325350006659e0000603500006b0200005676",
    [],[],"outer_terrain_plain"),
  ("village_100",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000143c08f060004e53a00000a500000187700007c9b",
    [],[],"outer_terrain_plain"),
  ("village_101",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a6b20006258b00006bb8000074df00002f18",
    [],[],"outer_terrain_plain"),
  ("village_102",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
  ("village_103",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d8320006358b00006d2b000005d5000023e5",
    [],[],"outer_terrain_plain"),
  ("village_104",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a2b20006097f00001342000050d900003545",
    [],[],"outer_terrain_town_thir_1"),
  ("village_105",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e02d0005ed7800002c2e0000688800005fe4",
    [],[],"outer_terrain_plain"),
  ("village_106",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130079a3200062d8b0000297c00000def000067b7",
    [],[],"outer_terrain_plain"),
  ("village_107",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_108",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_109",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000630079ab20005fd7f0000687300007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_110",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006300654ac00062d910000635800007c9600005d35",
    [],[],"outer_terrain_plain"),
	
# DAC Village Dupes Begin

  ("village_111",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030081763000589620000338e00004f2c00005cfb",
    [],[],"outer_terrain_plain"),
  ("village_112",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003007a21c0003ecfe000001f0000073b100000fd2",
    [],[],"outer_terrain_plain"),
  ("village_113",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023003dc4e0006118b000029f8000034670000105f",
    [],[],"outer_terrain_plain"),
  ("village_114",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079732000651a00000044c0000177200000234",
    [],[],"outer_terrain_plain"),
  ("village_115",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003001ce100006097d0000134c000016d8000042a2",
    [],[],"outer_terrain_plain"),
  ("village_116",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230035598000761df000058ea000006f3000005e7",
    [],[],"outer_terrain_plain"),
  ("village_117",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000031059a0d0004792000005c3a00004df500000dbc",
    [],[],"outer_terrain_plain"),
  ("village_118",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300798320006499200002acc000040d70000421d",
    [],[],"outer_terrain_plain"),
  ("village_119",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000004300005008005b57000004e31800017d80000754b",
    [],[],"outer_terrain_plain"),
  ("village_120",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4",
    [],[],"outer_terrain_plain"),
  ("village_121",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220029c4400077de100002dcc00002edf00003925",
    [],[],"outer_terrain_steppe"),
  ("village_122",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200213e300077ddf000019d3000034520000626e",
    [],[],"outer_terrain_steppe"),
  ("village_123",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300265e3400691a400005e4d80006dfa00003bc8",
    [],[], "outer_terrain_plain"),
  ("village_124",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029ce30004912400002acc000040d7000077db",
    [],[], "outer_terrain_plain"),
  ("village_125",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300029d4000691a4000015148000335800004190",
    [],[],"outer_terrain_plain"),
  ("village_126",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240031a0f0006b9ae00006e1b00006e9000007281",
    [],[],"outer_terrain_plain"),
  ("village_127",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002c003131700066da00000484c000008630000613d",
    [],[],),
  ("village_128",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003561a00070dbe000016f8000010ca000069f8",
    [],[],"outer_terrain_plain"),
  ("village_129",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006f9bc000011c5000035d100000e36",
    [],[],"outer_terrain_plain"),
  ("village_130",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_plain"),
  ("village_131",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240024d3800074dcc0000488b0000016100002047",
    [],[],"outer_terrain_plain"),
  ("village_132",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_plain"),
  ("village_133",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300415380007b5e600005f7b00000a9200001615",
    [],[],),
  ("village_134",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002e1ad00048924000031e70000677500002a0c",
    [],[],"outer_terrain_plain"),
  ("village_135",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002d0021ede000775dd000032670000173700007c40",
    [],[],"outer_terrain_steppe"),
  ("village_136",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230020a008005294c000063fc0000771c0000216f",
    [],[],"outer_terrain_plain"),
  ("village_137",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001b2320004a52900004d390000518c00001ab1",
    [],[],"outer_terrain_plain"),
# iJustWant2bPure's Verneuil
  ("village_138",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230000500000d234800000f570000698500002872",
    [],[],"outer_terrain_steppe"),
  ("village_139",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b2320004f93c000023ed000053e500002949",
    [],[],"outer_terrain_plain"),
  ("village_140",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025e0a0004dd3700004822000032ea0000011b",
    [],[],"outer_terrain_plain"),
  ("village_141",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300619e38003a8ec00004c8380005c6600001cb5", ##0x00000001300619e30003a8ec00004c8380007de100001cb5",
    [],[],"outer_terrain_plain"),
  ("village_142",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300619e30003a8ec00004c8380007de100001cb5",
    [],[],"outer_terrain_plain"),
  ("village_143",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001700000649920000423900007768000062c3",
    [],[],"outer_terrain_plain"),
  ("village_144",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300323e3000611860000392d00005c05000067e1",
    [],[],"outer_terrain_plain"),
  ("village_145",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079cb20005394e00001ef90000753000000731",
    [],[],"outer_terrain_town_thir_1"),
  ("village_146",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003a1560006118d00003ce300004123000043b2",
    [],[],"outer_terrain_plain"),
  ("village_147",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022004d36300077dd600002e08000036ab00004651",
    [],[],"outer_terrain_steppe"),
  ("village_148",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e21e0005fd7f000028920000650500005c53",
    [],[],"outer_terrain_plain"),
  ("village_149",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e5990005fd78000069670000446c00007476",
    [],[],"outer_terrain_plain"),
  ("village_150",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220031f6300076dda000056f100004f6d000070b3",
    [],[],"outer_terrain_steppe"),

  ("village_151",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000a3e300062d8d0000444e0000276e00006eb1",
    [],[],"outer_terrain_steppe"),
  ("village_152",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022007b23200062d8d000060b900003b8b00006c93",
    [],[],"outer_terrain_steppe"),
  ("village_153",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000320e0005856300001d770000792700002aa1",
    [],[],"outer_terrain_steppe"),
  ("village_154",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200020200005c574000075480000002d00004be7",
    [],[],"outer_terrain_steppe"),
  ("village_155",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a3df0004e52b0000167700005180000051ea",
    [],[],"outer_terrain_steppe"),
  ("village_156",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a03200061184000058d20000717a00001af0",
    [],[],"outer_terrain_plain"),
  ("village_157",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300621b100051d47000034e300007926000048d3",
    [],[],"outer_terrain_plain"),
  ("village_158",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001b0051ebc00062d8b0000570d00005b3900001ae1",
    [],[],"outer_terrain_plain"),
  ("village_159",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_plain"),
  ("village_160",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_plain"),
  ("village_161",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002b0e30006a5a90000722700002f5200005e2b",
    [],[],"outer_terrain_plain"),
  ("village_162",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220011de30005655900002c2300003b2400000d47",
    [],[],"outer_terrain_steppe"),
  ("village_163",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dd19000691a40000566a000012a000001037",
    [],[],"outer_terrain_plain"),
  ("village_164",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300032300005c5740000243e000056aa00003a7a",
    [],[],"outer_terrain_plain"),
  ("village_165",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300019500006c1b4000065c700002bea0000154e",
    [],[],"outer_terrain_plain"),
  ("village_166",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300296320006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_town_thir_1"),
  ("village_167",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300027b200065d9700004dcf0000212800001bf0",
    [],[],"outer_terrain_plain"),
  ("village_168",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300018e38005e58300000376000027e70000015c",
    [],[],"outer_terrain_plain"),
  ("village_169",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_170",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_171",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300325350006659e0000603500006b0200005676",
    [],[],"outer_terrain_plain"),
  ("village_172",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000143c08f060004e53a00000a500000187700007c9b",
    [],[],"outer_terrain_plain"),
  ("village_173",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a6b20006258b00006bb8000074df00002f18",
    [],[],"outer_terrain_plain"),
  ("village_174",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
  ("village_175",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d8320006358b00006d2b000005d5000023e5",
    [],[],"outer_terrain_plain"),
  ("village_176",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a2b20006097f00001342000050d900003545",
    [],[],"outer_terrain_town_thir_1"),
  ("village_177",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e02d0005ed7800002c2e0000688800005fe4",
    [],[],"outer_terrain_plain"),
  ("village_178",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130079a3200062d8b0000297c00000def000067b7",
    [],[],"outer_terrain_plain"),
  ("village_179",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_180",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_181",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000630079ab20005fd7f0000687300007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_182",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006300654ac00062d910000635800007c9600005d35",
    [],[],"outer_terrain_plain"),
  ("village_183",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079db200050d4500001b4b00007cf400001973",
    [],[],"outer_terrain_plain"),
  ("village_184",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300794320005f17c00003187000051540000350a",
    [],[],"outer_terrain_plain"),
  ("village_185",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002400798b20005ed7b000019160000650f000072d2",
    [],[],"outer_terrain_plain"),
  ("village_186",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022007a7b200045d19000004920000076d00003b0a",
    [],[],"outer_terrain_steppe"),
  ("village_187",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023009629a0005615800005564000023590000579e",
    [],[],"outer_terrain_plain"),
  ("village_188",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023004561e00069da700000f490000256b000058b5",
    [],[],"outer_terrain_plain"),
  ("village_189",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230084fac00057d5f00002ba900004a7a000060be",
    [],[],"outer_terrain_plain"),
  ("village_190",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001b21e0004f13e000042b2000058e400007fce",
    [],[],"outer_terrain_plain"),
  #################### Yeni koyler ######################
  ("village_191",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079ab20005fd7f0000621700007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_192",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002541c00062d8b00000a01000068cb00006d9b",
    [],[],"outer_terrain_plain"),
  ("village_193",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b2320005956300001e640000462c00003a51",
    [],[],"outer_terrain_plain"),
  ("village_194",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130069b270004dd390000689b00002d3b00001876",
    [],[],"outer_terrain_plain"),
  ("village_195",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
    [],[],"outer_terrain_plain"),
  ("village_196",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
    [],[],"outer_terrain_plain"),
  ("village_197",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98a0004dd3000001a5e00005c6200001ec9",
    [],[],"outer_terrain_plain"),
  ("village_198",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a83200049924000049bd00001f7a00006c57",
    [],[],"outer_terrain_steppe"),
  ("village_199",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001200513940005314c00001f6d00006d7700006698",
    [],[],"outer_terrain_steppe"),
  ("village_200",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002cd900005314c00001f6d00006d7700003493",
    [],[],"outer_terrain_steppe"),
  
  # Sarranid Villages 201 - 220 replaced by Villages 53-72
  ("village_201",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dd19000691a40000566a000012a000001037",
    [],[],"outer_terrain_plain"),
  ("village_202",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300032300005c5740000243e000056aa00003a7a",
    [],[],"outer_terrain_plain"),
  ("village_203",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300019500006c1b4000065c700002bea0000154e",
    [],[],"outer_terrain_plain"),
  ("village_204",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300296320006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_town_thir_1"),
  ("village_205",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300027b200065d9700004dcf0000212800001bf0",
    [],[],"outer_terrain_plain"),
  ("village_206",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300018e38005e58300000376000027e70000015c",
    [],[],"outer_terrain_plain"),
  ("village_207",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_208",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_209",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300325350006659e0000603500006b0200005676",
    [],[],"outer_terrain_plain"),
  ("village_210",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000143c08f060004e53a00000a500000187700007c9b",
    [],[],"outer_terrain_plain"),
# iJustWant2bPure's Trémazan
  ("village_211",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000a0748000042490000478a00006309",
    [],[],"outer_terrain_beach"),
  ("village_212",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
  ("village_213",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d8320006358b00006d2b000005d5000023e5",
    [],[],"outer_terrain_plain"),
  ("village_214",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a2b20006097f00001342000050d900003545",
    [],[],"outer_terrain_town_thir_1"),
  ("village_215",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e02d0005ed7800002c2e0000688800005fe4",
    [],[],"outer_terrain_plain"),
  ("village_216",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130079a3200062d8b0000297c00000def000067b7",
    [],[],"outer_terrain_plain"),
  ("village_217",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain"),
  ("village_218",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_219",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000630079ab20005fd7f0000687300007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_220",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006300654ac00062d910000635800007c9600005d35",
    [],[],"outer_terrain_plain"),

  ("village_221",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030081763000589620000338e00004f2c00005cfb",
    [],[],"outer_terrain_plain"),
  ("village_222",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003007a21c0003ecfe000001f0000073b100000fd2",
    [],[],"outer_terrain_plain"),
  ("village_223",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023003dc4e0006118b000029f8000034670000105f",
    [],[],"outer_terrain_plain"),
  ("village_224",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079732000651a00000044c0000177200000234",
    [],[],"outer_terrain_plain"),
  ("village_225",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003001ce100006097d0000134c000016d8000042a2",
    [],[],"outer_terrain_plain"),
  ("village_226",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230035598000761df000058ea000006f3000005e7",
    [],[],"outer_terrain_plain"),
  ("village_227",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000031059a0d0004792000005c3a00004df500000dbc",
    [],[],"outer_terrain_plain"),
  ("village_228",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300798320006499200002acc000040d70000421d",
    [],[],"outer_terrain_plain"),
  ("village_229",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000004300005008005b57000004e31800017d80000754b",
    [],[],"outer_terrain_plain"),
  ("village_230",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4",
    [],[],"outer_terrain_plain"),
	("village_231",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220029c4400077de100002dcc00002edf00003925",
    [],[],"outer_terrain_steppe"),
  ("village_232",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200213e300077ddf000019d3000034520000626e",
    [],[],"outer_terrain_steppe"),
  ("village_233",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300265e3400691a400005e4d80006dfa00003bc8",
    [],[], "outer_terrain_plain"),
  
	
  ("field_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a059a5a0009525600002005000060e300001175",
    [],[],"outer_terrain_plain"),
  ("field_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a079a3f000a3a8000006dfd000030a100006522",
    [],[],"outer_terrain_steppe"),
  ("field_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),

  ("test2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0078cb20003fd0000005e480000288c0000286f",
    [],[],"outer_terrain_steppe"),

    ("test3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00511d98004b12e0000039f00004e6300005c7d",
    [],[],"outer_terrain_plain"),

# multiplayer
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2",
    [],[],"outer_terrain_steppe"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89",
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e",
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",   
    [],[],"outer_terrain_plain"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_plain"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"outer_terrain_desert"),       
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c",
    [],[],"outer_terrain_desert"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  ("multi_scene_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002ab630004651800000d7a00007f3100002701",
    [],[],"outer_terrain_plain"),
  ("multi_scene_21",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_beach_snowy"),
  
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("wedding",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0", [],[]),
  ("lair_steppe_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200c69ac80043d0d0000556b0000768400003ea9",
    [],[],"outer_terrain_steppe"), #a box canyon with a spring? -tents...
  ("lair_taiga_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000004c079c3e000499280000420f0000495d000048d6",
    [],[],"outer_terrain_plain"),
  ("lair_desert_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005024cd120005595400003882000037a90000673e",
    [],[],"outer_terrain_desert"), #an encampment in the woods
  ("lair_forest_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00326d90003ecfb0000657e0000213500002461",
    [],[],"outer_terrain_plain"), #a cliffside ledge or cave overlooking a valley
  ("lair_mountain_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200434070004450c000022bf00006ad6000060ed",
    [],[],"outer_terrain_steppe"),
  ("lair_sea_raiders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00562e200040900000063f40000679f00006cda",
    [],[],"sea_outer_terrain_1"), #the longships beached on a hidden cove


  ("quick_battle_scene_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002dee300045d1d000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000250001d630005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_desert_b"),
  ("quick_battle_scene_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002b76300046d2400000190000076300000692a", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000025a00f23700057d5f00006d6a000050ba000036df", 
    [],[], "outer_terrain_desert_b"),
  ("quick_battle_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    [],[],"outer_terrain_plain"),
  ("quick_battle_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("tutorial_training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003000050000046d1b0000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
    
  ("town_1_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_5_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_room",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_room",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_room",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("meeting_scene_steppe",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_steppe_forest",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow_forest",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert_forest",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),

  ("enterprise_tannery",sf_generate,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0x000000012004480500040902000041cb00005ae800000ff5",
    [],[]),
  ("enterprise_winery",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_mill",sf_indoors,"mill_interior", "bo_mill_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_smithy",sf_indoors,"smithy_interior", "bo_smithy_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_dyeworks",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_linen_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_wool_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_brewery",sf_indoors,"brewery_interior", "bo_brewery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_oil_press",sf_indoors,"oil_press_interior", "bo_oil_press_interior", (-40,-40),(40,40),-100,"0",
    [],[]),

 # New Convo Scenes - Kham
("conversation_scene_tld_plain",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_plain"),
("conversation_scene_tld_snow",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_snow"),
("conversation_scene_tld_forest",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_town_thir_1"),

("player_camp",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_plain"),

]
