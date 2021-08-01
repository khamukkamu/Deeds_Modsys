from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

from compiler import *
####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

map_icons = [
    ("player",0,"player", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
    ("player_horseman",0,"player_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0),
    ("gray_knight",0,"knight_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
    ("vaegir_knight",0,"knight_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
    ("flagbearer_a",0,"flagbearer_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
    ("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
    ("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
    ("khergit",0,"khergit_horseman", avatar_scale,snd_gallop, 0.15, 0.173, 0),
    ("khergit_horseman_b",0,"khergit_horseman_b", avatar_scale,snd_gallop, 0.15, 0.173, 0),
    ("axeman",0,"bandit_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
    ("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
    ("woman_b",0,"woman_b", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  
    ("dac_breton_knight",0,"dac_breton_knight", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), 
    ("dac_burgundian_knight",0,"dac_burgundian_knight", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), 
    ("dac_english_knight",0,"dac_english_knight", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), 
    ("dac_french_knight",0,"dac_french_knight", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), 

    ("dac_routier",0,"dac_routier", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),    
    ("dac_flayer",0,"dac_flayer", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),    
    ("dac_retondeur",0,"dac_retondeur", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),    
    ("dac_tard_venu",0,"dac_tard_venu", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),    
    ("dac_rebel_peasants",0,"dac_rebel_peasants", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),    
    ("dac_deserter",0,"dac_deserter", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),    
  
    # ("town",mcn_no_shadow,"icon_town_a", 0.35,0),
    # ("town_steppe",mcn_no_shadow,"icon_town_b", 0.35,0),
    # ("town_desert",mcn_no_shadow,"map_village_a", 0.35,0),
  
    ("village_a",mcn_no_shadow,"map_village_a", 0.45, 0),
    ("village_b",mcn_no_shadow,"map_village_b", 0.45, 0),
    ("village_c",mcn_no_shadow,"map_village_a", 0.45, 0),
    ("village_burnt_a",mcn_no_shadow,"map_village_burnt_a", 0.45, 0),
    ("village_deserted_a",mcn_no_shadow,"map_village_deserted_a", 0.45, 0),
    ("village_burnt_b",mcn_no_shadow,"map_village_burnt_b", 0.45, 0),
    ("village_deserted_b",mcn_no_shadow,"map_village_deserted_b", 0.45, 0),
    ("village_burnt_c",mcn_no_shadow,"map_village_burnt_a", 0.45, 0),
    ("village_deserted_c",mcn_no_shadow,"map_village_deserted_a", 0.45, 0),
    ("village_snow_a",mcn_no_shadow,"map_village_a", 0.45, 0),
    ("village_snow_burnt_a",mcn_no_shadow,"map_village_burnt_a", 0.45, 0),
    ("village_snow_deserted_a",mcn_no_shadow,"map_village_deserted_a", 0.45, 0),


    ("camp",mcn_no_shadow,"camp_tent", 0.13, 0),
    ("ship",mcn_no_shadow,"boat_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
    ("ship_on_land",mcn_no_shadow,"boat_sail_off", 0.23, 0),

### Castles

    ("castle_a",mcn_no_shadow,"icon_castle_a", 0.35,0),
    ("castle_a_breton",mcn_no_shadow,"icon_castle_a_breton", 0.35,0),
    ("castle_a_southern",mcn_no_shadow,"icon_castle_a_southern", 0.35,0),
    
    ("castle_b",mcn_no_shadow,"icon_castle_b", 0.35,0),
    ("castle_b_breton",mcn_no_shadow,"icon_castle_b_breton", 0.35,0),
    ("castle_b_southern",mcn_no_shadow,"icon_castle_b_southern", 0.35,0),
    
    ("castle_bastille",mcn_no_shadow,"icon_castle_bastille", 0.35,0),
    
    ("castle_c",mcn_no_shadow,"icon_castle_c", 0.35,0),
    ("castle_c_breton",mcn_no_shadow,"icon_castle_c_breton", 0.35,0),
    ("castle_c_southern",mcn_no_shadow,"icon_castle_c_southern", 0.35,0),
    ("castle_c_southern_2",mcn_no_shadow,"icon_castle_c_southern_2", 0.35,0),
    
    ("castle_coucy",mcn_no_shadow,"icon_castle_coucy", 0.35,0),
    
    ("castle_d",mcn_no_shadow,"icon_castle_d", 0.35,0),
    ("castle_d_breton",mcn_no_shadow,"icon_castle_d_breton", 0.35,0),
    
    ("castle_e",mcn_no_shadow,"icon_castle_e", 0.35,0),
    
    ("castle_snow_a",mcn_no_shadow,"icon_castle_a", 0.35,0),
    ("castle_snow_b",mcn_no_shadow,"icon_castle_b", 0.35,0),
    
### Towns
    
    ("town_a",mcn_no_shadow,"icon_town_a", 0.35,0),
    ("town_a_breton",mcn_no_shadow,"icon_town_a_breton", 0.35,0),
    ("town_a_southern",mcn_no_shadow,"icon_town_a_southern", 0.35,0),
    ("town_a_southern_2",mcn_no_shadow,"icon_town_a_southern_2", 0.35,0),

    ("town_b",mcn_no_shadow,"icon_town_b", 0.35,0),
    ("town_b_breton",mcn_no_shadow,"icon_town_b_breton", 0.35,0),
    ("town_b_southern",mcn_no_shadow,"icon_town_b_southern", 0.35,0),
    ("town_b_southern_2",mcn_no_shadow,"icon_town_b_southern_2", 0.35,0),
    
    ("town_paris",mcn_no_shadow,"icon_town_paris", 0.35,0),


    ("mule",0,"icon_mule", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
    ("cattle",0,"icon_cow", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
    ("training_ground",mcn_no_shadow,"training", 0.35,0),

    ("bridge_a",mcn_no_shadow,"map_river_bridge_a", 1.0,0),
    ("bridge_b",mcn_no_shadow,"map_river_bridge_b", 1.0,0),
    ("bridge_snow_a",mcn_no_shadow,"map_river_bridge_a", 1.0,0),

    ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
    [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":leader_troop"),
        (try_end),
        ]),
     ]),
    ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
    [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":leader_troop"),
        (try_end),
        ]),
     ]),
    ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
    [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
        (try_end),
        ]),
     ]),

    # Banners
    ("map_flag_a01",0,"map_flag_a01", banner_scale,0),
    ("map_flag_a02",0,"map_flag_a02", banner_scale,0),
    ("map_flag_a03",0,"map_flag_a03", banner_scale,0),
    ("map_flag_a04",0,"map_flag_a04", banner_scale,0),
    ("map_flag_a05",0,"map_flag_a05", banner_scale,0),
    ("map_flag_a06",0,"map_flag_a06", banner_scale,0),
    ("map_flag_a07",0,"map_flag_a07", banner_scale,0),
    ("map_flag_a08",0,"map_flag_a08", banner_scale,0),
    ("map_flag_a09",0,"map_flag_a09", banner_scale,0),
    ("map_flag_a10",0,"map_flag_a10", banner_scale,0),
    ("map_flag_a11",0,"map_flag_a11", banner_scale,0),
    ("map_flag_a12",0,"map_flag_a12", banner_scale,0),
    ("map_flag_a13",0,"map_flag_a13", banner_scale,0),
    ("map_flag_a14",0,"map_flag_a14", banner_scale,0),
    ("map_flag_a15",0,"map_flag_a15", banner_scale,0),
    ("map_flag_a16",0,"map_flag_a16", banner_scale,0),
    ("map_flag_a17",0,"map_flag_a17", banner_scale,0),
    ("map_flag_a18",0,"map_flag_a18", banner_scale,0),
    ("map_flag_a19",0,"map_flag_a19", banner_scale,0),
    ("map_flag_a20",0,"map_flag_a20", banner_scale,0),
    ("map_flag_a21",0,"map_flag_a21", banner_scale,0),

    ("map_flag_b01",0,"map_flag_b01", banner_scale,0),
    ("map_flag_b02",0,"map_flag_b02", banner_scale,0),
    ("map_flag_b03",0,"map_flag_b03", banner_scale,0),
    ("map_flag_b04",0,"map_flag_b04", banner_scale,0),
    ("map_flag_b05",0,"map_flag_b05", banner_scale,0),
    ("map_flag_b06",0,"map_flag_b06", banner_scale,0),
    ("map_flag_b07",0,"map_flag_b07", banner_scale,0),
    ("map_flag_b08",0,"map_flag_b08", banner_scale,0),
    ("map_flag_b09",0,"map_flag_b09", banner_scale,0),
    ("map_flag_b10",0,"map_flag_b10", banner_scale,0),
    ("map_flag_b11",0,"map_flag_b11", banner_scale,0),
    ("map_flag_b12",0,"map_flag_b12", banner_scale,0),
    ("map_flag_b13",0,"map_flag_b13", banner_scale,0),
    ("map_flag_b14",0,"map_flag_b14", banner_scale,0),
    ("map_flag_b15",0,"map_flag_b15", banner_scale,0),
    ("map_flag_b16",0,"map_flag_b16", banner_scale,0),
    ("map_flag_b17",0,"map_flag_b17", banner_scale,0),
    ("map_flag_b18",0,"map_flag_b18", banner_scale,0),
    ("map_flag_b19",0,"map_flag_b19", banner_scale,0),
    ("map_flag_b20",0,"map_flag_b20", banner_scale,0),
    ("map_flag_b21",0,"map_flag_b21", banner_scale,0),

    ("map_flag_c01",0,"map_flag_c01", banner_scale,0),
    ("map_flag_c02",0,"map_flag_c02", banner_scale,0),
    ("map_flag_c03",0,"map_flag_c03", banner_scale,0),
    ("map_flag_c04",0,"map_flag_c04", banner_scale,0),
    ("map_flag_c05",0,"map_flag_c05", banner_scale,0),
    ("map_flag_c06",0,"map_flag_c06", banner_scale,0),
    ("map_flag_c07",0,"map_flag_c07", banner_scale,0),
    ("map_flag_c08",0,"map_flag_c08", banner_scale,0),
    ("map_flag_c09",0,"map_flag_c09", banner_scale,0),
    ("map_flag_c10",0,"map_flag_c10", banner_scale,0),
    ("map_flag_c11",0,"map_flag_c11", banner_scale,0),
    ("map_flag_c12",0,"map_flag_c12", banner_scale,0),
    ("map_flag_c13",0,"map_flag_c13", banner_scale,0),
    ("map_flag_c14",0,"map_flag_c14", banner_scale,0),
    ("map_flag_c15",0,"map_flag_c15", banner_scale,0),
    ("map_flag_c16",0,"map_flag_c16", banner_scale,0),
    ("map_flag_c17",0,"map_flag_c17", banner_scale,0),
    ("map_flag_c18",0,"map_flag_c18", banner_scale,0),
    ("map_flag_c19",0,"map_flag_c19", banner_scale,0),
    ("map_flag_c20",0,"map_flag_c20", banner_scale,0),
    ("map_flag_c21",0,"map_flag_c21", banner_scale,0),

    ("map_flag_d01",0,"map_flag_d01", banner_scale,0),
    ("map_flag_d02",0,"map_flag_d02", banner_scale,0),
    ("map_flag_d03",0,"map_flag_d03", banner_scale,0),
    ("map_flag_d04",0,"map_flag_d04", banner_scale,0),
    ("map_flag_d05",0,"map_flag_d05", banner_scale,0),
    ("map_flag_d06",0,"map_flag_d06", banner_scale,0),
    ("map_flag_d07",0,"map_flag_d07", banner_scale,0),
    ("map_flag_d08",0,"map_flag_d08", banner_scale,0),
    ("map_flag_d09",0,"map_flag_d09", banner_scale,0),
    ("map_flag_d10",0,"map_flag_d10", banner_scale,0),
    ("map_flag_d11",0,"map_flag_d11", banner_scale,0),
    ("map_flag_d12",0,"map_flag_d12", banner_scale,0),
    ("map_flag_d13",0,"map_flag_d13", banner_scale,0),
    ("map_flag_d14",0,"map_flag_d14", banner_scale,0),
    ("map_flag_d15",0,"map_flag_d15", banner_scale,0),
    ("map_flag_d16",0,"map_flag_d16", banner_scale,0),
    ("map_flag_d17",0,"map_flag_d17", banner_scale,0),
    ("map_flag_d18",0,"map_flag_d18", banner_scale,0),
    ("map_flag_d19",0,"map_flag_d19", banner_scale,0),
    # ("map_flag_d20",0,"map_flag_d20", banner_scale,0),
    # ("map_flag_d21",0,"map_flag_d21", banner_scale,0),

    ("map_flag_e01",0,"map_flag_e01", banner_scale,0),
    ("map_flag_e02",0,"map_flag_e02", banner_scale,0),
    ("map_flag_e03",0,"map_flag_e03", banner_scale,0),
    ("map_flag_e04",0,"map_flag_e04", banner_scale,0),
    ("map_flag_e05",0,"map_flag_e05", banner_scale,0),
    ("map_flag_e06",0,"map_flag_e06", banner_scale,0),
    ("map_flag_e07",0,"map_flag_e07", banner_scale,0),
    ("map_flag_e08",0,"map_flag_e08", banner_scale,0),
    ("map_flag_e09",0,"map_flag_e09", banner_scale,0),
    ("map_flag_e10",0,"map_flag_e10", banner_scale,0),
    ("map_flag_e11",0,"map_flag_e11", banner_scale,0),
    ("map_flag_e12",0,"map_flag_e12", banner_scale,0),
    ("map_flag_e13",0,"map_flag_e13", banner_scale,0),
    ("map_flag_e14",0,"map_flag_e14", banner_scale,0),
    # ("map_flag_e15",0,"map_flag_e15", banner_scale,0),
    # ("map_flag_e16",0,"map_flag_e16", banner_scale,0),
    # ("map_flag_e17",0,"map_flag_e17", banner_scale,0),
    # ("map_flag_e18",0,"map_flag_e18", banner_scale,0),
    # ("map_flag_e19",0,"map_flag_e19", banner_scale,0),
    # ("map_flag_e20",0,"map_flag_e20", banner_scale,0),
    # ("map_flag_e21",0,"map_flag_e21", banner_scale,0),  

    ("map_flag_f01",0,"map_flag_f01", banner_scale,0),
    ("map_flag_f02",0,"map_flag_f02", banner_scale,0),
    ("map_flag_f03",0,"map_flag_f03", banner_scale,0),
    ("map_flag_f04",0,"map_flag_f04", banner_scale,0),
    ("map_flag_f05",0,"map_flag_f05", banner_scale,0),
    ("map_flag_f06",0,"map_flag_f06", banner_scale,0),
    ("map_flag_f07",0,"map_flag_f07", banner_scale,0),
    ("map_flag_f08",0,"map_flag_f08", banner_scale,0),
    ("map_flag_f09",0,"map_flag_f09", banner_scale,0),
    ("map_flag_f10",0,"map_flag_f10", banner_scale,0),
    ("map_flag_f11",0,"map_flag_f11", banner_scale,0),
    ("map_flag_f12",0,"map_flag_f12", banner_scale,0),
    ("map_flag_f13",0,"map_flag_f13", banner_scale,0),
    ("map_flag_f14",0,"map_flag_f14", banner_scale,0),
    # ("map_flag_f15",0,"map_flag_f15", banner_scale,0),
    # ("map_flag_f16",0,"map_flag_f16", banner_scale,0),
    # ("map_flag_f17",0,"map_flag_f17", banner_scale,0),
    # ("map_flag_f18",0,"map_flag_f18", banner_scale,0),
    # ("map_flag_f19",0,"map_flag_f19", banner_scale,0),
    # ("map_flag_f20",0,"map_flag_f20", banner_scale,0),
    # ("map_flag_f21",0,"map_flag_f21", banner_scale,0),

    ("map_flag_kingdom_a",0,"map_flag_kingdom_a", banner_scale,0),
    ("map_flag_kingdom_b",0,"map_flag_kingdom_b", banner_scale,0),
    ("map_flag_kingdom_c",0,"map_flag_kingdom_c", banner_scale,0),
    ("map_flag_kingdom_d",0,"map_flag_kingdom_d", banner_scale,0),
    # ("map_flag_kingdom_e",0,"map_flag_kingdom_e", banner_scale,0),
    # ("map_flag_kingdom_f",0,"map_flag_kingdom_f", banner_scale,0),
    # ("map_flag_f14",0,"map_flag_f14", banner_scale,0),
    ("bandit_lair",mcn_no_shadow,"map_bandit_lair", 0.45, 0),
]
