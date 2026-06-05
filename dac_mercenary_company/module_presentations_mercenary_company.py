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

("dac_ct_view_armoury",0,mesh_mp_ui_profile,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),

        (str_store_string, s1, "@Armoury"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        
        (str_store_string, s2, "@Sell Item"),
        (create_text_overlay, reg2, s2, tf_center_justify),
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg2, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg2, pos1),
        
        (str_store_troop_name, s8, "$g_target_name_change"),
        (troop_get_slot, reg4, "$g_target_name_change", slot_troop_tier_custom_troop),
        (str_store_string, s9, "@Troop Name:^{s8}^Troop Tier: {reg4}"),        
        (create_text_overlay, reg5, s9, tf_left_align),
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 620),
        (overlay_set_position, reg5, pos1),
        
        (store_troop_gold, ":player_gold", "trp_player"),
        (assign, reg11, ":player_gold"),
        
        (create_mesh_overlay, reg0, "mesh_icon_gold"),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 650),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg0, pos1),
        
        (create_text_overlay, reg1, "@{reg11} Crowns", tf_left_align),
        (position_set_x, pos1, 640),
        (position_set_y, pos1, 650),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
      
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_armoury", "$g_target_armoury"),
        

        (try_begin),
            (eq, "$g_presentation_state", 1),
        
            (is_between, "$g_item_to_scrap", "itm_heraldic_mail_with_surcoat_for_tableau", "itm_items_end"), 
            (str_store_item_name, s7, "$g_item_to_scrap"),
            (str_store_string, s2, "@Selected: ^{s7}^Selling this item for scrap will recoup {reg75} crowns"),
            
            (create_text_overlay, reg1, s2, tf_scrollable|tf_left_align),
            (position_set_x, pos1, 600),
            (position_set_y, pos1, 180),
            (overlay_set_position, reg1, pos1),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 300),
            (position_set_y, pos1, 420),
            (overlay_set_area_size, reg1, pos1), 
            
            (create_mesh_overlay_with_item_id, reg2, "$g_item_to_scrap"),
            (position_set_x, pos1, 850),
            (position_set_y, pos1, 640),
            (overlay_set_position, reg2, pos1),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg2, pos1),
          
            (str_store_string, s3, "@Sell"),
            (create_game_button_overlay, "$g_presentation_obj_1", s3, tf_center_justify),
            (position_set_x, pos1, 750),
            (position_set_y, pos1, 450),
            (overlay_set_position, "$g_presentation_obj_1", pos1),
            
        (try_end),
        
### Text Desc
        (str_store_string, s1, "@These are all the items the troop has access to, left-click to select an item you wish the sell. Click the 'commission items' button to purchase items instead."),
        (create_text_overlay, reg1, s1, tf_scrollable|tf_left_align),
        (position_set_x, pos1, 93),
        (position_set_y, pos1, 25),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 303),
        (position_set_y, pos1, 150),
        (overlay_set_area_size, reg1, pos1), 
        
### Troop Mesh   
        (try_begin),
            (troop_is_guarantee_horse, "$g_target_name_change"),
            (assign, ":char_y", 200),
        (else_try),
            (assign, ":char_y", 180),            
        (try_end),
        
        (store_mul, reg30, "$g_target_name_change", 2),
        (create_mesh_overlay_with_tableau_material, "$g_multiplayer_poll_to_show", -1, "tableau_troop_tree_pic", reg30),
        (position_set_x, pos1, 330),
        (position_set_y, pos1, ":char_y"),
        (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, "$g_multiplayer_poll_to_show", pos1),
        
### Close
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_done", tf_center_justify),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

### Button
        (str_store_string, s11, "@Commission Items"),
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 40),
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
    # (store_trigger_param_2, ":mouse_state"),
    (try_begin),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
        (assign, "$g_presentation_state", 0),
        (presentation_set_duration, 0),
        (jump_to_menu, "mnu_dac_name_troops_3"),
    (else_try),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Quartermaster
        (assign, "$g_presentation_state", 0),
        (assign, "$g_presentation_credits_obj_4", -1),
        (assign, "$g_presentation_credits_obj_5", -1),
        (assign, "$g_presentation_credits_obj_6", -1),
        (assign, "$g_presentation_credits_obj_7", -1),
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
    # (else_try), # It triggers multiple times, haven't found a solution yet
        # (eq, ":mouse_state", 1), # Right Click
        # (call_script, "script_custom_troop_detail_remove_item_from_troop", "$g_target_name_change", ":object_id"),
        # (call_script, "script_custom_troop_detail_remove_item_from_troop", "$g_target_armoury", ":object_id"),
        # (item_get_value, reg75, ":object_id"),
        # (set_show_messages, 0),
        # (troop_add_gold, "trp_player", reg75),
        # (set_show_messages, 1),
        # (display_message, "@Scrapped {s7} from {s8}^{reg75} crowns recouped", color_good_news),
        # (assign, "$g_presentation_state", 0),
        # (start_presentation, "prsnt_dac_ct_view_armoury"),
    (else_try),
        (call_script, "script_custom_troop_detail_select_item_for_scrap",":object_id"),
    (try_end),
    ]),


      ] 
        + coord_helper 
        + prsnt_escape_close),

("dac_ct_buy_items_for_armoury",0,mesh_mp_ui_profile,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),
        (assign, reg85, 0), ### Stores how long it will take to finish the commission

        (str_store_string, s1, "@Smith"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        
        (str_store_string, s2, "@Commission Item"),
        (create_text_overlay, reg2, s2, tf_center_justify),
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg2, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg2, pos1),
        
        #DAC Kham: Set up Inventories.
        (store_add, "$g_target_armoury", "$g_target_name_change", 2),
        (call_script, "script_custom_troop_detail_inventory_armoury", "trp_player"),
        
### DAC Seek:
        (str_store_troop_name, s8, "$g_target_name_change"),
        (troop_get_slot, reg4, "$g_target_name_change", slot_troop_tier_custom_troop),
        (str_store_string, s9, "@Troop Name:^{s8}^Troop Tier: {reg4}"),        
        (create_text_overlay, reg5, s9, tf_left_align),
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 620),
        (overlay_set_position, reg5, pos1),
        
        (store_troop_gold, ":player_gold", "trp_player"),
        (assign, reg11, ":player_gold"),
        
        (create_mesh_overlay, reg0, "mesh_icon_gold"),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 650),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg0, pos1),
        
        (create_text_overlay, reg1, "@{reg11} Crowns", tf_left_align),
        (position_set_x, pos1, 640),
        (position_set_y, pos1, 650),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        

        (try_begin),
            (eq, "$g_presentation_state", 1),
            (is_between, "$g_item_to_scrap", "itm_ho_sumpter_1", "itm_items_end"), 
            (call_script, "script_cf_custom_troop_has_access_to_item","$g_target_name_change", "$g_item_to_scrap"), ### DAC Seek
            
            (str_store_item_name, s7, "$g_item_to_scrap"),
          
            (create_combo_label_overlay, "$g_presentation_obj_1"),
            (position_set_x, pos1, 755),
            (position_set_y, pos1, 550),
            (overlay_set_position, "$g_presentation_obj_1", pos1),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_obj_1", pos1),

            (overlay_add_item, "$g_presentation_obj_1", "@Target: {s8}"),           # 0
            (overlay_add_item, "$g_presentation_obj_1", "@Target: Infantry"),       # 1
            (overlay_add_item, "$g_presentation_obj_1", "@Target: Ranged"),         # 2
            (overlay_add_item, "$g_presentation_obj_1", "@Target: Light Cavalry"),  # 3
            (overlay_add_item, "$g_presentation_obj_1", "@Target: Nobles on Foot"), # 4
            (overlay_add_item, "$g_presentation_obj_1", "@Target: Nobles Mounted"), # 5
            (overlay_add_item, "$g_presentation_obj_1", "@Target: EVERYONE"),       # 6

            (overlay_set_val, "$g_presentation_obj_1", "$g_presentation_obj_1_val"),
            
            (try_begin),
                (eq, "$g_presentation_obj_1_val", 1),
                (assign, ":lower_bound", "trp_custom_merc_recruit"),
                (assign, ":higher_bound", "trp_custom_merc_skirmisher"),
            (else_try),
                (eq, "$g_presentation_obj_1_val", 2),
                (assign, ":lower_bound", "trp_custom_merc_skirmisher"),
                (assign, ":higher_bound", "trp_custom_merc_scout"),
            (else_try),
                (eq, "$g_presentation_obj_1_val", 3),
                (assign, ":lower_bound", "trp_custom_merc_scout"),
                (assign, ":higher_bound", "trp_custom_merc_foot_squire"),
            (else_try),
                (eq, "$g_presentation_obj_1_val", 4),
                (assign, ":lower_bound", "trp_custom_merc_foot_squire"),
                (assign, ":higher_bound", "trp_custom_merc_squire"),
            (else_try),    
                (eq, "$g_presentation_obj_1_val", 5),
                (assign, ":lower_bound", "trp_custom_merc_squire"),
                (assign, ":higher_bound", "trp_custom_mercs_end"),
            (else_try),    
                (eq, "$g_presentation_obj_1_val", 6),
                (assign, ":lower_bound", "trp_custom_merc_recruit"),
                (assign, ":higher_bound", "trp_custom_mercs_end"),
            (try_end),                 
            
            (str_clear, s9),
            (try_begin),
                (eq, "$g_presentation_obj_1_val", 0),
                (str_store_string, s9, s8),
                (assign, ":num_troops", 1),
            (else_try),
                (assign, ":num_troops", 0),
            
                (try_for_range, ":troop", ":lower_bound", ":higher_bound"),
                    (neg|troop_is_hero, ":troop"),
                    (call_script, "script_cf_custom_troop_has_access_to_item",":troop", "$g_item_to_scrap"),
                    (val_add,  ":num_troops", 1),
                    (str_store_troop_name, s10, ":troop"),
                    (try_begin),
                        (eq,  ":num_troops", 1),
                        (str_store_string_reg, s9, s10),
                    (else_try),
                        (str_store_string, s9, "@{!}{s9}, {s10}"),
                    (try_end),
                (try_end),
            (try_end),
            
            (assign, reg69, ":num_troops"),
            
            (try_begin),
                (eq, ":num_troops", 0),
                (str_store_string, s11, "@The troops in this group cannot make use of this item."),
                
            (else_try),
            
                (try_begin),
                    (eq, "$class_type", cc_peasant_smith),
                    (store_mul, ":base_price", reg75, 2), 
                (else_try),
                    (store_mul, ":base_price", reg75, 3), 
                (try_end),
                
                (store_mul, ":cost_increase", ":num_troops", 10),
                (store_add, ":cost_multiplier", 100, ":cost_increase"),
                (val_mul, ":base_price", ":cost_multiplier"),
                (val_div, ":base_price", 100),
                
                (assign, reg80, ":base_price"),
                (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
                
                (try_begin),
                    (ge, ":trade_skill", 1),
                    (store_mul, ":trade_bonus", 5, ":trade_skill"),
                    (store_sub, ":trade_factor", 100, ":trade_bonus"),
                    (store_mul, ":discounted_price", ":base_price", ":trade_factor"),
                    (val_div, ":discounted_price", 100),
                    (assign, reg81, ":discounted_price"),
                    (str_store_string, s3, "@, however thanks to your trade accuity you manage to haggle the price down to {reg81} crowns."),
                (else_try),
                    (str_store_string,s3, "@."),
                (try_end),
                
                (call_script, "script_dac_get_item_commission_hours", "$g_item_to_scrap", ":num_troops"),
                (assign, reg85, reg0),
            
                (str_store_string, s11, "@The {s7} will be commissioned for {s9}.^^The cost to commission this item is {reg80} crowns{s3}^^It will take {reg85} hour(s) to produce."),
            (try_end),
          
            (create_text_overlay, reg1, s11, tf_scrollable|tf_left_align),
            (position_set_x, pos1, 600),
            (position_set_y, pos1, 270),
            (overlay_set_position, reg1, pos1),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 300),
            (position_set_y, pos1, 260),
            (overlay_set_area_size, reg1, pos1),
            
            (create_mesh_overlay_with_item_id, reg5, "$g_item_to_scrap"),
            (position_set_x, pos1, 850),
            (position_set_y, pos1, 640),
            (overlay_set_position, reg5, pos1),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg5, pos1),

            (store_troop_gold, ":gold", "trp_player"),
            (try_begin),
                (lt, ":num_troops", 1),
                (str_store_string, s5, "@Invalid selection"),
            (else_try),
                (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item, -1),
                (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item_2, -1),
                (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item_3, -1),
                (str_store_string, s5, "@All slots filled"),
            (else_try),
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
            (position_set_x, pos1, 700),
            (position_set_y, pos1, 600),
            (overlay_set_position, "$g_presentation_obj_2", pos1), 
        (try_end),
        
### Commissions
        ### Separation line
        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (overlay_set_color, reg1, 0x000000),
        (position_set_x, pos1, 15000),
        (position_set_y, pos1, 60),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 605),
        (position_set_y, pos1, 270),
        (overlay_set_position, reg1, pos1),
        
        (try_begin),
            (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_hours_til_finished, -1),
            (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item),
            (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished),  
            (str_store_item_name, s21, ":item"),
            (assign, reg20, ":hours_til_finished"),    
            (str_store_string, s20, "@Commission slot 1 - Currently producing {s21} - {reg20} hour(s) remaining."),
        (else_try),
            (str_store_string, s20, "@Commission slot 1 is free"),
        (try_end),
        
        (try_begin),
            (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2, -1),
            (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item_2),
            (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2),  
            (str_store_item_name, s23, ":item"),
            (assign, reg21, ":hours_til_finished"),    
            (str_store_string, s22, "@Commission slot 2 - Currently producing {s23} - {reg21} hour(s) remaining."),
        (else_try),
            (str_store_string, s22, "@Commission slot 2 is free"),
        (try_end),
        
        (try_begin),
            (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3, -1),
            (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item_3),
            (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3),  
            (str_store_item_name, s25, ":item"),
            (assign, reg22, ":hours_til_finished"),    
            (str_store_string, s24, "@Commission slot 3 - Currently producing {s25} - {reg22} hour(s) remaining."),
        (else_try),
            (str_store_string, s24, "@Commission slot 3 is free"),
        (try_end),
    
    ### Commission 1 Text
    (create_text_overlay, reg2, s20, tf_scrollable|tf_left_align),
    (position_set_x, pos1, 600),
    (position_set_y, pos1, 190),
    (overlay_set_position, reg2, pos1),
    (position_set_x, pos1, 800),
    (position_set_y, pos1, 800),
    (overlay_set_size, reg2, pos1),
    (position_set_x, pos1, 300),
    (position_set_y, pos1, 60),
    (overlay_set_area_size, reg2, pos1),
    
    ### Commission 2 Text
    (create_text_overlay, reg3, s22, tf_scrollable|tf_left_align),
    (position_set_x, pos1, 600),
    (position_set_y, pos1, 140),
    (overlay_set_position, reg3, pos1),
    (position_set_x, pos1, 800),
    (position_set_y, pos1, 800),
    (overlay_set_size, reg3, pos1),
    (position_set_x, pos1, 300),
    (position_set_y, pos1, 60),
    (overlay_set_area_size, reg3, pos1),
    
    ### Commission 3 Text
    (create_text_overlay, reg4, s24, tf_scrollable|tf_left_align),
    (position_set_x, pos1, 600),
    (position_set_y, pos1, 80),
    (overlay_set_position, reg4, pos1),
    (position_set_x, pos1, 800),
    (position_set_y, pos1, 800),
    (overlay_set_size, reg4, pos1),
    (position_set_x, pos1, 300),
    (position_set_y, pos1, 60),
    (overlay_set_area_size, reg4, pos1), 
        
### Troop Mesh   
        (try_begin),
            (troop_is_guarantee_horse, "$g_target_name_change"),
            (assign, ":char_y", 200),
        (else_try),
            (assign, ":char_y", 180),            
        (try_end),
        
        (store_mul, reg30, "$g_target_name_change", 2),
        (create_mesh_overlay_with_tableau_material, "$g_multiplayer_poll_to_show", -1, "tableau_troop_tree_pic", reg30),
        (position_set_x, pos1, 330),
        (position_set_y, pos1, ":char_y"),
        (overlay_set_position, "$g_multiplayer_poll_to_show", pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, "$g_multiplayer_poll_to_show", pos1),
        
        # Helper text
        (str_store_string, s1, "@These are all the items in your inventory, left-click an item to select it but keep in mind the item's tier cannot exceed the tier of the selected troop."),
        (create_text_overlay, reg1, s1, tf_scrollable|tf_left_align),
        (position_set_x, pos1, 93),
        (position_set_y, pos1, 25),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 303),
        (position_set_y, pos1, 150),
        (overlay_set_area_size, reg1, pos1), 

        # Exit
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_done", tf_center_justify),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

        # Sell items presentation
        (str_store_string, s11, "@Sell Items"),
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
        
        # Manage Commissions
        (create_game_button_overlay, "$g_presentation_obj_3", "@Manage Commissions", tf_center_justify),
        (position_set_x, pos1, 495),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_obj_3", pos1),

        (presentation_set_duration, 999999),
        ]),

      (hover,[
        # (store_trigger_param_1, ":object"),
        # (store_trigger_param_2, ":enter_leave"),
        
        # (try_begin),
            # (eq, ":object", "$g_presentation_credits_obj_5"),
            # (eq, ":enter_leave", 0),
            
            # (position_set_x, pos1, 2000),
            # (position_set_y, pos1, 2000),
            # (overlay_animate_to_size, "$g_presentation_credits_obj_5", 250, pos1),
      
        # (else_try),
            # (eq, ":object", "$g_presentation_credits_obj_5"),
            # (eq, ":enter_leave", 1),
            
            # (position_set_x, pos1, 1000),
            # (position_set_y, pos1, 1000),
            # (overlay_animate_to_size, "$g_presentation_credits_obj_5", 250, pos1),
        
        # (else_try),
            (call_script, "script_custom_troop_detail_inventory_tooltip"),
        # (try_end),
      ]),


    (event, 
      [
        (store_trigger_param_1, ":object_id"),
        (store_trigger_param_2, ":value"),
        
        (try_begin),
            (eq, ":object_id", "$g_presentation_obj_1"),
            (assign, "$g_presentation_obj_1_val", ":value"),
            (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
        (else_try),
            (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
            (assign, "$g_presentation_state", 0),
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_dac_name_troops_3"),
        (try_end),

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
        (eq, ":object_id", "$g_presentation_obj_3"), # Commissions Presentations
        (assign, "$g_presentation_state", 0),
        (start_presentation, "prsnt_dac_manage_commissions"),
    (else_try),
        (neq, ":object_id", "$g_presentation_obj_1"), ### Other menu
        (neq, ":object_id", "$g_presentation_obj_2"), ### Buy
        (assign, "$g_presentation_obj_1_val", 0),
        (call_script, "script_custom_troop_detail_select_item_for_scrap", ":object_id"),
    (else_try),
        (eq, "$g_presentation_state", 1),
        (eq, ":object_id", "$g_presentation_obj_2"), ### Buy
        (display_message, "@clicked first"),
        
        (neq, "$g_item_to_scrap", "itm_no_item"),
        (str_store_item_name, s7, "$g_item_to_scrap"),
        (store_skill_level, ":trade_skill", skl_trade, "trp_player"),
        (store_troop_gold, ":gold", "trp_player"),
        
        (assign, ":continue", 0),
          
        (try_begin),
            (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item, -1),
            (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item_2, -1),
            (neg|troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item_3, -1),
            (display_message, "@All commission slots filled!", color_bad_news),        
        (else_try),
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
        (else_try),
            (display_message, "@Not Enough Crowns", color_bad_news),            
        (try_end),
        
        (try_begin),
            (eq, ":continue", 1),
            (assign, ":target", -1),
            (assign, ":hours_til_completed", reg85),
            
            (try_begin), 
                (eq, "$g_presentation_obj_1_val", 0), ### target group
                (assign, ":target", "$g_target_armoury"),
            (else_try),
                (assign, ":target", "$g_presentation_obj_1_val"), ### target group
            (try_end),
            
            (try_begin),
                (troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item, -1),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished, ":hours_til_completed"),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item, "$g_item_to_scrap"),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_item_target, ":target"),
            (else_try),
                (troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item_2, -1),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2, ":hours_til_completed"),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item_2, "$g_item_to_scrap"),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_item_target_2, ":target"),
            (else_try),                    
                (troop_slot_eq, "trp_merc_company_smith", slot_camp_smith_creating_item_3, -1),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3, ":hours_til_completed"),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_creating_item_3, "$g_item_to_scrap"),
                (troop_set_slot, "trp_merc_company_smith", slot_camp_smith_item_target_3, ":target"),
            (try_end),            
            
            (assign, "$g_presentation_state", 0),
            # (presentation_set_duration, 0),
            # (jump_to_menu, "mnu_dac_name_troops_3"),
            # (neq, ":object_id", "$g_presentation_obj_1"),
            (assign, "$g_presentation_state", 0),
            (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
        (try_end),
    (try_end),
    ]),


      ] 
        + coord_helper 
        + prsnt_escape_close),
        
        
("dac_manage_commissions",0,mesh_mp_ui_profile,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_target_armoury", 0),

        (str_store_string, s1, "@Commissions"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        
        (str_store_string, s2, "@Cancelations"),
        (create_text_overlay, reg2, s2, tf_center_justify),
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg2, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg2, pos1),
        
### Display Commissions

        (try_begin), ####Commission 1
            (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item),
            (gt, ":item", -1),
            (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished),  
            (str_store_item_name, s21, ":item"),
            (assign, reg20, ":hours_til_finished"),    
            
            (call_script, "script_dac_print_item_commission_targets_to_s2", 1, ":item"),
            
            (str_store_string, s20, "@Commissioning {s21} for {s2} with {reg20} hour(s) remaining"), 
        (else_try),
            (str_store_string, s20, "@Commission slot 1 is free."),         
        (try_end),
        
        (create_text_overlay, reg2, s20, tf_scrollable|tf_left_align),
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg2, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg2, pos1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 120),
        (overlay_set_area_size, reg2, pos1),
        
        (try_begin), ####Commission 2
            (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item_2),
            (gt, ":item", -1),
            (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished_2),  
            (str_store_item_name, s22, ":item"),
            (assign, reg21, ":hours_til_finished"),    
            
            (call_script, "script_dac_print_item_commission_targets_to_s2", 2, ":item"),
            
            (str_store_string, s23, "@Commissioning {s22} for {s2} with {reg21} hour(s) remaining"), 
        (else_try),
            (str_store_string, s23, "@Commission slot 2 is free."), 
        (try_end),
        
        (create_text_overlay, reg3, s23, tf_scrollable|tf_left_align),
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 360),
        (overlay_set_position, reg3, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg3, pos1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 120),
        (overlay_set_area_size, reg3, pos1),
            
        (try_begin), ####Commission 3
            (troop_get_slot, ":item", "trp_merc_company_smith", slot_camp_smith_creating_item_3),
            (gt, ":item", -1),
            (troop_get_slot, ":hours_til_finished", "trp_merc_company_smith", slot_camp_smith_hours_til_finished_3),  
            (str_store_item_name, s25, ":item"),
            (assign, reg22, ":hours_til_finished"),    
            
            (call_script, "script_dac_print_item_commission_targets_to_s2", 2, ":item"),
            
            (str_store_string, s24, "@Commissioning {s25} for {s2} with {reg22} hour(s) remaining"), 
        (else_try),
            (str_store_string, s24, "@Commission slot 3 is free."), 
        (try_end),
        
        (create_text_overlay, reg4, s24, tf_scrollable|tf_left_align),
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 160),
        (overlay_set_position, reg4, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg4, pos1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 120),
        (overlay_set_area_size, reg4, pos1),
        
### Cancel Commission 1
        (str_store_string, s12, "@Cancel C1"),
        (create_game_button_overlay, "$g_presentation_credits_obj_1", s12, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_credits_obj_1", pos1),
        
### Cancel Commission 2
        (str_store_string, s12, "@Cancel C2"),
        (create_game_button_overlay, "$g_presentation_credits_obj_2", s12, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_credits_obj_2", pos1),
        
### Cancel Commission 3
        (str_store_string, s12, "@Cancel C3"),
        (create_game_button_overlay, "$g_presentation_credits_obj_3", s12, tf_center_justify),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_credits_obj_3", pos1),
        
### Close
        # (create_game_button_overlay, "$g_presentation_obj_name_kingdom_2", "str_done", tf_center_justify),
        # (position_set_x, pos1, 750),
        # (position_set_y, pos1, 40),
        # (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),

### Return to Commissions
        (str_store_string, s11, "@Commission Items"),
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_1", s11, tf_center_justify),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),

        (presentation_set_duration, 999999),
        ]),

      # (hover,[
        # (call_script, "script_custom_troop_detail_inventory_tooltip"),
      # ]),
    # (event, 
      # [
        # (store_trigger_param_1, ":object_id"),
        # (eq, ":object_id", "$g_presentation_obj_name_kingdom_2"), # Continue
        # (assign, "$g_presentation_state", 0),
        # (presentation_set_duration, 0),
        # (jump_to_menu, "mnu_dac_name_troops_2"),
      # ]),

    (click,
    [
    (store_trigger_param_1, ":object_id"),
    (try_begin),
        (eq, ":object_id", "$g_presentation_credits_obj_1"),
        (display_message, "@Cancel Commission 1"),
    (else_try),
        (eq, ":object_id", "$g_presentation_credits_obj_2"),
        (display_message, "@Cancel Commission 2"),
    (else_try),
        (eq, ":object_id", "$g_presentation_credits_obj_3"),
        (display_message, "@Cancel Commission 3"),
    (else_try),
        (eq, ":object_id", "$g_presentation_obj_name_kingdom_1"), # Quartermaster
        (assign, "$g_presentation_state", 0),
        (assign, "$g_presentation_credits_obj_4", -1),
        (assign, "$g_presentation_credits_obj_5", -1),
        (assign, "$g_presentation_credits_obj_6", -1),
        (assign, "$g_presentation_credits_obj_7", -1),
        (start_presentation, "prsnt_dac_ct_buy_items_for_armoury"),
    (try_end),
    ]),


      ] 
        + coord_helper 
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

        (assign, ":base_scroll_y", 320),
        (assign, ":base_scroll_y_2", 320),
        (assign, ":base_scroll_size_y", 360), 
        (assign, ":base_scroll_size_y_2", 360), 
        (assign, ":base_candidates_y", 0), 
        (assign, ":y_shift", 25),
        
########## Text Headers  #####
    
# Troop List Header      
        (create_text_overlay, reg0, "str_dac_player_camp_recruitment", tf_center_justify),
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg0, pos1),
# Troop Recruitment Requirements  
        (create_text_overlay, reg1, "str_dac_player_camp_requirements", tf_center_justify),
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 260),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
# Party Information       
        (try_begin),
            (eq, "$g_presentation_obj_4_val", 0),
            (str_store_string, s1, "str_dac_player_camp_party_info"),
        (else_try),
            (eq, "$g_presentation_obj_4_val", 1),
            (str_store_string, s1, "str_dac_player_camp_troop_info"),
        (else_try),
            (eq, "$g_presentation_obj_4_val", 2),
            (str_store_string, s1, "str_dac_player_camp_troop_inv"),
        (try_end),
        
        (create_text_overlay, reg2, s1, tf_center_justify),
        (position_set_x, pos1, 160),
        (position_set_y, pos1, 715),
        (overlay_set_position, reg2, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg2, pos1),
# Player Information        
        (create_text_overlay, reg3, "str_dac_player_camp_player_info", tf_center_justify),
        (position_set_x, pos1, 160),
        (position_set_y, pos1, 260),
        (overlay_set_position, reg3, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg3, pos1),
        
########## Containers and Panels
### Party Information Panel + Troop Information Panel + Troop Equipment Panel
        (create_text_overlay, "$g_presentation_credits_obj_9", "str_empty_string", tf_scrollable_style_2),
        (position_set_x, pos1, 30),
        (position_set_y, pos1, ":base_scroll_y_2"),
        (overlay_set_position, "$g_presentation_credits_obj_9", pos1),
        (position_set_x, pos1, 262),
        (position_set_y, pos1, ":base_scroll_size_y_2"),
        (overlay_set_area_size, "$g_presentation_credits_obj_9", pos1),   

        ### Set container
        (set_container_overlay, "$g_presentation_credits_obj_9"),   
        
        (assign, ":container_x_value_2", 255),

        (try_begin),
        
            (eq, "$g_presentation_obj_4_val", 0),
        
            (party_get_slot, ":manpower_amount",    "p_player_camp", slot_player_camp_manpower_amount),    
            (party_get_slot, ":recruit_amount",     "p_player_camp", slot_player_camp_recruit_amount),    
            (party_get_slot, ":veteran_amount",     "p_player_camp", slot_player_camp_veteran_amount),    
            (party_get_slot, ":noble_amount",       "p_player_camp", slot_player_camp_noble_amount),    

            (party_get_slot, ":manpower_limit",    "p_player_camp", slot_player_camp_manpower_limit),    
            (party_get_slot, ":recruit_limit",     "p_player_camp", slot_player_camp_recruit_limit),    
            (party_get_slot, ":veteran_limit",     "p_player_camp", slot_player_camp_veteran_limit),    
            (party_get_slot, ":noble_limit",       "p_player_camp", slot_player_camp_noble_limit),   
            
            (party_get_slot, ":player_camp_level", "p_player_camp", slot_player_camp_level),

            (assign, reg30, ":manpower_amount"),
            (assign, reg31, ":manpower_limit"),
            (assign, reg32, ":recruit_amount"),
            (assign, reg33, ":recruit_limit"),
            (assign, reg34, ":veteran_amount"),
            (assign, reg35, ":veteran_limit"),
            (assign, reg36, ":noble_amount"),
            (assign, reg37, ":noble_limit"),
            
            (str_store_string, s3, "str_dac_player_camp_manpower"),
            (str_store_string, s4, "@{reg30}/{reg31}"),
            (str_store_string, s5, "str_dac_player_camp_recruits"),
            (str_store_string, s6, "@{reg32}/{reg33}"),
            (str_store_string, s7, "str_dac_player_camp_veterans"),
            (str_store_string, s8, "@{reg34}/{reg35}"),
            (str_store_string, s9, "str_dac_player_camp_nobles"),
            (str_store_string, s10, "@{reg36}/{reg37}"),
            
            
# Manpower  
            (create_text_overlay, reg1, s3, tf_left_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg1, s4, tf_right_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":container_x_value_2"),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
# Recruits
            (val_sub, ":base_scroll_y_2", ":y_shift"),
            
            (create_text_overlay, reg1, s5, tf_left_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg1, s6, tf_right_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":container_x_value_2"),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
# Veterans
            (val_sub, ":base_scroll_y_2", ":y_shift"),
            
            (create_text_overlay, reg1, s7, tf_left_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg1, s8, tf_right_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":container_x_value_2"),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
# Nobles
            (val_sub, ":base_scroll_y_2", ":y_shift"),
            
            (create_text_overlay, reg1, s9, tf_left_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg1, s10, tf_right_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":container_x_value_2"),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
# Improvements
            (val_sub, ":base_scroll_y_2", ":y_shift"),
            (val_sub, ":base_scroll_y_2", ":y_shift"),
            
            (str_clear, s4),
            
            (try_begin),
                (eq, ":player_camp_level", 1),
                (str_store_string, s3, "@Camp"),
            (else_try),
                (eq, ":player_camp_level", 2),
                (str_store_string, s3, "@Outpost"),
            (else_try),
                (eq, ":player_camp_level", 3),
                (str_store_string, s3, "@Manor"),
            (else_try),
                (str_store_string, s3, "@Fort"),
            (try_end),
            
            (assign, ":num_improvements", 0),

            (try_for_range, ":improvement_no", slot_player_camp_smithy, slot_player_camp_level),
                (party_slot_ge, "p_player_camp", ":improvement_no", 1),
                (val_add,  ":num_improvements", 1),
                (call_script, "script_player_camp_get_improvement_details", ":improvement_no"), ### Uses s0 and s1
                (try_begin),
                    (eq,  ":num_improvements", 1),
                    (str_store_string, s4, "@{!} » {s0}"),
                (else_try),
                    (str_store_string, s4, "@{!}{s4}^ » {s0}"),
                (try_end),
            (try_end),

            (try_begin),
                (eq,  ":num_improvements", 0),
                (str_store_string, s11, "@The {s3} has no improvements."),
            (else_try),
                (str_store_string, s11, "@{s3} buildings:"),
            (try_end),  
            
            (create_text_overlay, reg2, s11, tf_left_align),
            (overlay_set_color, reg2, 0xFFFFFFFF),
            (position_set_x, pos1, 900),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg2, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg2, pos1),
            
            (try_begin),
                (gt,  ":num_improvements", 0),
                
                (store_mul, ":y_shift_improvements", ":y_shift", ":num_improvements"),
                (val_sub, ":base_scroll_y_2", ":y_shift_improvements"),
                
                (create_text_overlay, reg3, s4, tf_left_align),
                (overlay_set_color, reg3, 0xFFFFFFFF),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg3, pos1),
                (position_set_x, pos1, 0),
                (position_set_y, pos1, ":base_scroll_y_2"),
                (overlay_set_position, reg3, pos1),
            (try_end),
            
        (else_try), ### Troop Information
        
            (eq, "$g_presentation_obj_4_val", 1),
            (gt, "$character_info_id", -1),
            
            (troop_get_class, ":troop_class", "$character_info_id"),
            (store_character_level, ":troop_level", "$character_info_id"),
            (assign, reg2, ":troop_level"),
            
            (store_troop_health, reg8, "$character_info_id", 1),
            (str_store_string, s19, "@Health:"),
            (str_store_string, s20, "@{reg8}"),
            (str_store_string, s21, "@Weapon Proficiencies"),
            (str_store_string, s22, "@Skills"),
            
            (str_store_string, s1, "@Troop Class:"),
            
            (try_begin),
                (eq, ":troop_class", 0),
                (str_store_string, s8, "@Infantry"),
            (else_try),
                (eq, ":troop_class", 1),
                (str_store_string, s8, "@Archer"),
            (else_try),
                (eq, ":troop_class", 2),
                (str_store_string, s8, "@Cavalry"),
            (else_try),
                (str_store_string, s8, "@Other"),
            (try_end),
            
            (str_store_string, s2, "@Troop Level:"),
            (str_store_string, s9, "@{reg2}"),
            
            (call_script, "script_game_get_troop_wage", "$character_info_id", 0),
            (assign, reg3, reg0), # Wage
            
            (str_store_string, s3, "@Troop Wage:"),
            (str_store_string, s10, "@{reg3}"),
            
            (store_attribute_level, reg4, "$character_info_id", ca_strength),
            (store_attribute_level, reg5, "$character_info_id", ca_agility),
        
            (str_store_string, s4, "@Strenght:"),
            (str_store_string, s11, "@{reg4}"),
            (str_store_string, s5, "@Agility:"),
            (str_store_string, s12, "@{reg5}"),
            
            (str_clear, s6),
            (str_clear, s15),
            
            (try_for_range, ":proficiency", wpt_one_handed_weapon, wpt_firearm + 1),
                (store_proficiency_level, reg6, "$character_info_id", ":proficiency"),
                (gt, reg6, 0),
                (store_add, ":string", "str_dac_wpt_onehanded", ":proficiency"),
                (str_store_string, s14, ":string"),
                (str_store_string, s6, "@{s6}^{s14}:"),
                (str_store_string, s15, "@{s15}^{reg6}"),
            (try_end),
            
            (str_clear, s7),
            (str_clear, s18),
            (try_for_range_backwards, ":skill", skl_trade, skl_reserved_18 + 1),
                (this_or_next|eq, ":skill", skl_ironflesh),
                (this_or_next|eq, ":skill", skl_power_strike),
                (this_or_next|eq, ":skill", skl_power_throw),
                (this_or_next|eq, ":skill", skl_power_draw),
                (this_or_next|eq, ":skill", skl_weapon_master),
                (this_or_next|eq, ":skill", skl_shield),
                (this_or_next|eq, ":skill", skl_athletics),
                (this_or_next|eq, ":skill", skl_riding),
                (eq, ":skill", skl_horse_archery),
                (store_skill_level, reg7, ":skill", "$character_info_id"),
                (gt, reg7, 0),
                (store_add, ":string", "str_skl_trade", ":skill"),
                (str_store_string, s16, ":string"),
                (str_store_string, s7, "@{s7}^{s16}:"),
                (str_store_string, s18, "@{s18}^{reg7}"),
            (try_end),
            
            (str_store_string, s19, "@{s1}^{s2}^{s3}^^{s19}^{s4}^{s5}^^{s21}{s6}^^{s22}{s7}"),
            (str_store_string, s20, "@{s8}^{s9}^{s10}^^{s20}^{s11}^{s12}^^{s15}^^{s18}"),
                    
### Troop Class
            (create_text_overlay, reg1, s19, tf_left_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg1, s20, tf_right_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":container_x_value_2"),
            (position_set_y, pos1, ":base_scroll_y_2"),
            (overlay_set_position, reg1, pos1),            
            
        (else_try), ### Troop Inventory
        
            (eq, "$g_presentation_obj_4_val", 2),
            (gt, "$character_info_id", -1),
            
            (troop_sort_inventory, "$character_info_id"),
            (troop_get_inventory_capacity, ":num_slots", "$character_info_id"),
            (store_free_inventory_capacity, ":num_free_slots", "$character_info_id"),
            (store_sub, ":num_items", ":num_slots", ":num_free_slots"),
            #(val_sub, ":num_items", 10),
      
            (store_div, ":y_max", ":num_items", 1),

            (assign, ":box_incr", 115),
            (val_max, ":y_max", 1),
            (val_mul, ":y_max", ":box_incr"),

            (assign, ":x_item", 75),
            (store_add, ":y_item", ":y_max", 60),
            (assign, ":count", 0),
            (assign, ":x_box", 15),
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
                (troop_get_inventory_slot, ":item", "$character_info_id", ":slot"),
                (neq, ":item", -1),
                (troop_get_inventory_slot_modifier, ":item_imod", "$character_info_id", ":slot"),

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
                        (assign, ":x_item", 75),
                        (assign, ":x_box", 15),
                    (try_end),
          
                #tooltip
                    (store_add, reg0, ":count", ":imod_slot_add"),
                    (troop_set_slot, "trp_temp_array_d", ":count", reg1),
                    (troop_set_slot, "trp_temp_array_e", ":count", ":item"),
                    (troop_set_slot, "trp_temp_array_e", reg0, ":item_imod"),
                (try_end),
            (try_end),
      
            (assign, "$temp", ":count"),
                      
    (try_end),
        
        (set_container_overlay, -1), 
        
### Player Information Panel
        (create_text_overlay, "$g_presentation_credits_obj_8", "str_empty_string", tf_scrollable_style_2),
        (position_set_x, pos1, 30),
        (position_set_y, pos1, 120),
        (overlay_set_position, "$g_presentation_credits_obj_8", pos1),
        (position_set_x, pos1, 262),
        (position_set_y, pos1, 115),
        (overlay_set_area_size, "$g_presentation_credits_obj_8", pos1),
        
        (set_container_overlay, "$g_presentation_credits_obj_8"), 
        
            # Variables
            (assign, ":container_x_value", 255),
            (assign, ":y_value", 180),

            (call_script, "script_game_get_party_companion_limit"),
            (assign, ":party_size_limit", reg0),
            (party_get_num_companions, ":num_companions", "p_main_party"),
            (troop_get_slot, ":renown", "trp_player", slot_troop_renown),       
            (store_troop_gold, ":gold", "trp_player"),
            
            ### Get troop types
            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
            
            (assign, ":mounted_troops", 0),
            (assign, ":ranged_troops", 0),
            (assign, ":infantry_troops", 0),
        
            (try_for_range, ":i_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
                (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
                (try_begin),
                    (troop_is_mounted, ":stack_troop"),
                    (val_add, ":mounted_troops", ":stack_size"),
                (else_try),
                    (troop_is_guarantee_ranged, ":stack_troop"),                
                    (val_add, ":ranged_troops", ":stack_size"),
                (else_try),
                    (val_add, ":infantry_troops", ":stack_size"),
                (try_end),
            (try_end),

            (assign, reg13, ":gold"),
            (assign, reg14, ":renown"),
            (assign, reg15, "$player_honor"),
            (assign, reg16, ":num_companions"),
            (assign, reg17, ":party_size_limit"),
            (assign, reg18, ":mounted_troops"),
            (assign, reg19, ":infantry_troops"),        
            (assign, reg20, ":ranged_troops"),
            
            (str_store_string, s1, "@Crowns:^Renown:^Honor:^^Party Size:^Cavalry:^Infantry:^Archers:"),
            (str_store_string, s2, "@{reg13}^{reg14}^{reg15}^^{reg16}/{reg17}^{reg18}^{reg19}^{reg20}"),
            
            # Panels
            (create_text_overlay, reg1, s1, tf_left_align),
            (overlay_set_color, reg1, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg2, s2, tf_right_align),
            (overlay_set_color, reg2, 0xFFFFFFFF),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg2, pos1),
            (position_set_x, pos1, ":container_x_value"),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg2, pos1),
            
        (set_container_overlay, -1), 
        
### Selected Troop
        (try_begin),
            (neq, "$character_info_id", -1),
            (str_store_troop_name, s1, "$character_info_id"),
        (else_try),
            (str_store_string, s1, "str_empty_string"),
        (try_end),
        
        (create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_with_outline),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 500), 
        (position_set_y, pos1, 715), 
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
            
            
### Variable initialization
            (assign, ":container_x_value", 255),
            (assign, ":y_value", 180),
            (assign, ":overlay_colour", color_neutral_news),
            
            (troop_get_slot, ":manpower_cost", "$character_info_id", slot_troop_manpower_cost),
            (troop_get_slot, ":troop_class", "$character_info_id", slot_troop_recruit_class),
            (call_script, "script_game_get_join_cost", "$character_info_id"),
            (assign, ":join_cost", reg0),
            
            ### Set container
            (set_container_overlay, "$g_presentation_credits_obj_10"),
            
            ### Hiring Cost
            (assign, reg18, ":join_cost"),
            (str_store_string, s13, "@Cost:"),
            (str_store_string, s14, "@{reg18}"),
           
            (try_begin),
                (ge, ":gold", ":join_cost"),
                (assign, ":overlay_colour", color_good_news),
            (else_try),
                (assign, ":overlay_colour", color_bad_news),
            (try_end),
            
            (create_text_overlay, reg1, s13, tf_left_align),
            (overlay_set_color, reg1, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, "$g_presentation_credits_obj_1", s14, tf_right_align),
            (overlay_set_color, "$g_presentation_credits_obj_1", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_1", pos1),
            (position_set_x, pos1, ":container_x_value"),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_1", pos1),
            
            ### Manpower
            (assign, reg20, ":manpower_cost"),
            (str_store_string, s15, "@Manpower:"),
            (str_store_string, s16, "@{reg20}"),
            (val_sub, ":y_value", ":y_shift"),
            
            (try_begin),
                (party_slot_ge, "p_player_camp", slot_player_camp_manpower_amount, ":manpower_cost"),
                (assign, ":overlay_colour", color_good_news),
            (else_try),
                (assign, ":overlay_colour", color_bad_news),
            (try_end),            
            
            (create_text_overlay, reg1, s15, tf_left_align),
            (overlay_set_color, reg1, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, "$g_presentation_credits_obj_2", s16, tf_right_align),
            (overlay_set_color, "$g_presentation_credits_obj_2", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_2", pos1),
            (position_set_x, pos1, ":container_x_value"),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_2", pos1),
            

            ### Troop Type
            (assign, ":overlay_colour", color_bad_news),
            
            (try_begin),
                (eq, ":troop_class", TROOP_CLASS_RECRUIT),
                (str_store_string, s17, "@Recruit:"),
                (try_begin),
                    (party_slot_ge, "p_player_camp", slot_player_camp_recruit_amount, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (eq, ":troop_class", TROOP_CLASS_VETERAN),
                (str_store_string, s17, "@Veteran:"),            
                (try_begin),
                    (party_slot_ge, "p_player_camp", slot_player_camp_veteran_amount, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (eq, ":troop_class", TROOP_CLASS_NOBLE),
                (str_store_string, s17, "@Noble:"),   
                (try_begin),
                    (party_slot_ge, "p_player_camp", slot_player_camp_noble_amount, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),                
            (try_end),
            
            (str_store_string, s18, "@1"), 
            (val_sub, ":y_value", ":y_shift"),
            
            (create_text_overlay, reg1, s17, tf_left_align),
            (overlay_set_color, reg1, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, "$g_presentation_credits_obj_3", s18, tf_right_align),
            (overlay_set_color, "$g_presentation_credits_obj_3", ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, "$g_presentation_credits_obj_3", pos1),
            (position_set_x, pos1, ":container_x_value"),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, "$g_presentation_credits_obj_3", pos1),

            
            ### Building 1
            (assign, ":overlay_colour", color_bad_news),
            
            (str_store_string, s19, "@Building:"),
            
            (try_begin),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_1, TROOP_REQ_BUILDING_CORRAL), 
                (str_store_string, s20, "@Corral"),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_1, TROOP_REQ_BUILDING_RANGE), 
                (str_store_string, s20, "@Archery Range"),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_archery_range, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_1, TROOP_REQ_BUILDING_CHAPTERHOUSE), 
                (str_store_string, s20, "@Chapterhouse"),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_chapterhouse, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (str_store_string, s19, "str_empty_string"),            
                (str_store_string, s20, "str_empty_string"),            
            (try_end),
            
            (val_sub, ":y_value", ":y_shift"),
            
            (create_text_overlay, reg1, s19, tf_left_align),
            (overlay_set_color, reg1, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg2, s20, tf_right_align),
            (overlay_set_color, reg2, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg2, pos1),
            (position_set_x, pos1, ":container_x_value"),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg2, pos1),


            ### Building 2
            (assign, ":overlay_colour", color_bad_news),
            (try_begin),
                (troop_slot_eq, "$character_info_id", slot_troop_building_req_2, TROOP_REQ_BUILDING_CORRAL), 
                (str_store_string, s21, "@Corral"),
                (try_begin),
                    (party_slot_eq, "p_player_camp", slot_player_camp_corral, 1),
                    (assign, ":overlay_colour", color_good_news),
                (try_end),
            (else_try),
                (str_store_string, s19, "str_empty_string"),            
                (str_store_string, s21, "str_empty_string"),            
            (try_end),
            
            (val_sub, ":y_value", ":y_shift"),

            (create_text_overlay, reg1, s19, tf_left_align),
            (overlay_set_color, reg1, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),
            
            (create_text_overlay, reg1, s21, tf_right_align),
            (overlay_set_color, reg1, ":overlay_colour"),
            (position_set_x, pos1, 1000),
            (position_set_y, pos1, 1000),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":container_x_value"),
            (position_set_y, pos1, ":y_value"),
            (overlay_set_position, reg1, pos1),

### The end
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
     
        (assign, ":num_chars", 0),
        (assign, ":num_slot", 0),
        (try_for_range, ":recruit", mercenary_troops_begin, customizable_troops_end),
            (store_sub, ":delta", ":recruit", mercenary_troops_begin),
            (store_sub, ":troop", customizable_troops_end, ":delta"),
            
            (call_script, "script_dac_player_camp_troop_can_be_recruited", ":troop"),
            (eq, reg0, 1),

            (store_mul, ":y_mult", ":num_chars", 16 * 1.4), # adapt y position to entry number, was 18
            (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

            (set_container_overlay, "$g_presentation_obj_1"),
            
            (str_store_troop_name, s1, ":troop"),
            (troop_get_slot, ":icon", ":troop", slot_troop_recruitment_icon),
            
            (try_begin),
                (le, ":icon", 0),
                (assign, ":icon", "mesh_icon_dagger"),
            (try_end),

            (create_text_overlay, reg10, "@ {s1}", tf_left_align),
            (overlay_set_color, reg10, 0xDDDDDD),
            (position_set_x, pos1, 590 * 1.4),
            (position_set_y, pos1, 700 * 1.4),
            (overlay_set_size, reg10, pos1),
            (position_set_x, pos1, 25),  
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),
            
            #add icons
            (store_add, ":line_y_icon", ":line_y", 8),

            (create_mesh_overlay, reg9, ":icon"),
            (position_set_x, pos1, 510),
            (position_set_y, pos1, 500),
            (overlay_set_size, reg9, pos1),
            (position_set_x, pos1, 15),
            (position_set_y, pos1, ":line_y_icon"),
            (overlay_set_position, reg9, pos1),

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
        
### Troop Mesh
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
            (position_set_x, pos1, 500),
            (position_set_y, pos1, 25),
            (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFFFF),
            (overlay_set_position, "$g_presentation_obj_3", pos1),
        
        (try_end),
        
###  Panel switch
        (create_combo_label_overlay, "$g_presentation_obj_4"),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        
        (overlay_add_item, "$g_presentation_obj_4", "@Party Information"),
        (overlay_add_item, "$g_presentation_obj_4", "@Troop Information"),
        (overlay_add_item, "$g_presentation_obj_4", "@Troop Inventory"),
        
        (overlay_set_val, "$g_presentation_obj_4", "$g_presentation_obj_4_val"),
        
###  Quit
        (create_in_game_button_overlay, "$g_presentation_obj_2", "str_done", tf_left_align),
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 25),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFFFF),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        ]),

      (hover,[
        (gt, "$character_info_id", -1),
        (eq, "$g_presentation_obj_4_val", 2), # Troop Inventory
        (call_script, "script_custom_troop_detail_inventory_tooltip_right"),
      ]),

      (event,[
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (assign, ":val_changed", 0),

        (try_begin),
            (eq, ":object", "$g_presentation_obj_4"),
            (assign, "$g_presentation_obj_4_val", ":value"),
            (start_presentation, "prsnt_dac_mercenary_camp_recruitment"),
        (else_try),
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
            (assign, reg2, reg0),
            (store_mul, reg3, reg2, "$g_presentation_obj_sliders_1_val"),
            
            (str_store_string, s2, "@Hire {reg1} for {reg3} Crowns"),
            (overlay_set_text, "$g_presentation_obj_3", s2),              
            
            (troop_get_slot, ":manpower_cost", "$character_info_id", slot_troop_manpower_cost),
            (assign, reg4, ":manpower_cost"),
            (store_mul, reg5, ":manpower_cost", "$g_presentation_obj_sliders_1_val"),

            (assign, reg6, "$g_presentation_obj_sliders_1_val"),
            
            (try_begin),
                (gt, "$g_presentation_obj_sliders_1_val", 1),
                (str_store_string, s3, "@{reg2} » {reg3}"),
                (overlay_set_text, "$g_presentation_credits_obj_1", s3), 
                
                (str_store_string, s4, "@{reg4} » {reg5}"),
                (overlay_set_text, "$g_presentation_credits_obj_2", s4),  
                
                (str_store_string, s5, "@1 » {reg6}"),
                (overlay_set_text, "$g_presentation_credits_obj_3", s5), 
            (else_try),
                (str_store_string, s3, "@{reg2}"),
                (overlay_set_text, "$g_presentation_credits_obj_1", s3), 
                
                (str_store_string, s4, "@{reg4}"),
                (overlay_set_text, "$g_presentation_credits_obj_2", s4), 
                
                (str_store_string, s5, "@{reg6}"),
                (overlay_set_text, "$g_presentation_credits_obj_3", s5), 
            (try_end),
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
            (try_for_range, ":i", 0, ":num_troops"),
                (troop_get_slot, ":control", "trp_temp_array_a", ":i"),
                (eq, ":control", ":object_id"),
                (troop_get_slot, "$character_info_id", "trp_temp_array_b", ":i"),
                (start_presentation, "prsnt_dac_mercenary_camp_recruitment"),
                (assign, ":num_troops", 0),
            (try_end), 
        (try_end),
    ]),


      ] 
        # + coord_helper 
        # + prsnt_escape_close
        ),



]