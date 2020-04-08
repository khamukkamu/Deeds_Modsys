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

mercenary_company_menus = [

## DAC Seek: Player Camp Notification
  (
    "player_camp_notification",0,
    "Yet another day is spent on the road... ^Feeling weary and tired, you sit to rest by the campfire as thoughts cycle through your mind. You think of the war and your place in the world, you wonder why the great mercenary companies never reformed as the short-lived peace was broken. Certainly it would be very profitable for a distinguished mercenary company to sell its services to one of the belligerent factions, perhaps you could be the one? You believe you have the experience and the renown to establish your own mercenary company, should you wish to do so. ^(You can now create a mercenary company from the camp menu under 'Take an Action')",
    "none",
    [(set_background_mesh, "mesh_pic_castle1"),],
    [ 
    ("player_camp_start_quest",
       [],
    "Make it your priority.",[
        (change_screen_return),
    ]),  
    ("player_camp_ignore",
       [],
    "Discard that thought.",[
        (change_screen_return),
    ]),  
  ]),

## DAC Seek: Player Camp Encounter
  (
    "player_camp_encounter",0,
    "You approach your {s11}... ^{reg6?^^You are currently upgrading to: {s7}. ^The process will take {reg8} day{reg9?s:} and you won't be able to access the camp until the work is finished.:}",
    "none",
    [
    (str_clear, s11),
    (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
    
    (try_begin),
        (eq, ":player_camp_level", 1),
        (str_store_string, s11, "@Camp"),
        (set_background_mesh, "mesh_pic_camp"),
    (else_try),
        (eq, ":player_camp_level", 2),
        (str_store_string, s11, "@Outpost"),
        (set_background_mesh, "mesh_pic_village_s"),
    (else_try),
        (eq, ":player_camp_level", 3),
        (str_store_string, s11, "@Manor"),
        (set_background_mesh, "mesh_pic_village_p"),
    (else_try),
        (str_store_string, s11, "@Stronghold"),
        (set_background_mesh, "mesh_pic_castle1"),
    (try_end),
        
    (assign, reg6, 0),
    (try_begin),
        (party_get_slot, ":cur_improvement", "p_player_camp", slot_center_current_improvement),
        (eq, ":cur_improvement", slot_player_camp_level),
        (call_script, "script_player_camp_get_improvement_details", ":cur_improvement"),
        (str_store_string, s7, s0),
        (assign, reg6, 1),
        (store_current_hours, ":cur_hours"),
        (party_get_slot, ":finish_time", "p_player_camp", slot_center_improvement_end_hour),
        (val_sub, ":finish_time", ":cur_hours"),
        (store_div, reg8, ":finish_time", 24),
        (val_max, reg8, 1),
        (store_sub, reg9, reg8, 1),
    (try_end),
    ],
    [
    ("player_camp_meet_quartermaster",
       [(eq, reg6, 0),],
    "Speak to the Quartermaster.",[
        (modify_visitors_at_site,"scn_player_camp"),
        (reset_visitors),    
        (assign, "$g_mt_mode", tcm_default),   		
        (set_jump_entry, 1),
        (set_visitor, 2, "trp_merc_company_quartermaster"),
        (jump_to_scene,"scn_player_camp"),
        (change_screen_map_conversation, "trp_merc_company_quartermaster"),
    ]),    
    ("player_camp_meet_smith",
       [(eq, reg6, 0),(party_slot_eq, "p_player_camp", slot_player_camp_smithy, 1),],
    "Speak to the Smith.",[
        (modify_visitors_at_site,"scn_player_camp"),
        (reset_visitors),    
        (assign, "$g_mt_mode", tcm_default),   		
        (set_jump_entry, 1),
        (set_visitor, 3, "trp_merc_company_smith"),
        (jump_to_scene,"scn_player_camp"),
        (change_screen_map_conversation, "trp_merc_company_smith"),
    ]),   
    ("player_camp_meet_merchant",
       [(eq, reg6, 0),(party_slot_eq, "p_player_camp", slot_player_camp_market, 1),],
    "Speak to the Merchant.",[
        (modify_visitors_at_site,"scn_player_camp"),
        (reset_visitors),    
        (assign, "$g_mt_mode", tcm_default),   		
        (set_jump_entry, 1),
        (set_visitor, 4, "trp_merc_company_merchant"),
        (jump_to_scene,"scn_player_camp"),
        (change_screen_map_conversation, "trp_merc_company_merchant"),
    ]), 
    ("player_camp_enter",
        [(eq, reg6, 0),],
    "Enter the {s11}.",[
        (modify_visitors_at_site,"scn_player_camp"),
        (reset_visitors),    
        (assign, "$g_mt_mode", tcm_default),   		
        (set_jump_entry, 1),
        (set_visitor, 2, "trp_merc_company_quartermaster"),
        (try_begin),
            (party_slot_eq, "p_player_camp", slot_player_camp_smithy, 1),
            (set_visitor, 3, "trp_merc_company_smith"),
        (try_end),
        (try_begin),
            (party_slot_eq, "p_player_camp", slot_player_camp_market, 1),
            (set_visitor, 4, "trp_merc_company_merchant"),
        (try_end),
        (set_visitor, 5, "trp_custom_merc_recruit"),
        (set_visitor, 6, "trp_custom_merc_footman"),
        (set_visitor, 7, "trp_custom_merc_footman"),
        (set_visitor, 8, "trp_custom_merc_veteran"),
        (set_visitor, 9, "trp_custom_merc_sergeant"),
        (set_jump_mission,"mt_visit_town_castle"),
        (jump_to_scene,"scn_player_camp"),
        (change_screen_mission),		
	]),	
      ("player_camp_manage",[(eq, reg6, 0),],"Manage the {s11}.",[(jump_to_menu, "mnu_player_camp_management"),]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),  
## DAC Seek: Player Camp Encounter End

## DAC Seek: Player Camp Management
  (
    "player_camp_management",0,
    "Management Options ^{s19}^{reg6?^^You are currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}",
    "none",
    [
    (str_clear, s11),
    (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
    
    (try_begin),
        (eq, ":player_camp_level", 1),
        (str_store_string, s11, "@Camp"),
    (else_try),
        (eq, ":player_camp_level", 2),
        (str_store_string, s11, "@Outpost"),
    (else_try),
        (eq, ":player_camp_level", 3),
        (str_store_string, s11, "@Manor"),
    (else_try),
        (str_store_string, s11, "@Stronghold"),
    (try_end),
    
    (assign, ":num_improvements", 0),
    (str_clear, s18),  

    (try_for_range, ":improvement_no", slot_player_camp_smithy, slot_player_camp_level),
        (party_slot_ge, "p_player_camp", ":improvement_no", 1),
        (val_add,  ":num_improvements", 1),
        (call_script, "script_player_camp_get_improvement_details", ":improvement_no"),
        (try_begin),
            (eq,  ":num_improvements", 1),
            (str_store_string_reg, s18, s0),
        (else_try),
            (str_store_string, s18, "@{!}{s18}, {s0}"),
        (try_end),
    (try_end),

    (try_begin),
        (eq,  ":num_improvements", 0),
        (str_store_string, s19, "@The {s11} has no improvements."),
    (else_try),
        (str_store_string, s19, "@The {s11} has the following improvements: {s18}."),
    (try_end),   

    (assign, reg6, 0),
    (try_begin),
        (party_get_slot, ":cur_improvement", "p_player_camp", slot_center_current_improvement),
        (gt, ":cur_improvement", 0),
        (call_script, "script_player_camp_get_improvement_details", ":cur_improvement"),
        (str_store_string, s7, s0),
        (assign, reg6, 1),
        (store_current_hours, ":cur_hours"),
        (party_get_slot, ":finish_time", "p_player_camp", slot_center_improvement_end_hour),
        (val_sub, ":finish_time", ":cur_hours"),
        (store_div, reg8, ":finish_time", 24),
        (val_max, reg8, 1),
        (store_sub, reg9, reg8, 1),
    (try_end),    
    
    (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),    
    (assign, reg10, ":player_camp_level"),    
    ],
    [    
    ("player_camp_change_name",[],"Change the name of your company.",
       [
       # (assign, "$g_presentation_state", rename_companion),
       # (assign, "$g_player_troop", "trp_merc_company_name"),
       # (start_presentation, "prsnt_name_kingdom"),
       (start_presentation, "prsnt_rename_company"),
       ]),
    ("player_camp_upgrade",
       [
        (eq, reg6, 0),
        (lt, reg10, 4),

       ],
    "Upgrade the {s11}. (Current level: {reg10}, Max level: 4)",[
        (assign, "$g_improvement_type", slot_player_camp_level),
        (jump_to_menu, "mnu_player_camp_build_improvements"),
    ]),  
    # ("player_camp_degrade", # This is just for testing, disable it after system implementation
       # [
        # (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),    
        # (assign, reg1, ":player_camp_level"),
       # ],
    # "Degrade the {s11}. (Current level: {reg1})",[
        # (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
        # (try_begin),
            # (gt, ":player_camp_level", 1),  
            # (val_sub, ":player_camp_level", 1),
            # (party_set_slot, "p_player_camp", slot_player_camp_level, ":player_camp_level"),
            # (call_script, "script_dac_upgrade_player_camp"),
        # (else_try),
            # (display_message, "@Min level reached!"),
        # (try_end),
        # (jump_to_menu, "mnu_player_camp_management"),
    # ]),     
    ("player_camp_build_smithy",
       [
        (eq, reg6, 0), 
        (party_slot_eq, "p_player_camp", slot_player_camp_smithy, -1),
       ],
    "Build a Smithy.",[
        (assign, "$g_improvement_type", slot_player_camp_smithy),
        (jump_to_menu, "mnu_player_camp_build_improvements"),
    ]),    
    ("player_camp_build_archery_range",
       [
        (eq, reg6, 0),
        (ge, reg10, 2),
        (party_slot_eq, "p_player_camp", slot_player_camp_archery_range, -1),
       ],
    "Build an Archery Range.",[
        (assign, "$g_improvement_type", slot_player_camp_archery_range),
        (jump_to_menu, "mnu_player_camp_build_improvements"),
    ]),     
    ("player_camp_build_corral",
       [
        (eq, reg6, 0),
        (ge, reg10, 3),        
        (party_slot_eq, "p_player_camp", slot_player_camp_corral, -1),
       ],
    "Build a Corral.",[
        (assign, "$g_improvement_type", slot_player_camp_corral),
        (jump_to_menu, "mnu_player_camp_build_improvements"),
    ]),    
    ("player_camp_build_market",
       [
        (eq, reg6, 0),
        (ge, reg10, 2),
        (party_slot_eq, "p_player_camp", slot_player_camp_market, -1),
       ],
    "Build a Market.",[
        (assign, "$g_improvement_type", slot_player_camp_market),
        (jump_to_menu, "mnu_player_camp_build_improvements"),
    ]),    
    ("player_camp_build_chapterhouse",
       [
        (eq, reg6, 0),
        (ge, reg10, 4),
        (party_slot_eq, "p_player_camp", slot_player_camp_chapterhouse, -1),
       ],
    "Build a Chapterhouse.",[
        (assign, "$g_improvement_type", slot_player_camp_chapterhouse),
        (jump_to_menu, "mnu_player_camp_build_improvements"),
    ]),      
    ("center_cancel_build",[(eq, reg6, 1),],
      "Cancel building the {s7}.",[
        (party_set_slot, "p_player_camp", slot_center_current_improvement, 0),
        (jump_to_menu, "mnu_player_camp_management"),
        ]),
      ("return",[],"Return.",[(jump_to_menu, "mnu_player_camp_encounter"),]),
    ]
  ),  
## DAC Seek: Player Camp Management End

## DAC Seek: Player Camp Building Begin
  (
    "player_camp_build_improvements",0,
    "{s19} ^As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you {reg5} crowns and will take {reg6} days.",
    "none",
    [
    (call_script, "script_player_camp_get_improvement_details", "$g_improvement_type"),
    (assign, ":improvement_cost", reg0),
    (str_store_string, s4, s0),
    (str_store_string, s19, s1),
    (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
    (assign, ":max_skill", reg0),
    (assign, ":max_skill_owner", reg1),
    (assign, reg2, ":max_skill"),

    (store_sub, ":multiplier", 20, ":max_skill"),
    (val_mul, ":improvement_cost", ":multiplier"),
    (val_div, ":improvement_cost", 20),

    (store_div, ":improvement_time", ":improvement_cost", 200),

    (assign, reg5, ":improvement_cost"),
    (assign, reg6, ":improvement_time"),

    #SB : tableau at bottom
    (try_begin),
        (eq, ":max_skill_owner", "trp_player"),
        (assign, reg3, 1),
    (else_try),
        (assign, reg3, 0),
        (str_store_troop_name, s3, ":max_skill_owner"),
    (try_end),

    #SB : assign globals to be safe
    (assign, "$diplomacy_var", ":improvement_cost"),
    (assign, "$diplomacy_var2", ":improvement_time"),
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":max_skill_owner", pos0),
    ],
    [ 
    ("improve_cont",[
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", "$diplomacy_var")],
    "Build the improvements.", [
        (try_begin), #fast build
            (ge, "$cheat_mode", 1),
            (assign, "$diplomacy_var2", 0),
        (else_try),
            (troop_remove_gold, "trp_player", "$diplomacy_var"),
        (try_end),
        (call_script, "script_improve_player_camp", "$g_encountered_party", "$diplomacy_var2"),
        (jump_to_menu,"mnu_player_camp_management"),
    ]),
    ("improve_not_enough_gold",[
        (store_troop_gold, ":cur_gold", "trp_player"),
        (lt, ":cur_gold", "$diplomacy_var"),
        #SB : disable_menu_option
        (disable_menu_option),
    ],
    "I don't have enough money for that.", []),
      ("forget_it",[], "Forget it.", [(jump_to_menu,"mnu_player_camp_management")]),

    ],
  ),


]