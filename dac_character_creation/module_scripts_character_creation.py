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

character_creation_scripts = [

# DAC-Kham: Character Creation Scripts

("start_as_noble", [
        
        (try_begin),
          (eq,"$character_gender",tf_male),
          (troop_raise_attribute, "trp_player",ca_intelligence,1),
          (troop_raise_attribute, "trp_player",ca_charisma,2),
          (troop_raise_attribute, "trp_player",ca_strength,1),
          (troop_raise_attribute, "trp_player",ca_agility,1),
		  
          (troop_raise_skill, "trp_player",skl_weapon_master,2),
          (troop_raise_skill, "trp_player",skl_power_strike,2),
          (troop_raise_skill, "trp_player",skl_riding,2),
          (troop_raise_skill, "trp_player",skl_tactics,1),
          (troop_raise_skill, "trp_player",skl_leadership,2),	  
		  
          (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,40),
          (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,40),
          (troop_raise_proficiency, "trp_player",wpt_polearm,40),
          (troop_raise_proficiency, "trp_player",wpt_archery,10),
          (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
          (troop_raise_proficiency, "trp_player",wpt_throwing,10),		  
		  
          (troop_set_slot, "trp_player", slot_troop_renown, 100),
          (call_script, "script_change_player_honor", 3),
          (troop_add_gold, "trp_player", 300),
		  
          (troop_add_item, "trp_player","itm_smoked_fish",0),
          (troop_add_item, "trp_player","itm_heraldic_mail_tabard",0),
          (troop_add_item, "trp_player","itm_b_mail_chausses",0),
          (troop_add_item, "trp_player","itm_h_bascinet_fi_hood_custom",0),
          (troop_add_item, "trp_player","itm_heraldic_banner",0),
          # (troop_add_item, "trp_player","itm_w_native_spear_b",0),
          (troop_add_item, "trp_player","itm_w_onehanded_sword_knight_2",0),
          (troop_add_item, "trp_player","itm_g_mail_gauntlets",0),
          (troop_add_item, "trp_player","itm_ho_rouncey_1",0),
		  
        (else_try),
		
          (troop_raise_attribute, "trp_player",ca_intelligence,2),
          (troop_raise_attribute, "trp_player",ca_charisma,1),
          (troop_raise_attribute, "trp_player",ca_intelligence,1),
          (troop_raise_attribute, "trp_player",ca_charisma,1),
		  
          (troop_raise_skill, "trp_player",skl_wound_treatment,1),
          (troop_raise_skill, "trp_player",skl_riding,2),
          (troop_raise_skill, "trp_player",skl_first_aid,1),
          (troop_raise_skill, "trp_player",skl_leadership,1),
          (troop_raise_skill, "trp_player",skl_persuasion,2),
          (troop_raise_skill, "trp_player",skl_wound_treatment,1),		  
		  
          (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
          (troop_raise_proficiency, "trp_player",wpt_crossbow,15),		  
		  
          (troop_set_slot, "trp_player", slot_troop_renown, 50),
          (troop_add_gold, "trp_player", 300),		  
		  
          (troop_add_item, "trp_player","itm_heraldic_mail_tabard",0),
          (troop_add_item, "trp_player","itm_b_mail_chausses",0),
          (troop_add_item, "trp_player","itm_h_bascinet_fi_hood_custom",0),
          (troop_add_item, "trp_player","itm_tab_shield_kite_c",0),
          (troop_add_item, "trp_player","itm_w_native_spear_b",0),
          (troop_add_item, "trp_player","itm_w_onehanded_sword_knight_2",0),
          (troop_add_item, "trp_player","itm_g_mail_gauntlets",0),
          (troop_add_item, "trp_player","itm_ho_rouncey_1",0),
          (troop_add_item, "trp_player","itm_smoked_fish",0),
        (try_end),

        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
		
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
		
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
		
        (call_script,"script_change_troop_renown", "trp_player", 15),
        (val_add, "$player_right_to_rule", 1),

  ]),

("start_as_merchant", [
        
        (troop_raise_attribute, "trp_player",ca_intelligence,4),
        (troop_raise_attribute, "trp_player",ca_charisma,3),
		
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,3),
        (troop_raise_skill, "trp_player",skl_inventory_management,3),
        (troop_raise_skill, "trp_player",skl_pathfinding,1),		
		
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
		
        (troop_add_gold, "trp_player", 250),
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
		
        (troop_add_item, "trp_player","itm_linen",0),
        (troop_add_item, "trp_player","itm_pottery",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        (troop_add_item, "trp_player","itm_ho_sumpter_1",0),
        (troop_add_item, "trp_player","itm_h_highlander_beret_red_2",0),
        (troop_add_item, "trp_player","itm_a_merchant_outfit",0),
        (troop_add_item, "trp_player","itm_b_leather_boots",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_dagger_italian",0),

  ]),

("start_as_warrior", [
        
        (troop_raise_attribute, "trp_player",ca_strength,3),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
		
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_trainer",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),		
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_shield",1),		
		
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,35),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,25),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),		
		
        (troop_add_gold, "trp_player", 200),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),

        (store_random_in_range, ":food_item", "itm_dried_meat", "itm_grain"),
        (troop_add_item, "trp_player",":food_item"),
        (troop_add_item, "trp_player","itm_w_mace_winged"),
        (troop_add_item, "trp_player","itm_tab_shield_heater_c"),
        (troop_add_item, "trp_player","itm_h_cerveliere_hood_custom"),
        (troop_add_item, "trp_player","itm_a_aketon_narf_custom"),
        (troop_add_item, "trp_player","itm_b_leather_boots"),

        # (display_message, "@Start as Warrior"),
  ]),

("start_as_hunter", [
		
        (troop_raise_attribute, "trp_player",ca_strength,3),
        (troop_raise_attribute, "trp_player",ca_agility,4),		
		
        (troop_raise_skill, "trp_player",skl_power_draw,2),
        (troop_raise_skill, "trp_player",skl_tracking,2),
        (troop_raise_skill, "trp_player",skl_pathfinding,1),
        (troop_raise_skill, "trp_player",skl_spotting,2),
        (troop_raise_skill, "trp_player",skl_athletics,2),
        (troop_raise_skill, "trp_player",skl_horse_archery,1),
        (troop_raise_skill, "trp_player",skl_power_throw,1),				
		
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_archery,60),	
        (troop_raise_proficiency, "trp_player",wpt_polearm,15),	
		
        (call_script,"script_change_troop_renown", "trp_player", 5),
        (troop_add_gold, "trp_player", 100),

        (store_random_in_range, ":food_item", "itm_cattle_meat", "itm_siege_supply"),
        (troop_add_item, "trp_player",":food_item"),		
        (troop_add_item, "trp_player","itm_w_archers_maul"),
        (troop_add_item, "trp_player","itm_w_arrow_broadhead"),
        (troop_add_item, "trp_player","itm_w_hunting_bow_yew"),
        (troop_add_item, "trp_player","itm_h_hood_black"),
        (troop_add_item, "trp_player","itm_a_hunter_coat_custom"),
        (troop_add_item, "trp_player","itm_b_wrapping_boots"),		
		
        # (party_add_members,"p_main_party","trp_french_peasant", 8),
        # (party_add_members,"p_main_party","trp_french_peasant_archer", 5),	
  ]),

("start_as_merc", [
        
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,4),
        (troop_raise_attribute, "trp_player",ca_charisma,3),	
		
        (troop_raise_skill, "trp_player",skl_weapon_master,3),
        (troop_raise_skill, "trp_player",skl_shield,2),
        (troop_raise_skill, "trp_player",skl_ironflesh,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trainer,1),
        (troop_raise_skill, "trp_player",skl_persuasion,1),		
		
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,35),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,40),		
        (try_for_range, ":unused", 0, 4),
          (store_random_in_range, ":wpt", wpt_one_handed_weapon, wpt_firearm),
          (troop_raise_proficiency, "trp_player",":wpt",5), 
        (try_end),		
		
        (troop_add_gold, "trp_player", 200),
        (troop_set_slot, "trp_player", slot_troop_renown, 30),

        (store_random_in_range, ":food_item", "itm_cattle_meat", "itm_siege_supply"),
        (troop_add_item, "trp_player",":food_item"),
        (troop_add_item, "trp_player","itm_w_dagger_pikeman"),
        (troop_add_item, "trp_player","itm_w_awlpike_1"),
        (troop_add_item, "trp_player","itm_h_cerveliere_hood_custom"),
        (troop_add_item, "trp_player","itm_a_padded_armor_custom"),
        (troop_add_item, "trp_player","itm_b_leather_boots"),
        (troop_add_item, "trp_player","itm_s_steel_buckler"),		
		
        # (party_add_members,"p_main_party","trp_mercenary_german_dismounted_knight", 1),
        # (party_add_members,"p_main_party","trp_flemish_militia_crossbowman", 3),
        # (party_add_members,"p_main_party","trp_mercenary_archer", 2),
        # (party_add_members,"p_main_party","trp_mercenary_pavise_spearman", 4),
        # (party_add_members,"p_main_party","trp_mercenary_maceman", 2),
        # (party_add_members,"p_main_party","trp_flemish_militia_pikeman", 3),

  ]),

("start_as_healer", [
        
        (troop_raise_attribute, "trp_player",ca_intelligence,5),
        (troop_raise_attribute, "trp_player",ca_charisma,2), 
    
        (troop_raise_skill, "trp_player",skl_wound_treatment,3),
        (troop_raise_skill, "trp_player",skl_surgery,3),
        (troop_raise_skill, "trp_player",skl_first_aid,3),
        (troop_raise_skill, "trp_player",skl_inventory_management,2),
        (troop_raise_skill, "trp_player",skl_persuasion,1),   
    
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,25),   
        (try_for_range, ":unused", 0, 4),
          (store_random_in_range, ":wpt", wpt_one_handed_weapon, wpt_firearm),
          (troop_raise_proficiency, "trp_player",":wpt",5), 
        (try_end),    
    
        (troop_add_gold, "trp_player", 200),
        (troop_set_slot, "trp_player", slot_troop_renown, 30),

        (store_random_in_range, ":food_item", "itm_cattle_meat", "itm_siege_supply"),
        (troop_add_item, "trp_player",":food_item"),
        (troop_add_item, "trp_player","itm_h_highlander_beret_red_2",0),
        (troop_add_item, "trp_player","itm_a_merchant_outfit",0),
        (troop_add_item, "trp_player","itm_b_leather_boots",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_dagger_italian",0),
  ]),

# KAOS Start as Ruler / Lord / Vassal Begin

("kaos_start_as_vassal", [
    (set_show_messages, 0),

    (store_script_param, ":faction", 1),
    (faction_get_slot, ":liege", ":faction", slot_faction_leader),

    (call_script, "script_player_join_faction", ":faction"),

    (assign, "$player_has_homage" ,1),
    (assign, "$g_player_banner_granted", 1),
    (assign, "$g_invite_faction", 1),
    (assign, "$g_invite_faction_lord", 1),

    (call_script, "script_get_poorest_village_of_faction", ":faction"),
    (assign, ":center", reg0),
    (call_script, "script_give_center_to_lord", ":center", "trp_player", 0),
    (assign, "$g_invite_offered_center", ":center"),
    (party_set_flags, ":center", pf_always_visible, 1),
    (party_set_note_available, ":center", 1),

    (party_relocate_near_party, "p_main_party", ":center", 3),

    (call_script, "script_troop_change_relation_with_troop", "trp_player", ":liege", 10),

    (call_script, "script_change_player_right_to_rule", 15),

    (store_random_in_range,":new_controversy",20, 45),
    (troop_set_slot, "trp_player", slot_troop_controversy, ":new_controversy"), 

    #(troop_get_slot, ":troop_party", "trp_player", slot_troop_leaded_party),
    #(str_store_troop_name, s5, "trp_player"),
    #(party_set_name, ":troop_party", "str_s5_s_party"),

    (troop_set_slot, "trp_player", slot_troop_renown, 200),

    (call_script, "script_update_all_notes"), 

    #(troop_raise_attribute, "trp_player", ca_strength, 18 - 4),
    (troop_raise_attribute, "trp_player", ca_strength, 25 - 4),
    (troop_raise_attribute, "trp_player", ca_agility, 12 - 4),
    (troop_raise_attribute, "trp_player", ca_intelligence, 5 - 4),
    (troop_raise_attribute, "trp_player", ca_charisma, 10 - 4),

    (troop_raise_skill, "trp_player", "skl_tactics", 2),
    (troop_raise_skill, "trp_player", "skl_prisoner_management", 1),
    (troop_raise_skill, "trp_player", "skl_leadership", 4),
    (troop_raise_skill, "trp_player", "skl_trainer", 2),
    (troop_raise_skill, "trp_player", "skl_athletics", 2),
    (troop_raise_skill, "trp_player", "skl_ironflesh", 3),
    (troop_raise_skill, "trp_player", "skl_power_strike", 3),
    (troop_raise_skill, "trp_player", "skl_weapon_master", 4),
    (troop_raise_skill, "trp_player", "skl_riding", 5),
    (troop_raise_skill, "trp_player", "skl_shield", 3),

    (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_archery, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 150 - 15),

    (assign, "$player_honor", 5),

    (call_script, "script_dac_equip_player_as_vassal", ":faction"),

    (faction_get_slot, ":party_template_a", ":faction", slot_faction_reinforcements_a),
    (faction_get_slot, ":party_template_b", ":faction", slot_faction_reinforcements_b),

    (party_add_template, "p_main_party", ":party_template_a"),
    (party_add_template, "p_main_party", ":party_template_b"),
    

    (troop_add_gold, "trp_player", 15000),

    (set_show_messages, 1),
  ]),

 ("kaos_start_as_king_or_lord", [
    (set_show_messages, 0),

    (store_script_param, ":troop", 1),
    (store_faction_of_troop, ":faction", ":troop"),

    (assign, "$player_has_homage" ,1),
    (assign, "$g_player_banner_granted", 1),
    (assign, "$g_invite_faction", 1),
    (assign, "$g_invite_faction_lord", 1),


    (assign, ":capital", -1),
    (try_for_range, ":settlement", towns_begin, villages_end),
        (party_slot_eq, ":settlement", slot_town_lord, ":troop"),
        (party_set_slot, ":settlement", slot_town_lord, "trp_player"),
        (party_set_flags, ":settlement", pf_always_visible, 1),
        (try_begin),
          (ge, ":settlement", villages_begin),
          (party_set_note_available, ":settlement", 1),
        (try_end),
        (eq, ":capital", -1),
        (assign, ":capital", ":settlement"),
    (try_end),

    (party_relocate_near_party, "p_main_party", ":capital", 3),

    (troop_set_slot, "trp_player", slot_troop_leaded_party, 1),

    (assign, "$g_invite_offered_center", ":capital"),

    (str_store_troop_name, s10, ":troop"),
    (troop_set_name, "trp_player", s10),
    (troop_set_plural_name, "trp_player", s10),

    (troop_get_type, ":type", ":troop"),
    (try_begin),
      (eq, ":type", tf_female),
      (troop_set_type, "trp_player", tf_female),
    (try_end),

    (troop_get_slot, ":troop_party", ":troop", slot_troop_leaded_party),
    (try_begin),
        (neq, ":troop_party", 0),
        (remove_party, ":troop_party"),
    (try_end),
    (troop_set_slot, ":troop", slot_troop_leaded_party, -1),
    (troop_set_slot, ":troop", slot_troop_occupation, slto_inactive),
    (troop_set_slot, ":troop", slot_troop_cur_center, -1),
    (troop_set_slot, ":troop", slot_troop_home, -1),
    (troop_set_note_available, ":troop", 0),

    (troop_get_slot, ":reworn", ":troop", slot_troop_renown),
    (troop_set_slot, "trp_player", slot_troop_renown, ":reworn"),

    (troop_get_slot, ":spouse", ":troop", slot_troop_spouse),
    (troop_get_slot, ":father", ":troop", slot_troop_father),
    (troop_get_slot, ":mother", ":troop", slot_troop_mother),
    (troop_get_slot, ":betrothed", ":troop", slot_troop_betrothed),
    (troop_set_slot, "trp_player", slot_troop_spouse, ":spouse"),
    (troop_set_slot, "trp_player", slot_troop_father, ":father"),
    (troop_set_slot, "trp_player", slot_troop_mother, ":mother"),
    (troop_set_slot, "trp_player", slot_troop_betrothed, ":betrothed"),

    (try_begin),
      (gt, ":spouse", 0),
      (troop_set_slot, ":spouse", slot_troop_spouse, "trp_player"),
      (is_between, ":capital", walled_centers_begin, walled_centers_end),
      (troop_set_slot, ":spouse", slot_troop_cur_center, ":capital"),
    (try_end),

    (troop_set_slot, ":troop", slot_troop_spouse, -1),
    (troop_set_slot, ":troop", slot_troop_father, -1),
    (troop_set_slot, ":troop", slot_troop_mother, -1),
    (troop_set_slot, ":troop", slot_troop_betrothed, -1),

    (troop_get_slot, ":banner", ":troop", slot_troop_banner_scene_prop),
    (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":banner"),
    (store_sub, ":offset", ":banner", banner_scene_props_begin),
    (store_add, ":banner_map_icon", banner_map_icons_begin, ":offset"),
    (party_set_banner_icon, "p_main_party", ":banner_map_icon"),

    (str_store_troop_face_keys, s57, ":troop", 0),
    (str_store_troop_face_keys, s58, ":troop", 1),
    (troop_set_face_keys, "trp_player", s57, 0),
    (troop_set_face_keys, "trp_player", s58, 1),

    (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_archery, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 150 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 150 - 15),

    (try_begin),
        (is_between, ":troop", kings_begin, kings_end),

        #(troop_raise_attribute, "trp_player", ca_strength, 18 - 4),
        (troop_raise_attribute, "trp_player", ca_strength, 25 - 4),
        (troop_raise_attribute, "trp_player", ca_agility, 15 - 4),
        (troop_raise_attribute, "trp_player", ca_intelligence, 12 - 4),
        (troop_raise_attribute, "trp_player", ca_charisma, 15 - 4),

        (troop_raise_skill, "trp_player", "skl_tactics", 5),
        (troop_raise_skill, "trp_player", "skl_prisoner_management", 1),
        (troop_raise_skill, "trp_player", "skl_leadership", 9),
        (troop_raise_skill, "trp_player", "skl_trainer", 2),
        (troop_raise_skill, "trp_player", "skl_athletics", 4),
        (troop_raise_skill, "trp_player", "skl_ironflesh", 3),
        (troop_raise_skill, "trp_player", "skl_power_strike", 3),
        (troop_raise_skill, "trp_player", "skl_weapon_master", 4),
        (troop_raise_skill, "trp_player", "skl_riding", 5),
        (troop_raise_skill, "trp_player", "skl_shield", 3),

        (assign, "$kaos_kit_used", 1),
        (call_script, "script_activate_player_faction", "trp_player"),
        (assign, "$kaos_kit_used", 0),
        (assign, "$g_player_minister", "trp_temporary_minister"),
        (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),

        (troop_set_slot, "trp_player", slot_troop_cur_center, ":capital"),
        (troop_set_slot, "trp_player", slot_troop_home, ":capital"),
        (assign, "$g_player_court", ":capital"),

        (assign, "$players_kingdom", "fac_player_supporters_faction"),

        #save info about villages:
        (try_for_range, ":village", villages_begin, villages_end),
            (store_faction_of_party, ":f", ":village"),
            (eq, ":f", ":faction"),
            (party_get_slot, ":owner", ":village", slot_town_lord),
            (troop_set_slot, "trp_temp_array_a", ":village", ":owner"),
        (try_end),

        ##knights/npc lords Transferring to the players kingdom
        (try_for_range, ":lord", lords_begin, lords_end), 
            (troop_set_note_available, ":lord", 1),   
            (store_faction_of_troop, ":lord_faction", ":lord"),
            (str_store_troop_name, s1, ":lord"),
            (eq, ":lord_faction", ":faction"),
            (call_script, "script_change_troop_faction", ":lord", "fac_player_supporters_faction"),
            (troop_set_slot, ":lord", slot_troop_occupation, slto_kingdom_hero),    
            (store_random_in_range, ":new_relation", -5, 35),
            (call_script, "script_troop_change_relation_with_troop", "trp_player", ":lord", ":new_relation"),
        (try_end),  
    
        (try_for_range, ":npc_lady", kingdom_ladies_begin, kingdom_ladies_end),   
            (store_faction_of_troop, ":lady_faction", ":npc_lady"),
            (eq, ":lady_faction", ":faction"),
            (call_script, "script_change_troop_faction", ":npc_lady", "fac_player_supporters_faction"),
        (try_end),  

        #restore info about villages:
        (try_for_range, ":village", villages_begin, villages_end),
            (store_faction_of_party, ":f", ":village"),
            (eq, ":f", "fac_player_supporters_faction"),
            (troop_get_slot, ":owner", "trp_temp_array_a", ":village"),
            (party_set_slot, ":village", slot_town_lord, ":owner"),
        (try_end),

        #Kings can see all the villages of their kingdoms at game start
        (try_for_range, ":village", villages_begin, villages_end),
            (store_faction_of_party, ":f", ":village"),
            (eq, ":f", "fac_player_supporters_faction"),
            (party_set_flags, ":village", pf_always_visible, 1),
            (party_set_note_available, ":village", 1),
        (try_end),

        (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
        (faction_set_note_available, "fac_player_supporters_faction", 1),
        (call_script, "script_update_faction_notes","fac_player_supporters_faction"),
        (call_script, "script_change_player_right_to_rule", 25),

        (assign, "$players_kingdom_name_set", 1),
        (faction_set_slot, ":faction", slot_faction_state, sfs_inactive), 

        (str_store_faction_name, s1, ":faction"),
        (faction_set_name, "fac_player_supporters_faction", s1),
        (faction_get_color, ":color", ":faction"),
        (faction_set_color, "fac_player_supporters_faction", ":color"),

        (troop_set_slot, "trp_player", slot_troop_cur_center, ":capital"),
        (troop_set_slot, "trp_player", slot_troop_home, ":capital"),
        (assign, "$g_player_court", ":capital"),

        (faction_get_slot, ":t1", ":faction", slot_faction_tier_1_troop),
        (faction_get_slot, ":t2", ":faction", slot_faction_tier_2_troop),
        (faction_get_slot, ":t3", ":faction", slot_faction_tier_3_troop),
        (faction_get_slot, ":t4", ":faction", slot_faction_tier_4_troop),
        (faction_get_slot, ":t5", ":faction", slot_faction_tier_5_troop),
        (faction_get_slot, ":t6", ":faction", slot_faction_tier_6_troop),
        (faction_get_slot, ":archer", ":faction", slot_faction_tier_1_archer),
        (faction_get_slot, ":adj", ":faction", slot_faction_adjective),

        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_1_troop, ":t1"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_2_troop, ":t2"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_3_troop, ":t3"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_4_troop, ":t4"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_5_troop, ":t5"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_6_troop, ":t6"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_tier_1_archer, ":archer"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_adjective, ":adj"),
        (troop_add_gold, "trp_player", 40000),
    (else_try),
        #(troop_raise_attribute, "trp_player", ca_strength, 18 - 4),
        (troop_raise_attribute, "trp_player", ca_strength, 25 - 4),
        (troop_raise_attribute, "trp_player", ca_agility, 14 - 4),
        (troop_raise_attribute, "trp_player", ca_intelligence, 10 - 4),
        (troop_raise_attribute, "trp_player", ca_charisma, 10 - 4),

        (troop_raise_skill, "trp_player", "skl_tactics", 3),
        (troop_raise_skill, "trp_player", "skl_prisoner_management", 1),
        (troop_raise_skill, "trp_player", "skl_leadership", 6),
        (troop_raise_skill, "trp_player", "skl_trainer", 2),
        (troop_raise_skill, "trp_player", "skl_athletics", 4),
        (troop_raise_skill, "trp_player", "skl_ironflesh", 3),
        (troop_raise_skill, "trp_player", "skl_power_strike", 3),
        (troop_raise_skill, "trp_player", "skl_weapon_master", 4),
        (troop_raise_skill, "trp_player", "skl_riding", 5),
        (troop_raise_skill, "trp_player", "skl_shield", 3),

        (call_script, "script_player_join_faction", ":faction"),

        (faction_get_slot, ":liege", ":faction", slot_faction_leader),
        (call_script, "script_troop_change_relation_with_troop", "trp_player", ":liege", 10),
        (call_script, "script_change_player_right_to_rule", 15),
        (store_random_in_range,":new_controversy", 20, 45),
        (troop_set_slot, "trp_player", slot_troop_controversy, ":new_controversy"), 

        (is_between, ":capital", centers_begin, centers_end),
        (troop_set_slot, "trp_player", slot_troop_cur_center, ":capital"),
        (troop_set_slot, "trp_player", slot_troop_home, ":capital"),
        (assign, "$g_player_court", ":capital"),

        (troop_add_gold, "trp_player", 30000),
    (try_end),

    (call_script, "script_update_all_notes"), 
    #(troop_get_slot, ":wealth", ":troop", slot_troop_wealth),
    #(troop_add_gold, "trp_player", ":wealth"),

    (call_script, "script_dac_equip_player_as_lord", ":troop"),

    (faction_get_slot, ":party_template_a", ":faction", slot_faction_reinforcements_a),
    (faction_get_slot, ":party_template_b", ":faction", slot_faction_reinforcements_b),
    (faction_get_slot, ":party_template_c", ":faction", slot_faction_reinforcements_c),
    (faction_get_slot, ":party_template_d", ":faction", slot_faction_reinforcements_d),   
    (faction_get_slot, ":party_template_e", ":faction", slot_faction_reinforcements_e),   

    (party_add_template, "p_main_party", ":party_template_a"),
    (party_add_template, "p_main_party", ":party_template_b"),
    (party_add_template, "p_main_party", ":party_template_c"),
    (party_add_template, "p_main_party", ":party_template_d"),
    (party_add_template, "p_main_party", ":party_template_e"),
    
    (call_script, "script_change_troop_faction", ":troop", "fac_outlaws"),

    (assign, "$player_honor", 5),

    (set_show_messages, 1),
  ]),


("dac_equip_player_as_vassal", [
    (store_script_param_1, ":faction_no"),

    (try_begin), 
       (eq, ":faction_no", "fac_kingdom_1"), #DAC Kham: Copied from knight_1_51
       (troop_add_item, "trp_player", "itm_w_bastard_sword_mercenary_2"),
       (troop_add_item, "trp_player", "itm_w_lance_colored_french_2_heraldic"),
       (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b"),
       (troop_add_item, "trp_player", "itm_ho_horse_barded_blue_chamfrom"),
       (troop_add_item, "trp_player", "itm_h_zitta_bascinet_novisor"),
       (troop_add_item, "trp_player", "itm_heraldic_early_transitional"),
       (troop_add_item, "trp_player", "itm_b_splinted_greaves_spurs"),
       (troop_add_item, "trp_player", "itm_g_wisby_gauntlets_black"),
       (troop_add_item, "trp_player", "itm_b_hosen_shoes_custom"),
    (else_try),
       (eq, ":faction_no", "fac_kingdom_2"), #DAC Kham: Copied from knight_2_51
       (troop_add_item, "trp_player", "itm_w_bastard_sword_duke_2"),
       (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b"),
       (troop_add_item, "trp_player", "itm_w_lance_colored_english_3_heraldic"),
       (troop_add_item, "trp_player", "itm_ho_horse_barded_red_chamfrom"),
       (troop_add_item, "trp_player", "itm_h_hounskull_narf"),
       (troop_add_item, "trp_player", "itm_heraldic_brigandine_native"),
       (troop_add_item, "trp_player", "itm_b_shynbaulds"),
       (troop_add_item, "trp_player", "itm_g_hourglass_gauntlets"),
       (troop_add_item, "trp_player", "itm_b_hosen_shoes_custom"),
    (else_try),
       (eq, ":faction_no", "fac_kingdom_3"), #DAC Kham: Copied from knight_3_20
       (troop_add_item, "trp_player", "itm_w_bastard_sword_regent"),
       (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b"),
       (troop_add_item, "trp_player", "itm_w_lance_4_heraldic"),
       (troop_add_item, "trp_player", "itm_ho_horse_barded_brown_chamfrom"),
       (troop_add_item, "trp_player", "itm_h_zitta_bascinet_novisor"),
       (troop_add_item, "trp_player", "itm_heraldic_early_transitional"),
       (troop_add_item, "trp_player", "itm_b_splinted_greaves_spurs"),
       (troop_add_item, "trp_player", "itm_g_wisby_gauntlets_black"),
       (troop_add_item, "trp_player", "itm_b_hosen_shoes_custom"),
    (else_try),
       #(eq, ":faction_no", "fac_kingdom_4"),  #DAC Kham: Copied from knight_4_18
       (troop_add_item, "trp_player", "itm_w_bastard_sword_crecy_2"),
       (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b"),
       (troop_add_item, "trp_player", "itm_w_lance_1_heraldic"),
       (troop_add_item, "trp_player", "itm_ho_horse_barded_black_chamfrom"),
       (troop_add_item, "trp_player", "itm_h_bascinet_great"),
       (troop_add_item, "trp_player", "itm_heraldic_tunic_new"),
       (troop_add_item, "trp_player", "itm_b_steel_greaves"),
       (troop_add_item, "trp_player", "itm_g_demi_gauntlets"),
       (troop_add_item, "trp_player", "itm_b_hosen_shoes_custom"),
    (try_end),
    (troop_equip_items, "trp_player"),
    (troop_add_item, "trp_player", "itm_smoked_fish"),
    (troop_add_item, "trp_player", "itm_cheese"),
    (troop_add_item, "trp_player", "itm_bread"),

  ]),

  ("dac_equip_player_as_lord", [
    #(set_show_messages, 1),
    (store_script_param_1, ":troop_no"),
    (troop_clear_inventory, "trp_player"),
    #(display_message, "@equipping"),
    (try_for_range, ":i_slot", ek_item_0, ek_horse + 1),
        (troop_get_inventory_slot, ":item", ":troop_no", ":i_slot"),
        (troop_get_inventory_slot_modifier, ":imod", ":troop_no", ":i_slot"),
        (troop_add_item, "trp_player", ":item", ":imod"),
        #(assign, reg33, ":item"),
        #(assign, reg34, ":imod"),
        #(display_message, "@equipping item={reg33}, imod={reg34}"),
        #(troop_set_inventory_slot, "trp_player", ":i_slot", ":item"),
        #(troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":imod"),
    (try_end),
    (troop_equip_items, "trp_player"),
    (troop_add_item, "trp_player", "itm_smoked_fish"),
    (troop_add_item, "trp_player", "itm_cheese"),
    (troop_add_item, "trp_player", "itm_bread"),

  ]),

  ("cf_select_lord_lord_in_culture", [
    (store_script_param, ":troop", 1),
    (store_script_param, ":filter", 2),

    (assign, ":res", 0),

    (try_begin),
      (eq, ":filter", 0),
      (assign, ":res", 1),
    (else_try),
      (store_faction_of_troop, ":tf", ":troop"),
      
      (val_sub, ":filter", 1),
      (val_add, ":filter", "fac_kingdom_1"),
      (eq, ":filter", ":tf"),
      (assign, ":res", 1),
    (try_end),

    (eq, ":res", 1),
  ]),

("cf_neg_select_lord_lord_in_culture", [
    (store_script_param, ":troop", 1),
    (store_script_param, ":filter", 2),

    (assign, ":res", 0),

    (try_begin),
      (eq, ":filter", 0),
      (assign, ":res", 1),
    (else_try),
      (store_faction_of_troop, ":tf", ":troop"),
      
      (val_sub, ":filter", 1),
      (val_add, ":filter", "fac_kingdom_1"),

      (eq, ":filter", ":tf"),
      (assign, ":res", 1),
    (try_end),

    (eq, ":res", 0),
  ]),
]