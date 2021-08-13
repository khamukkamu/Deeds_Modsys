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
##diplomacy end

from compiler import *

character_creation_presentations = [
 ("dac_select_lord_or_king", 0, mesh_message_window,
   [
     (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (str_clear, s0),
        (str_clear, s1),

        (assign, ":base_scroll_y", 110),
        (assign, ":base_scroll_size_y", 550), 
        (assign, ":base_candidates_y", 0), 

        (create_mesh_overlay, reg1, "mesh_face_gen_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),

        #(create_text_overlay, reg1, "@_Select Lord_", tf_center_justify),
        #(overlay_set_color, reg1, 0xDDDDDD),
        #(position_set_x, pos1, 500), # Higher, means more toward the right
        #(position_set_y, pos1, 705), # Higher, means more toward the top
        #(overlay_set_position, reg1, pos1),
        #(position_set_x, pos1, 2000),
        #(position_set_y, pos1, 2000),
        #(overlay_set_size, reg1, pos1),

        (try_begin),
          (neq, -1, "$character_info_id"),
          (str_store_troop_name, s1, "$character_info_id"),
        (else_try),
          (str_store_string, s1, "str_empty_string"),
        (try_end),
        (create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_with_outline),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 285), # Higher, means more toward the right
        (position_set_y, pos1, 233), # Higher, means more toward the top
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),

        (create_game_button_overlay, "$g_presentation_obj_2", "@_Back_"),
        (position_set_x, pos1, 280), #Was 540
        (position_set_y, pos1, 10),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

        (try_begin),
          (neq, "$character_info_id", -1),
          (create_game_button_overlay, "$g_presentation_obj_1", "@_Done_"),
          (position_set_x, pos1, 762), #Was 540
          (position_set_y, pos1, 10),
          (overlay_set_position, "$g_presentation_obj_1", pos1),
        (try_end),

        (try_begin),
          (neq, -1, "$character_info_id"),
          (call_script, "script_dac_get_info_about_lord", "$character_info_id", 0),
        (else_try),
          (str_store_string, s49, "str_empty_string"),
        (try_end),

### DAC Seek: attempt to add lord fief list
        (create_text_overlay, "$g_presentation_obj_6", s0, tf_left_align | tf_scrollable),
        (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFF),
        (position_set_x, pos1, 55), # Higher, means more toward the right
        (position_set_y, pos1, 55), # Higher, means more toward the top
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 1000), # smaller means smaller font
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 520 - 55 - 20), # smaller means smaller font
        (position_set_y, pos1, 210 - 55),
        (overlay_set_area_size, "$g_presentation_obj_6", pos1),
        
# DAC Seek: Backup:
        # (create_text_overlay, "$g_presentation_obj_6", s49, tf_left_align | tf_scrollable),
        # (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFF),
        # (position_set_x, pos1, 55), # Higher, means more toward the right
        # (position_set_y, pos1, 55), # Higher, means more toward the top
        # (overlay_set_position, "$g_presentation_obj_6", pos1),
        # (position_set_x, pos1, 1000), # smaller means smaller font
        # (position_set_y, pos1, 1000),
        # (overlay_set_size, "$g_presentation_obj_6", pos1),
        # (position_set_x, pos1, 520 - 55 - 20), # smaller means smaller font
        # (position_set_y, pos1, 210 - 55),
        # (overlay_set_area_size, "$g_presentation_obj_6", pos1),

        (create_combo_label_overlay, "$g_presentation_obj_5", "str_empty_string",0),
        (position_set_x, pos1, 755),
        (position_set_y, pos1, 668),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_5", pos1),

        # add elements to filter button
        (overlay_add_item, "$g_presentation_obj_5", "str_sel_lord_fac_adj_0"),
        (overlay_add_item, "$g_presentation_obj_5", "str_sel_lord_fac_adj_1"),
        (overlay_add_item, "$g_presentation_obj_5", "str_sel_lord_fac_adj_2"),
        (overlay_add_item, "$g_presentation_obj_5", "str_sel_lord_fac_adj_3"),
        (overlay_add_item, "$g_presentation_obj_5", "str_sel_lord_fac_adj_4"),

        (overlay_set_val, "$g_presentation_obj_5", "$select_lord_filter_value"),

        # (create_text_overlay, reg1, "@Filter: ", tf_left_align),
        # (overlay_set_color, reg1, 0xFF000000),
        # (position_set_x, pos1, 590), 
        # (position_set_y, pos1, 75),
        # (overlay_set_position, reg1, pos1),
        # (position_set_x, pos1, 1000),
        # (position_set_y, pos1, 1000),
        # (overlay_set_size, reg1, pos1),

        (create_text_overlay, "$g_presentation_obj_3", "str_empty_string", tf_scrollable_style_2),
        (position_set_x, pos1, 590),
        (position_set_y, pos1, ":base_scroll_y"),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (position_set_x, pos1, 335),
        (position_set_y, pos1, ":base_scroll_size_y"),
        (overlay_set_area_size, "$g_presentation_obj_3", pos1),

        # Fill listbox (overlay_add_item and extra storage)
        (store_add, ":end_lord", "trp_knight_4_18", 1),
        (assign, ":num_chars", 0),
        (assign, ":num_slot", 0),
        (try_for_range, ":lord_iter", "trp_kingdom_1_lord", ":end_lord"),
            (store_sub, ":delta", ":lord_iter", "trp_kingdom_1_lord"),
            (store_sub, ":lord", "trp_knight_4_18", ":delta"),

            (call_script, "script_cf_select_lord_lord_in_culture", ":lord", "$select_lord_filter_value"),

            (store_mul, ":y_mult", ":num_chars", 16 * 1.4), # adapt y position to entry number, was 18
            (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

            (set_container_overlay, "$g_presentation_obj_3"),
            
            (str_store_troop_name, s1, ":lord"),

            (try_begin),
              (eq, 0, "$select_lord_filter_value"),
              (str_store_string, s2, "@   "),
            (else_try),
              (str_store_string, s2, "str_empty_string"),
            (try_end),

            (create_text_overlay, reg10, "@{s2}{s1}", tf_left_align),
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
                (eq, ":lord", "$character_info_id"),
                (overlay_set_color, reg10, 0xFF6666FF),
                (overlay_set_alpha, reg10, 0x44),
            (try_end),

            (troop_set_slot, "trp_temp_array_a", ":num_slot", reg10),
            (troop_set_slot, "trp_temp_array_b", ":num_slot", ":lord"),
            (val_add, ":num_chars", 1),
            (val_add, ":num_slot", 1),

            (set_container_overlay, -1),
                (eq, 0, "$select_lord_filter_value"),
                (try_begin),
                  (this_or_next|eq, "trp_knight_4_1", ":lord"),
                  (this_or_next|eq, "trp_knight_3_1", ":lord"),
                  (this_or_next|eq, "trp_knight_2_1", ":lord"),
                  (eq, "trp_knight_1_1", ":lord"),

                  (store_troop_faction, ":fac", ":lord"),

                  (store_sub, ":str", ":fac", "fac_kingdom_1"),
                  (val_add, ":str", "str_sel_lord_fac_adj_1"),
                  (str_store_string, s1, ":str"),

                  (store_mul, ":y_mult", ":num_chars", 16 * 1.4), # adapt y position to entry number, was 18
                  (store_add, ":line_y", ":base_candidates_y", ":y_mult"),
                  (val_add, ":num_chars", 1),

                  (set_container_overlay, "$g_presentation_obj_3"),
                  (create_text_overlay, reg10, "@{s1}:", tf_left_align),
                  (overlay_set_color, reg10, 0xDDDDDD),
                  (position_set_x, pos1, 650 * 1.4),
                  (position_set_y, pos1, 750 * 1.4),
                  (overlay_set_size, reg10, pos1),
                  (position_set_x, pos1, 0),  
                  (position_set_y, pos1, ":line_y"),
                  (overlay_set_position, reg10, pos1),
                  (set_container_overlay, -1),
                (else_try),
                  (eq, "trp_kingdom_1_lord", ":lord"),

                  (store_mul, ":y_mult", ":num_chars", 16 * 1.4), # adapt y position to entry number, was 18
                  (store_add, ":line_y", ":base_candidates_y", ":y_mult"),
                  (val_add, ":num_chars", 1),

                  (set_container_overlay, "$g_presentation_obj_3"),
                  (create_text_overlay, reg10, "@Rulers:", tf_left_align),
                  (overlay_set_color, reg10, 0xDDDDDD),
                  (position_set_x, pos1, 650 * 1.4),
                  (position_set_y, pos1, 750 * 1.4),
                  (overlay_set_size, reg10, pos1),
                  (position_set_x, pos1, 0),  
                  (position_set_y, pos1, ":line_y"),
                  (overlay_set_position, reg10, pos1),
                  (set_container_overlay, -1),
                (try_end),
            (try_begin),
            (try_end),
        (try_end),

        # color selected entry
#        (overlay_set_color, "$g_jrider_last_checked_indicator", 0xFF6666FF),
#        (overlay_set_alpha, "$g_jrider_last_checked_indicator", 0x44),
        
        (try_begin),
          (neq, "$character_info_id", -1),
          (create_image_button_overlay_with_tableau_material, "$g_presentation_obj_4", -1, "tableau_troop_note_mesh", "$character_info_id"),
          (position_set_x, pos2, 100),
          (position_set_y, pos2, 280),
          (overlay_set_position, "$g_presentation_obj_4", pos2),
          (position_set_x, pos2, 1100), #1150
          (position_set_y, pos2, 1100), #1150
          (overlay_set_size, "$g_presentation_obj_4", pos2),
        (try_end),


    ]),

    (ti_on_presentation_event_state_change, [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":state"),
        

      (try_begin),
        (eq, ":object", "$g_presentation_obj_5"),
        (assign, "$select_lord_filter_value", ":state"),
        (try_begin),
          (neq, "$character_info_id", -1),
          (call_script, "script_cf_neg_select_lord_lord_in_culture", "$character_info_id", "$select_lord_filter_value"),
          (assign, "$character_info_id", -1),
        (try_end),
        (start_presentation, "prsnt_dac_select_lord_or_king"),
      (else_try),
        (eq, ":object", "$g_presentation_obj_1"),
        (assign, "$dac_selected_lord", "$character_info_id"),
        (jump_to_menu, "mnu_dac_choose_skill"),
        (presentation_set_duration, 0),
      (else_try),
        (eq, ":object", "$g_presentation_obj_2"),
        (jump_to_menu, "mnu_start_game_0"),
        (presentation_set_duration, 0),
      (else_try),
        (store_sub, ":num_lords", "trp_knight_4_18", "trp_kingdom_1_lord"),
        (val_add, ":num_lords", 1),
        (try_for_range, ":i", 0, ":num_lords"),
          (troop_get_slot, ":control", "trp_temp_array_a", ":i"),
          (eq, ":control", ":object"),
          (troop_get_slot, "$character_info_id", "trp_temp_array_b", ":i"),
          (start_presentation, "prsnt_dac_select_lord_or_king"),
          (assign, ":num_lords", 0),
        (try_end),

      (try_end),
    ]),

    (ti_on_presentation_run, [
      (try_begin),
        #(key_clicked, key_escape),
        #(presentation_set_duration, 0),
      #(else_try),
        (key_clicked, key_down),
        (neq, "$character_info_id", -1),

        (assign, ":founded", 0),
        (assign, ":lim", lords_end),
        (val_add, "$character_info_id", 1),
        (try_for_range, ":lord", "$character_info_id", ":lim"),
          (eq, ":founded", 0),
          #(str_store_troop_name, s1, ":lord"),
          #(display_message, "@check = {s1}"),
          (call_script, "script_cf_select_lord_lord_in_culture", ":lord", "$select_lord_filter_value"),
          #(display_message, "@ok"),
          (assign, "$character_info_id", ":lord"),
          (assign, ":founded", 1),
          (assign, ":lim", 0),
        (try_end),

        (try_begin),
          (eq, ":founded", 1),
          (start_presentation, "prsnt_dac_select_lord_or_king"),
        (try_end),

        (eq, ":founded", 0),

        (assign, ":lim", lords_end),
        (try_for_range, ":lord", kings_begin, ":lim"),
          (eq, ":founded", 0),
          (call_script, "script_cf_select_lord_lord_in_culture", ":lord", "$select_lord_filter_value"),
          (assign, "$character_info_id", ":lord"),
          (assign, ":founded", 1),
          (assign, ":lim", 0),
        (try_end),
        (start_presentation, "prsnt_dac_select_lord_or_king"),
      (else_try),
        (key_clicked, key_up),
        (neq, "$character_info_id", -1),

        (assign, ":founded", 0),
        (assign, ":lim", "$character_info_id"),
        (try_for_range, ":lord", kings_begin, ":lim"),
          (call_script, "script_cf_select_lord_lord_in_culture", ":lord", "$select_lord_filter_value"),
          (assign, "$character_info_id", ":lord"),
          (assign, ":founded", 1),
        (try_end),

        (try_begin),
          (eq, ":founded", 1),
          (start_presentation, "prsnt_dac_select_lord_or_king"),
        (try_end),

        (eq, ":founded", 0),

        (try_for_range, ":lord", kings_begin, lords_end),
          (call_script, "script_cf_select_lord_lord_in_culture", ":lord", "$select_lord_filter_value"),
          (assign, "$character_info_id", ":lord"),
        (try_end),
        (start_presentation, "prsnt_dac_select_lord_or_king"),
      (try_end),
    ]),
  ]),


("faction_selection",0,mesh_load_window,[
      (ti_on_presentation_load,
       [  
        (set_fixed_point_multiplier, 1000),

        (str_store_string, s1, "@Which Kingdom Do You Serve?"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1750),
        (position_set_y, pos1, 1750),
        (overlay_set_size, reg1, pos1),
        (overlay_set_text, reg1, s1),
        (create_button_overlay, "$g_presentation_obj_1", "@Go Back...", tf_center_justify),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        
    #FRANCE
    #text
     (create_text_overlay, "$g_option_france_text", "@The Kingdom^of France", tf_center_justify|tf_with_outline),
    #(create_button_overlay, "$g_presentation_obj_1", 0, tf_center_justify),
        (position_set_x, pos1, 200), # Higher, means more toward the right
        (position_set_y, pos1, 230), # Higher, means more toward the top
        (overlay_set_position, "$g_option_france_text", pos1),
    (overlay_set_alpha, "$g_option_france_text", 0x7D),
    (overlay_set_color, "$g_option_france_text", 0x4980d8),

    #logo
      #(create_image_button_overlay_with_tableau_material, "$g_option_france", -1, "tableau_faction_note_mesh_banner", "fac_gondor"),
      (create_image_button_overlay, "$g_option_france", "mesh_choose_icon_france", "mesh_choose_icon_france"),
           (position_set_x, pos1, 200),
           (position_set_y, pos1, 380),
           (overlay_set_position, "$g_option_france", pos1),
           (position_set_x, pos1, 350),
           (position_set_y, pos1, 350),
           (overlay_set_size, "$g_option_france", pos1),

    #ENGLAND
    #text
     (create_text_overlay, "$g_option_england_text", "@The Kingdom^of England", tf_center_justify|tf_with_outline),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 230),
        (overlay_set_position, "$g_option_england_text", pos1),
    (overlay_set_alpha, "$g_option_england_text", 0x7D),
    (overlay_set_color, "$g_option_england_text", 0xb21010),

    #logo
      (create_image_button_overlay, "$g_option_england", "mesh_choose_icon_england", "mesh_choose_icon_england"),
           (position_set_x, pos1, 400),
           (position_set_y, pos1, 380),
           (overlay_set_position, "$g_option_england", pos1),
           (position_set_x, pos1, 350),
           (position_set_y, pos1, 350),
           (overlay_set_size, "$g_option_england",pos1),

    #BURGANDY
    #text
     (create_text_overlay, "$g_presentation_obj_item_select_2", "@The Duchy^of Burgundy", tf_center_justify|tf_with_outline),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 230),
        (overlay_set_position, "$g_presentation_obj_item_select_2", pos1),
    (overlay_set_alpha, "$g_presentation_obj_item_select_2", 0x7D),
    (overlay_set_color, "$g_presentation_obj_item_select_2", 0xddb544),

    #logo
      (create_image_button_overlay, "$g_presentation_obj_item_select_3", "mesh_choose_icon_burgandy", "mesh_choose_icon_burgandy"),
           (position_set_x, pos1, 600),
           (position_set_y, pos1, 380),
           (overlay_set_position, "$g_presentation_obj_item_select_3", pos1),
           (position_set_x, pos1, 350),
           (position_set_y, pos1, 350),
           (overlay_set_size, "$g_presentation_obj_item_select_3",pos1),

    #BRITTANY
    #text
     (create_text_overlay, "$g_presentation_obj_item_select_4", "@The Duchy^of Brittany", tf_center_justify|tf_with_outline),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 230),
        (overlay_set_position, "$g_presentation_obj_item_select_4", pos1),
    (overlay_set_alpha, "$g_presentation_obj_item_select_4", 0x7D),
    (overlay_set_color, "$g_presentation_obj_item_select_4", 0x9495a5),

    #logo
      (create_image_button_overlay, "$g_presentation_obj_item_select_5", "mesh_choose_icon_breton", "mesh_choose_icon_breton"),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 380),
           (overlay_set_position, "$g_presentation_obj_item_select_5", pos1),
           (position_set_x, pos1, 350),
           (position_set_y, pos1, 350),
           (overlay_set_size, "$g_presentation_obj_item_select_5",pos1),

        (presentation_set_duration, 999999),
        ]),
    
    (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
      (try_begin),
        (eq, ":object", "$g_presentation_obj_1"),
        (presentation_set_duration, 0),
        (jump_to_menu,"mnu_start_game_1"),
        #(start_presentation, "prsnt_faction_selection"),
      (else_try),
        (eq, ":object", "$g_option_france"),
        (assign, "$background_answer_3", "fac_kingdom_1"),
        (jump_to_menu,"mnu_dac_choose_skill"),
        (presentation_set_duration, 0),
      (else_try),
        (eq, ":object", "$g_option_england"),
        (assign, "$background_answer_3", "fac_kingdom_2"),
        (jump_to_menu,"mnu_dac_choose_skill"),
        (presentation_set_duration, 0),
      (else_try),
        (eq, ":object", "$g_presentation_obj_item_select_3"),
        (assign, "$background_answer_3", "fac_kingdom_3"),
        (jump_to_menu,"mnu_dac_choose_skill"),
        (presentation_set_duration, 0),
      (else_try),
        (eq, ":object", "$g_presentation_obj_item_select_5"),
        (assign, "$background_answer_3", "fac_kingdom_4"),
        (jump_to_menu,"mnu_dac_choose_skill"),
        (presentation_set_duration, 0),
      (try_end),
    ]),

(ti_on_presentation_mouse_enter_leave,[

      (store_trigger_param_1, reg3),
      (store_trigger_param_2, reg4),
      (store_trigger_param_1, ":id"),
      (store_trigger_param_2, ":stage"),

      (try_begin),

        (eq, ":id", "$g_option_france"),
        (eq, ":stage", 0),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 350),
        
        (overlay_animate_to_size, "$g_option_england", 250, pos1),
        (overlay_animate_to_size, "$g_presentation_obj_item_select_3", 250, pos1),
        (overlay_animate_to_size, "$g_presentation_obj_item_select_5", 250, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        
        (overlay_animate_to_size, ":id", 50, pos1),
       # (overlay_animate_to_alpha, ":id", 150, 0x7D),
        (overlay_animate_to_alpha, "$g_option_france_text", 150, 0xFF),
    (else_try),
        
        (eq, ":id", "$g_option_france"),
        (eq, ":stage", 1),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 450),
        
        (overlay_animate_to_size, ":id", 50, pos1),
       #(overlay_animate_to_alpha, ":id", 150, 0x0),
        (overlay_animate_to_alpha, "$g_option_france_text", 150, 0x7D),
    (else_try),

      (eq, ":id", "$g_option_england"),
      (eq, ":stage", 0),
      (position_set_x, pos1, 350),
      (position_set_y, pos1, 350),

      (overlay_animate_to_size, "$g_option_france", 250, pos1),
      (overlay_animate_to_size, "$g_presentation_obj_item_select_3", 250, pos1),
      (overlay_animate_to_size, "$g_presentation_obj_item_select_5", 250, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 500),
        
      (overlay_animate_to_size, ":id", 50, pos1),
     # (overlay_animate_to_alpha, ":id", 150, 0x7D),
      (overlay_animate_to_alpha, "$g_option_england_text", 150, 0xFF),
    (else_try),

        (eq, ":id", "$g_option_england"),
        (eq, ":stage", 1),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 450),
        (overlay_animate_to_size, ":id", 50, pos1),
      # (overlay_animate_to_alpha, ":id", 150, 0x0),
        (overlay_animate_to_alpha, "$g_option_england_text", 150, 0x7D),  
    
    (else_try),

        (eq, ":id", "$g_presentation_obj_item_select_3"),
        (eq, ":stage", 0),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 350),
        
        (overlay_animate_to_size, "$g_option_france", 250, pos1),
        (overlay_animate_to_size, "$g_option_england", 250, pos1),
        (overlay_animate_to_size, "$g_presentation_obj_item_select_5", 250, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
      
        (overlay_animate_to_size, ":id", 50, pos1),
      # (overlay_animate_to_alpha, ":id", 150, 0x7D),
        (overlay_animate_to_alpha, "$g_presentation_obj_item_select_2", 150, 0xFF),
    (else_try),
        (eq, ":id", "$g_presentation_obj_item_select_3"),
        (eq, ":stage", 1),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 450),
        (overlay_animate_to_size, ":id", 50, pos1),
       #(overlay_animate_to_alpha, ":id", 150, 0x0),
        (overlay_animate_to_alpha, "$g_presentation_obj_item_select_2", 150, 0x7D),  

    (else_try),

        (eq, ":id", "$g_presentation_obj_item_select_5"),
        (eq, ":stage", 0),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 350),
        
        (overlay_animate_to_size, "$g_option_france", 250, pos1),
        (overlay_animate_to_size, "$g_option_england", 250, pos1),
        (overlay_animate_to_size, "$g_presentation_obj_item_select_3", 250, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
      
        (overlay_animate_to_size, ":id", 50, pos1),
      # (overlay_animate_to_alpha, ":id", 150, 0x7D),
        (overlay_animate_to_alpha, "$g_presentation_obj_item_select_4", 150, 0xFF),
    (else_try),
        (eq, ":id", "$g_presentation_obj_item_select_5"),
        (eq, ":stage", 1),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 450),
        (overlay_animate_to_size, ":id", 50, pos1),
       #(overlay_animate_to_alpha, ":id", 150, 0x0),
        (overlay_animate_to_alpha, "$g_presentation_obj_item_select_4", 150, 0x7D),  
    (try_end),

    ]),

  ]
),

]