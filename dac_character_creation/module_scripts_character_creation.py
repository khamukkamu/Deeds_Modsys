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
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,4),
        (troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_attribute, "trp_player",ca_agility,2),

        (troop_raise_skill, "trp_player",skl_weapon_master,2),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_tactics,2),
        (troop_raise_skill, "trp_player",skl_leadership,3),	  

        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,50),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,50),
        (troop_raise_proficiency, "trp_player",wpt_polearm,40),
        (troop_raise_proficiency, "trp_player",wpt_archery,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),		  

        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 300),

        (troop_add_item, "trp_player","itm_a_pistoia_mail_a_mail_sleeves_over_plate",0),
        (troop_add_item, "trp_player","itm_b_high_boots_3",0),
        (troop_add_item, "trp_player","itm_h_simple_cervelliere_mail_aventail",0),
        (troop_add_item, "trp_player","itm_s_heraldic_shield_leather",0),
        (troop_add_item, "trp_player","itm_w_native_spear_b",0),
        (troop_add_item, "trp_player","itm_w_onehanded_sword_knight",0),
        (troop_add_item, "trp_player","itm_g_gauntlets_mailed",0),
        (troop_add_item, "trp_player","itm_ho_rouncey_1",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),

    (else_try),

        (troop_raise_attribute, "trp_player",ca_intelligence,3),
        (troop_raise_attribute, "trp_player",ca_charisma,3),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,3),

        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_leadership,2),
        (troop_raise_skill, "trp_player",skl_persuasion,2),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),		  
        (troop_raise_skill, "trp_player",skl_tactics,1),
        
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,40),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,15),		
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),        

        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (troop_add_gold, "trp_player", 300),		  

        (troop_add_item, "trp_player","itm_a_pistoia_mail_b_mail_sleeves_over_plate",0),
        (troop_add_item, "trp_player","itm_b_high_boots_3",0),
        (troop_add_item, "trp_player","itm_h_simple_cervelliere_mail_aventail",0),
        (troop_add_item, "trp_player","itm_s_heraldic_shield_leather",0),
        (troop_add_item, "trp_player","itm_w_native_spear_b_custom",0),
        (troop_add_item, "trp_player","itm_w_onehanded_sword_knight",0),
        (troop_add_item, "trp_player","itm_g_gauntlets_mailed",0),
        (troop_add_item, "trp_player","itm_ho_rouncey_1",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        
    (try_end),

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
    (troop_add_item, "trp_player","itm_b_low_boots_4",0),
    (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
    (troop_add_item, "trp_player","itm_w_dagger_italian",0),

  ]),

("start_as_warrior", [
        
    (troop_raise_attribute, "trp_player",ca_strength,3),
    (troop_raise_attribute, "trp_player",ca_agility,2),
    (troop_raise_attribute, "trp_player",ca_intelligence,2),
    (troop_raise_attribute, "trp_player",ca_charisma,3),
    
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
    (troop_add_item, "trp_player","itm_w_onehanded_sword_a"),
    (troop_add_item, "trp_player","itm_s_heater_shield_french_3"),
    (troop_add_item, "trp_player","itm_h_chapel_de_fer_strap"),
    (troop_add_item, "trp_player","itm_a_gambeson_asher_belt_custom"),
    (troop_add_item, "trp_player","itm_b_turnshoes_2"),

    # (display_message, "@Start as Warrior"),
  ]),

("start_as_hunter", [
		
    (troop_raise_attribute, "trp_player",ca_strength,3),
    (troop_raise_attribute, "trp_player",ca_agility,4),		
    (troop_raise_attribute, "trp_player",ca_intelligence,2),		
    (troop_raise_attribute, "trp_player",ca_charisma,2),		
    
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
    (troop_add_item, "trp_player","itm_h_hood_big_liripipe_full_custom"),
    (troop_add_item, "trp_player","itm_a_hunter_coat_custom"),
    (troop_add_item, "trp_player","itm_b_turnshoes_4"),		
    
    # (party_add_members,"p_main_party","trp_french_peasant", 8),
    # (party_add_members,"p_main_party","trp_french_peasant_archer", 5),	
  ]),

("start_as_merc", [
        
    (troop_raise_attribute, "trp_player",ca_strength,4),
    (troop_raise_attribute, "trp_player",ca_agility,3),
    (troop_raise_attribute, "trp_player",ca_intelligence,2),	
    (troop_raise_attribute, "trp_player",ca_charisma,2),	
    
    (troop_raise_skill, "trp_player",skl_weapon_master,3),
    (troop_raise_skill, "trp_player",skl_shield,2),
    (troop_raise_skill, "trp_player",skl_ironflesh,1),
    (troop_raise_skill, "trp_player",skl_power_strike,1),
    (troop_raise_skill, "trp_player",skl_leadership,1),
    (troop_raise_skill, "trp_player",skl_trainer,1),
    (troop_raise_skill, "trp_player",skl_tactics,1),
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
    (troop_add_item, "trp_player","itm_h_simple_cervelliere_2_strap"),
    (troop_add_item, "trp_player","itm_a_light_gambeson_long_sleeves_custom"),
    (troop_add_item, "trp_player","itm_b_turnshoes_1"),
    (troop_add_item, "trp_player","itm_s_steel_buckler"),	
    
    # (party_add_members,"p_main_party","trp_mercenary_german_dismounted_knight", 1),
    # (party_add_members,"p_main_party","trp_flemish_militia_crossbowman", 3),
    # (party_add_members,"p_main_party","trp_mercenary_archer", 2),
    # (party_add_members,"p_main_party","trp_mercenary_pavise_spearman", 4),
    # (party_add_members,"p_main_party","trp_mercenary_maceman", 2),
    # (party_add_members,"p_main_party","trp_flemish_militia_pikeman", 3),

  ]),

("start_as_healer", [
        
    (troop_raise_attribute, "trp_player",ca_strength,1),
    (troop_raise_attribute, "trp_player",ca_agility,2),
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
    (troop_add_item, "trp_player","itm_b_turnshoes_6",0),
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

    (store_random_in_range,":new_controversy",0, 20),
    (troop_set_slot, "trp_player", slot_troop_controversy, ":new_controversy"), 

    #(troop_get_slot, ":troop_party", "trp_player", slot_troop_leaded_party),
    #(str_store_troop_name, s5, "trp_player"),
    #(party_set_name, ":troop_party", "str_s5_s_party"),

    (troop_set_slot, "trp_player", slot_troop_renown, 200),

    (call_script, "script_update_all_notes"), 

    (troop_raise_attribute, "trp_player",ca_intelligence,2),
    (troop_raise_attribute, "trp_player",ca_charisma,4),
    (troop_raise_attribute, "trp_player",ca_strength,2),
    (troop_raise_attribute, "trp_player",ca_agility,2),

    (get_level_boundary, ":xp_required_for_levelling", 10),
    (add_xp_to_troop, ":xp_required_for_levelling", "trp_player"),

    (troop_raise_skill, "trp_player",skl_weapon_master,3),
    (troop_raise_skill, "trp_player",skl_power_strike,2),
    (troop_raise_skill, "trp_player",skl_riding,2),
    (troop_raise_skill, "trp_player",skl_tactics,2),
    (troop_raise_skill, "trp_player",skl_leadership,3),	  

    (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 100 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 100 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 100 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_archery, 100 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 100 - 15),
    (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 100 - 15),

    (assign, "$player_honor", 5),

    (call_script, "script_dac_equip_player_as_vassal", ":faction"),

    (faction_get_slot, ":party_template_a", ":faction", slot_faction_reinforcements_a),
    (faction_get_slot, ":party_template_b", ":faction", slot_faction_reinforcements_b),

    (party_add_template, "p_main_party", ":party_template_a"),
    (party_add_template, "p_main_party", ":party_template_b"),


    (troop_add_gold, "trp_player", 10000),

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
        
        # DAC Seek: Fix attempt for capital loss bug
        (party_set_faction, ":settlement", "fac_player_supporters_faction"),
        
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

        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,4),
        (troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_attribute, "trp_player",ca_agility,2),

        (get_level_boundary, ":xp_required_for_levelling", 20),
        (add_xp_to_troop, ":xp_required_for_levelling", "trp_player"),        

        (troop_raise_skill, "trp_player",skl_weapon_master,4),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_riding,3),
        (troop_raise_skill, "trp_player",skl_tactics,2),
        (troop_raise_skill, "trp_player",skl_leadership,3),	  


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
        (troop_add_gold, "trp_player", 30000),
        
        ### DAC Seek: attempt to fix the neutral AI siege bug
        (try_begin),
            (eq, ":faction", "fac_kingdom_1"),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", -100),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_3", -20),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", 40),
            (call_script, "script_make_kingdom_hostile_to_player", "fac_kingdom_2", -100),
            (call_script, "script_make_kingdom_hostile_to_player", "fac_kingdom_3", -20),
        (else_try),
            (eq, ":faction", "fac_kingdom_2"),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -100),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_3", 20),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", -20),
            (call_script, "script_make_kingdom_hostile_to_player", "fac_kingdom_1", -100),
            (call_script, "script_make_kingdom_hostile_to_player", "fac_kingdom_4", -20),
        (else_try),
            (eq, ":faction", "fac_kingdom_3"),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -20),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", 20),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", 0),
            (call_script, "script_make_kingdom_hostile_to_player", "fac_kingdom_1", -20),
        (else_try),
            (eq, ":faction", "fac_kingdom_4"),      
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 20),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", -20),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_3", 0),
            (call_script, "script_make_kingdom_hostile_to_player", "fac_kingdom_2", -20),
        (try_end),
        
    (else_try),
    
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,4),
        (troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_attribute, "trp_player",ca_agility,2),

        (get_level_boundary, ":xp_required_for_levelling", 15),
        (add_xp_to_troop, ":xp_required_for_levelling", "trp_player"), 

        (troop_raise_skill, "trp_player",skl_weapon_master,4),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_riding,3),
        (troop_raise_skill, "trp_player",skl_tactics,2),
        (troop_raise_skill, "trp_player",skl_leadership,3),	  

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

        (troop_add_gold, "trp_player", 15000),
        
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
        (troop_add_item, "trp_player", "itm_w_bastard_sword_mercenary"),
        (troop_add_item, "trp_player", "itm_w_lance_colored_french_2_heraldic"),
        (troop_add_item, "trp_player", "itm_s_heraldic_shield_leather"),
        (troop_add_item, "trp_player", "itm_ho_horse_barded_blue_chamfrom"),
        (troop_add_item, "trp_player", "itm_h_great_bascinet_english_1410_visor"),
        (troop_add_item, "trp_player", "itm_a_brigandine_asher_custom"),
        (troop_add_item, "trp_player", "itm_b_leg_harness_3"),
        (troop_add_item, "trp_player", "itm_g_gauntlets_segmented_a"),
        (troop_add_item, "trp_player", "itm_b_turnshoes_1"),
    (else_try),
        (eq, ":faction_no", "fac_kingdom_2"), #DAC Kham: Copied from knight_2_51
        (troop_add_item, "trp_player", "itm_w_bastard_sword_duke"),
        (troop_add_item, "trp_player", "itm_s_heraldic_shield_leather"),
        (troop_add_item, "trp_player", "itm_w_lance_colored_english_3_heraldic"),
        (troop_add_item, "trp_player", "itm_ho_horse_barded_red_chamfrom"),
        (troop_add_item, "trp_player", "itm_h_great_bascinet_english_1410_visor"),
        (troop_add_item, "trp_player", "itm_a_brigandine_asher_custom"),
        (troop_add_item, "trp_player", "itm_b_leg_harness_2"),
        (troop_add_item, "trp_player", "itm_g_gauntlets_segmented_a"),
        (troop_add_item, "trp_player", "itm_b_turnshoes_1"),
    (else_try),
        (eq, ":faction_no", "fac_kingdom_3"), #DAC Kham: Copied from knight_3_20
        (troop_add_item, "trp_player", "itm_w_bastard_sword_regent"),
        (troop_add_item, "trp_player", "itm_s_heraldic_shield_leather"),
        (troop_add_item, "trp_player", "itm_w_lance_4_heraldic"),
        (troop_add_item, "trp_player", "itm_ho_horse_barded_brown_chamfrom"),
        (troop_add_item, "trp_player", "itm_h_great_bascinet_english_1410_visor"),
        (troop_add_item, "trp_player", "itm_a_brigandine_asher_custom"),
        (troop_add_item, "trp_player", "itm_b_leg_harness_2"),
        (troop_add_item, "trp_player", "itm_g_gauntlets_segmented_a"),
        (troop_add_item, "trp_player", "itm_b_turnshoes_1"),
    (else_try),
        #(eq, ":faction_no", "fac_kingdom_4"),  #DAC Kham: Copied from knight_4_18
        (troop_add_item, "trp_player", "itm_w_bastard_sword_crecy"),
        (troop_add_item, "trp_player", "itm_s_heraldic_shield_leather"),
        (troop_add_item, "trp_player", "itm_w_lance_1_heraldic"),
        (troop_add_item, "trp_player", "itm_ho_horse_barded_black_chamfrom"),
        (troop_add_item, "trp_player", "itm_h_great_bascinet_english_1410_visor"),
        (troop_add_item, "trp_player", "itm_a_light_gambeson_long_sleeves_custom"),
        (troop_add_item, "trp_player", "itm_b_leg_harness_10"),
        (troop_add_item, "trp_player", "itm_g_demi_gauntlets"),
        (troop_add_item, "trp_player", "itm_b_turnshoes_1"),
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

#script_dac_get_info_about_lord
  # Copy of game get troop note without triggers and links
  # INPUT: arg1 = troop_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("dac_get_info_about_lord",
    [
  (store_script_param_1, ":troop_no"),
  (store_script_param_2, ":note_index"),

  (str_store_troop_name, s54, ":troop_no"),
    (try_begin),
    (eq, ":troop_no", "trp_player"),
    (this_or_next|eq, "$player_has_homage", 1),
    (eq, "$players_kingdom", "fac_player_supporters_faction"),
    (assign, ":troop_faction", "$players_kingdom"),
  (else_try),
    (store_troop_faction, ":troop_faction", ":troop_no"),
  (try_end),
  
  (str_clear, s49),

  #Family notes
  (try_begin),

    (this_or_next|eq, ":troop_no", "trp_player"),
    (this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),#includes pretenders
    (is_between, ":troop_no", kings_begin, kings_end),

    (assign, ":num_relations", 0),

    (try_begin),
      (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
      (gt, reg0, 0),
      (val_add, ":num_relations", 1),
    (try_end),
##diplomacy start+
#Display relations with kings and claimants
    (try_for_range, ":aristocrat", heroes_begin, heroes_end),
      (this_or_next|is_between, ":aristocrat", lords_begin, kingdom_ladies_end),#includes pretenders
      (is_between, ":aristocrat", kings_begin, kings_end),
##diplomacy end+
      (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
      (gt, reg0, 0),
      (val_add, ":num_relations", 1),
    (try_end),
    
# DAC Seek: Get troop age for lords without families      
    (try_begin),
      (eq, ":num_relations", 0),  
      
      (try_begin),    
        (neq, ":troop_no", "trp_player"),   
        (troop_get_slot, reg1, ":troop_no", slot_troop_age),
        (str_store_string, s49, "str__age_reg1"),       
      (try_end),  
      
    (else_try),
      (gt, ":num_relations", 0),
      
      (try_begin),
        (eq, ":troop_no", "trp_player"),
        (str_store_string, s49, "str__family_"),
      (else_try),
        (troop_get_slot, reg1, ":troop_no", slot_troop_age),
        (str_store_string, s49, "str__age_reg1_family_"),
      (try_end),
      
      (try_begin),
        (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
        (gt, reg0, 0),
        (str_store_troop_name, s12, "trp_player"),
        (val_sub, ":num_relations", 1),
        (try_begin),
          (eq, ":num_relations", 0),
          (str_store_string, s49, "str_s49_s12_s11_end"),
        (else_try),
        (str_store_string, s49, "str_s49_s12_s11"),
      (try_end),      
      
    (try_end),
    
  
      #Display relations with kings and claimants
      (try_for_range, ":aristocrat", heroes_begin, heroes_end),
        (this_or_next|is_between, ":aristocrat", lords_begin, kingdom_ladies_end),#includes pretenders
         (is_between, ":aristocrat", kings_begin, kings_end),
      ##diplomacy end+
            (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
            (gt, reg0, 0),
            (try_begin),
              (neg|is_between, ":aristocrat", kingdom_ladies_begin, kingdom_ladies_end),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s12, ":aristocrat"),
              (call_script, "script_troop_get_relation_with_troop", ":aristocrat", ":troop_no"),
              (str_store_string, s49, "str_s49_s12_s11_rel_reg0"),
            (else_try),
              (str_store_troop_name, s12, ":aristocrat"),
              (val_sub, ":num_relations", 1),
              (try_begin),
                (eq, ":num_relations", 0),
                (str_store_string, s49, "str_s49_s12_s11_end"),
              (else_try),
                (str_store_string, s49, "str_s49_s12_s11"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
      (try_end),

      (try_begin),
        (neq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
        (neg|is_between, ":troop_no", companions_begin, companions_end),
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),

        (try_begin),
          (eq, ":note_index", 0),
          (str_store_string, s0, "str_s54_has_left_the_realm"),
          ##diplomacy start+
          #Check for "deceased" instead
          (try_begin),
             (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
             (str_store_string, s0, "str_s54_is_deceased"),
          (try_end),
          ##diplomacy end+
        (else_try),
          (str_clear, s0),
          (this_or_next|eq, ":note_index", 1),
          (eq, ":note_index", 2),
        (try_end),

      (else_try),
        (is_between, ":troop_no", companions_begin, companions_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (eq, ":note_index", 0),
        (str_clear, s0),
        (assign, ":companion", ":troop_no"),
        (str_store_troop_name, s4, ":companion"),
        (try_begin),
      # (troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),

      (this_or_next|main_party_has_troop, ":companion"),
      (this_or_next|troop_slot_ge, ":companion", slot_troop_current_mission, 1),
        (eq, "$g_player_minister", ":companion"),
            #SB : replace the call
            (call_script, "script_companion_get_mission_string", ":companion"),

    ##diplomacy start+
    #Check for explicit "exiled" and "dead" settings
    (else_try),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
      (str_store_string, s0, "str_s54_is_deceased"),
    (else_try),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
      (str_store_string, s0, "str_s54_has_left_the_realm"),
    ##diplomacy end+
    (else_try),
      (str_store_string, s0, "str_whereabouts_unknown"),
    (try_end),


      (else_try),
        (is_between, ":troop_no", pretenders_begin, pretenders_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, ":troop_no", "$supported_pretender"),


        (troop_get_slot, ":orig_faction", ":troop_no", slot_troop_original_faction),
        (try_begin),
          (faction_slot_eq, ":orig_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":orig_faction", slot_faction_has_rebellion_chance, 1),
          (try_begin),
            (eq, ":note_index", 0),
            (str_store_faction_name, s56, ":orig_faction"),
            (str_store_string, s0, "@{s54} is a claimant to the throne of {s56}."),
            ##diplomacy end+
          (try_end),
        (else_try),
          (try_begin),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
          (try_end),
        (try_end),

      (else_try),
        (try_begin),
          (eq, ":note_index", 0),
          (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
          (str_store_troop_name, s55, ":faction_leader"),
          (str_store_faction_name, s56, ":troop_faction"),
          (assign, ":troop_is_player_faction", 0),
          (assign, ":troop_is_faction_leader", 0),
          (try_begin),
            (eq, ":troop_faction", "fac_player_faction"),
            (assign, ":troop_is_player_faction", 1),
          (else_try),
            (eq, ":faction_leader", ":troop_no"),
            (assign, ":troop_is_faction_leader", 1),
          (try_end),
          #SB: add marshal check
          (try_begin),
            (faction_slot_eq, ":troop_faction", slot_faction_marshall, ":troop_no"),
            (assign, ":troop_is_marshal", 1),
          (else_try),
            (assign, ":troop_is_marshal", 0),
          (try_end),
          (assign, ":num_centers", 0),
          (str_store_string, s58, "@nowhere"),
          (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
            (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
            (try_begin),
              (eq, ":num_centers", 0),
              (str_store_party_name, s58, ":cur_center"),
            (else_try),
              (eq, ":num_centers", 1),
              (str_store_party_name, s57, ":cur_center"),
              (str_store_string, s58, "@{s57} and {s58}"),
            (else_try),
              (str_store_party_name, s57, ":cur_center"),
              (str_store_string, s58, "@{!}{s57}, {s58}"),
            (try_end),
            (val_add, ":num_centers", 1),
          (try_end),
          ##diplomacy start+ use script for gender
          #(troop_get_type, reg3, ":troop_no"),
          (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 3),
          #(assign, reg3, reg0),
          ##diplomacy end+


          (str_clear, s59),
          (try_begin),
            (call_script, "script_troop_get_player_relation", ":troop_no"),
            (assign, ":relation", reg0),
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            (store_add, ":str_id", "str_relation_mnus_100_ns",  ":str_offset"),
            (neq, ":str_id", "str_relation_plus_0_ns"),
            (str_store_string, s60, "@{reg3?She:He}"),
            (str_store_string, s59, ":str_id"),
            (str_store_string, s59, "@{!}^{s59}"),
          (try_end),
          #lord recruitment changes begin
          #This sends a bunch of political information to s47.

          #refresh registers
          (assign, reg9, ":num_centers"),
          ##diplomacy start+ use script for gender
          (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 3),
          ##diplomacy end+

          #SB : rearrange registers a bit
          (assign, reg4, ":troop_is_faction_leader"),
          (assign, reg5, ":troop_is_marshal"),
          (assign, reg6, ":troop_is_player_faction"),

          #SB : TODO, add rounding based on personal relation/time last met?
          (troop_get_slot, reg15, ":troop_no", slot_troop_renown),
          (troop_get_slot, reg16, ":troop_no", slot_troop_controversy),
          #SB : actually use this wealth in string
          (troop_get_slot, reg17, ":troop_no", slot_troop_wealth), #DEBUGS
          ##diplomacy start+ xxx remove third argument (was it doing anything?)
          #(str_store_string, s0, "str_lord_info_string", 0),
          (str_store_string, s0, "str_lord_info_string"),
          ##diplomacy end+
          #lord recruitment changes end
          (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
        (try_end),
      (try_end),
     ]),
     
  #script_add_troop_to_cur_tableau_for_retirement
  # INPUT: type
  # OUTPUT: none
  ("dac_add_troop_to_cur_tableau_with_animation", [
    (store_script_param, ":animation", 1),

    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
    (assign, ":cam_height", 155),
    (assign, ":camera_distance", 575),
    (assign, ":camera_yaw", -5),
    (assign, ":camera_pitch", 10),

    (init_position, pos5),
    (position_set_z, pos5, ":cam_height"),
    # camera looks towards -z axis
    (position_rotate_x, pos5, -90),
    (position_rotate_z, pos5, 180),
    # now apply yaw and pitch
    (position_rotate_y, pos5, ":camera_yaw"),
    (position_rotate_x, pos5, ":camera_pitch"),
    (position_move_z, pos5, ":camera_distance", 0),
    (position_move_x, pos5, 60, 0),

    (init_position, pos2),
    (cur_tableau_add_troop, "trp_player", pos2, ":animation", 0),
    (cur_tableau_set_camera_position, pos5),

    (copy_position, pos8, pos5),
    (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
    (position_rotate_z, pos8, 30),
    (position_rotate_x, pos8, -60),
    (cur_tableau_add_sun_light, pos8, 175,150,125),
    ]),
    
("dac_clear_player_attributes", [
    (set_show_messages, 0),
    
    # ca_strength     = 0
    # ca_agility      = 1
    # ca_intelligence = 2
    # ca_charisma     = 3
    # (store_attribute_level, ":strenght", "trp_player", ca_strength),
    # (store_attribute_level, ":agility", "trp_player", ca_agility),
    # (store_attribute_level, ":intelligence", "trp_player", ca_intelligence),
    # (store_attribute_level, ":charisma", "trp_player", ca_charisma),
    
    # pc_strenght = 4
    # pc_agility = 4
    # pc_intelligence = 4
    # pc_charisma = 4
    
    # (store_sub, ":strenght", pc_strenght, ":strenght"),
    # (store_sub, ":agility", pc_agility, ":agility"),
    # (store_sub, ":intelligence", pc_intelligence, ":intelligence"),
    # (store_sub, ":charisma", pc_charisma, ":charisma"),
    
    # (troop_raise_attribute, "trp_player", ca_strength, ":strenght"),
    # (troop_raise_attribute, "trp_player", ca_agility, ":agility"),
    # (troop_raise_attribute, "trp_player", ca_intelligence, ":intelligence"),
    # (troop_raise_attribute, "trp_player", ca_charisma, ":charisma"),
    
    (try_for_range, ":attribute", ca_strength, ca_charisma + 1),
        (store_attribute_level, ":attribute_level", "trp_player", ":attribute"),
        (store_sub, ":attribute_level", pc_attribute, ":attribute_level"),
        (troop_raise_attribute, "trp_player", ":attribute", ":attribute_level"),
    (try_end),
        
    (try_for_range, ":skill", skl_trade, skl_reserved_18 + 1),
        (store_skill_level, ":skill_level", ":skill", "trp_player"),
        (store_sub, ":skill_level", 0, ":skill_level"),
        (troop_raise_skill, "trp_player", ":skill", ":skill_level"),
    (try_end),
    
    (try_for_range, ":weapon_skill", wpt_one_handed_weapon, wpt_firearm + 1),
        (store_proficiency_level, ":proficiency_level", "trp_player", ":weapon_skill"),
        (store_sub, ":proficiency_level", pc_wp_all, ":proficiency_level"),
        (troop_raise_proficiency_linear, "trp_player", ":weapon_skill", ":proficiency_level"),
    (try_end),
    
    (store_troop_gold, ":gold", "trp_player"),
    (try_begin),
        (gt, ":gold", 0),
        (troop_remove_gold, "trp_player", ":gold"),
    (try_end),
    
    (troop_set_slot, "trp_player", slot_troop_renown, 0),
    (assign, "$player_honor", 0),
    (assign, "$player_gold", 0),
    
    (set_show_messages, 1),
  ]),
    
("dac_clear_player_equipment", [
    (set_show_messages, 0),
    
    (troop_clear_inventory, "trp_player"),
    
    (try_for_range, ":i_slot", ek_item_0, ek_horse + 1),
        (troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
        (gt, ":item", -1),
        (troop_remove_item, "trp_player", ":item",),
    (try_end),
    
    (set_show_messages, 1),
  ]),
    
### DAC Seek: Equipment for custom character start and presentation
("dac_commoner_start_equipment", [
    (set_show_messages, 0),
    (store_script_param, ":background", 1),
    
    
    
    (try_begin),
        (eq, ":background", cc_noble_governor),        
        (troop_add_item, "trp_player","itm_h_highlander_beret_black",0),
        (troop_add_item, "trp_player","itm_a_houpelande_decorated_b_1",0),
        (troop_add_item, "trp_player","itm_b_poulaines_lined_2",0),
        (troop_add_item, "trp_player","itm_w_dagger_italian", imodbit_masterwork),
        (troop_add_item, "trp_player","itm_ho_rouncey_1",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 2),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 6),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_inventory_management,3),
        (troop_raise_skill, "trp_player",skl_engineer,4),
        (troop_raise_skill, "trp_player",skl_persuasion,3),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),	 
        (troop_raise_skill, "trp_player",skl_trade,1),	 
       
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
        
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (assign, "$player_honor", 5),
        (assign, "$player_gold", 5000),
        
        (item_set_slot, "itm_bread", slot_item_enterprise_building_cost, 1200),
        (item_set_slot, "itm_ale", slot_item_enterprise_building_cost, 2000),
        (item_set_slot, "itm_wine", slot_item_enterprise_building_cost, 4000),
        (item_set_slot, "itm_leatherwork", slot_item_enterprise_building_cost, 6400),
        (item_set_slot, "itm_wool_cloth", slot_item_enterprise_building_cost, 4800),
        (item_set_slot, "itm_linen", slot_item_enterprise_building_cost, 4800),
        (item_set_slot, "itm_tools", slot_item_enterprise_building_cost, 2800),
        (item_set_slot, "itm_oil", slot_item_enterprise_building_cost, 3600),
        (item_set_slot, "itm_velvet", slot_item_enterprise_building_cost, 8000),

    (else_try),
        (eq, ":background", cc_noble_tactician),   
        (troop_add_item, "trp_player","itm_h_highlander_beret_red_2",0),
        (troop_add_item, "trp_player","itm_a_noble_shirt_red",0),
        (troop_add_item, "trp_player","itm_b_high_boots_9",0),
        (troop_add_item, "trp_player","itm_w_onehanded_sword_martyr",0),
        (troop_add_item, "trp_player","itm_ho_courser_1",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 2),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 4),
        (troop_raise_attribute, "trp_player", ca_charisma, 6),
        
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_trainer,1),
        (troop_raise_skill, "trp_player",skl_tactics,2), 
        (troop_raise_skill, "trp_player",skl_pathfinding,1),	 
        (troop_raise_skill, "trp_player",skl_inventory_management,1),	 
        (troop_raise_skill, "trp_player",skl_engineer,2),	 
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),	 
        (troop_raise_skill, "trp_player",skl_leadership,4),	 
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 125),
        (assign, "$player_honor", 5),
        (assign, "$player_gold", 2500),
        
    (else_try),
        (eq, ":background", cc_noble_jouster),   
        (troop_add_item, "trp_player","itm_a_pistoia_mail_b_mail_sleeves_over_plate",0),
        (troop_add_item, "trp_player","itm_b_high_boots_3",0),
        (troop_add_item, "trp_player","itm_h_simple_cervelliere_mail_aventail",0),
        (troop_add_item, "trp_player","itm_s_heraldic_shield_leather",0),
        (troop_add_item, "trp_player","itm_w_native_spear_b_custom",0),
        (troop_add_item, "trp_player","itm_w_onehanded_sword_knight",0),
        (troop_add_item, "trp_player","itm_g_gauntlets_mailed",0),
        (troop_add_item, "trp_player","itm_ho_horse_barded_black",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 8),
        (troop_raise_attribute, "trp_player", ca_agility, 6),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 2),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,2),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_power_throw,1),
        (troop_raise_skill, "trp_player",skl_power_draw,1),
        (troop_raise_skill, "trp_player",skl_weapon_master,2),
        (troop_raise_skill, "trp_player",skl_shield,2),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_riding,3),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 80 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 80 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           80 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 150),
        (assign, "$player_honor", 10),
        (assign, "$player_gold", 2000),
        
    (else_try),
        (eq, ":background", cc_merchant_goods),   
        (troop_add_item, "trp_player","itm_h_highlander_beret_red_2",0),
        (troop_add_item, "trp_player","itm_a_merchant_outfit",0),
        (troop_add_item, "trp_player","itm_b_low_boots_4",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_dagger_italian",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 1),
        (troop_raise_attribute, "trp_player", ca_agility, 1),
        (troop_raise_attribute, "trp_player", ca_intelligence, 6),
        (troop_raise_attribute, "trp_player", ca_charisma, 6),
        
        (troop_raise_skill, "trp_player",skl_pathfinding,2),
        (troop_raise_skill, "trp_player",skl_spotting,1),
        (troop_raise_skill, "trp_player",skl_inventory_management,1),
        (troop_raise_skill, "trp_player",skl_persuasion,4),
        (troop_raise_skill, "trp_player",skl_trade,4),

        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           30 - pc_wp_all),
                 
        (troop_set_slot, "trp_player", slot_troop_renown, 40),
        (assign, "$player_honor", 1),
        (assign, "$player_gold", 2500),
        
    (store_random_in_range, ":trade_item", trade_goods_begin, trade_goods_end),
    (troop_add_item, "trp_player",":trade_item",0),
        
    (else_try),
        (eq, ":background", cc_merchant_slave),   
        (troop_add_item, "trp_player","itm_h_simple_coif_black",0),
        (troop_add_item, "trp_player","itm_a_aketon_asher_dagged_thick_black_1",0),
        (troop_add_item, "trp_player","itm_b_turnshoes_2",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_archers_maul",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 3),
        (troop_raise_attribute, "trp_player", ca_agility, 3),
        (troop_raise_attribute, "trp_player", ca_intelligence, 4),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_tracking,2),
        (troop_raise_skill, "trp_player",skl_pathfinding,2),
        (troop_raise_skill, "trp_player",skl_spotting,2),
        (troop_raise_skill, "trp_player",skl_prisoner_management,3),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,2),

        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 50 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           30 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
        (assign, "$player_honor", -5),
        (assign, "$player_gold", 1850),
        
    (else_try),
        (eq, ":background", cc_merchant_investor),   
        (troop_add_item, "trp_player","itm_h_bycocket_1_custom",0),
        (troop_add_item, "trp_player","itm_a_houpelande_a_1",0),
        (troop_add_item, "trp_player","itm_b_poulaines_lined_1",0),
        (troop_add_item, "trp_player","itm_w_dagger_quillon",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 1),
        (troop_raise_attribute, "trp_player", ca_agility, 1),
        (troop_raise_attribute, "trp_player", ca_intelligence, 7),
        (troop_raise_attribute, "trp_player", ca_charisma, 5),
        
        (troop_raise_skill, "trp_player",skl_looting,1),
        (troop_raise_skill, "trp_player",skl_inventory_management,1),
        (troop_raise_skill, "trp_player",skl_engineer,2),
        (troop_raise_skill, "trp_player",skl_persuasion,5),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_trade,4),

        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           30 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (assign, "$player_honor", -1),
        (assign, "$player_gold", 6000),
        
    (else_try),
        (eq, ":background", cc_soldier_scout),   
        (troop_add_item, "trp_player","itm_w_onehanded_sword_a_long"),
        (troop_add_item, "trp_player","itm_w_lance_2"),
        (troop_add_item, "trp_player","itm_s_heater_shield_burgundian_1"),
        (troop_add_item, "trp_player","itm_h_makeshift_kettle_strap"),
        (troop_add_item, "trp_player","itm_a_light_gambeson_long_sleeves_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_2"),
        (troop_add_item, "trp_player","itm_ho_courser_3"),
        
        (troop_raise_attribute, "trp_player", ca_strength, 4),
        (troop_raise_attribute, "trp_player", ca_agility, 6),
        (troop_raise_attribute, "trp_player", ca_intelligence, 3),
        (troop_raise_attribute, "trp_player", ca_charisma, 1),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_power_throw,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_horse_archery,1),
        (troop_raise_skill, "trp_player",skl_tracking,1),
        (troop_raise_skill, "trp_player",skl_pathfinding,3),
        (troop_raise_skill, "trp_player",skl_spotting,3),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          50 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 25),
        (assign, "$player_honor", 2),
        (assign, "$player_gold", 750),
        
    (else_try),
        (eq, ":background", cc_soldier_quartermaster),  
        (troop_add_item, "trp_player","itm_w_archer_hatchet_red"),
        (troop_add_item, "trp_player","itm_w_crossbow_light"),
        (troop_add_item, "trp_player","itm_w_bolt_triangular"),
        (troop_add_item, "trp_player","itm_h_arming_cap"),
        (troop_add_item, "trp_player","itm_a_peasant_cotehardie_custom"),
        (troop_add_item, "trp_player","itm_b_poulaines_1"),
        
        (troop_raise_attribute, "trp_player", ca_strength, 3),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 6),
        (troop_raise_attribute, "trp_player", ca_charisma, 3),
        
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_athletics,2),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_inventory_management,4),
        (troop_raise_skill, "trp_player",skl_engineer,1),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,3),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           60 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 30),
        (assign, "$player_honor", 2),
        (assign, "$player_gold", 1250),
        
    (store_random_in_range, ":food_item", food_begin, food_end),
    (troop_add_item, "trp_player",":food_item",0),
    (store_random_in_range, ":trade_item", trade_goods_begin, trade_goods_end),
    (troop_add_item, "trp_player",":trade_item",0),
        
    (else_try),
        (eq, ":background", cc_soldier_cook),   
        (troop_add_item, "trp_player","itm_w_dagger_quillon"),
        (troop_add_item, "trp_player","itm_h_peasant_bycocket_1_custom"),
        (troop_add_item, "trp_player","itm_a_peasant_man_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_2"),
        
        (troop_raise_attribute, "trp_player", ca_strength, 4),
        (troop_raise_attribute, "trp_player", ca_agility, 3),
        (troop_raise_attribute, "trp_player", ca_intelligence, 3),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,2),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_inventory_management,2),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_persuasion,2),
        (troop_raise_skill, "trp_player",skl_prisoner_management,2),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,2),

        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 35),
        (assign, "$player_honor", 2),
        (assign, "$player_gold", 850),
        
        (store_random_in_range, ":food_item", food_begin, food_end),
        (troop_add_item, "trp_player",":food_item",0),
        
    (else_try),
        (eq, ":background", cc_soldier_sergeant),   
        (troop_add_item, "trp_player","itm_w_bastard_sword_c"),
        (troop_add_item, "trp_player","itm_heraldic_banner"),
        (troop_add_item, "trp_player","itm_h_sallet_strap"),
        (troop_add_item, "trp_player","itm_a_gambeson_asher_belt_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_2"),
        
        (troop_raise_attribute, "trp_player", ca_strength, 5),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 5),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,2),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_looting,1),
        (troop_raise_skill, "trp_player",skl_trainer,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_leadership,3),

        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 50 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (assign, "$player_honor", 2),
        (assign, "$player_gold", 900),
        
    (else_try),
        (eq, ":background", cc_hunter_poacher),   
        (troop_add_item, "trp_player","itm_w_archers_maul"),
        (troop_add_item, "trp_player","itm_w_arrow_broadhead"),
        (troop_add_item, "trp_player","itm_w_hunting_bow_yew"),
        (troop_add_item, "trp_player","itm_h_hood_big_liripipe_full_custom"),
        (troop_add_item, "trp_player","itm_a_hunter_coat_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_4"),	
        
        (troop_raise_attribute, "trp_player", ca_strength, 4),
        (troop_raise_attribute, "trp_player", ca_agility, 4),
        (troop_raise_attribute, "trp_player", ca_intelligence, 4),
        (troop_raise_attribute, "trp_player", ca_charisma, 2),
        
        (troop_raise_skill, "trp_player",skl_power_draw,3),
        (troop_raise_skill, "trp_player",skl_athletics,2),
        (troop_raise_skill, "trp_player",skl_tracking,2),
        (troop_raise_skill, "trp_player",skl_pathfinding,4),
        (troop_raise_skill, "trp_player",skl_spotting,3),
    
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           80 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
        (assign, "$player_honor", 3),
        (assign, "$player_gold", 250),
        
    (else_try),
        (eq, ":background", cc_hunter_manhunter),   
        (troop_add_item, "trp_player","itm_w_mace_winged"),
        (troop_add_item, "trp_player","itm_h_shingle_helmet_strap"),
        (troop_add_item, "trp_player","itm_a_tunic_over_gambeson_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_1"),	
        
        (troop_raise_attribute, "trp_player", ca_strength, 4),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 3),
        (troop_raise_attribute, "trp_player", ca_charisma, 5),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_tracking,1),
        (troop_raise_skill, "trp_player",skl_pathfinding,2),
        (troop_raise_skill, "trp_player",skl_spotting,2),
        (troop_raise_skill, "trp_player",skl_prisoner_management,4),
        (troop_raise_skill, "trp_player",skl_leadership,1),
    
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 70 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
        (assign, "$player_honor", -5),
        (assign, "$player_gold", 650),
        
    (else_try),
        (eq, ":background", cc_hunter_marksman),   
        (troop_add_item, "trp_player","itm_w_dagger_quillon"),
        (troop_add_item, "trp_player","itm_w_bolt_triangular"),
        (troop_add_item, "trp_player","itm_w_crossbow_light"),
        (troop_add_item, "trp_player","itm_h_peasant_bycocket_2_custom"),
        (troop_add_item, "trp_player","itm_a_tailored_cotehardie_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_2"),	
        
        (troop_raise_attribute, "trp_player", ca_strength, 4),
        (troop_raise_attribute, "trp_player", ca_agility, 4),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_power_throw,2),
        (troop_raise_skill, "trp_player",skl_power_draw,4),
        (troop_raise_skill, "trp_player",skl_weapon_master,2),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_pathfinding,2),
        (troop_raise_skill, "trp_player",skl_spotting,2),
        (troop_raise_skill, "trp_player",skl_persuasion,1),
    
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           60 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 60),
        (assign, "$player_honor", 3),
        (assign, "$player_gold", 775),
        
    (else_try),
        (eq, ":background", cc_mercenary_condottiero),   
        (troop_add_item, "trp_player","itm_w_light_lance"),
        (troop_add_item, "trp_player","itm_w_onehanded_sword_italian"),
        (troop_add_item, "trp_player","itm_h_barbuta_nooxy_1_mail_collar"),
        (troop_add_item, "trp_player","itm_a_pistoia_mail_a_mail_sleeves_short_plate_1"),
        (troop_add_item, "trp_player","itm_b_high_boots_1"),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet"),	
        
        (troop_raise_attribute, "trp_player", ca_strength, 5),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 5),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_trainer,1),
        (troop_raise_skill, "trp_player",skl_tactics,2),
        (troop_raise_skill, "trp_player",skl_inventory_management,1),
        (troop_raise_skill, "trp_player",skl_persuasion,1),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_leadership,4),
        (troop_raise_skill, "trp_player",skl_trade,1),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 120),
        (assign, "$player_honor", 2),
        (assign, "$player_gold", 6000),
        
    (else_try),
        (eq, ":background", cc_mercenary_flemish),   
        (troop_add_item, "trp_player","itm_w_dagger_pikeman"),
        (troop_add_item, "trp_player","itm_w_awlpike_1"),
        (troop_add_item, "trp_player","itm_h_german_kettlehat_4_liripipe_hood_custom"),
        (troop_add_item, "trp_player","itm_a_pistoia_breastplate_half_mail_sleeves"),
        (troop_add_item, "trp_player","itm_b_poulaines_lined_1"),
        (troop_add_item, "trp_player","itm_s_steel_buckler"),	
        
        (troop_raise_attribute, "trp_player", ca_strength, 4),
        (troop_raise_attribute, "trp_player", ca_agility, 3),
        (troop_raise_attribute, "trp_player", ca_intelligence, 3),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,2),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_shield,1),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_looting,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_pathfinding,1),
        (troop_raise_skill, "trp_player",skl_spotting,1),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_leadership,3),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           80 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           40 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 60),
        (assign, "$player_honor", 0),
        (assign, "$player_gold", 4500),
        
    (else_try),
        (eq, ":background", cc_mercenary_scottish),   
        (troop_add_item, "trp_player","itm_w_onehanded_sword_scottish"),
        (troop_add_item, "trp_player","itm_s_heraldic_shield_heater"),
        (troop_add_item, "trp_player","itm_h_bascinet_1_mail_aventail"),
        (troop_add_item, "trp_player","itm_a_churburg_13_asher_plain_custom"),
        (troop_add_item, "trp_player","itm_b_turnshoes_1"),
        
        (troop_raise_attribute, "trp_player", ca_strength, 6),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,2),
        (troop_raise_skill, "trp_player",skl_power_strike,3),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_trainer,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_persuasion,1),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_skill, "trp_player",skl_leadership,2),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 80 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (assign, "$player_honor", 5),
        (assign, "$player_gold", 3750),
        
    (else_try),
        (eq, ":background", cc_peasant_farmer),   
        (troop_add_item, "trp_player","itm_h_straw_hat",0),
        (troop_add_item, "trp_player","itm_a_farmer_tunic",0),
        (troop_add_item, "trp_player","itm_b_turnshoes_1",0),
        (troop_add_item, "trp_player","itm_w_fork_1",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 6),
        (troop_raise_attribute, "trp_player", ca_agility, 4),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 2),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,3),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_athletics,3),
        (troop_raise_skill, "trp_player",skl_pathfinding,2),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_engineer,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,1),
    
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
        (assign, "$player_honor", 1),
        (assign, "$player_gold", 50),
        
    (else_try),
        (eq, ":background", cc_peasant_revolutionary),   
        (troop_add_item, "trp_player","itm_h_wicker_helmet_strap",0),
        (troop_add_item, "trp_player","itm_a_peasant_cote_custom",0),
        (troop_add_item, "trp_player","itm_b_turnshoes_2",0),
        (troop_add_item, "trp_player","itm_w_fauchard_1",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 2),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 4),
        (troop_raise_attribute, "trp_player", ca_charisma, 6),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,2),
        (troop_raise_skill, "trp_player",skl_power_strike,2),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_looting,2),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_pathfinding,1),
        (troop_raise_skill, "trp_player",skl_persuasion,2),
        (troop_raise_skill, "trp_player",skl_leadership,3),

        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 50 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 25),
        (assign, "$player_honor", -3),
        (assign, "$player_gold", 725),
        
    (else_try),
        (eq, ":background", cc_peasant_smith),   
        (troop_add_item, "trp_player","itm_h_leather_cap",0),
        (troop_add_item, "trp_player","itm_a_commoner_apron",0),
        (troop_add_item, "trp_player","itm_b_turnshoes_6",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_warhammer_1_brown",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 6),
        (troop_raise_attribute, "trp_player", ca_agility, 2),
        (troop_raise_attribute, "trp_player", ca_intelligence, 2),
        (troop_raise_attribute, "trp_player", ca_charisma, 4),
        
        (troop_raise_skill, "trp_player",skl_power_strike,3),
        (troop_raise_skill, "trp_player",skl_inventory_management,3),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_engineer,2),
        (troop_raise_skill, "trp_player",skl_prisoner_management,2),
        (troop_raise_skill, "trp_player",skl_trade,2),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 60 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
  
        (troop_set_slot, "trp_player", slot_troop_renown, 15),
        (assign, "$player_honor", 1),
        (assign, "$player_gold", 300),
        
    (else_try),
        (eq, ":background", cb_healer_surgeon),   
        (troop_add_item, "trp_player","itm_h_simple_coif",0),
        (troop_add_item, "trp_player","itm_a_surgeon_dress",0),
        (troop_add_item, "trp_player","itm_b_turnshoes_6",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_dagger_italian",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 2),
        (troop_raise_attribute, "trp_player", ca_agility, 3),
        (troop_raise_attribute, "trp_player", ca_intelligence, 6),
        (troop_raise_attribute, "trp_player", ca_charisma, 3),
        
        (troop_raise_skill, "trp_player",skl_ironflesh,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_weapon_master,2),
        (troop_raise_skill, "trp_player",skl_wound_treatment,2),
        (troop_raise_skill, "trp_player",skl_surgery,5),
        (troop_raise_skill, "trp_player",skl_first_aid,3),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
        (assign, "$player_honor", 5),
        (assign, "$player_gold", 350),
        
    (else_try),
        (eq, ":background", cb_healer_priest),   
        (troop_add_item, "trp_player","itm_h_straw_hat_3",0),
        (troop_add_item, "trp_player","itm_a_priest_robe",0),
        (troop_add_item, "trp_player","itm_b_turnshoes_2",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 1),
        (troop_raise_attribute, "trp_player", ca_agility, 1),
        (troop_raise_attribute, "trp_player", ca_intelligence, 6),
        (troop_raise_attribute, "trp_player", ca_charisma, 6),
        
        (troop_raise_skill, "trp_player",skl_wound_treatment,4),
        (troop_raise_skill, "trp_player",skl_surgery,1),
        (troop_raise_skill, "trp_player",skl_first_aid,2),
        (troop_raise_skill, "trp_player",skl_persuasion,3),
        (troop_raise_skill, "trp_player",skl_leadership,2),
        (troop_raise_skill, "trp_player",skl_trade,2),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           20 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (assign, "$player_honor", 10),
        (assign, "$player_gold", 500),         
         
    (else_try),
        (eq, ":background", cb_healer_alchemist),  
        (troop_add_item, "trp_player","itm_h_hood_black",0),
        (troop_add_item, "trp_player","itm_a_noble_shirt_black",0),
        (troop_add_item, "trp_player","itm_b_high_boots_2",0),
        (troop_add_item, "trp_player","itm_g_leather_gauntlet",0),
        (troop_add_item, "trp_player","itm_w_dagger_italian",0),
        
        (troop_raise_attribute, "trp_player", ca_strength, 2),
        (troop_raise_attribute, "trp_player", ca_agility, 4),
        (troop_raise_attribute, "trp_player", ca_intelligence, 7),
        (troop_raise_attribute, "trp_player", ca_charisma, 1),

        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_inventory_management,2),
        (troop_raise_skill, "trp_player",skl_wound_treatment,2),
        (troop_raise_skill, "trp_player",skl_surgery,1),
        (troop_raise_skill, "trp_player",skl_first_aid,4),
        (troop_raise_skill, "trp_player",skl_engineer,2),
        (troop_raise_skill, "trp_player",skl_persuasion,1),
        (troop_raise_skill, "trp_player",skl_trade,1),
        
        (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 40 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_polearm,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_archery,           20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_crossbow,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_throwing,          20 - pc_wp_all),
        (troop_raise_proficiency_linear, "trp_player", wpt_firearm,           40 - pc_wp_all),
         
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
        (assign, "$player_honor", 1),
        (assign, "$player_gold", 800),         
         
    (try_end),
    
    (troop_equip_items, "trp_player"),
    
    (store_random_in_range, ":food_item", food_begin, food_end),
    (troop_add_item, "trp_player",":food_item",0),
    
    (set_show_messages, 1),
  ]),
    
    
]