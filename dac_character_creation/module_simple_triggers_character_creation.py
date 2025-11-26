from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from module_constants import *

from compiler import *

character_creation_simple_triggers = [

# QUEST: floris_active_tournament
# Determine if tournaments are active in a town.
#  - Deliver quest if tournament active and quest is not.  
#  - End quest if tournament is not active and quest is.
(12,
	[
		(map_free),
		(eq, "$class_type_feature_active", 1),
		(assign, ":closest_town_no", -1),
		(assign, ":closest_town_dist", -1),
        (eq, "$class_type", cc_noble_jouster),
		(try_for_range, ":center_no", towns_begin, towns_end),
			(party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament), # 0 = no, 1 = last day, 2+ = ongoing.
			(try_begin),
				##### ACQUIRE QUEST: Determine appropriate city #####
				# Make sure there is enough time to travel there.
				(ge, ":has_tournament", 3),
				# Check if the town is hostile to the player.
				(call_script, "script_tpe_store_town_faction_to_reg0", ":center_no"),
				(store_relation, ":relation", reg0, "fac_player_supporters_faction"),
				(ge, ":relation", 0),
				(party_get_slot, ":troop_host", ":center_no", slot_town_lord),
				(ge, ":troop_host", 0), # Make sure someone actually controls the town.
				(neq, ":troop_host", "trp_player"), # Make sure the player isn't inviting himself.
				# See if this town is closer than the current candidate.
				(store_distance_to_party_from_party, ":distance", "p_main_party", ":center_no"),
				(this_or_next|lt, ":distance", ":closest_town_dist"),
				(eq, ":closest_town_dist", -1),
				(assign, ":closest_town_dist", ":distance"),
				(assign, ":closest_town_no", ":center_no"),
				# (ge, DEBUG_TPE_QUESTS, 1),
				# (assign, reg31, ":has_tournament"),
				# (str_store_party_name, s31, ":center_no"),
				# (display_message, "@DEBUG (Quest Pack 1): {s31} has a tournament with {reg31} days left."),
			(else_try),
				##### FAIL QUEST: EXPIRED #####
				(le, ":has_tournament", 0),
				# Condition: Ensure quest IS active.
				(check_quest_active, "qst_floris_active_tournament"),
				(neg|quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_participated_in_tournament),
				(neg|quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_refused_invitation),
				(quest_slot_eq, "qst_floris_active_tournament", slot_quest_target_center, ":center_no"),
				# Set quest to failed due to timeout.
				(fail_quest, "qst_floris_active_tournament"),
				(complete_quest, "qst_floris_active_tournament"),
				(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_refused_invitation),
				(try_begin),
					(quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_message_received), # If you weren't invited then no one should care if you don't attend.
					# (ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_MEDIUM),
					(call_script, "script_change_troop_renown", "trp_player", -1),
					# (ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_HIGH),
					# (quest_get_slot, ":town_lord", "qst_floris_active_tournament", slot_quest_giver_troop),
					# (str_store_troop_name, s21, ":town_lord"),
					# (display_message, "@{s21} is insulted by your refusal of his invitation.", color_bad_news),
                    (troop_slot_ge, "trp_player", slot_troop_renown, 200),
					(display_message, "@People are disappointed that you didn't participate in the tournament.", color_bad_news),
					# (call_script, "script_troop_change_relation_with_troop", "trp_player", ":town_lord", -2),
				(try_end),
				# Let the player know he failed the quest if he's close enough to hear of it end.
				#(call_script, "script_cf_qus_party_close_to_center", "p_main_party", ":center_no"),
				(str_store_party_name, s31, ":center_no"),
				(display_message, "@The tournament in {s31} has ended."),
			(else_try),
				##### FAIL QUEST: HELD IN HOSTILE CITY ####
				(check_quest_active, "qst_floris_active_tournament"),
				(quest_slot_eq, "qst_floris_active_tournament", slot_quest_target_center, ":center_no"),
				(call_script, "script_tpe_store_town_faction_to_reg0", ":center_no"),
				(store_relation, ":relation", reg0, "fac_player_supporters_faction"),
				(lt, ":relation", 0),
				# Set quest to failed due to inability to attend.
				(fail_quest, "qst_floris_active_tournament"),
				(complete_quest, "qst_floris_active_tournament"),
				(str_store_party_name, s31, ":center_no"),
				(display_message, "@Quest ended due to {s31} becoming hostile."),
				(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0),
			(try_end),
		(try_end),
		
		# Now assign a tournament to go to if there is a valid option and the quest isn't already active.
		(is_between, ":closest_town_no", towns_begin, towns_end),
		(neg|check_quest_active, "qst_floris_active_tournament"),
		(quest_slot_eq, "qst_floris_active_tournament", slot_quest_dont_give_again_remaining_days, 0),
		#(call_script, "script_cf_qus_party_close_to_center", "p_main_party", ":center_no"),
				
		# Initialize some quest information.
		(party_get_slot, ":days_left", ":closest_town_no", slot_town_has_tournament),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_target_center, ":closest_town_no"),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_expiration_days, ":days_left"),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_dont_give_again_period, 10),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_dont_give_again_remaining_days, 10),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_xp_reward, 100),
		(party_get_slot, ":town_lord", ":closest_town_no", slot_town_lord),
		(troop_is_hero, ":town_lord"),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_giver_troop, ":town_lord"),
		
		(str_clear, s8),
		(str_clear, s9),
		(str_clear, s12),
		(str_clear, s13),
		
		# Set quest to active.
		(quest_get_slot, ":town_lord", "qst_floris_active_tournament", slot_quest_giver_troop),
		(quest_get_slot, ":closest_town_no", "qst_floris_active_tournament", slot_quest_target_center),
		(str_store_troop_name_link, s9, ":town_lord"),
		(str_store_party_name_link, s13, ":closest_town_no"),
		(str_store_troop_name, s8, ":town_lord"),
		(str_store_party_name, s12, ":closest_town_no"),
		(try_begin), # Checks if your renown warrants an invitation based on distance away.
			(store_distance_to_party_from_party, ":distance", "p_main_party", ":closest_town_no"),
			(val_mul, ":distance", 2),
			(troop_slot_ge, "trp_player", slot_troop_renown, 50),
			(troop_slot_ge, "trp_player", slot_troop_renown, ":distance"),
			(dialog_box, "str_qp1_tournaments_invited_by_s8_to_s12", "@A Messenger Arrives"),
			(str_store_string, s2, "str_qp1_quest_desc_tournament_invited_by_s9_to_s13"),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_message_received),
		(else_try),
			(dialog_box, "str_qp1_tournaments_held_by_s8_in_s12", "@Rumor of the Road"),
			(str_store_string, s2, "str_qp1_quest_desc_tournament_held_by_s9_to_s13"),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0), # Should mean no one cares if you come or not.
		(try_end),
		(setup_quest_text, "qst_floris_active_tournament"),
		(call_script, "script_start_quest", "qst_floris_active_tournament", ":town_lord"),
	]),
    
### DAC Seek: Scout Foraging
(3,
   [
        (eq, "$class_type", cc_hunter_poacher),
		(map_free),
        
        (party_get_current_terrain, ":terrain_type", "p_main_party"),
        (this_or_next|eq, ":terrain_type", rt_steppe_forest),
        (this_or_next|eq, ":terrain_type", rt_forest),
        (eq, ":terrain_type", rt_snow_forest),
        
        (store_free_inventory_capacity, ":inv_cap", "trp_player"),
        (gt, ":inv_cap", 0),
        (call_script, "script_rand", 0, 100),
        (assign, ":rand_no", reg0),
        (str_clear, s1),
   
        (try_begin),
            (is_between, ":rand_no", 0, 5),
            (assign, ":foraged_food", "itm_honey"),
        (else_try),
            (is_between, ":rand_no", 5, 10),
            (assign, ":foraged_food", "itm_dried_meat"),
        (else_try),
            (is_between, ":rand_no", 10, 15),
            (assign, ":foraged_food", "itm_apples"),
        (else_try),
            (is_between, ":rand_no", 15, 20),
            (assign, ":foraged_food", "itm_chicken"),
        (else_try),
            (is_between, ":rand_no", 20, 25),
            (assign, ":foraged_food", "itm_pork"),
        (else_try),
            (assign, ":foraged_food", -1),     
        (try_end),
        
        (gt, ":foraged_food", -1),
        (troop_add_item, "trp_player", ":foraged_food", 0),
        (str_store_item_name, s1, ":foraged_food"),
        (display_message, "str_dac_successfully_foraged_s1", color_good_news),
     ]),

# QUEST: floris_active_tournament
# Determine if tournaments are active in a town.
#  - Deliver quest if tournament active and quest is not.  
#  - End quest if tournament is not active and quest is.
# (12,
	# [
		# (map_free),
		# (this_or_next|ge, DEBUG_TPE_general, 1),
		# (ge, DEBUG_TPE_QUESTS, 1),
		# (eq, "$g_wp_tpe_active", 1),
		# (str_clear, s21),
		# (display_message, "@List of Active Tournaments"),
		# (try_for_range, ":center_no", towns_begin, towns_end),
			# (party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament), # 0 = no, 1 = last day, 2+ = ongoing.
			# (ge, ":has_tournament", 1),
			# (assign, reg31, ":has_tournament"),
			# (str_store_party_name, s31, ":center_no"),
			# (display_message, "@{s31} has a tournament with {reg31} days left."),
		# (try_end),
	# ]),
    
### DAC Seek: Work in villages as a farmer
  (1, [
        (this_or_next|ge, "$g_camp_mode", 1), ### Rest in camp or location
        (neg|map_free),
        
        (this_or_next|eq, "$class_type", cc_peasant_farmer),
        (eq, "$class_type", cc_peasant_smith),
       
        (try_begin),
            (troop_get_slot, ":rest_hours", "trp_player", slot_troop_player_workday_rest),
            (ge, ":rest_hours", 1),
            (val_sub, ":rest_hours", 1),
            (troop_set_slot, "trp_player", slot_troop_player_workday_rest, ":rest_hours"),
        (try_end),

        (try_begin),
            (eq, "$class_type_feature_active", 1),
            (troop_get_slot, ":work_hours", "trp_player", slot_troop_player_workday_hours),
            (val_sub, ":work_hours", 1),
            (troop_set_slot, "trp_player", slot_troop_player_workday_hours, ":work_hours"),
            
            (try_begin),
                (lt, ":work_hours", 0),
                (assign, "$class_type_feature_active", 0),
                (rest_for_hours, 0, 0, 0),
                (jump_to_menu, "mnu_dac_work_town_village_complete"),
            (else_try),
                (troop_get_slot, ":payment", "trp_player", slot_troop_player_workday_payment),
                (call_script, "script_troop_add_gold", "trp_player", ":payment"),
                
                (call_script, "script_rand", 0, 100),
                (assign, ":random", reg0),
                (try_begin),
                    (lt, ":random", 5),
                    (store_random_in_range, ":food_item", food_begin, food_end),
                    (troop_add_item, "trp_player", ":food_item", 0),
                    (str_store_item_name, s1, ":food_item"),
                    (display_message, "str_dac_successfully_earned_s1", color_good_news),
                (try_end),
                
           (try_end),
           
        (try_end),
       ]),


  # Refresh troops and merchant inventory
  (24 * 3,
   [
    (try_begin),
        (eq, "$dac_hideout_built", 1),
        (call_script, "script_refresh_hideout_troops"),
        (call_script, "script_refresh_hideout_merchant_inventory"),
    (try_end),  
    ]),
]