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
        (create_text_overlay, "$g_presentation_obj_1", s60, tf_center_justify), #SB : continue str
        (position_set_x, pos1, 470),
        (position_set_y, pos1, 105),
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
          (troop_set_name, "$g_target_name_change", s7),
          (troop_set_plural_name, "$g_target_name_change", s8),
          # (display_message, "@Break 3 - {s8}", color_bad_news),
          # (display_message, "@Break 3 s0 - {s0}", color_bad_news),
          (presentation_set_duration, 0),
          (jump_to_menu, "mnu_dac_name_troops_2"),
          #(change_screen_map),
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

("dac_ct_view_armoury_buggy",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),

        (str_store_string, s1, "@Smith"),
        (create_text_overlay, "$g_presentation_obj_name_kingdom_1", s1, tf_center_justify),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 620),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
      
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_left", "$g_target_armoury"),
        (call_script, "script_custom_troop_detail_inventory_right", "trp_player"),
        

        (try_begin),
          (eq, "$g_presentation_state", 1),
          (is_between, "$g_item_to_scrap", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"), 
          (str_store_string, s2, "@Selling this item for scrap^will cost {reg75} crowns"),
          (create_text_overlay, "$g_multiplayer_poll_to_show", s2, tf_center_justify),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 500),
          (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
          
          (str_store_string, s3, "@Sell"),
          (create_button_overlay, "$g_presentation_obj_1", s3, tf_center_justify), #SB : continue str
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 450),
          (overlay_set_position, "$g_presentation_obj_1", pos1),
        (else_try),
          (eq, "$g_presentation_state", 2),
          (is_between, "$g_item_to_buy", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"), 
          (val_mul, reg75, 25), 
          (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
          (try_begin),
            (ge, ":trade_skill", 1),
            (store_sub, ":multiplier", 25, ":trade_skill"),
            (store_mul, ":discounted_price", reg75, ":multiplier"),
            (assign, reg76, ":discounted_price"),
            (str_store_string, s3, "@, however you have been making good contacts with some tradesmen and will actually cost you {reg76} crowns"),
          (else_try),
            (str_store_string,s3, "@."),
          (try_end),
          (str_store_string, s2, "@Buying this item ^will cost {reg75} crowns{s3}"),
          (create_text_overlay, "$g_multiplayer_poll_to_show", s2, tf_center_justify),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 500),
          (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
          
          (str_store_string, s4, "@Buy"),
          (create_button_overlay, "$g_presentation_obj_2", s4, tf_center_justify), #SB : continue str
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 450),
          (overlay_set_position, "$g_presentation_obj_2", pos1),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_continue_dot", tf_center_justify), #SB : continue str
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        (presentation_set_duration, 999999),
        ]),

      (hover,[
        (call_script, "script_custom_troop_detail_inventory_tooltip"),
        (call_script, "script_custom_troop_detail_inventory_tooltip_right"),
      ]),

    (click,
    [
      (store_trigger_param_1, ":object_id"),
      (store_trigger_param_2, ":mouse_state"),

        (try_begin),
          (neq, ":mouse_state", 1),
          (eq, "$g_presentation_state", 0),
          (call_script, "script_custom_troop_detail_remove_item_from_troop", "$g_target_armoury", ":object_id"),
        (else_try),
          (eq, ":mouse_state", 1), #Right Click
          (call_script, "script_custom_troop_detail_select_item_for_scrap",":object_id"),
          (display_message, "@Right Click, Select For Scrap"),
        (else_try),
          (call_script, "script_custom_troop_detail_select_item_for_buying", ":object_id"),
          (display_message, "@Left Click, Select For Buy"),
        (else_try),
          (eq, "$g_presentation_state", 1),
          (eq, ":object_id", "$g_presentation_obj_1"),
          (troop_remove_item,"$g_target_armoury", "$g_item_to_scrap"),
          (troop_add_gold, "trp_player", reg75),
          (str_store_item_name, s7, "$g_item_to_scrap"),
          (display_message, "@{s7} scrapped for {reg75} crowns", color_good_news),
          (assign, "$g_presentation_state", 0),
          (start_presentation, "prsnt_dac_ct_view_armoury"),
        (else_try),
          (eq, "$g_presentation_state", 2),
          (eq, ":object_id", "$g_presentation_obj_2"),
          (troop_add_item,"$g_target_armoury", "$g_item_to_buy"),
          (str_store_item_name, s7, "$g_item_to_buy"),
          (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
          (try_begin),
            (ge, ":trade_skill", 1),
            (troop_remove_gold, "trp_player", reg76),
            (display_message, "@{s7} bought for the armoury for {reg76} crowns", color_good_news),
          (else_try),
            (troop_remove_gold, "trp_player", reg75),
            (display_message, "@{s7} bought for the armoury for {reg75} crowns", color_good_news),
          (try_end),
          (assign, "$g_presentation_state", 0),
          (display_message, "@Left Click, Buy"),
          (start_presentation, "prsnt_dac_ct_view_armoury"),
        (else_try),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
          (assign, "$g_presentation_state", 0),
          (presentation_set_duration, 0),
          (jump_to_menu, "mnu_dac_name_troops_2"),
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
        (position_set_y, pos1, 620),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
      
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_armoury", "$g_target_armoury"),
        

        (try_begin),
          (eq, "$g_presentation_state", 1),
          (is_between, "$g_item_to_scrap", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"), 
          (str_store_string, s2, "@Selling this item for scrap^will cost {reg75} crowns"),
          (create_text_overlay, "$g_multiplayer_poll_to_show", s2, tf_center_justify),
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 500),
          (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
          
          (str_store_string, s3, "@Sell"),
          (create_button_overlay, "$g_presentation_obj_1", s3, tf_center_justify), #SB : continue str
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 430),
          (overlay_set_position, "$g_presentation_obj_1", pos1),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_continue_dot", tf_center_justify), #SB : continue str
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        (str_store_string, s11, "@Smith"),
        (create_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify), #SB : continue str
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
          (jump_to_menu, "mnu_dac_name_troops_2"),
        (else_try),
          (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Quartermaster
          (assign, "$g_presentation_state", 0),
          (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
        (else_try),
          (call_script, "script_custom_troop_detail_select_item_for_scrap",":object_id"),
        (else_try),
          (eq, "$g_presentation_state", 1),
          (eq, ":object_id", "$g_presentation_obj_1"),
          (troop_remove_item,"$g_target_armoury", "$g_item_to_scrap"),
          (troop_add_gold, "trp_player", reg75),
          (str_store_item_name, s7, "$g_item_to_scrap"),
          (display_message, "@{s7} scrapped for {reg75} crowns", color_good_news),
          (assign, "$g_presentation_state", 0),
          (start_presentation, "prsnt_dac_ct_view_armoury"),

        (try_end),
    ]),


      ] #+ coord_helper 
        + prsnt_escape_close),

("dac_ct_buy_items_for_armoury",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),

        (str_store_string, s1, "@Smith"),
        (create_text_overlay, "$g_presentation_obj_name_kingdom_1", s1, tf_center_justify),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 620),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
      
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_armoury", "trp_player"),
        

        (try_begin),
          (eq, "$g_presentation_state", 1),
          (is_between, "$g_item_to_scrap", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"), 
          (store_mul, ":base_price", reg75, 20), 
          (assign, reg80, ":base_price"),
          (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
          (try_begin),
            (ge, ":trade_skill", 1),
            (store_sub, ":multiplier", 20, ":trade_skill"),
            (store_mul, ":discounted_price", reg75, ":multiplier"),
            (assign, reg81, ":discounted_price"),
            (str_store_string, s3, "@,^however made good contacts^with some tradesmen^and will actually cost you {reg81} crowns"),
          (else_try),
            (str_store_string,s3, "@."),
          (try_end),
          (str_store_string, s2, "@Reproducing this item for the armoury^will cost {reg80} crowns{s3}"),
          (create_text_overlay, "$g_multiplayer_poll_to_show", s2, tf_center_justify),
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 500),
          (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
          
          (item_get_type, ":type", "$g_item_to_scrap"),
          (try_begin),
            (is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows), #weapons
            (val_add, reg85, 5),
          (else_try),
            (is_between, ":type", itp_type_head_armor, itp_type_pistol), #armour
            (val_add, reg85, 3),
          (else_try),
            (is_between, ":type", itp_type_bow, itp_type_thrown), #bows/crossbow
            (val_add, reg85, 4),
          (else_try),
            (val_add, reg85, 2),
          (try_end),

          (str_store_string, s4, "@These will also take {reg85} days to make."),
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
          (create_button_overlay, "$g_presentation_obj_2", s5, tf_center_justify), #SB : continue str
          (position_set_x, pos1, 770),
          (position_set_y, pos1, 330),
          (overlay_set_position, "$g_presentation_obj_2", pos1),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_continue_dot", tf_center_justify), #SB : continue str
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 75),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        (str_store_string, s11, "@Armoury"),
        (create_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify), #SB : continue str
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
          (jump_to_menu, "mnu_dac_name_troops_2"),
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
          (str_store_item_name, s7, "$g_item_to_scrap"),
          (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
          (store_troop_gold, ":gold", "trp_player"),
          (try_begin),
            (ge, ":trade_skill", 1),
            (ge, ":gold", reg81),
            (troop_remove_gold, "trp_player", reg81),
            (display_message, "@{s7} will be made for the armoury for {reg81} crowns and will take {reg85} days.", color_good_news),
            (store_current_day, ":cur_day"),
            (store_add, ":days_til_completed", ":cur_day", reg85),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_days_til_finished, ":days_til_completed"),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item, "$g_item_to_scrap"),
          (else_try),
            (ge, ":gold", reg80),
            (troop_remove_gold, "trp_player", reg80),
            (display_message, "@{s7} bought for the armoury for {reg80} crowns and will take {reg85} days", color_good_news),
            (store_current_day, ":cur_day"),
            (store_add, ":days_til_completed", ":cur_day", reg85),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_days_til_finished, ":days_til_completed"),
            (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item, "$g_item_to_scrap"),
            (assign, "$g_presentation_state", 0),
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_dac_name_troops_2"),
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



]