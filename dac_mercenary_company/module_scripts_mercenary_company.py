from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from header_items import *

from header_parties import *
from header_skills import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *
from module_items import items
# from module_scripts_character_creation import *

from compiler import *

mercenary_company_scripts = [

###################################
# Custom Troops Scripts Begin

### DAC Seek: Init Custom Troops and player camp variables for game_start
("dac_init_custom_troops", [
    # Player Camp
    (assign, "$player_camp_built", 0),
    (party_set_slot, "p_player_camp", slot_player_camp_archery_range, -1),    
    (party_set_slot, "p_player_camp", slot_player_camp_smithy, -1),    
    (party_set_slot, "p_player_camp", slot_player_camp_corral, -1),    
    (party_set_slot, "p_player_camp", slot_player_camp_market, -1),    
    (party_set_slot, "p_player_camp", slot_player_camp_chapterhouse, -1),    
    # Custom Troops
    (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item, -1),
    (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_days_til_finished, -1),
  ]),  

  ("start_customizing", [
    (store_script_param_1, ":troop"),
    
    (store_skill_level, "$g_player_inventory_management", skl_inventory_management, "$g_player_troop"),
    (store_sub, ":skill_raise", 10, "$g_player_inventory_management"),
    (troop_raise_skill, "$g_player_troop", skl_inventory_management, ":skill_raise"),
    (call_script, "script_copy_inventory", "$g_player_troop", "trp_inventory_backup"),
    (call_script, "script_unequip_troop", ":troop"),
    (store_add, ":selection_troop", 2, ":troop"),
    (call_script, "script_copy_inventory", ":selection_troop", "$g_player_troop"),
    (change_screen_loot, ":troop"),
  ]),

  ("finish_customizing", [
    (store_script_param_1, ":troop"),

    (store_sub, ":skill_raise", "$g_player_inventory_management", 10),
    (troop_raise_skill, "$g_player_troop", skl_inventory_management, ":skill_raise"),
    (call_script, "script_copy_inventory", "trp_inventory_backup", "$g_player_troop"),
    (call_script, "script_unequip_troop", ":troop"),
    (store_add, ":bak_troop", 1, ":troop"),
    (call_script, "script_copy_inventory", ":troop", ":bak_troop"),
    (troop_equip_items, ":troop"),
  ]),

  ("unequip_troop", [
    (store_script_param_1, ":troop"),
    
    (try_for_range, ":i_slot", 0, 10),
      (troop_get_inventory_slot, ":item",":troop", ":i_slot"),
      (gt, ":item", 0),
      (troop_get_inventory_slot_modifier, ":imod",":troop", ":i_slot"),
      (troop_set_inventory_slot, ":troop", ":i_slot", -1),
      (troop_add_item, ":troop", ":item", ":imod"),
    (try_end),
  ]),

  ("reload_custom_troops", [
    (try_for_range, ":troop", customizable_troops_begin,  customizable_troops_end),
      (neg|troop_is_hero, ":troop"),
      (store_add, ":bak_troop", 1, ":troop"),
      (call_script, "script_copy_inventory", ":bak_troop", ":troop"),    
      (troop_equip_items, ":troop"),
    (try_end),
  ]),

  ("dac_add_item_to_custom_troop", [
    (store_script_param_1, ":item"),
    
    (try_for_range, ":troop", customizable_troops_begin, customizable_troops_end),
      (troop_is_hero, ":troop"), #DAC Kham: Inventory Troops are Heroes.
      (store_add, ":armoury_troop", 1, ":troop"), #Access the Selection Troop (Armoury)
      (troop_add_item, ":armoury_troop", ":item"),
    (try_end),
  ]),


# Uses trp_temp_troop to gather the items
  # "script_custom_troop_detail_inventory"
  # Output: $temp2 with the quantity of items on inventory
  # Output: trp_temp_array_a, trp_temp_array_b, trp_temp_array_c
  ("custom_troop_detail_inventory_left",
    [# Container 1: selection

      (store_script_param_1, ":troop_id"),
      (create_text_overlay, ":gear_container", "str_empty_string", tf_scrollable),
      (position_set_x, pos1, 40),(position_set_y, pos1, 110),
      (overlay_set_position, ":gear_container", pos1),
      (position_set_x, pos1, 240),(position_set_y, pos1, 500),
      (overlay_set_area_size, ":gear_container", pos1),
      (set_container_overlay, ":gear_container"),
      
      (troop_sort_inventory, ":troop_id"),
      (troop_get_inventory_capacity, ":num_slots", ":troop_id"),
      (store_free_inventory_capacity, ":num_free_slots", ":troop_id"),
      (store_sub, ":num_items", ":num_slots", ":num_free_slots"),
      #(val_sub, ":num_items", 10),
      
      (store_div, ":y_max", ":num_items", 2),
      
      (assign, ":box_incr", 115),
      (val_max, ":y_max", 1),
      (val_mul, ":y_max", ":box_incr"),
      
      (assign, ":x_item", 60),
      (store_add, ":y_item", ":y_max", 60),
      (assign, ":count", 0),
      (assign, ":x_box", 0),
      (assign, ":y_box", ":y_max"),
      
      # 0-70 for body armor, 71-140 for helmet, 141-210 for boots, 211-299 rest
      # 300+ for imod of each item
      (assign, ":limit_temp_c", 300),
      (store_mul, reg0, ":limit_temp_c", 2),
      
      (try_for_range, ":slot", 0, reg0),
        (troop_set_slot, "trp_temp_array_a", ":slot", -1),
        (troop_set_slot, "trp_temp_array_b", ":slot", -1),
        (troop_set_slot, "trp_temp_array_c", ":slot", -1),
      (try_end),
      
      (assign, ":armor_slot", 0),
      (assign, ":helmet_slot", 71),
      (assign, ":boots_slot", 141),
      (assign, ":rest_slot", 211),
      (assign, ":imod_slot_add", 300),
      
      (try_for_range, ":slot", 0, ":num_slots"),
        (troop_get_inventory_slot, ":item", ":troop_id", ":slot"),
        (neq, ":item", -1),
        (troop_get_inventory_slot_modifier, ":item_imod", ":troop_id", ":slot"),
        
        (item_get_type, ":type", ":item"),
        
        (try_begin),
          (eq, ":type", itp_type_body_armor),
          (troop_set_slot, "trp_temp_array_c", ":armor_slot", ":item"),
          (store_add, reg0, ":armor_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":armor_slot", 1),
        (else_try),
          (eq, ":type", itp_type_head_armor),
          (troop_set_slot, "trp_temp_array_c", ":helmet_slot", ":item"),
          (store_add, reg0, ":helmet_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":helmet_slot", 1),
        (else_try),
          (eq, ":type", itp_type_foot_armor),
          (troop_set_slot, "trp_temp_array_c", ":boots_slot", ":item"),
          (store_add, reg0, ":boots_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":boots_slot", 1),
        (else_try),
          (troop_set_slot, "trp_temp_array_c", ":rest_slot", ":item"),
          (store_add, reg0, ":rest_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":rest_slot", 1),
        (try_end),
      (try_end),
      
      (try_for_range, ":slot", 0, ":limit_temp_c"),
        (troop_get_slot, ":item", "trp_temp_array_c", ":slot"),
        
        (try_begin),
          (neq, ":item", -1),
          (store_add, reg0, ":slot", 300),
          (troop_get_slot, ":item_imod", "trp_temp_array_c", reg0),
          
          (val_add, ":count", 1),
          
          (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
          (position_set_x, pos1, ":x_box"),(position_set_y, pos1, ":y_box"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 900),(position_set_y, pos1, 900),
          (overlay_set_size, reg1, pos1),
          (overlay_set_alpha, reg1, 0xFF),
          
          (create_mesh_overlay_with_item_id, reg1, ":item"),
          (position_set_x, pos1, ":x_item"),(position_set_y, pos1, ":y_item"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 1250),(position_set_y, pos1, 1250),
          (overlay_set_size, reg1, pos1),
          
          (val_add, ":x_item", 115),
          (val_add, ":x_box", 115),
          
          (try_begin),# next row items
            (store_mod, ":mod", ":count", 2),
            (eq, ":mod", 0),
            (val_sub, ":y_item", 115),
            (val_sub, ":y_box", 115),
            (assign, ":x_item", 60),
            (assign, ":x_box", 0),
          (try_end),
          
          #tooltip
          (store_add, reg0, ":count", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_a", ":count", reg1),
          (troop_set_slot, "trp_temp_array_b", ":count", ":item"),
          (troop_set_slot, "trp_temp_array_b", reg0, ":item_imod"),
        (try_end),
      (try_end),
      
      (assign, "$temp2", ":count"),
      (set_container_overlay, -1),
      
      # Text about troop inventory
      (try_begin),
        (create_text_overlay, reg1,
          "@Left+Click  to display item on troop.^ Right+Click to remove item from troop inventory.",
        tf_center_justify),
        (position_set_x, pos1, 180),(position_set_y, pos1, 60),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, font_small),(position_set_y, pos1, font_small),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0x000000),
      (try_end),

      (try_begin),
        (create_text_overlay, reg1,
          "@Troop Equipment",
        tf_center_justify),
        (position_set_x, pos1, 160),(position_set_y, pos1, 650),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1500),(position_set_y, pos1, 1500),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0x000000),
      (try_end)
  ]),

# Uses trp_temp_troop to gather the items
  # "script_custom_troop_detail_inventory"
  # Output: $temp with the quantity of items on inventory
  # Output: trp_temp_array_d, trp_temp_array_e, trp_temp_array_f
  ("custom_troop_detail_inventory_right",
    [# Container 1: selection
      (store_script_param_1, ":troop_id"),

      (create_text_overlay, ":gear_container", "str_empty_string", tf_scrollable),
      (position_set_x, pos1, 710),(position_set_y, pos1, 110),
      (overlay_set_position, ":gear_container", pos1),
      (position_set_x, pos1, 240),(position_set_y, pos1, 500),
      (overlay_set_area_size, ":gear_container", pos1),
      (set_container_overlay, ":gear_container"),
      
      (troop_sort_inventory, ":troop_id"),
      (troop_get_inventory_capacity, ":num_slots", ":troop_id"),
      (store_free_inventory_capacity, ":num_free_slots", ":troop_id"),
      (store_sub, ":num_items", ":num_slots", ":num_free_slots"),
      #(val_sub, ":num_items", 10),
      
      (store_div, ":y_max", ":num_items", 1),
      
      (assign, ":box_incr", 115),
      (val_max, ":y_max", 1),
      (val_mul, ":y_max", ":box_incr"),
      
      (assign, ":x_item", 60),
      (store_add, ":y_item", ":y_max", 60),
      (assign, ":count", 0),
      (assign, ":x_box", 0),
      (assign, ":y_box", ":y_max"),
      
      # 0-70 for body armor, 71-140 for helmet, 141-210 for boots, 211-299 rest
      # 300+ for imod of each item
      (assign, ":limit_temp_c", 300),
      (store_mul, reg0, ":limit_temp_c", 2),
      
      (try_for_range, ":slot", 0, reg0),
        (troop_set_slot, "trp_temp_array_d", ":slot", -1),
        (troop_set_slot, "trp_temp_array_e", ":slot", -1),
        (troop_set_slot, "trp_temp_array_f", ":slot", -1),
      (try_end),
      
      (assign, ":armor_slot", 0),
      (assign, ":helmet_slot", 71),
      (assign, ":boots_slot", 141),
      (assign, ":rest_slot", 211),
      (assign, ":imod_slot_add", 300),
      
      (try_for_range, ":slot", 0, ":num_slots"),
        (troop_get_inventory_slot, ":item", ":troop_id", ":slot"),
        (neq, ":item", -1),
        (troop_get_inventory_slot_modifier, ":item_imod", ":troop_id", ":slot"),
        
        (item_get_type, ":type", ":item"),
        
        (try_begin),
          (eq, ":type", itp_type_body_armor),
          (troop_set_slot, "trp_temp_array_f", ":armor_slot", ":item"),
          (store_add, reg0, ":armor_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_f", reg0, ":item_imod"),
          (val_add, ":armor_slot", 1),
        (else_try),
          (eq, ":type", itp_type_head_armor),
          (troop_set_slot, "trp_temp_array_f", ":helmet_slot", ":item"),
          (store_add, reg0, ":helmet_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_f", reg0, ":item_imod"),
          (val_add, ":helmet_slot", 1),
        (else_try),
          (eq, ":type", itp_type_foot_armor),
          (troop_set_slot, "trp_temp_array_f", ":boots_slot", ":item"),
          (store_add, reg0, ":boots_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_f", reg0, ":item_imod"),
          (val_add, ":boots_slot", 1),
        (else_try),
          (troop_set_slot, "trp_temp_array_f", ":rest_slot", ":item"),
          (store_add, reg0, ":rest_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_f", reg0, ":item_imod"),
          (val_add, ":rest_slot", 1),
        (try_end),
      (try_end),
      
      (try_for_range, ":slot", 0, ":limit_temp_c"),
        (troop_get_slot, ":item", "trp_temp_array_f", ":slot"),
        
        (try_begin),
          (neq, ":item", -1),
          (store_add, reg0, ":slot", 300),
          (troop_get_slot, ":item_imod", "trp_temp_array_f", reg0),
          
          (val_add, ":count", 1),
          
          (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
          (position_set_x, pos1, ":x_box"),(position_set_y, pos1, ":y_box"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 900),(position_set_y, pos1, 900),
          (overlay_set_size, reg1, pos1),
          (overlay_set_alpha, reg1, 0xFF),
          
          (create_mesh_overlay_with_item_id, reg1, ":item"),
          (position_set_x, pos1, ":x_item"),(position_set_y, pos1, ":y_item"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 1250),(position_set_y, pos1, 1250),
          (overlay_set_size, reg1, pos1),
          
          (val_add, ":x_item", 115),
          (val_add, ":x_box", 115),
          
          (try_begin),# next row items
            (store_mod, ":mod", ":count", 2),
            (eq, ":mod", 0),
            (val_sub, ":y_item", 115),
            (val_sub, ":y_box", 115),
            (assign, ":x_item", 60),
            (assign, ":x_box", 0),
          (try_end),
          
          #tooltip
          (store_add, reg0, ":count", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_d", ":count", reg1),
          (troop_set_slot, "trp_temp_array_e", ":count", ":item"),
          (troop_set_slot, "trp_temp_array_e", reg0, ":item_imod"),
        (try_end),
      (try_end),
      
      (assign, "$temp", ":count"),
      (set_container_overlay, -1),
      
      # Text about troop inventory
      (try_begin),
        (create_text_overlay, reg1,
          "@Click on pieces of gear^to add to troop inventory.",
        tf_center_justify),
        (position_set_x, pos1, 840),(position_set_y, pos1, 65),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, font_small),(position_set_y, pos1, font_small),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0x000000),
      (try_end),

      (try_begin),
        (create_text_overlay, reg1,
          "@Armoury",
        tf_center_justify),
        (position_set_x, pos1, 820),(position_set_y, pos1, 650),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1500),(position_set_y, pos1, 1500),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0x000000),
      (try_end)
  ]),

# "script_custom_troop_detail_inventory_tooltip"
  ("custom_troop_detail_inventory_tooltip",
    [(try_begin),
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        
        (try_begin),
          (eq, ":enter_leave", 1),
          (close_item_details),
          
        (else_try),
          (assign, ":end_loop", "$temp2"),
          (val_add, ":end_loop", 1),
          
          (try_for_range, ":i", 1, ":end_loop"),
            (troop_get_slot, reg1, "trp_temp_array_a", ":i"),
            (eq, ":object", reg1),
            (troop_get_slot, reg2, "trp_temp_array_b", ":i"),
            
            (store_add, reg3, ":i", 300),
            (troop_get_slot, reg4, "trp_temp_array_b", reg3),
            (overlay_get_position, pos1, ":object"),
            (show_item_details_with_modifier, reg2, reg4, pos1, 100),
            (assign, ":end_loop", 0),
          (try_end),
        (try_end),
      (try_end),]),


# "script_custom_troop_detail_inventory_tooltip"
  ("custom_troop_detail_inventory_tooltip_right",
    [(try_begin),
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        
        (try_begin),
          (eq, ":enter_leave", 1),
          (close_item_details),
          
        (else_try),
          (assign, ":end_loop", "$temp"),
          (val_add, ":end_loop", 1),
          
          (try_for_range, ":i", 1, ":end_loop"),
            (troop_get_slot, reg11, "trp_temp_array_d", ":i"),
            (eq, ":object", reg11),
            (troop_get_slot, reg21, "trp_temp_array_e", ":i"),
            
            (store_add, reg31, ":i", 300),
            (troop_get_slot, reg41, "trp_temp_array_e", reg31),
            (overlay_get_position, pos11, ":object"),
            (show_item_details_with_modifier, reg21, reg41, pos11, 100),
            (assign, ":end_loop", 0),
          (try_end),
        (try_end),
      (try_end),]),


  # "script_custom_troop_detail_add_item_from_armoury"
  # Input: troop_id, $temp2: quantity of items, trp_temp_array_a,
  # trp_temp_array_b
  # Output: reg10 : should update presentation
  ("custom_troop_detail_add_item_from_armoury",
    [(store_script_param_1, ":troop_id"),
      (store_script_param_2, ":object"),
      
      (try_begin),
        # Change gear
        (assign, ":end_loop", "$temp"),
        (val_add, ":end_loop", 1),
        (assign, ":new_item", -1),
        
        (try_for_range, ":i", 1, ":end_loop"),
          (troop_get_slot, reg11, "trp_temp_array_d", ":i"),
          (eq, ":object", reg11),
          (troop_get_slot, ":new_item", "trp_temp_array_e", ":i"),
          (store_add, reg10, ":i", 300),
          (troop_get_slot, ":new_item_imod", "trp_temp_array_e", reg10),
          
          (assign, ":end_loop", 0),
          (troop_add_item, ":troop_id", ":new_item", ":new_item_imod"),
          (troop_sort_inventory, ":troop_id"),
          
        (try_end),
      (try_end),
      
      (start_presentation, "prsnt_name_troop"),
  ]),

# "script_custom_troop_detail_remove_item_from_troop"
  # Input: troop_id, $temp2: quantity of items, trp_temp_array_a,
  # trp_temp_array_b
  # Output: reg10 : should update presentation
  ("custom_troop_detail_remove_item_from_troop",
    [(store_script_param_1, ":troop_id"),
      (store_script_param_2, ":object"),
      
      (try_begin),
        # Change gear
        (assign, ":end_loop", "$temp2"),
        (val_add, ":end_loop", 1),
        (assign, ":new_item", -1),
        
        (try_for_range, ":i", 1, ":end_loop"),
          (troop_get_slot, reg1, "trp_temp_array_a", ":i"),
          (eq, ":object", reg1),
          (troop_get_slot, ":new_item", "trp_temp_array_b", ":i"),
          (store_add, reg0, ":i", 300),
          
          (assign, ":end_loop", 0),
          (troop_remove_item, ":troop_id", ":new_item"),
          (troop_sort_inventory, ":troop_id"),
          
        (try_end),
      (try_end),
      
      (try_begin),
        (is_presentation_active, "prsnt_name_troop"),
        (start_presentation, "prsnt_name_troop"),
      (else_try),
        (start_presentation, "prsnt_dac_ct_view_armoury"),
      (try_end),
  ]),

  # "script_custom_troop_detail_select_item_for_scrap"
  # Input: troop_id, $temp2: quantity of items, trp_temp_array_a,
  # trp_temp_array_b
  # Output: reg10 : should update presentation
  ("custom_troop_detail_select_item_for_scrap",
    [
      (store_script_param_1, ":object"),
      (assign, "$g_item_to_scrap", 0),
      
      (try_begin),
        # Change gear
        (assign, ":end_loop", "$temp2"),
        (val_add, ":end_loop", 1),
        (assign, ":new_item", -1),
        
        (try_for_range, ":i", 1, ":end_loop"),
          (troop_get_slot, reg1, "trp_temp_array_a", ":i"),
          (eq, ":object", reg1),
          (troop_get_slot, ":new_item", "trp_temp_array_b", ":i"),
          
          (assign, ":end_loop", 0),
          (assign, "$g_item_to_scrap", ":new_item"),
          (item_get_value, reg75, "$g_item_to_scrap"),
          (item_get_difficulty, reg85, "$g_item_to_scrap"),
        (try_end),
      (try_end),
      (assign, "$g_presentation_state", 1),
      (try_begin),
        (is_presentation_active, "prsnt_dac_ct_view_armoury"),
        (start_presentation, "prsnt_dac_ct_view_armoury"),
      (else_try),
        (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
      (try_end),
  ]),

  # "script_custom_troop_detail_select_item_for_buying"
  # Input: troop_id, $temp2: quantity of items, trp_temp_array_a,
  # trp_temp_array_b
  # Output: reg10 : should update presentation
  ("custom_troop_detail_select_item_for_buying",
    [
      (store_script_param_1, ":object"),
      (assign, "$g_item_to_buy", 0),
      (try_begin),
        # Change gear
        (assign, ":end_loop", "$temp"),
        (val_add, ":end_loop", 1),
        (assign, ":new_item", -1),
        
        (try_for_range, ":i", 1, ":end_loop"),
          (troop_get_slot, reg11, "trp_temp_array_d", ":i"),
          (eq, ":object", reg11),
          (troop_get_slot, ":new_item", "trp_temp_array_e", ":i"),

          (assign, ":end_loop", 0),
          (assign, "$g_item_to_buy", ":new_item"),
          (item_get_value, reg75, "$g_item_to_buy"),
        (try_end),
      (try_end),
      (assign, "$g_presentation_state", 2),
      
      (start_presentation, "prsnt_dac_ct_view_armoury"),
  ]),


# Uses trp_temp_troop to gather the items
  # "script_custom_troop_detail_inventory"
  # Output: $temp2 with the quantity of items on inventory
  # Output: trp_temp_array_a, trp_temp_array_b, trp_temp_array_c
  ("custom_troop_detail_inventory_armoury",
    [# Container 1: selection

      (store_script_param_1, ":troop_id"),
      (create_text_overlay, ":gear_container", "str_empty_string", tf_scrollable),
      (position_set_x, pos1, 80),(position_set_y, pos1, 190),
      (overlay_set_position, ":gear_container", pos1),
      (position_set_x, pos1, 470),(position_set_y, pos1, 380),
      (overlay_set_area_size, ":gear_container", pos1),
      (set_container_overlay, ":gear_container"),
      
      (troop_sort_inventory, ":troop_id"),
      (troop_get_inventory_capacity, ":num_slots", ":troop_id"),
      (store_free_inventory_capacity, ":num_free_slots", ":troop_id"),
      (store_sub, ":num_items", ":num_slots", ":num_free_slots"),
      #(val_sub, ":num_items", 10),
      
      (store_div, ":y_max", ":num_items", 3),
      
      (assign, ":box_incr", 115),
      (val_max, ":y_max", 3),
      (val_mul, ":y_max", ":box_incr"),
      
      (assign, ":x_item", 60),
      (store_add, ":y_item", ":y_max", 60),
      (assign, ":count", 0),
      (assign, ":x_box", 0),
      (assign, ":y_box", ":y_max"),
      
      # 0-70 for body armor, 71-140 for helmet, 141-210 for boots, 211-299 rest
      # 300+ for imod of each item
      (assign, ":limit_temp_c", 300),
      (store_mul, reg0, ":limit_temp_c", 2),
      
      (try_for_range, ":slot", 0, reg0),
        (troop_set_slot, "trp_temp_array_a", ":slot", -1),
        (troop_set_slot, "trp_temp_array_b", ":slot", -1),
        (troop_set_slot, "trp_temp_array_c", ":slot", -1),
      (try_end),
      
      (assign, ":armor_slot", 0),
      (assign, ":helmet_slot", 71),
      (assign, ":boots_slot", 141),
      (assign, ":rest_slot", 211),
      (assign, ":imod_slot_add", 300),
      
      (try_for_range, ":slot", 0, ":num_slots"),
        (troop_get_inventory_slot, ":item", ":troop_id", ":slot"),
        (neq, ":item", -1),
        (troop_get_inventory_slot_modifier, ":item_imod", ":troop_id", ":slot"),
        (is_between, ":item", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"),
        (item_get_type, ":type", ":item"),
        
        (try_begin),
          (eq, ":type", itp_type_body_armor),
          (troop_set_slot, "trp_temp_array_c", ":armor_slot", ":item"),
          (store_add, reg0, ":armor_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":armor_slot", 1),
        (else_try),
          (eq, ":type", itp_type_head_armor),
          (troop_set_slot, "trp_temp_array_c", ":helmet_slot", ":item"),
          (store_add, reg0, ":helmet_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":helmet_slot", 1),
        (else_try),
          (eq, ":type", itp_type_foot_armor),
          (troop_set_slot, "trp_temp_array_c", ":boots_slot", ":item"),
          (store_add, reg0, ":boots_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":boots_slot", 1),
        (else_try),
          (troop_set_slot, "trp_temp_array_c", ":rest_slot", ":item"),
          (store_add, reg0, ":rest_slot", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_c", reg0, ":item_imod"),
          (val_add, ":rest_slot", 1),
        (try_end),
      (try_end),
      
      (try_for_range, ":slot", 0, ":limit_temp_c"),
        (troop_get_slot, ":item", "trp_temp_array_c", ":slot"),
        
        (try_begin),
          (neq, ":item", -1),
          (store_add, reg0, ":slot", 300),
          (troop_get_slot, ":item_imod", "trp_temp_array_c", reg0),
          
          (val_add, ":count", 1),
          
          (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
          (position_set_x, pos1, ":x_box"),(position_set_y, pos1, ":y_box"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 900),(position_set_y, pos1, 900),
          (overlay_set_size, reg1, pos1),
          (overlay_set_alpha, reg1, 0xFF),
          
          (create_mesh_overlay_with_item_id, reg1, ":item"),
          (position_set_x, pos1, ":x_item"),(position_set_y, pos1, ":y_item"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 1250),(position_set_y, pos1, 1250),
          (overlay_set_size, reg1, pos1),
          
          (val_add, ":x_item", 115),
          (val_add, ":x_box", 115),
          
          (try_begin),# next row items
            (store_mod, ":mod", ":count", 4),
            (eq, ":mod", 0),
            (val_sub, ":y_item", 115),
            (val_sub, ":y_box", 115),
            (assign, ":x_item", 60),
            (assign, ":x_box", 0),
          (try_end),
          
          #tooltip
          (store_add, reg0, ":count", ":imod_slot_add"),
          (troop_set_slot, "trp_temp_array_a", ":count", reg1),
          (troop_set_slot, "trp_temp_array_b", ":count", ":item"),
          (troop_set_slot, "trp_temp_array_b", reg0, ":item_imod"),
        (try_end),
      (try_end),
      
      (assign, "$temp2", ":count"),
      (set_container_overlay, -1),
      
      (try_begin),
        (is_presentation_active, "prsnt_dac_ct_view_armoury"),
        (str_store_string, s57, "@This is your Company's Armoury. All your Company Troops have access^however, some may not have the stats to use them^Left+Click to sell item for scrap."),
      (else_try),
        (str_store_string, s57, "@You can only reproduce what you present to your Quartermaster.^Left+Click to buy an item for the armoury."),
      (try_end),
      # Text about troop inventory
      (try_begin),
        (create_text_overlay, reg1,
          s57,
        tf_left_align),
        (position_set_x, pos1, 85),(position_set_y, pos1, 145),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, font_small),(position_set_y, pos1, font_small),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0x000000),
      (try_end),
  ]),



# Custom Troops End

### DAC Seek: Player Camp Scripts

("dac_upgrade_player_camp", [
    (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
    
    (try_begin),
        (eq, ":player_camp_level", 1),
        (party_set_icon, "p_player_camp", "icon_camp"),
        (str_store_string, s1, "@Encampment"),
    (else_try), 
        (eq, ":player_camp_level", 2),
        (party_set_icon, "p_player_camp", "icon_village_a"),
        (str_store_string, s1, "@Outpost"),
    (else_try),         
        (eq, ":player_camp_level", 3),
        (party_set_icon, "p_player_camp", "icon_castle_e"),
        (str_store_string, s1, "@Manor"),
    (else_try), 
        (eq, ":player_camp_level", 4),
        (party_set_icon, "p_player_camp", "icon_castle_a"),
        (str_store_string, s1, "@Stronghold"),
    (try_end), 
    
    (str_store_troop_name_plural, s0, "trp_merc_company_name"),
    (str_store_string, s1, "str_s0_s1"),    
    (party_set_name, "p_player_camp", s1),
]),
  
("improve_player_camp", [
    (store_script_param, ":center_no", 1),
    (store_script_param, ":improvement_time", 2),
    
    (party_set_slot, ":center_no", slot_center_current_improvement, "$g_improvement_type"),
    (store_current_hours, ":cur_hours"),
    (store_mul, ":hours_takes", ":improvement_time", 24),
    (val_add, ":hours_takes", ":cur_hours"),
    (party_set_slot, ":center_no", slot_center_improvement_end_hour, ":hours_takes"),
    (assign, reg6, ":improvement_time"),
    (call_script, "script_player_camp_get_improvement_details", "$g_improvement_type"),
    (add_party_note_from_sreg, ":center_no", 2, "@A {s0} is being built. It will finish in {reg6} days", 1),
    
    # (try_begin),
        # (eq, "$g_improvement_type", slot_player_camp_level),
        # (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
        # (lt, ":player_camp_level", 4),  
        # (val_add, ":player_camp_level", 1),
        # (party_set_slot, "p_player_camp", slot_player_camp_level, ":player_camp_level"),
        # (call_script, "script_dac_upgrade_player_camp"),
    # (try_end),  
]),  

("player_camp_get_improvement_details",
    [
    (store_script_param, ":improvement_no", 1),
    (try_begin),
        (eq, ":improvement_no", slot_player_camp_smithy),
        (str_store_string, s0, "@Smithy"),
        (str_store_string, s1, "@A smithy allows the option to produce new equipment for your mercenary company."),
        (assign, reg0, 5000),
    (else_try),
        (eq, ":improvement_no", slot_player_camp_archery_range),
        (str_store_string, s0, "@Archery Range"),
        (str_store_string, s1, "@An archery range grants you access to ranged troops for your mercenary company."),
        (assign, reg0, 3000),
    (else_try),
        (eq, ":improvement_no", slot_player_camp_corral),
        (str_store_string, s0, "@Corral"),
        (str_store_string, s1, "@A corral grants you access to mounted troops for your mercenary company."),
        (assign, reg0, 5000),
    (else_try),
        (eq, ":improvement_no", slot_player_camp_market),
        (str_store_string, s0, "@Marketplace"),
        (str_store_string, s1, "@A marketplace grants you access to a trader and slightly reduces the upkeep for your mercenary company troops."),
        (assign, reg0, 2500),
    (else_try),
        (eq, ":improvement_no", slot_player_camp_chapterhouse),
        (str_store_string, s0, "@Chapterhouse"),
        (str_store_string, s1, "@A chapterhouse grants you access to knights and allows you to create your own knighthood order."),
        (assign, reg0, 1500),
    # (else_try),
        # (party_get_slot, ":cur_improvement", "p_player_camp", slot_center_current_improvement),
        # (eq, ":cur_improvement", slot_player_camp_level),
        # (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
        # (try_begin),
            # (eq, ":player_camp_level", 2),
            # (str_store_string, s0, "@Outpost"),   
        # (else_try),
            # (eq, ":player_camp_level", 3),
            # (str_store_string, s0, "@Manor"),      
        # (else_try),
            # (eq, ":player_camp_level", 4),
            # (str_store_string, s0, "@Stronghold"),    
        # (try_end),
    (else_try),        
        (eq, ":improvement_no", slot_player_camp_level),
        (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
        (try_begin),
            (eq, ":player_camp_level", 1),
            (str_store_string, s0, "@Outpost"),
            (str_store_string, s1, "@Upgrading the encampment to an outpost grants you access to the archery range and marketplace buildings. ^Warning: Upgrading the base will lock access to it until the improvements are finished."),
            (assign, reg0, 5000),        
        (else_try),
            (eq, ":player_camp_level", 2),
            (str_store_string, s0, "@Manor"),
            (str_store_string, s1, "@Upgrading the outpost to a manor grants you access to the corral building. ^Warning: Upgrading the base will lock access to it until the improvements are finished."),
            (assign, reg0, 10000),        
        (else_try),
            (eq, ":player_camp_level", 3),
            (str_store_string, s0, "@Stronghold"),
            (str_store_string, s1, "@Upgrading the manor to a stronghold grants you access to the chapterhouse building. ^Warning: Upgrading the base will lock access to it until the improvements are finished."),
            (assign, reg0, 20000),        
        (try_end),
    (try_end),
]),

  # script_refresh_mercenary_camp_troops
  # Input: none
  # Output: none
  ("refresh_mercenary_camp_troops",
    [
    (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),
    
    (try_begin),
        (eq, ":player_camp_level", 1),
        (assign, ":ideal_size", 10),
    (else_try),
        (eq, ":player_camp_level", 2),
        (assign, ":ideal_size", 20),
    (else_try),
        (eq, ":player_camp_level", 3),
        (assign, ":ideal_size", 30),
    (else_try),
        (assign, ":ideal_size", 40),        
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_archery_range, 1),
        (val_add, ":ideal_size", 10),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
        (val_add, ":ideal_size", 5),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_chapterhouse, 1),
        (val_add, ":ideal_size", 10),
    (try_end),
    
    # Debug
    (assign, reg30, ":ideal_size"),
    (display_message, "@Player camp max size set to {reg30}"),

    (party_get_num_companions, ":party_size", "p_player_camp"),	
    (try_begin),
        (gt, ":party_size", ":ideal_size"), # We're past the ideal number of troops in the camp
        (party_clear,"p_player_camp"), # Reset the troop pool
    (try_end), 
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
        (party_add_template, "p_player_camp", "pt_mercenary_company_cavalry"),	  
        (display_message, "@Cavalry template added to camp"),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_archery_range, 1),
        (party_add_template, "p_player_camp", "pt_mercenary_company_ranged"),	  
        (display_message, "@Ranged template added to camp"),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_chapterhouse, 1),
        (party_add_template, "p_player_camp", "pt_mercenary_company_noble_infantry"),	  
        (display_message, "@Noble Infantry template added to camp"),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
        (party_slot_eq, "p_player_camp", slot_player_camp_chapterhouse, 1),
        (party_add_template, "p_player_camp", "pt_mercenary_company_noble_cavalry"),	  
        (display_message, "@Noble cavalry template added to camp"),
    (try_end),
    
    (try_begin),
        (party_add_template, "p_player_camp", "pt_mercenary_company_infantry"),		
        (display_message, "@Melee template added to camp"),
    (try_end),
  ]),
  

  ("refresh_mercenary_camp_merchant_inventory",
    [
    (reset_item_probabilities,100),
    (set_merchandise_modifier_quality,150),
    (troop_clear_inventory, "trp_merc_company_merchant"),
    
    (troop_add_merchandise, "trp_merc_company_merchant", itp_type_goods, 8),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_horse, 4),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_archery_range, 1),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_bow, 4),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_crossbow, 4),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_arrows, 3),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_bolts, 3),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_musket, 2),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_bullets, 2),
    (try_end),
    
    (try_begin),
        (party_slot_eq, "p_player_camp", slot_player_camp_smithy, 1),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_one_handed_wpn, 3),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_two_handed_wpn, 1),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_polearm, 5),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_shield, 5),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_head_armor, 5),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_body_armor, 5),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_foot_armor, 4),
        (troop_add_merchandise, "trp_merc_company_merchant", itp_type_hand_armor, 3),
    (try_end),
    
    (troop_ensure_inventory_space, "trp_merc_company_merchant", 30),
    (troop_sort_inventory, "trp_merc_company_merchant"),
    
    (store_troop_gold, reg6, "trp_merc_company_merchant"),
    (try_begin),
        (lt, reg6, 1200),
        (store_random_in_range,":new_gold", 400, 800),
        (call_script, "script_troop_add_gold", "trp_merc_company_merchant", ":new_gold"),
    (try_end),

  ]),



]