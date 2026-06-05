from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from module_constants import *

from compiler import *

mercenary_company_simple_triggers = [

  # Camp upgrades
  (1,
   [
   
    # Piggyback for CT Smith - DAC Kham ### DAC Seek: Converted to hourly
    (try_begin),
        (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_hours_til_finished, -1),
        (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item),
        (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished),

        (try_begin),
            (le, ":hours_til_finished", 0),
            (str_store_item_name, s1, ":item"),
            (call_script, "script_dac_print_item_commission_targets_to_s2_add_item", 1, ":item"),
            (display_message, "str_dac_player_camp_smith_item_finished", color_good_news),            
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item, -1),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished, -1),
        (else_try),
            (val_sub, ":hours_til_finished", 1),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished, ":hours_til_finished"),
        (try_end),
    (try_end),
    
    (try_begin),
        (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2, -1),
        (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item_2),
        (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2),

        (try_begin),
            (le, ":hours_til_finished", 0),
            (str_store_item_name, s1, ":item"),
            (call_script, "script_dac_print_item_commission_targets_to_s2_add_item", 2, ":item"),
            (display_message, "str_dac_player_camp_smith_item_finished", color_good_news),            
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item_2, -1),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2, -1),
        (else_try),
            (val_sub, ":hours_til_finished", 1),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2, ":hours_til_finished"),
        (try_end),
    (try_end),
    
    (try_begin),
        (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3, -1),
        (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item_3),
        (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3),

        (try_begin),
            (le, ":hours_til_finished", 0),
            (str_store_item_name, s1, ":item"),
            (call_script, "script_dac_print_item_commission_targets_to_s2_add_item", 3, ":item"),
            (display_message, "str_dac_player_camp_smith_item_finished", color_good_news),            
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item_3, -1),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3, -1),
        (else_try),
            (val_sub, ":hours_til_finished", 1),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3, ":hours_til_finished"),
        (try_end),
    (try_end),
    
    
    # DAC Seek: Player Camp buildings
    (party_get_slot, ":cur_improvement", "p_player_camp", slot_center_current_improvement),
    (gt, ":cur_improvement", 0),
    (party_get_slot, ":cur_improvement_end_time", "p_player_camp", slot_center_improvement_end_hour),
    (store_current_hours, ":cur_hours"),
    (ge, ":cur_hours", ":cur_improvement_end_time"),
    
    (try_begin),  
        (neq, ":cur_improvement", slot_player_camp_level),
        (party_set_slot, "p_player_camp", ":cur_improvement", 1),
    (try_end),    
    
    (party_set_slot, "p_player_camp", slot_center_current_improvement, 0),
    (call_script, "script_player_camp_get_improvement_details", ":cur_improvement"),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_town_lord, "trp_player"),
        (str_store_party_name, s4, "p_player_camp"),
        (display_log_message, "@Building of {s0} in {s4} has been completed.", color_good_news),
        
        (try_begin),
            (eq, ":cur_improvement", slot_player_camp_level),
            (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
            (lt, ":player_camp_level", 4),  
            (val_add, ":player_camp_level", 1),
            (party_set_slot, "p_player_camp", slot_player_camp_level, ":player_camp_level"),
            (call_script, "script_dac_upgrade_player_camp"),
        (try_end),
        
        (try_begin),
            (eq, ":cur_improvement", slot_player_camp_market),
            (call_script, "script_refresh_mercenary_camp_merchant_inventory"),
        (try_end),
        
    (try_end),
    
    ]),
    
  # Refresh troops and merchant inventory
  (24 * 3,
   [
    (try_begin),
        (eq, "$player_camp_built", 1),
        (call_script, "script_refresh_mercenary_camp_troops"),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_market, 1),
        (call_script, "script_refresh_mercenary_camp_merchant_inventory"),
    (try_end),
    
    ]),

    # Merc Company Quest / Tutorial Start
  (24,
   [
   
    (try_begin),
        (eq, "$class_type", cc_peasant_revolutionary),
        (assign, ":renown_requirement", 200),
    (else_try),
        (assign, ":renown_requirement", 120),
    (try_end),

    (troop_slot_ge, "trp_player", slot_troop_renown, ":renown_requirement"),
    (quest_slot_eq, "qst_merc_company_tutorial", slot_quest_current_state, 0),
    (lt, "$player_camp_built", 1), # Condottiero Starts with the camp already built

    (assign, "$player_camp_available", 1),
    (jump_to_menu, "mnu_player_camp_notification"),
    
    ]),
]