import string
from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from ID_factions import *
from header_operations import *
from header_triggers import *
#SB: import skills from ID_skills import *
from module_constants import *
##diplomacy start+ Import for use with terrain advantage
from header_terrain_types import *
from module_items import *
#SB : import colors
from module_factions import *
# from module_presentations import coord_helper
##diplomacy end

from compiler import *

load = ti_on_presentation_load
run = ti_on_presentation_run
event = ti_on_presentation_event_state_change
hover = ti_on_presentation_mouse_enter_leave
click = ti_on_presentation_mouse_press

# Shows coordinates on a presentation for easy development
# Set debug_show_presentation_coordinates on module_constants.py
coord_helper = [
  (load, [
      #(eq, debug_show_presentation_coordinates, 1),
      (create_text_overlay, "$mouse_coordinates", "str_empty_string"),
      (overlay_set_color, "$mouse_coordinates", 0xFF0000),
      (position_set_x, pos1, 10),
      (position_set_y, pos1, 700),
      (overlay_set_position, "$mouse_coordinates", pos1),
  ]),
  (run, [
      #(eq, debug_show_presentation_coordinates, 1),
      (set_fixed_point_multiplier, 1000),
      
      (mouse_get_position, pos1),
      (position_get_x, reg1, pos1),
      (position_get_y, reg2, pos1),
      (overlay_set_text, "$mouse_coordinates", "@{reg1}, {reg2}"),
  ])
]
prsnt_escape_close = [
  (run,
    [
      (try_begin),
        (this_or_next|key_clicked, key_escape),
        (key_clicked, key_xbox_start),
        (presentation_set_duration, 0),
        (change_screen_return,0),
      (try_end),
  ]),
]

mercenary_company_presentations = [

("name_troop",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        
        (str_store_string, s4, "@What will you name this troop?"),
        (create_text_overlay, reg1, s4, tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 390),
        (position_set_y, pos1, 640),
        (overlay_set_position, reg1, pos1),

        (create_simple_text_box_overlay, "$g_presentation_obj_name_kingdom_1"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 610),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
        (assign, "$g_presentation_obj_banner_selection_1", -1),
        #SB : set up text box
        # (str_store_troop_name, s0, "$g_target_name_change"),
        (str_store_troop_name, s7, "$g_target_name_change"),
        (overlay_set_text, "$g_presentation_obj_name_kingdom_1", s7),

        (str_store_string, s5, "@Plural Name"),
        (create_text_overlay, reg1, s5, tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 590),
        (overlay_set_position, reg1, pos1),

        (create_simple_text_box_overlay, "$g_presentation_credits_obj_1"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 565),
        (overlay_set_position, "$g_presentation_credits_obj_1", pos1),
        (assign, "$g_presentation_obj_banner_selection_1", -1),
        #SB : set up text box
        # (str_store_troop_name_plural, s11, "$g_target_name_change"),
        (str_store_troop_name_plural, s8, "$g_target_name_change"),
        (overlay_set_text, "$g_presentation_credits_obj_1", s8),

        (call_script, "script_custom_troop_detail_inventory_left", "$g_target_name_change"),
        (store_add, ":armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_right", ":armoury"),
        
        (store_mul, ":cur_troop", "$g_target_name_change", 2),#with weapons
        (create_mesh_overlay_with_tableau_material, "$g_multiplayer_poll_to_show", -1, "tableau_troop_tree_pic",":cur_troop"),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 650),
        (overlay_set_size, "$g_multiplayer_poll_to_show", pos1),

        (create_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_continue_dot", tf_left_align), #SB : continue str
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        (troop_get_slot, reg22, "$g_target_name_change", slot_troop_tier_custom_troop),
        (str_store_string, s60, "@Troop Tier: {reg22}"),
        (create_text_overlay, "$g_presentation_obj_1", s60, tf_left_align),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        (presentation_set_duration, 999999),
        ]),

      (hover,[
        (call_script, "script_custom_troop_detail_inventory_tooltip"),
        (call_script, "script_custom_troop_detail_inventory_tooltip_right"),
      ]),


    (event, 
      [
        (store_trigger_param_1, ":object_id"),
        (try_begin),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Change Name
          (str_store_string, s7, s0),
          (troop_set_name, "$g_target_name_change", s7),
        (else_try),       
          (eq, ":object_id", "$g_presentation_credits_obj_1"), #Change Plural Name
          (str_store_string, s8, s0),
          # (display_message, "@Break 1 - {s8}", color_bad_news),
          # (display_message, "@Break 1 s0 - {s0}", color_bad_news),
          (troop_set_plural_name, "$g_target_name_change", s8),
        (try_end),
      ]),

    (click,
    [
      (store_trigger_param_1, ":object_id"),
      (store_trigger_param_2, ":mouse_state"),
        (try_begin),
          (eq, ":mouse_state", 1), #Right Click
          (call_script, "script_custom_troop_detail_remove_item_from_troop", "$g_target_name_change", ":object_id"),
        (else_try),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Change Name
          (str_store_string, s7, s0),
          (troop_set_name, "$g_target_name_change", s7),
        (else_try),
          (eq, ":object_id", "$g_presentation_credits_obj_1"), #Change Plural Name
          (str_store_string, s8, s0),
          # (display_message, "@Break 2 - {s8}", color_bad_news),
          # (display_message, "@Break 2 s0 - {s0}", color_bad_news),
          (troop_set_plural_name, "$g_target_name_change", s8),
        (else_try),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
### DAC Seek: Store the name as well
          (store_add, ":bak_troop", 1, "$g_target_name_change"),
          (troop_set_name, ":bak_troop", s7),
          (troop_set_plural_name, ":bak_troop", s8),
### DAC Seek End
          (troop_set_name, "$g_target_name_change", s7),
          (troop_set_plural_name, "$g_target_name_change", s8),
          # (display_message, "@Break 3 - {s8}", color_bad_news),
          # (display_message, "@Break 3 s0 - {s0}", color_bad_news),
### DAC Seek, this was forgotten
          (call_script, "script_copy_inventory", "$g_target_name_change", ":bak_troop"),
          (troop_equip_items, "$g_target_name_change"),
### DAC Seek End
          (presentation_set_duration, 0),
          (jump_to_menu, "mnu_dac_name_troops_2"),
          # (change_screen_map),
        #(else_try),
        #  (eq, ":object_id", "$g_presentation_obj_1"),
        #  (start_presentation, "prsnt_dac_ct_buy_weapons_for_armoury"),
        (else_try),
              (call_script, "script_troop_detail_update_dummy", "$g_target_name_change", ":object_id"),
              (call_script, "script_custom_troop_detail_add_item_from_armoury", "$g_target_name_change", ":object_id"),
        (try_end),
    ]),


      ] #+ coord_helper 
        + prsnt_escape_close),

("dac_ct_view_armoury",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),

        (str_store_string, s1, "@Armoury"),
        (create_text_overlay, "$g_presentation_obj_name_kingdom_1", s1, tf_center_justify),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 660),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
        (position_set_x, pos1, 1250),
        (position_set_y, pos1, 1250),
        (overlay_set_size, "$g_presentation_obj_name_kingdom_1", pos1),
        
        (str_store_troop_name, s8, "$g_target_name_change"),
        (troop_get_slot, reg4, "$g_target_name_change", slot_troop_tier_custom_troop),
        (str_store_string, s9, "@Troop Name: {s8}^Troop Tier: {reg4}"),        
        (create_text_overlay, reg5, s9, tf_left_align),
        (position_set_x, pos1, 85),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg5, pos1),
        
        (store_troop_gold, ":player_gold", "trp_player"),
        (assign, reg11, ":player_gold"),
        (create_text_overlay, reg0, "str_dac_player_camp_smith_available_gold", tf_left_align),
        (position_set_x, pos1, 620),
        (position_set_y, pos1, 620),
        (overlay_set_position, reg0, pos1),
        
      
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_armoury", "$g_target_armoury"),
        

        (try_begin),
          (eq, "$g_presentation_state", 1),
          (is_between, "$g_item_to_scrap", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"), 
          (str_store_item_name, s7, "$g_item_to_scrap"),
          (str_store_string, s2, "@Selected: ^{s7}^Selling this item for scrap^will recoup {reg75} crowns"),
          (create_text_overlay, "$g_multiplayer_poll_to_show", s2, tf_center_justify),
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 500),
          (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
          
          (str_store_string, s3, "@Sell"),
          (create_game_button_overlay, "$g_presentation_obj_1", s3, tf_center_justify), #SB : continue str
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 430),
          (overlay_set_position, "$g_presentation_obj_1", pos1),
        (try_end),

        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_continue_dot", tf_center_justify), #SB : continue str
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        (str_store_string, s11, "@Commission Items"),
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify), #SB : continue str
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),

        (presentation_set_duration, 999999),
        ]),

      (hover,[
        (call_script, "script_custom_troop_detail_inventory_tooltip"),
      ]),


    (event, 
      [
        (store_trigger_param_1, ":object_id"),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
        (assign, "$g_presentation_state", 0),
        (presentation_set_duration, 0),
        (jump_to_menu, "mnu_dac_name_troops_2"),

      ]),

    (click,
    [
      (store_trigger_param_1, ":object_id"),

        (try_begin),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
          (assign, "$g_presentation_state", 0),
          (presentation_set_duration, 0),
          (jump_to_menu, "mnu_dac_name_troops_3"),
        (else_try),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Quartermaster
          (assign, "$g_presentation_state", 0),
          (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
        (else_try),
          (eq, "$g_presentation_state", 1),
          (eq, ":object_id", "$g_presentation_obj_1"),
          (troop_remove_item,"$g_target_name_change", "$g_item_to_scrap"),
          (troop_remove_item,"$g_target_armoury", "$g_item_to_scrap"),
          (set_show_messages, 0),
          (troop_add_gold, "trp_player", reg75),
          (set_show_messages, 1),
          (display_message, "@Scrapped {s7} from {s8}^{reg75} crowns recouped", color_good_news),
          (assign, "$g_presentation_state", 0),
          (start_presentation, "prsnt_dac_ct_view_armoury"),
        (else_try),
          (call_script, "script_custom_troop_detail_select_item_for_scrap",":object_id"),
        (try_end),
    ]),


      ] #+ coord_helper 
        + prsnt_escape_close),

("dac_ct_buy_items_for_armoury",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),
        (assign, reg85, 0), ### Stores how long it will take to finish the commission

        (str_store_string, s1, "@Smith"),
        (create_text_overlay, "$g_presentation_obj_name_kingdom_1", s1, tf_center_justify),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 660),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
        (position_set_x, pos1, 1250),
        (position_set_y, pos1, 1250),
        (overlay_set_size, "$g_presentation_obj_name_kingdom_1", pos1),
        
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_armoury", "trp_player"),
        
### DAC Seek:
        (str_store_troop_name, s8, "$g_target_name_change"),
        (troop_get_slot, reg4, "$g_target_name_change", slot_troop_tier_custom_troop),
        (str_store_string, s9, "@Troop Name: {s8}^Troop Tier: {reg4}"),        
        (create_text_overlay, reg5, s9, tf_left_align),
        (position_set_x, pos1, 85),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg5, pos1),
        
        (store_troop_gold, ":player_gold", "trp_player"),
        (assign, reg11, ":player_gold"),
        (create_text_overlay, reg0, "str_dac_player_camp_smith_available_gold", tf_left_align),
        (position_set_x, pos1, 620),
        (position_set_y, pos1, 620),
        (overlay_set_position, reg0, pos1),
        

        (try_begin),
          (eq, "$g_presentation_state", 1),
          (is_between, "$g_item_to_scrap", "itm_ho_sumpter_1", "itm_items_end"), 
          (call_script, "script_cf_custom_troop_has_access_to_item","$g_target_name_change", "$g_item_to_scrap"), ### DAC Seek
          (try_begin),
            (eq, "$class_type", cc_peasant_smith),
            (store_mul, ":base_price", reg75, 3), 
          (else_try),
            (store_mul, ":base_price", reg75, 4), 
          (try_end),
          (assign, reg80, ":base_price"),
          (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
          (try_begin),
            (ge, ":trade_skill", 1),
            (store_mul, ":trade_bonus", 5, ":trade_skill"),
            (store_sub, ":trade_factor", 100, ":trade_bonus"),
            (store_mul, ":discounted_price", ":base_price", ":trade_factor"),
            (val_div, ":discounted_price", 100),
            (assign, reg81, ":discounted_price"),
            (str_store_string, s3, "@,^however we made good deals^with some tradesmen^and it will actually cost you {reg81} crowns"),
          (else_try),
            (str_store_string,s3, "@."),
          (try_end),
          (str_store_string, s2, "@Reproducing this item for the armoury^will cost {reg80} crowns{s3}"),
          (create_text_overlay, "$g_multiplayer_poll_to_show", s2, tf_center_justify),
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 500),
          (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
          
         
          (call_script, "script_dac_get_item_commission_hours", "$g_item_to_scrap"),
          (assign, reg85, reg0),

          (str_store_string, s4, "@It will take {reg85} hour(s) to make."),
          (create_text_overlay, "$g_presentation_obj_1", s4, tf_center_justify), #SB : continue str
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 430),
          (overlay_set_position, "$g_presentation_obj_1", pos1),

          (store_troop_gold, ":gold", "trp_player"),
          (try_begin),
            (ge, ":trade_skill", 1),
            (ge, ":gold", reg81),
            (str_store_string, s5, "@Buy"),
          (else_try),
            (ge, ":gold", reg80),
            (str_store_string, s5, "@Buy"),
          (else_try),
            (str_store_string, s5, "@Not Enough Crowns"),
          (try_end),
          (create_game_button_overlay, "$g_presentation_obj_2", s5, tf_center_justify),
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 330),
          (overlay_set_position, "$g_presentation_obj_2", pos1), 
        (try_end),

        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_continue_dot", tf_center_justify), #SB : continue str
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        (str_store_string, s11, "@Scrap Items"),
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify), #SB : continue str
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),

        (presentation_set_duration, 999999),
        ]),

      (hover,[
        (call_script, "script_custom_troop_detail_inventory_tooltip"),
      ]),


    (event, 
      [
        (store_trigger_param_1, ":object_id"),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
        (assign, "$g_presentation_state", 0),
        (presentation_set_duration, 0),
        (jump_to_menu, "mnu_dac_name_troops_3"),

      ]),

    (click,
    [
    (store_trigger_param_1, ":object_id"),

    (try_begin),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
        (assign, "$g_presentation_state", 0),
        (presentation_set_duration, 0),
        (jump_to_menu, "mnu_dac_name_troops_3"),
    (else_try),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Quartermaster
        (assign, "$g_presentation_state", 0),
        (start_presentation, "prsnt_dac_ct_view_armoury"),
    (else_try),
        (neq, ":object_id", "$g_presentation_obj_2"),
        (call_script, "script_custom_troop_detail_select_item_for_scrap", ":object_id"),
    (else_try),
        (eq, "$g_presentation_state", 1),
        (eq, ":object_id", "$g_presentation_obj_2"),
        (neq, "$g_item_to_scrap", "itm_no_item"),
        (str_store_item_name, s7, "$g_item_to_scrap"),
        (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
        (store_troop_gold, ":gold", "trp_player"),
        
        (assign, ":continue", 0),
          
        (try_begin),
            (ge, ":trade_skill", 1),
            (ge, ":gold", reg81),
            (troop_remove_gold, "trp_player", reg81),
            (display_message, "@{s7} will be made for the armoury for {reg81} crowns and will take {reg85} hour(s).", color_good_news),
            (assign, ":continue", 1),
        (else_try),
            (ge, ":gold", reg80),
            (troop_remove_gold, "trp_player", reg80),
            (display_message, "@{s7} bought for the armoury for {reg80} crowns and will take {reg85} hour(s)", color_good_news),
            (assign, ":continue", 1),
        (try_end),
        
        (try_begin),
            (eq, ":continue", 1),
            (assign, "$g_target_troop_name", "$g_target_name_change"),
            (assign, ":hours_til_completed", reg85),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished, ":hours_til_completed"),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item, "$g_item_to_scrap"),
            (assign, "$g_target_new_item", "$g_target_armoury"),
            (assign, "$g_presentation_state", 0),
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_dac_name_troops_3"),
        (else_try),
            (display_message, "@Not Enough Crowns", color_bad_news),
        (try_end),
          
          
        (assign, "$g_presentation_state", 0),
        (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
    (try_end),
    ]),


      ] #+ coord_helper 
        + prsnt_escape_close),
        
  ("rename_company",0,mesh_load_window,[
      (ti_on_presentation_load,
       [
        (set_fixed_point_multiplier, 1000),
        (str_store_string, s1, "@Enter the name of your company"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_position, reg1, pos1),

        (create_simple_text_box_overlay, "$g_presentation_obj_name_company"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_name_company", pos1),

        (str_store_troop_name, s7, "trp_merc_company_name"),

        (overlay_set_text, "$g_presentation_obj_name_company", s7),

        (create_button_overlay, "$g_presentation_obj_name_company_2", "str_continue_dot", tf_center_justify), #SB : continue str
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_name_company_2", pos1),

        (presentation_set_duration, 999999),
        ]),
        
    (event, 
        [
        (store_trigger_param_1, ":object_id"),
        (try_begin),
            (eq, ":object_id", "$g_presentation_obj_name_company"), # Change Name
            (str_store_string, s7, s0),
            (troop_set_name, "trp_merc_company_name", s7),
            (troop_set_plural_name, "trp_merc_company_name", s7),
            (call_script, "script_dac_upgrade_player_camp"),
        (else_try),
            (eq, ":object_id", "$g_presentation_obj_name_company_2"),
            (assign, "$g_presentation_next_presentation", -1), #break out
            (presentation_set_duration, 0),
        (try_end),
    ]),
      # (ti_on_presentation_event_state_change,
       # [
        # (store_trigger_param_1, ":object"),
        # (try_begin),
            # (eq, ":object", "$g_presentation_obj_name_company"),
            # (str_store_string, s7, s0),
        # (else_try),

        # (try_end),
            # (assign, "$g_presentation_next_presentation", -1), #break out
            # (presentation_set_duration, 0),
        # ]),
      ]),
      
      
("dac_mercenary_camp_recruitment",0,mesh_party_window_b,[
      (ti_on_presentation_load,
       [
        (presentation_set_duration, 999999),       
        (set_fixed_point_multiplier, 1000),
        
        (str_clear, s0),
        (str_clear, s1),
        (str_clear, s12),

        (assign, ":base_scroll_y", 320),
        (assign, ":base_scroll_size_y", 360), 
        (assign, ":base_candidates_y", 0), 
        
### Text        
# Troop List Header      
        (create_text_overlay, reg0, "str_dac_player_camp_recruitment", tf_center_justify),
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg0, pos1),
# Troop Recruitment Requirements  
        (create_text_overlay, reg2, "str_dac_player_camp_requirements", tf_center_justify),
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 260),
        (overlay_set_position, reg2, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg2, pos1),
# Party Information       
        (create_text_overlay, reg3, "str_dac_player_camp_party_info", tf_center_justify),
        (position_set_x, pos1, 160),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg3, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg3, pos1),
# Player Information        
        (create_text_overlay, reg4, "str_dac_player_camp_player_info", tf_center_justify),
        (position_set_x, pos1, 160),
        (position_set_y, pos1, 260),
        (overlay_set_position, reg4, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg4, pos1),
        
### Player Information Panel
        (call_script, "script_game_get_party_companion_limit"),
        (assign, ":party_size_limit", reg0),
        (party_get_num_companions, ":num_companions", "p_main_party"),
        (troop_get_slot, ":renown", "trp_player", slot_troop_renown),       
        (store_troop_gold, ":gold", "trp_player"),

        (assign, reg13, ":gold"),
        (assign, reg14, ":renown"),
        (assign, reg15, "$player_honor"),
        (assign, reg16, ":num_companions"),
        (assign, reg17, ":party_size_limit"),

        (create_text_overlay, reg1, "str_dac_player_camp_player_info_registers", tf_scrollable|tf_left_align),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 1250),
        (position_set_y, pos1, 1250),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 35),
        (position_set_y, pos1, 125),
        (overlay_set_position, reg1, pos1),
        # (position_set_x, pos1, 160),
        # (position_set_y, pos1, 180),
        # (overlay_set_area_size, reg1, pos1), 
        
### Party Information Panel
        (call_script, "script_dac_list_player_camp_available_troops_to_s10"),
        (call_script, "script_dac_list_player_camp_improvements_to_s11"),
        (str_store_string, s12, "@{s10}^^{s11}"),
        (create_text_overlay, reg1, s12, tf_scrollable_style_2|tf_left_align),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 35),
        (position_set_y, pos1, 320),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 262),
        (position_set_y, pos1, 360),
        (overlay_set_area_size, reg1, pos1), 
        
### Selected Troop
        (try_begin),
            (neq, "$character_info_id", -1),
            (str_store_troop_name, s1, "$character_info_id"),
        (else_try),
            (str_store_string, s1, "str_empty_string"),
        (try_end),
        
        (create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_with_outline),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 500), # Higher, means more toward the right
        (position_set_y, pos1, 715), # Higher, means more toward the top
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        
### Selected Troop Requirements
        (try_begin),
            (neq, "$character_info_id", -1),
            
### Container Overlay
            (create_text_overlay, "$g_presentation_credits_obj_10", "str_empty_string", tf_scrollable_style_2),
            (position_set_x, pos1, 685),
            (position_set_y, pos1, 120),
            (overlay_set_position, "$g_presentation_credits_obj_10", pos1),
            (position_set_x, pos1, 262),
            (position_set_y, pos1, 115),
            (overlay_set_area_size, "$g_presentation_credits_obj_10", pos1),
            
            
        # (create_text_overlay, "$g_presentation_obj_1", "str_empty_string", tf_scrollable_style_2),
        # (position_set_x, pos1, 685),
        # (position_set_y, pos1, 320),
        # (overlay_set_position, "$g_presentation_obj_1", pos1),
        # (position_set_x, pos1, 262),
        # (position_set_y, pos1, 360),
        # (overlay_set_area_size, "$g_presentation_obj_1", pos1),
            
### Variable initialization
            (assign, ":y_value", 180),
            (assign, ":overlay_colour", color_neutral_news),
            
            (str_clear, s13),
            (str_clear, s14),
            (str_clear, s15),
            (str_clear, s16),
            (str_clear, s17),
            
            (troop_get_slot, ":manpower_cost", "$character_info_id", slot_troop_manpower_cost),
            (troop_get_slot, ":troop_class", "$character_info_id", slot_troop_recruit_class),
            (call_script, "script_game_get_join_cost", "$character_info_id"),
            (assign, ":join_cost", reg0),
            
            ### Set container
            (set_container_overlay, "$g_presentation_credits_obj_10"),
            
            ### Hiring Cost
            (assign, reg18, ":join_cost"),
            (str_store_string, s17, "@Cost: {reg18}"),
            
            (try_begin),
                (ge, ":gold", ":join_cost"),
                (assign, ":overlay_colour", color_good_news),
            (else_try),
                (assign, ":overlay_colour", color_bad_news),
            (try_end),
            
            (create_text_overlay, "$g_presentation_credits_obj_1", s17, tf_left_align),
            (overlay_set_color, "$g_presentation_credits_obj_1", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_1", pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_1", pos1),
            
            ### Manpower
            (assign, reg19, ":manpower_cost"),
            (str_store_string, s13, "@Manpower: {reg19}"),
            (val_sub, ":y_value", 20),
            
            (try_begin),
                (party_slot_ge, "p_player_camp", slot_player_camp_manpower_amount, ":manpower_cost"),
                (assign, ":overlay_colour", color_good_news),
            (else_try),
                (assign, ":overlay_colour", color_bad_news),
            (try_end),            
            
            (create_text_overlay, "$g_presentation_credits_obj_2", s13, tf_left_align),
            (overlay_set_color, "$g_presentation_credits_obj_2", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_2", pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_2", pos1),
            
            (assign, ":overlay_colour", color_bad_news),
            ### Troop Type
            (try_begin),
                (eq, ":troop_class", TROOP_CLASS_RECRUIT),
                (str_store_string, s14, "@Recruit: 1"),
                (try_begin),
                    (party_slot_ge, "p_player_camp", slot_player_camp_recruit_amount, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (eq, ":troop_class", TROOP_CLASS_VETERAN),
                (str_store_string, s14, "@Veteran: 1"),            
                (try_begin),
                    (party_slot_ge, "p_player_camp", slot_player_camp_veteran_amount, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (eq, ":troop_class", TROOP_CLASS_NOBLE),
                (str_store_string, s14, "@Noble: 1"),   
                (try_begin),
                    (party_slot_ge, "p_player_camp", slot_player_camp_noble_amount, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),                
            (try_end),
            
            (val_sub, ":y_value", 20),
            
            (create_text_overlay, "$g_presentation_credits_obj_3", s14, tf_left_align),
            (overlay_set_color, "$g_presentation_credits_obj_3", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_3", pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_3", pos1),
            
            ### Building 1
            (assign, ":overlay_colour", color_bad_news),
            
            (try_begin),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_1, TROOP_REQ_BUILDING_CORRAL), 
                (str_store_string, s15, "@Building: ^Corral"),
                (val_sub, ":y_value", 40),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_1, TROOP_REQ_BUILDING_RANGE), 
                (str_store_string, s15, "@Building: ^Archery Range"),
                (val_sub, ":y_value", 40),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_archery_range, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_1, TROOP_REQ_BUILDING_CHAPTERHOUSE), 
                (str_store_string, s15, "@Building: ^Chapterhouse"),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_chapterhouse, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
                (val_sub, ":y_value", 40),
            (else_try),
                (str_store_string, s15, "str_empty_string"),            
            (try_end),
            
            (create_text_overlay, "$g_presentation_credits_obj_4", s15, tf_left_align),
            (overlay_set_color, "$g_presentation_credits_obj_4", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_4", pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_4", pos1),

            ### Building 2
            (assign, ":overlay_colour", color_bad_news),
            (try_begin),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_2, TROOP_REQ_BUILDING_CORRAL), 
                (str_store_string, s16, "@Building: ^Corral"),
                (val_sub, ":y_value", 40),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (str_store_string, s16, "str_empty_string"),            
            (try_end),

            (create_text_overlay, "$g_presentation_credits_obj_5", s16, tf_left_align),
            (overlay_set_color, "$g_presentation_credits_obj_5", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_5", pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_5", pos1),

            (set_container_overlay, -1),
        (try_end),
        
### Troop List
        (create_text_overlay, "$g_presentation_obj_1", "str_empty_string", tf_scrollable_style_2),
        (position_set_x, pos1, 685),
        (position_set_y, pos1, ":base_scroll_y"),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (position_set_x, pos1, 262),
        (position_set_y, pos1, ":base_scroll_size_y"),
        (overlay_set_area_size, "$g_presentation_obj_1", pos1),

        # Fill listbox (overlay_add_item and extra storage)      
        (assign, ":num_chars", 0),
        (assign, ":num_slot", 0),
        (try_for_range, ":recruit", mercenary_troops_begin, customizable_troops_end),
            (store_sub, ":delta", ":recruit", mercenary_troops_begin),
            (store_sub, ":troop", "trp_custom_merc_knight_selection", ":delta"),
            
            (try_begin),
                (eq, "$class_type", cc_mercenary_condottiero),
                (assign, ":troop_start", "trp_italian_light_infantry"),
                (assign, ":troop_end", "trp_scottish_poor_archer"),
            (else_try),
                (eq, "$class_type", cc_mercenary_flemish),
                (assign, ":troop_start", "trp_flemish_peasant_crossbowman"),
                (assign, ":troop_end", "trp_italian_light_infantry"),
            (else_try),
                (eq, "$class_type", cc_mercenary_scottish),
                (assign, ":troop_start", "trp_scottish_poor_archer"),
                (assign, ":troop_end", "trp_mercenaries_end"),
            (else_try),
                (assign, ":troop_start", customizable_troops_begin),
                (assign, ":troop_end",   customizable_troops_end),            
            (try_end),
            
            (this_or_next|is_between, ":troop", ":troop_start", ":troop_end"),
            (is_between, ":troop", customizable_troops_begin, customizable_troops_end),            
            
            (neg|troop_is_hero, ":troop"),

            (store_mul, ":y_mult", ":num_chars", 16 * 1.4), # adapt y position to entry number, was 18
            (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

            (set_container_overlay, "$g_presentation_obj_1"),
            
            (str_store_troop_name, s1, ":troop"),


            (create_text_overlay, reg10, "@ {s1}", tf_left_align),
            (overlay_set_color, reg10, 0xDDDDDD),
            (position_set_x, pos1, 650 * 1.4),
            (position_set_y, pos1, 750 * 1.4),
            (overlay_set_size, reg10, pos1),
            (position_set_x, pos1, 0),  
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),

            (create_image_button_overlay, reg10, "mesh_white_plane", "mesh_white_plane"),
            (position_set_x, pos1, 0), # 590 real, 0 scrollarea
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),
            (position_set_x, pos1, 16000 * 1.4),
            (position_set_y, pos1, 750 * 1.4),
            (overlay_set_size, reg10, pos1),
            (overlay_set_alpha, reg10, 0),
            (overlay_set_color, reg10, 0xDDDDDD),

            (try_begin),
                (eq, ":troop", "$character_info_id"),
                (overlay_set_color, reg10, 0xFF6666FF),
                (overlay_set_alpha, reg10, 0x44),
            (try_end),

            (troop_set_slot, "trp_temp_array_a", ":num_slot", reg10),
            (troop_set_slot, "trp_temp_array_b", ":num_slot", ":troop"),
            (val_add, ":num_chars", 1),
            (val_add, ":num_slot", 1),

            (set_container_overlay, -1),
        (try_end),
        
### Troop Mesh + Inventory Box
        (try_begin),
            (neq, "$character_info_id", -1),
            
            (try_begin),
                (troop_is_guarantee_horse, "$character_info_id"),
                (assign, ":char_y", 200),
            (else_try),
                (assign, ":char_y", 180),            
            (try_end),
            
            # (call_script, "script_custom_troop_detail_inventory_left", "$character_info_id"), ### Troop Inventory Box
            (store_mul, reg30, "$character_info_id", 2),
            (create_mesh_overlay_with_tableau_material, "$g_multiplayer_poll_to_show", -1, "tableau_troop_tree_pic", reg30),
            (position_set_x, pos1, 260),
            (position_set_y, pos1, ":char_y"),
            (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
            (position_set_x, pos1, 700),
            (position_set_y, pos1, 700),
            (overlay_set_size, "$g_multiplayer_poll_to_show", pos1),
        (try_end),
        
### Slider
        (try_begin),
            (neq, "$character_info_id", -1),
            (call_script, "script_dac_player_camp_recruit_requirement_met", "$character_info_id"),
            (assign, ":can_recruit", reg0),
            (assign, ":max_amount", reg1),
            (gt, ":can_recruit", 0),
            (ge, ":max_amount", 1),
            
            (create_slider_overlay, "$g_presentation_obj_sliders_1", 1, ":max_amount"),
            (position_set_x, pos1, 500),
            (position_set_y, pos1, 140),   
            (overlay_set_position, "$g_presentation_obj_sliders_1", pos1),            
            (position_set_x, pos1, 900),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_obj_sliders_1", pos1),
            
            (overlay_set_val, "$g_presentation_obj_sliders_1", 1),
            (assign, "$g_presentation_obj_sliders_1_val", 1),
            
            (assign, reg1, "$g_presentation_obj_sliders_1_val"),
            (call_script, "script_game_get_join_cost", "$character_info_id"),
            (assign, ":join_cost", reg0),
            (val_mul, ":join_cost", "$g_presentation_obj_sliders_1_val"),
            (assign, reg2, ":join_cost"),
            
            (create_text_overlay, "$g_presentation_obj_sliders_2", "@Amount: {reg1}", tf_center_justify),
            (position_set_x, pos1, 500),
            (position_set_y, pos1, 175),   
            (overlay_set_position, "$g_presentation_obj_sliders_2", pos1),            
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_obj_sliders_2", pos1),
            (overlay_set_color, "$g_presentation_obj_sliders_2", 0xFFFFFFFF),
            
###  Hire
        (create_in_game_button_overlay, "$g_presentation_obj_3", "@Hire {reg1} for {reg2} Crowns", tf_left_align), #SB : continue str
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 25),
        (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFFFF),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        
        (try_end),
        

        
###  Quit
        (create_in_game_button_overlay, "$g_presentation_obj_2", "str_continue_dot", tf_left_align), #SB : continue str
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFFFF),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        ]),

      (hover,[
        (call_script, "script_custom_troop_detail_inventory_tooltip"),
      ]),

      (event,[
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (assign, ":val_changed", 0),

        (try_begin),
            (eq, ":object", "$g_presentation_obj_sliders_1"),
            (try_begin),
                (neq, "$g_presentation_obj_sliders_1_val", ":value"),
                (assign, "$g_presentation_obj_sliders_1_val", ":value"),
                (assign, ":val_changed", 1),
            (try_end),
            (eq, ":val_changed", 1),
            (assign, reg1, "$g_presentation_obj_sliders_1_val"),
            (str_store_string, s1, "@Amount: {reg1}"),
            (overlay_set_text, "$g_presentation_obj_sliders_2", s1), 
            
            (call_script, "script_game_get_join_cost", "$character_info_id"),
            (assign, ":join_cost", reg0),
            (val_mul, ":join_cost", "$g_presentation_obj_sliders_1_val"),
            (assign, reg2, ":join_cost"),
            (str_store_string, s2, "@Hire {reg1} for {reg2} Crowns"),
            (overlay_set_text, "$g_presentation_obj_3", s2),   
        (try_end),
      ]),

    (click,
    [
      (store_trigger_param_1, ":object_id"),
      # (store_trigger_param_2, ":state"),
        (try_begin),
            (eq, ":object_id", "$g_presentation_obj_3"), # Hire
            (call_script, "script_dac_player_camp_recruit_troop", "$character_info_id", "$g_presentation_obj_sliders_1_val"), # param1 troop, param2 amount
            (start_presentation, "prsnt_dac_mercenary_camp_recruitment"),
        (else_try),
            (eq, ":object_id", "$g_presentation_obj_2"), # Continue
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_player_camp_encounter"),
        (else_try),
            (eq, ":object_id", "$g_presentation_obj_1"),
            (start_presentation, "prsnt_dac_mercenary_camp_recruitment"),
      (else_try),
            (store_sub, ":num_troops", customizable_troops_end, mercenary_troops_begin),
            # (val_div, ":num_troops", 3),
            # (val_add, ":num_troops", 1),
            (try_for_range, ":i", 0, ":num_troops"),
                (troop_get_slot, ":control", "trp_temp_array_a", ":i"),
                (eq, ":control", ":object_id"),
                (troop_get_slot, "$character_info_id", "trp_temp_array_b", ":i"),
                (start_presentation, "prsnt_dac_mercenary_camp_recruitment"),
                (assign, ":num_troops", 0),
            (try_end),
            # (assign, "$g_presentation_obj_sliders_1_val", 1),
            # (assign, reg1, "$g_presentation_obj_sliders_1_val"),
            # (str_store_string, s1, "@Amount: {reg1}"),
            # (overlay_set_text, "$g_presentation_obj_sliders_2", s1),
        # (else_try),
            # (overlay_set_val, "$g_presentation_obj_sliders_1", 1),
            # (assign, "$g_presentation_obj_sliders_1_val", 1),
            # (assign, reg1, "$g_presentation_obj_sliders_1_val"),
            # (str_store_string, s1, "@Amount: {reg1}"),
            # (overlay_set_text, "$g_presentation_obj_sliders_2", s1),    
        (try_end),
    ]),


      ] 
        # + coord_helper 
        # + prsnt_escape_close
        ),



]