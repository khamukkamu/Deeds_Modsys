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

  # Checking center upgrades
  (12,
   [
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
        
        (try_begin),
            (eq, ":cur_improvement", slot_player_camp_level),
            (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
                (try_begin),
                    (eq, ":player_camp_level", 2),
                    (str_store_string, s0, "@Outpost"),     
                (else_try),
                    (eq, ":player_camp_level", 3),
                    (str_store_string, s0, "@Manor"),       
                (else_try),
                    (eq, ":player_camp_level", 4),
                    (str_store_string, s0, "@Stronghold"),     
                (try_end),
        (try_end),
        
        (display_log_message, "@Building of {s0} in {s4} has been completed.", color_good_news),
    (try_end),
    ]),

]