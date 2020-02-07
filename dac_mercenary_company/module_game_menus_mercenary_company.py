from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
#SB : optional menu toggles
# from header_sounds import sf_vol_1
from ID_info_pages import *
from header_triggers import key_left_shift, key_right_shift
from module_constants import *

from compiler import *

# mercenary_company_creation_menus = [
      # ("action_create_camp",[],"Set up an encampment here.",
       # [
        # (party_relocate_near_party, "p_player_camp", "p_main_party"),
        # (enable_party, "p_player_camp"),
        # ]
       # ),
# ]

mercenary_company_menus = [

## DAC Seek: Player Camp Encounter
  (
    "player_camp_encounter",0,
    "You approach your encampment...",
    "none",
    [],
    [
    ("player_camp_meet_quartermaster",
       [],
    "Speak to the Quartermaster.",[
        (modify_visitors_at_site,"scn_player_camp"),
        (reset_visitors),    
        (assign, "$g_mt_mode", tcm_default),   		
        (set_jump_entry, 1),
        (set_visitor, 2, "trp_merc_company_quartermaster"),
        (set_visitor, 5, "trp_custom_merc_recruit"),
        (set_visitor, 6, "trp_custom_merc_veteran"),
        (set_visitor, 7, "trp_custom_merc_veteran"),
        (set_visitor, 8, "trp_custom_merc_elite"),
        (set_visitor, 9, "trp_custom_merc_elite"),
        (set_jump_mission,"mt_visit_town_castle"),
        (jump_to_scene,"scn_player_camp"),
        (change_screen_map_conversation, "trp_merc_company_quartermaster"),
    ]),    
    ("player_camp_enter",
        [],
    "Enter the Encampment.",[
        (modify_visitors_at_site,"scn_player_camp"),
        (reset_visitors),    
        (assign, "$g_mt_mode", tcm_default),   		
        (set_jump_entry, 1),
        (set_visitor, 2, "trp_merc_company_quartermaster"),
        (set_visitor, 5, "trp_custom_merc_recruit"),
        (set_visitor, 6, "trp_custom_merc_veteran"),
        (set_visitor, 7, "trp_custom_merc_veteran"),
        (set_visitor, 8, "trp_custom_merc_elite"),
        (set_visitor, 9, "trp_custom_merc_elite"),
        (set_jump_mission,"mt_visit_town_castle"),
        (jump_to_scene,"scn_player_camp"),
        (change_screen_mission),		
	]),	
      ("player_camp_manage",[],"Manage the encampment.",[(jump_to_menu, "mnu_player_camp_management"),]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),  
## DAC Seek: Player Camp Encounter End

## DAC Seek: Player Camp Management
  (
    "player_camp_management",0,
    "Management Options",
    "none",
    [],
    [
    ("player_camp_upgrade",
       [
        (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),    
        (assign, reg1, ":player_camp_level"),
       ],
    "Upgrade the encampment. (Current level: {reg1})",[
        (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
        (try_begin),
            (lt, ":player_camp_level", 4),  
            (val_add, ":player_camp_level", 1),
            (party_set_slot, "p_player_camp", slot_player_camp_level, ":player_camp_level"),
            (call_script, "script_dac_upgrade_player_camp"),
        (else_try),
            (display_message, "@Max level reached!"),
        (try_end),
        (jump_to_menu, "mnu_player_camp_management"),
    ]),  
    ("player_camp_degrade", # This is just for testing, disable it after system implementation
       [
        (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),    
        (assign, reg1, ":player_camp_level"),
       ],
    "Degrade the encampment. (Current level: {reg1})",[
        (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
        (try_begin),
            (gt, ":player_camp_level", 1),  
            (val_sub, ":player_camp_level", 1),
            (party_set_slot, "p_player_camp", slot_player_camp_level, ":player_camp_level"),
            (call_script, "script_dac_upgrade_player_camp"),
        (else_try),
            (display_message, "@Min level reached!"),
        (try_end),
        (jump_to_menu, "mnu_player_camp_management"),
    ]),     
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),  
## DAC Seek: Player Camp Management End


]