from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *

##diplomacy start+
from module_factions import dplmc_factions_begin, dplmc_factions_end, dplmc_non_generic_factions_begin
#SB : update info pages
from ID_info_pages import *
##diplomacy end+

##diplomacy begin
##jrider reports
from header_presentations import tf_left_align
  #### Autoloot improved by rubik begin
from module_items import *

from compiler import *

diplomacy_scripts = [
##diplomacy begin
  #recruiter kit begin
  ("dplmc_send_recruiter",
    [
      (store_script_param, ":number_of_recruits", 1),
      #daedalus begin
      (store_script_param, ":faction_of_recruits", 2),
      #daedalus end
      # (assign, ":expenses", ":number_of_recruits"),
      #SB : use consts
      (store_mul, ":expenses", ":number_of_recruits", dplmc_recruits_cost),
      (val_add, ":expenses", dplmc_recruiter_salary),
      (call_script, "script_dplmc_withdraw_from_treasury", ":expenses"),
      (set_spawn_radius, 1),
      (spawn_around_party, "$current_town", "pt_dplmc_recruiter"),
      (assign,":spawned_party",reg0),
      (party_set_ai_behavior, ":spawned_party", ai_bhvr_hold),
      (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_recruiter),
      (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits, ":number_of_recruits"),
      #daedalus begin
      (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits_faction, ":faction_of_recruits"),
      #daedalus end
      (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_origin, "$current_town"),
      # (assign, ":faction", "$players_kingdom"),
      (party_set_faction, ":spawned_party", "$players_kingdom"),
      # (party_set_extra_text, ":spawned_party", "str_empty_string"),
      #SB : extra string
      (call_script, "script_dplmc_set_recruiter_extra_text", ":spawned_party", ":number_of_recruits"),
    ]),
#recruiter kit end

####################################################################################
#
# Autoloot Scripts begin
# ---------------------------------------------------
####################################################################################

  #### Autoloot improved by rubik begin
  # ("dplmc_init_item_difficulties", set_item_difficulty()),
  #### Autoloot improved by rubik end


###################################
   # Can a troop qualify to use this item?
   # Returns 1 = yes, 0 = no.
   ("dplmc_troop_can_use_item",
   [
      (store_script_param, ":troop", 1),
      (store_script_param, ":item", 2),
      (store_script_param, ":item_modifier", 3),

      # (item_get_slot, ":difficulty", ":item", dplmc_slot_item_difficulty),
      (item_get_difficulty, ":difficulty", ":item"),
      (item_get_type, ":type", ":item"),
      (try_begin),
        (eq, ":difficulty", 0), # don't apply imod modifiers if item has no requirement
      (else_try),
        (eq, ":item_modifier", imod_stubborn),
        (val_add, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_timid),
        (val_sub, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_heavy),
        (neq, ":type", itp_type_horse), #heavy horses don't increase difficulty
        (val_add, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_strong),
        (val_add, ":difficulty", 2),
      (else_try),
        (eq, ":item_modifier", imod_masterwork),
        (val_add, ":difficulty", 4),
      (try_end),

      (item_get_type, ":type", ":item"),
      (try_begin),
        (eq, ":type", itp_type_horse),
        (store_skill_level, ":skill", skl_riding, ":troop"),
      (else_try),
        (this_or_next|eq, ":type", itp_type_crossbow),
        (this_or_next|eq, ":type", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type", itp_type_two_handed_wpn),
        (this_or_next|eq, ":type", itp_type_polearm),
        (this_or_next|eq, ":type", itp_type_head_armor),
        (this_or_next|eq, ":type", itp_type_body_armor),
        (this_or_next|eq, ":type", itp_type_foot_armor),
        (eq, ":type", itp_type_hand_armor),
        (store_attribute_level, ":skill", ":troop", ca_strength),
      (else_try),
        (eq, ":type", itp_type_shield),
        (store_skill_level, ":skill", skl_shield, ":troop"),
      (else_try),
        (eq, ":type", itp_type_bow),
        (store_skill_level, ":skill", skl_power_draw, ":troop"),
      (else_try),
        (eq, ":type", itp_type_thrown),
        (store_skill_level, ":skill", skl_power_throw, ":troop"),
      (try_end),

      (try_begin),
        (lt, ":skill", ":difficulty"),
        (assign, reg0, 0),
      (else_try),
        (assign, reg0, 1),
      (try_end),
   ]),

#####################################################################
# gets an item's value
# Param1: item ID
# Param2: item modifier
#####################################################################
("dplmc_get_item_value_with_imod", [  # returns the sell price based on the item's money value and its imod
	(store_script_param, ":item", 1),
	(store_script_param, ":imod", 2),
	(store_item_value, ":score", ":item"),
	(try_begin),
		(eq, ":imod", imod_plain),
		(val_mul, ":score", 100),
	(else_try),
		(eq, ":imod", imod_cracked),
		(val_mul, ":score", 50),
	(else_try),
		(eq, ":imod", imod_rusty),
		(val_mul, ":score", 55),
	(else_try),
		(eq, ":imod", imod_bent),
		(val_mul, ":score", 65),
	(else_try),
		(eq, ":imod", imod_chipped),
		(val_mul, ":score", 72),
	(else_try),
		(eq, ":imod", imod_battered),
		(val_mul, ":score", 75),
	(else_try),
		(eq, ":imod", imod_poor),
		(val_mul, ":score", 80),
	(else_try),
		(eq, ":imod", imod_crude),
		(val_mul, ":score", 83),
	(else_try),
		(eq, ":imod", imod_old),
		(val_mul, ":score", 86),
	(else_try),
		(eq, ":imod", imod_cheap),
		(val_mul, ":score", 90),
	(else_try),
		(eq, ":imod", imod_fine),
		(val_mul, ":score", 190),
	(else_try),
		(eq, ":imod", imod_well_made),
		(val_mul, ":score", 250),
	(else_try),
		(eq, ":imod", imod_sharp),
		(val_mul, ":score", 160),
	(else_try),
		(eq, ":imod", imod_balanced),
		(val_mul, ":score", 350),
	(else_try),
		(eq, ":imod", imod_tempered),
		(val_mul, ":score", 670),
	(else_try),
		(eq, ":imod", imod_deadly),
		(val_mul, ":score", 850),
	(else_try),
		(eq, ":imod", imod_exquisite),
		(val_mul, ":score", 1450),
	(else_try),
		(eq, ":imod", imod_masterwork),
		(val_mul, ":score", 1750),
	(else_try),
		(eq, ":imod", imod_heavy),
		(val_mul, ":score", 190),
	(else_try),
		(eq, ":imod", imod_strong),
		(val_mul, ":score", 490),
	(else_try),
		(eq, ":imod", imod_powerful),
		(val_mul, ":score", 320),
	(else_try),
		(eq, ":imod", imod_tattered),
		(val_mul, ":score", 50),
	(else_try),
		(eq, ":imod", imod_ragged),
		(val_mul, ":score", 70),
	(else_try),
		(eq, ":imod", imod_rough),
		(val_mul, ":score", 60),
	(else_try),
		(eq, ":imod", imod_sturdy),
		(val_mul, ":score", 170),
	(else_try),
		(eq, ":imod", imod_thick),
		(val_mul, ":score", 260),
	(else_try),
		(eq, ":imod", imod_hardened),
		(val_mul, ":score", 390),
	(else_try),
		(eq, ":imod", imod_reinforced),
		(val_mul, ":score", 650),
	(else_try),
		(eq, ":imod", imod_superb),
		(val_mul, ":score", 250),
	(else_try),
		(eq, ":imod", imod_lordly),
		(val_mul, ":score", 1150),
	(else_try),
		(eq, ":imod", imod_lame),
		(val_mul, ":score", 40),
	(else_try),
		(eq, ":imod", imod_swaybacked),
		(val_mul, ":score", 60),
	(else_try),
		(eq, ":imod", imod_stubborn),
		(val_mul, ":score", 90),
	(else_try),
		(eq, ":imod", imod_timid),
		(val_mul, ":score", 180),
	(else_try),
		(eq, ":imod", imod_meek),
		(val_mul, ":score", 180),
	(else_try),
		(eq, ":imod", imod_spirited),
		(val_mul, ":score", 650),
	(else_try),
		(eq, ":imod", imod_champion),
		(val_mul, ":score", 1450),
	(else_try),
		(eq, ":imod", imod_fresh),
		(val_mul, ":score", 100),
	(else_try),
		(eq, ":imod", imod_day_old),
		(val_mul, ":score", 100),
	(else_try),
		(eq, ":imod", imod_two_day_old),
		(val_mul, ":score", 90),
	(else_try),
		(eq, ":imod", imod_smelling),
		(val_mul, ":score", 40),
	(else_try),
		(eq, ":imod", imod_rotten),
		(val_mul, ":score", 5),
	(else_try),
		(eq, ":imod", imod_large_bag),
		(val_mul, ":score", 190),
	(try_end),

	(assign, reg0, ":score"),
]),

  #### Autoloot improved by rubik begin
  # ("dplmc_init_item_base_score", set_item_base_score()),

  ("dplmc_get_item_score_with_imod",
    [# returns the score on the item's base score and its imod
      (store_script_param, ":item", 1),
      (store_script_param, ":imod", 2),

      (item_get_type, ":type", ":item"),
      (assign, ":imod_effect", 0), #default modifier
      (try_begin),
        # horse score = horse_speed*horse_armor*horse_sell_price
        (eq, ":type", itp_type_horse),
        # (item_get_slot, ":horse_speed", ":item", dplmc_slot_item_horse_speed),
        # (item_get_slot, ":horse_armor", ":item", dplmc_slot_item_horse_armor),
        (item_get_horse_speed, ":horse_speed", ":item"),
        (item_get_body_armor, ":horse_armor", ":item"),
        # (call_script, "script_dplmc_get_item_value_with_imod", ":item", ":imod"),
        (item_get_value, ":i_score", ":item"),
        # (assign, ":i_score", reg0),

        ## SB : price now secondary (additive) instead of multiplicative with actual attributes
        (item_get_horse_speed, ":horse_speed", ":item"),
        (item_get_horse_maneuver, ":horse_manu", ":item"),
        (item_get_body_armor, ":horse_armor", ":item"),
        (item_get_horse_charge_damage, ":horse_charge", ":item"),
        (item_get_hit_points, ":horse_health", ":item"),

        #imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
        #imodbits_horse_good = imodbit_spirited|imodbit_heavy
        (try_begin),
          (eq, ":imod", imod_swaybacked),
          (val_sub, ":horse_speed", 2),
          (val_sub, ":horse_manu", 2),
        (else_try), #do not pick lame horses at all other than last resort
          (eq, ":imod", imod_lame),
          (assign, ":horse_speed", 0),
        (else_try),
          (eq, ":imod", imod_heavy),
          (val_add, ":horse_armor", 3),
          (val_add, ":horse_charge", 4),
          (val_add, ":horse_health", 10),
        (else_try),
          (eq, ":imod", imod_stubborn),
          (val_add, ":horse_health", 5),
        (else_try),
          (eq, ":imod", imod_spirited),
          (val_add, ":horse_speed", 1),
          (val_add, ":horse_manu", 1),
          (val_add, ":horse_armor", 1),
          (val_add, ":horse_charge", 1),
        (else_try),
          (eq, ":imod", imod_champion),
          (val_add, ":horse_speed", 2),
          (val_add, ":horse_manu", 2),
          (val_add, ":horse_armor", 2),
          (val_add, ":horse_charge", 2),
        (try_end),

        (val_mul, ":horse_speed", ":horse_manu"),
        (val_add, ":i_score", ":horse_speed"),

        (val_mul, ":horse_charge", ":horse_armor"),
        (val_mul, ":horse_charge", ":horse_health"),
        (val_div, ":horse_charge", 100),#baseline hp
        (val_add, ":i_score", ":horse_charge"),
      (else_try),
        # shield score = shield_size*shield_armor
        (eq, ":type", itp_type_shield),
        # (item_get_slot, ":shield_size", ":item", dplmc_slot_item_shield_size),
        # (item_get_slot, ":shield_armor", ":item", dplmc_slot_item_shield_armor),

        ## SB : factor in speed and height
        (item_get_shield_height, ":shield_height", ":item"),
        (item_get_weapon_length, ":shield_width", ":item"),
        (item_get_body_armor, ":shield_armor", ":item"),
        (item_get_speed_rating, ":shield_speed", ":item"),
        (item_get_hit_points, ":shield_health", ":item"),

        (try_begin),
          (gt, ":shield_height", 0),
          (val_mul, ":shield_width",  ":shield_height"),
          (set_fixed_point_multiplier, 100),
          (store_mul, ":i_score", ":shield_width", 100),
          (store_sqrt, ":i_score", ":i_score"),
          (val_div, ":i_score", 100),
        (else_try),
          # (val_mul, ":shield_width", ":shield_width"),
          (assign, ":i_score", ":shield_width"),
        (try_end),


        #imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
        (try_begin),
          # (eq, ":imod", imod_plain),
          # (assign, ":imod_effect", 0),
        # (else_try),
          (eq, ":imod", imod_cracked),
          (assign, ":imod_effect", -4),
          (val_sub, ":shield_health", 56),
        (else_try),
          (eq, ":imod", imod_battered),
          (assign, ":imod_effect", -2),
          (val_sub, ":shield_health", 26),
        (else_try),
          (eq, ":imod", imod_hardened),
          (assign, ":imod_effect", 3),
        (else_try),
          (eq, ":imod", imod_heavy),
          (assign, ":imod_effect", 3),
          (val_add, ":shield_health", 10),
        (else_try),
          (eq, ":imod", imod_thick),
          (assign, ":imod_effect", 2),
          (val_add, ":shield_health", 47),
        (else_try),
          (eq, ":imod", imod_reinforced),
          (assign, ":imod_effect", 4),
          (val_add, ":shield_health", 83),
        (else_try),
          (eq, ":imod", imod_lordly),
          (assign, ":imod_effect", 6),
          (val_add, ":shield_health", 155),
        (try_end),

        (val_add, ":shield_armor", ":imod_effect"),
        (val_add, ":shield_armor", 5), # add 5 to make sure shield_armor greater than 0
        (val_mul, ":i_score", ":shield_armor"),
        (val_mul, ":i_score", ":shield_speed"),
        (val_div, ":i_score", 92), #average speed of all Native's tableau
        (val_add, ":i_score", ":shield_health"), #tie-breaker
      (else_try),
        # armor score = head_armor + body_armor + foot_armor
        (this_or_next|eq, ":type", itp_type_head_armor),
        (this_or_next|eq, ":type", itp_type_body_armor),
        (this_or_next|eq, ":type", itp_type_foot_armor),
        (eq, ":type", itp_type_hand_armor),
        # (item_get_slot, ":head_armor", ":item", dplmc_slot_item_head_armor),
        # (item_get_slot, ":body_armor", ":item", dplmc_slot_item_body_armor),
        # (item_get_slot, ":leg_armor", ":item", dplmc_slot_item_leg_armor),
        (item_get_head_armor, ":head_armor", ":item"),
        (item_get_body_armor, ":body_armor", ":item"),
        (item_get_leg_armor, ":leg_armor", ":item"),
        (store_add, ":i_score", ":head_armor", ":body_armor"),
        (val_add, ":i_score", ":leg_armor"), # get total base score

        (try_begin),
          # (eq, ":imod", imod_plain),
          # (assign, ":imod_effect", 0),
        # (else_try),
          (eq, ":imod", imod_cracked),
          (assign, ":imod_effect", -4),
        (else_try),
          (eq, ":imod", imod_rusty),
          (assign, ":imod_effect", -3),
        (else_try),
          (eq, ":imod", imod_battered),
          (assign, ":imod_effect", -2),
        (else_try),
          (eq, ":imod", imod_crude),
          (assign, ":imod_effect", -1),
        (else_try),
          (eq, ":imod", imod_tattered),
          (assign, ":imod_effect", -3),
        (else_try),
          (eq, ":imod", imod_ragged),
          (assign, ":imod_effect", -2),
        (else_try),
          (eq, ":imod", imod_sturdy),
          (assign, ":imod_effect", 1),
        (else_try),
          (eq, ":imod", imod_thick),
          (assign, ":imod_effect", 2),
        (else_try),
          (eq, ":imod", imod_hardened),
          (assign, ":imod_effect", 3),
        (else_try),
          (eq, ":imod", imod_reinforced),
          (assign, ":imod_effect", 4),
        (else_try),
          (eq, ":imod", imod_lordly),
          (assign, ":imod_effect", 6),
        (try_end),

        (try_begin), # for armors have 2 or 3 defence of different part
          (neq, ":imod_effect", 0), # and item modifers that matter
          (assign, ":imod_effect_mul", 0),
          (try_begin), #do nothing if no armor part at all
            (gt, ":head_armor", 0),
            (store_add, ":temp_armor", ":head_armor", ":imod_effect"),
            (try_begin), #only calculate if imod degrades item's rating
              (gt, ":temp_armor", 0),
              (val_add, ":imod_effect_mul", 1),
            (else_try), #downgrade armor rating to 0 from bad armor instead of going negative
              (val_sub, ":i_score", ":head_armor"),
            (try_end),
          (try_end),
          (try_begin),
            (gt, ":body_armor", 0),
            (store_add, ":temp_armor", ":body_armor", ":imod_effect"),
            (try_begin),
              (gt, ":temp_armor", 0),
              (val_add, ":imod_effect_mul", 1),
            (else_try),
              (val_sub, ":i_score", ":body_armor"),
            (try_end),
          (try_end),
          (try_begin),
            (gt, ":leg_armor", 0),
            (store_add, ":temp_armor", ":leg_armor", ":imod_effect"),
            (try_begin),
              (gt, ":temp_armor", 0),
              (val_add, ":imod_effect_mul", 1),
            (else_try),
              (val_sub, ":i_score", ":leg_armor"),
            (try_end),
          (try_end),

          (val_mul, ":imod_effect", ":imod_effect_mul"),
          (val_add, ":i_score", ":imod_effect"),
        (try_end),
      (else_try),
        # weapon score = max(swing_damage , thrust_damage)
        (this_or_next|eq, ":type", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type", itp_type_two_handed_wpn),
        (this_or_next|eq, ":type", itp_type_bow),
        (this_or_next|eq, ":type", itp_type_crossbow),
        ##diplomacy start+ add extra types
        #(this_or_next|eq, ":type", itp_type_pistol),
        #(this_or_next|eq, ":type", itp_type_musket),
        ##diplomacy end+
        (eq, ":type", itp_type_polearm),
        (item_get_swing_damage, ":swing_damage", ":item"),
        (item_get_thrust_damage, ":thrust_damage", ":item"),
        (assign, reg1, ":swing_damage"), #sb : debug
        (assign, reg2, ":thrust_damage"), #sb : debug
        # (item_get_slot, ":swing_damage", ":item", dplmc_slot_item_swing_damage),
        # (item_get_slot, ":thrust_damage", ":item", dplmc_slot_item_thrust_damage),
        (val_mod, ":swing_damage", 256), # get actual damage value
        (val_mod, ":thrust_damage", 256),
        (assign, ":i_score", ":swing_damage"),
        (val_max, ":i_score", ":thrust_damage"),

        ##SB : get additional parameters
        (item_get_speed_rating, ":item_speed", ":item"),
        (item_get_weapon_length, ":item_length", ":item"),
        #shootspeed?

        (try_begin),
          # (eq, ":imod", imod_plain),
          # (assign, ":imod_effect", 0),
        # (else_try),
          (eq, ":imod", imod_cracked),
          (assign, ":imod_effect", -5),
        (else_try),
          (eq, ":imod", imod_rusty),
          (assign, ":imod_effect", -3),
        (else_try),
          (eq, ":imod", imod_bent),
          (assign, ":imod_effect", -3),
          (val_sub, ":item_speed", 3),
        (else_try),
          (eq, ":imod", imod_chipped),
          (assign, ":imod_effect", -1),
        (else_try), #SB : add fine
          (eq, ":imod", imod_fine),
          (assign, ":imod_effect", 1),
        (else_try),
          (eq, ":imod", imod_balanced),
          (assign, ":imod_effect", 3),
          (val_add, ":item_speed", 3),
        (else_try),
          (eq, ":imod", imod_tempered),
          (assign, ":imod_effect", 4),
        (else_try),
          (eq, ":imod", imod_masterwork),
          (assign, ":imod_effect", 5),
          (val_add, ":item_speed", 1),
        (else_try),
          (eq, ":imod", imod_heavy),
          (assign, ":imod_effect", 2),
          (val_sub, ":item_speed", 2),
        (else_try),
          (eq, ":imod", imod_strong),
          (assign, ":imod_effect", 3),
          (val_sub, ":item_speed", 3),
        (try_end),

        (val_add, ":i_score", ":imod_effect"),
        (try_begin), #try to pre-filter civilian weapons that are improvised from being looted (clubs, scythes, etc that should be passed over)
          (call_script, "script_cf_melee_weapon_is_civilian", ":item"),
          (val_div, ":i_score", 3),
        (try_end),
        (try_begin), #item_get_missile_speed is technically an important rating for ranged weapons, but we'll pretend NPCs can't math
          (this_or_next|is_between, ":type", itp_type_bow, itp_type_thrown),
          (is_between, ":type", itp_type_pistol, itp_type_bullets),
          (val_mul, ":i_score", ":item_speed"),
        (else_try), #assume base of 100 speed, 100 length
          (this_or_next|eq, ":type", itp_type_one_handed_wpn),
          (eq, ":type", itp_type_two_handed_wpn),
          (val_mul, ":item_length", ":item_speed"),
          (val_mul, ":i_score", ":item_length"),
        (else_try), #length priority over speed
          (eq, ":type", itp_type_polearm),
          (try_begin), #unless they're slashing
            (gt, ":thrust_damage", ":swing_damage"),
            (item_has_property, ":item", itp_couchable),
            # (item_has_property, ":item", itp_cant_use_on_horseback),
            (ge, ":item_length", dplmc_pike_length_cutoff),
            (val_sub, ":item_length", 50), #offset
            #no penalty for war spear range
            (val_max, ":item_length", 100),
            (val_mul, ":item_length", 4),
            #item speed rounded off when we couch
            (val_add, ":item_speed", 25),
            (val_div, ":item_speed", 10),
            # (val_mul, ":item_speed", 2),
          (try_end),
          (val_mul, ":item_length", ":item_speed"),
          (val_mul, ":i_score", ":item_length"),
        (try_end),
      (else_try),
        # ammo score = (thrust_damage + imod_effect)*2
        # a_large_bag will make score added by 1 to discriminate the same ammo with the plain modifier
        (this_or_next|eq, ":type", itp_type_arrows),
        (this_or_next|eq, ":type", itp_type_bolts),
        (eq, ":type", itp_type_thrown),
        (item_get_thrust_damage, ":thrust_damage", ":item"),
        (val_mod, ":thrust_damage", 256), # get actual damage value
        (store_add, ":i_score", ":thrust_damage", 3), # SB : make sure imods do not reduce damage to 0

        #imodbits_missile   = imodbit_bent | imodbit_large_bag
        #imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
        (try_begin),
          (eq, ":imod", imod_plain),
          (val_mul, ":i_score", 2),
        (else_try),
          (eq, ":imod", imod_large_bag),
          (val_mul, ":i_score", 2),
          (val_add, ":i_score", 1),
        (else_try),
          (eq, ":imod", imod_bent),
          (val_sub, ":i_score", 3),
          (val_mul, ":i_score", 2),
        (else_try),
          (eq, ":imod", imod_heavy),
          (val_add, ":i_score", 2),
          (val_mul, ":i_score", 2),
        (else_try),
          (eq, ":imod", imod_balanced),
          (val_add, ":i_score", 3),
          (val_mul, ":i_score", 2),
        (try_end),
      (try_end),

      (assign, reg0, ":i_score"),
    ]),
  #### Autoloot improved by rubik end

###################
# Used in conversations

("dplmc_print_wpn_upgrades_to_s0", [
	(store_script_param_1, ":troop"),

	(str_store_string, s0, "str_empty_string"),
	(troop_get_slot, ":upg", ":troop", dplmc_slot_upgrade_wpn_0),
	(troop_get_inventory_slot, ":item", ":troop", 0),
	(try_begin),
		(ge, ":item", 0),
		(str_store_item_name, s10, ":item"),
	(else_try),
		(str_store_string, s10, "str_dplmc_none"),
	(try_end),
	(val_add, ":upg", "str_dplmc_hero_wpn_slot_none"),
	(str_store_string, s1, ":upg"),
	(str_store_string, s0, "@{s0}^{s1}"),
	(troop_get_slot, ":upg", ":troop", dplmc_slot_upgrade_wpn_1),
	(troop_get_inventory_slot, ":item", ":troop", 1),
	(try_begin),
		(ge, ":item", 0),
		(str_store_item_name, s10, ":item"),
	(else_try),
		(str_store_string, s10, "str_dplmc_none"),
	(try_end),
	(val_add, ":upg", "str_dplmc_hero_wpn_slot_none"),
	(str_store_string, s1, ":upg"),
	(str_store_string, s0, "@{s0}^{s1}"),
	(troop_get_slot, ":upg", ":troop", dplmc_slot_upgrade_wpn_2),
	(troop_get_inventory_slot, ":item", ":troop", 2),
	(try_begin),
		(ge, ":item", 0),
		(str_store_item_name, s10, ":item"),
	(else_try),
		(str_store_string, s10, "str_dplmc_none"),
	(try_end),
	(val_add, ":upg", "str_dplmc_hero_wpn_slot_none"),
	(str_store_string, s1, ":upg"),
	(str_store_string, s0, "@{s0}^{s1}"),
	(troop_get_slot, ":upg", ":troop", dplmc_slot_upgrade_wpn_3),
	(troop_get_inventory_slot, ":item", ":troop", 3),
	(try_begin),
		(ge, ":item", 0),
		(str_store_item_name, s10, ":item"),
	(else_try),
		(str_store_string, s10, "str_dplmc_none"),
	(try_end),
	(val_add, ":upg", "str_dplmc_hero_wpn_slot_none"),
	(str_store_string, s1, ":upg"),
	(str_store_string, s0, "@{s0}^{s1}"),
]),

################################
# Copy this troop's upgrade options to everyone

# ("dplmc_copy_upgrade_to_all_heroes", [
	# (store_script_param_1, ":troop"),

	# (troop_get_slot,":upg_armor", ":troop",dplmc_slot_upgrade_armor),
	# (troop_get_slot,":upg_horse",":troop",dplmc_slot_upgrade_horse),
	# (troop_get_slot,":upg_wpn0",":troop",dplmc_slot_upgrade_wpn_0),
	# (troop_get_slot,":upg_wpn1",":troop",dplmc_slot_upgrade_wpn_1),
	# (troop_get_slot,":upg_wpn2",":troop",dplmc_slot_upgrade_wpn_2),
	# (troop_get_slot,":upg_wpn3",":troop",dplmc_slot_upgrade_wpn_3),

	# (try_for_range, ":hero", companions_begin, companions_end),
		# (troop_set_slot,":hero",dplmc_slot_upgrade_armor,":upg_armor"),
		# (troop_set_slot,":hero",dplmc_slot_upgrade_horse,":upg_horse"),
		# (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_0,":upg_wpn0"),
		# (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_1,":upg_wpn1"),
		# (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_2,":upg_wpn2"),
		# (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_3,":upg_wpn3"),
	# (try_end),
# ]),

####################################
# Let each hero loot from the pool

("dplmc_auto_loot_all", [
    (store_script_param_1, ":pool_troop"),
    (store_script_param_2, ":sreg"),
    # for all the NPCs, in order of party listing

    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
        (call_script, "script_cf_troop_can_autoloot", ":this_hero"),
        #SB : show strings for first iteration
        (call_script, "script_dplmc_auto_loot_troop", ":this_hero", ":pool_troop", ":sreg"),
        (val_add, ":sreg", 1),
    (try_end),

    #SB : get starting index once again
    (store_script_param_2, ":sreg"),
    # pick up any discards and format string
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
        (call_script, "script_cf_troop_can_autoloot", ":this_hero"),
        (try_begin), #if first iteration picked up nothing
          (str_is_empty, ":sreg"),
          (call_script, "script_dplmc_auto_loot_troop", ":this_hero", ":pool_troop", ":sreg"),
        (else_try), #do not overwrite string from first iteration
          (call_script, "script_dplmc_auto_loot_troop", ":this_hero", ":pool_troop", -1),
        (try_end),
        (try_begin), #skip the first one
          (gt, ":sreg", dplmc_loot_string),
          (neg|str_is_empty, ":sreg"), # in case second hasn't picked up changes either
          (str_store_string_reg, s1, ":sreg"),
          (str_store_string_reg, s0, dplmc_loot_string),
          (str_store_string, dplmc_loot_string, "str_dplmc_s0_newline_s1"),
        (try_end),
        (val_add, ":sreg", 1), #go to next string register
    (try_end),

    #Done. Now sort the remainder
    (troop_sort_inventory, ":pool_troop"),

]),


####################################
# let this troop take its pick from the loot pool

("dplmc_auto_loot_troop", [
	# (try_begin),
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		(store_script_param, ":sreg", 3), #SB : new param for storing changes

		(troop_get_slot,":upg_armor", ":troop",dplmc_slot_upgrade_armor),
		(troop_get_slot,":upg_horses",":troop",dplmc_slot_upgrade_horse),

		# dump whatever rubbish is in the main inventory
		(troop_get_inventory_capacity, ":inv_cap", ":troop"),
		(try_for_range, ":i_slot", dplmc_ek_alt_items_end, ":inv_cap"), #SB raise from 10, skip over civilian stuff
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
			(troop_add_item, ":pool", ":item", ":imod"), #put it back in the pool
			(troop_set_inventory_slot, ":troop", ":i_slot", -1), # delete it
		(try_end),

        #clear slot
        # (try_for_range, ":slot_no", dplmc_slot_upgrade_wpn_0, dplmc_slot_upgrade_wpn_3 + 1),
          # (troop_slot_eq, ":troop", ":slot_no", 0), #0 is keep
          # (troop_set_slot, "trp_heroes_end", ":slot_no", 999999),
        # (else_try), #otherwise we reset to default
          # (troop_set_slot, "trp_heroes_end", ":slot_no", -1),
        # (try_end),

        #SB : loop, calculate current item's score
        # (assign, ":slot_no", dplmc_slot_upgrade_wpn_0 - 1),
        (try_for_range, ":item_slot", ek_item_0, ek_head),
          #SB : clear the pool troop's ek_slots
          (troop_set_inventory_slot, ":pool", ":item_slot", -1), #delete it
          (store_add, ":slot_no", dplmc_slot_upgrade_wpn_0, ":item_slot"), #pre-increment
          (troop_get_slot, ":item_preference", ":troop", ":slot_no"),
          (gt, ":item_preference", 0), #0 is keep
          (troop_get_inventory_slot, ":item", ":troop", ":item_slot"),
          (ge, ":item", 0), #initial item check
          (troop_get_inventory_slot_modifier, ":imod", ":troop", ":item_slot"),

          (try_begin),
            (store_mod, ":item_type", ":item_preference", meta_itp_mask),
            (item_get_type, ":itp", ":item"),
            (neq, ":itp", ":item_type"),
            (troop_set_inventory_slot, ":troop", ":item_slot", -1), #delete it
            (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
            (assign, ":item", -1), #so we fail this loop
          (try_end),
          (ge, ":item", 0),
          #SB : cache the original equipment to see changes
          (troop_set_inventory_slot, ":pool", ":item_slot", ":item"),
          (troop_set_inventory_slot_modifier, ":pool", ":item_slot", ":imod"),

          (call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
          (assign, ":cur_value", reg0),
          #check to see whether damage is preferred
          (try_begin),
            (call_script, "script_cf_item_type_has_advanced_autoloot", ":item_type"),
            (store_div, ":dmg_type", ":item_preference", meta_dmg_mask),
            (neq, ":dmg_type", 0),
            (item_get_swing_damage, ":swing_damage", ":item"),
            (item_get_thrust_damage, ":thrust_damage", ":item"),
            (try_begin),
              (ge, ":swing_damage", ":thrust_damage"),
              (item_get_swing_damage_type, ":item_dmg_type", ":item"),
            (else_try),
              (lt, ":swing_damage", ":thrust_damage"),
              (item_get_thrust_damage_type, ":item_dmg_type", ":item"),
            (try_end),
            #check if it matches preference
            (val_add, ":item_dmg_type", 1),
            (eq, ":dmg_type", ":item_dmg_type"),
            (val_mul, ":cur_value", 4),
          (try_end),
          (troop_set_slot, "trp_heroes_end", ":slot_no", ":cur_value"),
        (else_try),
          (eq, ":item_preference", 0), #0 is keep
          (troop_set_slot, "trp_heroes_end", ":slot_no", 999999),
        (else_try), #whether no item or discarded
          (lt, ":item", 0),
          (troop_set_slot, "trp_heroes_end", ":slot_no", 0),
        (try_end),

        # (try_for_range, ":slot_no", dplmc_slot_upgrade_wpn_0, dplmc_slot_upgrade_wpn_3 + 1),
          # (troop_get_slot, reg0, ":troop", ":slot_no"),
          # (troop_get_slot, reg1, "trp_heroes_end", ":slot_no"),
          # (store_sub, reg2, ":slot_no", dplmc_slot_upgrade_wpn_0),
          # (troop_get_inventory_slot, ":item", ":troop", reg2),
          # (try_begin),
            # (eq, ":item", -1),
            # (str_store_string, s1, "str_dplmc_none"),
          # (else_try),
            # (str_store_item_name, s1, ":item"),
          # (try_end),

          # (display_message, "@upgrading slot {reg2} with {reg0}, cur score for {s1}: {reg1}"),
        # (try_end),

		(try_for_range, ":i_slot", ek_head, ek_food),
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
            (troop_set_inventory_slot, ":pool", ":i_slot", -1), #delete it
			(ge, ":item", 0),
            (troop_set_inventory_slot, ":pool", ":i_slot", ":item"), #store it
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
            (troop_set_inventory_slot_modifier, ":pool", ":i_slot", ":imod"), #store it
			(try_begin),
				(neq, ":upg_armor", 0), # we're upgrading armors
				(is_between, ":i_slot", ek_head, ek_horse), # it's an armor slot
				(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
				(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(else_try),
				(neq, ":upg_horses", 0), # we're upgrading horses
				(eq, ":i_slot", ek_horse), # it's a horse slot
				(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
				(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(try_end),
		(try_end),

		# clear best matches
		(assign, ":best_helmet_slot", -1),
		(assign, ":best_helmet_val", 0),
		(assign, ":best_body_slot", -1),
		(assign, ":best_body_val", 0),
		(assign, ":best_boots_slot", -1),
		(assign, ":best_boots_val", 0),
		(assign, ":best_gloves_slot", -1),
		(assign, ":best_gloves_val", 0),
		(assign, ":best_horse_slot", -1),
		(assign, ":best_horse_val", 0),

		# Now search through the pool for the best items
		(troop_get_inventory_capacity, ":inv_cap", ":pool"),
		(try_for_range, ":i_slot", ek_food + 1, ":inv_cap"), #SB: skip cached items
			(troop_get_inventory_slot, ":item", ":pool", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":i_slot"),
			(call_script, "script_dplmc_troop_can_use_item", ":troop", ":item", ":imod"),
			(eq, reg0, 1), # can use
			#(call_script, "script_get_item_value_with_imod", ":item", ":imod"),  # use the following instead

			#### Autoloot improved by rubik begin
			# get item_score instead of price
			(call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
			#### Autoloot improved by rubik end
			(assign, ":score", reg0),
			(item_get_type, ":item_type", ":item"),

			(try_begin),
				(eq, ":item_type", itp_type_horse), #it's a horse
				(eq, ":upg_horses", 1), # we're upgrading horses
				(gt, ":score", ":best_horse_val"),
				(assign, ":best_horse_slot", ":i_slot"),
				(assign, ":best_horse_val", ":score"),
			(else_try), #SB : move armor checks here
				(is_between, ":item_type", itp_type_head_armor, itp_type_hand_armor + 1), # we're checking armor
				(eq, ":upg_armor", 1), # we're upgrading armor
				(try_begin),
					(eq, ":item_type", itp_type_head_armor),
					(gt, ":score", ":best_helmet_val"),
					(assign, ":best_helmet_slot", ":i_slot"),
					(assign, ":best_helmet_val", ":score"),
				(else_try),
					(eq, ":item_type", itp_type_body_armor),
					(gt, ":score", ":best_body_val"),
					(assign, ":best_body_slot", ":i_slot"),
					(assign, ":best_body_val", ":score"),
				(else_try),
					(eq, ":item_type", itp_type_foot_armor),
					(gt, ":score", ":best_boots_val"),
					(assign, ":best_boots_slot", ":i_slot"),
					(assign, ":best_boots_val", ":score"),
				(else_try),
					(eq, ":item_type", itp_type_hand_armor),
					(gt, ":score", ":best_gloves_val"),
					(assign, ":best_gloves_slot", ":i_slot"),
					(assign, ":best_gloves_val", ":score"),
				(try_end),
            (else_try), #SB : move weapon checks back here
              (assign, ":limit", dplmc_slot_upgrade_wpn_3 + 1),
              (try_begin), #check for denying use on horseback
                  (this_or_next|gt, ":best_horse_val", 0),
                  (eq, ":upg_horses", 1), # we're upgrading horses
                  (this_or_next|item_has_property, ":item", itp_cant_use_on_horseback),
                  (this_or_next|item_has_property, ":item", itp_cant_reload_on_horseback),
                  (item_has_property, ":item", itp_cant_reload_while_moving_mounted),
                  (assign, ":limit", 0),
              (try_end),
              (try_for_range, ":slot_no", dplmc_slot_upgrade_wpn_0, ":limit"),
                (troop_get_slot, ":item_preference", ":troop", ":slot_no"),
                (neq, ":item_preference", 0), #not keep current
                (store_div, ":damage_type", ":item_preference", meta_dmg_mask),
                (val_mod, ":item_preference", meta_dmg_mask), #get the itp + meta
                (call_script, "script_item_get_type_aux", ":item"),
                (this_or_next|eq, ":item_preference", reg0), #either same meta-type
                (eq, ":item_preference", ":item_type"), #or matching base itp

                #check to see whether damage is preferred
                (try_begin),
                  (neq, ":damage_type", 0),
                  (item_get_swing_damage, ":swing_damage", ":item"),
                  (item_get_thrust_damage, ":thrust_damage", ":item"),
                  (try_begin),
                    (ge, ":swing_damage", ":thrust_damage"),
                    (item_get_swing_damage_type, ":item_dmg_type", ":item"),
                  (else_try),
                    (lt, ":swing_damage", ":thrust_damage"),
                    (item_get_thrust_damage_type, ":item_dmg_type", ":item"),
                  (try_end),
                  #check if it matches preference
                  (val_add, ":item_dmg_type", 1),
                  (eq, ":damage_type", ":item_dmg_type"),
                  (val_mul, ":score", 4),
                (try_end),
                #if current score is not ge, replace item and score
                (neg|troop_slot_ge, "trp_heroes_end", ":slot_no", ":score"),
                (troop_set_slot, "trp_heroes_end", ":slot_no", ":score"),
                (assign, ":limit", -1), #loop break
                (store_sub, ":item_slot", ":slot_no", dplmc_slot_upgrade_wpn_0), #ek item slots
                (troop_get_inventory_slot, ":item_no", ":troop", ":item_slot"),
                (try_begin),
                  (eq, ":item_no", -1),
                  (troop_set_inventory_slot, ":pool", ":i_slot", -1),
                (else_try), #replace into pool
                  (troop_get_inventory_slot_modifier, ":imod_no", ":troop", ":item_slot"),
                  (troop_set_inventory_slot, ":pool", ":i_slot", ":item_no"),
                  (troop_set_inventory_slot_modifier, ":pool", ":i_slot", ":imod_no"),
                (try_end),
                (troop_set_inventory_slot, ":troop", ":item_slot", ":item"),
                (troop_set_inventory_slot_modifier, ":troop", ":item_slot", ":imod"),
                # (try_begin),
                  # (str_store_item_name, s1, ":item"),
                  # (try_begin),
                    # (eq, ":item_no", -1),
                    # (str_store_string, s2, "str_dplmc_none"),
                  # (else_try),
                    # (str_store_item_name, s2, ":item_no"),
                  # (try_end),
                  # (assign, reg1, ":score"),
                  # (display_message, "@{s1} better than {s2}, score of {reg1}"),
                # (try_end),
              (try_end),
            (try_end),
        (try_end),

		# Now we know which ones are the best. Give them to the troop.
		(try_begin),
			(assign, ":best_slot", ":best_helmet_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_head, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_head, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_body_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_body, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_body, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_boots_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_foot, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_foot, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_gloves_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_gloves, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_gloves, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_horse_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_horse, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_horse, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		# (try_for_range, ":i_slot", ek_item_0, ek_head),
			# (store_add, ":trp_slot", ":i_slot", dplmc_slot_upgrade_wpn_0),
			# (troop_get_slot, ":type", ":troop", ":trp_slot"),
			# (gt, ":type", 0), #we're upgrading for this slot
			# (call_script, "script_dplmc_scan_for_best_item_of_type", ":pool", ":type", ":troop"), #search for the best
			# (assign, ":best_slot", reg0),
			# (neq, ":best_slot", -1), #got something
			# (troop_get_inventory_slot, ":item", ":pool", ":best_slot"), #get it
			# (ge, ":item", 0),
			# (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			# (troop_set_inventory_slot, ":pool", ":best_slot", -1), #remove from pool
			# (troop_set_inventory_slot, ":troop", ":i_slot", ":item"), #add to slot
			# (troop_set_inventory_slot_modifier, ":troop", ":i_slot", ":imod"),
		# (try_end),

        #SB : string storage
        (try_begin),
          (neq, ":sreg", -1),
          (str_store_troop_name, ":sreg", ":troop"),
          (assign, ":num_changes", 0),
          (assign, ":last_change", 0),
          #three cases : discarded item -1, no change 0, change 1 (upgraded/swapped depending on item flags)
          (try_for_range, ":i_slot", ek_item_0, ek_food),
            (troop_get_inventory_slot, ":old_item", ":pool", ":i_slot"),
            (troop_get_inventory_slot, ":new_item", ":troop", ":i_slot"),
            (try_begin),
              (gt, ":old_item", -1),
              (troop_get_inventory_slot_modifier, ":old_imod", ":pool", ":i_slot"),
              (store_add, ":imod_no", ":old_imod", "str_imod_plain"),
              # (str_store_string, s10, ":imod_no"),
              # (str_store_item_name, s20, ":old_item"),
              # (display_message, "@old:{s10}{s20}"),
            (else_try),
              (assign, ":old_imod", imod_plain),
            (try_end),
            (try_begin),
              (gt, ":new_item", -1),
              (troop_get_inventory_slot_modifier, ":new_imod", ":troop", ":i_slot"),
              (store_add, ":imod_no", ":new_imod", "str_imod_plain"),
              # (str_store_string, s10, ":imod_no"),
              # (str_store_item_name, s20, ":new_item"),
              # (display_message, "@new:{s10}{s20}"),
            (else_try),
              (assign, ":new_imod", imod_plain),
            (try_end),

            # #placeholder swap strings
            # (str_clear, s0), #sreg
            # (str_clear, s1), #new string
            # (str_clear, s10), #imod
            # (str_clear, s20), #item

            (try_begin), #keep current
              (is_between, ":i_slot", ek_item_0, ek_head),
              (store_add, ":upgrade_slot", ":i_slot", dplmc_slot_upgrade_wpn_0),
              (troop_slot_eq, ":troop", ":upgrade_slot", 0),
              (assign, ":item_changed", 0),
            (else_try), #same
              (eq, ":new_item", ":old_item"),
              (eq, ":old_imod", ":new_imod"),
              (assign, ":item_changed", 0),
            (else_try), #discarded
              (eq, ":new_item", -1),
              (gt, ":old_item", -1),
              (assign, ":item_changed", 2),
              (assign, ":item_no", ":old_item"),
              (assign, ":imod_no", ":old_imod"),
            (else_try), #swapped/equipped
              (gt, ":new_item", -1),
              (assign, ":item_changed", 1),
              (assign, ":item_no", ":new_item"),
              (assign, ":imod_no", ":new_imod"),
            (try_end),

            #build string
            (try_begin),
              (gt, ":item_changed", 0),
              (val_add, ":imod_no", "str_imod_plain"),
              (str_store_string, s10, ":imod_no"), #this comes with a space
              (str_store_item_name, s20, ":item_no"),

              (try_begin),
                (neq, ":last_change", 1),
                (eq, ":item_changed", 1),
                (str_store_string, s1, "@equipped {s10}{s20}"),
              (else_try),
                (neq, ":last_change", 2),
                (eq, ":item_changed", 2),
                (str_store_string, s1, "@discarded {s10}{s20}"),
              (else_try), #same as before, no need to qualify
                (str_store_string, s1, "@{s10}{s20}"),
              (try_end),
              (str_store_string_reg, s0, ":sreg"),
              (try_begin), #no comma for first part
                (eq, ":num_changes", 0),
                (str_store_string, ":sreg", "str_s0_s1"),
              (else_try),
                (str_store_string, ":sreg", "str_dplmc_s0_comma_s1"),
              (try_end),
              # (assign, reg1, ":num_changes"),
              # (display_message, "@{reg1} : {s1}"),
              (val_add, ":num_changes", ":item_changed"),
              (assign, ":last_change", ":item_changed"),
            (try_end),
          (try_end),
          (try_begin), #discard if we didn't touch the inventory at all
            (le, ":num_changes", 0), #this is a flag, not a count
            (str_clear, ":sreg"),
          (try_end),
        (try_end),

    # (try_end),
]),

#######################
# Search for the most expensive item of a specified type

##diplomacy start+
#"script_dplmc_scan_for_best_item_of_type"
#
#INPUT:
#   arg1 :troop
#   arg2 :item_type
#   arg3 :troop_using
#
#OUTPUT:
#   reg0 index of best item (-1 if not found)
##diplomacy end+
("dplmc_scan_for_best_item_of_type", [
	(store_script_param, ":troop",1),
	(store_script_param, ":item_type",2),
	(store_script_param, ":troop_using", 3),


    #SB : parse damage type and meta type (if any)
    # (store_div, ":dmg_type", ":item_type", meta_dmg_mask),
    (store_mod, ":meta_type", ":item_type", meta_dmg_mask), #use this instead
    (store_mod, ":item_type", ":meta_type", meta_itp_mask), #base type

    (assign, ":best_slot", -1),
    (assign, ":best_value", -1),
    # iterate through the list of items
    (troop_get_inventory_capacity, ":inv_cap", ":troop"),
    (try_for_range, ":i_slot", 0, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
        (ge, ":item", 0),
        (troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
        #(item_get_type, ":this_item_type", ":item"),  use the following instead

        # #### Autoloot improved by rubik begin
        # (try_begin),
            # # (item_slot_eq, ":item", dplmc_slot_two_handed_one_handed, 1),
            # (item_has_property, ":item", itp_type_two_handed_wpn),
            # (neg|item_has_property, ":item", itp_two_handed),
            # (assign, ":this_item_type", 11), # type 11 = two-handed/one-handed
        # (else_try),
            # (item_get_type, ":this_item_type", ":item"),
        # (try_end),
        # #### Autoloot improved by rubik end
        (call_script, "script_item_get_type_aux", ":item"), #SB : compare metatype
        (eq, ":meta_type", reg0), # it's one of the kind we're looking for (meta-type holds itp if none exists)
        (call_script, "script_dplmc_troop_can_use_item", ":troop_using", ":item", ":imod"),
        (eq, reg0, 1), # can use
        #(call_script, "script_get_item_value_with_imod", ":item", ":imod"),  # use the following instead

        #### Autoloot improved by rubik begin
        # get item_score instead of price
        (call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
        #### Autoloot improved by rubik end
        (assign, ":cur_value", reg0),
        #SB : adjust value here for damage preference
        # (try_begin),
          # (call_script, "script_cf_item_type_has_advanced_autoloot", ":item_type"),
          # (item_get_swing_damage, ":swing_damage", ":item"),
          # (item_get_thrust_damage, ":thrust_damage", ":item"),
          # (try_begin),
            # (ge, ":swing_damage", ":thrust_damage"),
            # (item_get_swing_damage_type, ":item_dmg_type", ":item"),
          # (else_try),
            # (lt, ":swing_damage", ":thrust_damage"),
            # (item_get_thrust_damage_type, ":item_dmg_type", ":item"),
          # (try_end),
          # #check if it matches preference
          # (eq, ":dmg_type", ":item_dmg_type"),
          # (val_mul, ":cur_value", 3),
        # (try_end),
        (gt, ":cur_value", ":best_value"), # best one we've seen yet
        (assign, ":best_slot", ":i_slot"),
        (assign, ":best_value", ":cur_value"),
    (try_end),



    # return the slot of the best one
    (assign, reg0, ":best_slot"),
]),

##diplomacy start+
#"script_dplmc_count_better_items_of_same_type"
#
#INPUT:
#   arg1 :inventory_troop
#   arg2 :item
#   arg2 :item_imod
#   arg3 :troop_using
#
#OUTPUT:
#   reg0 number of items of same type
("dplmc_count_better_items_of_same_type", [
	(store_script_param, ":inventory_troop",1),
	(store_script_param, ":base_item",2),
	(store_script_param, ":base_imod",3),
	(store_script_param, ":troop_using", 4),

	(assign, ":number_better_of_type", 0),
	#(assign, ":total_items_of_type", 0),

	# (item_get_type, ":main_item_type", ":base_item"),
	# (try_begin),
		# (item_has_property, ":item", itp_type_two_handed_wpn),
		# (neg|item_has_property, ":item", itp_two_handed),
		# (assign, ":main_item_type", 11), # type 11 = two-handed/one-handed
	# (try_end),
    #SB : metatype
    (call_script, "script_item_get_type_aux", ":base_item"),
    (assign, ":main_item_type", reg0),

	(call_script, "script_dplmc_get_item_score_with_imod", ":base_item", ":base_imod"),
	(assign, ":primary_score", reg0),

	(call_script, "script_dplmc_troop_can_use_item", ":troop_using", ":base_item", ":base_imod"),
	(assign, ":can_use", 1),
	(try_begin),
		(neq, reg0, 1),
		(assign, ":primary_score", -1000),
		(assign, ":can_use", 0),
	(try_end),
	(assign, ":exact_matches_found", 0),

	(troop_get_inventory_capacity, ":inv_cap", ":inventory_troop"),
	(try_for_range, ":i_slot", 0, ":inv_cap"),
		(troop_get_inventory_slot, ":item", ":inventory_troop", ":i_slot"),
		(ge, ":item", 0),
        # SB : metatype
        (call_script, "script_item_get_type_aux", ":item"),
		(eq, ":main_item_type", reg0),
		#(val_add, ":total_items_of_type", 1),
		(troop_get_inventory_slot_modifier, ":imod", ":inventory_troop", ":i_slot"),
		(call_script, "script_dplmc_troop_can_use_item", ":troop_using", ":item", ":imod"),
		(this_or_next|eq, ":can_use", 0),
			(ge, reg0, 1),
		(try_begin),
			(eq, ":item", ":base_item"),
			(eq, ":imod", ":base_imod"),
			(val_add, ":exact_matches_found", 1),
		(try_end),
		(this_or_next|neq, ":item", ":base_item"),
		(this_or_next|neq, ":imod", ":base_imod"),
			(ge, ":exact_matches_found", 2),
		(call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
		(ge, reg0, ":primary_score"),#deliberately ge instead of gt because of what I want this for
		(val_add, ":number_better_of_type", 1),
	(try_end),

	(assign, reg0, ":number_better_of_type"),
	#(assign, reg1, ":total_items_of_type"),
]),
##diplomacy end+

("dplmc_copy_upgrade_to_all_heroes",
  [
    (store_script_param_1, ":troop"),
    (store_script_param_2, ":type"),

    (try_begin),
      (eq, ":type", dplmc_wpn_setting_1),
      (troop_get_slot,":upg_wpn0", ":troop",dplmc_slot_upgrade_wpn_0),
      (troop_get_slot,":upg_wpn1", ":troop",dplmc_slot_upgrade_wpn_1),
      (troop_get_slot,":upg_wpn2", ":troop",dplmc_slot_upgrade_wpn_2),
      (troop_get_slot,":upg_wpn3", ":troop",dplmc_slot_upgrade_wpn_3),
      (try_for_range, ":hero", companions_begin, companions_end),
        (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_0,":upg_wpn0"),
        (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_1,":upg_wpn1"),
        (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_2,":upg_wpn2"),
        (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_3,":upg_wpn3"),
      (try_end),
    (else_try),
      (eq, ":type", dplmc_armor_setting),
      (troop_get_slot,":upg_armor", ":troop",dplmc_slot_upgrade_armor),
      (try_for_range, ":hero", companions_begin, companions_end),
        (troop_set_slot,":hero",dplmc_slot_upgrade_armor,":upg_armor"),
      (try_end),
    (else_try),
      (eq, ":type", dplmc_horse_setting),
      (troop_get_slot,":upg_horse", ":troop",dplmc_slot_upgrade_horse),
      (try_for_range, ":hero", companions_begin, companions_end),
        (troop_set_slot,":hero",dplmc_slot_upgrade_horse,":upg_horse"),
      (try_end),
    (try_end),
  ]),

  ("dplmc_get_current_item_for_autoloot",
  [
    (store_script_param_1, ":slot_no"),

    #(try_begin),
      (assign, ":dest_slot", ":slot_no"),
      (troop_get_inventory_slot, ":item", "$temp", ":dest_slot"),
    #(else_try),
    #  (store_sub, ":dest_slot", "$temp", companions_begin),
    #  (val_mul, ":dest_slot", 4),
    #  (val_add, ":dest_slot", 10),
    #  (val_add, ":dest_slot", ":slot_no"),
    #  (troop_get_inventory_slot, ":item", "trp_merchants_end", ":dest_slot"),
    #(try_end),
    (try_begin),
      (ge, ":item", 0),
      (str_store_item_name, s10, ":item"),
    (else_try),
      (str_store_string, s10, "str_dplmc_none"),
    (try_end),
  ]),

  ("dplmc_get_troop_max_hp",
   [
    (store_script_param_1, ":troop"),

    (store_skill_level, ":skill", skl_ironflesh, ":troop"),
    (store_attribute_level, ":attrib", ":troop", ca_strength),
    (val_mul, ":skill", 2),
    (val_add, ":skill", ":attrib"),
    (val_add, ":skill", 35),
    (assign, reg0, ":skill"),
  ]),
  #cc end

  ("dplmc_describe_prosperity_to_s4",
    [
      (store_script_param_1, ":center_no"),

      (str_store_party_name, s60,":center_no"),
      (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
      (str_store_string, s4, "str_empty_string"),
      (try_begin),
        (is_between, ":center_no", towns_begin, towns_end),
        (try_begin),
          (eq, ":prosperity", 0),
          (str_store_string, s4, "str_town_prosperity_0"),
        (else_try),
          (is_between, ":prosperity", 1, 11),
          (str_store_string, s4, "str_town_prosperity_10"),
        (else_try),
          (is_between, ":prosperity", 11, 21),
          (str_store_string, s4, "str_town_prosperity_20"),
        (else_try),
          (is_between, ":prosperity", 21, 31),
          (str_store_string, s4, "str_town_prosperity_30"),
        (else_try),
          (is_between, ":prosperity", 31, 41),
          (str_store_string, s4, "str_town_prosperity_40"),
        (else_try),
          (is_between, ":prosperity", 41, 51),
          (str_store_string, s4, "str_town_prosperity_50"),
        (else_try),
          (is_between, ":prosperity", 51, 61),
          (str_store_string, s4, "str_town_prosperity_60"),
        (else_try),
          (is_between, ":prosperity", 61, 71),
          (str_store_string, s4, "str_town_prosperity_70"),
        (else_try),
          (is_between, ":prosperity", 71, 81),
          (str_store_string, s4, "str_town_prosperity_80"),
        (else_try),
          (is_between, ":prosperity", 81, 91),
          (str_store_string, s4, "str_town_prosperity_90"),
        (else_try),
          (is_between, ":prosperity", 91, 101),
          (str_store_string, s4, "str_town_prosperity_100"),
        (try_end),
      (else_try),
        (is_between, ":center_no", villages_begin, villages_end),
        (try_begin),
          (eq, ":prosperity", 0),
          (str_store_string, s4, "str_village_prosperity_0"),
        (else_try),
          (is_between, ":prosperity", 1, 11),
          (str_store_string, s4, "str_village_prosperity_10"),
        (else_try),
          (is_between, ":prosperity", 11, 21),
          (str_store_string, s4, "str_village_prosperity_20"),
        (else_try),
          (is_between, ":prosperity", 21, 31),
          (str_store_string, s4, "str_village_prosperity_30"),
        (else_try),
          (is_between, ":prosperity", 31, 41),
          (str_store_string, s4, "str_village_prosperity_40"),
        (else_try),
          (is_between, ":prosperity", 41, 51),
          (str_store_string, s4, "str_village_prosperity_50"),
        (else_try),
          (is_between, ":prosperity", 51, 61),
          (str_store_string, s4, "str_village_prosperity_60"),
        (else_try),
          (is_between, ":prosperity", 61, 71),
          (str_store_string, s4, "str_village_prosperity_70"),
        (else_try),
          (is_between, ":prosperity", 71, 81),
          (str_store_string, s4, "str_village_prosperity_80"),
        (else_try),
          (is_between, ":prosperity", 81, 91),
          (str_store_string, s4, "str_village_prosperity_90"),
        (else_try),
          (is_between, ":prosperity", 91, 101),
          (str_store_string, s4, "str_village_prosperity_100"),
        (try_end),
      (try_end),
        ]),

  ("dplmc_pay_into_treasury",
    [
      (store_script_param_1, ":amount"),
      (troop_add_gold, "trp_household_possessions", ":amount"),
      (assign, reg0, ":amount"),
      (play_sound, "snd_money_received"),
      (display_message, "@{reg0} denars added to treasury."),
  ]),

  ("dplmc_withdraw_from_treasury",
    [
      (store_script_param_1, ":amount"),
      (troop_remove_gold, "trp_household_possessions", ":amount"),
      (assign, reg0, ":amount"),
      (play_sound, "snd_money_paid"),
      (display_message, "@{reg0} denars removed from treasury."),
  ]),

  ("dplmc_describe_tax_rate_to_s50",
    [
      (store_script_param_1, ":tax_rate"),
      (val_div, ":tax_rate", 25),
      (store_add, ":str_id","str_dplmc_tax_normal", ":tax_rate"),
      (str_store_string, s50, ":str_id"),
  ]),


  ("dplmc_player_troops_leave",
   [
    (store_script_param_1, ":percent"),

    (try_begin),#debug
     (eq, "$cheat_mode", 1),
     (assign, reg0, ":percent"),
     (display_message, "@{!}DEBUG : removing player troops: {reg0}%"),
    (try_end),

    (assign, ":deserters", 0),
    (try_for_parties, ":party_no"),
      (assign, ":remove_troops", 0),
      (try_begin),
        (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
        (party_slot_eq, ":party_no", slot_party_type, spt_castle),
        (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
        (assign, ":remove_troops", 1),
      (else_try),
         (eq, "p_main_party", ":party_no"),
         (assign, ":remove_troops", 1),
      (try_end),

      (eq, ":remove_troops", 1),
      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
        (val_mul, ":stack_size", ":percent"),
        (val_div, ":stack_size", 100),
        (party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
        (party_remove_members, ":party_no", ":troop_id", ":stack_size"),
        (val_add, ":deserters", ":stack_size"),
      (try_end),
    (try_end),
    (assign, reg0, ":deserters"),
   ]
  ),

  ("dplmc_get_item_buy_price_factor",
    [
	##nested diplomacy start+
    #(store_script_param_1, ":item_kind_id"),
    #(store_script_param_2, ":center_no"),
	#Add two parameters
	(store_script_param, ":item_kind_id", 1),
	(store_script_param, ":center_no", 2),
	(store_script_param, ":customer_no", 3),
	(store_script_param, ":merchant_no", 4),
	##nested diplomacy start+
    (assign, ":price_factor", 100),

	##nested diplomacy start+
    #(call_script, "script_get_trade_penalty", ":item_kind_id"),
	(call_script, "script_dplmc_get_trade_penalty", ":item_kind_id", ":center_no", ":customer_no", ":merchant_no"),
	##nested diplomacy end+
    (assign, ":trade_penalty", reg0),

    (try_begin),
	  ##nested diplomacy start+
	  (gt, ":center_no", 0),
  	  (this_or_next|is_between, ":center_no", centers_begin, centers_end),
		(party_is_active, ":center_no"),

	  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
	  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
	  ##nested diplomacy end+
      (is_between, ":center_no", centers_begin, centers_end),
      (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
      (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
      (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
      (party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),

      (try_begin),
		##nested diplomacy start+
		#OLD:
        #(is_between, ":center_no", villages_begin, villages_end),
        #(party_get_slot, ":market_town", ":center_no", slot_village_market_town),
		##NEW:
		(gt, ":center_no", 0),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
			(is_between, ":center_no", villages_begin, villages_end),
		(party_get_slot, ":market_town", ":center_no", slot_village_market_town),

		(ge, ":market_town", centers_begin),
		(this_or_next|party_slot_eq, ":market_town", slot_party_type, spt_town),
		(this_or_next|party_slot_eq, ":market_town", slot_party_type, spt_village),
			(is_between, ":market_town", centers_begin, centers_end),
		##nested diplomacy end+
        (party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
        (val_max, ":price_factor", ":price_in_market_town"),
      (try_end),
	  ##nested diplomacy start+
	  #Enforce constraints
	  (val_clamp, ":price_factor", minimum_price_factor, maximum_price_factor + 1),
	  ##nested diplomacy end+

      #For villages, the good will be sold no cheaper than in the market town
      #This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers

      (val_mul, ":price_factor", 100), #normalize price factor to range 0..100
      (val_div, ":price_factor", average_price_factor),
    (try_end),

    (store_add, ":penalty_factor", 100, ":trade_penalty"),

    (val_mul, ":price_factor", ":penalty_factor"),
    (val_div, ":price_factor", 100),

    (assign, reg0, ":price_factor"),
    (set_trigger_result, reg0),
  ]),

  ("dplmc_party_calculate_strength",
    [
      (store_script_param_1, ":party"), #Party_id
      (store_script_param_2, ":exclude_leader"), #Party_id

      (assign, reg0,0),
      (party_get_num_companion_stacks, ":num_stacks", ":party"),
      (assign, ":first_stack", 0),
      (try_begin),
        (neq, ":exclude_leader", 0),
        (assign, ":first_stack", 1),
      (try_end),

      (assign, ":sum", 0),
      (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),

        (try_begin),
          (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size",":party",":i_stack"),
        (try_end),
        (val_add, ":sum", ":stack_size"),
      (try_end),
      (assign, reg0, ":sum"),

      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (display_message, "@{!}DEBUG : sum: {reg0}"),
      (try_end),
  ]),

#script_dplmc_start_alliance_between_kingdoms, 20 days alliance, 40 days truce after that
  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
  # Output: none
  ("dplmc_start_alliance_between_kingdoms", #sets relations between two kingdoms
    [
      (store_script_param, ":kingdom_a", 1),
      (store_script_param, ":kingdom_b", 2),
      (store_script_param, ":initializing_war_peace_cond", 3),
	  ##diplomacy start+
	  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
	  #run by the player, intercept that here instead of the various places this is
	  #called from.
	  (assign, ":save_reg1", reg1),
	  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
	  (assign, ":kingdom_a", reg0),
	  (assign, ":kingdom_b", reg1),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+

      (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
      (val_add, ":relation", 15),
      (val_max, ":relation", 40),
      (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
      (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

      (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
      (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
      (try_end),

      (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
		##diplomacy start+ #Due to complaints about the wording
        #(display_log_message, "@{s1} and {s2} have concluded an alliance with each other."),
		(display_log_message, "@{s1} and {s2} have entered into an alliance with each other."),
		##diplomacy end+

        (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),


      (try_end),

	  (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace 80 with a named constant
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 80),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_alliance_days_initial),
	    ##nested diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace 80 with a named constant
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 80),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_alliance_days_initial),
	    ##nested diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

	  (try_end),

    # share wars
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
      (neq, ":kingdom_a", ":faction_no"),
      (neq, ":kingdom_b", ":faction_no"),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
      #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
      (eq, reg0, -2),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
      (ge, reg0, -1),
      (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", 2),
    (try_end),
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
      (neq, ":kingdom_a", ":faction_no"),
      (neq, ":kingdom_b", ":faction_no"),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
      #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
      (eq, reg0, -2),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
      (ge, reg0, -1),
      (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", 2),
    (try_end),
  ]),

#script_dplmc_start_defensive_between_kingdoms, 20 days defensive: 20 days trade aggreement, 20 days non-aggression after that
  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
  # Output: none
  ("dplmc_start_defensive_between_kingdoms", #sets relations between two kingdoms
    [
      (store_script_param, ":kingdom_a", 1),
      (store_script_param, ":kingdom_b", 2),
      (store_script_param, ":initializing_war_peace_cond", 3),
	  ##diplomacy start+
	  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
	  #run by the player, intercept that here instead of the various places this is
	  #called from.
	  (assign, ":save_reg1", reg1),
	  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
	  (assign, ":kingdom_a", reg0),
	  (assign, ":kingdom_b", reg1),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+

      (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
      (val_add, ":relation", 10),
      (val_max, ":relation", 30),
      (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
      (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

      (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 10),
        (val_max, ":relation", 30),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
      (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 10),
        (val_max, ":relation", 30),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
      (try_end),

      (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        (display_log_message, "@{s1} and {s2} have concluded a defensive pact with each other."),

        (call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),


      (try_end),

	  (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##diplomacy start+ replace 60 with named variable
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 60),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_defense_days_initial),
	    ##diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##diplomacy start+ replace 60 with named variable
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 60),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_defense_days_initial),
	    ##diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

	  (try_end),
  ]),

#script_dplmc_start_trade_between_kingdoms, 20 days trade aggreement, 20 days non-aggression after that
  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
  # Output: none
  ("dplmc_start_trade_between_kingdoms", #sets relations between two kingdoms
    [
      (store_script_param, ":kingdom_a", 1),
      (store_script_param, ":kingdom_b", 2),
      (store_script_param, ":initializing_war_peace_cond", 3),
	  ##diplomacy start+
	  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
	  #run by the player, intercept that here instead of the various places this is
	  #called from.
	  (assign, ":save_reg1", reg1),
	  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
	  (assign, ":kingdom_a", reg0),
	  (assign, ":kingdom_b", reg1),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+

      (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
      (val_add, ":relation", 5),
      (val_max, ":relation", 20),
      (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
      (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

      (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 5),
        (val_max, ":relation", 20),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
      (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 5),
        (val_max, ":relation", 20),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
      (try_end),

      (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        (display_log_message, "@{s1} and {s2} have concluded a trade agreement with each other."),

        (call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),


      (try_end),

	  (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number of days with a variable
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_trade_days_initial),
	    ##nested diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number of days with a variable
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_trade_days_initial),
	    ##nested diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

	  (try_end),
  ]),

#script_dplmc_start_nonaggression_between_kingdoms, 20 days non-aggression
  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
  # Output: none
  ("dplmc_start_nonaggression_between_kingdoms", #sets relations between two kingdoms
    [
      (store_script_param, ":kingdom_a", 1),
      (store_script_param, ":kingdom_b", 2),
      (store_script_param, ":initializing_war_peace_cond", 3),
	  ##diplomacy start+
	  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
	  #run by the player, intercept that here instead of the various places this is
	  #called from.
	  (assign, ":save_reg1", reg1),
	  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
	  (assign, ":kingdom_a", reg0),
	  (assign, ":kingdom_b", reg1),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+

      (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
      (val_add, ":relation", 3),
      (val_max, ":relation", 10),
      (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
      (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

      (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 3),
        (val_max, ":relation", 10),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
      (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 3),
        (val_max, ":relation", 10),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
      (try_end),

      (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        (display_log_message, "@{s1} and {s2} have concluded a non aggression pact with each other."),

        (call_script, "script_add_notification_menu", "mnu_dplmc_notification_nonaggression_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),


      (try_end),

	  (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number with a variable
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 20),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_truce_days_initial),
	    ##nested diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number with a variable
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_truce_days_initial),
	    ##nested diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

	  (try_end),
  ]),



# Input: arg1 = faction_no_1, arg2 = faction_no_2
  ("dplmc_get_prisoners_value_between_factions",
   [
       (store_script_param, ":faction_no_1", 1),
       (store_script_param, ":faction_no_2", 2),

       (assign, ":faction_no_1_value", 0),
       (assign, ":faction_no_2_value", 0),

       (try_for_parties, ":party_no"),
         (store_faction_of_party, ":party_faction", ":party_no"),
         (try_begin),
           (eq, ":party_faction", ":faction_no_1"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
           (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
             (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
             (store_troop_faction, ":cur_faction", ":cur_troop_id"),

             (eq, ":cur_faction", ":faction_no_2"),
             (try_begin),
               (troop_is_hero, ":cur_troop_id"),
               (call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
               (val_add, ":faction_no_1_value", reg0),

               (try_begin),#debug
                 (eq, "$cheat_mode", 1),
                 (assign, reg0, ":faction_no_1_value"),
                 (display_message, "@{!}DEBUG : faction_no_1_value: {reg0}"),
               (try_end),

             (try_end),
           (try_end),
         (else_try),
           (eq, ":party_faction", ":faction_no_2"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
           (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
             (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
             (store_troop_faction, ":cur_faction", ":cur_troop_id"),

             (eq, ":cur_faction", ":faction_no_1"),
             (try_begin),
               (troop_is_hero, ":cur_troop_id"),
               (call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
               (val_add, ":faction_no_2_value", reg0),

               (try_begin), #debug
                 (eq, "$cheat_mode", 1),
                 (assign, reg0, ":faction_no_2_value"),
                 (display_message, "@{!}DEBUG : faction_no_2_value: {reg0}"),
               (try_end),

             (try_end),
           (try_end),
         (try_end),
       (try_end),
       (store_sub, reg0, ":faction_no_1_value", ":faction_no_2_value"),
    ]),

# Input: arg1 = faction_no_1, arg2 = faction_no_2
  ("dplmc_get_truce_pay_amount",
   [
       (store_script_param, ":faction_no_1", 1),
       (store_script_param, ":faction_no_2", 2),
       (store_script_param, ":check_peace_war_result", 3),
	   ##diplomacy start+
	   #Since "fac_player_supporters_faction" is used as a shorthand for the faction
	   #run by the player, intercept that here instead of the various places this is
	   #called from.
	   (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":faction_no_1", ":faction_no_2"),
	   (assign, ":faction_no_1", reg0),
	   (assign, ":faction_no_2", reg1),
	   ##diplomacy end+

       (try_begin),
         (eq, "$cheat_mode", 1),
         (assign, reg0, ":check_peace_war_result"), #debug
         (display_message, "@{!}DEBUG : peace_war_result: {reg0}"),#debug
       (try_end),

       ##nested diplomacy start+
       #Improve this script; costs were too low befow.
       #faction_no_1 is player faction asking for peace
       #faction_no_2 is NPC faction that already considered peace and considers
       #      it a bad idea, so the price should not be nominal.

       #(Also, a sign error meant that the amount asked was almost always
       #zero.)

       #Because the PC wants peace and the NPC doesn't, we aren't going to
       #bother calculating relative strength or the like.  Instead, we are
       #going to assume the NPC can achieve his strategic objectives if he
       #does not make peace, and set the price accordingly.

       #Add a generic cost for check_peace_war_result
       #These are the same as in Wahiti's original script.
       (assign, ":base_cost",  4000),
       (try_begin),
          #It's dubious that this is ever currently called if the check-peace-war
          #result was >= 0, but include this for completeness.
          (ge, ":check_peace_war_result", 0),
          (assign, ":base_cost", 4000),
       (else_try),
          (ge, ":check_peace_war_result", -1),
          (assign, ":base_cost", 8000),
       (else_try),
          (ge, ":check_peace_war_result", -2),
          (assign, ":base_cost", 12000),
       (else_try),
          #It shouldn't be used with this parameter; this is for the
          #sake of completeness.
          (le, ":check_peace_war_result", -3),
          (store_mul, ":base_cost", -6000, ":check_peace_war_result"),
       (try_end),

       #Get reparations for held centers.  A truce lasts 20 days, so the
       #value "lost" in rents and tarriffs by declaring peace now cannot be
       #is not greater than 3 times the weekly average (that upper bound is
       #if the NPC is in a position to immediately recapture all of them).

       #If the NPC kingdom is currently attacking a specific village or walled
       #center, even if it isn't an ex-possession it effectively becomes one.
       #(Also, assign it or its center as a demanded fief if there wasn't one
       #already.)
       (assign, ":target_fief", -1),
       (try_begin),
          (lt, ":check_peace_war_result", 1),#This should always be true anyway, but still.
          (this_or_next|faction_slot_eq, ":faction_no_2", slot_faction_ai_state, sfai_attacking_center),
          (faction_slot_eq, ":faction_no_2", slot_faction_ai_state, sfai_raiding_village),
          (faction_get_slot, reg0, ":faction_no_2", slot_faction_ai_object),
          (is_between, reg0, centers_begin, centers_end),
          (assign, ":target_fief", reg0),
       (try_end),

       (assign, ":center_cost", 0),
       (assign, ":concession_value", 0),
       #This this old are newer are considered "recently conquered", meaning that
       #faction_no_2 thinks there's a good chance they could reclaim them if the
       #fighting continued.
       (store_current_hours, ":recently_conquered"),
       (try_begin),
          (ge, ":check_peace_war_result", 1),#ordinarily this should not be true
          (val_sub, ":recently_conquered", 24 * 2),#only the last two days
       (else_try),
          (eq, ":check_peace_war_result", 0),
          (val_sub, ":recently_conquered", 24 * 15),#last 15 days
       (else_try),
          (eq, ":check_peace_war_result", -1),
          (val_sub, ":recently_conquered", 24 * 20),#last 20 days
       (else_try),
          (eq, ":check_peace_war_result", -2),
          (val_sub, ":recently_conquered", 24 * 30),#last 30 days
       (else_try),
          (val_sub, ":recently_conquered", 24 * 60),#last 60 days
       (try_end),

       (try_for_range, ":party_no", centers_begin, centers_end),
          (store_faction_of_party, ":party_current_faction", ":party_no"),
          (eq, ":party_current_faction", ":faction_no_1"),

          #party_value is the estimated weekly income of the fief,
          #applied three times and time discounted
          (call_script, "script_dplmc_estimate_center_weekly_income", ":party_no"),
          (store_mul, ":party_value", reg0, 3),

          (try_begin),
             (ge, "$g_concession_demanded", spawn_points_begin),
             (this_or_next|eq, "$g_concession_demanded", ":party_no"),
             (party_slot_eq, ":party_no", slot_village_bound_center, "$g_concession_demanded"),
             (val_add, ":concession_value", ":party_value"),
          (try_end),

          (assign, ":continue", 0),

          (try_begin),
             #A former possession of faction 2 (must have recently changed hands, or
             #faction 2 must be enthusiastic about the war)
             (party_slot_eq, ":party_no", slot_center_original_faction, ":faction_no_2"),
             (party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":recently_conquered"),
             (assign, ":continue", 1),
          (else_try),
             #A former possession of faction 2 (must have recently changed hands, or
             #faction 2 must be enthusiastic about the war)
             (party_slot_eq, ":party_no", slot_center_ex_faction, ":faction_no_2"),
             (party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":recently_conquered"),
             (assign, ":continue", 1),
          (else_try),
             #The center is being attacked by faction 2, or is a village whose castle
             #or town is being attacked by faction 2.
             (ge, ":target_fief", centers_begin),
             (this_or_next|eq, ":party_no", ":target_fief"),
             (party_slot_eq, ":party_no", slot_village_bound_center, ":target_fief"),
             (assign, ":continue", 1),
          (else_try),
             #The center is under siege by faction 2.
             (party_get_slot, reg0, ":party_no", slot_center_is_besieged_by),
             (gt, reg0, 0),
             (party_is_active, reg0),
             (store_faction_of_party, reg0, reg0),
             (eq, reg0, ":faction_no_2"),
             (assign, ":continue", 1),
          (else_try),
             #The center is a village, and the castle or town it is bound to
             #is under siege by faction 2.
             (is_between, ":party_no", villages_begin, villages_end),
             (party_get_slot, reg0, ":party_no", slot_village_bound_center),
             (is_between, reg0, centers_begin, centers_end),
             (party_get_slot, reg0, reg0, slot_center_is_besieged_by),
             (gt, reg0, -1),
             (party_is_active, reg0),
             (store_faction_of_party, reg0, reg0),
             (eq, reg0, ":faction_no_2"),
             (assign, ":continue", 1),
          (try_end),

          (gt, ":continue", 0),

          (val_add, ":center_cost", ":party_value"),
       (try_end),

       #If no held centers were found, assume the campaign objective is to
       #conquer territory rather than recover lost territory, if the
       #NPC is sufficiently enthusiastic about the war.
       (try_begin),
          #Equivalent of a castle and a village
          (eq, ":check_peace_war_result", -1),
          (val_max, ":center_cost", (1500 + 750) * 3),
       (else_try),
          #Equivalent of two castles with two villages
          (le, ":check_peace_war_result", -2),
          (val_max, ":center_cost", (1500 + 750) * 3 * 2),
       (try_end),

	   #If the war started very recently, or a center changed hands very recently,
	   #increase the cost.  The reasoning behind this is to make the AI less prone
	   #to whipsawing.
	   #
	   #The multiplier is 2x for the first 48 hours, then decreases linearly from
       #the two-day mark until it reaches zero at the 8-day mark.
	   #
	   #As an example, here is how a cost of 10,000 would scale over this time:
	   # 1 day  - 20000
	   # 2 days - 20000
	   # 3 days - 18333
	   # 4 days - 16667
	   # 5 days - 15000
	   # 6 days - 13333
	   # 7 days - 11667
	   # 8 days - 10000
	   # 9 days - 10000
	   (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":faction_ai_last_decisive_event", ":faction_no_2", slot_faction_ai_last_decisive_event),
       (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
	   (val_max, ":hours_since_last_decisive_event", 0),
	   (try_begin),
	      #First 48 hours, the base & center costs are doubled.
	      (lt, ":hours_since_last_decisive_event", 48 + 1),
		  (val_mul, ":base_cost", 2),
		  (val_mul, ":center_cost", 2),
	   (else_try),
	      #From 2 days to 8 days, the cost multiplier goes from 2 to 1
		  (lt, ":hours_since_last_decisive_event", 24 * 8),
		  (store_sub, reg0, 24 * 2, ":hours_since_last_decisive_event"),#0 to 6 days
		  (store_sub, ":multiplier", 24 * 12, reg0),# 6 to 12 days

		  (val_mul, ":base_cost", ":multiplier"),
		  (val_add, ":base_cost", (24 * 6) // 2),
		  (val_div, ":base_cost", 24 * 6),

		  (val_mul, ":center_cost", ":multiplier"),
		  (val_add, ":center_cost", (24 * 6) // 2),
		  (val_div, ":center_cost", 24 * 6),
	   (try_end),

       #Get (value of ransoms held by faction #1) - (value of ransoms held by faction #2)
       (call_script, "script_dplmc_get_prisoners_value_between_factions", ":faction_no_1", ":faction_no_2"),

       (try_begin),
         (eq, "$cheat_mode", 1),
         (display_message, "@{!}DEBUG : prisoner_value: {reg0}"),#debug
       (try_end),
       (assign, ":prisoner_value", reg0),

       #Write result to reg0
       (store_add, reg0, ":base_cost", ":center_cost"),

	   #Scale for the player's wealth, to partially mitigate the problem
	   #of the cost becoming meaningless as the player's wealth increases.
	   #(Scale less than 1-to-1, so it is possible to become richer in real
	   #terms.)  This is also aimed at reducing the necessity of replacing
	   #the values in mods that alter gold scarcity.
	   (store_troop_gold, ":player_gold", "trp_household_possessions"),
	   (store_troop_gold, reg1, "trp_player"),
	   (val_add, ":player_gold", reg1),
	   (try_begin),
		  #Arbitrarily pick 100,000 as the target wealth, since that's when
		  #you get the Steam "gold farmer" achievement.
	      (gt, ":player_gold", 100000),
		  (store_div, reg1, ":player_gold", 1000),
		  (val_mul, reg1, reg0),
		  (val_div, reg1, 100),

		  (val_add, reg0, reg1),
		  (val_div, reg0, 2),

		  #Apply the same scaling to the concession value
		  (store_div, reg1, ":player_gold", 1000),
		  (val_mul, reg1, ":concession_value"),
		  (val_div, reg1, 100),

		  (val_add, ":concession_value", reg1),
		  (val_div, ":concession_value", 2),
	   (try_end),

       #Take into account campaign difficulty
	   (assign, ":min_cost", reg0),
       (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
       (try_begin),
           (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
           (val_mul, reg0, 3),
           (val_div, reg0, 2),
		   (val_mul, ":min_cost", 87),#set min_cost to 87% of the original base_cost + center_cost
		   (val_div, ":min_cost", 100),
       (else_try),
           (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
		   (val_mul, ":min_cost", 3),
		   (val_div, ":min_cost", 4),#set min_cost to 75% (base cost + center cost)
       (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy (0.75x)
            (val_mul, reg0, 3),
			(val_div, reg0, 4),
			(val_mul, ":min_cost", 9),
			(val_div, ":min_cost", 16),#set min_cost to (75% squared) of (base cost + center cost)
       (try_end),

       (val_sub, reg0, ":prisoner_value"),

       #Because the NPC kingdom doesn't want peace, it will not agree to peace
       #for free, as that would be a contradiction.
       (val_max, reg0, ":min_cost"),

       (try_begin),
         (eq, "$cheat_mode", 1),
         (display_message, "@{!}DEBUG : peace_war_result after prisoners: {reg0}"),#debug
       (try_end),

       #The value of the concession (if any) was already calculated above
       (assign, reg1, -1),
       (try_begin),
          (gt, "$g_concession_demanded", 0),
       	  (gt, ":concession_value", 0),
          (store_sub, reg1, reg0, ":concession_value"),
          (val_max, reg1, 0),
          #Only accept cash alone in lieu of a fief if you don't partcularly
          #want war, or if the AI is on "easy".
          (try_begin),
             (neq, ":reduce_campaign_ai", 2),#hard or medium
             (lt, ":check_peace_war_result", 0),
             (assign, reg0, -1),
          (try_end),
       (try_end),

     (try_begin), #debug
       (eq, "$cheat_mode", 1),
	     (display_message, "@{!}DEBUG : truce_pay_amount0: {reg0}"),
	     (display_message, "@{!}DEBUG : truce_pay_amount1: {reg1}"),
     (try_end),
     ##nested diplomacy end+
    ]),

  ("dplmc_player_center_surrender",
  [
    (store_script_param, ":center_no", 1),

    #protect player for 24 hours
    (store_current_hours,":protected_until"),
    (val_add, ":protected_until", 48),
    (party_get_slot, ":besieger", ":center_no", slot_center_is_besieged_by),
    (store_faction_of_party, ":besieger_faction",":besieger"),
    ##nested diplomacy start+
    #In this version this variable currently isn't used for anything
    #(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
    ##nested diplomacy end+

    (party_set_slot,":besieger",slot_party_ignore_player_until,":protected_until"),
    (party_ignore_player, ":besieger", 48),
	##nested diplomacy start+
	#Add support for promoted kingdom ladies
    #(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
	(try_for_range, ":lord", heroes_begin, heroes_end),
	  (this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
	  (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
	##nested diplomacy end+
      (store_faction_of_troop, ":lord_faction", ":lord"),
      (eq, ":lord_faction", ":besieger_faction"),
      (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
      (party_is_active, ":led_party"),

      (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
      (party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),

      (party_is_active, ":besieger"),
      (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
      (lt, ":distance_to_marshal", 20),

      (party_set_slot,":led_party",slot_party_ignore_player_until,":protected_until"),
      (party_ignore_player, ":led_party", 48),
    (try_end),

    (party_set_faction,"$current_town","fac_neutral"), #temporarily erase faction so that it is not the closest town
    (party_get_num_attached_parties, ":num_attached_parties_to_castle",":center_no"),
    (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
      (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":iap"),
      (party_detach, ":attached_party"),
      (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
      (eq, ":attached_party_type", spt_kingdom_hero_party),
      (neq, ":attached_party_type", "p_main_party"),
      (store_faction_of_party, ":attached_party_faction", ":attached_party"),
      (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
      (try_begin),
        (gt, reg0, 0),
        (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
      (else_try),
        (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, ":center_no"),
      (try_end),
    (try_end),
    (call_script, "script_party_remove_all_companions", ":center_no"),
    (change_screen_return),
    (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"), #recalculate so that
    (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured

	##nested diplomacy start+
	#Anyone who lost a fief due to your surrender will be irritated
	(try_for_range, ":village_no", centers_begin, centers_end),
       (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
	   (party_get_slot, ":village_lord", ":village_no", slot_town_lord),
	   (neq, ":village_lord", "trp_player"),
	   (is_between, ":village_lord", heroes_begin, heroes_end),
	   (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
    (try_end),
	##nested diplomacy end+
    ##diplomacy
    (call_script, "script_give_center_to_faction", "$current_town", ":besieger_faction"),
    (call_script, "script_order_best_besieger_party_to_guard_center", ":center_no", ":besieger_faction"),

    #relation and controversy
    ##nested diplomacy start+, There should be no relation bonus with the enemy lord
    #(call_script, "script_change_player_relation_with_troop", ":enemy_party_leader", 2),
    ##nested diplomacy end+
    (try_begin),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (neq, "$players_kingdom", "fac_player_faction"),
      (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
  	  ##diplomacy start+
	  ##OLD:
      #(neq, ":faction_leader", "trp_player"),
	  ##NEW:
	  #Also guard against faction leader being some invalid negative number
	  (gt, ":faction_leader", "trp_player"),
	  ##diplomacy end+
      (call_script, "script_change_player_relation_with_troop", ":faction_leader", -2),
    (try_end),

  	(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
  	(val_add, ":controversy", 4),
  	(val_min, ":controversy", 100),
  	(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
    ##nested diplmacy start+ add garrison to fief
    #The average # of troops added by script_cf_reinforce_party is 11.5.
    (assign, ":garrison_strength", 3),#easy: 34.5 for a castle
    (try_begin),
       (party_slot_eq, ":center_no", slot_party_type, spt_town),
       (assign, ":garrison_strength", 9),#easy: 103.5 for a town
    (try_end),
    #Take into account campaign difficulty.
    (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
    (try_begin),
       (eq, ":reduce_campaign_ai", 0), #hard 166% + 3 waves
       (val_mul, ":garrison_strength", 5),
       (val_div, ":garrison_strength", 3),
       (val_add, ":garrison_strength", 3),
    (else_try),
       (eq, ":reduce_campaign_ai", 1), #moderate 166%
       (val_mul, ":garrison_strength", 5),
       (val_div, ":garrison_strength", 3),
    #(else_try),
    #   (eq, ":reduce_campaign_ai", 2), #easy 100%
    #   (store_mul, ":garrison_strength", 1),
    (try_end),

    (try_for_range, ":unused", 0, ":garrison_strength"),
       (call_script, "script_cf_reinforce_party", ":center_no"),
    (try_end),
    (try_for_range, ":unused", 0, 7),# ADD some XP initially
       (store_mul, ":xp_range_min", 150, ":garrison_strength"),
       (store_mul, ":xp_range_max", 200, ":garrison_strength"),
       (store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
       (party_upgrade_with_xp, ":center_no", ":xp", 0),
    (try_end),
    ##nested diplomacy end+
  ]),


  ("dplmc_send_messenger_to_troop",
  [
    (store_script_param, ":target_troop", 1),
    (store_script_param, ":message", 2),
    (store_script_param, ":orders_object", 3),

    #SB : correcting destination for lords waiting to respawn
    (troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
    (try_begin),
      (le, ":target_party", 0),
      (call_script, "script_lord_get_home_center", ":target_troop"),
      (assign, ":target_party", reg0),
    (try_end),

    (set_spawn_radius, 1),
    (spawn_around_party, "$current_town", "pt_messenger_party"),
    (assign,":spawned_party",reg0),
    #SB : factionalized messenger
    (store_faction_of_party, ":faction_no", ":target_party"),
    (try_begin),
      (eq, ":faction_no", "fac_player_supporters_faction"),
      (is_between, "$g_player_culture", npc_kingdoms_begin, kingdoms_end),
      (assign, ":faction_no", "$g_player_culture"),
    (try_end),
    (try_begin),
      (is_between, ":faction_no", npc_kingdoms_begin, kingdoms_end),
      (faction_get_slot, ":messenger_troop", ":faction_no", slot_faction_messenger_troop),
    (else_try),
      (assign, ":messenger_troop", "trp_dplmc_messenger"),
    (try_end),
    (party_add_members, ":spawned_party", ":messenger_troop", 1),


    (try_begin),
      (eq, ":message", spai_accompanying_army),
      (assign, ":orders_object", "p_main_party"),
    (try_end),

    # (party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
    (store_faction_of_troop, ":player_faction", "trp_player"),
    (party_set_faction, ":spawned_party", ":player_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_messenger),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
    (party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
    #SB : cache the actual troop while going towards known center
    (party_set_slot, ":spawned_party", dplmc_slot_party_origin, ":target_troop"),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (str_store_party_name, s13, ":target_party"),
      (display_message, "@{!}DEBUG - Send message to {s13}"),
    (try_end),
  ]
  ),

  ("dplmc_send_messenger_to_party",
  [
    (store_script_param, ":target_party", 1),
    (store_script_param, ":message", 2),
    (store_script_param, ":orders_object", 3),

    (set_spawn_radius, 1),
    (spawn_around_party, "$current_town", "pt_messenger_party"),
    (assign, ":spawned_party", reg0),

    #SB : factionalized messenger
    (store_faction_of_party, ":faction_no", ":target_party"),
    (try_begin),
      (eq, ":faction_no", "fac_player_supporters_faction"),
      (is_between, "$g_player_culture", npc_kingdoms_begin, kingdoms_end),
      (assign, ":faction_no", "$g_player_culture"),
    (try_end),

    (try_begin),
      (is_between, ":faction_no", npc_kingdoms_begin, kingdoms_end),
      (faction_get_slot, ":messenger_troop", ":faction_no", slot_faction_messenger_troop),
    (else_try),
      (assign, ":messenger_troop", "trp_dplmc_messenger"),
    (try_end),
    (party_add_members, ":spawned_party", ":messenger_troop", 1),
    (party_set_faction, ":spawned_party", "fac_player_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_messenger),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
    (party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (str_store_party_name, s13, ":target_party"),
      (display_message, "@{!}DEBUG - Send message to {s13}"),
    (try_end),
  ]
  ),

  ("dplmc_send_gift",
    [
    (store_script_param, ":target_troop", 1),
    (store_script_param, ":gift", 2),
    (store_script_param, ":amount", 3),

    (try_begin),
      (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
      (troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
    (else_try),
      (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
      (troop_get_slot, ":target_party", ":target_troop", slot_troop_cur_center),
    (try_end),


    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (str_store_item_name, s12, ":gift"),
      (str_store_party_name, s13, ":target_party"),
      (display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
    (try_end),

    (try_begin),
       #Guard against this being called without an explicit amount
       (lt, ":amount", 1),
       (display_message, "@{!} ERROR: Bad gift amount {reg0}.  (Tell the mod writer he needs to update his code.)  Using a safe default."),
       (assign, ":amount", 1),
       (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
       (assign, ":amount", 150),
    (try_end),
    (assign, ":original_amount", ":amount"),#Save this here because amount gets modified below!

    (call_script, "script_dplmc_withdraw_from_treasury", 50),
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),

  	  (try_for_range, ":inventory_slot", 0, ":capacity"),
  	    (gt, ":amount", 0),
  		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
  		  (eq, ":item", ":gift"),
  		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
  		  (try_begin),
  		    (le, ":tmp_amount", ":amount"),
  		    (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
  		    (val_sub, ":amount", ":tmp_amount"),
  		  (else_try),
  		    (val_sub, ":tmp_amount", ":amount"),
  		    (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
  		    (assign, ":amount", 0),
  		  (try_end),
  	  (try_end),

    (set_spawn_radius, 1),
    (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
    (assign,":spawned_party",reg0),
    (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
    (party_set_slot, ":spawned_party",  slot_party_orders_object,  ":target_troop"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
    (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_parameter_1, ":original_amount"),
    ]),

  ("dplmc_send_gift_to_center",
    [
    (store_script_param, ":target_party", 1),
    (store_script_param, ":gift", 2),
    (store_script_param, ":amount", 3),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (str_store_item_name, s12, ":gift"),
      (str_store_party_name, s13, ":target_party"),
      (display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
    (try_end),

    (try_begin),
       #Guard against this being called without an explicit amount
       (lt, ":amount", 1),
       (display_message, "@{!} ERROR: Bad gift amount {reg0}.  (Tell the mod writer he needs to update his code.)  Using a safe default."),
       (assign, ":amount", 300),
    (try_end),
    (assign, ":original_amount", ":amount"),#Save this here because amount gets modified below!

    (call_script, "script_dplmc_withdraw_from_treasury", 50),
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
	    (gt, ":amount", 0),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", ":gift"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
		  (try_begin),
		    (le, ":tmp_amount", ":amount"),
		    (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
		    (val_sub, ":amount", ":tmp_amount"),
		  (else_try),
		    (val_sub, ":tmp_amount", ":amount"),
		    (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
		    (assign, ":amount", 0),
		  (try_end),
	  (try_end),

    (set_spawn_radius, 1),
    (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
    (assign,":spawned_party",reg0),
    (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
    (party_set_slot, ":spawned_party",  slot_party_orders_object, 0),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
    (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
    (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_parameter_1, ":original_amount"),
    ]),

  ("dplmc_troop_political_notes_to_s47",
      [
    (store_script_param, ":troop_no", 1),
    ##diplomacy start+
	(assign, ":save_reg1", reg1),#save to revert
    (assign, ":save_reg4", reg4),#save to revert

    (try_begin),
       (eq, 0, 1),#Always disable this right now
       (is_between, "$g_talk_troop", heroes_begin, heroes_end),#i.e. not your chancellor
       (assign, ":troop_speaker", "$g_talk_troop"),
	   (call_script, "script_troop_get_player_relation", ":troop_speaker"),
	   (assign, ":speaker_player_relation", reg0),
    (else_try),
       (assign, ":troop_speaker", -1),
	   (assign, ":speaker_player_relation", 100),
    (try_end),
    ##diplomacy end+

    (try_begin),
      (str_clear, s47),

      (store_faction_of_troop, ":troop_faction", ":troop_no"),

      (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),

      (str_clear, s40),
      (assign, ":logged_a_rivalry", 0),
      ##nested diplomacy start+
      (str_clear, s41),
      #lord can be married or related to player
      #(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
      (try_for_range, ":kingdom_hero", active_npcs_including_player_begin, active_npcs_end),
        #Also, don't include rivalries with retired (or dead) characters
        (neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_retirement),
      ##nested diplomacy end+
        (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_hero"),
        (lt, reg0, -10),

        (str_store_troop_name_link, s39, ":kingdom_hero"),
		  ##nested diplomacy start+ use second person
        (try_begin),
           (eq, ":kingdom_hero", "trp_player"),
           (str_store_string, s39, "str_you"),
        (try_end),
		  ##nested diplomacy end+
        (try_begin),
          (eq, ":logged_a_rivalry", 0),
          ##nested diplomacy start+
          (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),#use reg4 for gender-correct pronoun
          ##nested diplomacy end+
          (str_store_string, s40, "str_dplmc_s39_rival"),
          (assign, ":logged_a_rivalry", 1),
        (else_try),
          (str_store_string, s41, "str_s40"),
          (str_store_string, s40, "str_dplmc_s41_s39_rival"),
        (try_end),

      (try_end),

      (str_clear, s46),
      ##nested diplomacy start+
      #(troop_get_type, reg4, ":troop_no"),#use for gender-correct pronoun
		(call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
      (str_store_troop_name, s46,":troop_no"),
	  (assign, ":details_available", 0),
	  (try_begin),
		#Enable details for lords you have met
		(neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
		(assign, ":details_available", 1),
          (else_try),
                #Enable details when using an "omniscient" or non-specific speaker
                (neg|is_between, ":troop_speaker", heroes_begin, heroes_end),
                (assign, ":details_available", 1),
          (else_try),
                #Enable details for NPCs that aren't standard heroes, because the following checks don't apply
                (neg|is_between, ":troop_no", heroes_begin, heroes_end),
                (assign, ":details_available", 1),
          (else_try),
                #Enable details for lords the speaker has met
                (is_between, ":troop_speaker", heroes_begin, heroes_end),
                (is_between, ":troop_no", heroes_begin, heroes_end),
                (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":troop_speaker"),
                (neq, reg0, 0),#between NPCs, relation 0 means "have not met"
                (assign, ":details_available", 1),
          (else_try),
                #Enable details for v. notable lords (based on renown)
                (troop_slot_ge, ":troop_no", slot_troop_renown, 500),
                (assign, ":details_available", 1),
          (else_try),
                #Enable details for v. notable lords (based on fiefs)
                (assign, reg0, 0),
                (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                   (this_or_next|party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
                   (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_no"),
                     (troop_slot_eq, ":troop_no", slot_troop_home, ":center_no"),
                   (val_add, reg0, 2),
                   (party_slot_eq, ":center_no", slot_party_type, spt_town),
                   (val_add, reg0, 2),
                (try_end),
                (ge, reg0, 4),#one town, or 2+ castles
                (assign, ":details_available", 1),
          (try_end),
      #xxx TODO: Make a full implementation of the above that takes into account the time of the last spy report.
      (try_begin),
        (eq, ":details_available", 0),
        (troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
        (str_store_string, s46, "str_dplmc_reputation_unknown"),
      (else_try), #SB : promoted companion rep
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_roguish),
        (str_store_string, s46, "str_dplmc_reputation_roguish"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
        (str_store_string, s46, "str_dplmc_reputation_benefactor"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
        (str_store_string, s46, "str_dplmc_reputation_custodian"),
      (else_try),
      ##nested diplomacy end+
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
        (str_store_string, s46, "str_dplmc_reputation_martial"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
        (str_store_string, s46, "str_dplmc_reputation_debauched"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
        (str_store_string, s46, "str_dplmc_reputation_pitiless"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
        (str_store_string, s46, "str_dplmc_reputation_calculating"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
        (str_store_string, s46, "str_dplmc_reputation_quarrelsome"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
        (str_store_string, s46, "str_dplmc_reputation_goodnatured"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
        (str_store_string, s46, "str_dplmc_reputation_upstanding"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
        (str_store_string, s46, "str_dplmc_reputation_conventional"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_adventurous),
        (str_store_string, s46, "str_dplmc_reputation_adventurous"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_otherworldly),
        (str_store_string, s46, "str_dplmc_reputation_romantic"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
        (str_store_string, s46, "str_dplmc_reputation_moralist"),
      (else_try),
        (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_ambitious),
        (str_store_string, s46, "str_dplmc_reputation_ambitious"),
      (else_try),
        (troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
        (str_store_string, s46, "str_dplmc_reputation_unknown"),
      (try_end),

      ##diplomacy start+
      (str_clear, s39),#remove annoying bug
      (str_clear, s45),#remove annoying bug

      #Special-case spouse into showing up if it doesn't get added below
      (try_begin),
         (troop_get_slot, ":spouse", ":troop_no", slot_troop_spouse),
         (ge, ":spouse", 0),

         #Because blank memory is initially zero, enforce this
         (this_or_next|is_between, ":troop_no", heroes_begin, heroes_end),
            (neq, ":spouse", "trp_player"),
         #Initialize s45
         (str_store_troop_name, s39, ":spouse"),
         (try_begin),
           (eq, ":spouse", "trp_player"),
           (str_store_string, s39, "str_you"),##<-- dplmc+ note, this was s59 before, probably an accidental bug
         (else_try), #SB : speaker
           (eq, ":spouse", ":troop_speaker"),
           (str_store_string, s39, "str_me"),
         (try_end),
         (str_store_string, s45, "str_dplmc_s40_married_s39"),
      (try_end),
      ##diplomacy end+

      (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
        (troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
        ##nested diplomacy start+ ; some lords could romance opposite-gender lords
        #(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
        (is_between, ":love_interest", active_npcs_begin, kingdom_ladies_end),
        #Also prevent a bug for companions / claimants who are lords
        (neq, ":love_interest", "trp_knight_1_1_wife"),#<- should not appear in the game
        #Also prevent bad messages for married/betrothed lords
        (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":love_interest"),
           (troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
        (this_or_next|troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
           (troop_slot_eq, ":troop_no", slot_troop_betrothed, -1),
        ##nested diplomacy end+
        (str_store_troop_name, s39, ":love_interest"),
        ##nested diplomacy start+ Use second person properly
        (try_begin),
           (eq, ":love_interest", "trp_player"),
           (str_store_string, s39, "str_you"),
         (else_try), #SB : speaker
           (eq, ":love_interest", ":troop_speaker"),
           (str_store_string, s39, "str_me"),
        (try_end),
        ##nested diplomacy start+
        (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":love_interest"),
        ##nested diplomacy start+
        (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),#use reg4 for gender-correct pronoun
        ##nested diplomacy end+
        (str_store_string, s45, "str_dplmc_s40_love_interest_s39"),
        (try_begin),
        	(troop_slot_eq, ":troop_no", slot_troop_spouse, ":love_interest"),
        	(str_store_string, s45, "str_dplmc_s40_married_s39"),
        (else_try),
        	(troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
        	(str_store_string, s45, "str_dplmc_s40_betrothed_s39"),
        (try_end),
      (try_end),

    (str_clear, s44),
    (try_begin),
      (neq, ":troop_no", ":faction_leader"),
      ##nested diplomacy start+
      (gt, ":details_available", 0),
	  #Ensure leader is valid
	  (assign, reg0, 0),#continue if 0
	  (try_begin),
	     (neq, ":troop_no", "trp_player"),
		 (neq, ":faction_leader", "trp_player"),
		 (this_or_next|neg|is_between, ":troop_no", heroes_begin, heroes_end),
			(neg|is_between, ":faction_leader", heroes_begin, heroes_end),
		 (assign, reg0, 1),
	  (try_end),
	  (eq, reg0, 0),

	  (try_begin),
	     (gt, ":troop_speaker", 0),
		 (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", ":troop_speaker"),
		 #(val_min, reg0, 20),
		 #(neq, ":faction_leader", "trp_player"),
		 #(val_div, reg0, 2),
	  (try_end),
	  (this_or_next|lt, reg0, 1),
		(ge, ":speaker_player_relation", 1),
      ##nested diplomacy end+
      (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),

      (assign, ":relation", reg0),
	  ##diplomacy start+ Don't mention anything for kingdom ladies at the beginning; it doesn't add information.
	  (this_or_next|lt, reg0, 0),
	  (this_or_next|gt, reg0, 1),#Remember that relation 1 is neutral (it just means "met") between NPCs
	  (this_or_next|neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
	  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
	     (troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
	  ##diplomacy end+
      (store_add, ":normalized_relation", ":relation", 100),
      (val_add, ":normalized_relation", 5),
      (store_div, ":str_offset", ":normalized_relation", 10),
      (val_clamp, ":str_offset", 0, 20),
      ##nested diplomacy start+
      #(troop_get_type, reg4, ":troop_no"),#use for gender-correct pronoun
      (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
      #TODO: Come back and add this (take into account spying)
      #(neq, ":details_available", 0),#don't show unless more details are available
      ##nested diplomacy end+
      (store_add, ":str_id", "str_dplmc_relation_mnus_100_ns",  ":str_offset"),
      (try_begin),
        (eq, ":faction_leader", "trp_player"),
        ##nested diplomacy start+ "str_you" exists, so we might as well use it
        #(str_store_string, s59, "@you"),
        (str_store_string, s59, "str_you"),
        ##diplomacy end+
      (else_try),
        (str_store_troop_name, s59, ":faction_leader"),
      (try_end),
      (str_store_string, s59, ":str_id"),
      (str_store_string, s44, "@{!}^{s59}"),
    (try_end),

    (str_clear, s48),

    (try_begin),
      (eq, "$cheat_mode", 1),
      (store_current_hours, ":hours"),
      (gt, ":hours", 0),
      (call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),
      (str_store_string, s48, "str_sense_of_security_military_reg1_court_position_reg3_"),
    (try_end),

    (str_store_string, s47, "str_s46s45s44s48"),

  (try_end),
     ##diplomacy start+
     (assign, reg1, ":save_reg1"),#revert register
     (assign, reg4, ":save_reg4"),#revert register to avoid clobbering
     ##diplomacy end+
    ]),

  ("dplmc_send_patrol",
  [
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":size", 3), #0 small, 1 medium, 2, big, 3 elite
    (store_script_param, ":template_faction", 4),
    (store_script_param, ":order_troop", 5),

    (set_spawn_radius, 1),
    (spawn_around_party, ":start_party", "pt_patrol_party"),
    (assign,":spawned_party",reg0),
    (party_set_faction, ":spawned_party", ":template_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
    (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"),
    (str_store_party_name, s5, ":target_party"),
    (party_set_name, ":spawned_party", "str_s5_patrol"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),

    (try_begin),
      (neg|is_between, ":template_faction", npc_kingdoms_begin, npc_kingdoms_end),

      (party_get_slot, ":template_faction", ":start_party", slot_center_original_faction),
      (try_begin),
        (is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
        (assign, ":template_faction", "$g_player_culture"),
      (else_try),
        (party_get_slot, ":town_lord", ":start_party", slot_town_lord),
        (gt, ":town_lord", 0),
        (troop_get_slot, ":template_faction", ":town_lord", slot_troop_original_faction),
      (try_end),

      (try_begin),
        (eq, ":size", 0),
        (call_script, "script_dplmc_withdraw_from_treasury", 1000),
      (else_try),
        (this_or_next|eq, ":size", 1),
        (eq, ":size", 3),
        (call_script, "script_dplmc_withdraw_from_treasury", 2000),
      (else_try),
        (eq, ":size", 2),
        (call_script, "script_dplmc_withdraw_from_treasury", 3000),
      (try_end),
    (try_end),

    (faction_get_slot, ":party_template_a", ":template_faction", slot_faction_reinforcements_a),
    (faction_get_slot, ":party_template_b", ":template_faction", slot_faction_reinforcements_b),
    (faction_get_slot, ":party_template_c", ":template_faction", slot_faction_reinforcements_c),

    (try_begin),
      (eq, ":size", 3),
      (party_add_template, ":spawned_party", ":party_template_c"),
      (party_add_template, ":spawned_party", ":party_template_c"),
      #SB : personality change
      (party_set_aggressiveness, ":spawned_party", 7),
      (party_set_courage, ":spawned_party", 11),
    (else_try), #SB : same goes here
      (store_add, ":aggressiveness", ":size", 8),
      (party_set_aggressiveness, ":spawned_party", ":aggressiveness"),
      (val_add, ":size", 1),
      (val_mul, ":size", 2),
      (try_for_range, ":cur_i", 0, ":size"),
        (store_random_in_range, ":random", 0, 3),
        (try_begin),
          (eq, ":random", 0),
          (party_add_template, ":spawned_party", ":party_template_a"),
        (else_try),
          (eq, ":random", 1),
          (party_add_template, ":spawned_party", ":party_template_b"),
        (else_try),
          (party_add_template, ":spawned_party", ":party_template_c"),
        (try_end),

        (try_begin), #debug
          (eq, "$cheat_mode", 1),
          (assign, reg0, ":cur_i"),
          (str_store_faction_name, s7, ":template_faction"),
          (display_message, "@{!}DEBUG - Added {reg0}.template of faction {s7} to patrol."),
        (try_end),
      (try_end),
    (try_end),


    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (str_store_party_name, s13, ":target_party"),
      (str_store_faction_name, s14, ":template_faction"),
      (str_store_party_name, s15, ":start_party"),
      (display_message, "@{!}DEBUG - Send {s14} patrol from {s15} to {s13}"),
    (try_end),
  ]),

  ("dplmc_send_patrol_party",
  [
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":party_no", 3),
    (store_script_param, ":template_faction", 4),

    (set_spawn_radius, 1),
    (spawn_around_party, ":start_party", "pt_patrol_party"),
    (assign,":spawned_party",reg0),
    (party_set_faction, ":spawned_party", ":template_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
    (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
    (str_store_party_name, s5, ":target_party"),
    (party_set_name, ":spawned_party", "str_s5_patrol"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),

    (call_script, "script_party_add_party", ":spawned_party", ":party_no"),
  ]),

  ("dplmc_move_troops_party",
  [
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":party_no", 3),
    (store_script_param, ":template_faction", 4),

    (set_spawn_radius, 1),
    (spawn_around_party, ":start_party", "pt_patrol_party"),
    (assign,":spawned_party",reg0),
    (party_set_faction, ":spawned_party", ":template_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
    (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
    (str_store_party_name, s5, ":target_party"),
    #SB : fixed string
    (party_set_name, ":spawned_party", "str_s5_transfer"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_state, spai_retreating_to_center),
    (party_set_aggressiveness, ":spawned_party", 0),
    (party_set_courage, ":spawned_party", 3),
    (party_set_ai_initiative, ":spawned_party", 100),

    (call_script, "script_party_add_party", ":spawned_party", ":party_no"),
  ]),

  ("dplmc_send_scout_party",
  [
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":faction", 3),

    (set_spawn_radius, 1),
    (spawn_around_party, ":start_party", "pt_scout_party"),
    (assign,":spawned_party",reg0),
    (party_set_faction, ":spawned_party", ":faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_scout),
    (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
    (str_store_party_name, s5, ":target_party"),
    (party_set_name, ":spawned_party", "str_s5_scout"),

    (party_add_members, ":spawned_party", "trp_dplmc_scout", 1),

    (party_get_position, pos1, ":target_party"),
    (map_get_random_position_around_position, pos2, pos1, 1),
    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_point),
    (party_set_ai_target_position, ":spawned_party", pos2),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":target_party"),
    (party_set_aggressiveness, ":spawned_party", 0),
    (party_set_courage, ":spawned_party", 3),
    (party_set_ai_initiative, ":spawned_party", 100),
  ]),

  ("dplmc_init_domestic_policy",
  [
    (try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
      # (try_begin),
        # (store_random_in_range, ":random", -3, 4),
        # (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, ":random"),
        # (store_random_in_range, ":random", -3, 4),
        # (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, ":random"),
        # (store_random_in_range, ":random", -3, 4),
        # (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, ":random"),
        # (store_random_in_range, ":random", -3, 4),
        # (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, ":random"),
      # (try_end),
      #SB : randomize mercantilism as well via script below
      (call_script, "script_dplmc_randomize_faction_domestic_policy", ":kingdom"),
    (try_end),
  ]),

  #SB : add this to allow randomization of a single faction (see prsnt_dplmc_policy_management)
  ("dplmc_randomize_faction_domestic_policy",
    [
    (store_script_param, ":kingdom", 1),
    (try_for_range, ":slot", dplmc_slot_faction_policies_begin, dplmc_slot_faction_policies_end),
      (store_random_in_range, ":random", -3, 4),
      (faction_set_slot, ":kingdom", ":slot", ":random"),
    (try_end),
    ]),

  ("dplmc_is_affiliated_family_member",
  [
      (store_script_param, ":troop_id", 1),

      (assign, ":is_affiliated_family_member", 0),
	  ##nested diplomacy start+
	  (assign, ":save_reg1", reg1),#<- Save reg1 which gets overwritten by script_dplmc_troop_get_family_relation_to_troop
	  ##nested diplomacy end+
      (try_begin),
        (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
        (try_begin),
		  ##nested diplomacy start+ add use of dplmc_slot_troop_affiliated
		  (this_or_next|troop_slot_eq, ":troop_id", dplmc_slot_troop_affiliated, 3),
		  ##diplomacy end+
          (eq, "$g_player_affiliated_troop", ":troop_id"),
          (assign, ":is_affiliated_family_member", 1),
        (else_try),
          (is_between, ":troop_id", lords_begin, kingdom_ladies_end),
		  ##nested diplomacy start+
          #(call_script, "script_troop_get_family_relation_to_troop", ":troop_id", "$g_player_affiliated_troop"),
		  (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "$g_player_affiliated_troop"),
		  ##nested diplomacy end+
          (gt, reg0, 0),
          (call_script, "script_troop_get_relation_with_troop", "$g_player_affiliated_troop", ":troop_id"),
          (ge, reg0, -10),
		  (assign, ":is_affiliated_family_member", 1),
        (try_end),
      (try_end),
	  ##nested diplomacy start+
	  (assign, reg1, ":save_reg1"),#revert register
	  ##nested diplomacy end+
      (assign, reg0, ":is_affiliated_family_member"),
  ]),

  ("dplmc_affiliate_end",
  [
    (store_script_param, ":cause", 1),

    (assign, "$g_player_affiliated_troop", 0),

    (try_begin),
      (eq, ":cause", 1),
      (assign, ":max_penalty", -16),
      (assign, ":term", 20),
      (assign, ":honor_val", 10),
    (else_try),
      (assign, ":max_penalty", -12),
      (assign, ":honor_val", 5),
      (assign, ":term", 15),
    (try_end),

    (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
      (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
      (gt, reg0, 0),

      (store_skill_level, ":value", "skl_persuasion", "trp_player"),
      (store_random_in_range, ":value", 0, ":value"),
      ##nested diplomacy start+   Fix mistake.
      ##
      ##OLD:
      #(val_add, ":value", ":max_penalty", ":value"),
      #
      #NEW:
      #I'm pretty sure this is what was intended.
      (val_add, ":value", ":max_penalty"),
      ##nested diplomacy end+
      (val_min, ":value", 0),
      (call_script, "script_change_player_relation_with_troop", ":family_member", ":value"),
    (try_end),

    (try_begin),
      (gt, "$player_honor", ":honor_val"),
      (val_add, ":term", ":honor_val"),
    (else_try),
      (val_add, ":term", "$player_honor"),
    (try_end),

    (store_current_hours, ":cur_hours"),
    (store_sub, ":affiliated_hours", ":cur_hours", "$g_player_affiliated_time"),
    (store_div, ":affiliated_days", ":affiliated_hours", 24),
    (val_sub, ":term", ":affiliated_days"),
    (val_max, ":term", 0),
    (val_min, ":term", 40),


    (troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
    (val_add, ":controversy", ":term"),
    (val_min, ":controversy", 100),
    (troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),

  ]),

  ("dplmc_appoint_chamberlain",
  [
    (troop_set_auto_equip, "trp_dplmc_chamberlain", 0),
    (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_tabard"),
    (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_leather_boots"),
    (assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
    #SB : grab all gold from chest troops (seneschals)
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
      (store_sub, ":chest_troop", ":center_no", towns_begin),
      (val_add, ":chest_troop", "trp_town_1_seneschal"),
      (store_troop_gold, ":cur_gold", ":chest_troop"),
      (troop_remove_gold, ":chest_troop", ":cur_gold"),
      (troop_add_gold, "trp_household_possessions", ":cur_gold"), #no script call
    (try_end),
  ]),

  ("dplmc_appoint_chancellor",
  [
    (troop_set_auto_equip, "trp_dplmc_chancellor", 0),
    (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_nobleman_outfit"),
    (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_leather_boots"),
    (assign, "$g_player_chancellor", "trp_dplmc_chancellor"),
  ]),

  ("dplmc_appoint_constable",
  [
    (troop_set_auto_equip, "trp_dplmc_constable", 0),
    (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_dplmc_coat_of_plates_red_constable"),
    (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_leather_boots"),
    (assign, "$g_player_constable", "trp_dplmc_constable"),
  ]),

##diplomacy end

##diplomacy start+
#Importing a script used in Custom Commander.  The inventory copying is used
#as a clever way to make "unmodifiable" views of others' equipment (both the
#PC and NPC have their inventory copied before viewing, and after the window
#closes the copies are written back over the originals).
  ("dplmc_copy_inventory",
    [
      (store_script_param_1, ":source"),
      (store_script_param_2, ":target"),

      (troop_clear_inventory, ":target"),
      (troop_get_inventory_capacity, ":inv_cap", ":source"),
      (try_for_range, ":i_slot", 0, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
        (troop_set_inventory_slot, ":target", ":i_slot", ":item"),
        (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
        (troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
        (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
        (gt, ":amount", 0),
        (troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
      (try_end),
    ]),


#Decide whether an NPC wants to exchange a fief or not.
#
# param#1 is NPC being asked
# param#2 is that NPC's fief being asked for
# param#3 is the one asking (usually the player)
# param#4 is the fief being offered in exchange
#
# Result is returned in reg0.  Negative means "no", zero means "yes",
# positive means "yes but you have to pay me this amount".
# If the result is negative, the response string is stored in s14.
  ("dplmc_evaluate_fief_exchange",
    [
      (store_script_param, ":target_npc", 1),
      (store_script_param, ":target_fief", 2),
      (store_script_param, ":asker", 3),
      (store_script_param, ":offered_fief", 4),

      (assign, ":result", -1),
      (assign, reg0, ":result"),
      (str_store_string, s14, "str_ERROR_string"),

      (try_begin),
          #Both NPCs are valid, and are not same character.  One can be the player.
          (neq, ":target_npc", ":asker"),
          (is_between, ":target_npc", heroes_begin, heroes_end),
          (this_or_next|is_between, ":asker", heroes_begin, heroes_end),
             (eq,":asker","trp_player"),
          #Both fiefs are valid and owned by the lords in the arguments
          (is_between, ":target_fief", centers_begin, centers_end),
          (party_slot_eq, ":target_fief", slot_town_lord, ":target_npc"),
          (is_between, ":offered_fief", centers_begin, centers_end),
          (party_slot_eq, ":offered_fief", slot_town_lord, ":asker"),
          #The lords are in the same faction
          (store_troop_faction, ":target_faction", ":target_npc"),
          (store_troop_faction, ":asker_faction", ":asker"),
          (try_begin),
             #Special handling needed for player faction
             (eq, ":asker", "trp_player"),
             (neg|eq, ":target_faction", ":asker_faction"),
             (assign, ":asker_faction", "$players_kingdom"),
          (try_end),
          (this_or_next|eq, ":target_faction", ":asker_faction"),
             (this_or_next|faction_slot_eq,":target_faction",slot_faction_leader,":asker"),
             (faction_slot_eq,":asker_faction",slot_faction_leader,":target_npc"),
          #Get prosperity for use in later tests
          (party_get_slot, ":target_prosperity", ":target_fief", slot_town_prosperity),
          (party_get_slot, ":offered_prosperity", ":offered_fief", slot_town_prosperity),
          (store_div, ":min_prosperity", ":target_prosperity", 10),
          (val_mul, ":min_prosperity", 10),
          #...take into account relation
          (call_script, "script_troop_get_relation_with_troop", ":target_npc", ":asker"),
          (store_div, ":relation_div_10", reg0, 10),
          (val_sub, ":min_prosperity", ":relation_div_10"),
          #...take into account persuasion
          (store_skill_level, ":asker_persuasion", "skl_persuasion", ":asker"),
          (val_sub, ":min_prosperity", ":asker_persuasion"),
          #...take into account personal (not party) trade skill
          (store_skill_level, ":asker_trade", "skl_trade", ":asker"),
          (val_sub, ":min_prosperity", ":asker_trade"),
          #...don't let it rise above original's prosperity.
          (val_min, ":min_prosperity", ":target_prosperity"),
          #target_type 1 = village, 2 = castle, 3 = town
		  (assign, ":target_type", 0),
          (try_begin),
            (party_slot_eq, ":target_fief", slot_party_type, spt_town),
            (assign, ":target_type", 3),
          (else_try),
            (party_slot_eq, ":target_fief", slot_party_type, spt_castle),
            (assign, ":target_type", 2),
          (else_try),
  		    (party_slot_eq, ":target_fief", slot_party_type, spt_village),
            (assign, ":target_type", 1),
          (try_end),
		  (ge, ":target_type", 1),#break with error if the type was bad
          #offered_type: 1 = village, 2 = castle, 3 = town
		  (assign, ":offered_type", 0),
          (try_begin),
            (party_slot_eq, ":offered_fief", slot_party_type, spt_town),
            (assign, ":offered_type", 3),
          (else_try),
            (party_slot_eq, ":offered_fief", slot_party_type, spt_castle),
            (assign, ":offered_type", 2),
          (else_try),
			(party_slot_eq, ":offered_fief", slot_party_type, spt_village),
            (assign, ":offered_type", 1),
          (try_end),
		  (ge, ":offered_type", 1),#break with error if the type was bad
          #Now execute comparison logic:
          (try_begin),
            #refuse to trade town for a castle or village
            (lt, ":offered_type", ":target_type"),
            (eq, ":target_type", 3),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_town"),
          (else_try),
            #refuse to trade any better type for a worse type
            (lt, ":offered_type", ":target_type"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_castle"),
          (else_try),
            #refuse to trade for something under siege or being raided
            (this_or_next|party_slot_eq, ":offered_fief", slot_village_state, svs_under_siege),
            (party_slot_eq, ":offered_fief", slot_village_state, svs_being_raided),
            (str_store_party_name, s14, ":offered_fief"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_s14_attack"),
          (else_try),
            #accept a trade if the offered type is better
            (lt, ":target_type", ":offered_type"),
            (str_store_string, s14, "str_dplmc_fief_exchange_accept"),
            (assign, ":result", 0),
		  (else_try),
			#refuse to trade away home center (unless trading up for a better type)
			#Target fief is home of NPC...
			(this_or_next|party_slot_eq, ":target_fief", dplmc_slot_center_original_lord, ":target_npc"),
			   (troop_slot_eq, ":target_npc", slot_troop_home, ":target_fief"),
			(neg|party_slot_eq, ":offered_fief", dplmc_slot_center_original_lord, ":target_npc"),
			#...and offered fief is not.
			(neg|troop_slot_eq, ":target_npc", slot_troop_home, ":offered_fief"),
			(this_or_next|neg|is_between, ":target_npc", companions_begin, companions_end),
				(neg|troop_slot_eq, ":target_npc", slot_troop_town_with_contacts, ":offered_fief"),
			(str_store_party_name, s14, ":target_fief"), #Line added by zerilius
			(str_store_string, s14, "str_dplmc_fief_exchange_refuse_home"),
          (else_try),
            #refuse trade if prosperity is too low
            (lt, ":offered_prosperity", ":min_prosperity"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_rich"),
          (else_try),
            #accept trade for 0 or more denars
            (store_sub, ":result", ":target_prosperity", ":offered_prosperity"),
            (val_mul, ":result", ":target_type"),
            (val_mul, ":result", 36),#Should probably be 60 instead
            #(val_div, ":result", 100),
            (val_add, ":result", 2000),
            (val_max, ":result", 0),
            (try_begin),
               (ge, ":result", 1),
               (assign, reg3, ":result"),
               (str_store_string, s14, "str_dplmc_fief_exchange_accept_reg3_denars"),
            (else_try),
               (str_store_string, s14, "str_dplmc_fief_exchange_accept"),
            (try_end),
          (try_end),
      (try_end),
      (assign, reg0, ":result"),
    ]),

  # script_dplmc_time_sorted_heroes_for_center_aux
  # For internal use only
  # param 1: center no
  # param 2: party_no_to_collect_heroes
  # param 3: minimum time since last met (inclusive), or negative for no restriction
  # param 4: maximum time since last met (exclusive), or negative for no restriction
  ("dplmc_time_sorted_heroes_for_center_aux",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":party_no_to_collect_heroes"),
      (store_script_param, ":min_time", 3),
      (store_script_param, ":max_time", 4),

      (store_current_hours, ":current_hours"),

      (party_get_num_companion_stacks, ":num_stacks",":center_no"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
        (troop_is_hero, ":stack_troop"),
        #get time since last talk
        (troop_get_slot, ":troop_last_talk_time", ":stack_troop", slot_troop_last_talk_time),
        (store_sub, ":time_since_last_talk", ":current_hours", ":troop_last_talk_time"),
        #add if time meets constraints
        (this_or_next|ge, ":time_since_last_talk", ":min_time"),
           (lt, ":min_time", 0),
        (this_or_next|lt, ":time_since_last_talk", ":max_time"),
           (lt, ":max_time", 0),
        (party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
      (try_end),
      (party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
      (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
        (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
        (call_script, "script_dplmc_time_sorted_heroes_for_center_aux", ":attached_party", ":party_no_to_collect_heroes",":min_time",":max_time"),
      (try_end),
  ]),

  # script_dplmc_time_sorted_heroes_for_center
  # Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
  # Output: none, adds heroes to the party_no_to_collect_heroes party
  # The catch is that it returns heroes who haven't been met in a day
  # or more before others, for greater use in feasts.
  ("dplmc_time_sorted_heroes_for_center",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":party_no_to_collect_heroes"),
      (party_clear, ":party_no_to_collect_heroes"),

      #SB: include these heroes in sorting
      (try_begin),
        (eq, "$g_player_court", ":center_no"),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"),
        ##diplomacy start+
        #It's not exactly clear if this would work for kingdom ladies.  If they
        #can go from slto_kingdom_lady to slto_inactive, this could take them
        #from there to slto_kingdom_hero unintentionally.
        #
        #Because of this, don't enable this for now.  Elsewhere (where defections
        #occur) add alternate behavior for promoted kingdom ladies.
        #
        #TODO: Later, make sure that kingdom ladies are never inactive normally,
        #so this loop can be expanded to work with them.
        ##diplomacy end+
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
          (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
          (eq, ":active_npc_faction", "fac_player_supporters_faction"),
          (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
          (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
          (neg|troop_slot_ge, ":active_npc", slot_troop_leaded_party, 0), #if he/she does not have a party
          (neq, ":active_npc", "$g_player_minister"),
          (party_add_members, ":party_no_to_collect_heroes", ":active_npc", 1), #SB : lol bugfix
          # (set_visitor, ":cur_pos", ":active_npc"),
          # (val_add,":cur_pos", 1),
        (try_end),
      (try_end),

     #Non-attached pretenders (make sure they're not thrown under the bus)
     (try_for_range, ":pretender", pretenders_begin, pretenders_end),
        (neq, ":pretender", "$supported_pretender"),
        (troop_slot_eq, ":pretender", slot_troop_cur_center, ":center_no"),
        (party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
     (try_end),

     #Heroes you haven't spoken to in 24+ hours
     (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",
         ":center_no", ":party_no_to_collect_heroes", 24, -1),

     #Heroes you haven't spoken to in 12 to 24 hours
     (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",
         ":center_no", ":party_no_to_collect_heroes", 12, 24),

     #Everyone else
     (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",
         ":center_no", ":party_no_to_collect_heroes", -1, 12),
  ]),

  # script_script_dplmc_faction_leader_splits_gold
  # INPUT: arg1 = troop_id, arg2 = new faction_no
  # OUTPUT: none
  ("dplmc_faction_leader_splits_gold",
    [
	(store_script_param_1, ":faction_no"),
    (store_script_param_2, ":king_gold"),
	(assign, ":push_reg0", reg0),#revert register value at end of script
	(assign, ":push_reg1", reg1),#revert register value at end of script

	(faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
	(faction_get_slot, reg0, ":faction_no", dplmc_slot_faction_centralization),
	(val_clamp, reg0, -3, 4),
	(val_mul, reg0, -5),
	(try_begin),
		(troop_slot_ge, ":faction_liege", slot_troop_wealth, 20000),
		(val_add, reg0, 20),#20% if the king is at or above his starting gold
	(else_try),
		(val_add, reg0, 50),#50% otherwise
	(try_end),
	(val_add, reg0, 50),
	(store_mul, ":lord_gold", ":king_gold", reg0),#king splits other half among lords
	(val_div, ":lord_gold", 100),
	(val_sub, ":king_gold", ":lord_gold"),
	(try_begin),
		#If there's enough gold to give a meaningful amount to everyone, do so.
		#(This accomplishes two things.  It makes the distribution more even, and
		#it prevents this script from taking an unreasonably long time for very
		#large amounts of gold.)
		#
		#"Meaningful" is at least 300, because that's the minimum amount of gold a
		#lord will to to a fief to collect (it is also the AI recruitment cost on
		#hard).
		(assign, ":num_lords", 0),#<-- number of lords in faction, not including faction leader
		(try_for_range, ":lord_no", heroes_begin, heroes_end),
			(store_troop_faction, ":lord_faction_no", ":lord_no"),
			(eq, ":faction_no", ":lord_faction_no"),
			(troop_set_slot, ":lord_no", slot_troop_temp_slot, 0),
			(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
			(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
			(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
			(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
			(ge, ":lord_party", 0),
			(val_add, ":num_lords", 1),
		(try_end),
		(try_begin),
			#handle player
			(eq, "$players_kingdom", ":faction_no"),
			(neq, "trp_player", ":faction_liege"),
			(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
			(val_add, ":num_lords", 1),
		(try_end),
		(gt, ":num_lords", 0),#<-- can fail
		(store_div, ":gold_to_each", ":lord_gold", ":num_lords"),
		(ge, ":gold_to_each", 300),
		(val_div, ":gold_to_each", 150),#regularize (standard reinforcement costs for easy/medium/hard are 600/450/300, which are multiples of 150)
		(val_mul, ":gold_to_each", 150),

		#(try_begin),
		#	(ge, "$cheat_mode", 1),
		#	(assign, reg0, ":num_lords"),
		#	(assign, reg1, ":gold_to_each"),
		#	(str_store_faction_name, s5, ":faction_no"),
		#	(display_message, "@ {reg0} vassals of the {s5} receive {reg1} denars each (dplmc_faction_leader_splits_gold)"),
		#(try_end),

		(try_for_range, ":lord_no", heroes_begin, heroes_end),
			(ge, ":lord_gold", ":gold_to_each"),
			#verify lord is vassal of kingdom
			(store_troop_faction, ":lord_faction_no", ":lord_no"),
			(eq, ":faction_no", ":lord_faction_no"),
			(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
			(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
			(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
			(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
			(ge, ":lord_party", 0),
			#give gold to lord
			(val_sub, ":lord_gold", ":gold_to_each"),
			#(troop_get_slot, reg0, ":lord_no", slot_troop_temp_slot),
			#(val_add, reg0, ":gold_to_each"),
			#(troop_set_slot, ":lord_no", slot_troop_temp_slot, reg0),
			##(call_script, "script_troop_add_gold", ":lord_no", ":gold_to_each"),
			(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_to_each", ":lord_no"),
		(try_end),
		(try_begin),
			(ge, ":lord_gold", ":gold_to_each"),
			#give gold to player if player is vassal of kingdom
			(eq, "$players_kingdom", ":faction_no"),
			(neq, "trp_player", ":faction_liege"),
			(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
			(val_sub, ":lord_gold", ":gold_to_each"),
			(troop_get_slot, reg0, "trp_player", slot_troop_temp_slot),
			(val_add, reg0, ":gold_to_each"),
			(troop_set_slot, "trp_player", slot_troop_temp_slot, reg0),
			##(call_script, "script_troop_add_gold", ":lord_no", ":gold_to_each"),
		(try_end),
	(try_end),
	#Now, distribute the remaining gold.  Assign gold in increments of 300,
	#because that's the minimum amount of gold a lord will go to a fief for
	#(also the AI recruitment cost on hard).
	(store_div, ":count", ":lord_gold", 300),
	(val_max, ":count", 1),
	(try_for_range, ":unused", 0, ":count"),
		(ge, ":lord_gold", 300),
		(call_script, "script_cf_get_random_lord_except_king_with_faction", ":faction_no"),
		(is_between, reg0, heroes_begin, heroes_end),
		(assign, ":troop_no", reg0),
		(val_sub, ":lord_gold", 300),
		(troop_get_slot, reg0, ":troop_no", slot_troop_temp_slot),
		(val_add, reg0, 300),
		(troop_set_slot, ":troop_no", slot_troop_temp_slot, reg0),
		#(call_script, "script_troop_add_gold", ":troop_no", 300),
	(try_end),

	#Now the distribution is set.  Give each one his allotment.
	(try_for_range, ":lord_no", heroes_begin, heroes_end),
		(ge, ":lord_gold", ":gold_to_each"),
		#verify lord is vassal of kingdom
		(store_troop_faction, ":lord_faction_no", ":lord_no"),
		(eq, ":faction_no", ":lord_faction_no"),
		(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
		(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
		(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
		(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
		(ge, ":lord_party", 0),
		#get promised gold
		(troop_get_slot, reg0, ":lord_no", slot_troop_temp_slot),
		(neq, reg0, 0),
		#(try_begin),
		#	(ge, "$cheat_mode", 1),
		#	(str_store_troop_name, s4, ":lord_no"),
		#	(str_store_faction_name, s5, ":faction_no"),
		#	(str_store_troop_name, s6, ":faction_liege"),
		#	(display_message, "@{!}{s4} of the {s5} receives {reg0} denars (dplmc_faction_leader_splits_gold)"),
		#(try_end),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", reg0, ":lord_no"),
		(troop_set_slot, ":lord_no", slot_troop_temp_slot, 0),
	(try_end),

	(val_add, ":king_gold", ":lord_gold"),#Give remaining gold to king
	(try_begin),
		(ge, "$cheat_mode", 1),
		(str_store_troop_name, s4, ":troop_no"),
		(str_store_faction_name, s5, ":faction_no"),
		(str_store_troop_name, s6, ":faction_liege"),
		(display_message, "@{!}{s6} of the {s5} retains the remaining {reg0} denars (dplmc_faction_leader_splits_gold)"),
	(try_end),

	#(call_script, "script_troop_add_gold", ":faction_liege", ":king_gold"),
	(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":king_gold", ":faction_liege"),
	(assign, reg0, ":push_reg0"),#revert register value
	(assign, reg1, ":push_reg1"),#revert register value
	]),


  #script_dplmc_lord_return_from_exile
  # INPUT: arg1 = troop_id, arg2 = new faction_no
  # OUTPUT: none
  ("dplmc_lord_return_from_exile",
    [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":faction_no"),
      #Check validity
	  (try_begin),
		  (is_between, ":troop_no", heroes_begin, heroes_end),
		  (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
		  (neq, ":troop_no", "trp_player"),
		  (faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
		  #The lord definitely should not already belong to a kingdom
		  (store_troop_faction, ":old_faction", ":troop_no"),
		  (neg|is_between, ":old_faction", kingdoms_begin, kingdoms_end),
		  (try_begin),
			#Handle separately for adding to the player's faction
			#The player may decide to accept or reject the return
			(this_or_next|eq, ":faction_liege", "trp_player"),
			(eq, ":faction_no", "fac_player_supporters_faction"),
			#(eq, 1, 0),#<-- temporarily disable
			#Lord comes to petition the player instead of automatically returning
			(call_script, "script_change_troop_faction", ":troop_no", ":faction_no"),
			(troop_set_slot, ":troop_no", slot_troop_occupation, slto_inactive),
			#Show event (no log without actual faction change)
			(str_store_troop_name_link, s4, ":troop_no"),
			(str_store_faction_name_link, s5, ":faction_no"),
			(faction_get_color, ":color", ":faction_no"), #SB : store colour for logs
			(str_store_troop_name_link, s6, ":faction_liege"),
			(display_message, "@{s4} has returned from exile, seeking refuge with {s6} of {s5}.", ":color"),
		    #Remove party
			(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
			(try_begin),
				(party_is_active, ":led_party"),
				(neq, ":led_party", "p_main_party"),
				(remove_party, ":led_party"),
				(troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
			(try_end),
			#
		  (else_try),
			 #NPC king auto-accepts
			 #Normalize relation between NPC and king
			 (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_liege"),
			 (store_sub, ":relation_change", 0, reg0),#enough to increase to 0 if negative
			 (val_max, ":relation_change", 5),
			 (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_liege", ":relation_change"),
			 #Perform reverse of relation change for exile
			 (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end), #all lords in own faction, and relatives regardless of faction
				(assign, ":relation_change", 0),#no change for non-relatives in other factions
				(try_begin),
					(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
					(eq, ":faction_no", ":active_npc_faction"),
					#Auto-exiling someone at -75 relation to his liege gives a -1 base
					#relation penalty from other lords, so the gain is 1 by default.
					(assign, ":relation_change", 1),
				(try_end),
				##(call_script, "script_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
				(assign, ":family_relation", reg0),
				(try_begin),
					(gt, ":family_relation", 1),
					(store_div, ":family_modifier", reg0, 3),
					(val_add, ":relation_change", ":family_modifier"),
				(try_end),

				(neq, ":relation_change", 0),

				(call_script, "script_troop_change_relation_with_troop", ":faction_liege", ":active_npc", ":relation_change"),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s17, ":active_npc"),
					(str_store_troop_name, s18, ":faction_liege"),
					(assign, reg3, ":relation_change"),
					(display_message, "str_trial_influences_s17s_relation_with_s18_by_reg3"),
				(try_end),
			 (try_end),#end try for range :active_npc

			#Now actually change the faction
			(call_script, "script_change_troop_faction", ":troop_no", ":faction_no"),
			(try_begin), #new-begin
				(neq, ":faction_no", "fac_player_supporters_faction"),
				(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_retirement),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile), #SB : revoke exile
				(troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		    (try_end), #new-end

			#Log event
			(str_store_troop_name_link, s4, ":troop_no"),
			(str_store_faction_name_link, s5, ":faction_no"),
			(str_store_troop_name_link, s6, ":faction_liege"),
			(faction_get_color, ":color", ":faction_no"), #SB : store colour for logs
			(display_log_message, "@{s4} has been granted a pardon by {s6} of {s5} and has returned from exile.", ":color"),

            #SB : spawn full army
            (troop_set_slot, ":troop_no", slot_troop_spawned_before, 0),
			(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
			(try_begin),
				(party_is_active, ":led_party"),
				(neq, ":led_party", "p_main_party"),
				(remove_party, ":led_party"),
				(troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
			(try_end),
		  (try_end),#end NPC king auto-accepts
      (else_try),
	    #Failure.  Perform string register assignment first to avoid differences
		#between debug and non-debug behavior.
		(str_store_troop_name, s5, ":troop_no"),
		(str_store_faction_name, s7, ":faction_no"),
		#(ge, "$cheat_mode", 1),#<-- always show this
		(display_message, "@{!}DEBUG : failure in dplmc_lord_return_from_exile((s5}, {s7})"),
	  (try_end),
    ]),

    #script_dplmc_get_troop_morality_value
    # INPUT: arg1 = troop_id, arg2 = morality type
    # OUTPUT: reg0 has morality value, or 0 if inapplicable
    ("dplmc_get_troop_morality_value",
	[
		(store_script_param, ":troop_id", 1),
		(store_script_param, ":morality_type", 2),

		(assign, reg0, 0),
		(try_begin),
			(neg|is_between, ":troop_id", companions_begin, companions_end),#<-- result is 0 for non-companions
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_morality_type, ":morality_type"),
			(troop_get_slot, reg0, ":troop_id", slot_troop_morality_value),
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_2ary_morality_type, ":morality_type"),
			(troop_get_slot, reg0, ":troop_id", slot_troop_2ary_morality_value),
		(try_end),

	]),

    #script_dplmc_print_subordinate_says_sir_madame_to_s0
    #
    #In a number of circumstances a subordinate (a soldier in the player's employ) will refer
    #to him as "sir" or "madame".  This is intended as a sign of respect, but becomes
    #unintentionally disrespectful if the player would ordinarily merit a higher title.
    #
    #This function does not take into account the personal characteristics of the speaker in
    #any way.  That logic should occur elsewhere.
    #
    #input: none
    #output: reg0 gets a number corresponding to the title used
    ("dplmc_print_subordinate_says_sir_madame_to_s0",
        [
        (assign, ":highest_honor", 1),#{sir/madame}
        #1: str_dplmc_sirmadame
        #2: str_dplmc_my_lordlady
        #3: str_dplmc_your_highness
        (try_begin),
            #disable extra honors when the player is not recognized
            (gt, "$sneaked_into_town", disguise_none),
            (assign, ":highest_honor", 1),
        (else_try),
            #initialize variables for following steps
            (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
            (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
            #check if the player is the spouse of one of a widely recognized monarch,
            #or if the player is the ruler of one of the starting kingdoms (this can't happen but check anyway)
            (ge, ":player_spouse", 1),
            (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
                (this_or_next|faction_slot_eq, ":faction_no", slot_faction_leader, "trp_player"),
                (faction_slot_eq, ":faction_no", slot_faction_leader, ":player_spouse"),
                (val_max, ":highest_honor", 3),
            (try_end),
            (this_or_next|is_between, ":player_spouse", kings_begin, kings_end),
            (this_or_next|is_between, ":player_spouse", pretenders_begin, pretenders_end),
                (ge, ":highest_honor", 3),
            (val_max, ":highest_honor", 3),
            #Do not continue, since you've already used the highest available honor.
        (else_try),
            #the player is head of his own faction
            (ge, "$players_kingdom", 0),
            #faction leader is player, or faction leader is spouse and spouse is valid
            (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                (faction_slot_eq, "$players_kingdom", slot_faction_leader, ":player_spouse"),
            (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                (ge, ":player_spouse", 1),

            (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
            (try_begin),
                #If you have sufficient right-to-rule and renown, your subjects
                #will call you "highness".
                (ge, "$player_right_to_rule", 10),
                (store_sub, reg0, 75 + 75, "$player_right_to_rule"),
                (val_mul, reg0, 1200 // 75),#minimum required renown (as an aside, 1200 is evenly divisibly by 75)
                #examples: at right to rule 50, renown must be at least 1600
                #          at right to rule 99, renown must be at least 816
                #          at right to rule 10, renown must be at least 2240
                (ge, ":player_renown", reg0),
                (val_max, ":highest_honor", 3),
            (else_try),
                #"Highness" is also used if the player's kingdom holds meaningful territory.
                (try_begin),
                    #Recalculate the cached value if it's suspicious
                    (faction_slot_eq, "$players_kingdom", slot_faction_num_castles, 0),
                    (faction_slot_eq, "$players_kingdom", slot_faction_num_towns, 0),
                    (call_script, "script_faction_recalculate_strength", "$players_kingdom"),
                (else_try),
                    #Recalculate the cached value if it's obviously wrong
                    (this_or_next|neg|faction_slot_ge, "$players_kingdom", slot_faction_num_castles, 0),
                    (neg|faction_slot_ge, "$players_kingdom", slot_faction_num_towns, 0),
                    (call_script, "script_faction_recalculate_strength", "$players_kingdom"),
                (try_end),
                #Territory points: castles = 2, towns = 3 (ignore villages)
                (faction_get_slot, ":territory_points", "$players_kingdom", slot_faction_num_towns),
                (val_mul, ":territory_points", 3),
                (faction_get_slot, reg0, "$players_kingdom", slot_faction_num_castles),
                (val_add, ":territory_points", reg0),
                (val_add, ":territory_points", reg0),
                #If the player owns even a single center, that's worth at least "my lord" from his followers
                (ge, ":territory_points", 1),
                (val_max, ":highest_honor", 2),
                #By default there are around 48 castles and 22 towns on the map, for a total of 70
                #centers, and 162 "points" if weighting castles = 2 and towns = 3.
                (store_sub, ":global_points", towns_end, towns_begin),
                (val_mul, ":global_points", 3),
                (store_sub, reg0, castles_end, castles_begin),
                (val_add, ":global_points", reg0),
                (val_add, ":global_points", reg0),
                #By default there are 6 NPC kingdoms, averaging 8 castles and 3.66... towns or
                #27 points each (although the initial distribution of territory is not even).
                (store_sub, ":number_kingdoms", npc_kingdoms_end, npc_kingdoms_begin),
                (val_max,  ":number_kingdoms", 1),
                #Territory must be at least 3/4 the total points divided by number of initial kingdoms.
                #Right to rule applied as a percentage bonus, scaled so that you gain recognition with
                #75% right to rule and a 50% size kingdom.

                #What I want is: ( (RtR * 2/3) + 100 ) * territory * kingdoms >= globe * 3/4
                #This is equivalent to: (RtR * 2 + 300) * territory * kingdoms * 4 >= globe * 9
                #The re-ordering is because of rounding.
                (store_mul, ":target_points", ":global_points", 9),
                (store_mul, reg0, "$player_right_to_rule", 2),
                (val_add, reg0, 300),
                (val_mul, reg0, ":territory_points"),
                (val_mul, reg0, ":number_kingdoms"),
                (val_mul, reg0, 4),
                (ge, reg0, ":target_points"),
                (val_max, ":highest_honor", 3),
            (try_end),
            #stop evaluation if you reached highest honor
            (ge, ":highest_honor", 3),
        (else_try),
            #the player is a vassal of one of the initial kingdoms
            (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
            (val_max, ":highest_honor", 1),
            (eq, "$player_has_homage", 1),#<- can fail
            (val_max, ":highest_honor", 2),
        (try_end),

        (try_begin),
           (ge, ":highest_honor", 3),
           (str_store_string, s0, "str_dplmc_your_highness"),
        (else_try),
           (eq, ":highest_honor", 2),
           (str_store_string, s0, "str_dplmc_my_lordlady"),
        (else_try),
           (str_store_string, s0, "str_dplmc_sirmadam"),
        (try_end),

          ##Special cases
        (try_begin),
          (eq, "$sneaked_into_town", disguise_none),
          (is_between, "$g_talk_troop", companions_begin, companions_end),
          (ge, ":highest_honor", 1),
          (neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
          (this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_inactive),
          (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
          (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
          (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
          (ge, ":honorific", "str_npc1_honorific"),
          (str_store_string, s0, ":honorific"),
        (else_try),
          (eq, ":highest_honor", 1),
          (is_between, "$g_talk_troop", heroes_begin, heroes_end),
          (str_store_string, s0, "str_dplmc_sirmadame"),
        (try_end),

        (assign, reg0, ":highest_honor"),
    ]),


	#"script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0"
	#
	#In a number of circumstances a commoner, who might or might not be a subject of
	#the player, will refer to him as "sir" or "madame."  This script determines whether
	#a different title would be warranted.
	#
	#input: party_no (usually a village or town)
	#output: reg0 gets a number corresponding to the title used
	("dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", [
		(store_script_param_1, ":party_no"),

		(assign, ":title_level", 1),
		(str_store_string, s0, "str_dplmc_sirmadam"),
		(store_faction_of_party, ":party_faction"),

		(try_begin),
			(eq, "$sneaked_into_town", disguise_none),#disable extra honors when the player is not recognized
			(ge, ":party_no", 0),

			#This is used in various conditions below, so I am calling it once
			#for simplicity.
			(assign, ":save_g_talk_troop", "$g_talk_troop"),
			(assign, ":save_g_encountered_party", "$g_encountered_party"),
            (try_begin),
              (neq, ":party_no", "$g_encountered_party"),
              (assign, "$g_encountered_party", -1),
              (assign, "$g_talk_troop", -1),
            (try_end),
			(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
			(assign, ":title_level", reg0),
			(assign, "$g_encountered_party", ":save_g_encountered_party"),
			(assign, "$g_talk_troop", ":save_g_talk_troop"),

			(try_begin),
				#The player is a full member of the faction: use full honors
				(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
				(ge, reg0, DPLMC_FACTION_STANDING_DEPENDENT),
				#(nothing more needs to be done)
			(else_try),
				#the faction has recognized him formally: use full honors
				(this_or_next|eq, ":party_no", "p_main_party"),
				(this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
				   (faction_slot_ge, ":party_faction", slot_faction_recognized_player, 1),
				#(nothing more needs to be done)
			(else_try),
				#The player is the lord of the town: keep result from script_dplmc_print_subordinate_says_sir_madame_to_s0
				(is_between, ":party_no", centers_begin, centers_end),
				(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
				#(nothing more needs to be done)
			(else_try),
				#Subjects of neutral kingdoms will use titles up to "my lord".
				(store_relation, ":relation", "fac_player_supporters_faction", ":party_faction"),
				(ge, ":relation", 0),
				(try_begin),
					(ge, ":title_level", 3),
					(assign, ":title_level", 2),
					(str_store_string, s0, "str_dplmc_my_lordlady"),
				(try_end),
			(else_try),
				#Subjects of kingdoms at war (that do not recognize the player) and all cases not
				#yet mentioned will reduce the "level" of the title awarded to the player by 1, to
				#a minimum of 1.
				(try_begin),
					(ge, ":title_level", 3),
					(assign, ":title_level", 2),
					(str_store_string, s0, "str_dplmc_my_lordlady"),
				(else_try),
					(eq, ":title_level", 2),
					(assign, ":title_level", 1),
				   (str_store_string, s0, "str_dplmc_sirmadam"),
				(try_end),
			(try_end),
		(try_end),

		##Special cases
		(try_begin),
			(neq, ":party_no", "$g_encountered_party"),
		(else_try),
			(eq, "$sneaked_into_town", disguise_none),
			(ge, ":title_level", 1),
			(is_between, "$g_talk_troop", companions_begin, companions_end),
			(neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
			(this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_inactive),
				(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
			(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
			(troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
			(ge, ":honorific", "str_npc1_honorific"),
			(str_store_string, s0, ":honorific"),
		(else_try),
			(eq, ":title_level", 1),
			(is_between, "$g_talk_troop", heroes_begin, heroes_end),
			(assign, ":title_level", "str_dplmc_sirmadame"),
		(try_end),

		(assign, reg0, ":title_level"),

		##Switch to cultural equivalents
      #(try_begin),
		#   (eq, ":party_no", "$g_encountered_party"),
		#   (is_between, "$g_talk_troop", heroes_begin, heroes_end),
	   #   (troop_get_slot, ":culture_faction", "$g_talk_troop", slot_troop_original_faction),
		#   (is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
		#(else_try),
		#   (eq, ":party_no", "$g_encountered_party"),
		#   (ge, "$g_talk_troop", soldiers_begin),
		#   (store_faction_of_troop, ":culture_faction", "$g_talk_troop"),
		#	(is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
		#(else_try),
      #   (is_between, ":party_no", centers_begin, centers_end),
      #   (party_get_slot, ":culture_faction", ":party_no", slot_center_original_faction),
  		#	(is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
		#(else_try),
		#   (assign, ":culture_faction", ":party_faction"),
		#(try_end),
		#(try_begin),
		#   (is_between, "$g_talk_troop", companions_begin, companions_end),#do not switch
		#(else_try),
		#  (eq, ":title_level", 1),
		#	(eq, ":culture_faction", "fac_kingdom_6"),
		#	(str_store_string, s0, "@{!}{sahib/sahiba}"),
		#(try_end),
	]),

  ##script_cf_dplmc_troop_is_female
  #
  #This exists to make it easy to modify this to work with mods that redefine the troop types.
  #See script_dplmc_store_troop_is_female
  #
  #INPUT: arg1: troop_no
  #OUTPUT: none
  ("cf_dplmc_troop_is_female",
  [
	(store_script_param_1, ":troop_no"),
	(assign, ":is_female", 0),
	(ge, ":troop_no", 0),#Undefined behavior when the arguments are invalid.
	(try_begin),
	   (eq, ":troop_no", active_npcs_including_player_begin),
	   (assign, ":troop_no", "trp_player"),
	(try_end),
  	(troop_get_type, ":is_female", ":troop_no"),
	#The following will make it so, for example, tf_undead does not appear to be female.
	#Mods where this is relevant will likely want to tweak it, but this will work in at
	#least one that I know of that has non-human lords.
	(eq, ":is_female", tf_female),
  ]),

  ##script_dplmc_store_troop_is_female
  #
  #This exists to make it easy to modify this to work with mods that redefine the troop types.
  #
  #If you change this, remember to also change script_cf_dplmc_troop_is_female and
  #script_dplmc_store_is_female_troop_1_troop_2
  #
  #INPUT: arg1: troop_no
  #
  #OUTPUT:
  #       reg0: 1 is yes, 0 is no
  ("dplmc_store_troop_is_female",
  [
    (store_script_param_1, ":troop_no"),
    (try_begin),
       (eq, ":troop_no", active_npcs_including_player_begin),
       (assign, ":troop_no", "trp_player"),
    (try_end),
    (troop_get_type, reg0, ":troop_no"),
    (try_begin), #SB : use consts
        (neq, reg0, tf_male),
        (neq, reg0, tf_female),
        (assign, reg0, 0),#e.g. this would apply to tf_undead
    (try_end),
  ]),

  ("dplmc_store_troop_is_female_reg",
  [
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":reg_no"),
    (troop_get_type, ":is_female", ":troop_no"),
    #The following will make it so, for example, tf_undead does not appear to be female.
    #Mods where this is relevant will likely want to tweak it, but this will work in at
    #least one that I know of that has non-human lords.
    (try_begin), #SB : use consts
        (neq, ":is_female", 0),
        (neq, ":is_female", 1),
        (assign, ":is_female", 0),
    (try_end),
        ##Can asign to registers 0,1,2,3, 65, or 4
    (try_begin),
      (eq, ":reg_no", 4),
      (assign, reg4, ":is_female"),
    (else_try),
      (eq, ":reg_no", 3),
      (assign, reg3, ":is_female"),
    (else_try),
      (eq, ":reg_no", 2),
      (assign, reg2, ":is_female"),
    (else_try),
      (eq, ":reg_no", 1),
      (assign, reg1, ":is_female"),
    (else_try),
      (eq, ":reg_no", 0),
      (assign, reg0, ":is_female"),
    (else_try),
      (eq, ":reg_no", 65),
      (assign, reg65, ":is_female"),
    (else_try),
      ##default to reg4
      (assign, reg4, ":reg_no"),
      (display_message, "@{!} ERROR: called script dplmc-store-troop-is-female-reg with bad argument {reg4}"),
      (assign, reg4, ":is_female"),
    (try_end),
  ]),

  ##script_dplmc_store_is_female_troop_1_troop_2
  #
  #This exists to make it easy to modify this to work with mods that redefine the troop types.
  #See script_dplmc_store_troop_is_female
  #
  #INPUT:
  #      arg1: troop_1
  #      arg2: troop_2
  #OUTPUT:
  #       reg0: 0 for not female, 1 for female
  #       reg1: 0 for not female, 1 for female
  ("dplmc_store_is_female_troop_1_troop_2",
  [
	(store_script_param_1, ":troop_1"),
	(store_script_param_2, ":troop_2"),
	(troop_get_type, ":is_female_1", ":troop_1"),
	(troop_get_type, ":is_female_2", ":troop_2"),
	#The following will make it so, for example, tf_undead does not appear to be female.
	#Mods where this is relevant will likely want to tweak it, but this will work in at
	#least one that I know of that has non-human lords.
	(try_begin),
		(neq, ":is_female_1", 0),
		(neq, ":is_female_1", 1),
		(assign, ":is_female_1", 0),
	(try_end),
	(try_begin),
		(neq, ":is_female_2", 0),
		(neq, ":is_female_2", 1),
		(assign, ":is_female_2", 0),
	(try_end),
	(assign, reg0, ":is_female_1"),
	(assign, reg1, ":is_female_2"),
  ]),

  #script_cf_dplmc_evaluate_pretender_proposal
  # INPUT: arg1 = troop_id for pretender
  # OUTPUT: reg0 = answer
  #
  # Writes reason to s14
  # May clobber s0, s1
  #
  ("cf_dplmc_evaluate_pretender_proposal",
    [
      (store_script_param_1, ":pretender"),
	  (assign, ":answer", -1),
	  (assign, ":save_reg1", reg1),
	  (assign, ":save_reg65", reg65),
	  (call_script, "script_dplmc_store_troop_is_female", ":pretender"),
	  (assign, reg65, reg0),

	  (str_store_string, s14, "str_ERROR_string"),

	  (is_between, ":pretender", pretenders_begin, pretenders_end),
	  (troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

	  (store_troop_faction, ":pretender_faction", ":pretender"),
	  (is_between, ":pretender_faction", npc_kingdoms_begin, npc_kingdoms_end),
	  (troop_slot_eq, ":pretender", slot_troop_original_faction, ":pretender_faction"),
	  (faction_slot_eq, ":pretender_faction", slot_faction_leader, ":pretender"),
	  (faction_slot_eq, ":pretender_faction", slot_faction_state, sfs_active),

	  (troop_slot_eq, ":pretender", slot_troop_spouse, -1),
	  (troop_slot_eq, ":pretender", slot_troop_betrothed, -1),

	  (troop_get_slot, ":pretender_renown", ":pretender", slot_troop_renown),
	  (val_max, ":pretender_renown", 1),

	  #There, we've covered the preliminaries: this should be a standard post-rebellion
	  #setup.  Now verify that the player is in a correct state.

	  (eq, "$players_kingdom", ":pretender_faction"),
	  (eq, "$player_has_homage", 1),
	  (troop_slot_eq, "trp_player", slot_troop_spouse, -1),
	  (troop_slot_eq, "trp_player", slot_troop_betrothed, -1),

	  (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
	  (call_script, "script_troop_get_player_relation", ":pretender"),
	  (assign, ":player_relation", reg0),

	  #Find competitors
	  (assign, ":b", -1),
	  (assign, ":b_relation", -101),
	  (assign, ":c", -1),
	  (assign, ":c_renown", -1),

	  (store_add, ":faction_renown", ":pretender_renown", ":player_renown"),
	  (assign, ":faction_lords", 2),#the player and the pretender

	  (troop_set_slot, ":pretender", slot_troop_temp_slot, 0),#clear
	  (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),#clear

      (try_for_range_backwards, ":competitor", heroes_begin, heroes_end),
        (troop_slot_eq, ":competitor", slot_troop_occupation, slto_kingdom_hero),
        (store_faction_of_troop, ":competitor_faction", ":competitor"),
        (eq, ":competitor_faction", ":pretender_faction"),
        (try_begin),
          (is_between, ":competitor", kings_begin, kings_end), #SB : exclude former monarchs
          (troop_slot_eq, ":competitor", slot_troop_original_faction, ":pretender_faction"),
          (troop_set_slot, ":competitor", slot_troop_temp_slot, -99999),#low value
          (assign, ":competitor_renown", 0), #do not factor in
        (else_try),
          (troop_set_slot, ":competitor", slot_troop_temp_slot, 0),#clear
          (troop_get_slot, ":competitor_renown", ":competitor", slot_troop_renown),
        (try_end),

        (neq, ":competitor", active_npcs_including_player_begin),
        (neq, ":competitor", ":pretender"),

        (call_script, "script_troop_get_relation_with_troop", ":competitor", ":pretender"),
        (assign, ":competitor_relation", reg0),

        (val_add, ":faction_renown", ":competitor_renown"),
        (val_add, ":faction_lords", 1),

        (try_begin),
           (ge, ":competitor_relation", ":b_relation"),
           (neg|troop_slot_eq, ":competitor", slot_troop_spouse, "trp_player"),
           (neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":competitor"),
           (assign, ":b", ":competitor"),
           (assign, ":b_relation", ":competitor_relation"),
        (try_end),
        (try_begin),
           (ge, ":competitor_renown", ":c_renown"),
           (assign, ":c", ":competitor"),
           (assign, ":c_renown", ":competitor_renown"),
        (try_end),
      (try_end),

      (assign, ":pretender_towns", 0),
      (assign, ":pretender_castles", 0),
      (assign, ":pretender_villages", 0),

      (assign, ":player_towns", 0),
      (assign, ":player_castles", 0),
      (assign, ":player_villages", 0),

      (assign, ":faction_towns", 0),
      (assign, ":faction_castles", 0),
      (assign, ":faction_villages", 0),

      (assign, ":original_towns", 0),
      (assign, ":original_castles", 0),
      (assign, ":original_villages", 0),

   	  #(store_sub, ":global_towns", towns_end, towns_begin),
	  #(store_sub, ":global_castles", castles_end, castles_begin),
	  #(store_sub, ":global_villages", villages_end, villages_begin),

	  (assign, ":highest_score", -1),
	  (assign, ":highest_score_lord", -1),

	  (try_for_range, ":center_no", towns_begin, towns_end),
		(store_faction_of_party, ":center_faction", ":center_no"),
		(try_begin),
			(party_slot_eq, ":center_no", slot_town_lord, ":pretender"),
			(val_add, ":pretender_towns", 1),
			(val_add, ":faction_towns", 1),
		(else_try),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			(val_add, ":player_towns", 1),
			(val_add, ":faction_towns", 1),
		(else_try),
			(this_or_next|eq, ":center_faction", ":pretender_faction"),
				(eq, ":center_faction", "fac_player_supporters_faction"),
			(val_add, ":faction_towns", 1),
			(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
			(this_or_next|eq, ":town_lord", "trp_player"),
				(is_between, ":town_lord", heroes_begin, heroes_end),
			(troop_get_slot, ":local_temp", ":town_lord", slot_troop_temp_slot),
			(val_add, ":local_temp", 3),
			(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":local_temp"),
			(ge, ":local_temp", ":highest_score"),
			(assign, ":highest_score", ":local_temp"),
			(assign, ":highest_score_lord", ":town_lord"),
		(try_end),
		(try_begin),
			(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
			(val_add, ":original_towns", 1),
		(try_end),
	  (try_end),

	  (try_for_range, ":center_no", castles_begin, castles_end),
		(store_faction_of_party, ":center_faction", ":center_no"),
		(try_begin),
			(party_slot_eq, ":center_no", slot_town_lord, ":pretender"),
			(val_add, ":pretender_castles", 1),
			(val_add, ":faction_castles", 1),
		(else_try),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			(val_add, ":player_castles", 1),
			(val_add, ":faction_castles", 1),
		(else_try),
			(this_or_next|eq, ":center_faction", ":pretender_faction"),
				(eq, ":center_faction", "fac_player_supporters_faction"),
			(val_add, ":faction_castles", 1),
			(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
			(this_or_next|eq, ":town_lord", "trp_player"),
				(is_between, ":town_lord", heroes_begin, heroes_end),
			(troop_get_slot, ":local_temp", ":town_lord", slot_troop_temp_slot),
			(val_add, ":local_temp", 2),
			(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":local_temp"),
			(ge, ":local_temp", ":highest_score"),
			(assign, ":highest_score", ":local_temp"),
			(assign, ":highest_score_lord", ":town_lord"),
		(try_end),
		(try_begin),
			(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
			(val_add, ":original_castles", 1),
		(try_end),
	  (try_end),

	  (try_for_range, ":center_no", villages_begin, villages_end),
		(store_faction_of_party, ":center_faction", ":center_no"),
		(try_begin),
			(party_slot_eq, ":center_no", slot_town_lord, ":pretender"),
			(val_add, ":pretender_villages", 1),
			(val_add, ":faction_villages", 1),
		(else_try),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			(val_add, ":player_villages", 1),
			(val_add, ":faction_villages", 1),
		(else_try),
			(this_or_next|eq, ":center_faction", ":pretender_faction"),
				(eq, ":center_faction", "fac_player_supporters_faction"),
			(val_add, ":faction_villages", 1),
			(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
			(this_or_next|eq, ":town_lord", "trp_player"),
				(is_between, ":town_lord", heroes_begin, heroes_end),
			(troop_get_slot, ":local_temp", ":town_lord", slot_troop_temp_slot),
			(val_add, ":local_temp", 1),
			(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":local_temp"),
			(ge, ":local_temp", ":highest_score"),
			(assign, ":highest_score", ":local_temp"),
			(assign, ":highest_score_lord", ":town_lord"),
		(try_end),
		(try_begin),
			(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
			(val_add, ":original_villages", 1),
		(try_end),
	  (try_end),

	  #Update stats
	  (faction_set_slot, ":pretender_faction", slot_faction_num_castles, ":faction_castles"),
	  (faction_set_slot, ":pretender_faction", slot_faction_num_towns, ":faction_towns"),

	  #Point totals used below
	  #Faction Score A: (4 * towns) + (2 * castles) + villages
	  (store_mul, ":faction_score_a", ":faction_towns", 4),
	  (val_add, ":faction_score_a", ":faction_castles"),
	  (val_add, ":faction_score_a", ":faction_castles"),
	  (val_add, ":faction_score_a", ":faction_villages"),

	  #Faction Score B: (3 * towns) + (2 * castles) + villages
	  (store_sub, ":faction_score_b", ":faction_score_a", ":faction_towns"),

	  #Original Score A: (4 * towns) + (2 * castles) + villages
	  (store_mul, ":original_score_a", ":original_towns", 4),
	  (val_add, ":original_score_a", ":original_castles"),
	  (val_add, ":original_score_a", ":original_castles"),
	  (val_add, ":original_score_a", ":original_villages"),

	  #Original Score B: (3 * towns) + (2 * castles) + villages
	  (store_sub, ":original_score_b", ":faction_score_b", ":faction_towns"),

	  #The first fail-condition encountered will be the explanation used,
	  #so make sure the most pressing ones go first.
	  (try_begin),
	      #relation low: using the same cutoff normally used for becoming a vassal
		  (lt, ":player_relation", 0),
		  (assign, ":answer", -1),
		  (str_store_string, s14, "@Given the way things stand between us at the moment, {playername}, I would not consider it prudent to enter into such an arrangement."),
	  (else_try),
         #check player right to rule
		 (store_add, ":player_score", "$player_right_to_rule", ":player_relation"),
		 (this_or_next|lt, "$player_right_to_rule", 20),#the level required for your spouse to join a rebellion
			(lt, ":player_score", 100),
		 (assign, ":answer", -1),
		 (str_store_string, s14, "@{playername}, I am grateful to you, but in the eyes of the people you do not have sufficient legitimacy as a potential co-ruler.  Marrying you would undermine my own claim to the throne."),
	  (else_try),
         #check player renown
		 (store_mul, ":min_score", ":pretender_renown", 2),
		 (val_div, ":min_score", 3),#2/3 pretender renown, 750 by default
		 (val_clamp, ":min_score", 500, 1200),#500 is the minimum to begin the claimant quest; 1200 is the initial value for original lords #SB fixed comment

		 (lt, ":player_renown", ":min_score"),
		 (assign, ":answer", -1),
		 (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_renown"),
			(assign, reg1, ":min_score"),
			(display_message, "@{!}DEBUG - player renown {reg0}, required renown {reg1}"),
		  (try_end),
		 (str_store_string, s14, "@{playername}, I know that if it were not for you I would not sit on this throne, but your name is little renowned in Calradia.  Marrying you would be perceived as an uneven match and would call into question my own claim to the throne."),
	  (else_try),
		  #check player has sufficient fiefs
		  (store_mul, ":player_score", ":player_towns", 3),
		  (val_add, ":player_score", ":player_castles"),
		  (val_add, ":player_score", ":player_castles"),
		  (val_add, ":player_score", ":player_villages"),# player_score = (3 * towns) + (2 * castles) + villages

		  (assign, ":min_score", 6),#A town, a castle, and a village; two towns; three castles; six villages; etc...

		  (try_begin),
			#Ensure the minimum is not unreasonable on small maps.
			(lt, ":original_score_b", 18),
			(lt, ":faction_score_b", 18),
			(assign, reg0, ":original_score_b"),
			(val_max, reg0, ":faction_score_b"),
			(store_div, ":min_score", reg0, 3),
		  (try_end),

		  (troop_get_slot, ":two_thirds_pretender_score", ":pretender", slot_troop_temp_slot),
		  (val_mul, ":two_thirds_pretender_score", 2),
		  (val_add, ":two_thirds_pretender_score", 1),
		  (val_div, ":two_thirds_pretender_score", 3),
		  (val_max, ":min_score", ":two_thirds_pretender_score"),

		  (lt, ":player_score", ":min_score"),
		  (assign, ":answer", -1),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_score"),
			(assign, reg1, ":min_score"),
			(display_message, "@{!}DEBUG - player score {reg0} out of a required {reg1}"),
		  (try_end),
		  (str_store_string, s14, "@{playername}, I am grateful for your assistance in regaining my rightful throne, but you do not have sufficient personal holdings to be a suitable match for me.  It would be an uneven partnership."),
     (else_try),
	      #does the player have as much renown as competitors?
		  (lt, ":player_renown", ":c_renown"),
	      (assign, ":answer", -1),
		  (str_store_troop_name, s14, ":c"),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_renown"),
			(assign, reg1, ":c_renown"),
			(display_message, "@{!}DEBUG - player score {reg0}, competitor score {reg1}"),
		  (try_end),
		  (str_store_string_reg, s0, s15),#clobber s0, save s15
		  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":c"),
		  (str_store_string, s14, "@{playername}, I am grateful to you, but if I were to accept at this time I would risk offending powerful lords such as {s15}, who may consider themselves to have honor equal to or greater than your own."),
		  (str_store_string_reg, s15, s0),#revert s15
	 (else_try),
	      #is the player outfieffed by a competitor?
          (gt, ":highest_score_lord", "trp_player"),
          (neq, ":highest_score_lord", ":pretender"),

		  (store_mul, ":player_score", ":player_towns", 3),
		  (val_add, ":player_score", ":player_castles"),
		  (val_add, ":player_score", ":player_castles"),
		  (val_add, ":player_score", ":player_villages"),# player_score = (3 * towns) + (2 * castles) + villages
             (lt, ":player_score", ":highest_score"),

		  (store_mul, reg0, ":highest_score", 3),#allow small differences
		  (val_add, reg0, 2),
		  (val_div, reg0, 4),
		  (gt, reg0, ":player_score"),

	     (assign, ":answer", -1),
		  (str_store_troop_name, s14, ":highest_score_lord"),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_score"),
			(assign, reg1, ":highest_score"),
			(display_message, "@{!}DEBUG - player score {reg0}, competitor score {reg1}"),
		  (try_end),
		  (str_store_string_reg, s0, s15),#clobber s0, save s15
		  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":highest_score_lord"),
		  (str_store_string, s14, "@{playername}, I am grateful to you, but if I were to accept at this time I would risk offending great lords such as {s15}, who may consider themselves to have honor equal to or greater than your own."),
		  (str_store_string_reg, s15, s0),#revert s15
      (else_try),
		  #does the player have as much relation as competitors?
		  (lt, ":player_relation", ":b_relation"),
		  (ge, ":b_relation", 5),
		  (assign, ":answer", -1),
		 (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_relation"),
			(assign, reg1, ":b_relation"),
			(display_message, "@{!}DEBUG - player relation {reg0}, rival relation {reg1}"),
		  (try_end),
		  (str_store_string_reg, s0, s15),#clobber s0, save s15
		  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":b"),
		  (str_store_string, s14, "@{playername}, while I am grateful to you, I must confess I am fond of {s15}."),
		  (str_store_string_reg, s15, s0),#revert s15
	  (else_try),
		  #check: sufficient lords?
		  (assign, ":needed_lords", 1),
		  (try_for_range, ":troop_no", lords_begin, lords_end),
			(troop_slot_eq, ":troop_no", slot_troop_original_faction, ":pretender_faction"),
			(val_add, ":needed_lords", 1),
		  (try_end),
		  #Must be at least 75% of original size
		  (val_mul, ":needed_lords", 3),
		  (val_div, ":needed_lords", 4),

		  (lt, ":faction_lords", ":needed_lords"),
		  (assign, ":answer", -1),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":faction_lords"),
			(assign, reg1, ":needed_lords"),
			(display_message, "@{!}DEBUG - lords in faction {reg0}, required lords {reg1}"),
		  (try_end),

		  (str_store_string, s14, "@Our realm has too few vassals.  In the current precarious state of the affairs I must use the lure of a potential political alliance to attract new vassals, and cannot yet be seen to commit to any single {reg65?suitor:candidate}."),
	  (else_try),
		  #check: pretender has enough fiefs?
		  #Must not be exceeded in fiefs by anyone in the faction.
		  (store_mul, ":pretender_score", ":pretender_towns", 3),
		  (val_add, ":pretender_score", ":pretender_castles"),
		  (val_add, ":pretender_score", ":pretender_castles"),
		  (val_add, ":pretender_score", ":pretender_villages"),
		  (troop_set_slot, ":pretender", slot_troop_temp_slot, ":pretender_score"),

		  (store_mul, reg0, ":highest_score", 3),#allow small differences
		  (val_add, reg0, 2),
		  (val_div, reg0, 4),

		  (gt, reg0, ":pretender_score"),

		  (assign, ":answer", -1),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg1, reg0),
			(assign, reg0, ":pretender_score"),
			(display_message, "@{!}DEBUG - liege has {reg0} center points, needs at least {reg1}"),
		  (try_end),
		  (str_store_string_reg, s0, s15),#clobber s0, save s15
		  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":highest_score_lord"),
		  (str_store_string, s14, "@Because I have insufficient personal holdings compared to {s15}, if I entered into such an arrangement I would risk appearing to be a puppet, throwing the stability of the realm into jeopardy."),
		  (str_store_string_reg, s15, s0),#revert s15
	 (else_try),
		  #Check if pretender has enough fiefs, part 2.
		  #Must not have fewer fief points than the number of faction points divided by the
		  #number of lords (so this condition can't be bypassed by just failing to assign
		  #centers to anyone during the rebellion)
		  (store_mul, ":points_per_lord", ":faction_towns", 3),
		  (val_add, ":points_per_lord", ":faction_castles"),
		  (val_add, ":points_per_lord", ":faction_castles"),
		  (val_add, ":points_per_lord", ":faction_villages"),
		  (val_div, ":points_per_lord", ":faction_lords"),#includes pretender so cannot be zero

		  (gt, ":points_per_lord", ":pretender_score"),

		  (assign, ":answer", -1),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":pretender_score"),
			(assign, reg1, ":points_per_lord"),
			(display_message, "@{!}DEBUG - liege has {reg0} center points, needs at least {reg1}"),
		  (try_end),
		  (str_store_faction_name, s14, ":pretender_faction"),
		  (str_store_string, s14, "@Because my personal holdings are insufficiently large compared to other lords of the {s14}, if I entered into such an arrangement I would risk appearing to be a puppet, throwing the stability of the realm into jeopardy."),
	  (else_try),
		  #check if player is widely hated in faction
		  (assign, ":total_negative", 0),
		  (assign, ":total_enemies", 0),
		  (assign, ":total_positive", 0),
		  (assign, ":total_friends", 0),
		  (try_for_range, ":troop_no", heroes_begin, heroes_end),
		     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			 (store_troop_faction, reg0, ":troop_no"),
			 (eq, reg0, ":pretender_faction"),
			 (call_script, "script_troop_get_player_relation", ":troop_no"),
			 (try_begin),
				(lt, reg0, 0),
				(val_add, ":total_negative", 1),
				(lt, reg0, -19),
				(val_add, ":total_enemies", 1),
			 (else_try),
				(gt, reg0, 0),
				(val_add, ":total_positive", 1),
				(gt, reg0, 19),
				(val_add, ":total_friends", 1),
			 (try_end),
		  (try_end),
		  #Must not have a "disapproval rating" of over 33%
		  (val_mul, ":total_enemies", 2),
		  (val_mul, ":total_negative", 2),
		  (this_or_next|gt, ":total_enemies", ":total_friends"),
		     (gt, ":total_negative", ":total_positive"),

		  (assign, ":answer", -1),
		  (str_store_faction_name, s14, ":pretender_faction"),
		  (str_store_string, s14, "@I am grateful to you, {playername}, but you have too many enemies among the lords of the {s14} for your proposal to be politically viable.  If I were to accept, there might be a revolt."),
	  (else_try),
		  #controversy must be less than 25, and less than half the relation with the liege
		  (troop_get_slot, ":controversy_2", "trp_player", slot_troop_controversy),
		  (ge, ":controversy_2", 1),
		  (val_mul, ":controversy_2", 2),
		  (this_or_next|ge, ":controversy_2", 50),
		     (ge, ":controversy_2", ":player_relation"),
		  (assign, ":answer", -1),
		  (str_store_faction_name, s14, ":pretender_faction"),
		  (str_store_string, s14, "@You have engendered too much controversy recently, {playername} .  If I were to accept at this time, there might be a revolt among the lords of the {s14}.  Let us speak of this later when the furor has died down."),
	  (else_try),
		  #check is marshall
		  (neg|faction_slot_eq, ":pretender_faction", slot_faction_marshall, "trp_player"),
		  (assign, ":answer", -2),#<-- negative two, not -1
		  (str_store_faction_name, s14, ":pretender_faction"),
		  (str_store_string, s14, "@If you desire to lead the {s14} alongside me, gather support among my vassals to become marshall, and demonstrate to them your abilities as a war leader."),
	  (else_try),
		  #player is marshall: is the territory sufficient?

		  #The faction must have at least 80% of its former territory under scoring system A or scoring system B.
		  (store_mul, ":four_fifths_original_score_a", ":original_score_a", 4),
		  (val_div, ":four_fifths_original_score_a", 5),

		  (store_mul, ":four_fifths_original_score_b", ":original_score_b", 4),
		  (val_div, ":four_fifths_original_score_b", 5),

		  (lt, ":faction_score_a", ":four_fifths_original_score_a"),
		  (lt, ":faction_score_b", ":four_fifths_original_score_b"),
		  (assign, ":answer", -3),

		  (call_script, "script_dplmc_print_centers_in_numbers_to_s0", ":original_towns", ":original_castles", ":original_villages"),
		  (str_store_string_reg, s1, s0),
		  (call_script, "script_dplmc_print_centers_in_numbers_to_s0", ":faction_towns", ":faction_castles", ":faction_villages"),

		  (str_store_faction_name, s14, ":pretender_faction"),
		  (str_store_string, s14, "@Our realm has lost too much territory.  We once held {s1} but now only hold {s0}.  In the current precarious state of affairs I must retain the possibility of a political alliance to use as a bargaining chip with the other sovereigns, so I yet be seen to commit to any single {reg65?suitor:candidate}.  Restore the {s14} to its former glory, and I will gladly have you rule beside me as my {husband/wife}."),
	  (else_try),
		 #player is marshall: are any native centers lost?

		 (str_clear, s0),
		 (str_clear, s1),
		 (assign, ":num_lost_towns_and_castles", 0),

		 (try_for_range, ":center_no", centers_begin, centers_end),
			(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
			(store_faction_of_party, ":center_faction", ":center_no"),
			(neq, ":center_faction", ":pretender_faction"),
			(neq, ":center_faction", "fac_player_supporters_faction"),
			(try_begin),
				(eq, ":num_lost_towns_and_castles", 0),
				(str_store_party_name, s0, ":center_no"),
			(else_try),
				(eq, ":num_lost_towns_and_castles", 1),
				(str_store_party_name, s1, ":center_no"),
			(else_try),
				(str_store_string, s0, "str_dplmc_s0_comma_s1"),
				(str_store_party_name, s1, ":center_no"),
			(try_end),
			(val_add, ":num_lost_towns_and_castles", 1),
		 (try_end),
		 #post-loop cleanup
		 (try_begin),
			(ge, ":num_lost_towns_and_castles", 2),
			(str_store_string, s0, "str_dplmc_s0_and_s1"),
		 (try_end),
		 #native towns lost
		 (ge, ":num_lost_towns_and_castles", 1),
		 (store_sub, reg0, ":num_lost_towns_and_castles", 1),
		 (str_store_faction_name, s14, ":pretender_faction"),
		 (str_store_string, s14, "@{s0} {reg0?have:has} been lost to foreign hands.  Restore the {s14} to its rightful boundaries, and I will gladly have you rule beside me as my {husband/wife}."),
		 (assign, ":answer", -3),
	  (else_try),
	  #Timer answer
	     (lt, "$g_player_days_as_marshal", 14),
		  (assign, reg0, "$g_player_days_as_marshal"),
		  (store_sub, reg1, reg0, 1),
		  (str_store_faction_name, s14, ":pretender_faction"),
		  (str_store_string, s14, "@You have only been marshall for {reg0} {reg1?days:day}.  Let us speak of this after you have held the post for at least two weeks."),
		  (assign, ":answer", -4),
	  (else_try),
		#In the future we may need a proper quest of some kind, or at least a timer, but this will do for now.
		(assign, ":answer", 1),
		(str_store_faction_name, s14, ":pretender_faction"),
		(str_store_string, s14, "@If not for you I would not sit on this throne, {playername}.  When we started our long walk, few people had the courage to support me.  And fewer still would be willing to put their lives at risk for my cause.  But you didn't hesitate for a moment in throwing yourself at my enemies. We have gone through a lot together, and with God's help, we prevailed.  I will gladly accept you as both my {husband/wife} and co-ruler of the {s14}."),
	  (try_end),

	  (assign, reg65, ":save_reg65"),
	  (assign, reg1, ":save_reg1"),
	  (assign, reg0, ":answer"),
  ]),

  #script_dplmc_center_point_calc
  # INPUT: arg1 = faction_id
  #        arg2 = troop_1
  #        arg2 = troop_2
  #        arg3 = town_point_value (see explanation below)
  #
  # OUTPUT:
  #        reg0 = total renown / total faction points (or 0 if no centers held)
  #        reg1 = troop_1 total (not divided)
  #        reg2 = troop_2 total (not divided)
  #        reg3 = faction average lord renown (or 0 if no lords)
  #
  #In various places the game tallies center points differently.  The values of
  #villages/castles/fiefs, respectively, in some places are 1/2/2, in other
  #places are 1/2/3, and in others are 1/3/4.
  #Specifying the town point value determines which scheme will be used to
  #determine ceter points:
  #        arg3 = 2 gives 1/2/2
  #        arg3 = 3 gives 1/2/3
  #        arg3 = 4 gives 1/2/4
  #
  #If the specified town_point_value is not 2,3, or 4, the script is allowed to
  #clamp the value or substitute a default.
  ("dplmc_center_point_calc",
    [
		(store_script_param, ":faction_id", 1),
		(store_script_param, ":troop_1", 2),
		(store_script_param, ":troop_2", 3),
		(store_script_param, ":town_point_value", 4),

		(val_clamp, ":town_point_value", 2, 5),

		#The outputs
		(assign, ":faction_score", 0),
		(assign, ":troop_1_score", 0),
		(assign, ":troop_2_score", 0),
		#(assign, ":average_renown", 0),

		#Intermediate values we use for computing outputs
		(assign, ":total_renown", 0),
		(assign, ":num_lords", 0),

		#Handle the player first
		#(assign, ":player_in_faction", 0),
		(assign, ":faction_alias", ":faction_id"),
		(try_begin),
			(this_or_next|eq, ":faction_id", "$players_kingdom"),
				(eq, ":faction_id", "fac_player_supporters_faction"),
			(val_add, ":num_lords", 1),
			(troop_get_slot, ":total_renown", "trp_player", slot_troop_renown),
			#(assign, ":player_in_faction", 1),
			(assign, ":faction_alias", "fac_player_supporters_faction"),
			(eq, ":faction_id", "fac_player_supporters_faction"),
			(assign, ":faction_alias", "$players_kingdom"),
		(try_end),

		#Get lords in faction
		(try_for_range, ":troop_no", heroes_begin, heroes_end),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(neq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
			(store_troop_faction, ":faction_no", ":troop_no"),
			(this_or_next|eq, ":faction_no", ":faction_id"),
				(eq, ":faction_no", ":faction_alias"),

			(val_add, ":num_lords", 1),
			(troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
			(val_max, ":renown", 0),
			(val_add, ":total_renown", ":renown"),
		(try_end),

		#Get stats for centers
		(try_for_parties, ":center_no"),
			(assign, ":points", 0),
			(try_begin),
				#Towns are 2, 3, or 4 points
				(this_or_next|is_between, ":center_no", towns_begin, towns_end),
				(party_slot_eq, ":center_no", slot_party_type, spt_town),
				(assign, ":points", ":town_point_value"),
			(else_try),
				#Castles are always 2 points
				(this_or_next|is_between, ":center_no", castles_begin, castles_end),
				(party_slot_eq, ":center_no", slot_party_type, spt_castle),
				(assign, ":points", 2),#castles are always 2
			(else_try),
				#Villages are always 1 point
				(this_or_next|is_between, ":center_no", villages_begin, villages_end),
				(party_slot_eq, ":center_no", slot_party_type, spt_village),
			(try_end),

			#Don't process parties that aren't centers.
			(ge, ":points", 1),

			#NB: We don't know for sure that troop_1 and troop_2 aren't the
			#same value, and we don't even necessarily know that they're part
			#of the specified faction.
			(try_begin),
				(party_slot_eq, ":center_no", slot_town_lord, ":troop_1"),
				(val_add, ":troop_1_score", ":points"),
			(try_end),

			(try_begin),
				(party_slot_eq, ":center_no", slot_town_lord, ":troop_2"),
				(val_add, ":troop_2_score", ":points"),
			(try_end),

			(store_faction_of_party, ":faction_no", ":center_no"),
			(this_or_next|eq, ":faction_no", ":faction_id"),
				(eq, ":faction_no", ":faction_alias"),
			(val_add, ":faction_score", ":points"),
		(try_end),

		# OUTPUT:
		#        reg0 = faction renown / faction points (or 0 if faction has no centers)
		#        reg1 = troop_1 total (not divided)
		#        reg2 = troop_2 total (not divided)
		#        reg3 = faction average lord renown (or 0 if no lords)
		(assign, reg0, 0),
		(try_begin),
			(neq, ":faction_score", 0),
			(store_div, reg0, ":total_renown", ":faction_score"),
		(try_end),
		(assign, reg1, ":troop_1_score"),
		(assign, reg2, ":troop_2_score"),
		(assign, reg3, 0),
		(try_begin),
			(neq, ":num_lords", 0),
			(store_div, reg0, ":total_renown", ":num_lords"),
		(try_end),
	]),


  #script_dplmc_good_produced_at_center_or_its_villages
  # For towns, also includes the villages that attach to it
  #
  # INPUT: arg1 = good_no
  #        arg2 = center_no
  # OUTPUT:
  #        reg0 = 0 if no, 1 if yes
  ("dplmc_good_produced_at_center_or_its_villages",
  [
	(store_script_param, ":good_no", 1),
	(store_script_param, ":center_no", 2),

	(assign, ":has_good", 0),
	(assign, ":save_reg1", reg1),
	(assign, ":save_reg2", reg2),
	(store_current_hours, ":cur_hours"),
	(store_sub, ":recent_time", ":cur_hours", 3 * 24),


	(try_begin),
		(is_between, ":good_no", trade_goods_begin, trade_goods_end),
		(ge, ":center_no", 1),
		(this_or_next|is_between, ":center_no", centers_begin, centers_end),
			(party_is_active, ":center_no"),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_castle),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
			(is_between, ":center_no", centers_begin, centers_end),
		(call_script, "script_center_get_production", ":center_no", ":good_no"),
		(try_begin),
			#Positive production
			(ge, reg0, 1),
			(assign, ":has_good", 1),
		(else_try),
			#Is a town or a castle, and one of its villages has positive prodution
			(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
				(party_slot_eq, ":center_no", slot_party_type, spt_castle),
			(try_for_range, ":cur_village", villages_begin, villages_end),
				(eq, ":has_good", 0),
				#is bound to center
				(this_or_next|party_slot_eq, ":cur_village", slot_village_market_town, ":center_no"),
					(party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),#for castles
               (assign, reg0, 0),
               (try_begin),
                  #If a trading party from the village reached the town recently, its goods are
				  #available.
                  (party_slot_ge, ":cur_village", dplmc_slot_village_trade_last_arrived_to_market, ":recent_time"),
                  (assign, reg0, 1),
               (else_try),
                  #If the village is not looted and this center is not under siege, the
				  #goods from the village could be acquired if they were needed.
					   (neg|party_slot_eq, ":cur_village", slot_village_state, svs_looted),
					   (neg|party_slot_eq, ":cur_village", slot_village_state, svs_deserted),
                  (neg|party_slot_eq, ":center_no", slot_village_state, svs_under_siege),
                  (assign, reg0, 1),
               (try_end),
               (eq, reg0, 1),
				#If an eligible village has positive production, set "has_good" to true.
				(call_script, "script_center_get_production", ":cur_village", ":good_no"),
				(ge, reg0, 1),
				(assign, ":has_good", 1),
			(try_end),
		(try_end),
	(try_end),

	(assign, reg0, ":has_good"),
	(assign, reg1, ":save_reg1"),
	(assign, reg2, ":save_reg2"),
  ]),

  #script_dplmc_assess_ability_to_purchase_good_from_center
  # INPUT: arg1 = good_no
  #        arg2 = center_no
  # OUTPUT:
  #        reg0 = actual price (may be theoretical if unavailable)
  #        reg1 = 1 if available, 0 if unavailable
  ("dplmc_assess_ability_to_purchase_good_from_center",
    [
		(store_script_param, ":good_no", 1),
		(store_script_param, ":center_no", 2),

		#This is still quite experimental.  This is a work in progress
                #rather than a finished formula.
		(assign, ":price_factor", average_price_factor),
		(assign, ":has_good", 0),

		(try_begin),
			(is_between, ":center_no", centers_begin, centers_end),
			(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
				(party_slot_eq, ":center_no", slot_party_type, spt_town),

			(is_between, ":good_no", trade_goods_begin, trade_goods_end),

			(store_sub, ":item_slot_no", ":good_no", trade_goods_begin),
			(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
			(party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),

			(call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":good_no", ":center_no"),
			(assign, ":has_good", reg0),
			#abort if good is found
			(lt, ":has_good", 1),

			(store_faction_of_party, ":center_faction", ":center_no"),
			(faction_get_slot, ":mercantilism", ":center_faction", dplmc_slot_faction_mercantilism),
			(val_clamp, ":mercantilism", -3, 4),

			#For towns, check trade centers.
			(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
				(is_between, ":center_no", towns_begin, towns_end),

			(store_current_hours, ":cur_hours"),
			(assign, ":best_foreign_price", maximum_price_factor),
         (assign, ":worst_price_seen", ":price_factor"),

			(try_for_range, ":trade_town_index", slot_town_trade_routes_begin, slot_town_trade_routes_end),
				(party_get_slot, ":trade_town", ":center_no", ":trade_town_index"),
            (is_between, ":trade_town", centers_begin, centers_end),

				(party_get_slot, ":price_factor_2", ":trade_town", ":item_slot_no"),
				(val_max, ":worst_price_seen", ":price_factor_2"),

            (party_slot_eq, ":trade_town", slot_party_type, spt_town),
				(call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":good_no", ":trade_town"),
				#The town has or produces the item
				(ge, reg0, 1),

				#Get the number of hours since the last caravan arrival, and set the penalty accordingly.
				(assign, ":hours_since", 0),
				#The slot storing the arrival time.  This may be uninitialized for old saved games used
				#with this mod.
				(store_sub, ":arrival_slot", ":trade_town_index", slot_town_trade_routes_begin),
				(val_add, ":arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin),
				(try_begin),
					#This condition can only occur if the number of trade route slots was increased
					#but the number of trade arrival time slots was not.  Check just in case, to avoid
					#strange errors.
					(neg|is_between, ":arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
					#Set "hours-since" to one week.
					(assign, ":hours_since", 7 * 24),
				(else_try),
					#If the slot is uninitialized, give it a random plausible value.
					(party_slot_eq, ":center_no", ":arrival_slot", 0),#Uninitialzed memory!
					(store_random_in_range, ":hours_since", 1, (24 * 7 * 5) + 1),#random time in last five weeks
					(party_get_slot, ":prosperity_factor", ":center_no", slot_town_prosperity),
					(val_clamp, ":prosperity_factor", 0, 101),
					(val_add, ":prosperity_factor", 75),
					(val_mul, ":hours_since", 125),
					(val_div, ":hours_since", ":prosperity_factor"),#last arrival some time in the last five weeks, plus or minus up to 40% based on prosperity
					(store_sub, ":last_arrival", ":cur_hours", ":hours_since"),
					(party_set_slot, ":center_no", ":arrival_slot", ":last_arrival"),
				(else_try),
					(party_get_slot, ":last_arrival", ":center_no", ":arrival_slot"),
					(store_sub, ":hours_since", ":cur_hours", ":last_arrival"),
					(val_max, ":hours_since", 0),
				(try_end),


				#Base penalty is 5%.  It stays at a flat 5% for the first week, then begins rising
				#at a rate of 5% per week afterwards (incremented continuously).
				#Clamp the maximum penalty at 50%.
				(store_mul, ":penalty", ":hours_since", 5),
				(val_add, ":penalty", (24 * 7) // 2),
				(val_div, ":penalty", 24 * 7),
				(val_max, ":penalty", 5),#required for the first week
				(val_min, ":penalty", 50),#don't increase above 50%

				#Apply mercantilism
				(store_faction_of_party, ":other_faction", ":trade_town"),
				(try_begin),
					#Decrease penalty for mercantilism, increase for free trade
					(eq, ":other_faction", ":center_faction"),
					(val_sub, ":penalty", ":mercantilism"),
				(else_try),
					#Increase penalty for mercantilism, decrease for free trade
					(val_add, ":penalty", ":mercantilism"),
				(try_end),

				(try_begin),
					(ge, ":price_factor_2", average_price_factor),
					(val_mul, ":price_factor_2", ":penalty"),
					(val_add, ":price_factor_2", 50),
					(val_div, ":price_factor_2", 100),
				(else_try),
					(store_add, reg0, 100, ":penalty"),
					(val_mul, reg0, average_price_factor),
					(val_add, reg0, 50),
					(val_div, reg0, 100),
					(val_add, ":price_factor_2", reg0),
				(try_end),
				#Make use of the source
				(assign, ":has_good", 1),
				(val_min, ":best_foreign_price", ":price_factor_2"),
			(try_end),
			(try_begin),
			   (ge, ":has_good", 1),
				(val_max, ":price_factor", ":best_foreign_price"),
			(else_try),
  		      #Make it so that lack of supply will not make the price lower
			   (lt, ":has_good", 1),
			   (val_max, ":price_factor", ":worst_price_seen"),
			(try_end),
		(try_end),

		(try_begin),
			(lt, ":has_good", 1),
			(val_max, ":price_factor", average_price_factor),#don't give bargains if there is no supply
			(val_mul, ":price_factor", 8),#sixty percent penalty
			(val_div, ":price_factor", 5),
		(try_end),

		#Apply constraints at the last step
		(val_clamp, ":price_factor", minimum_price_factor, maximum_price_factor),

		(assign, reg0, ":price_factor"),
		(assign, reg1, ":has_good"),
	]),

	# script_dplmc_get_faction_truce_length_with_faction
	# INPUT
	#   arg1:  faction_1
	#   arg2:  faction_2
	# OUTPUT
	#   reg0:  The length in days of faction_1's truce with faction_2, if any.
	#          If no truce exists, the appropriate value to return is zero.
    ("dplmc_get_faction_truce_length_with_faction",
	   [
	    (store_script_param, ":faction_1", 1),
		(store_script_param, ":faction_2", 2),

		(assign, ":truce_length", 0),

		(try_begin),
			(is_between, ":faction_1", kingdoms_begin, kingdoms_end),
			(is_between, ":faction_2", kingdoms_begin, kingdoms_end),
			(neq, ":faction_1", ":faction_2"),
			(store_add, ":truce_slot", ":faction_2", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_get_slot, ":truce_length", ":faction_1", ":truce_slot"),
        (try_end),
	    (assign, reg0, ":truce_length"),
	   ]),

  #script_dplmc_get_terrain_code_for_battle
  #
  # Gets the terrain code for a battle between two parties, which
  # is usually a value like rt_desert, but can instead be two
  # special values: -1 for
  #
  # INPUT: arg1 = attacker_party
  #        arg2 = defender_party
  # OUTPUT: reg0 = terrain code (-1 for invalid, -2 for siege)
  ("dplmc_get_terrain_code_for_battle",
   [
      (store_script_param, ":attacker_party", 1),
      (store_script_param, ":defender_party", 2),

      (assign, reg0, dplmc_terrain_code_unknown), #Terrain code, defined in header_terrain_types.py

	  (try_begin),
		#Check for village missions
         (this_or_next|eq, ":attacker_party", "p_main_party"),
			(eq, ":defender_party", "p_main_party"),
		 (ge, "$g_encounter_is_in_village", 1),
		 (assign, reg0, dplmc_terrain_code_village),#defined in header_terrain_types.py
      (else_try),
		#If the attacker party is a town, a castle, a village, a bandit lair, or a ship,
		#set the terrain code to "none" since we don't have any specific ideas for modifying
		#the unit-type performance in scenarios of that type (whatever they are).
         (ge, ":attacker_party", 0),
         (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_town),#no modifier for being attacked by garrisoned troops
         (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_castle),
         (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_village),
         (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_bandit_lair),
			(party_slot_eq, ":attacker_party", slot_party_type, spt_ship),#no modifier for being attacked by a ship
         (assign, reg0, dplmc_terrain_code_unknown),#no terrain options, defined in header_terrain_types.py
	  (else_try),
		#If the attacker party is *attached* to a town/castle/village, a bandit lair, or a ship,
		#set the terrain code to "none" since we don't have any specific ideas for modifying
		#the unit-type performance in scenarios of that type (whatever they are).
	     (ge, ":attacker_party", 0),
	     (party_get_attached_to, ":attachment", ":attacker_party"),
		 (ge, ":attachment", 0),
		 (party_is_active, ":attachment"),
		 (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_town),#no modifier for being attacked by garrisoned troops
         (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_castle),
         (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_village),
         (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_bandit_lair),
			(party_slot_eq, ":attachment", slot_party_type, spt_ship),#no modifier for being attacked by a ship
         (assign, reg0, dplmc_terrain_code_unknown),#no terrain modifiers
      (else_try),
		#If the attacker party isn't a weird type, the terrain is entirely based on the
		#defender (unless the defender is invalid).
         (ge, ":defender_party", 0),
         (try_begin),
			#If the defender is a walled center, use siege mode.
            (this_or_next|party_slot_eq, ":defender_party", slot_party_type, spt_town),
            (party_slot_eq, ":defender_party", slot_party_type, spt_castle),
            (assign, reg0, dplmc_terrain_code_siege),#siege mode, defined in header_terrain_types.py
		 (else_try),
			#If the defender is a village
			(party_slot_eq, ":defender_party", slot_party_type, spt_village),
			(assign, reg0, dplmc_terrain_code_village),
         (else_try),
			#If the defender is a bandit lair or a ship, use no terrain modifier.
            (this_or_next|party_slot_eq, ":defender_party", slot_party_type, spt_bandit_lair),
				(party_slot_eq, ":defender_party", slot_party_type, spt_ship),
            (assign, reg0, dplmc_terrain_code_unknown),#no terrain modifiers
 		 (else_try),
			#If the defender is attached, do the same checks but for the attachment.
		    (party_get_attached_to, ":attachment", ":defender_party"),
			(ge, ":attachment", 0),
			(party_is_active, ":attachment"),
			(assign, ":attachment_value", -100),
			(try_begin),
				#Walled centers use siege modifiers
			   (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_town),
			      (party_slot_eq, ":attachment", slot_party_type, spt_castle),
			   (assign, ":attachment_value", dplmc_terrain_code_siege),
			(else_try),
				#Villages
			   (party_slot_eq, ":attachment", slot_party_type, spt_village),
			   (assign, ":attachment_value", dplmc_terrain_code_village),
			(else_try),
				#bandit-lairs and ships have no modifiers currently
			   (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_bandit_lair),
				(party_slot_eq, ":attachment", slot_party_type, spt_ship),
			   (assign, ":attachment_value", dplmc_terrain_code_unknown),#no terrain modifiers
			(try_end),
			#If neither of the above apply, fall through to the next condition.
			(neq, ":attachment_value", -100),
			(assign, reg0, ":attachment_value"),
         (else_try),
			#Use the terrain under the defender.
			#In the future I might want to change this so there's a tactics contest
			#between the attacker and defender to choose the more favorable ground
			#from their immediate surroundings.  I would also have to change the actual
			#terrain-type code.
            (party_get_current_terrain, reg0, ":defender_party"),
		 (try_end),
      (else_try),
		 #If we get here, it means the defender was invalid, so use the terrain under
		 #the attacker.
         (ge, ":attacker_party", 0),
         (party_get_current_terrain, reg0, ":attacker_party"),#terrain under attacker
      (try_end),
   ]),

  #script_dplmc_party_calculate_strength_in_terrain
  # INPUT: arg1 = party_id
  #        arg2 = terrain (from header_terrain_types.py)
  #        arg3 = exclude leader (0 for do-not-exclude, 1 for exclude)
  #        arg4 = cache policy (1 is use terrain, 2 is use non-terrain, 0 is do not use)
  # OUTPUT: reg0 = strength with terrain
  #         reg1 = strength ignoring terrain
  ("dplmc_party_calculate_strength_in_terrain",
    [
      (store_script_param, ":party", 1), #Party_id
      (store_script_param, ":terrain_type", 2),#a value from header_terrain_types.py
      (store_script_param, ":exclude_leader", 3),#(0 for do-not-exclude, 1 for exclude)
      (store_script_param, ":cache_policy", 4),#1 is use terrain, 2 is use non-terrain, 0 is do not use)

      (assign, ":total_strength_terrain", 0),
      (assign, ":total_strength_no_terrain", 0),

      (party_get_num_companion_stacks, ":num_stacks", ":party"),
      (assign, ":first_stack", 0),
      (try_begin),
        (neq, ":exclude_leader", 0),
        (assign, ":first_stack", 1),
      (try_end),
	  #Bonus for heroes on top of the rest
	  (assign, ":hero_percent", 110),
	  ##Moved setting the multipliers out of the loop...
	  (assign, ":guaranteed_horse_percent", 100),
	  (assign, ":guaranteed_ranged_percent", 100),
	  (assign, ":guaranteed_neither_percent", 100),
	  #First, test for some special codes:
	  (try_begin),
	     (eq, ":terrain_type", dplmc_terrain_code_none),#Apply no modifiers
		 (assign, ":hero_percent", 100),
	  (else_try),
	  	(eq, ":terrain_type", dplmc_terrain_code_village),#A dismounted fight at a village (apply hero modifier, nothing else)
      (else_try),
        (eq, ":terrain_type", dplmc_terrain_code_siege),#A siege battle, not including sorties.
        (assign, ":guaranteed_ranged_percent", 120),
	  #The rest are ordinary rt_* codes.
	  #I changed the balance of these to make the variations less extreme (e.g. 150% mounted strength on rt_steppe).
	  #I believe that the version from ArcherOS is trying to create certain map results, rather than solely
	  #make autocalc strength more accurate in terms of "what would happen if they fought the player".
	  (else_try),
        (eq, ":terrain_type", rt_steppe),
		#The 150% increase in the steppe strikes me as excessive.
		#Since the NPC cost increase for mounted troops is 20%, and the PC cost is 65%,
		#it isn't entirely implausible.
	    #(assign, ":guaranteed_horse_percent", 150),
		#Archer uses 150%, Custom Commander uses a flat 125%.
		(assign, ":guaranteed_horse_percent", 120),
	  (else_try),
		#I am unaware of any game mechanic in live battles that gives any disadvantage
		#to horses on snow or sand as opposed to a plain.
		(this_or_next|eq, ":terrain_type", rt_snow),
		(this_or_next|eq, ":terrain_type", rt_desert),
			(eq, ":terrain_type", rt_plain),
		(assign, ":guaranteed_horse_percent", 120),
     (else_try),
		#I suspect that the 120% mounted bonus for steppe forests is inaccurate,
		#but I haven't checked it out yet.
	    (eq, ":terrain_type", rt_steppe_forest),
        (assign, ":guaranteed_horse_percent", 120),
     (else_try),
        (this_or_next|eq, ":terrain_type", rt_forest),
        (this_or_next|eq, ":terrain_type", rt_mountain_forest),
		     (eq, ":terrain_type", rt_snow_forest),
        #(assign, ":guaranteed_neither_percent", 120),
		(assign, ":guaranteed_neither_percent", 110),
	 (try_end),

      (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
        (store_character_level, ":stack_strength", ":stack_troop"),
        (val_add, ":stack_strength", 4), #new was 12 (patch 1.125)
        (val_mul, ":stack_strength", ":stack_strength"),
        (val_mul, ":stack_strength", 2), #new (patch 1.125)
        #move the next two lines to after terrain advantage
        #(val_div, ":stack_strength", 100),
        #(val_max, ":stack_strength", 1), #new (patch 1.125)
        (assign, ":terrain_free_strength", ":stack_strength"),
        ##use Arch3r's terrain advantage code (bug-fix changes 2011-04-13; other changes 2011-04-25)
        (try_begin),
           ##AotE terrain advantages
           (assign, ":hero_horse", 0),#added for heroes (any positive number = has a horse)
           (try_begin),
		      (this_or_next|eq, "trp_player", ":stack_troop"),
				(troop_is_hero, ":stack_troop"),
		      (gt, ":guaranteed_horse_percent", ":hero_percent"),#don't bother if we wouldn't use the result
              (neg|troop_is_guarantee_horse, ":stack_troop"),#don't bother if we already know the troop has a horse
			  (store_skill_level, reg0, "skl_riding", ":stack_troop"),
			  (ge, reg0, 2),#don't bother if the troop has no/minimal riding skill
			  #Just checking ek_horse may not work for non-companions, so check the inventory
			  (troop_get_inventory_capacity, ":inv_cap", ":stack_troop"),
			  (ge, ":inv_cap", 1),
			  (val_min, ":inv_cap", dplmc_ek_alt_items_begin + 8),#Don't check too much of the inventory
			  (try_for_range, ":inv_slot", 0, ":inv_cap"),
				(troop_inventory_slot_get_item_amount, reg1, ":stack_troop", ":inv_slot"),
				(ge, reg1, 1),#quantity must be greater than zero
				(troop_get_inventory_slot, reg0, ":stack_troop", ":inv_slot"),
				(ge, reg0, 1),#must be a valid item
				(item_get_type, reg1, reg0),#check if the item is a horse
				(eq, reg1, itp_type_horse),
				(assign, ":inv_cap", ":inv_slot"),#break loop
			  (try_end),
			  #If no horse found, set to zero
              (neg|is_between, ":hero_horse", horses_begin, horses_end),
              (assign, ":hero_horse", 0),
           (try_end),
		   (assign, ":stack_strength_multiplier", 100),#<-- percent multiplier
           (try_begin),#Mounted troops
			  (this_or_next|ge, ":hero_horse", 1),
              (troop_is_guarantee_horse, ":stack_troop"),
              (assign, ":stack_strength_multiplier", ":guaranteed_horse_percent"),
		   (else_try),#Ranged troops
              (troop_is_guarantee_ranged, ":stack_troop"),
              (assign, ":stack_strength_multiplier", ":guaranteed_ranged_percent"),
           (else_try),#Infantry
              (assign, ":stack_strength_multiplier", ":guaranteed_neither_percent"),
           (try_end),

		   #Use hero/player modifiers if a better one didn't apply
		   (try_begin),
		      (this_or_next|eq, ":stack_troop", "trp_player"),
			     (troop_is_hero, ":stack_troop"),
			  (val_max, ":stack_strength_multiplier", ":hero_percent"),#hero bonus
		   (try_end),

		   (val_mul, ":stack_strength", ":stack_strength_multiplier"),
		   (val_add, ":stack_strength", 50),#add this before division for correct rounding
           (val_div, ":stack_strength", 100),
           ##AotE terrain advantages
        (try_end),
        #moved the next two lines here from above
        (val_div, ":stack_strength", 100),#<- moved here from above
        (val_max, ":stack_strength", 1), #new (patch 1.125) #<- moved here from above
        (val_div, ":terrain_free_strength", 100),
        (val_max, ":terrain_free_strength", 1),
        (try_begin),
          (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size",":party",":i_stack"),
          (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
          (val_sub, ":stack_size", ":num_wounded"),
          (val_mul, ":stack_strength", ":stack_size"),
          (val_mul, ":terrain_free_strength", ":stack_size"),
        (else_try),
          (troop_is_wounded, ":stack_troop"), #hero & wounded
          (assign, ":stack_strength", 0),
          (assign, ":terrain_free_strength", 0),
        (try_end),
        (val_add, ":total_strength_terrain", ":stack_strength"),
        (val_add, ":total_strength_no_terrain", ":terrain_free_strength"),
      (try_end),
	  #Load results into registers and cache if appropriate
	  (assign, reg0, ":total_strength_terrain"),
	  (assign, reg1, ":total_strength_no_terrain"),
      (try_begin),
         (eq, ":cache_policy", 1),
         (party_set_slot, ":party", slot_party_cached_strength, reg0),
      (else_try),
         (eq, ":cache_policy", 2),
         (party_set_slot, ":party", slot_party_cached_strength, reg1),
      (try_end),
  ]),


  #script_dplmc_player_can_give_troops_to_troop  (Warning, clobbers {s11}!)
  #
  # INPUT: arg1 = troop_id
  # OUTPUT: reg0 = 1 or more is yes, 0 or less is no
  #
  # This script does not take into account things like whether the troop
  # is a prisoner of a party, so it can be used for checking whether troops
  # can be added to a garrison.
  #
  # The general logic is that you can give troops to a member of your
  # own faction if any of the following are true:
  #   - You are the faction leader or marshall
  #   - You are the spouse of the faction leader, and the faction
  #     leader is not on bad terms with you
  #   - The troop is an affiliated family member
  #   - The troop is your spouse, and is either pliable or not on bad terms
  #   - The troop is a former companion with whom you are on good terms
  #   - The troop is related to you by marriage and you are on good terms
  #
  # For allied factions, the conditions are similar to the above.
  # However, being the marshall or leader of your own faction does not
  # guarantee cooperation from lords who dislike you.
  #
  # For non-allied other factions, the check for faction leader or
  # marshall are not relevant, and the faction must not be at war
  # with the player's faction.
  ("dplmc_player_can_give_troops_to_troop",
  [
	(store_script_param, ":troop_id", 1), #Party_id
	(assign, ":can_give_troops", 0),
	(assign, ":save_reg1", reg1),

	(try_begin),
		(this_or_next|eq, ":troop_id", "trp_kingdom_heroes_including_player_begin"),
		(eq, ":troop_id", "trp_player"),
		(assign, ":can_give_troops", 1),
	(else_try),
		(lt, ":troop_id", 1),
		(assign, ":can_give_troops", 0),
	(else_try),
		(store_faction_of_troop, ":troop_faction", ":troop_id"),

		(call_script, "script_troop_get_player_relation", ":troop_id"),
		(assign, ":troop_relation", reg0),
		(troop_get_slot, ":troop_reputation", ":troop_id", slot_lord_reputation_type),

		(try_begin),
			#Troop is member of player supporters faction
			(eq, ":troop_faction", "fac_player_supporters_faction"),
			##Always yes in Native, but if centralization is negative allow non-compliance
			(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
			(try_begin),
				(ge, reg0, 0),
				(assign, reg0, -200),
			(else_try),
				(val_mul, reg0, -10),
				(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
			(try_end),
			(gt, ":troop_relation", reg0),
			(assign, ":can_give_troops", 1),
		(else_try),
			#Troop is a member of the same faction as the player
			(eq, ":troop_faction", "$players_kingdom"),
			(faction_get_slot, ":troop_faction_leader", ":troop_faction", slot_faction_leader),
			(try_begin),
				#Leader or marshall
				(this_or_next|eq, ":troop_faction_leader", "trp_player"),
					(faction_slot_eq, ":troop_faction", slot_faction_marshall, "trp_player"),
				#If centralization is negative allow non-compliance
				(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
				(try_begin),
					(ge, reg0, 0),
					(assign, reg0, -200),
				(else_try),
					(val_mul, reg0, -10),
					(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
				(try_end),
				(gt, ":troop_relation", reg0),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of leader
				(gt, ":troop_faction_leader", 1),
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_faction_leader", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_faction_leader"),
				(call_script, "script_troop_get_player_relation", ":troop_faction_leader"),
				(ge, reg0, 0),
				#If centralization is negative allow non-compliance
				(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
				(try_begin),
					(ge, reg0, 0),
					(assign, reg0, -200),
				(else_try),
					(val_mul, reg0, -10),
					(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
				(try_end),
				(gt, ":troop_relation", reg0),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of troop
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|ge, ":troop_relation", 0),
				(this_or_next|eq, ":troop_reputation", lrep_conventional),
				(this_or_next|eq, ":troop_reputation", lrep_moralist),
					(eq, ":troop_reputation", lrep_otherworldly),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Affiliated family member
				(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
				(ge, reg0, 1),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Close companion previously under arms
				(this_or_next|is_between, ":troop_id", companions_begin, companions_end),
					(is_between, ":troop_id", pretenders_begin, pretenders_end),
				(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(else_try),
				#In-law (or hypothetically a blood relative) who is close with the player
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
				(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
				(ge, ":troop_relation", 14),
				(this_or_next|ge, reg0, 10),
					(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(try_end),
		(else_try),
			#Troop is member of a faction allied with the player's
			(call_script, "script_dplmc_get_faction_truce_length_with_faction", "$players_kingdom", ":troop_faction"),
			(gt, reg0, dplmc_treaty_defense_days_expire),
			(faction_get_slot, ":player_faction_leader", "$players_kingdom", slot_faction_leader),
			(try_begin),
				#Leader or marshall
				(this_or_next|eq, ":player_faction_leader", "trp_player"),
					(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
				(ge, ":troop_relation", 0),#only for allied factions, not for the player's own faction
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of leader
				(gt, ":player_faction_leader", 1),
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":player_faction_leader", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":player_faction_leader"),
				(ge, ":troop_relation", 0),#only for allied factions, not for the player's own faction
				(call_script, "script_troop_get_player_relation", ":player_faction_leader"),
				(ge, reg0, 0),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of troop
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|ge, ":troop_relation", 0),
				(this_or_next|eq, ":troop_reputation", lrep_conventional),
				(this_or_next|eq, ":troop_reputation", lrep_moralist),
					(eq, ":troop_reputation", lrep_otherworldly),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Affiliated family member
				(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
				(ge, reg0, 1),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Close companion previously under arms
				(this_or_next|is_between, ":troop_id", companions_begin, companions_end),
					(is_between, ":troop_id", pretenders_begin, pretenders_end),
				(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(else_try),
				#In-law (or hypothetically a blood relative) who is close with the player
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
				(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
				(ge, ":troop_relation", 14),
				(this_or_next|ge, reg0, 10),
					(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(try_end),
		(else_try),
			#Troop is a member of a faction that isn't hostile to the player's
			(store_relation, reg0, ":troop_faction", "fac_player_faction"),
			(ge, reg0, 0),
			(store_relation, reg0, ":troop_faction", "$players_kingdom"),
			(ge, reg0, 0),
			(try_begin),
				#Spouse of troop
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|ge, ":troop_relation", 0),
				(this_or_next|eq, ":troop_reputation", lrep_conventional),
				(this_or_next|eq, ":troop_reputation", lrep_moralist),
					(eq, ":troop_reputation", lrep_otherworldly),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Affiliated family member
				(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
				(ge, reg0, 1),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Close companion previously under arms
				(this_or_next|is_between, ":troop_id", companions_begin, companions_end),
					(is_between, ":troop_id", pretenders_begin, pretenders_end),
				(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(else_try),
				#In-law (or hypothetically a blood relative) who is close with the player
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
				(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
				(ge, ":troop_relation", 14),
				(this_or_next|ge, reg0, 10),
					(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(try_end),
		(try_end),
	(try_end),

	(assign, reg1, ":save_reg1"),
	(assign, reg0, ":can_give_troops"),
  ]),

  #script_dplmc_print_centers_in_numbers_to_s0
  #
  #similar to script_print_troop_owned_centers_in_numbers_to_s0
  #
  #INPUT:
  #  arg1: owned_towns
  #  arg2: owned_castles
  #  arg3: owned_villages
  #
  #OUTPUT:
  #  reg0: owned_towns + owned_castles + owned_villages
  #    s0: a string describing the numbers of centers
    ("dplmc_print_centers_in_numbers_to_s0",
   [
     (store_script_param_1, ":owned_towns"),
	 (store_script_param_2, ":owned_castles"),
	 (store_script_param, ":owned_villages", 3),
     (str_store_string, s0, "@nothing"),

     (assign, ":num_types", 0),
     (try_begin),
       (gt, ":owned_villages", 0),
       (assign, reg0, ":owned_villages"),
       (store_sub, reg1, reg0, 1),
       (str_store_string, s0, "@{reg0} village{reg1?s:}"),
       (val_add, ":num_types", 1),
     (try_end),

     (try_begin),
       (gt, ":owned_castles", 0),
       (assign, reg0, ":owned_castles"),
       (store_sub, reg1, reg0, 1),
       (try_begin),
         (eq, ":num_types", 0),
         (str_store_string, s0, "@{reg0} castle{reg1?s:}"),
       (else_try),
         (str_store_string, s0, "@{reg0} castle{reg1?s:} and {s0}"),
       (try_end),
       (val_add, ":num_types", 1),
     (try_end),

     (try_begin),
       (gt, ":owned_towns", 0),
       (assign, reg0, ":owned_towns"),
       (store_sub, reg1, reg0, 1),
       (try_begin),
         (eq, ":num_types", 0),
         (str_store_string, s0, "@{reg0} town{reg1?s:}"),
       (else_try),
         (eq, ":num_types", 1),
         (str_store_string, s0, "@{reg0} town{reg1?s:} and {s0}"),
       (else_try),
         (str_store_string, s0, "@{reg0} town{reg1?s:}, {s0}"),
       (try_end),
     (try_end),

     (store_add, reg0, ":owned_villages", ":owned_castles"),
     (val_add, reg0, ":owned_towns"),
     ]),

  #"script_dplmc_distribute_gold_to_lord_and_holdings"
  #
  #Related to script_dplmc_remove_gold_from_lord_and_holdings, divides the gold
  #between the lord and his fortresses in a semi-intelligent way.
  #
  #INPUT:
  #   arg1: the amount of gold
  #   arg2: the lord's ID
  ("dplmc_distribute_gold_to_lord_and_holdings",
   [
	(store_script_param_1, ":gold_left"),
	(store_script_param_2, ":lord_no"),

	(try_begin),
		(lt, ":lord_no", 0),#Invalid ID
	(else_try),
		#If the number is negative, handle this using script_dplmc_remove_gold_from_lord_and_holdings
		(lt, ":gold_left", 0),
		(val_mul, ":gold_left", -1),
		(call_script, "script_dplmc_remove_gold_from_lord_and_holdings", ":gold_left", ":lord_no"),
		(assign, ":gold_left", 0),
	(else_try),
		(neq, ":lord_no", "trp_player"),
		(neg|troop_is_hero, ":lord_no"),#Not hero or player
        (troop_add_gold, ":lord_no", ":gold_left"),
        (assign, ":gold_left", 0),
	(else_try),
		#The player doesn't use center wealth to pay garrison wages, so just
		#give it directly.
		(eq, ":lord_no", "trp_player"),
		(troop_add_gold, "trp_player", ":gold_left"),
		(assign, ":gold_left", 0),
	(else_try),
		(neg|troop_is_hero, ":lord_no"),#If the lord isn't the player, and isn't a hero, do nothing
	(else_try),
		(troop_get_slot, ":target_gold", ":lord_no", slot_troop_wealth),
		(val_max, ":target_gold", 0),
		#If the lord is low on gold, first he takes enough gold so he isn't low on funds,
		#or all of the gold, whichever is less.
		(store_sub, ":gold_to_give", 6000, ":target_gold"),#6000 is the standard starting gold for lords (kings start with more, but don't increase this for them, since I'm using this number as a "low on gold" threshold)
		(val_max, ":gold_to_give", 0),
		(val_min, ":gold_to_give", ":gold_left"),

		(val_add, ":target_gold", ":gold_to_give"),
		(troop_set_slot, ":lord_no", slot_troop_wealth, ":target_gold"),
		(val_sub, ":gold_left", ":gold_to_give"),
		#If gold remains, the lord gives some to any castles or towns he owns that have
		#low wealth.  Note that iterating in this order means that towns get checked
		#before castles do.
		(gt, ":gold_left", 0),
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
			(party_get_slot, ":target_gold", ":center_no", slot_town_wealth),
			#Don't give gold to centers with garrisons more than 50% above the ideal size
			(store_party_size_wo_prisoners, ":garrison_size", ":center_no"),
			(call_script, "script_party_get_ideal_size", ":center_no"),#This script has been modified to support this use
			(val_mul, reg0, 3),
			(val_div, reg0, 2),
			(ge, reg0, ":garrison_size"),

			(try_begin),
				(party_slot_eq, ":center_no", slot_party_type, spt_town),
				(store_sub, ":gold_to_give", 4000, ":target_gold"),#4000 is the standard starting gold for towns
			(else_try),
				(store_sub, ":gold_to_give", 2000, ":target_gold"),#2000 is the standard starting gold for castles
			(try_end),

			(val_max, ":gold_to_give", 0),
			(val_min, ":gold_to_give", ":gold_left"),
			(gt, ":gold_to_give", 0),
			(val_add, ":target_gold", ":gold_to_give"),
			(party_set_slot, ":center_no", slot_town_wealth, ":target_gold"),
			(val_sub, ":gold_left", ":gold_to_give"),
		(try_end),
		#If gold is left -- the lord isn't low on gold, and none of his walled centers are --
		#he pockets the remainder.
		(gt, ":gold_left", 0),
		(troop_get_slot, ":target_gold", ":lord_no", slot_troop_wealth),
		(val_add, ":target_gold", ":gold_left"),
		(val_max, ":target_gold", 0),
		(troop_set_slot, ":lord_no", slot_troop_wealth, ":target_gold"),
		(assign, ":gold_left", 0),
	(try_end),
	]),


  #"script_dplmc_remove_gold_from_lord_and_holdings"
  #
  #
  #INPUT:
  #   arg1: the amount of money to remove (greater than zero)
  #   arg2: the ID of the lord spending the money
  #
  #OUTPUT:
  #   None
    ("dplmc_remove_gold_from_lord_and_holdings",
   [
    (store_script_param_1, ":gold_cost"),
	(store_script_param_2, ":lord_no"),

	(try_begin),
		(lt, ":lord_no", 0),#Invalid ID
	(else_try),
		(neq, ":lord_no", "trp_player"),
		(neg|troop_is_hero, ":lord_no"),#Not player or hero
	(else_try),
		#If the number is negative, give gold instead of taking it.
		#Handle this using script_dplmc_distribute_gold_to_lord_and_holdings
		(lt, ":gold_cost", 0),
		(val_mul, ":gold_cost", -1),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_cost", ":lord_no"),
		(assign, ":gold_cost", 0),
	(else_try),
		#For the player, first subtract the gold from his treasury (if any).
		(eq, ":lord_no", "trp_player"),
	    (store_troop_gold, ":treasury", "trp_household_possessions"),
		(try_begin),
		(ge, ":treasury", 1),
		(val_min, ":treasury", ":gold_cost"),
		(call_script, "script_dplmc_withdraw_from_treasury", ":treasury"),
		(val_sub, ":gold_cost", ":treasury"),
		(try_end),
		(store_troop_gold, ":treasury", "trp_player"),
		(try_begin),
			(ge, ":treasury", 1),
			(val_min, ":treasury", ":gold_cost"),
			(troop_remove_gold, "trp_player", ":treasury"),
			(val_sub, ":gold_cost", ":treasury"),
		(try_end),
		#Fall through to the next section if the treasury didn't cover it.
		(lt, ":gold_cost", 1),
	(else_try),
		#Remove the gold directly from the lord's wealth slot
		(ge, ":gold_cost", 1),
		(ge, ":lord_no", 1),#not the player
		(troop_get_slot, ":treasure", ":lord_no", slot_troop_wealth),
		(ge, ":treasure", 1),
		(try_begin),
			(ge, ":treasure", ":gold_cost"),
			(val_sub, ":treasure", ":gold_cost"),
			(assign, ":gold_cost", 0),
		(else_try),
			(val_sub, ":gold_cost", ":treasure"),
			(assign, ":treasure", 0),
		(try_end),
		(troop_set_slot, ":lord_no", slot_troop_wealth, ":treasure"),
		#Fall through to the next section if his personal wealth didn't cover it.
		(lt, ":gold_cost", 1),
	(else_try),
		#Remove remaining gold from uncollected taxes.
		#We iterate backwards in order to remove from villages before castles and towns.
		(ge, ":gold_cost", 1),
		(try_for_range_backwards, ":center_no", centers_begin, centers_end),
			(ge, ":gold_cost", 1),
			(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
			(party_get_slot, ":treasure", ":center_no", slot_center_accumulated_rents),
			(try_begin),
               	(gt, ":treasure", 0),
				(ge, ":treasure", ":gold_cost"),
				(val_sub, ":treasure", ":gold_cost"),
				(assign, ":gold_cost", 0),
			(else_try),
               	(gt, ":treasure", 0),
				(val_sub, ":gold_cost", ":treasure"),
				(assign, ":treasure", 0),
			(try_end),
				(party_set_slot, ":center_no", slot_center_accumulated_rents, ":treasure"),

			(ge, ":gold_cost", 1),
			(party_get_slot, ":treasure", ":center_no", slot_center_accumulated_tariffs),
			(try_begin),
               	(gt, ":treasure", 0),
				(ge, ":treasure", ":gold_cost"),
				(val_sub, ":treasure", ":gold_cost"),
				(assign, ":gold_cost", 0),
			(else_try),
               	(gt, ":treasure", 0),
				(val_sub, ":gold_cost", ":treasure"),
				(assign, ":treasure", 0),
			(try_end),
			(party_set_slot, ":center_no", slot_center_accumulated_tariffs, ":treasure"),
		(try_end),
		#Fall through to the next section if the uncollected taxes didn't cover it.
		(lt, ":gold_cost", 1),
	(else_try),
		#Remove remaining gold from center wealth.  We iterate backwards to remove from
		#castles before towns.
		(ge, ":gold_cost", 1),
		(try_for_range_backwards, ":center_no", centers_begin, centers_end),
			(ge, ":gold_cost", 1),
			(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
			(party_get_slot, ":treasure", ":center_no", slot_town_wealth),
		(ge, ":treasure", 1),
		(try_begin),
			(ge, ":treasure", ":gold_cost"),
			(val_sub, ":treasure", ":gold_cost"),
			(assign, ":gold_cost", 0),
		(else_try),
			(val_sub, ":gold_cost", ":treasure"),
			(assign, ":treasure", 0),
		(try_end),
			(party_set_slot, ":center_no", slot_town_wealth, ":treasure"),
		(try_end),
		(lt, ":gold_cost", 1),
	(else_try),
	    #Try to remove the gold from the hero himself
		(store_troop_gold, ":treasure", ":lord_no"),
		(gt, ":treasure", 0),
		(try_begin),
			(ge, ":treasure", ":gold_cost"),
			(troop_remove_gold, ":lord_no", ":gold_cost"),
			(assign, ":gold_cost", 0),
		(else_try),
			(troop_remove_gold, ":treasure"),
			(val_sub, ":gold_cost", ":treasure"),
		(try_end),
	(try_end),

   ]),

  # "script_dplmc_prepare_hero_center_points_ignoring_center"
  #
  # Input: arg1 = target_center
   ("dplmc_prepare_hero_center_points_ignoring_center",[
	  (store_script_param, ":target_center", 1),

	  (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
	  (troop_set_slot, "trp_player", dplmc_slot_troop_temp_slot, 0),

	  (try_for_range, ":troop_no", heroes_begin, heroes_end),
		(troop_set_slot, ":troop_no", slot_troop_temp_slot, 0),
		(troop_set_slot, ":troop_no", dplmc_slot_troop_temp_slot, 0),
	  (try_end),

	  (try_for_range, ":center_no", centers_begin, centers_end),
	    #Skip "target center"
		(neq, ":center_no", ":target_center"),

		#Lord is player or a hero
		(party_get_slot, ":troop_no", ":center_no", slot_town_lord),
		(this_or_next|eq, ":troop_no", "trp_player"),
			(is_between, ":troop_no", heroes_begin, heroes_end),

		#Update lord point total
		(assign, ":center_points", 1),
		(try_begin),
			(party_slot_eq, ":center_no", slot_party_type, spt_town),
			(assign, ":center_points", 3),
		(else_try),
			(party_slot_eq, ":center_no", slot_party_type, spt_castle),
			(assign, ":center_points", 2),
		(try_end),

		(troop_get_slot, ":slot_value", ":troop_no", slot_troop_temp_slot),
		(val_add, ":slot_value", ":center_points"),
		(troop_set_slot, ":troop_no", slot_troop_temp_slot, ":slot_value"),

		#Update distance from closest owned center to target
		(is_between, ":target_center", centers_begin, centers_end),
		(troop_get_slot, ":slot_value", ":troop_no", dplmc_slot_troop_temp_slot),
		(store_distance_to_party_from_party, ":cur_distance", ":target_center", ":center_no"),
		(val_max, ":cur_distance", 1),
		(try_begin),
			(eq, ":slot_value", 0),
			(assign, ":slot_value", ":cur_distance"),
		(try_end),
		(val_min, ":slot_value", ":cur_distance"),
		(troop_set_slot, ":troop_no", dplmc_slot_troop_temp_slot, ":slot_value"),
	  (try_end),
	  ##Update cached totals
	  (try_for_range, ":troop_no", heroes_begin, heroes_end),
		(troop_get_slot, reg0, ":troop_no", slot_troop_temp_slot),
		(val_add, reg0, 1),
		(troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
          (try_end),
          (troop_get_slot, reg0, "trp_player", slot_troop_temp_slot),
          (val_add, reg0, 1),
          (troop_set_slot, "trp_player", dplmc_slot_troop_center_points_plus_one, reg0),
          #Since the target center was omitted from the point totals, handle it here
	  (try_begin),
		(is_between, ":target_center", centers_begin, centers_end),
		(party_get_slot, ":troop_no", ":target_center", slot_town_lord),
		#Only perform this update for a troop whose center point value was updated above
		(this_or_next|is_between, ":troop_no", heroes_begin, heroes_end),
		(eq, ":troop_no", "trp_player"),
		(troop_get_slot, reg0, ":troop_no", dplmc_slot_troop_center_points_plus_one),
		(val_add, reg0, 1),#1 point for villages
		(try_begin),
		   (is_between, ":target_center", walled_centers_begin, walled_centers_end),
		   (val_add, reg0, 1),#2 points for castles
		   (is_between, ":target_center", towns_begin, towns_end),
		   (val_add, reg0, 1),#3 points for towns
		(try_end),
		(troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
	  (try_end),
   ]),


  # script_dplmc_calculate_troop_score_for_center_aux
  #  Similar to script_calculate_troop_score_for_center
  #
  # slot_troop_temp_slot must already be loaded with center points;
  # dplmc_slot_troop_temp_slot must already be loaded with distance.
  #
  # Input: arg1 = evaluator
  #        arg2 = troop_no
  #        arg3 = center_no
  # Output: reg0 = score
  #         reg1 = explanation string
  ("dplmc_calculate_troop_score_for_center_aux",
   [(store_script_param, ":troop_1", 1),
    (store_script_param, ":troop_2", 2),
	 (store_script_param, ":center_no", 3),

	 (assign, ":explanation", "str_political_explanation_most_deserving_in_faction"),
	 (assign, ":explanation_priority", -1),

   (try_begin),
      (lt, ":troop_1", 0),
      (assign, ":relation", 0),
      (assign, ":reputation", lrep_none),
   (else_try),
      (eq, ":troop_1", ":troop_2"),
      (assign, ":relation", 50),
	   (troop_get_slot, ":reputation", ":troop_1", slot_lord_reputation_type),
   (else_try),
      (call_script, "script_troop_get_relation_with_troop", ":troop_1", ":troop_2"),
      (assign, ":relation", reg0),
      (troop_get_slot, ":reputation", ":troop_1", slot_lord_reputation_type),
   (try_end),
   (val_clamp, ":relation", -100, 101),

   (troop_get_slot, reg0, ":troop_2", slot_troop_renown),
   (val_max, reg0, 0),
   (store_add, ":score", 500, reg0),
	(troop_get_slot, ":num_center_points", ":troop_2", slot_troop_temp_slot),
	(val_max, ":num_center_points", 0),
	(val_add, ":num_center_points", 1),

	#Subtract distance from closest other fief owned, except when
	#considering the lord's original holdings.
	(try_begin),
	  (troop_slot_ge, ":troop_2", slot_troop_temp_slot, 1),
	  (neg|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
	  (neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2"),

	  (troop_get_slot, reg0, ":troop_2", dplmc_slot_troop_temp_slot),
	  (gt, reg0, 1),
	  (val_min, reg0, 250),#upper cap on distance effect (bear in mind that this is subtracted from 500 + troop renown)
	  (val_sub, ":score", reg0),
	(try_end),

   #(store_random_in_range, ":random", 50, 100),
   #(val_mul, ":score", ":random"),
	(val_mul, ":score", 75),
   (val_div, ":score", ":num_center_points"),

	(assign, ":fiefless_bonus_used", 0),
	(try_begin),
	   #Bonus for lords with no other fiefs when a village is being considered.
      (lt, ":num_center_points", 2),
	  (party_slot_eq, ":center_no", slot_party_type, spt_village),
      (neq, ":reputation", lrep_debauched),
      (neq, ":reputation", lrep_selfrighteous),
      (neq, ":reputation", lrep_quarrelsome),
		(val_mul, ":score", 2),
		(try_begin),
		  (lt, ":explanation_priority", 100),
		  (assign, ":explanation_priority", 100),
		  (assign, ":explanation", "str_political_explanation_lord_lacks_center"),
		(try_end),
	 (assign, ":fiefless_bonus_used", 1),#because it has already been applied
	(try_end),

	(assign, ":troop_2_slot_alias", ":troop_2"),
	(try_begin),
		(eq, ":troop_2", "trp_player"),
		(assign, ":troop_2_slot_alias", "trp_kingdom_heroes_including_player_begin"),
	(try_end),

   (try_begin),
	#Bonus for conquerer
		(neq, ":reputation",  lrep_debauched),
		(this_or_next|neq, ":reputation", lrep_selfrighteous),
		   (eq, ":troop_1", ":troop_2"),
		(neq, ":reputation", lrep_cunning),
	  (neg|party_slot_eq, ":center_no", slot_party_type, spt_village),
      (party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":troop_2_slot_alias"),
	  (try_begin),
		 (lt, ":num_center_points", 2),
		 (eq, ":fiefless_bonus_used", 0),
		 (assign, reg1, 50),#50% increase
	  (else_try),
	     (this_or_next|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
		 (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2_slot_alias"),
		 (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
			(eq, ":reputation", lrep_martial),
		 (assign, reg1, 50),#50% increase
	  (else_try),
		 (assign, reg1, 25),#25% increase
	  (try_end),
	  (store_add, reg0, 100, reg1),
	  (val_mul, ":score", reg0),
	  (val_div, ":score", 100),
		(try_begin),
		  (ge, reg1, ":explanation_priority"),
		  (assign, ":explanation_priority", reg1),
		  (assign, ":explanation", "str_political_explanation_lord_took_center"),
 		(try_end),
	(else_try),
	#Bonus for original owner
		(gt, ":troop_2", 0),
		(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2_slot_alias"),
		(try_begin),
			(lt, ":num_center_points", 2),
			(eq, ":fiefless_bonus_used", 0),
			(assign, reg1, 50),#50% increase
		(else_try),
			(this_or_next|eq, ":troop_2", ":troop_1"),
			(this_or_next|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
				(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
			(assign, reg1, 50),#50% increase
		(else_try),
			(assign, reg1, 25),#25% increase
		(try_end),
		(store_add, reg0, 100, reg1),
		(val_mul, ":score", reg0),
		(val_div, ":score", 100),
		(try_begin),
		  (ge, reg1, ":explanation_priority"),
		  (assign, ":explanation_priority", reg1),
        (assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
 		(try_end),
	(else_try),
	#Bonus for previous owner, lord
		(gt, ":troop_2", 0),
		(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
		(try_begin),
			(lt, ":num_center_points", 2),
			(eq, ":fiefless_bonus_used", 0),
			(assign, reg1, 50),#50% increase
		(else_try),
		(troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
			(assign, reg1, 50),
		(else_try),
			(assign, reg1, 25),#25% increase
		(try_end),
		(store_add, reg0, 100, reg1),
		(val_mul, ":score", reg0),
		(val_div, ":score", 100),
		(try_begin),
		  (ge, reg1, ":explanation_priority"),
		  (assign, ":explanation_priority", reg1),
        (assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
 		(try_end),
	(else_try),
	#Bonus for lord claiming the center as home
		(troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
		(val_mul, ":score", 5),
		(val_div, ":score", 4),
		(try_begin),
		  (ge, 25, ":explanation_priority"),
		  (assign, ":explanation_priority", 25),
        (assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
 		(try_end),
	(else_try),
	#Aesthetic penalty (doesn't apply when there was a bonus)
	#To try to make the late game less mixed, have a preference towards
	#assigning lords to their own faction types.
		(troop_get_slot, reg0, ":troop_2", slot_troop_original_faction),
		(party_get_slot, reg1, ":center_no", slot_center_original_faction),
		(neq, reg0, reg1),
	#These extra checks are to avoid penalizing the player or promoted companions
	#unintentionally.
		(is_between, reg0, npc_kingdoms_begin, npc_kingdoms_end),
		(is_between, reg1, npc_kingdoms_begin, npc_kingdoms_end),
		#Take 95% of score
		(val_mul, ":score", 19),
		(val_add, ":score", 10),
		(val_div, ":score", 20),
   (try_end),

	#add 2 x relation (minus controversy) to score
   (troop_get_slot, ":controversy", ":troop_2", slot_troop_controversy),
   (val_clamp, ":controversy", 0, 101),
	(store_mul, ":relation_mod", ":relation", 2),
	(val_sub, ":relation_mod", ":controversy"),
	#this modifier will not raise the score by more than 50%
	(store_add, reg0, ":score", 1),
	(val_div, reg0, 2),
	(val_max, reg0, 1),
	(val_min, ":relation_mod", reg0),

	(store_mul, reg0, ":score", 100),#rego has pre-relationship modified score
	(val_add, ":score", ":relation_mod"),
	(val_div, reg0, ":score"),
	(store_sub, reg1, ":score", 100),#reg1 has percentage change (i.e. 1.5 times becomes 50% change) from relation/controversy

	(try_begin),
		(ge, reg1, 0),
		(ge, reg1, ":explanation_priority"),
		  (ge, ":relation", 15),
		(assign, ":explanation_priority", reg1),
		  (assign, ":explanation", "str_political_explanation_most_deserving_friend"),
	(try_end),

   (assign, reg0, ":score"),
	(assign, reg1, ":explanation"),
   ]),


  #Adapted "auto-sell" from rubik's Custom Commander
  #auto sell credit rubik (CC) begin:
  #
  # script_dplmc_auto_sell
  # INPUTS:
  #    arg1 :customer (the one selling the stuff)
  #    arg2 :merchant (the one buying the stuff)
  #    arg3 :auto_sell_price_limit (only sell stuff less expensive than this)
  #    arg4 :valid_items_begin (use this to only sell a limited range of things)
  #    arg5 :valid_items_end   (use this to only sell a limited range of things)
  #    arg6 :actually_sell_items (set to 0 for a "dry run"; set to 2 to print a descriptive message)
  #
  # OUTPUTS:
  #    reg0 amount of gold gained by customer (not actually gained if this was a dry run)
  #    reg1 number of items sold by customer (not actually sold if this was a dry run)
  ("dplmc_auto_sell", [
	#This script has various changes from the CC version.
	#In particular, all parameters other than "customer" and "merchant",
	#and reporting the number of items & gold change.
	(store_script_param, ":customer", 1),
	(store_script_param, ":merchant", 2),
	#dplmc+ start added parameters
	(store_script_param, ":auto_sell_price_limit", 3),
	(store_script_param, ":valid_items_begin", 4),
	(store_script_param, ":valid_items_end", 5),
	(store_script_param, ":actually_sell_items", 6),
	#dplmc+ end added parameters

	#dplmc+ added section begin
	(assign, ":save_reg2", reg2),
	(assign, ":save_reg3", reg3),
	(assign, ":save_reg65", reg65),
	(assign, ":save_talk_troop", "$g_talk_troop"),
	#The talk troop is used for price information, but it's possible for this to be called
	#from other contexts (like a menu).
	(assign, "$g_talk_troop", ":merchant"),

	(assign, ":gold_gained", 0),
	(assign, ":items_sold", 0),
	#(assign, ":most_expensive_sold_item", -1),
	#(assign, ":most_expensive_sold_imod", -1),
	#(assign, ":most_expensive_sold_price", -1),
	#dplmc+ added section end

    (store_free_inventory_capacity, ":space", ":merchant"),
    (troop_get_inventory_capacity, ":inv_cap", ":customer"),
	(set_show_messages, 0),#<-dplmc+ added
	(store_troop_gold, ":m_gold", ":merchant"),#dplmc+: to support "dry runs", move this out of the loop
    (try_for_range_backwards, ":i_slot", dplmc_ek_alt_items_end, ":inv_cap"),#we're reserving several "safe" slots in the beginning of the inventory
      (troop_get_inventory_slot, ":item", ":customer", ":i_slot"),
      (troop_get_inventory_slot_modifier, ":imod", ":customer", ":i_slot"),
      (gt, ":item", -1),
      (item_get_type, ":type", ":item"),
      (item_slot_eq, ":type", dplmc_slot_item_type_not_for_sell, 0),
	  #dplmc+ begin added constraints
	  (is_between, ":item", ":valid_items_begin", ":valid_items_end"),
	  (neg|is_between, ":type", books_begin, books_end),
	  (this_or_next|neg|is_between, ":type", food_begin, food_end),
	     (eq, ":imod", imod_rotten),
	  (neg|is_between, ":type", trade_goods_begin, trade_goods_end),
	  (neq, ":imod", imod_lordly),#dplmc+: never sell "lordly" items
	  #dplmc+ end added constraints

      (call_script, "script_dplmc_get_item_value_with_imod", ":item", ":imod"),
      (assign, ":score", reg0),
      (val_div, ":score", 100),
      (call_script, "script_game_get_item_sell_price_factor", ":item"),
      (assign, ":sell_price_factor", reg0),
      (val_mul, ":score", ":sell_price_factor"),
      (val_div, ":score", 100),
      (val_max, ":score",1),

	  #dplmc+ start changed section
	  (le, ":score", ":auto_sell_price_limit"),
	  (le, ":score", ":m_gold"),
	  (gt, ":space", 0),

	  #For equipment, in general don't sell the item unless you have a better one,
	  #or the item is useless to you.  (The idea is to stop from accidentally
	  #selling the player's own equipment.)
	  (item_get_type, ":this_item_type", ":item"),

	  #Normally, we would do the following:

	  #(try_begin),
	  #   (item_slot_eq, ":item", dplmc_slot_two_handed_one_handed, 1),
	  #	 (assign, ":this_item_type", 11), # type 11 = two-handed/one-handed
	  #(try_end),

	  #However, we are delaying that step until later, because type 11 is the
	  #same as itp_type_goods.


	  #Don't sell items if there's a reasonable chance that they might
	  #be the player's alternate personal equipment.  It goes without saying
	  #that items the player can't use aren't counted.
	  #
	  #(Items the player has equipped will not even be considered for sale,
	  #but it is common for players to have a variety of items they use in
	  #different circumstances, which might not all be equipped.)
	  #
	  #For melee weapons: don't sell the best weapon or the second-best of a type
	  #   (it might be a backup, or there might be a variety of weapons of
	  #   the same type in situational use)
	  #For shields: don't sell the best or second-best shield
	  #For thrown weapons: don't sell the best three thrown weapons
	  #For ammunition: don't sell the best three of the ammunition kind (arrows,
	  #   bolts) unless you lack a weapon that uses the ammunition.
	  #For armor: don't sell the best armor of a kind.
	  #For horses: don't sell the best or second-best horse
	  #For bows and crossbows: don't sell the best item of a kind (all bows are
	  #   very similar, so there's little chance someone would carry an alternate)
	  #For muskets and pistols: don't sell the best or second-best weapon of
	  #   a kind.

	  (assign, ":can_sell", 1),

	  (try_begin),
		 #Ammunition type: arrows (if you have a bow you can use, don't sell the best 3 arrow packs you have)
	     (eq, ":this_item_type", itp_type_arrows),
		 (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_bow, ":customer"),
		 (try_begin),
			(ge, reg0, 0),
			(call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
			(lt, reg0, 3),#must not be best (0), second-best (1), or third-best (2)
			(assign, ":can_sell", 0),
		 (try_end),
	  (else_try),
		#Ammunition type: bolts (if you have a crossbow you can use, don't sell the best 3 bolt packs you have)
	     (eq, ":this_item_type", itp_type_bolts),
		 (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_crossbow, ":customer"),
		 (try_begin),
			(ge, reg0, 0),
			(call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
			(lt, reg0, 3),#must not be best (0), second-best (1), or third-best (2)
			(assign, ":can_sell", 0),
		 (try_end),
	  (else_try),
		#Ammunition type: bullets (if you have a pistol or musket you can use, don't sell the best 3 bullet packs you have)
	     (eq, ":this_item_type", itp_type_bullets),
		 #Do muskets and pistols both use bullets?  I'll assume so.
		 (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_musket, ":customer"),
		 (assign, reg1, reg0),
		 (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_pistol, ":customer"),
		 (try_begin),
			(this_or_next|ge, reg0, 0),
				(ge, reg1, 0),
			(call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
			(lt, reg0, 3),
			(assign, ":can_sell", 0),
		 (try_end),
	  (else_try),
		#Catch: all non-usable equipment
		(is_between, ":this_item_type", itp_type_horse, itp_type_musket + 1),
		(neq, ":this_item_type", itp_type_goods),
		(call_script, "script_dplmc_troop_can_use_item", ":customer", ":item", ":imod"),
		(eq, reg0, 0),#Past here, we don't have to check for usability
	  (else_try),
		#Thrown weapons: don't sell best 3 you can use
		(eq, ":this_item_type", itp_type_thrown),
		(call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
		(store_sub, ":can_sell", reg0, 2),#must not be best (0) or second-best (1) or third-best (2)
	  (else_try),
		#Types where both the best and the second-best aren't sold
		#Horses, shields, melee weapons, and firearms
		(this_or_next|is_between, ":this_item_type", itp_type_horse, itp_type_polearm + 1),
		(this_or_next|eq, ":this_item_type", itp_type_shield),
		(this_or_next|eq, ":this_item_type", itp_type_pistol),
			(eq, ":this_item_type", itp_type_musket),
		(call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
		(store_sub, ":can_sell", reg0, 1),#must not be best (0) or second best (1)
 	  (else_try),
		#Types where the best isn't sold (armor, not including shields)
		(is_between, ":this_item_type", itp_type_head_armor, itp_type_hand_armor + 1),
		(call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
		(assign, ":can_sell", reg0),#must not be best (0)
	  (try_end),

	  #(try_begin),
	  #   (lt, ":can_sell", 1),
	  #	 (gt, "$cheat_mode", 0),
	  #	 (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
 	  #	 (assign, reg1, ":i_slot"),
	  #	 (str_store_item_name, s0, ":item"),
	  #	 (display_message, "@{!} DEBUG - Will not sell item {s0} at slot {reg1}.  Better items of same kind: {reg0}"),
	  #(try_end),

	  (ge, ":can_sell", 1),

	  #(try_begin),
	  #	(ge, ":score", ":most_expensive_sold_price"),
	  #	(assign, ":most_expensive_sold_item", ":item"),
	  #	(assign, ":most_expensive_sold_imod", ":imod"),
	  #	(assign, ":most_expensive_sold_price", ":score"),
	  #(try_end),

	  #Log the transaction even if in dry run mode
	  (val_sub, ":m_gold", ":score"),
	  (val_add, ":gold_gained", ":score"),
	  (val_add, ":items_sold", 1),
	  (val_sub, ":space", 1),

	  #If not a dry run, apply the transaction
	  (neq, ":actually_sell_items", 0),
	  (troop_add_item, ":merchant", ":item", ":imod"),
	  (troop_set_inventory_slot, ":customer", ":i_slot", -1),
	  (troop_remove_gold, ":merchant", ":score"),
	  (troop_add_gold, ":customer", ":score"),
      #dplmc+ end changed section
    (try_end),

	(set_show_messages, 1),#<- dplmc+ added

	#dplmc+ added section begin
	#Print a message if appropriate
	(try_begin),
		(is_between, ":actually_sell_items", 2, 4),#2 or 3
		(this_or_next|ge, ":items_sold", 1),
			(eq, ":actually_sell_items", 3),
		(assign, reg0, ":gold_gained"),
		(assign, reg1, ":items_sold"),
		(store_sub, reg3, reg1, 1),
		(str_store_troop_name, s0, ":merchant"),
		(try_begin),
			(this_or_next|is_between, ":merchant", quick_battle_troops_begin, quick_battle_troops_end),
			(this_or_next|is_between, ":merchant", heroes_begin, heroes_end),
			(this_or_next|is_between, ":merchant", dplmc_employees_begin, dplmc_employees_end),
			(is_between, ":merchant", walkers_end, tournament_champions_end),
			(display_message, "@You sold {reg1} {reg3?items:item} to {s0} and gained {reg0} {reg3?denars:denar}."),
		(else_try),
			(display_message, "@You sold {reg1} {reg3?items:item} to the {s0} and gained {reg0} {reg3?denars:denar}."),
		(try_end),
	(try_end),

	#Revert variables
	(assign, reg2, ":save_reg2"),
	(assign, reg3, ":save_reg3"),
	(assign, reg65, ":save_reg65"),
	(assign, "$g_talk_troop", ":save_talk_troop"),

	#Return diagnostics
	(assign, reg0, ":gold_gained"),
	(assign, reg1, ":items_sold"),
	#dplmc+ added section end
  ]),
  #auto sell credit rubik (CC) end

  ##For use with autosell
  #Input: center_no
  #Output: none
  ("dplmc_player_auto_sell_at_center", [
     (store_script_param, ":center_no", 1),
	 (assign, ":save_reg0", reg0),
	 (assign, ":save_reg1", reg1),
	 (try_begin),
	    ##For Towns:
		(is_between, ":center_no", towns_begin, towns_end),
		(try_begin),
			#1. Selling weapons, shields, and ranged weapons to the weaponsmith
		    (party_get_slot, ":merchant_troop", ":center_no", slot_town_weaponsmith),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", weapons_begin, ranged_weapons_end, 2),
		(try_end),
		(try_begin),
			#2. Selling armor to the armorer
			(party_get_slot, ":merchant_troop", ":center_no", slot_town_armorer),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", armors_begin, armors_end, 2),
 		(try_end),
		(try_begin),
			#3. Selling horses to the horse merchant
			(party_get_slot, ":merchant_troop", ":center_no", slot_town_horse_merchant),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", horses_begin, horses_end, 2),
		(try_end),
		(try_begin),
			#4. Selling whatever may remain to the general merchant
			(party_get_slot, ":merchant_troop", ":center_no", slot_town_merchant),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", all_items_begin, all_items_end, 2),
		(try_end),
	 (else_try),
		##For Villages:
		(is_between, ":center_no", villages_begin, villages_end),
		(party_get_slot, ":merchant_troop", ":center_no", slot_town_elder),
		(ge, ":merchant_troop", 1),
		(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", all_items_begin, all_items_end, 2),
	 (else_try),
	    ##Error
		(assign, reg0, ":center_no"),
		(display_message, "@{!} ERROR FOR AUTOSELL for town ID {reg0}: Bad town or merchant was missing"),
	 (try_end),
	 (assign, reg0, ":save_reg0"),
	 (assign, reg1, ":save_reg1"),
  ]),

##Adapted Auto-Buy-Food from rubik's Custom Commander
#Changed to parameterize merchant and customer, but did not finish expanding
#the script to work with non-player arguments.  (There is currently no need,
#but I can imagine using it for NPCs sent on item-purchasing missions, or if
#NPC parties had to buy food.)
#
##OLD: Overwrites: reg1, reg2, reg3, reg4
##NEW: Overwrite reg0
#
#INPUT:
#      arg1 :customer
#      arg2 :merchant_troop
  ("dplmc_auto_buy_food", [
    (store_script_param, ":customer", 1),
    (store_script_param, ":merchant_troop", 2),
    ##added section begin, preserve registers
    (assign, ":save_reg1", reg1),
    (assign, ":save_reg2", reg2),
    (assign, ":save_reg3", reg3),
    (assign, ":save_reg4", reg4),
    ##added section end

    (assign, ":customer_in_player_party", 0),#Always assumed true... re-write if you need to use for others

    (store_troop_gold, ":begin_gold", ":customer"),
    (store_free_inventory_capacity, ":begin_space", ":customer"),
    (troop_get_inventory_capacity, ":inv_cap", ":merchant_troop"),
    (set_show_messages, 0),
    (try_for_range, ":i_slot", 10, ":inv_cap"),
      (troop_get_inventory_slot, ":item", ":merchant_troop", ":i_slot"),
      (gt, ":item", -1),
      (is_between, ":item", food_begin, food_end),
      (troop_inventory_slot_get_item_amount, ":amount", ":merchant_troop", ":i_slot"),
      ##dplmc+: The next line required making a change to header_operations.py
      (troop_inventory_slot_get_item_max_amount, ":max_amount", ":merchant_troop", ":i_slot"),
      (eq, ":amount", ":max_amount"),

      (item_get_slot, ":food_portion", ":item", dplmc_slot_item_food_portion),
      (val_max, ":food_portion", 0),#dplmc+ added
      (store_item_kind_count, ":food_count", ":item", ":customer"),
      (lt, ":food_count", ":food_portion"),
      (store_free_inventory_capacity, ":free_inv_cap", ":customer"),
      (gt, ":free_inv_cap", 0),

      (call_script, "script_game_get_item_buy_price_factor", ":item"),
      (assign, ":buy_price_factor", reg0),
      (store_item_value,":score",":item"),
      (val_mul, ":score", ":buy_price_factor"),
      (val_div, ":score", 100),
      (val_max, ":score",1),
      (store_troop_gold, ":customer_gold", ":customer"),
      (ge, ":customer_gold", ":score"),

      (troop_add_item, ":customer", ":item"),
      (troop_set_inventory_slot, ":merchant_troop", ":i_slot", -1),
      (troop_remove_gold, ":customer", ":score"),
      (troop_add_gold, ":merchant_troop", ":score"),
    (try_end),
    (set_show_messages, 1),
    (store_troop_gold, ":end_gold", ":customer"),
    (store_free_inventory_capacity, ":end_space", ":customer"),
    (try_begin),
      (neq, ":end_gold", ":begin_gold"),
      (store_sub, reg1, ":begin_gold", ":end_gold"),
      (store_sub, reg2, ":begin_space", ":end_space"),
      (store_sub, reg3, reg1, 1),
      (store_sub, reg4, reg2, 1),
      (eq, ":customer_in_player_party", 1),#<- added
      (display_message, "@You have bought {reg2} {reg4?kinds:kind} of food and lost {reg1} {reg3?denars:denar}."),
    (try_end),

    # sell rotten food
    (store_troop_gold, ":begin_gold", ":customer"),
    (store_free_inventory_capacity, ":begin_space", ":customer"),
    (troop_get_inventory_capacity, ":inv_cap", ":customer"),
    (set_show_messages, 0),
    (try_for_range, ":i_slot", 10, ":inv_cap"),
      (troop_get_inventory_slot, ":item", ":customer", ":i_slot"),
      (gt, ":item", -1),
      (is_between, ":item", food_begin, food_end),
      (troop_get_inventory_slot_modifier, ":imod", ":customer", ":i_slot"),
      (eq, ":imod", imod_rotten),
      (store_free_inventory_capacity, ":free_inv_cap", ":merchant_troop"),
      (gt, ":free_inv_cap", 0),

      (call_script, "script_dplmc_get_item_value_with_imod", ":item", ":imod"),
      (assign, ":score", reg0),
      (val_div, ":score", 100),
      (call_script, "script_game_get_item_sell_price_factor", ":item"),
      (assign, ":sell_price_factor", reg0),
      (val_mul, ":score", ":sell_price_factor"),
      (troop_inventory_slot_get_item_amount, ":amount", ":customer", ":i_slot"),
      (troop_inventory_slot_get_item_max_amount, ":max_amount", ":customer", ":i_slot"),
      (val_mul, ":score", ":amount"),
      (val_div, ":score", ":max_amount"),
      (val_div, ":score", 100),
      (val_max, ":score",1),
      (store_troop_gold, ":merchant_gold", ":merchant_troop"),
      (ge, ":merchant_gold", ":score"),

      #(troop_add_item, ":merchant_troop", ":item", ":imod"),
      (troop_set_inventory_slot, ":customer", ":i_slot", -1),
      (troop_remove_gold, ":merchant_troop", ":score"),
      (troop_add_gold, ":customer", ":score"),
    (try_end),
    (set_show_messages, 1),
    (store_troop_gold, ":end_gold", ":customer"),
    (store_free_inventory_capacity, ":end_space", ":customer"),
    (try_begin),
      (neq, ":end_gold", ":begin_gold"),
      (store_sub, reg1, ":end_gold", ":begin_gold"),
      (store_sub, reg2, ":end_space", ":begin_space"),
      (store_sub, reg3, reg1, 1),
      (store_sub, reg4, reg2, 1),
      (eq, ":customer_in_player_party", 1), #<- added
      (display_message, "@You sold {reg2} {reg4?kinds:kind} of rotten food and gained {reg1} {reg3?denars:denar}."),
    (try_end),
    ##added section begin, preserve registers
    (assign, reg1, ":save_reg1"),
    (assign, reg2, ":save_reg2"),
    (assign, reg3, ":save_reg3"),
    (assign, reg4, ":save_reg4"),
    ##added section end
  ]),
##Auto-Buy-Food from rubik's Custom Commander end

  # script_dplmc_get_trade_penalty
  #
  #This is similar to the old script_get_trade_penalty,
  #except it uses parameters instead of relying on global variables.
  #
  # Input:
  # param1: item_kind_id
  # param2: market center
  # param3: customer troop (-1 for a non-troop-specific answer, -2 to notify the script that this is being used to evaluate a gift)
  # param4: merchant troop (-1 for a non-troop-specific answer)
  # Output: reg0

  ("dplmc_get_trade_penalty",
    [
	  #Additions begin:
      (store_script_param, ":item_kind_id", 1),
      (store_script_param, ":market_center", 2),
      (store_script_param, ":customer_troop", 3),
      (store_script_param, ":merchant_troop", 4),
      #End Additions
      (assign, ":penalty",0),

	  ##Change this to support alternative customers
      ##(party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
	  (try_begin),
		 #Player: use skill of player party
	     (eq, ":customer_troop", "trp_player"),
		 (party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
	  (else_try),
		 #Hero leading a party: use skill of led party
	     (gt, ":customer_troop", -1),
	     (troop_is_hero, ":customer_troop"),
		 (troop_get_slot, ":customer_party", ":customer_troop", slot_troop_leaded_party),
		 (gt, ":customer_party", 0),
		 (party_is_active, ":customer_party"),
		 (party_get_skill_level, ":trade_skill", ":customer_party", skl_trade),
	  (else_try),
		 #Troop: use troop skill
		 (gt, ":customer_troop", -1),
		 (store_skill_level, ":trade_skill", ":customer_troop"),
	  (else_try),
		 (assign, ":trade_skill", 0),
	  (try_end),
	  ##End Change
      (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (assign, ":penalty",15), #reduced slightly
        (store_mul, ":skill_bonus", ":trade_skill", 1),
        (val_sub, ":penalty", ":skill_bonus"),
      (else_try),
        (assign, ":penalty",100),
        (store_mul, ":skill_bonus", ":trade_skill", 5),
        (val_sub, ":penalty", ":skill_bonus"),
      (try_end),

      (assign, ":penalty_multiplier", average_price_factor),#<-- replaced 1000 with average_price_factor
##       # Apply penalty if player is hostile to merchants faction
##      (store_relation, ":merchants_reln", "fac_merchants", "fac_player_supporters_faction"),
##      (try_begin),
##        (lt, ":merchants_reln", 0),
##        (store_sub, ":merchants_reln_dif", 10, ":merchants_reln"),
##        (store_mul, ":merchants_relation_penalty", ":merchants_reln_dif", 20),
##        (val_add, ":penalty_multiplier", ":merchants_relation_penalty"),
##      (try_end),

       # Apply penalty if player is on bad terms with the town
      (try_begin),
		(eq, ":customer_troop", "trp_player"),#added
        (is_between, ":market_center", centers_begin, centers_end),#changed $g_encountered_party to :market_center
        (party_get_slot, ":center_relation", ":market_center", slot_center_player_relation),#changed $g_encountered_party to :market_center
        (store_mul, ":center_relation_penalty", ":center_relation", -3),
        (val_add, ":penalty_multiplier", ":center_relation_penalty"),
        (try_begin),
          (lt, ":center_relation", 0),
          (store_sub, ":center_penalty_multiplier", 100, ":center_relation"),
          (val_mul, ":penalty_multiplier", ":center_penalty_multiplier"),
          (val_div, ":penalty_multiplier", 100),
        (try_end),
      (try_end),

       # Apply penalty if player is on bad terms with the merchant (not currently used)
	   ##Begin Change
      #(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
      #(assign, ":troop_reln", reg0),
	  (try_begin),
		 (this_or_next|eq, ":merchant_troop", "trp_player"),
			(eq, ":customer_troop", "trp_player"),
		 (gt, ":merchant_troop", -1),
		 (gt, ":customer_troop", -1),
		 (call_script, "script_troop_get_player_relation", ":merchant_troop"),
		 (assign, ":troop_reln", reg0),
	  (else_try),
	    (is_between, ":merchant_troop", heroes_begin, heroes_end),
		 (is_between, ":customer_troop", heroes_begin, heroes_end),
		 (call_script, "script_troop_get_relation_with_troop", ":merchant_troop", ":customer_troop"),
		 (assign, ":troop_reln", reg0),
	  (else_try),
	     (assign, ":troop_reln", 0),
	  (try_end),
	  ##End Change
      #(troop_get_slot, ":troop_reln", "$g_talk_troop", slot_troop_player_relation),
      (try_begin),
        (lt, ":troop_reln", 0),
        (store_sub, ":troop_reln_dif", 0, ":troop_reln"),
        (store_mul, ":troop_relation_penalty", ":troop_reln_dif", 20),
        (val_add, ":penalty_multiplier", ":troop_relation_penalty"),
      (try_end),


	  (try_begin),
		##Begin Change
		#(is_between, "$g_encountered_party", villages_begin, villages_end),
		(is_between, ":market_center", centers_begin, centers_end),
		(party_slot_eq, ":market_center", slot_party_type, spt_village),
		##End Change
	    (val_mul, ":penalty", 2),
	  (try_end),

	  (try_begin),
        (is_between, ":market_center", centers_begin, centers_end),#changed $g_encountered_party to :market_center
	    #Double trade penalty if no local production or consumption
	    (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
		##Begin Change
		#(OPTIONAL CHANGE: Do not apply this to food)
		(this_or_next|eq, ":customer_troop", -2),
        (this_or_next|lt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		   (neg|is_between, ":item_kind_id", food_begin, food_end),

		(assign, ":save_reg1", reg1),
		(assign, ":save_reg2", reg2),
		##End Change
	    (call_script, "script_center_get_production", ":market_center", ":item_kind_id"),#changed $g_encountered_party to :market_center
	    (eq, reg0, 0),
	    (call_script, "script_center_get_consumption", ":market_center", ":item_kind_id"),#changed $g_encountered_party to :market_center
	    (eq, reg0, 0),
	    (val_mul, ":penalty", 2),
		##Begin Change
		(assign, reg1, ":save_reg1"),
		(assign, reg2, ":save_reg2"),
		##End Change
	  (try_end),

      (val_mul, ":penalty",  ":penalty_multiplier"),
	  ##Begin Change
	  (val_add, ":penalty", average_price_factor // 2),#round in the correct direction (we don't need to worry about penalty < 0)
      (val_div, ":penalty", average_price_factor),#replace the hardcoded constant 1000 with average_price_factor
	  ##End Change
      (val_max, ":penalty", 1),
      (assign, reg0, ":penalty"),
  ]),


##"script_dplmc_print_cultural_word_to_sreg"
##INPUTS:
#  arg1  - speaker troop
#  arg2  - which word/phrase to retrieve (arbitrary code)
#  arg3  - string register
#OUTPUTS:
#  writes result to string register
   ("dplmc_print_cultural_word_to_sreg", [
     (store_script_param, ":speaker", 1),
     (store_script_param, ":context", 2),
     (store_script_param, ":string_register", 3),

     #Right now this is entirely faction-based, but you could give different
     #results for individual lords.
	 #(Note: Now certain parts of it do vary for heroes, to mimic the behavior in Native
	 #feast dialogs for the word for wine.)

     (assign, ":speaker_faction", -1),
     (try_begin),
		#Player faction
		(this_or_next|eq, ":speaker", "trp_player"),
			(eq, ":speaker", "trp_kingdom_heroes_including_player_begin"),
		(assign, ":speaker_faction", "fac_player_supporters_faction"),#<- This will potentially get translated later
	 (else_try),
		#Hero original faction
        (is_between, ":speaker", heroes_begin, heroes_end),
        (troop_get_slot, ":speaker_faction", ":speaker", slot_troop_original_faction),
	 (else_try),
		#Hero original faction
		(gt, ":speaker", -1),
		(troop_is_hero, ":speaker"),
		(troop_slot_ge, ":speaker", slot_troop_original_faction, npc_kingdoms_begin),
		(neg|troop_slot_ge, ":speaker", slot_troop_original_faction, npc_kingdoms_end),
		(troop_get_slot, ":speaker_faction", ":speaker", slot_troop_original_faction),
     (else_try),
		#Troop current faction
        (gt, ":speaker", -1),
        (store_troop_faction, ":speaker_faction", ":speaker"),
     (try_end),

	 (try_begin),
      (lt, ":speaker", 1),
     (else_try),
	   ##Only continue if the current faction isn't associated with a distinctive culture
	   (lt, ":speaker_faction", dplmc_non_generic_factions_begin),
	   ##This will work unless the order of the first factions gets changed
	 (else_try),
	   #Translate raiders into the equivalent kingdoms
	   (is_between, ":speaker", bandits_begin, bandits_end),
         (try_begin),
			(eq, ":speaker", "trp_mountain_bandit"),#Mountain bandits
			(assign, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
		 (else_try),
			(eq, ":speaker", "trp_forest_bandit"),#Forest bandits
			(assign, ":speaker_faction", "fac_kingdom_1"),#Swadian
		 (else_try),
			(eq, ":speaker", "trp_sea_raider"),#Sea raiders
			(assign, ":speaker_faction", "fac_kingdom_4"),#Nords
		 (else_try),
			(eq, ":speaker", "trp_steppe_bandit"),#Steppe bandits
			(assign, ":speaker_faction", "fac_kingdom_3"),#Khergits
		 (else_try),
			(eq, ":speaker", "trp_taiga_bandit"),#Taiga bandits
			(assign, ":speaker_faction", "fac_kingdom_2"),#Vaegir
		 (else_try),
			(eq, ":speaker", "trp_desert_bandit"),#Desert bandits
			(assign, ":speaker_faction", "fac_kingdom_6"),#Sarranid
		 (try_end),
		 (ge, ":speaker_faction", dplmc_non_generic_factions_begin),
    (else_try),
		#For companions without default initial cultures, infer one from their home.
		#(Actually, don't limit this to companions, since there's a chance that others
		#could have a valid home slot.)
		#(is_between, ":speaker", companions_begin, companions_end),
		#(is_between, ":speaker", heroes_begin, heroes_end),
		(troop_is_hero, ":speaker"),
		(troop_get_slot, ":home_center", ":speaker", slot_troop_home),
		(is_between, ":home_center", centers_begin, centers_end),
		(party_get_slot, ":speaker_faction", ":home_center", slot_center_original_faction),
	 (else_try),
		#For villagers, merchants, etc.
		(eq, ":speaker", "$g_talk_troop"),
		(neg|is_between, ":speaker", heroes_begin, heroes_end),#Not a character that might have an explicitly-set faction
		(neg|is_between, ":speaker", training_ground_trainers_begin, tavern_minstrels_end),#Not a trainer, ransom broker, traveler, bookseller, or minstrel
		(ge, "$g_encountered_party", 0),
		(try_begin),
			#For towns / castles / villages, use the original faction
			(is_between, "$g_encountered_party", centers_begin, centers_end),
			(party_get_slot, ":speaker_faction", "$g_encountered_party", slot_center_original_faction),
		(else_try),
			#Use faction of encountered party
			(party_is_active, "$g_encountered_party"),
			(store_faction_of_party, ":speaker_faction", "$g_encountered_party"),
			#For generic factions, use the closest center
			(lt, ":speaker_faction", dplmc_non_generic_factions_begin),
			(assign, ":speaker_faction", reg0),#save register
			(call_script, "script_get_closest_center", "$g_encountered_party"),
			(assign, ":home_center", reg0),
			(assign, reg0, ":speaker_faction"),#revert register
			(party_get_slot, ":speaker_faction", ":home_center", slot_center_original_faction),
		(try_end),
	 (try_end),

    #Translate for player's kingdom
	 (try_begin),
		(ge, "$players_kingdom", dplmc_non_generic_factions_begin),
		(this_or_next|eq, ":speaker_faction", "fac_player_faction"),
		(this_or_next|eq, ":speaker_faction", "fac_player_supporters_faction"),
		(eq, ":speaker_faction", "$players_kingdom"),
		(assign, ":speaker_faction", "$players_kingdom"),
		(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(this_or_next|is_between, "$g_player_culture", cultures_begin, cultures_end),
		(is_between,"$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
		(assign, ":speaker_faction", "$g_player_culture"),
	 (try_end),

     #Store variant
     (try_begin),
        #Iconic cultural weapon that can be used metonymously for force of arms.
		#Native equivalent is "sword".
		#Non-Warband example: "He who lives by the {sword}, dies by the {sword}."
		#Example usage: "My {sword} is at the disposal of my liege."
		(eq, ":context", DPLMC_CULTURAL_TERM_WEAPON),
        (try_begin),
           (this_or_next|eq, ":speaker_faction", "fac_kingdom_4"),#Nords
           (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
           (str_store_string, ":string_register", "@axe"),
        (else_try),
           (eq, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
           (str_store_string, ":string_register", "@spear"),
        (else_try),
           (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
           (str_store_string, ":string_register", "@bow"),
        (else_try),
			#Default: Swadia, Sarranid, others
           (str_store_string, ":string_register", "@sword"),
        (try_end),
    (else_try),
        #Plural version of iconic cultural weapon that can be used metonymously for force of arms.
		#Native equivalent is "swords".
		(eq, ":context", DPLMC_CULTURAL_TERM_WEAPON_PLURAL),
        (try_begin),
           (this_or_next|eq, ":speaker_faction", "fac_kingdom_4"),#Nords
           (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
           (str_store_string, ":string_register", "@axes"),
        (else_try),
           (eq, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
           (str_store_string, ":string_register", "@spears"),
        (else_try),
           (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
           (str_store_string, ":string_register", "@bows"),
        (else_try),
			#Default: Swadia, Sarranid, others
           (str_store_string, ":string_register", "@swords"),
        (try_end),
	 (else_try),
		#Cultural phrase that means "fight" (first person singular)
		#Native equivalent is "swing my sword."
		#Example usage: "I want to be able to {swing my sword} with a good conscience."
        (eq, ":context", DPLMC_CULTURAL_TERM_USE_MY_WEAPON),
        (try_begin),
           (eq, ":speaker_faction", "fac_kingdom_4"),#Nords
           (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
           (str_store_string, ":string_register", "@swing my axe"),
        (else_try),
           (eq, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
           (str_store_string, ":string_register", "@lift my spear"),
        (else_try),
           (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
           (str_store_string, ":string_register", "@loose my arrows"),
        (else_try),
			#Default: Swadia, Sarranid, others
           (str_store_string, ":string_register", "@swing my sword"),
        (try_end),
	(else_try),
		#equivalent to lowercase "king" or "queen"
		(this_or_next|eq, ":context", DPLMC_CULTURAL_TERM_KING_FEMALE),
		(eq, ":context", DPLMC_CULTURAL_TERM_KING),
		(try_begin),
		   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergit
		   (str_store_string, ":string_register", "str_khan"),
		(else_try),
		   (eq, ":speaker_faction", "fac_kingdom_6"),#Sarranid
		   (str_store_string, ":string_register", "@sultan"),
		(else_try),
		   #Default: Swadia, Rhodok, Nord, Vaegir, others
		   (str_store_string, ":string_register", "str_king"),
		   (eq, ":context", DPLMC_CULTURAL_TERM_KING_FEMALE),
		   (str_store_string, ":string_register", "str_queen"),
		(try_end),
	(else_try),
		#equivalent to lowercase "kings"
		(eq, ":context", DPLMC_CULTURAL_TERM_KING_PLURAL),
		(try_begin),
		   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergit
		   (str_store_string, ":string_register", "@khans"),
		(else_try),
		   (eq, ":speaker_faction", "fac_kingdom_6"),#Sarranid
		   (str_store_string, ":string_register", "@sultans"),
		(else_try),
 		   #Default: Swadia, Rhodok, Nord, Vaegir, others
		   (str_store_string, ":string_register", "@kings"),
		(try_end),
	(else_try),
		#equivalent to lowercase "lord"
		(eq, ":context", DPLMC_CULTURAL_TERM_LORD),
		(str_store_string, ":string_register", "@lord"),
	(else_try),
		#equivalent to lowercase "lords"
		(eq, ":context", DPLMC_CULTURAL_TERM_LORD_PLURAL),
		(str_store_string, ":string_register", "@lords"),
	(else_try),
		#As in, "I shall tell my {swineherd} about your sweet promises" or "Any {swineherd} can claim to be king".
		(eq, ":context", DPLMC_CULTURAL_TERM_SWINEHERD),
		(assign, ":mode", ":speaker"),
		(try_begin),
		   (gt, ":speaker", 0),
		   (neg|troop_is_hero, ":speaker"),
		   (store_current_hours, ":mode"),
		   (val_add, ":mode", "$g_encountered_party"),
		(try_end),
		(val_max, ":mode", 0),#Default to mode 0 for negative speakers
		(val_mod, ":mode", 2),
		(try_begin),
           (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
		   (try_begin),
		      (eq, ":mode", 0),
              (str_store_string, ":string_register", "@goatherd"),
		   (else_try),
		       (str_store_string, ":string_register", "@swineherd"),
		   (try_end),
        (else_try),
		   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
		   (try_begin),
		      (eq, ":mode", 0),
              (str_store_string, ":string_register", "@stable {boy/girl}"),
        (else_try),
		      (str_store_string, ":string_register", "@shepherd {boy/girl}"),
		   (try_end),
		(else_try),
		   (eq, ":speaker_faction", "fac_kingdom_6"),#Sarranids
		   (try_begin),
		      (eq, ":mode", 0),
		      (str_store_string, ":string_register", "@goatherd"),
		   (else_try),
		      (str_store_string, ":string_register", "@shepherd {boy/girl}"),
		   (try_end),
        (else_try),
           #Swadia, Rhodok, Nord, others
           (str_store_string, ":string_register", "@swineherd"),
        (try_end),
	(else_try),
		#As in, "I'd like to buy every man who comes in here tonight a jar of your best wine."
		(this_or_next|eq, ":context", DPLMC_CULTURAL_TERM_TAVERNWINE),
		#Follow the pattern used in Native for lords in feasts
		#(c.f. "str_flagon_of_mead", "str_skin_of_kumis", "str_mug_of_kvass", "str_cup_of_wine")

		(try_begin),
			#For lords, use "mode" so it works the same as in feast dialogs
			(is_between, ":speaker", heroes_begin, heroes_end),
			(this_or_next|neg|is_between, ":speaker", companions_begin, companions_end),
				(neg|troop_slot_eq, ":speaker", slot_troop_original_faction, ":speaker_faction"),
			(store_mod, ":mode", ":speaker", 2),
		(else_try),
			#Otherwise set mode to 0, to always use the cultural alternative
			(assign, ":mode", 0),
		(try_end),

		(try_begin),
			(eq, ":speaker_faction", "fac_kingdom_2"),
			(eq, ":mode", 0),#From feast: 50% chance of falling through to "wine"
			(str_store_string, ":string_register", "@kvass"),#Vaegirs: kvass
		(else_try),
			(eq, ":speaker_faction", "fac_kingdom_3"),
			(eq, ":mode", 0),#From feast: 50% chance of falling through to "wine"
			(str_store_string, ":string_register", "@kumis"),#Khergits: kumis
		(else_try),
			(eq, ":speaker_faction", "fac_kingdom_4"),
			(str_store_string, ":string_register", "@mead"),#Nords: mead
		(else_try),
			(str_store_string, ":string_register", "@wine"),#Default: wine
		(try_end),
    (else_try),
	#Error string
        (assign, ":save_reg0", reg0),
		(assign, reg0, ":context"),
		(display_message, "@{!}ERROR - dplmc_print_cultural_word_to_sreg called for bad context {reg0}"),
		(str_store_string, ":string_register", "str_ERROR_string"),
		(assign, reg0, ":save_reg0"),
    (try_end),

   ]),


  #script_dplmc_print_player_spouse_says_my_husband_wife_to_s0
  #
  #INPUT:
  #  arg1: troop_no
  #  arg2: whether the first letter must be capitalized
  #
  #OUTPUT:
  #    s0: a string that can be substituted for "my {husband/wife}" or "my love"
  ("dplmc_print_player_spouse_says_my_husband_wife_to_s0",
   [
     (store_script_param_1, ":troop_no"),
     (store_script_param_2, ":capitalized"),

 	 (assign, ":save_reg0", reg0),
	 (assign, ":save_reg6", reg6),
	 (assign, ":save_reg7", reg7),
	 #(assign, reg6, ":capitalized"),
	 (assign, reg7, 0),

    #Base switch is 50 (i.e. where the "brave champion" greeting starts)
    (try_begin),
      (lt, ":troop_no", 1),#bad value
      (assign, reg0, 0),
      (assign, reg6, lrep_none),
    (else_try),
	   (call_script, "script_troop_get_player_relation", ":troop_no"),#write relation to reg0
      (troop_get_slot, reg6, ":troop_no", slot_lord_reputation_type),#write relation to reg6
      (eq, reg6, lrep_conventional),#...jumps to next branch (keeping reg0 and reg6) if this isn't true
		(val_add, reg0, 25),#from 25+
	 (else_try),
      (eq, reg6, lrep_otherworldly),
		(val_add, reg0, 30),#from 20+
	 (else_try),
      (eq, reg6, lrep_moralist),
      (store_sub, reg7, "$player_honor", 10),
      (val_clamp, reg7, -40, 31),
      (val_add, reg0, reg7),
      (assign, reg7, 0),
    (else_try),
      (eq, reg6, lrep_ambitious),
      (assign, reg7, -10),
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
         (val_add, reg7, 10),
         (party_slot_eq, ":center_no", slot_party_type, spt_town),
         (val_add, reg7,  10),
      (try_end),
      (val_clamp, reg7, -10, 30),
      (val_add, reg0, reg7),
      (assign, reg7, 0),
    (else_try),
      (eq, reg6, lrep_adventurous),
      (val_add, reg7, 20),#from 30+
    (else_try),
      (eq, reg6, lrep_none),
      (is_between, reg6, heroes_begin, heroes_end),
      (val_sub, reg0, 20),#from 70+
    (else_try),
      (eq, reg6, lrep_cunning),
      (val_sub, reg0, 20),#from 70+
    (else_try),
      (this_or_next|eq, reg6, lrep_debauched),
      (this_or_next|eq, reg6, lrep_quarrelsome),
      (this_or_next|eq, reg6, lrep_selfrighteous),
      (val_sub, reg0, 30),#from 80+
	 (try_end),

    (try_begin),
       (ge, reg0, 50),
       (assign, reg7, 1),
    (try_end),

    (try_begin),
       #Embellishment: diminuitive pet-names
       (eq, reg6, lrep_debauched),
       (gt, ":troop_no", 0),
       (store_character_level, ":player_level", "trp_player"),
       (store_character_level, ":troop_level", ":troop_no"),
       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
       (this_or_next|ge, ":troop_level", ":player_level"),
       (this_or_next|troop_slot_ge, ":troop_no", slot_troop_renown, ":player_renown"),
          (lt, reg0, 50),
       (assign, reg6, ":capitalized"),#Whether the first letter needs to be upper case
       (str_store_string, s0, "@{reg6?M:m}y poppet"),
    (else_try),
       #The basic idea.  Further embellishments may come.
       (assign, reg6, ":capitalized"),#Whether the first letter needs to be upper case
       (str_store_string, s0, "str_dplmc_reg6my_reg7spouse"),
    (try_end),

	 #Revert registers
	 (assign, reg0, ":save_reg0"),
	 (assign, reg6, ":save_reg6"),
	 (assign, reg7, ":save_reg7"),
   ]),

  ##"script_dplmc_initialize_autoloot"
  ##
  ##Only needs to be called once, but it's safe to call multiple times
  ##(it uses "$g_autoloot" to store the version)
  ##
  ##Inputs: arg1: 1 to force this to run
  ##Outputs: None
  ("dplmc_initialize_autoloot",
  [
	(store_script_param_1, ":force_to_run"),

	(try_begin),
		#Check if there is anything to do
		(this_or_next|eq, ":force_to_run", 1),
			(neq, "$g_autoloot", 2),
      (try_begin),
		   #Print a message to make it obvious when this is happening more than it should.
		   (ge, "$cheat_mode", 1),
		   (store_current_hours, ":hours"),
		   (gt, ":hours", 0),
		   (display_message, "@{!}Initializing auto-loot.  This message should not appear more than once."),
      (try_end),
		#Initialize
		(try_for_range, ":cur_food", food_begin, food_end),
			(item_set_slot, ":cur_food", dplmc_slot_item_food_portion, 1),
		(try_end),

		# #deprecated due to 1.165 operations
		# (call_script, "script_dplmc_init_item_difficulties"),
		# (call_script, "script_dplmc_init_item_base_score"),

		(assign, "$g_dplmc_auto_sell_price_limit", 50),
		(assign, "$g_dplmc_sell_items_when_leaving", 0),
		(assign, "$g_dplmc_buy_food_when_leaving", 0),

		(item_set_slot, itp_type_book, dplmc_slot_item_type_not_for_sell, 1),
		(item_set_slot, itp_type_goods, dplmc_slot_item_type_not_for_sell, 1),
		(item_set_slot, itp_type_animal, dplmc_slot_item_type_not_for_sell, 1),

		(assign, "$g_autoloot", 2),
	(try_end),
  ]),


##"script_dplmc_get_troop_standing_in_faction"
#
#INPUT: arg1  :troop_no
#       arg2  :faction_no
#
#OUTPUT:
#       reg0  A constant with the value DPLMC_FACTION_STANDING_<something>
#
## Constants defined in module_constants.py
#DPLMC_FACTION_STANDING_LEADER = 60
#DPLMC_FACTION_STANDING_LEADER_SPOUSE = 50
#DPLMC_FACTION_STANDING_MARSHALL = 40
#DPLMC_FACTION_STANDING_LORD = 30
#DPLMC_FACTION_STANDING_DEPENDENT = 20
#DPLMC_FACTION_STANDING_MEMBER = 10#includes mercenaries
#DPLMC_FACTION_STANDING_PETITIONER = 5
#DPLMC_FACTION_STANDING_UNAFFILIATED = 0
##diplomacy end+
 ("dplmc_get_troop_standing_in_faction",
 [
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":faction_no"),

    (assign, ":standing", DPLMC_FACTION_STANDING_UNAFFILIATED),
    (assign, ":original_faction_no", ":faction_no"),
    (try_begin),
        #Translate fac_player_faction
        (eq, ":faction_no", "fac_player_faction"),
        (assign, ":faction_no", "fac_player_supporters_faction"),
    (try_end),

    (try_begin),
       (this_or_next|lt, ":troop_no", 0),#Do nothing, bad troop ID
          (lt, ":faction_no", 0),#Do nothing, bad faction
    (else_try),
       #Because of how this script is used, if fac_player_supporters_faction is active,
       # this always reports that the player is its leader (even though that is sometimes
       # untrue, for example in a claimant quest)
       (eq, ":troop_no", "trp_player"),#Short-circuit the remainder if these are true
       (eq, ":faction_no", "fac_player_supporters_faction"),
       (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
       # (neg|is_between, "$supported_pretender", pretenders_begin, pretenders_end), #SB : claimant exception
       (assign, ":standing", DPLMC_FACTION_STANDING_LEADER),
    (else_try),
		(try_begin),
			#Translate fac_player_supporters_faction
			(eq, ":faction_no", "fac_player_supporters_faction"),
			(gt, "$players_kingdom", 0),
			(assign, ":faction_no", "$players_kingdom"),
		(try_end),

        (store_faction_of_troop, ":troop_faction", ":troop_no"),
        (try_begin),
           #Translate fac_player_supporters_faction
           (this_or_next|eq, ":troop_no", "trp_player"),
           (this_or_next|eq, ":troop_faction", "fac_player_faction"),
           (eq, ":troop_faction", "fac_player_supporters_faction"),
           (assign, ":troop_faction", "fac_player_supporters_faction"),
           (gt, "$players_kingdom", 0),
           (assign, ":troop_faction", "$players_kingdom"),
        (try_end),
        (eq, ":troop_faction", ":faction_no"),#<- Short-circuit the remainder if this is false
        (assign, ":standing", DPLMC_FACTION_STANDING_MEMBER),

        (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
        (try_begin),
           #Faction leader
           (eq, ":faction_leader", ":troop_no"),
           (assign, ":standing", DPLMC_FACTION_STANDING_LEADER),
        (else_try),
           #Spouse of faction leader
           (gt, ":faction_leader", -1),
           (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
              (troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
           #Deal with possible uninitialized slot
           (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
           (this_or_next|neq, ":faction_leader", 0),
              (is_between, ":troop_no", heroes_begin, heroes_end),
           (assign, ":standing", DPLMC_FACTION_STANDING_LEADER_SPOUSE),
        (else_try),
           #Faction marshall
           (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
           (assign, ":standing", DPLMC_FACTION_STANDING_MARSHALL),
        (else_try),
           #If the troop is the player, if he has homage he is a lord.
           #Otherwise he is a mercenary.
           (eq, ":troop_no", "trp_player"),
           (try_begin),
              (this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
              (ge, "$player_has_homage", 1),
              (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
           (else_try),
              #If the player is married to a lord/lady in the faction, the
              #homage variable should always be set to 1+, but add a separate
              #check just in case.
              (troop_get_slot, reg0, "trp_player", slot_troop_spouse),
              (is_between, reg0, heroes_begin, heroes_end),
              (store_faction_of_troop, reg0, reg0),
              (this_or_next|eq, reg0, "fac_player_supporters_faction"),
              (eq, reg0, ":faction_no"),
              (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
           (try_end),
        (else_try),
            #None of the following conditions apply for non-heroes
            (this_or_next|lt, ":troop_no", heroes_begin),
                (neg|troop_is_hero, ":troop_no"),
        (else_try),
           #For kingdom heroes, part 1 (check lordship based on occupation)
           (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
           (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
           (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
        (else_try),
           #For kingdom ladies
           (this_or_next|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
           (assign, ":standing", DPLMC_FACTION_STANDING_DEPENDENT),
        (else_try),
           #For petitioners
           (eq, ":original_faction_no", "fac_player_supporters_faction"),
           (is_between, ":troop_no", lords_begin, lords_end),
           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
           (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
           (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
           (assign, ":standing", DPLMC_FACTION_STANDING_PETITIONER),
        (else_try),
            #For kingdom heroes, part 2 (all non-companion active NPCs)
            (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
            (neg|is_between, ":troop_no", companions_begin, companions_end),
            (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
        (try_end),
    (try_end),

    (assign, reg0,  ":standing"),
 ]),

 ## "script_dplmc_store_troop_is_eligible_for_affiliate_messages"
 ("dplmc_store_troop_is_eligible_for_affiliate_messages",
 [
	(store_script_param_1, ":troop_no"),
	(assign, ":is_eligible", 0),
	(assign, ":save_reg1", reg1),
	(try_begin),
		(lt, ":troop_no", 1),
	(else_try),
		(neg|troop_is_hero, ":troop_no"),
	(else_try),
		#Initialize :faction_no and :faction_relation
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		(store_relation, ":faction_relation", ":faction_no", "fac_player_supporters_faction"),
		(try_begin),
			(eq, ":faction_no", "$players_kingdom"),
			(val_max, ":faction_relation", 1),
		(try_end),
		#Companion
		(gt, ":faction_relation", -1),
		(is_between, ":troop_no", companions_begin, companions_end),
		(neg|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
		(troop_slot_ge, ":troop_no", slot_troop_player_relation, 20),
		(assign, ":is_eligible", 1),
	(else_try),
		#Faction marshall (if the player is the faction leader)
		#Faction leader (if the player is the faction marshall)
		(eq, ":faction_no", "$players_kingdom"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
		(call_script, "script_dplmc_get_troop_standing_in_faction", ":troop_no", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
		(assign, ":is_eligible", 1),
	(else_try),
		#Spouse / relatives / in-laws
		(gt, ":faction_relation", -1),
		#(is_between, ":troop_no", heroes_begin, heroes_end),## should be safe even for non-heroes
		(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", "trp_player"),
		(ge, reg0, 2),
		(troop_get_slot, reg1, ":troop_no", slot_troop_player_relation),
		(val_add, reg0, reg1),
		(ge, reg0, 20),
		(assign, ":is_eligible", 1),
	(else_try),
		#Affiliates
		(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
		(ge, reg0, 1),
		(assign, ":is_eligible", 1),
	(else_try),
		#Cheat mode: add faction leaders to test this out
		(gt, "$cheat_mode", 0),
		(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
		(faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
		(assign, ":is_eligible", 1),
	(try_end),
	(assign, reg1, ":save_reg1"),
	(assign, reg0, ":is_eligible"),
 ]),

# "script_dplmc_sell_all_prisoners"
#
# Taken from rubik's Custom Commander, and altered to have parameters
# and return feedback.
#
#INPUT:
#Arg 1: actually remove (positive for yes, zero or negative for no)
#Arg 2: if positive, use this as a fixed price instead of calculating dynamically
#OUTPUT:
#reg0: amount of gold gained (or would have been gained if the sale occurred)
#reg1: number of prisoners sold (or would have been sold if the sale occurred)
  ("dplmc_sell_all_prisoners",
   [
    (store_script_param_1, ":actually_remove"),
    (store_script_param_2, ":fixed_price"),

    (assign, ":total_removed", 0),
    (assign, ":total_income", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
    (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
      (party_prisoner_stack_get_troop_id, ":troop_no", "p_main_party", ":i_stack"),
      #SB : correction to use game script
      (call_script, "script_game_check_prisoner_can_be_sold", ":troop_no"),
      (eq, reg0, 1),
      # (neg|troop_is_hero, ":troop_no"),
      (party_prisoner_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
      (try_begin),
         (gt, ":fixed_price", 0),
         (assign, ":sell_price", ":fixed_price"),
      (else_try),
         (call_script, "script_game_get_prisoner_price", ":troop_no"),
         (assign, ":sell_price", reg0),
      (try_end),
      (store_mul, ":stack_total_price", ":sell_price", ":stack_size"),
      (val_add, ":total_income", ":stack_total_price"),
      (val_add, ":total_removed", ":stack_size"),
      (gt, ":actually_remove", 0),#Stop short if this is a dry run
      (party_remove_prisoners, "p_main_party", ":troop_no", ":stack_size"),
    (try_end),
    (try_begin),
      (gt, ":actually_remove", 0),#Stop short if this is a dry run
      (troop_add_gold, "trp_player", ":total_income"),
    (try_end),
    (assign, reg0, ":total_income"),
    (assign, reg1, ":total_removed"),
  ]),

#"script_dplmc_translate_inactive_player_supporter_faction_2"
#
#Since "fac_player_supporters_faction" is often used as a parameter when what
#is really meant is "the faction led by the player" (which is never a different
#faction in Native), there are many calls we want to change.  Another solution
#is to approach the problem from the other side, and "correct" the arguments.
#
#If exactly one argument is equal to fac_player_supporters_faction, and fac_player_supporters_faction
#is not sfs_active, and $players_kingdom is an NPC kingdom of which the player is ruler or co-ruler,
#and the other argument is not equal to $players_kingdom, then the argument equal to fac_player_supporters_faction
#will be replaced with $players_kingdom.
#
#INPUT:
# arg1 - faction_1
# arg2 - faction_2
#OUTPUT:
# reg0 - faction_1, possibly replacing fac_player_supporters_faction with $players_kingdom (see above)
# reg1 - faction_2, possibly replacing fac_player_supporters_faction with $players_kingdom (see above)
("dplmc_translate_inactive_player_supporter_faction_2",
[
    (store_script_param_1, ":faction_1"),
    (store_script_param_2, ":faction_2"),

	(try_begin),
		(this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
		(this_or_next|neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(this_or_next|eq, ":faction_1", "$players_kingdom"),
		(this_or_next|eq, ":faction_2", "$players_kingdom"),
			(eq, ":faction_1", ":faction_2"),
      #Do nothing
	(else_try),
		(eq, ":faction_1", "fac_player_supporters_faction"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":faction_1", "$players_kingdom"),
	(else_try),
		(eq, ":faction_2", "fac_player_supporters_faction"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":faction_2", "$players_kingdom"),
	(try_end),

	(assign, reg0, ":faction_1"),
	(assign, reg1, ":faction_2"),
]),

##"script_cf_dplmc_player_party_meets_autoloot_conditions"
##
#
#INPUT:
#   None
#OUTPUT:
#   reg0   -1 means there are no companions and skill is too low
#           0 means there are companions and skill is too low
#           1 means skill is high enough but there are no companions
#           2 means skill is high enough and there are companions
#
# Will fail if it does not set reg0 to 2.
##
("cf_dplmc_player_party_meets_autoloot_conditions",
[
	  (store_skill_level, ":best_loot_skill", "skl_looting", "trp_player"),
	  (store_skill_level, ":player_inv_skill", "skl_inventory_management", "trp_player"),
	  (assign, ":best_inv_skill", ":player_inv_skill"),
	  (assign, ":num_companions", 0),
      (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
         (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
		 (ge, ":stack_troop", 0),
		 #Check skill
		 (is_between, ":stack_troop", heroes_begin, heroes_end),
		 (store_skill_level, ":hero_skill", "skl_inventory_management", ":stack_troop"),
		 (val_max, ":best_inv_skill", ":hero_skill"),

		 (store_skill_level, ":hero_skill", "skl_looting", ":stack_troop"),
		 (val_max, ":best_loot_skill", ":hero_skill"),
		 #Check is companion
         (is_between, ":stack_troop", companions_begin, companions_end),
         (val_add, ":num_companions", 1),
      (try_end),

	  (try_begin),
	    (lt, ":player_inv_skill", 2),
		(lt, ":best_inv_skill", 3),
		(lt, ":best_loot_skill", 2),
		(assign, reg0, 0),
		(try_begin),
			(lt, ":num_companions", 1),#change 2011-06-07
			(assign, reg0, -1),
		(try_end),
	  (else_try),
		(assign, reg0, 1),
		(gt, ":num_companions", 0),
		(assign, reg0, 2),
	  (try_end),

	  (eq, reg0, 2),
]),


##"script_dplmc_troop_get_family_relation_to_troop"
##
##Like troop_get_family_relation_to_troop, except instead of writing to s11,
##it writes the index of the relation string to reg1, and writes nothing at
##all to reg4.
  ("dplmc_troop_get_family_relation_to_troop",
    [
    (store_script_param_1, ":troop_1"),
    (store_script_param_2, ":troop_2"),

    ##dplmc start+

	(try_begin),
		(eq, ":troop_1", active_npcs_including_player_begin),
		(assign, ":troop_1", "trp_player"),
	(try_end),
	(try_begin),
		(eq, ":troop_2", active_npcs_including_player_begin),
		(assign, ":troop_2", "trp_player"),
	(try_end),

	#use gender script
    #(troop_get_type, ":gender_1", ":troop_1"),
	(call_script, "script_dplmc_store_troop_is_female", ":troop_1"),
	(assign, ":gender_1", reg0),
	(assign, ":relation_string", "str_no_relation"),
	##dplmc end+
	(assign, ":relation_strength", 0),

	##dplmc start+
	#Uninitialized memory is 0, which equals "trp_player", which is the cause
	#of some annoying bugs.  In Native the game doesn't set the various family
	#slots to -1 except for the player and in the heroes_begin to heroes_end
	#range.

	(troop_get_slot, ":spouse_of_1", ":troop_1", slot_troop_spouse),#just do this to get an error if the troop ID is bad
	(troop_get_slot, ":spouse_of_2", ":troop_2", slot_troop_spouse),#just do this to get an error if the troop ID is bad

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_spouse),
	(assign, ":spouse_of_1", reg0),
	(assign, ":spouse_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":spouse_of_1", ":spouse_of_2", slot_troop_father),
	(assign, ":father_of_spouse_of_1", reg0),
	(assign, ":father_of_spouse_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":spouse_of_1", ":spouse_of_2", slot_troop_mother),
	#(assign, ":mother_of_spouse_of_1", reg0),
	(assign, ":mother_of_spouse_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_father),
	(assign, ":father_of_1", reg0),
	(assign, ":father_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_mother),
	(assign, ":mother_of_1", reg0),
	(assign, ":mother_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":father_of_1", ":father_of_2", slot_troop_father),
	(assign, ":paternal_grandfather_of_1", reg0),
	(assign, ":paternal_grandfather_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":father_of_1", ":father_of_2", slot_troop_mother),
	(assign, ":paternal_grandmother_of_1", reg0),
	(assign, ":paternal_grandmother_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":mother_of_1", ":mother_of_2", slot_troop_father),
	(assign, ":maternal_grandfather_of_1", reg0),
	(assign, ":maternal_grandfather_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":mother_of_1", ":mother_of_2", slot_troop_mother),
	(assign, ":maternal_grandmother_of_1", reg0),
	(assign, ":maternal_grandmother_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_guardian),
	(assign, ":guardian_of_1", reg0),
	(assign, ":guardian_of_2", reg1),
	##diplomacy end+

	#(str_store_string, s11, "str_no_relation"),

	(try_begin),
	  (eq, ":troop_1", ":troop_2"),
	  #self
	(else_try),
	  ##diplomacy start+
      (this_or_next|eq, ":spouse_of_2", ":troop_1"),#polygamy helper
	  ##diplomacy end+
	  (eq, ":spouse_of_1", ":troop_2"),
	  (assign, ":relation_strength", 20),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_wife"),
	  (else_try),
	    (assign, ":relation_string", "str_husband"),
	  (try_end),
	(else_try),
	  (eq, ":father_of_2", ":troop_1"),
	  (assign, ":relation_strength", 15),
	  (assign, ":relation_string", "str_father"),
	(else_try),
	  (eq, ":mother_of_2", ":troop_1"),
	  (assign, ":relation_strength", 15),
	  (assign, ":relation_string", "str_mother"),
	(else_try),
	  (this_or_next|eq, ":father_of_1", ":troop_2"),
	  (eq, ":mother_of_1", ":troop_2"),
	  (assign, ":relation_strength", 15),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_daughter"),
	  (else_try),
	    (assign, ":relation_string", "str_son"),
	  (try_end),
	##diplomacy start+
	(else_try),
	   #Check for half-siblings: sharing a father
	   (neq, ":father_of_1", -1),
	   (eq, ":father_of_1", ":father_of_2"),
	   (neq, ":mother_of_1", ":mother_of_2"),
	   (assign, ":relation_strength", 10),
	   (try_begin),
	     (eq, ":gender_1", tf_female),
	     (assign, ":relation_string", "str_dplmc_half_sister"),
	   (else_try),
	     (assign, ":relation_string", "str_dplmc_half_brother"),
	   (try_end),
   (else_try),
	   #Check for half-siblings: sharing a mother
	   (neq, ":mother_of_1", -1),
	   (eq, ":mother_of_1", ":mother_of_2"),
	   (neq, ":father_of_1", ":father_of_2"),
	   (assign, ":relation_strength", 10),
	   (try_begin),
	     (eq, ":gender_1", tf_female),
	     (assign, ":relation_string", "str_dplmc_half_sister"),
	   (else_try),
	     (assign, ":relation_string", "str_dplmc_half_brother"),
	   (try_end),
	##diplomacy end+
	(else_try),
	  #(gt, ":father_of_1", -1), #necessary, as some lords do not have the father registered #dplmc+ replaced
	  (neq, ":father_of_1", -1), #dplmc+ added
	  (eq, ":father_of_1", ":father_of_2"),
	  (assign, ":relation_strength", 10),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_sister"),
	  (else_try),
	    (assign, ":relation_string", "str_brother"),
	  (try_end),
	(else_try),
	  (eq, ":guardian_of_2", ":troop_1"),
	  (assign, ":relation_strength", 10),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_sister"),
	  (else_try),
	    (assign, ":relation_string", "str_brother"),
	  (try_end),
	(else_try),
	  (eq, ":guardian_of_1", ":troop_2"),
	  (assign, ":relation_strength", 10),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_sister"),
	  (else_try),
	    (assign, ":relation_string", "str_brother"),
	  (try_end),
	##diplomacy start+
    (else_try),#polygamy, between two people married to the same person
	   (neq, ":spouse_of_1", -1),
	   (eq, ":spouse_of_2", ":spouse_of_1"),
	   (assign, ":relation_strength", 10),
	   (try_begin),
	      (call_script, "script_dplmc_store_troop_is_female", ":troop_2"),
		  (neq, ":gender_1", reg0),
		  (assign, ":relation_string", "str_dplmc_co_spouse"),
	   (else_try),
	      (eq, ":gender_1", tf_female),
	     (assign, ":relation_string", "str_dplmc_sister_wife"),
	   (else_try),
	      (assign, ":relation_string", "str_dplmc_co_husband"),
	   (try_end),
	##diplomacy end+
	(else_try),
	  #(gt, ":paternal_grandfather_of_1", -1),#dplmc+ replaced
	  (neq, ":father_of_2", -1),#dplmc+ added
	  (this_or_next|eq, ":maternal_grandfather_of_1", ":father_of_2"),#dplmc+ added
	  (eq, ":paternal_grandfather_of_1", ":father_of_2"),
	  (assign, ":relation_strength", 4),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_niece"),
	  (else_try),
	    (assign, ":relation_string", "str_nephew"),
	  (try_end),
	##diplomacy start+: add niece/nephew through mother
	(else_try),
	  (neq, ":mother_of_2", -1),
  	  (this_or_next|eq, ":maternal_grandmother_of_1", ":mother_of_2"),
	  (eq, ":paternal_grandmother_of_1", ":mother_of_2"),
	  (assign, ":relation_strength", 4),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_niece"),
	  (else_try),
	    (assign, ":relation_string", "str_nephew"),
	  (try_end),
	##diplomacy end+
	(else_try), #specifically aunt and uncle by blood -- i assume that in a medieval society with lots of internal family conflicts, they would not include aunts and uncles by marriage
	  #(gt, ":paternal_grandfather_of_2", -1),#dplmc+ replaced
	  (neq, ":father_of_1", -1),#dplmc+ added
	  (this_or_next|eq, ":maternal_grandfather_of_2", ":father_of_1"),#dplmc+ added
	  (eq, ":paternal_grandfather_of_2", ":father_of_1"),
	  (assign, ":relation_strength", 4),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_aunt"),
	  (else_try),
	    (assign, ":relation_string", "str_uncle"),
	  (try_end),
	##diplomacy start+
	#blood uncles & blood aunts, continued (via mother)
	(else_try),
	  (neq, ":mother_of_1", -1),
	  (this_or_next|eq, ":maternal_grandmother_of_2", ":mother_of_1"),
	  (eq, ":paternal_grandmother_of_2", ":mother_of_1"),
	  (assign, ":relation_strength", 4),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_aunt"),
	  (else_try),
	    (assign, ":relation_string", "str_uncle"),
	  (try_end),
	##diplomacy end+
	(else_try),
	  #(gt, ":paternal_grandfather_of_1", 0),#dplmc+ replaced (why was this one "gt 0" but the previous "gt -1"?)
	  (neq, ":paternal_grandfather_of_1", -1),#dplmc+ added
	  (this_or_next|eq, ":maternal_grandfather_of_2", ":paternal_grandfather_of_1"),#dplmc+ added
	  (eq, ":paternal_grandfather_of_2", ":paternal_grandfather_of_1"),
	  (assign, ":relation_strength", 2),
	  (assign, ":relation_string", "str_cousin"),
	##diplomacy start+
	#Add cousin via paternal grandmother or maternal grandparents
	(else_try),
	  (neq, ":maternal_grandfather_of_1", -1),
	  (this_or_next|eq, ":maternal_grandfather_of_2", ":maternal_grandfather_of_1"),
	  (eq, ":paternal_grandfather_of_2", ":maternal_grandfather_of_1"),
	  (assign, ":relation_strength", 2),
	  (assign, ":relation_string", "str_cousin"),
	(else_try),
	  (neq, ":paternal_grandmother_of_1", -1),
	  (this_or_next|eq, ":maternal_grandmother_of_2", ":paternal_grandmother_of_1"),
	  (eq, ":paternal_grandmother_of_2", ":paternal_grandmother_of_1"),
	  (assign, ":relation_strength", 2),
	  (assign, ":relation_string", "str_cousin"),
	(else_try),
	  (neq, ":maternal_grandmother_of_1", -1),
	  (this_or_next|eq, ":maternal_grandmother_of_2", ":maternal_grandmother_of_1"),
	  (eq, ":paternal_grandmother_of_2", ":maternal_grandmother_of_1"),
	  (assign, ":relation_strength", 2),
	  (assign, ":relation_string", "str_cousin"),
	##diplomacy end+
   	(else_try),
   	  (eq, ":father_of_spouse_of_1", ":troop_2"),
   	  (assign, ":relation_strength", 5),
   	  (try_begin),
   	    (eq, ":gender_1", tf_female),
   	    (assign, ":relation_string", "str_daughterinlaw"),
   	  (else_try),
   	    (assign, ":relation_string", "str_soninlaw"),
   	  (try_end),
	(else_try),
	  (eq, ":father_of_spouse_of_2", ":troop_1"),
	  (assign, ":relation_strength", 5),
	  (assign, ":relation_string", "str_fatherinlaw"),
	(else_try),
	  (eq, ":mother_of_spouse_of_2", ":troop_1"),
	  (neq, ":mother_of_spouse_of_2", "trp_player"), #May be necessary if mother for troops not set to -1
	  (assign, ":relation_strength", 5),
	  (assign, ":relation_string", "str_motherinlaw"),

	(else_try),
	  #(gt, ":father_of_spouse_of_1", -1), #necessary #dplmc+ replaced
	  (neq, ":father_of_spouse_of_1", -1), #dplmc+ added
	  (eq, ":father_of_spouse_of_1", ":father_of_2"),
	  (assign, ":relation_strength", 5),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_sisterinlaw"),
	  (else_try),
	    (assign, ":relation_string", "str_brotherinlaw"),
	  (try_end),
	(else_try),
	  #(gt, ":father_of_spouse_of_2", -1), #necessary #dplmc+ replaced
	  (neq, ":father_of_spouse_of_2", -1), #dplmc+ added
	  (eq, ":father_of_spouse_of_2", ":father_of_1"),
	  (assign, ":relation_strength", 5),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_sisterinlaw"),
	  (else_try),
	    (assign, ":relation_string", "str_brotherinlaw"),
	  (try_end),
	(else_try),
#	  (gt, ":spouse_of_2", -1), #necessary to avoid bug #dplmc+ replaced
	  (neq, ":spouse_of_2", -1), #dplmc+ added
	  (troop_slot_eq, ":spouse_of_2", slot_troop_guardian, ":troop_1"),
	  (assign, ":relation_strength", 5),
	  (try_begin),
	    #(eq, ":gender_1", tf_female),#dplmc+ replaced
	    (eq, ":gender_1", tf_female),#dplmc+ added
	    (assign, ":relation_string", "str_sisterinlaw"),
	  (else_try),
	    (assign, ":relation_string", "str_brotherinlaw"),
	  (try_end),
	(else_try),
	  #(gt, ":spouse_of_1", -1), #necessary to avoid bug #dplmc+ replaced
	  (neq, ":spouse_of_1", -1), #dplmc+ added
	  (troop_slot_eq, ":spouse_of_1", slot_troop_guardian, ":troop_2"),
	  (assign, ":relation_strength", 5),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_sisterinlaw"),
	  (else_try),
	    (assign, ":relation_string", "str_brotherinlaw"),
	  (try_end),
	(else_try),
	  #grandchild
	  (neq, ":troop_2", -1),
	   (this_or_next|eq, ":paternal_grandfather_of_1", ":troop_2"),
	   (this_or_next|eq, ":maternal_grandfather_of_1", ":troop_2"),
	   (this_or_next|eq, ":paternal_grandmother_of_1", ":troop_2"),
		   (eq, ":maternal_grandmother_of_1", ":troop_2"),
	   (assign, ":relation_strength", 4),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_dplmc_granddaughter"),
	  (else_try),
	    (assign, ":relation_string", "str_dplmc_grandson"),
	  (try_end),
	(else_try),
	   #grandparent
	   (neq, ":troop_1", -1),
	   (this_or_next|eq, ":paternal_grandfather_of_2", ":troop_1"),
	   (this_or_next|eq, ":maternal_grandfather_of_2", ":troop_1"),
	   (this_or_next|eq, ":paternal_grandmother_of_2", ":troop_1"),
		   (eq, ":maternal_grandmother_of_2", ":troop_1"),
	  (assign, ":relation_strength", 4),
	  (try_begin),
	    (eq, ":gender_1", tf_female),
	    (assign, ":relation_string", "str_dplmc_grandmother"),
	  (else_try),
	    (assign, ":relation_string", "str_dplmc_grandfather"),
	  (try_end),
	(try_end),
	##diplomacy start+
	##Add relations for rulers not already encoded
	(try_begin),
		(eq, ":relation_strength", 0),
		(neq, ":troop_1", ":troop_2"),
		(try_begin),
			#Lady Isolla of Suno's father King Esterich was King Harlaus's cousin,
			#making them first cousins once removed.  Assign a weight of "1"
			#to this (for reference, the lowest value normally given in Native is 2).
			(this_or_next|eq, ":troop_1", "trp_kingdom_1_lord"),
			    (eq, ":troop_1", "trp_kingdom_1_pretender"),
			(this_or_next|eq, ":troop_2", "trp_kingdom_1_lord"),
			    (eq, ":troop_2", "trp_kingdom_1_pretender"),
			(assign, ":relation_strength", 1),
			(assign, ":relation_string", "str_cousin"),
		(else_try),
			#Prince Valdym's uncle was Regent Burelek, father of King Yaroglek,
			#making the two of them first cousins.
			(this_or_next|eq, ":troop_1", "trp_kingdom_2_lord"),
			    (eq, ":troop_1", "trp_kingdom_2_pretender"),
			(this_or_next|eq, ":troop_2", "trp_kingdom_2_lord"),
				(eq, ":troop_2", "trp_kingdom_2_pretender"),
			(assign, ":relation_strength", 2),
			(assign, ":relation_string", "str_cousin"),
		(else_try),
			#Sanjar Khan and Dustum Khan were both sons of Janakir Khan
			#(although by different mothers) making them half-brothers.
			(this_or_next|eq, ":troop_1", "trp_kingdom_3_lord"),
			    (eq, ":troop_1", "trp_kingdom_3_pretender"),
			(this_or_next|eq, ":troop_2", "trp_kingdom_3_lord"),
				(eq, ":troop_2", "trp_kingdom_3_pretender"),
			(assign, ":relation_strength", 10),
			(assign, ":relation_string", "str_dplmc_half_brother"),
			#Adjust their parentage to make this work automatically
			(try_begin),
		      	(troop_slot_eq, ":troop_1", slot_troop_father, -1),
				(troop_slot_eq, ":troop_2", slot_troop_father, -1),
				#Set their "father" slot to a number guaranteed not to have spurious collisions
				(store_mul, ":janakir_khan", "trp_kingdom_3_lord", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),#defined in module_constants.py
				(val_add, ":janakir_khan", DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),#defined in module_constants.py
				(troop_set_slot, ":troop_1", slot_troop_father, ":janakir_khan"),
				(troop_set_slot, ":troop_2", slot_troop_father, ":janakir_khan"),
				#Differentiate their mothers, so they are half-brothers instead of full-brothers
				(try_begin),
					(troop_slot_eq, ":troop_1", slot_troop_mother, -1),
					(store_mul, reg0, ":troop_1", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
					(val_add, reg0, DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
					(troop_set_slot, ":troop_1", slot_troop_mother, reg0),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop_2", slot_troop_mother, -1),
					(store_mul, reg0, ":troop_2", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
					(val_add, reg0, DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
					(troop_set_slot, ":troop_2", slot_troop_mother, reg0),
				(try_end),
			(try_end),
		(try_end),
	(try_end),
	##Add uncles and aunts by marriage.
	##In Native, the relation strength for blood uncles/aunts is 4, and for cousins is 2.
	##In light of this I've decided to set the relation strength for aunts/uncles by marriage to 2.
	(try_begin),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_1 is married to a sibling of one of troop_2's parents, pt. 1
		(ge, ":spouse_of_1", 0),
		(neg|troop_slot_eq, ":spouse_of_1", slot_troop_father, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_1", slot_troop_father, ":paternal_grandfather_of_2"),
			(troop_slot_eq, ":spouse_of_1", slot_troop_father, ":maternal_grandfather_of_2"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_aunt"),
		(else_try),
			(assign, ":relation_string", "str_uncle"),
		(try_end),
	(else_try),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_1 is married to a sibling of one of troop_2's parents, pt. 2
		(ge, ":spouse_of_1", 0),
		(neg|troop_slot_eq, ":spouse_of_1", slot_troop_mother, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_1", slot_troop_mother, ":paternal_grandmother_of_2"),
			(troop_slot_eq, ":spouse_of_1", slot_troop_mother, ":maternal_grandmother_of_2"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_aunt"),
		(else_try),
			(assign, ":relation_string", "str_uncle"),
		(try_end),
	(else_try),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_2 is married to a sibling of one of troop_1's parents, pt. 1
		(ge, ":spouse_of_2", 0),
		(neg|troop_slot_eq, ":spouse_of_2", slot_troop_father, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_2", slot_troop_father, ":paternal_grandfather_of_1"),
			(troop_slot_eq, ":spouse_of_2", slot_troop_father, ":maternal_grandfather_of_1"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_niece"),
		(else_try),
			(assign, ":relation_string", "str_nephew"),
		(try_end),
	(else_try),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_2 is married to a sibling of one of troop_1's parents, pt. 2
		(ge, ":spouse_of_2", 0),
		(neg|troop_slot_eq, ":spouse_of_2", slot_troop_mother, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_2", slot_troop_mother, ":paternal_grandmother_of_1"),
			(troop_slot_eq, ":spouse_of_2", slot_troop_mother, ":maternal_grandmother_of_1"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_niece"),
		(else_try),
			(assign, ":relation_string", "str_nephew"),
		(try_end),
	(try_end),

	(try_begin),
		(this_or_next|neg|troop_is_hero, ":troop_1"),
		(neg|troop_is_hero, ":troop_2"),
		(assign, ":relation_string", "str_no_relation"),
		(assign, ":relation_strength", 0),
	(try_end),

	(assign, reg0, ":relation_strength"),
	(assign, reg1, ":relation_string"),
	]),

##"script_cf_dplmc_faction_has_bias_against_gender"
("cf_dplmc_faction_has_bias_against_gender", [
	(store_script_param_1, ":faction_no"),
	(store_script_param_2, ":test_gender"),#Special: 1 is female

    (assign, reg0, 0),
	(lt, "$g_disable_condescending_comments", 2),#If bias is disabled, do not continue
	(is_between, ":test_gender", 0, 2),#valid genders are 0 and 1

	(try_begin),
		(eq, ":faction_no", "fac_player_supporters_faction"),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(assign, ":faction_no", "$players_kingdom"),
	(try_end),

	(try_begin),
		#For a-typical factions, nothing by default.
		(neg|is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
	(else_try),
		#If the leader has that gender, no prejudice.
		(faction_get_slot, ":active_npc", ":faction_no", slot_faction_leader),
		(gt, ":active_npc", -1),
		(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
		(eq, reg0, ":test_gender"),
		(assign, reg0, 0),
	(else_try),
		#Traditional gender prejudice if both are true:
		#1.  The faction has no original members of the specified gender.
		#2.  The faction has original members with non-accepting lord personalities.

		(assign, ":num_closeminded", 0),
		(assign, ":end_cond", active_npcs_end),

		(try_for_range, ":active_npc", active_npcs_begin, ":end_cond"),#Deliberately do not include kingdom ladies
			#Also deliberately exclude companions and pretenders
			#(Pretenders are marginalized at the start of the game, and
			#companions don't necessarily start in positions of power either)
			(this_or_next|is_between, ":active_npc", kings_begin, kings_end),
				(is_between, ":active_npc", lords_begin, lords_end),
			(troop_slot_eq, ":active_npc", slot_troop_original_faction, ":faction_no"),

			(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
			(try_begin),
				(eq, reg0, ":test_gender"),
				(assign, ":num_closeminded", -1000),
				(assign, ":end_cond", ":active_npc"),
			(else_try),
				(troop_get_slot, reg0, ":active_npc", slot_lord_reputation_type),
				(is_between, reg0, lrep_none + 1, lrep_roguish),#Lord (non-commoner, non-liege, non-lady) personality type
				(neq, reg0, lrep_cunning),
				(neq, reg0, lrep_goodnatured),
				(val_add, ":num_closeminded", 1),
			(try_end),
		(try_end),

		(store_sub, reg0, ":num_closeminded", 1),#Needs at least one
		(val_clamp, reg0, 0, 2),
	(try_end),

	(try_begin),
		(eq, "$cheat_mode", 4), #SB : political debugmode
		(assign, ":end_cond", reg1),#just save reg1 and reg2 (ignore the normal meaning of the variable names)
		(assign, ":active_npc", reg2),
		(assign, reg1, ":faction_no"),
		(assign, reg2, ":test_gender"),
		(display_message, "@{!} Checked if faction {reg1} is prejudiced against {reg2?women:men}: {reg0?true:false}"),
		(assign, reg1, ":end_cond"),#revert reg1 and reg2 (ignore the normal meaning of the variable names)
		(assign, reg2, ":active_npc"),
	(try_end),
	(gt, reg0, 0),
]),

#"script_dplmc_store_troop_personality_caution_level"
#
# INPUT:
#   arg1 :troop_no
# OUTPUT:
#   reg0 -1 for aggressive
#         0 for neither
#         1 for cautious
("dplmc_store_troop_personality_caution_level", [
	#Used a number of places to determine whether a lord is cautious
	#or aggressive.  The standard is something like:
	#
	#For cautious:
	#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
    #    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
    #    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
    #    (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
	#
	#For aggressive:
	#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
    #    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
    #    (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
	#
	#I've expanded this for companion/lady personalities.
	#The result can be either:
	# -1  =  aggressive
	#  0  =  neutral
	#  1  =  cautious
	(store_script_param_1, ":troop_no"),

	(try_begin),
		(neg|is_between, ":troop_no", heroes_begin, heroes_end),#The player or troops that don't have slot_lord_reputation_type
		(assign, reg0, 0),#neither cautious nor aggressive
	(else_try),
		(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_aristocratic),
		(lt, reg0, 0),#compliments when the player retreats
		(assign, reg0, 1),#cautious
	(else_try),
		(gt, reg0, 0),#complains when the player retreats
		(assign, reg0, -1),#aggressive
	(else_try),
		(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
		(this_or_next|eq, ":reputation", lrep_adventurous),
		(this_or_next|eq, ":reputation", lrep_martial),
		(this_or_next|eq, ":reputation", lrep_quarrelsome),
			(eq, ":reputation", lrep_selfrighteous),
		(assign, reg0, -1),#aggressive
	(else_try),
		(this_or_next|ge, ":reputation", lrep_conventional),
		(this_or_next|eq, ":reputation", lrep_upstanding),
		(this_or_next|eq, ":reputation", lrep_debauched),
		(this_or_next|eq, ":reputation", lrep_goodnatured),
			(eq, ":reputation", lrep_cunning),
		(assign, reg0, 1),#cautious
	(else_try),
		(assign, reg0, 0),#neither cautious nor aggressive
	(try_end),
]),

##"script_dplmc_cap_troop_describes_troop_to_troop_s1"
#
# e.g.
#
#(call_script, "script_dplmc_cap_troop_describes_troop_to_troop_s1", 1, "trp_player", ":third_lord", "$g_talk_troop"),
#
#INPUT:
#        arg1  :capitalization (0 if middle of sentence, 1 if sentence start)
#        arg2  :speaker (the one doing the talking)
#        arg3  :described (the one being named)
#        arg4  :listener (the one being spoken to)
#
#OUTPUT:
#        Writes result to s1, clobbers s0
#
#Similar to "script_troop_describes_troop_to_s15", except
#it takes into account the perspective of the one being
#spoken to, and writes to s1
  ("dplmc_cap_troop_describes_troop_to_troop_s1",
  [
	(store_script_param, ":capitalization", 1),
	(store_script_param, ":speaker", 2),
	(store_script_param, ":described", 3),
	(store_script_param, ":listener", 4),

	(assign, ":save_reg0", reg0),
	(assign, ":save_reg1", reg1),

	(str_store_troop_name, s0, ":described"),

	(assign, reg0, ":capitalization"),
	(try_begin),
		(eq, ":described", ":listener"),
		(neq, ":speaker", ":listener"),
		(str_store_string, s0, "@{reg0?Y:y}ou"),
		(assign, reg0, 1),
	(else_try),
		(eq, ":described", ":speaker"),
		(str_store_string, s0, "@{reg0?M:m}yself"),
		(assign, reg0, 1),
	(else_try),
		(this_or_next|eq, ":described", "trp_player"),#only calculate family relationships for the player and heroes
			(is_between, ":described", heroes_begin, heroes_end),
		(assign, ":speaker_relation", 0),
		(assign, ":speaker_relation_string", 0),
		(try_begin),
			(this_or_next|eq, ":speaker", "trp_player"),#only calculate family relationships for the player and heroes
				(is_between, ":speaker", heroes_begin, heroes_end),
			(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":described", ":speaker"),
			(assign, ":speaker_relation", reg0),
			(assign, ":speaker_relation_string", reg1),
		(try_end),
		(assign, reg0, 0),
		(try_begin),
			(this_or_next|eq, ":described", "trp_player"),#only calculate family relationships for the player and heroes
				(is_between, ":described", heroes_begin, heroes_end),
			(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":described", ":listener"),
		(try_end),
		(this_or_next|ge, ":speaker_relation", 1),
			(ge, reg0, 1),
		(try_begin),
			(eq, ":speaker_relation", reg0),
			(eq, reg1, ":speaker_relation_string"),
			(neq, ":speaker", ":listener"),
			(assign, reg0, ":capitalization"),
			(str_store_string, s1, ":speaker_relation_string"),
			(str_store_string, s1, "@{reg0?O:o}ur {s1} {s0}"),
		(else_try),
			(ge, ":speaker_relation", reg0),
			(assign, reg0, ":capitalization"),
			(str_store_string, s1, ":speaker_relation_string"),
			(str_store_string, s1, "@{reg0?M:m}y {s1} {s0}"),
		(else_try),
			(assign, reg0, ":capitalization"),
			(str_store_string, s1, reg1),
			(str_store_string, s1, "@{reg0?Y:y}our {s1} {s0}"),
		(try_end),
	###Disable "marshall/liege", because that's done elsewhere anyway
	#(else_try),
	#	(store_faction_of_troop, ":speaker_faction", ":speaker"),
	#	(try_begin),
	#		(eq, ":speaker", "trp_player"),
	#		(assign, ":speaker_faction", "$players_kingdom"),
	#	(try_end),
	#
	#	(store_faction_of_troop, ":listener_faction", ":listener"),
	#	(try_begin),
	#		(eq, ":listener", "trp_player"),
	#		(assign, ":listener_faction", "$players_kingdom"),
	#	(try_end),
	#
	#	(faction_slot_eq, ":speaker_faction", slot_faction_leader, ":described"),
	#	(this_or_next|is_between, ":speaker_faction", npc_kingdoms_begin, npc_kingdoms_end),
	#		(faction_slot_eq, ":speaker_faction", slot_faction_state, sfs_active),
	#	(this_or_next|neq, ":described", "trp_player"),
	#		(eq, ":speaker_faction", "$players_kingdom"),
	#	(assign, reg0, ":capitalization"),
	#	(try_begin),
	#		(eq, ":speaker_faction", ":listener_faction"),
	#		(neq, ":speaker", ":listener"),
	#		(str_store_string, s1, "@{reg0?O:o}ur liege {s0}"),
	#	(else_try),
	#		(str_store_string, s1, "@{reg0?M:m}y liege {s0}"),
	#	(try_end),
	#(else_try),
	#	(faction_slot_eq, ":speaker_faction", slot_faction_marshall, ":described"),
	#	(this_or_next|is_between, ":speaker_faction", npc_kingdoms_begin, npc_kingdoms_end),
	#		(faction_slot_eq, ":speaker_faction", slot_faction_state, sfs_active),
	#	(this_or_next|neq, ":described", "trp_player"),
	#		(eq, ":speaker_faction", "$players_kingdom"),
	#	(try_begin),
	#		(eq, ":speaker_faction", ":listener_faction"),
	#		(neq, ":speaker", ":listener"),
	#		(str_store_string, s1, "@{reg0?O:o}ur marshall {s0}"),
	#	(else_try),
	#		(str_store_string, s1, "@{reg0?M:m}y marshall {s0}"),
	#	(try_end),
	#(else_try),
	#	(this_or_next|is_between, ":listener_faction", npc_kingdoms_begin, npc_kingdoms_end),
	#		(faction_slot_eq, ":listener_faction", slot_faction_state, sfs_active),
	#	(faction_slot_eq, ":listener_faction", slot_faction_leader, ":described"),
	#	(this_or_next|neq, ":described", "trp_player"),
	#		(eq, ":listener_faction", "$players_kingdom"),
	#	(assign, reg0, ":capitalization"),
	#	(str_store_string, s1, "@{reg0?Y:y}our liege {s0}"),

	###Disable "friend", because it gets really spammy.  (It looks really stupid to have
	###a list of fifty names, all of them starting with "Your Friend So-and-So".)
	#(else_try),
	#	(call_script, "script_troop_get_relation_with_troop", ":described", ":listener"),
	#	(ge, reg0, 20),
	#	(this_or_next|neq, ":listener", "trp_player"),
	#		(ge, reg0, 50),
	#	(call_script, "script_troop_get_relation_with_troop", ":described", ":speaker"),
	#	(this_or_next|neq, ":listener", "trp_player"),
	#		(neq, ":speaker_trp_player"),
	#	(try_begin),
	#		(ge, reg0, 20),
	#		(this_or_next|neq, ":speaker", "trp_player"),
	#			(ge, reg0, 50),
	#		(assign, reg0, ":capitalization"),
	#		(str_store_string, s1, "@{reg0?O:o}ur friend {s0}"),
	#	(else_try),
	#		(assign, reg0, ":capitalization"),
	#		(str_store_string, s1, "@{reg0?Y:y}our friend {s0}"),
	#	(try_end),
	#(else_try),
	#	(call_script, "script_troop_get_relation_with_troop", ":described", ":speaker"),
	#	(ge, reg0, 20),
	#	(this_or_next|neq, ":speaker", "trp_player"),
	#		(ge, reg0, 50),
	#	(assign, reg0, ":capitalization"),
	#	(str_store_string, s1, "@{reg0?M:m}y friend {s0}"),

	###The "<Jarl Aedin> of <Tihr>" condition works fine, but I'm not particularly impressed.
	###I'm not sure it's an improvement over just using their name, so I'm disabling it for now.
	#(else_try),
	#	#Did not use relation string: name by owned town.
	#	#Do not use names of castles, due to potential absurdities like "Count Harringoth of Harringoth Castle".
	#	#Skip kings and pretenders because of "Lady Isolla of Suno of Suno" and similar things.
	#	(neg|is_between, ":described", kings_begin, kings_end),
	#	(neg|is_between, ":described", pretenders_begin, pretenders_end),
	#	(this_or_next|eq, ":described", "trp_player"),
	#		(is_between, ":described", heroes_begin, heroes_end),
	#
	#	(assign, ":owned_town", -1),
	#	(assign, ":owned_town_score", -1),
	#	(troop_get_slot, ":original_faction", ":described", slot_troop_original_faction),
	#	(try_for_range, ":town_no", towns_begin, towns_end),
	#		(party_get_slot, ":town_lord", ":town_no", slot_town_lord),
	#		(ge, ":town_lord", 0),
	#		(assign, reg0, 0),
	#		(try_begin),
	#			(eq, ":town_lord", ":described"),
	#			(assign, reg0, 10),
	#		(else_try),
	#			(this_or_next|troop_slot_eq, ":town_lord", slot_troop_spouse, ":described"),
	#				(troop_slot_eq, ":described", slot_troop_spouse, ":town_lord"),
	#			(this_or_next|is_between, ":described", kingdom_ladies_begin, kingdom_ladies_end),
	#				(troop_slot_eq, ":described", slot_troop_occupation, slto_kingdom_lady),
	#			(assign, reg0, 1),
	#		(else_try),
	#			(assign, reg0, 0),
	#		(try_end),
	#		(gt, reg0, 0),
	#		(try_begin),
	#			(party_slot_eq, ":town_no", slot_center_original_faction, ":original_faction"),
	#			(val_add, reg0, 1),
	#		(try_end),
	#		(try_begin),
	#			(this_or_next|party_slot_eq, ":town_no", dplmc_slot_center_original_lord, ":described"),
	#				(party_slot_eq, ":town_no", dplmc_slot_center_original_lord, ":town_lord"),
	#			(val_add, reg0, 2),
	#		(try_end),
	#		(try_begin),
	#			(this_or_next|troop_slot_eq, ":town_lord", slot_troop_home, ":town_no"),
	#				(troop_slot_eq, ":town_lord", slot_troop_home, ":town_no"),
	#			(val_add, reg0, 2),
	#		(try_end),
	#		(gt, reg0, ":owned_town_score"),
	#		(assign, ":owned_town_score", reg0),
	#		(assign, ":owned_town", ":town_no"),
	#	(try_end),
	#	(is_between, ":owned_town", towns_begin, towns_end),
	#	(str_store_party_name, s1, ":owned_town"),
	#	(str_store_string, s1, "@{s0} of {s1}"),
	(else_try),
		(str_store_string, s1, "str_s0"),
	(try_end),

	(assign, reg0, ":save_reg0"),
	(assign, reg1, ":save_reg1"),
	(str_store_string_reg, s0, s1),
	]),

##"script_dplmc_helper_get_troop1_troop2_family_slot_aux"
##
## Helper function that does something specific that I want in
## script_dplmc_troop_get_family_relation_to_troop.
##
## Gets the slot value, but for troops that aren't trp_player
## and are not within (heroes_begin, heroes_end), values of "0"
## are transformed to -1.  Also gives a result of -1 (instead of
## an error) for negative troop IDs, which is what I want in
## this situation (otherwise I'd be explicitly checking this and
## setting the result to -1 if it was bad).
##
## Also, values equal to "active_npcs_including_player_begin" are
## transformed to "trp_player" (i.e. 0), to allow storing that
## value.
##
##INPUT:  arg1   :troop_1
##        arg2   :troop_2
##        arg3   :slot_no
##
##OUTPUT: reg0   value of slot for troop_1, or -1
##        reg1   value of slot for troop_2, or -1
("dplmc_helper_get_troop1_troop2_family_slot_aux",
	[
		(store_script_param, ":troop_1", 1),
		(store_script_param, ":troop_2", 2),
		(store_script_param, ":slot_no", 3),

		#(1) Get the value for the first troop into reg0
		(try_begin),
			#Negative numbers are placeholders for invalid family members
			(lt, ":troop_1", 0),
			(assign, reg0, -1),
		(else_try),
			#For active_npcs_including_player_begin, use the family slot from trp_player
			(eq, ":troop_1", active_npcs_including_player_begin),
			(troop_get_slot, reg0, "trp_player", ":slot_no"),
		(else_try),
			#Otherwise get the family member slot
			(troop_get_slot, reg0, ":troop_1", ":slot_no"),
			#However, for non-heroes, the memory might not be initialized,
			#so don't take a value of 0 at face-value.
			(eq, reg0, 0),
			(neg|is_between, ":troop_1", heroes_begin, heroes_end),
			(neq, ":troop_1", "trp_player"),
			(assign, reg0, -1),
		(try_end),

		#Translate from active_npcs_including_player_begin to trp_player
		(try_begin),
			(eq, reg0, active_npcs_including_player_begin),
			(assign, reg0, "trp_player"),
		(try_end),

		#(2) Get the value for the second troop into reg1
		(try_begin),
			#Negative numbers are placeholders for invalid family members
			(lt, ":troop_2", 0),
			(assign, reg1, -1),
		(else_try),
			#For active_npcs_including_player_begin, use the family slot from trp_player
			(eq, ":troop_2", active_npcs_including_player_begin),
			(troop_get_slot, reg1, "trp_player", ":slot_no"),
		(else_try),
			#Otherwise get the family member slot
			(troop_get_slot, reg1, ":troop_2", ":slot_no"),
			#However, for non-heroes, the memory might not be initialized,
			#so don't take a value of 0 at face-value.
			(eq, reg1, 0),
			(neg|is_between, ":troop_2", heroes_begin, heroes_end),
			(neq, ":troop_2", "trp_player"),
			(assign, reg1, -1),
		(try_end),

		#Translate from active_npcs_including_player_begin to trp_player
		(try_begin),
			(eq, reg1, active_npcs_including_player_begin),
			(assign, reg1, "trp_player"),
		(try_end),
	]),

	##"script_dplmc_estimate_center_weekly_income"
	#
	#  INPUT:  arg1   :center_no
	# OUTPUT:  reg0   estimated value of weekly income
	#
	#TODO: Add a better explanation for why this function does not include tarrifs.
	("dplmc_estimate_center_weekly_income", [
		(store_script_param_1, ":center_no"),
		(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
		(try_begin),
		  #If there is some sort of aberration, assign to 50 instead of
		  #clamping, on the assumption that the value bears no relation
		  #to the true prosperity at all.
		  (neg|is_between, ":prosperity", 0, 101),
		  (assign, ":prosperity", 50),
		(try_end),
		(store_add, reg0, 20, ":prosperity"),
		(val_mul, reg0, 1200),
		(val_div, reg0, 120),
		(try_begin),
		  (party_slot_eq, ":center_no", slot_party_type, spt_town),
		  #Towns have higher base rent than castles and villages
		  (val_mul, reg0, 2),
		  #Include town garrison allowance
		  (val_mul, ":prosperity", 15),
		  (val_add, ":prosperity", 700),
		  (val_mul, ":prosperity", 3),
		  (val_div, ":prosperity", 2),
		  (val_add, reg0, ":prosperity"),
		(else_try),
		  (party_slot_eq, ":center_no", slot_party_type, spt_castle),
		  #Include castle garrison allowance
		  (val_mul, ":prosperity", 15),
		  (val_add, ":prosperity", 700),
		  (val_add, reg0, ":prosperity"),
		(try_end),
		#At this point, the final result is in reg0.
	]),

  # "script_dplmc_get_closest_center_or_two"
  # Input: arg1 = party_no
  # Output: reg0 = center_no (closest)
  #         reg1 = center_no2 (another close center or -1)
  #
  # If reg1 is non-negative, it should make some sense to say "<party_no> is
  # between <reg0> and <reg1>".
  #
  # The way I do this is:
  #   1.  Find the closest center to the party.
  #   2.  Excluding the center from (1), find the closest center to the
  #       party which is not closer to the center from (1) than it is to
  #       the party.  (There might not be any centers matching this
  #       description.)
  #
  # If the party is much closer to center_1 than center_2, I discard
  # the second center.  (The rationale is that if I'm standing on my
  # doorstep, it is be helpful to say "I am between my house and the
  # grocery store".  It is less misleading to just say "I am near my
  # house.")
  ("dplmc_get_closest_center_or_two",
    [
      (store_script_param_1, ":party_no"),
      (call_script, "script_get_closest_center", ":party_no"),#writes closest center to reg0
      (store_distance_to_party_from_party, ":distance_to_beat", ":party_no", reg0),
      (val_mul, ":distance_to_beat", 2),
      (val_add, ":distance_to_beat", 1),

      (assign, reg1, -1),
      (try_for_range, ":center_no", centers_begin, centers_end),
        (neq, ":center_no", reg0),
        (store_distance_to_party_from_party, ":party_to_center_distance", ":party_no", ":center_no"),
        (lt, ":party_to_center_distance", ":distance_to_beat"),
        (store_distance_to_party_from_party, ":center_to_center_distance", reg0, ":center_no"),
        (gt, ":center_to_center_distance", ":party_to_center_distance"),
        (assign, ":distance_to_beat", ":party_to_center_distance"),
        (assign, reg1, ":center_no"),
      (try_end),
  ]),


# Jrider +
   ###################################################################################
   # REPORT PRESENTATIONS v1.2 scripts
   # Script overlay_container_add_listbox_item
   # use ...
   # return ...
   ("overlay_container_add_listbox_item", [
        (store_script_param, ":line_y", 1),
        (store_script_param, ":npc_id", 2),

        (set_container_overlay, "$g_jrider_character_relation_listbox"),

        # create text overlay for entry
        (create_text_overlay, reg10, s1, tf_left_align),
        (overlay_set_color, reg10, 0xDDDDDD),
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 750),
        (overlay_set_size, reg10, pos1),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, ":line_y"),
        (overlay_set_position, reg10, pos1),

        # create button
        (create_image_button_overlay, reg10, "mesh_white_plane", "mesh_white_plane"),
        (position_set_x, pos1, 0), # 590 real, 0 scrollarea
        (position_set_y, pos1, ":line_y"),
        (overlay_set_position, reg10, pos1),
        (position_set_x, pos1, 16000),
        (position_set_y, pos1, 750),
        (overlay_set_size, reg10, pos1),
        (overlay_set_alpha, reg10, 0),
        (overlay_set_color, reg10, 0xDDDDDD),

        # store relation of button id to character number for use in triggers
        (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", reg10),
        (troop_set_slot, "trp_temp_array_b", ":current_storage_index", "$num_charinfo_candidates"),

        # reset variables if appropriate flags are up
        (try_begin),
            (try_begin),
                (this_or_next|eq, "$g_jrider_pres_called_from_menu", 1),
                (ge, "$g_jrider_reset_selected_on_faction", 1),

                (assign, "$character_info_id", ":npc_id"),
                (assign, "$g_jrider_last_checked_indicator", reg10),
                (assign, "$g_latest_character_relation_entry", "$num_charinfo_candidates"),
            (try_end),
        (try_end),

        # close the container
        (set_container_overlay, -1),
   ]),

   # script get_relation_candidate_list_for_presentation
   # return a list of candidate according to type of list and restrict options
   # Use ...
   ("fill_relation_canditate_list_for_presentation",
    [
        (store_script_param, ":pres_type", 1),
        (store_script_param, ":base_candidates_y", 2),

        # Type of list from global variable: 0 courtship, 1 known lords
        (try_begin),
        ## For courtship:
            (eq, ":pres_type", 0),

            (try_for_range_backwards, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
                (troop_slot_ge, ":lady", slot_troop_met, 1), # met or better
                (troop_slot_eq, ":lady", slot_troop_spouse, -1), # unmarried

                # use faction filter
                (store_troop_faction, ":lady_faction", ":lady"),
                (val_sub, ":lady_faction", kingdoms_begin),
                (this_or_next|eq, "$g_jrider_faction_filter", -1),
                (eq, "$g_jrider_faction_filter", ":lady_faction"),

                (call_script, "script_troop_get_relation_with_troop", "trp_player", ":lady"),
                (gt, reg0, 0),
                (assign, reg3, reg0),

                (str_store_troop_name, s2, ":lady"),

                (store_current_hours, ":hours_since_last_visit"),
                (troop_get_slot, ":last_visit_hour", ":lady", slot_troop_last_talk_time),
                (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
                (store_div, ":days_since_last_visit", ":hours_since_last_visit", 24),
                (assign, reg4, ":days_since_last_visit"),

                #(str_store_string, s1, "str_s1_s2_relation_reg3_last_visit_reg4_days_ago"),
                (str_store_string, s1, "@{s2}: {reg3}, {reg4} days"),

                # create custom listbox entry, set the container first
                (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

                (call_script, "script_overlay_container_add_listbox_item", ":line_y", ":lady"),

                # candidate found, store troop id for later use
                (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                (troop_set_slot, "trp_temp_array_c", ":current_storage_index", ":lady"),

                # update entry counter
                (val_add, "$num_charinfo_candidates", 1),
            (try_end),
        ## End courtship relations
        (else_try),
        ## For lord relations
            (eq, ":pres_type", 1),

            # Loop to identify
            (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                (troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
            (try_end),

            (try_for_range, ":unused", active_npcs_begin, active_npcs_end),

                (assign, ":score_to_beat", 101),
                (assign, ":best_relation_remaining_npc", -1),

                (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                        (troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
                        (troop_slot_ge, ":active_npc", slot_troop_met, 1),
                        (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),

                        (call_script, "script_troop_get_player_relation", ":active_npc"),
                        (assign, ":relation_with_player", reg0),
                        (le, ":relation_with_player", ":score_to_beat"),

                        (assign, ":score_to_beat", ":relation_with_player"),
                        (assign, ":best_relation_remaining_npc", ":active_npc"),
                (try_end),
                (gt, ":best_relation_remaining_npc", -1),

                (str_store_troop_name, s4, ":best_relation_remaining_npc"),
                (assign, reg4, ":score_to_beat"),

                (str_store_string, s1, "@{s4}: {reg4}"),
                (troop_set_slot, ":best_relation_remaining_npc", slot_troop_temp_slot, 1),

                # use faction filter
                (store_troop_faction, ":npc_faction", ":best_relation_remaining_npc"),
                (val_sub, ":npc_faction", kingdoms_begin),
                (this_or_next|eq, "$g_jrider_faction_filter", -1),
                (eq, "$g_jrider_faction_filter", ":npc_faction"),

                # candidate found,
                # create custom listbox entry, set the container first
                (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

                (call_script, "script_overlay_container_add_listbox_item", ":line_y", ":best_relation_remaining_npc"),

                #store troop id for later use (could be merged with the object id)
                (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                (troop_set_slot, "trp_temp_array_c", ":current_storage_index", ":best_relation_remaining_npc"),

                # update entry counter
                (val_add, "$num_charinfo_candidates", 1),
            (try_end),
        ## END Lords relations
        (else_try),
        ## Character and Companions
            (eq, ":pres_type", 2),

            # companions
            (try_for_range_backwards, ":companion", companions_begin, companions_end),
                (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

                (str_store_troop_name, s1, ":companion"),

        (try_begin),
                    (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
                    (str_store_string, s1, "@{s1}(gathering support)"),
                (else_try),
                    (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
                    (str_store_string, s1, "@{s1} (intelligence)" ),
                (else_try),
                    (troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
                    (neg|troop_slot_eq, ":companion", slot_troop_current_mission, 8),
                    (str_store_string, s1, "@{s1} (ambassy)"),
                (else_try),
                        (eq, ":companion", "$g_player_minister"),
                    (str_store_string, s1, "@{s1} (minister"),
                (else_try),
                    (main_party_has_troop, ":companion"),
                    (str_store_string, s1, "@{s1} (under arms)"),
                (else_try),
                    (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                    (str_store_string, s1, "@{s1} (attempting to rejoin)"),
                (else_try),
                    (troop_slot_ge, ":companion", slot_troop_cur_center, 1),
                    (str_store_string, s1, "@{s1} (separated after battle)"),
                (try_end),
                # candidate found,
                # create custom listbox entry, set the container first
                (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

                (call_script, "script_overlay_container_add_listbox_item", ":line_y", ":companion"),

                #store troop id for later use (could be merged with the object id)
                (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                (troop_set_slot, "trp_temp_array_c", ":current_storage_index", ":companion"),

                # update entry counter
                (val_add, "$num_charinfo_candidates", 1),
            (try_end),
            # END companions

            # Wife/Betrothed
            # END Wife/Betrothed

            (try_begin),
            # Character
                (str_store_troop_name, s1, "trp_player"),

                # candidate found,
                # create custom listbox entry, set the container first
                (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                (store_add, ":line_y", ":base_candidates_y", ":y_mult"),

                (call_script, "script_overlay_container_add_listbox_item", ":line_y", "trp_player"),

                #store troop id for later use (could be merged with the object id)
                (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                (troop_set_slot, "trp_temp_array_c", ":current_storage_index", "trp_player"),

                # update entry counter
                (val_add, "$num_charinfo_candidates", 1),
            (try_end),
            # End Character

        (try_end),
        ## END Character and Companions
    ]),

    # script get_troop_relation_to_player_string
    # return relation to player string in the specified parameters
    #
    ("get_troop_relation_to_player_string",
     [
         (store_script_param, ":target_string", 1),
         (store_script_param, ":troop_no", 2),

         (call_script, "script_troop_get_player_relation", ":troop_no"),
         (assign, ":relation", reg0),
         (str_clear, s61),

         (store_add, ":normalized_relation", ":relation", 100),
         (val_add, ":normalized_relation", 5),
         (store_div, ":str_offset", ":normalized_relation", 10),
         (val_clamp, ":str_offset", 0, 20),
         (store_add, ":str_rel_id", "str_relation_mnus_100_ns",  ":str_offset"),

         ## Make something if troop has relation but not strong enought to warrant a string
         (try_begin),
           (neq, ":str_rel_id", "str_relation_plus_0_ns"),
           (str_store_string, s61, ":str_rel_id"),
         (else_try),
           (neg|eq, reg0, 0),
           (str_is_empty, s61),
           (str_store_string, s61, "@ knows of you."),
         (else_try),
           (eq, reg0, 0),
           (str_is_empty, s61),
           (str_store_string, s61, "@ has no opinion about you."),
         (try_end),

         ## copy result string to target string
         (str_store_string_reg, ":target_string", s61),
     ]),

    # script get_troop_holdings
    # returns number of fief and list name (reg50, s50)
    ("get_troop_holdings",
     [
         (store_script_param, ":troop_no", 1),

         (assign, ":owned_centers", 0),
         (assign, ":num_centers", 0),
         (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
             (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
             (try_begin),
               (eq, ":num_centers", 0),
               (str_store_party_name, s50, ":cur_center"),
               (val_add, ":owned_centers", 1),
             (else_try),
               (eq, ":num_centers", 1),
               (str_store_party_name, s57, ":cur_center"),
               (str_store_string, s50, "@{s57} and {s50}"),
               (val_add, ":owned_centers", 1),
             (else_try),
               (str_store_party_name, s57, ":cur_center"),
               (str_store_string, s50, "@{!}{s57}, {s50}"),
               (val_add, ":owned_centers", 1),
             (try_end),
             (val_add, ":num_centers", 1),
         (try_end),
         (assign, reg50, ":owned_centers"),
     ]),

    # script generate_extended_troop_relation_information_string
    # return information about troop according to type (lord, lady, maiden)
    # Use (hm lots of registers and strings)
    # result stored in s1
    ("generate_extended_troop_relation_information_string",
     [
         (store_script_param, ":troop_no", 1),

         # clear the strings and registers we'll use to prevent external interference
         (str_clear, s1),
         (str_clear, s2),
         (str_clear, s60),
         (str_clear, s42),
         (str_clear, s43),
         (str_clear, s44),
         (str_clear, s45),
         (str_clear, s46),
         (str_clear, s47),
         (str_clear, s48),
         (str_clear, s49),
         (str_clear, s50),
         (assign, reg40,0),
         (assign, reg41,0),
         (assign, reg43,0),
         (assign, reg44,0),
         (assign, reg46,0),
         (assign, reg47,0),
         (assign, reg48,0),
         (assign, reg49,0),
         (assign, reg50,0),
         (assign, reg51,0),

         (try_begin),
             (eq, ":troop_no", "trp_player"),
             (overlay_set_display, "$g_jrider_character_faction_filter", 0),

             # Troop name
             (str_store_troop_name, s1, ":troop_no"),

             # Get renown - slot_troop_renown
             (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
             (assign, reg40, ":renown"),

             # Controversy - slot_troop_controversy
             (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
             (assign, reg41, ":controversy"),

             # Honor - $player_honor
             (assign, reg42, "$player_honor"),

             # Right to rule - $player_right_to_rule
             (assign, reg43, "$player_right_to_rule"),

             # Current faction
             (store_add, reg45, "$players_kingdom"),
             (try_begin),
                 (is_between, "$players_kingdom", "fac_player_supporters_faction", npc_kingdoms_end),
                 (str_store_faction_name, s45, "$players_kingdom"),
             (else_try),
                 (assign, reg45, 0),
                 (str_store_string, s45, "@Calradia."),
             (try_end),

             # status
             (assign, ":origin_faction", "$players_kingdom"),
             #SB : gender strings
             (try_begin),
                 (is_between, ":origin_faction", npc_kingdoms_begin, npc_kingdoms_end),
                 (str_store_string, s44, "@sworn {man/woman}"),
             (else_try),
                 (eq, ":origin_faction", "fac_player_supporters_faction"),
                 (str_store_string, s44, "@ruler"),
             (else_try),
                 (str_store_string, s44, "@free {man/woman}"),
             (try_end),

             # Current liege and relation
             (faction_get_slot, ":liege", "$players_kingdom", slot_faction_leader),
             (str_store_troop_name, s46, ":liege"),
             (try_begin),
                 (eq, ":liege", ":troop_no"),
                 (assign, reg46, 0),
             (else_try),
                 (assign, reg46, ":liege"),
                 (str_clear, s47),
                 (str_clear, s60),

                 # Relation to liege
                 (call_script, "script_get_troop_relation_to_player_string", s47, ":liege"),
             (end_try),

             # Holdings
             (call_script, "script_get_troop_holdings", ":troop_no"),

             #### Final Storage
             (str_store_string, s1, "@{s1} Renown: {reg40}, Controversy: {reg41}^Honor: {reg42}, Right to rule: {reg43}^\
You are a {s44} of {s45}^{reg45?{reg46?Your liege, {s46},{s47}:You are the ruler of {s45}}:}^^Friends: ^Enemies: ^^Fiefs:^  {reg50?{s50}:no fief}"),
         #######################
         # END Player information
         (else_try),
         #######################
         # Lord information
             (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

             # Troop name
             (str_store_troop_name, s1, ":troop_no"),

             # relation to player
             (str_clear, s2),
             (str_clear, s60),
             (call_script, "script_get_troop_relation_to_player_string", s2, ":troop_no"),

             # Get renown - slot_troop_renown
             (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
             (assign, reg40, ":renown"),

             # Controversy - slot_troop_controversy
             (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
             (assign, reg41, ":controversy"),

             # Get Reputation type - slot_lord_reputation_type
             (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
             (assign, reg42, "str_personality_archetypes"),
             (val_add, reg42, ":reputation"),
             (str_store_string, s42, reg42),

             (assign, reg42, ":reputation"),
             # Intrigue impatience - slot_troop_intrigue_impatience
             (troop_get_slot, ":impatience", ":troop_no", slot_troop_intrigue_impatience),
             (assign, reg43, ":impatience"),

             # Current faction - store_troop_faction
             (store_troop_faction, ":faction", ":troop_no"),
             (troop_get_slot, ":origin_faction", ":troop_no", slot_troop_original_faction),

             # Original faction - slot_troop_original_faction
             (try_begin), #SB : do not display original faction string if same
               (neq, ":faction", ":origin_faction"),
               (val_sub, ":origin_faction", npc_kingdoms_begin),
               (val_add, ":origin_faction", "str_kingdom_1_adjective"),
               (str_store_string, s44, ":origin_faction"),
               (assign, reg44, 1),
             (else_try), #if same, start line with capitalized Noble
               (assign, reg44, 0),
             (try_end), #actually skip this line altogether if ruler
             (str_store_faction_name, s45, ":faction"),

             # Current liege - deduced from current faction
             (faction_get_slot, ":liege", ":faction", slot_faction_leader),
             (try_begin),
               #When a member of a faction without a valid leader
               (lt, ":liege", 0),
               (assign, reg46, ":liege"),
               (str_store_string, s46, "str_noone"),
               (assign, reg47, 0),
             (else_try),
               (str_store_troop_name, s46, ":liege"),
               (try_begin),
                 (eq, ":liege", ":troop_no"),
                 (assign, reg46, 0),
               (else_try),
                 (assign, reg46, ":liege"),
                 # Relation to liege
                 (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
                 (assign, reg47, reg0),
               (end_try),
             (try_end),

             # Promised a fief ?
             (troop_get_slot, reg51, ":troop_no", slot_troop_promised_fief),

             # Holdings
             (call_script, "script_get_troop_holdings", ":troop_no"),

              # slot_troop_prisoner_of_party
              (assign, reg48, 0),
              (try_begin),
                (troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                (assign, reg48, 1),
                (troop_get_slot, ":prisoner_party", ":troop_no", slot_troop_prisoner_of_party),
                (store_faction_of_party, ":party_faction", ":prisoner_party"),
                (str_store_faction_name, s48, ":party_faction"),
              (try_end),

              # Days since last meeting
              (store_current_hours, ":hours_since_last_visit"),
              (troop_get_slot, ":last_visit_hour", ":troop_no", slot_troop_last_talk_time),
              (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
              (store_div, reg49, ":hours_since_last_visit", 24),

              #### Final Storage (8 lines)
              (str_store_string, s1, "@{s1}{s2} {reg46?Reputed to be {s42}:}^Renown: {reg40}, Controversy: {reg41} {reg46?Impatience: {reg43}:}^\
{reg46?{reg44?{s44} noble:Noble} of the {s45}^Liege: {s46}, Relation: {reg47}:Ruler of the {s45}}^^{reg48?Currently prisoner of the {s48}:}^\
Days since last meeting: {reg49}^^Fiefs {reg51?(was promised a fief):}:^  {reg50?{s50}:no fief}"),
        ######################
        ## END lord infomation
        (else_try),
        #########################
        # kingdom lady, unmarried
             (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
             (troop_slot_eq, ":troop_no", slot_troop_spouse, -1),

             (str_store_troop_name, s1, ":troop_no"),

             # relation to player
             (str_clear, s2),
             (str_clear, s60),
             (call_script, "script_get_troop_relation_to_player_string", s2, ":troop_no"),

             # Controversy - slot_troop_controversy
             (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
             (assign, reg41, ":controversy"),

             # Reputation type
             (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
             (try_begin),
                 (eq, ":reputation", lrep_conventional),
                 (str_store_string, s42, "@conventional"),
             (else_try),
                 (eq, ":reputation", lrep_adventurous),
                 (str_store_string, s42, "@adventurous"),
             (else_try),
                 (eq, ":reputation", lrep_otherworldly),
                 (str_store_string, s42, "@otherwordly"),
             (else_try),
                 (eq, ":reputation", lrep_ambitious),
                 (str_store_string, s42, "@ambitious"),
             (else_try),
                 (eq, ":reputation", lrep_moralist),
                 (str_store_string, s42, "@moralist"),
             (else_try),
                 (assign, reg42, "str_personality_archetypes"),
                 (val_add, reg42, ":reputation"),
                 (str_store_string, s42, reg42),
             (try_end),

             # courtship state - slot_troop_courtship_state
             (troop_get_slot, ":courtship_state", ":troop_no", slot_troop_courtship_state),
             (try_begin),
               (eq, ":courtship_state", 1),
               (str_store_string, s43, "@just met"),
             (else_try),
               (eq, ":courtship_state", 2),
               (str_store_string, s43, "@admirer"),
             (else_try),
               (eq, ":courtship_state", 3),
               (str_store_string, s43, "@promised"),
             (else_try),
               (eq, ":courtship_state", 4),
               (str_store_string, s43, "@breakup"),
             (else_try),
               (str_store_string, s43, "@unknown"),
             (try_end),

             # Current faction - store_troop_faction
             (store_troop_faction, ":faction", ":troop_no"),
             (troop_get_slot, ":origin_faction", ":troop_no", slot_troop_original_faction),

             # Original faction - slot_troop_original_faction
             (try_begin),
               (val_sub, ":origin_faction", npc_kingdoms_begin),
               (val_add, ":origin_faction", "str_kingdom_1_adjective"),
               (str_store_string, s44, ":origin_faction"),
             (end_try),
             (str_store_faction_name, s45, ":faction"),

             # Father/Guardian
             (assign, reg46, 0),
             (try_begin),
                 (troop_slot_ge, ":troop_no", slot_troop_father, 0),
                 (troop_get_slot, ":guardian", ":troop_no", slot_troop_father),
                 (assign, reg46, 1),
             (else_try),
                 (troop_get_slot, ":guardian", ":troop_no", slot_troop_guardian),
             (try_end),
             (str_store_troop_name, s46, ":guardian"),

             # Relation with player
             (str_clear, s47),
             (str_clear, s60),
             (call_script, "script_get_troop_relation_to_player_string", s47, ":guardian"),

             # courtship permission - slot_lord_granted_courtship_permission
             (try_begin),
                 (troop_slot_ge, ":guardian", slot_lord_granted_courtship_permission, 1),
                 (assign, reg45, 1),
             (else_try),
                 (assign, reg45, 0),
             (try_end),

             # betrothed
             (assign, reg48, 0),
             (try_begin),
                 (troop_slot_ge, ":troop_no", slot_troop_betrothed, 0),
                 (troop_get_slot, reg48, ":troop_no", slot_troop_betrothed),
                 (str_store_troop_name, s48, reg48),
                 (assign, reg48, 1),
             (try_end),

             # Days since last meeting
             (store_current_hours, ":hours_since_last_visit"),
             (troop_get_slot, ":last_visit_hour", ":troop_no", slot_troop_last_talk_time),
             (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
             (store_div, reg49, ":hours_since_last_visit", 24),

             # Heard poems
             (assign, reg50, 0),
             (str_clear, s50),

             (try_begin),
                 (troop_slot_eq, ":troop_no", slot_lady_courtship_heroic_recited, 1),
                 (val_add, reg50, 1),
                 (str_store_string, s50, "@Heroic {s50}"),
             (try_end),
             (try_begin),
                 (troop_slot_eq, ":troop_no", slot_lady_courtship_allegoric_recited, 1),
                 (val_add, reg50, 1),
                 (str_store_string, s50, "@Allegoric {s50}"),
             (try_end),
             (try_begin),
                 (troop_slot_eq, ":troop_no", slot_lady_courtship_comic_recited, 1),
                 (val_add, reg50, 1),
                 (str_store_string, s50, "@Comic {s50}"),
             (try_end),
             (try_begin),
                 (troop_slot_eq, ":troop_no", slot_lady_courtship_mystic_recited, 1),
                 (val_add, reg50, 1),
                 (str_store_string, s50, "@Mystic {s50}"),
             (try_end),
             (try_begin),
                 (troop_slot_eq, ":troop_no", slot_lady_courtship_tragic_recited, 1),
                 (val_add, reg50, 1),
                 (str_store_string, s50, "@Tragic {s50}"),
             (try_end),

             #### Final Storage (8 lines)
             (str_store_string, s1, "@{s1}{s2} Controversy: {reg41}^Reputation: {s42}, Courtship state: {s43}^\
Belongs to the {s45}^{reg46?Her father, {s46}:Her guardian, {s46}}{s47}^Allowed to visit: {reg45?yes:no} {reg48?Betrothed to {s48}:}^^\
Days since last meeting: {reg49}^^Poems:^  {reg50?{s50}:no poem heard}"),
        #########################
        # END kingdom lady, unmarried
        (else_try),
        #########################
        # companions
            (is_between, ":troop_no", companions_begin, companions_end),
            (overlay_set_display, "$g_jrider_character_faction_filter", 0),

            (str_store_troop_name, s1, ":troop_no"),

            (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),

            (assign, reg42, "str_personality_archetypes"),
            (val_add, reg42, ":reputation"),
            (str_store_string, s42, reg42),

            # birthplace
            (troop_get_slot, ":home", ":troop_no", slot_troop_home),
            (str_store_party_name, s43, ":home"),

            # contacts town - slot_troop_town_with_contacts
            (troop_get_slot, ":contact_town", ":troop_no", slot_troop_town_with_contacts),
            (str_store_party_name, s44, ":contact_town"),

            # current faction of contact town
            (store_faction_of_party, ":town_faction", ":contact_town"),
            (str_store_faction_name, s45, ":town_faction"),

            # slot_troop_prisoner_of_party
            (assign, reg48, 0),
            (try_begin),
                (troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                (assign, reg48, 1),
                (troop_get_slot, ":prisoner_party", ":troop_no", slot_troop_prisoner_of_party),
                (store_faction_of_party, ":party_faction", ":prisoner_party"),
                (str_store_faction_name, s48, ":party_faction"),
            (try_end),

            # Days since last meeting
            (store_current_hours, ":hours_since_last_visit"),
            (troop_get_slot, ":last_visit_hour", ":troop_no", slot_troop_last_talk_time),
            (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
            (store_div, reg49, ":hours_since_last_visit", 24),

            (try_begin), # Companion gathering support for Right to Rule
                (troop_slot_eq, ":troop_no", slot_troop_current_mission, npc_mission_kingsupport),
                (str_store_string, s50, "@Gathering support"),
            (else_try), # Companion gathering intelligence
                (troop_slot_eq, ":troop_no", slot_troop_current_mission, npc_mission_gather_intel),
                (troop_get_slot, ":contact_town", ":troop_no", slot_troop_town_with_contacts),
                (store_faction_of_party, ":town_faction", ":contact_town"),
                (str_store_faction_name, s66, ":town_faction"),
                (str_store_string, s50, "@Gathering intelligence in the {s66}"),
            (else_try), # Companion on peace mission
                (troop_slot_ge, ":troop_no", slot_troop_current_mission, npc_mission_peace_request),
                (neg|troop_slot_ge, ":troop_no", slot_troop_current_mission, 8),

                (troop_get_slot, ":troop_no", ":troop_no", slot_troop_mission_object),
                (str_store_faction_name, s66, ":faction"),

                (str_store_string, s50, "@Ambassy to {s66}"),
            (else_try), # Companion is serving as minister player has court
                (eq, ":troop_no", "$g_player_minister"),
                (str_store_string, s50, "@Minister"),
            (else_try),
                (str_store_string, s50, "str_dplmc_none"),
        (try_end),

            # days left
            (troop_get_slot, reg50, ":troop_no", slot_troop_days_on_mission),

            #### Final Storage (8 lines)
            (str_store_string, s1, "@{s1}, {s2}^Reputation: {s42}^\
Born at {s43}^Contact in {s44} of the {s45}.^\
^{reg48?Currently prisoner of the {s48}:}^Days since last talked to: {reg49}^^Current mission:^  {s50}{reg50?, back in {reg50} days.:}"),
        #########################
        # END companions
        (try_end),
    ]),

    # Script generate_known_poems_string
    # generate in s1 list of known poems filling with blank lines for unknown ones
    ("generate_known_poems_string",
     [
        # Known poems string
        (assign, ":num_poems", 0),
        (str_store_string, s1, "str_s1__poems_known"),
        (try_begin),
            (gt, "$allegoric_poem_recitations", 0),
            (str_store_string, s1, "str_s1_storming_the_castle_of_love_allegoric"),
            (val_add, ":num_poems", 1),
        (try_end),
        (try_begin),
            (gt, "$tragic_poem_recitations", 0),
            (str_store_string, s1, "str_s1_kais_and_layali_tragic"),
            (val_add, ":num_poems", 1),
        (try_end),
        (try_begin),
            (gt, "$comic_poem_recitations", 0),
            (str_store_string, s1, "str_s1_a_conversation_in_the_garden_comic"),
            (val_add, ":num_poems", 1),
        (try_end),
        (try_begin),
            (gt, "$heroic_poem_recitations", 0),
            (str_store_string, s1, "str_s1_helgered_and_kara_epic"),
            (val_add, ":num_poems", 1),
        (try_end),
        (try_begin),
            (gt, "$mystic_poem_recitations", 0),
            (str_store_string, s1, "str_s1_a_hearts_desire_mystic"),
            (val_add, ":num_poems", 1),
        (try_end),

        # fill blank lines
        (try_for_range, ":num_poems", 5),
            (str_store_string, s1, "@{s1}^"),
        (try_end),
    ]),
   # Jrider -

#"script_dplmc_save_civilian_clothing"
##Save civilian clothing so it will still appear later
#
#INPUT: troop number
#OUTPUT: none
   ("dplmc_save_civilian_clothing", [
     (store_script_param, ":troop_no", 1),
     #SB : this interferes with auto-loot
     (try_begin),
        (gt, ":troop_no", 0),#deliberately exclude player
        (troop_is_hero, ":troop_no"),#only applies to unique characters
        (try_for_range, ":dest_slot", dplmc_ek_alt_items_begin, min(dplmc_ek_alt_items_end, dplmc_ek_alt_items_begin + 4)),
           (store_add, ":source_slot", ":dest_slot", ek_head - dplmc_ek_alt_items_begin),
           (troop_get_inventory_slot, ":item_id", ":troop_no", ":dest_slot"),
           (lt, ":item_id", 1),#do not overwrite an existing item in the destination slot
           (troop_get_inventory_slot, ":item_id", ":troop_no", ":source_slot"),
           (troop_set_inventory_slot, ":troop_no", ":dest_slot", ":item_id"),
        (try_end),
     (try_end),
   ]),
##diplomacy end+

##diplomacy end+

  #Equipment cost fix
   ("player_get_value_of_original_items",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":agent_no", 2),
      (store_script_param, ":troop_id", 3),
      (assign, ":total_equipment_cost", 0),
      (try_for_range, ":i_item_slot", 0, 8),
          (neg|player_item_slot_is_picked_up, ":player_no", ":i_item_slot"),
          (agent_get_item_slot, ":item_id", ":agent_no", ":i_item_slot"), #value between 0-7, order is weapon1, weapon2, weapon3, weapon4, head_armor, body_armor, leg_armor, hand_armor
          #(player_get_item_id, ":item_id", ":player_no", ":i_item_slot"), #only for server
          (neq, ":item_id", -1),
          (call_script, "script_multiplayer_get_item_value_for_troop", ":item_id", ":troop_id"),
          (val_add, ":total_equipment_cost", reg0),

          #Debugging
          #(assign, reg1, ":total_equipment_cost"),
          #(str_store_item_name, s0, ":item_id"),
          #(multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@{s0} for {reg0}g added to total equipment cost, which is now: {reg1}g"),
          ##
      (try_end),
      (try_for_agents, ":cur_horse"),
         #Check all horses in the scene and see if one of them is agent_no's bought horse. Won't be enough to just do (agent_get_horse, ":horse", ":agent_no"),
         #since you get money back for a bought horse, even if you have dismounted it, if the horse is still alive and has no other rider.
         (agent_is_alive, ":cur_horse"),
         (neg|agent_is_human, ":cur_horse"),  #Spawned agent is horse
         (agent_get_slot, ":agent_no_bought_horse", ":agent_no", slot_agent_bought_horse),
         (eq, ":agent_no_bought_horse", ":cur_horse"),
         (assign, ":add_horse_cost_to_equipment_value", 0),
         (try_begin),
             (agent_get_rider, ":rider_agent_id", ":cur_horse"),
             (try_begin),
                 (neq, ":rider_agent_id", -1),
                 (neg|agent_is_non_player, ":rider_agent_id"),
                 (agent_get_slot, ":agent_no_bought_horse", ":rider_agent_id", slot_agent_bought_horse),
                 (eq, ":agent_no_bought_horse", ":cur_horse"), #agent_no is mounted on the same horse he bought
                 (assign, ":add_horse_cost_to_equipment_value", 1),

                 #Debugging
                 #(agent_get_item_id, ":mount_type", ":cur_horse"), #(works only for horses, returns -1 otherwise)
                 #(str_store_item_name, s0, ":mount_type"),
                 #(multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@You are mounted on your bought {s0} and will get money for it"),
                 ##
             (else_try),
                 (eq, ":rider_agent_id", -1), #If cur_horse doesn't have a rider
                 (agent_get_horse, ":agent_no_mount", ":agent_no"),
                 (eq, ":agent_no_mount", -1), #If agent_no is not mounted on another horse
                 (agent_get_slot, ":agent_no_bought_horse", ":agent_no", slot_agent_bought_horse),
                 (eq, ":agent_no_bought_horse", ":cur_horse"),
                 (assign, ":add_horse_cost_to_equipment_value", 1),

                 #Debugging
                 #(agent_get_item_id, ":mount_type", ":cur_horse"), #(works only for horses, returns -1 otherwise)
                 #(str_store_item_name, s0, ":mount_type"),
                 #(multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@Your bought {s0} is alive so you get money for it"),
                 ##
            (try_end),
            (eq, ":add_horse_cost_to_equipment_value", 1),
            (agent_get_item_id, ":cur_mount_type", ":cur_horse"), #Checks which type the horse is
            (call_script, "script_multiplayer_get_item_value_for_troop", ":cur_mount_type", ":troop_id"),
            (val_add, ":total_equipment_cost", reg0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@Added money for your old horse"),
         (try_end),
      (try_end),
      (agent_set_slot, ":agent_no", slot_agent_bought_horse, -1),
      (assign, reg0, ":total_equipment_cost"),
     ]),
     ###

     ##script_improve_center
     #helper script for building in centers
    ("improve_center", [
        (store_script_param, ":center_no", 1),
        (store_script_param, ":builder", 2),
        (store_script_param, ":improvement_time", 3),
        (party_set_slot, ":center_no", slot_center_current_improvement, "$g_improvement_type"),
        (store_current_hours, ":cur_hours"),
        (store_mul, ":hours_takes", ":improvement_time", 24),
        (val_add, ":hours_takes", ":cur_hours"),
        (party_set_slot, ":center_no", slot_center_improvement_end_hour, ":hours_takes"),
        (assign, reg6, ":improvement_time"),
        (call_script, "script_get_improvement_details", "$g_improvement_type"),
        (add_party_note_from_sreg, ":center_no", 2, "@A {s0} is being built. It will finish in {reg6} days", 1),
        (try_begin), #should probably raise this depending on project instead of constant reward
          (troop_is_hero, ":builder"),
          (neq, ":builder", "trp_player"),
          (call_script, "script_change_troop_renown", ":builder", dplmc_companion_skill_renown),
        (try_end),
    ]),

     ##script_calculate_improvement_limit
     #calculate threshold for building stuff
     #input: troop_no, center_no (unused)
     #output: reg0
    ("calculate_improvement_limit", [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":unused_2"),
        (assign, ":limit", dplmc_improvement_limit),
        (troop_get_slot, ":personality", ":troop_no", slot_lord_reputation_type),
        (try_begin), #bad personality, unlikely to ever build property
            (is_between, ":personality", lrep_selfrighteous, lrep_goodnatured),
            (val_mul, ":limit", ":personality"),
            (val_div, ":limit", 2),
        (else_try), #include companion personality types
            (is_between, ":personality", lrep_goodnatured, lrep_custodian),
            (try_begin), #exception
              (neq, ":personality", lrep_roguish),
              (store_mul, ":level", ":personality", 250),
              (val_sub, ":limit", ":level"),
            (try_end),
        (try_end),
        (assign, reg0, ":limit"),
    ]),

     ##script_calculate_equipment_limit
     #calculate threshold for upgrading equipment imod from merchants
     #input: troop_no, center_no (unused)
     #output: reg0
    ("calculate_equipment_limit", [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":center_no"),
        (assign, ":limit", dplmc_equipment_limit),
        (troop_get_slot, ":personality", ":troop_no", slot_lord_reputation_type),

        (try_begin), #focus on arms
          (is_between, ":personality", lrep_martial, lrep_selfrighteous),
          (val_div, ":limit", 2),
        (else_try), #invest in gear not fief
          (eq, ":personality", lrep_roguish),
          (val_sub, ":limit", 1000),
        (try_end),

        #aristocracy modifier as enthusiasm for shopping
        (store_faction_of_party, ":faction_no", ":center_no"),
        (faction_get_slot, ":aristocracy", ":faction_no", dplmc_slot_faction_aristocracy),
        (val_mul, ":aristocracy", -100), #high plutocracy more shopping, decreasing threshold
        (val_add, ":limit", ":aristocracy"),

        (assign, reg0, ":limit"),
    ]),
    #script_change_troop_intrigue_impatience
    #inputs: troop_no ($g_talk_troop), amount
    #output: slot_troop_intrigue_impatience changed
    ("change_troop_intrigue_impatience", [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":amount"),
        (troop_get_slot, ":impatience", ":troop_no", slot_troop_intrigue_impatience),
        (val_max, ":impatience", ":amount"),
        (troop_set_slot, ":troop_no", slot_troop_intrigue_impatience, ":impatience"),
    ]),
    #script_center_get_bandits
    #inputs: center_no, mode
    #output: bandit_troop in reg0
    # get an appropriate bandit to infest the village
  ("center_get_bandits",[

    (store_script_param_1, ":village_no"),
    (store_script_param_2, ":mode"),
    (assign, ":bandit_troop", "trp_looter"),

    (try_begin), #native mode
      (eq, ":mode", -1),
      (store_random_in_range, ":random_no", 0, 3),
      (try_begin),
        (eq, ":random_no", 0),
        (assign, ":bandit_troop", "trp_bandit"),
      (else_try),
        (eq, ":random_no", 1),
        (assign, ":bandit_troop", "trp_mountain_bandit"),
      (else_try),
        (assign, ":bandit_troop", "trp_forest_bandit"),
      (try_end),
    (else_try), #faction mode
      (eq, ":mode", 0),

      (assign, ":bandit_troop", "trp_looter"),
      # (store_faction_of_party, ":faction", ":village_no"),
      (party_get_slot, ":faction", ":village_no", slot_center_original_faction),
      (store_random_in_range, ":random_no", 0, 10),
      (try_begin), #deserter troops, 10% chance
        (eq, ":random_no", 0),
        (faction_get_slot, ":bandit_troop", ":faction", slot_faction_deserter_troop),
      (else_try),
        (lt, ":random_no", 6),  #regular bandits (looter to brigand), 50%
        (val_div, ":random_no", 2),
        (store_add, ":bandit_troop","trp_looter",":random_no"),
      (else_try), #regional bandits, 40% (should be terrain based though)
        (try_begin),
          (eq, ":faction", "fac_kingdom_6"),
          (assign, ":bandit_troop", "trp_desert_bandit"),
        (else_try),
          (eq, ":faction", "fac_kingdom_5"),
          (assign, ":bandit_troop", "trp_mountain_bandit"),
        (else_try),
          (eq, ":faction", "fac_kingdom_4"),
          (assign, ":bandit_troop", "trp_sea_raider"),
        (else_try),
          (eq, ":faction", "fac_kingdom_3"),
          (assign, ":bandit_troop", "trp_steppe_bandit"),
        (else_try),
          (eq, ":faction", "fac_kingdom_2"),
          (assign, ":bandit_troop", "trp_taiga_bandit"),
        (else_try),
          (eq, ":faction", "fac_kingdom_1"),
          (assign, ":bandit_troop", "trp_forest_bandit"),
        (try_end),
      (try_end),
    (else_try), #terrain mode
      (eq, ":mode", 1),
      #base type first
      (party_get_current_terrain, ":terrain_type", ":village_no"),
      (try_begin),
        (this_or_next|eq, ":terrain_type", rt_steppe),
        (eq, ":terrain_type", rt_steppe_forest),
        (assign, ":bandit_troop", "trp_steppe_bandit"),
      # (else_try),
        # (eq, ":terrain_type", rt_plain),
        # (assign, ":bandit_troop", "trp_bandit"),
      (else_try),
        (this_or_next|eq, ":terrain_type", rt_snow),
        (eq, ":terrain_type", rt_snow_forest),
        (assign, ":bandit_troop", "trp_taiga_bandit"),
      (else_try),
        (this_or_next|eq, ":terrain_type", rt_desert),
        (eq, ":terrain_type", rt_desert_forest),
        (assign, ":bandit_troop", "trp_desert_bandit"),
      # (else_try),
        # (eq, ":terrain_type", rt_forest),
        # (assign, ":bandit_troop", "trp_forest_bandit"),
      (try_end),
      (try_begin),
        (eq, ":bandit_troop", "trp_looter"), #still not picked
        #proximity to features (forest, mountain, ocean),
        (party_get_position, pos1, ":village_no"),
        (try_begin), #cf operation to see if it's near water
          (map_get_water_position_around_position, pos2, pos1, 5),
          # after finding water limit range of spawning (so sea raiders don't appear upriver)
          (store_add, ":limit", "p_sea_raider_spawn_point_1", num_sea_raider_spawn_points),
          (try_for_range, ":spawn_point", "p_sea_raider_spawn_point_1", ":limit"),
            (store_distance_to_party_from_party, ":distance", ":village_no", ":spawn_point"),
            (lt, ":distance", 50), # 200% bandit spawning radius
            (assign, ":limit", -1),
          (try_end),
          (eq, ":limit", -1), #within boundaries
          (assign, ":bandit_troop", "trp_sea_raider"),
        (else_try), #sample random points until we find forest/mountain (coast)
          (assign, ":forest_count", 0),
          (assign, ":mountain_count", 0),
          (assign, ":other_count", 0),
          (try_for_range, ":unused", 0, 100),
            (map_get_land_position_around_position, pos2, pos1, 5),
            (party_set_position, "p_temp_party", pos2),
            (party_get_current_terrain, ":terrain_type", "p_temp_party"),
            (try_begin),
              (eq, ":terrain_type", rt_forest),
              (val_add, ":forest_count", 1),
            (else_try),
              (eq, ":terrain_type", rt_mountain),
              (val_add, ":mountain_count", 1),
            (else_try),
              (val_add, ":other_count", 1),
            (try_end),
          (try_end),
          (try_begin), # not enough features
            (gt, ":other_count", 75), #pass through to faction calls
            (call_script, "script_center_get_bandits", ":village_no", 0),
            (assign, ":bandit_troop", reg0),
          (else_try),
            (gt, ":forest_count", ":mountain_count"),
            (gt, ":forest_count", 15),
            (assign, ":bandit_troop", "trp_forest_bandit"),
          (else_try),
            (gt, ":mountain_count", ":forest_count"),
            (gt, ":mountain_count", 15),
            (assign, ":bandit_troop", "trp_mountain_bandit"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
    (assign, reg0, ":bandit_troop"),
  ]),


  ("create_wpn_slot_overlay", [
      (store_script_param, ":slot", 1),
      (store_script_param, ":pos", 2),
      (init_position, pos1),
      (position_set_x, pos1, 270),
      (position_set_y, pos1, ":pos"),
      (create_combo_button_overlay, ":obj"),
      (overlay_set_position, ":obj", pos1),
      (assign, ":sub_overlay_id", 0),
      (store_add, ":upgrade_slot", ":slot", dplmc_slot_upgrade_wpn_0),

      # #SB : add meta-types
      # (overlay_add_item, ":obj", "str_dplmc_hero_wpn_slot_pikes"),
      # (overlay_add_item, ":obj", "str_dplmc_hero_wpn_slot_lance"),
      # (overlay_add_item, ":obj", "str_dplmc_hero_wpn_slot_morningstar"),
      # (try_for_range_backwards, ":item_type", dplmc_itp_morningstar, dplmc_itp_pike + 1),
        # (troop_slot_eq, "$temp", ":upgrade_slot", ":item_type"),
        # (overlay_set_val, ":obj", ":sub_overlay_id"),
      # (else_try),
        # (val_add, ":sub_overlay_id", 1),
      # (try_end),
      (call_script, "script_dplmc_get_current_item_for_autoloot", ":slot"), #goes to "keep current", s10
      (try_for_range_backwards, ":item_type", 0, itp_type_animal),
        (this_or_next|is_between, ":item_type", itp_type_one_handed_wpn, itp_type_goods),
        (this_or_next|is_between, ":item_type", itp_type_pistol, itp_type_animal),
        (eq, ":item_type", 0),
        (store_add, ":out_string", "str_dplmc_hero_wpn_slot_none", ":item_type"),
        (overlay_add_item, ":obj", ":out_string"),
        (try_begin), #find base type
          (troop_get_slot, ":cur_value", "$temp", ":upgrade_slot"),
          (val_mod, ":cur_value", meta_itp_mask),
          (eq, ":cur_value", ":item_type"),
          (overlay_set_val, ":obj", ":sub_overlay_id"),
        (try_end),
        (val_add, ":sub_overlay_id", 1),
      (try_end),

      #store id in slot
      (troop_set_slot, "trp_stack_selection_ids", ":slot", ":obj"),
      # # only works for original button, not drop-down lists
      # (overlay_set_additional_render_height, ":obj", 99),

      (assign, reg1, ":obj"), #return overlay id
  ]),


  ("update_wpn_slot_itp", [
      (store_script_param, ":slot", 1),
      (store_script_param, ":value", 2),
      (troop_get_slot, ":item_type", "trp_temp_array_c", ":value"),
      (troop_get_slot, ":slot_value", "$temp", ":slot"),
      (try_begin), #if new value supports metamods, inherit
        (call_script, "script_cf_item_type_has_advanced_autoloot", ":item_type"),
        (store_mod, ":original_value", ":slot_value", meta_itp_mask),
        (val_sub, ":slot_value", ":original_value"), #remove original itp
        (val_add, ":slot_value", ":item_type"), #add new
      (else_try), #otherwise replace value
        (assign, ":slot_value", ":item_type"),
      (try_end),
      (troop_set_slot, "$temp", ":slot", ":slot_value"),
      (assign, "$temp_2", ":slot"),
      #restart presentation instead of updating overlay value (because we can't)
      (start_presentation, "prsnt_dplmc_autoloot_upgrade_management"),
  ]),
  #script_item_get_type_aux : auxiliary item classification script, see header_items for values
  #input : item
  #output: reg0, item type or meta-type
  ("item_get_type_aux", [
    (store_script_param, ":item", 1),

    (item_get_type, ":itp", ":item"),
    (try_begin),
      # (item_slot_eq, ":item", dplmc_slot_two_handed_one_handed, 1),
      # (item_has_property, ":item", itp_type_two_handed_wpn),
      (eq, ":itp", itp_type_two_handed_wpn),
      (neg|item_has_property, ":item", itp_two_handed),
      (assign, ":itp", dplmc_itp_morningstar), # type 11 = two-handed/one-handed
    (else_try),
      (eq, ":itp", itp_type_polearm),
      (item_get_swing_damage, ":swing", ":item"),
      (item_get_thrust_damage, ":thrust", ":item"),
      (try_begin),
        (ge, ":swing", ":thrust"),
        (item_get_swing_damage_type, ":damage_type", ":item"),
        (eq, ":damage_type", cut),
        (assign, ":itp", dplmc_itp_halberd),
      (else_try),
        (lt, ":swing", ":thrust"),
        (try_begin), #lances
          (item_has_property, ":item", itp_couchable),
          (assign, ":itp", dplmc_itp_lance),
        (else_try), #can't be both lance and pike
          # (item_has_property, ":item", itp_cant_use_on_horseback), #too restrictive
          (item_get_weapon_length, ":length", ":item"),
          (ge, ":length", dplmc_pike_length_cutoff), #arbitrary value to allow awlpikes to fall in range
          (item_has_capability, ":item", itcf_thrust_polearm), #has two-handed thrust
          (this_or_next|item_has_property, ":item", itp_two_handed),
          (item_has_property, ":item", itp_penalty_with_shield),
          (assign, ":itp", dplmc_itp_pike),
        (try_end),
      (try_end),
    (try_end),
    (assign, reg0, ":itp"),
  ]),

  #check if weapons are wholly inappropriate for actual combat
  ("cf_melee_weapon_is_civilian", [
    (store_script_param, ":item", 1),
    (this_or_next|is_between, ":item", "itm_sickle", "itm_dagger"),
    (this_or_next|is_between, ":item", "itm_scythe", "itm_military_fork"),
    (this_or_next|eq, ":item", "itm_wooden_stick"),
    (eq, ":item", "itm_torch"),
    # (eq, ":item", "itm_stones"),
     #include arena weapons here as well
  ]),

  #check if the item type has advanced auto-loot options available (damage type, meta-type)
  ("cf_item_type_has_advanced_autoloot", [
    (store_script_param, ":item_type", 1),
    (this_or_next|is_between, ":item_type", itp_type_one_handed_wpn, itp_type_shield),
    (eq, ":item_type", itp_type_thrown), #throwing axe vs jaridss vs rocks
    #all other ranged weapons are pierce (for now) excluding arena ones
  ]),

  #script_display_policy_string_to_reg
  #unify string register usage to one temp s0 and one output s20
  #register reg2,3 are used for mode and postfix
  ("display_policy_string_to_reg", [
    (store_script_param, ":faction_no", 1),
    (store_script_param, reg2, 2), #whether it is third person "the" or first person "our"
    (store_script_param, reg3, 3), #spaces or line breaks as the postfix delimiter

    (str_store_faction_name_link, s5, ":faction_no"),
    (assign, ":string", "str_dplmc_neither_centralize_nor_decentralized"),
    (faction_get_slot, ":centralization", ":faction_no", dplmc_slot_faction_centralization),
    (val_add, ":string", ":centralization"),
    (str_store_string, s0, ":string"),
    (str_store_string, s20, "@{s20}{reg2?Our government:The goverment of the {s5}} is {s0}.{reg3?^: }"),

    (assign, ":string", "str_dplmc_neither_aristocratic_nor_plutocratic"),
    (faction_get_slot, ":aristocraty", ":faction_no", dplmc_slot_faction_aristocracy),
    (val_add, ":string", ":aristocraty"),
    (str_store_string, s0, ":string"),
    (str_store_string, s20, "@{s20}The upper class society is {s0}.{reg3?^: }"),

    (assign, ":string", "str_dplmc_mixture_serfs"),
    (faction_get_slot, ":serfdom", ":faction_no", dplmc_slot_faction_serfdom),
    (val_add, ":string", ":serfdom"),
    (str_store_string, s0, ":string"),
    (str_store_string, s20, "@{s20}{reg2?Our:The} people are {s0}.{reg3?^: }"),

    (assign, ":string", "str_dplmc_mediocre_quality"),
    (faction_get_slot, ":quality", ":faction_no", dplmc_slot_faction_quality),
    (val_add, ":string", ":quality"),
    (str_store_string, s0, ":string"),
    (str_store_string, s20, "@{s20}{reg2?Our:The} troops have {s0}.{reg3?^: }"),

    ##nested diplomacy start+ add mercantilism
    (assign, ":string", "str_dplmc_neither_mercantilist_nor_laissez_faire"),
    (faction_get_slot, ":mercantilism", ":faction_no", dplmc_slot_faction_mercantilism),
    (val_add, ":string", ":mercantilism"),
    (str_store_string, s0, ":string"),
    (str_store_string, s20, "@{s20}{reg2?Our:The government's} approach to trade is {s0}.{reg3?^: }"),
  ]),

  #native stuff for startup merchants
  ("get_troop_of_merchant",
  [
        (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),
        (store_sub, ":troop_of_merchant", ":starting_town_faction", npc_kingdoms_begin),
        (val_add, ":troop_of_merchant", startup_merchants_begin),
        (assign, reg0, ":troop_of_merchant"),
  ]),

  #reusable code to check whether npcs in a specific range have been met
  #does not account for alternative towns
  ("cf_no_known_taverngoers",
  [
      (store_script_param_1, ":begin"),
      (store_script_param_2, ":end"),
      # (assign, ":num_towns", tavern_booksellers_end),
      (try_for_range, ":troop_no", ":begin", ":end"),
        # (neg|party_slot_eq, ":town_no", slot_center_tavern_bookseller, 0),
        # (party_get_slot, ":seller", ":town_no", slot_center_tavern_bookseller),#addition - fixed 2011-03-29
        (troop_slot_ge, ":troop_no", slot_troop_met, 1),
        (troop_get_slot, ":town_no", ":troop_no", slot_troop_cur_center),
        (is_between, ":town_no", walled_centers_begin, walled_centers_end),
        (assign, ":end", ":begin"), #loop break
      (try_end),
      (neq, ":begin", ":end"),
  ]),

  #script_list_known_taverngoers
  #input: starting/ending troop range, also party slot if necessary as error check
  #output: location of known tavern npcs to s11
  ("list_known_taverngoers",
  [
      (store_script_param, ":begin", 1),
      (store_script_param, ":end", 2),
      (store_script_param, ":slot_no", 3),

      (assign, ":num_towns", 0),
      (try_for_range, ":troop_no", ":begin", ":end"),
        (this_or_next|troop_slot_ge, ":troop_no", slot_troop_met, 1),
        (troop_slot_eq, ":troop_no", slot_troop_cur_center, "$current_town"),
        (troop_get_slot, ":town_no", ":troop_no", slot_troop_cur_center),
        (is_between, ":town_no", walled_centers_begin, walled_centers_end),
        # (neg|party_slot_eq, ":town_no", slot_center_ransom_broker, 0),
        (party_slot_eq, ":town_no", ":slot_no", ":troop_no"),
        (val_add, ":num_towns", 1),
        (str_store_party_name_link, s50, ":town_no"),
        (try_begin),
          (eq, ":num_towns", 1),
          (str_store_string, s51, s50),
        (else_try),
          (eq, ":num_towns", 2),
          (str_store_string, s51, "str_s50_and_s51"),
        (else_try),
          (str_store_string, s51, "str_s50_comma_s51"),
        (try_end),

        (try_begin), #list false tavern npcs
          (call_script, "script_cf_find_alternative_town_for_taverngoers", ":town_no", -9),
          (assign, ":alternative_town", reg0),
          (neg|party_slot_ge, ":alternative_town", ":slot_no", ":begin"),
          (val_add, ":num_towns", 1),
          (str_store_party_name_link, s52, ":alternative_town"),
          (try_begin), #this is at least the second town in the string
            (eq, ":num_towns", 2),
            (str_store_string, s51, "str_s52_and_s51"),
          (else_try),
            (str_store_string, s51, "str_s52_comma_s51"),
          (try_end),
        (try_end),
        # (display_message, "@{s51}"),
      (try_end),
      (str_store_troop_name_plural, s10, ":begin"), #default titles "book_merchant" "ransom_broker" etc
      (str_store_string_reg, s11, s51),
      (display_message, "@You can find {s10}s at {s11}."),
  ]),
  #native functionality to increase tavern diversity
  ("cf_find_alternative_town_for_taverngoers",
  [
      (store_script_param_1, ":town_no"),
      (store_script_param_2, ":adder"),
      (store_add, ":alternative_town", ":town_no", ":adder"), #should really randomize this

      # (store_sub, ":num_towns", towns_end, towns_begin),
      (try_begin),
        (ge, ":alternative_town", towns_end),
        (val_sub, ":alternative_town", towns_end),
        (val_add, ":alternative_town", towns_begin),
      (else_try),
        (lt, ":alternative_town", towns_begin),
        (val_add, ":alternative_town", towns_end),
      (try_end),
      ##diplomacy start+
      #The above code makes assumptions about the number of towns that might not be true on other maps.
      #Changing it to support variable sizes would not be hard, but I'm not convinced that it is so
      #desirable in the first place.
      (is_between, ":alternative_town", towns_begin, towns_end),
      # (party_slot_eq, ":alternative_town", slot_party_type, spt_town),
      (assign, reg0, ":alternative_town"),
  ]),

  #script_calculate_ransom_contribution
  #input : troop_no, amount expected, properly set up qst_rescue_prisoner targets
  #assumes no other sources of debt (dialog prevents condition) and quest troop is active and related
  #output : amount lord_no personally pays in reg0, cached in slot_troop_player_debt, cleared when player rejects it
  ("calculate_ransom_contribution", [
    (store_script_param_1, ":lord_no"), #usually $g_talk_troop
    (store_script_param_2, ":ransom_size"), #2000 from quest giver, up to 125*strength for other relatives
    #because kingdom ladies aren't landholders, they give it without consequence of debt if quest fails (also less dialogue to write)
    (assign, ":ransom_amount", 0),

    (try_begin),
      (check_quest_active, "qst_rescue_prisoner"),
      (quest_get_slot, ":prisoner", "qst_rescue_prisoner", slot_quest_target_troop),
      (quest_get_slot, ":cur_ransom", "qst_rescue_prisoner", slot_quest_target_state),
      (try_begin),
        #each +-2 relation has 1% effect on calculation to the effect of 50%/150% initial value
        (call_script, "script_troop_get_relation_with_troop", ":lord_no", ":prisoner"),
        (store_div, ":relation", reg0, 2),
        (val_add, ":relation", 100),
        (val_mul, ":ransom_amount", ":relation"),
        (val_div, ":ransom_amount", 100),
      (try_end),
      # problem is this script has variance in output, we can use the cached slot_quest_target_amount
      (call_script, "script_calculate_ransom_amount_for_troop", ":prisoner"),
      (assign, ":ransom", reg0), #original amount
      (val_add, ":ransom_size", ":cur_ransom"),
      (try_begin), #contributed too much, get remainder before arbitrary cap
        (gt, ":ransom_size", ":ransom"),
        (store_sub, ":ransom_amount", ":ransom", ":cur_ransom"),
      (else_try), #give full amount
        (store_sub, ":ransom_amount", ":ransom_size", ":cur_ransom"), #undo adding existing ransom
      (try_end),

      (try_begin), #active npcs have wealth
        (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":cur_wealth", ":lord_no", slot_troop_wealth),
        (val_div, ":cur_wealth", 2), #at most half for contributing
        (val_min, ":cur_wealth", ":ransom"),
        (val_min, ":ransom_amount", ":cur_wealth"), #actual amount the lord can give
      (try_end),
      (troop_set_slot, ":lord_no", slot_troop_player_debt, ":ransom_amount"),
    (try_end),
    (assign, reg0, ":ransom_amount"),
    ]
  ),

  #script_lend_money_for_ransom
  #actually parcels out the amount calculated in the above script
  ("lend_money_for_ransom", [
    (store_script_param_1, ":lord_no"), #usually $g_talk_troop
    (try_begin),
      (troop_get_slot, ":ransom_amount", ":lord_no", slot_troop_player_debt),
      (le, ":ransom_amount", 0),
      (store_script_param_2, ":ransom_amount"),
    (try_end),
    (quest_get_slot, ":cur_ransom", "qst_rescue_prisoner", slot_quest_target_state),
    (val_add, ":cur_ransom", ":ransom_amount"), #actual amount to give

    #set up quests
    (quest_set_slot, "qst_rescue_prisoner", slot_quest_target_state, ":cur_ransom"),
    (assign, reg0, ":cur_ransom"),
    #the amount calculated at the start, will differ from expected ransom
    (quest_get_slot, reg1, "qst_rescue_prisoner", slot_quest_target_amount),
    (str_store_string, s1, "@You have raised {reg0}/{reg1} denars for the ransom"),
    (add_quest_note_from_sreg, "qst_rescue_prisoner", 4, s1, 1), #0:date, 1:giver, 2:desc 3:time

    #move actual gold
    (troop_add_gold, "trp_player", ":ransom_amount"),
    (try_begin),
      (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
      (call_script, "script_dplmc_remove_gold_from_lord_and_holdings", ":ransom_amount", ":lord_no"),
      (val_add, ":ransom_amount", dplmc_ransom_debt_mask), #masking this from "real" debt
      (troop_set_slot, ":lord_no", slot_troop_player_debt, ":ransom_amount"),
    (try_end),

    ]
  ),


  #script_cf_dplmc_battle_continuation
  #new camera setup scripts, setting up other calls

  ("cf_dplmc_battle_continuation", [
    (eq, "$g_dplmc_battle_continuation", 0),
    (assign, ":num_allies", 0),
    (try_for_agents, ":agent"),
      (agent_is_ally, ":agent"),
      (agent_is_alive, ":agent"),
      (val_add, ":num_allies", 1),
    (try_end),
    (gt, ":num_allies", 0),
    (try_begin),
      (eq, "$g_dplmc_cam_activated", 0),
      #(store_mission_timer_a, "$g_dplmc_main_hero_fallen_seconds"),
      (assign, "$g_dplmc_cam_activated", "$g_dplmc_cam_default"),

      (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
      (store_add, ":string", "$g_dplmc_cam_activated", "str_camera_keyboard"),
      (val_sub, ":string", 1),
      (display_message, ":string"),
      # (display_message, "@To watch the fight you can use 'w, a, s, d, numpad_+/numpad_-' to move and 'numpad_1,2,3,4,6,8' to rotate the cam."),

      (try_begin), #http://forums.taleworlds.com/index.php/topic,322343.0.html
        (eq, "$g_dplmc_charge_when_dead", 1),
        (get_player_agent_no, ":player_agent"),
        (agent_get_team, ":player_team", ":player_agent"),
        (set_show_messages, 0),
        (team_give_order, ":player_team", grc_everyone, mordr_charge),
        (team_give_order, ":player_team", grc_everyone, mordr_use_any_weapon),
        (team_give_order, ":player_team", grc_everyone, mordr_fire_at_will),
        (set_show_messages, 1),
      (try_end),

      (mission_cam_get_position, pos1), #Death pos
      (position_get_rotation_around_z, ":rot_z", pos1),

      (init_position, pos47),
      (position_copy_origin, pos47, pos1), #Copy X,Y,Z pos
      (position_rotate_z, pos47, ":rot_z"), #Copying X-Rotation is likely possible, but I haven't figured it out yet

      (mission_cam_set_mode, 1, 0, 0), #Manual?

      (try_begin), #auto-assign the closest agent
        (eq, "$g_dplmc_cam_activated", camera_follow),
        (call_script, "script_dmod_closest_agent"),
      (try_end),

      (mission_cam_set_position, pos47),
    (try_end),
    ]),

    ("init_keys_array", keys_array()),
    ("setup_camera_keys", [

      # (assign, "$g_dplmc_cam_default", camera_keyboard),
      # (assign, "$g_camera_up", key_w),
      # (assign, "$g_camera_down", key_s),
      # (assign, "$g_camera_left", key_a),
      # (assign, "$g_camera_right", key_d),

      #default custom commander y/z offsets
      (call_script, "script_setup_camera_offset"),
      #these will be retained after being changed inside missions

      #deathcam
      (assign, "$g_cam_tilt_left", key_numpad_1),
      (assign, "$g_cam_tilt_right", key_numpad_3),

      (assign, "$g_camera_adjust_add", key_numpad_plus),
      (assign, "$g_camera_adjust_sub", key_numpad_minus),

      #normally numpad swaps equipment, but we're dead so w/e
      (assign, "$g_camera_rot_up", key_numpad_8),
      (assign, "$g_camera_rot_down", key_numpad_2),
      (assign, "$g_camera_rot_left", key_numpad_4),
      (assign, "$g_camera_rot_right", key_numpad_6),
    ]),

    #call when camera positions get weird
    ("setup_camera_offset",
      [
      (assign, "$g_camera_z", 200),
      (assign, "$g_camera_y", -175),
      (assign, "$g_camera_rotate_x", 0),
      (assign, "$g_camera_rotate_y", 0),
      (assign, "$g_camera_rotate_z", 0),

      ]),

    #initialize all active death cam globals
    ("init_death_cam",
      [
        (assign, "$deathcam_mouse_last_x", 5000),
        (assign, "$deathcam_mouse_last_y", 3750),
        (assign, "$deathcam_mouse_last_notmoved_x", 5000),
        (assign, "$deathcam_mouse_last_notmoved_y", 3750),
        (assign, "$deathcam_mouse_notmoved_x", 5000), #Center screen (10k fixed pos)
        (assign, "$deathcam_mouse_notmoved_y", 3750),
        (assign, "$deathcam_mouse_notmoved_counter", 0),

        (assign, "$deathcam_total_rotx", 0),

        (assign, "$deathcam_sensitivity_x", 400), #4:3 ratio may be best
        (assign, "$deathcam_sensitivity_y", 300), #If modified, change values in common_move_deathcam

        (assign, "$deathcam_prsnt_was_active", 0),

        (assign, "$deathcam_keyboard_rotation_x", 0),
        (assign, "$deathcam_keyboard_rotation_y", 0),

        (assign, "$g_dplmc_cam_activated", 0),
        (assign, "$dmod_current_agent", -1),
        # check if keys are not set/invalid
        (try_begin),
          (neg|is_between, "$g_dplmc_cam_default", camera_keyboard, camera_follow + 1),
          (call_script, "script_setup_camera_keys"),
          (assign, "$g_dplmc_cam_default", camera_keyboard),
        (try_end),

        (get_player_agent_no, "$g_player_agent"),
        (agent_get_team, "$g_player_team", "$g_player_agent"),
      ]),

    ("cf_cancel_camera_keys", [
      (this_or_next|game_key_is_down, gk_view_char),
      (this_or_next|game_key_is_down, gk_zoom),
      (game_key_is_down, gk_cam_toggle),
      (mission_cam_set_mode, 0),
    ]),

    ("dmod_closest_agent", [
          (assign, ":cur_agent", -1),
          (assign, ":distance", 999999),
          (mission_cam_get_position, pos11),
          (position_set_z_to_ground_level, pos11),
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            (agent_is_ally, ":agent_no"),
            #position on the ground
            (agent_get_position, pos13, ":agent_no"),
            # (position_get_screen_projection, pos14, pos13),
            # (get_distance_between_positions, ":cur_distance", pos12, pos14),
            (get_distance_between_positions, ":cur_distance", pos11, pos13),
            (lt, ":cur_distance", ":distance"),
            (assign, ":distance", ":cur_distance"),
            (assign, ":cur_agent", ":agent_no"),
          (try_end),
          (try_begin),
            (neq, ":cur_agent", 1),
            (assign, "$dmod_current_agent", ":cur_agent"),
            (str_store_agent_name, 1, "$dmod_current_agent"),
            (display_message, "@Selected Troop: {s1}"),
          (try_end),

      ]
    ),
    # script_dmod_cycle_forwards
      # Output: New $dmod_current_agent
      # Used to cycle forwards through valid agents
      ("dmod_cycle_forwards",[

         (assign, ":agent_moved", 0),
         (assign, ":first_agent", -1),
         # (get_player_agent_no, ":player_agent"),
         # (agent_get_team, ":player_team", ":player_agent"),

        (try_for_agents, ":agent_no"),
            (neq, ":agent_moved", 1),
            (neq, ":agent_no", "$g_player_agent"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            (agent_is_ally, ":agent_no"),
            # (agent_get_team, ":cur_team", ":agent_no"),
            # (this_or_next|eq, ":cur_team", 5), #bodyguards
            # (eq, ":cur_team", ":player_team"),
            (try_begin),
              (lt, ":first_agent", 0),
              (assign, ":first_agent", ":agent_no"),
            (try_end),
            (gt, ":agent_no", "$dmod_current_agent"),
            (assign, "$dmod_current_agent", ":agent_no"),
            (assign, ":agent_moved", 1),
        (try_end),

        (try_begin),
            (eq, ":agent_moved", 0),
            (neq, ":first_agent", -1),
            (assign, "$dmod_current_agent", ":first_agent"),
            (assign, ":agent_moved", 1),
        (else_try),
            (eq, ":agent_moved", 0),
            (eq, ":first_agent", -1),
            (display_message, "@No Troops Left."),
        (try_end),

        (try_begin),
            (eq, ":agent_moved", 1),
            (str_store_agent_name, s1, "$dmod_current_agent"),
            (display_message, "@Selected Troop: {s1}"),
        (try_end),
      #(assign, "$dmod_move_camera", 1),
      ]),

      # script_dmod_cycle_backwards
      # Output: New $dmod_current_agent
      # Used to cycle backwards through valid agents
      ("dmod_cycle_backwards",[

        (assign, ":new_agent", -1),
        (assign, ":last_agent", -1),
        # (get_player_agent_no, ":player_agent"),
        # (agent_get_team, ":player_team", ":player_agent"),

        (try_for_agents, ":agent_no"),
            (neq, ":agent_no", "$g_player_agent"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            (agent_is_ally, ":agent_no"),
        # (agent_get_team, ":cur_team", ":agent_no"),
        # (this_or_next|eq, ":cur_team", 5), #bodyguards
        # (eq, ":cur_team", ":player_team"),
            (assign, ":last_agent", ":agent_no"),
            (lt, ":agent_no", "$dmod_current_agent"),
            (assign, ":new_agent", ":agent_no"),
        (try_end),

        (try_begin),
            (eq, ":new_agent", -1),
            (neq, ":last_agent", -1),
            (assign, ":new_agent", ":last_agent"),
        (else_try),
            (eq, ":new_agent", -1),
            (eq, ":last_agent", -1),
            (display_message, "@No Troops Left."),
        (try_end),

        (try_begin),
            (neq, ":new_agent", -1),
            (assign, "$dmod_current_agent", ":new_agent"),
            (str_store_agent_name, 1, "$dmod_current_agent"),
            (display_message, "@Selected Troop: {s1}"),
        (try_end),
      ]),



  #script_start_town_conversation
  #input: center's slot no, entry points
  #used to talk to various center merchant npcs including guildmaster
  ("start_town_conversation",
    [
      (store_script_param, ":troop_slot_no", 1),
      (store_script_param, ":entry_no", 2),

      (assign, "$talk_context", tc_town_talk),
      (try_begin),
        (eq, ":troop_slot_no", slot_town_merchant),
        (assign, ":scene_slot_no", slot_town_store),
      (else_try),
        (eq, ":troop_slot_no", slot_town_tavernkeeper),
        (assign, ":scene_slot_no", slot_town_tavern),
        (assign, "$talk_context", tc_tavern_talk),
      (else_try),
        (assign, ":scene_slot_no", slot_town_center),
      (try_end),

      (party_get_slot, ":conversation_scene", "$current_town", ":scene_slot_no"),
      (modify_visitors_at_site, ":conversation_scene"),
      (reset_visitors),
      (set_visitor, 0, "trp_player"),

      (try_begin),
        (gt, "$sneaked_into_town", disguise_none),
        (mission_tpl_entry_set_override_flags, "mt_conversation_encounter", 0, af_override_all),
        #SB : use script call
        (call_script, "script_set_disguise_override_items", "mt_conversation_encounter", 0, 0),
      (else_try),
        (mission_tpl_entry_set_override_flags, "mt_conversation_encounter", 0, af_override_horse),
        (mission_tpl_entry_clear_override_items, "mt_conversation_encounter", 0),
      (try_end),
      (party_get_slot, ":conversation_troop", "$current_town", ":troop_slot_no"),
      (set_visitor, ":entry_no", ":conversation_troop"),
      (set_jump_mission,"mt_conversation_encounter"),
      (jump_to_scene, ":conversation_scene"),
      (change_screen_map_conversation, ":conversation_troop"),
    ]),
    #talking to people outside the court (neutral, tc_castle_gate)

    ("start_courtyard_conversation",
    [
      (store_script_param, ":conversation_troop", 1),
      (store_script_param, ":center_no", 2),

      (party_get_slot, ":conversation_scene", ":center_no", slot_town_center), #castle's exterior
      (modify_visitors_at_site, ":conversation_scene"),
      (reset_visitors),
      (try_begin), #player vs troop, not much processing
        (neg|troop_is_hero, ":conversation_troop"),

      (else_try), #talking to lords, compare relative positions
        (assign, ":supplicant", "trp_player"),
        (store_faction_of_party, ":faction_no", ":center_no"),
        (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":faction_no"),
        (assign, ":player_standing", reg0),
        (call_script, "script_dplmc_get_troop_standing_in_faction", ":conversation_troop", ":faction_no"),
        (assign, ":other_troop_standing", reg0),

        #23 : castle guard (adjacent), 2: lord's hall door
        (assign, ":entry_lower", 23),
        (assign, ":entry_upper", 2),
        #overwrite standing if center owned
        (try_begin),
          (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (assign, ":player_standing", 9999),
        (else_try),
          (party_slot_eq, ":center_no", slot_town_lord, ":conversation_troop"),
          (assign, ":other_troop_standing", 9999),
        (else_try), #strangers, use default street entry point (this may be outside in towns, 0 preferred)
          (this_or_next|eq, ":player_standing", DPLMC_FACTION_STANDING_UNAFFILIATED),
          (eq, ":other_troop_standing", DPLMC_FACTION_STANDING_UNAFFILIATED),
          (assign, ":entry_lower", 1),
        (try_end),

        (try_begin), #player is usually supplicant
          (gt, ":player_standing", ":other_troop_standing"),
          (assign, ":supplicant", ":conversation_troop"),
          (assign, ":conversation_troop", "trp_player"),
        (else_try),
          (is_between, ":center_no", towns_begin, towns_end),
          (eq, ":player_standing", ":other_troop_standing"),
          (assign, ":entry_upper", 27),
          (assign, ":entry_lower", 28),
        (try_end),
      (try_end),

      (mission_tpl_entry_set_override_flags, "mt_conversation_encounter", ":entry_lower", af_override_horse|af_override_head|af_override_weapons),
      (mission_tpl_entry_set_override_flags, "mt_conversation_encounter", ":entry_upper", af_override_horse|af_override_fullhelm),
      (set_visitor, ":entry_lower", ":supplicant"),
      (set_visitor, ":entry_upper", ":conversation_troop"),

      (set_jump_mission,"mt_conversation_encounter"),
      (jump_to_scene, ":conversation_scene"),
      (change_screen_map_conversation, ":conversation_troop"),
    ]),

    #talking to people within the court (after capture for instance)
    ("start_court_conversation",
    [
        (store_script_param, ":conversation_troop", 1),
        (store_script_param, ":center_no", 2),

        (party_get_slot, ":conversation_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site, ":conversation_scene"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (mission_tpl_entry_set_override_flags, "mt_conversation_encounter", 0, af_override_horse),

        #clear flags for actual courtly conversations?
        (store_random_in_range, ":entry_no", 16, 32),
        (mission_tpl_entry_set_override_flags, "mt_conversation_encounter", ":entry_no", af_override_horse),
        (try_begin),
          (troop_is_hero, ":conversation_troop"),
          (set_visitor, ":entry_no", ":conversation_troop"),
        (else_try),
          (store_script_param, ":troop_dna", 3),
          (set_visitor, ":entry_no", ":conversation_troop", ":troop_dna"),
        (try_end),
        (set_jump_mission,"mt_conversation_encounter"),
        (jump_to_scene, ":conversation_scene"),
        (change_screen_map_conversation, ":conversation_troop"),
    ]),


    #script_companion_get_mission_string
    #input: companion troop_id
    #output: "{!}{s4}: {s8} ({s5})" to s0
    #unify the menu (rarely called) and troop notes for consistency
    #side-effects include overwriting s9, reg3, etc.
    ("companion_get_mission_string", [
        (store_script_param, ":companion", 1),
        (try_begin), #do not impose conditions here, do so from calling script
            # (this_or_next|main_party_has_troop, ":companion"),
            # (this_or_next|troop_slot_ge, ":companion", slot_troop_current_mission, 1),
                # (eq, "$g_player_minister", ":companion"),
            (str_store_troop_name, s4, ":companion"),
            (str_clear, s5),
            (str_clear, s8),
            (troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),
            (troop_get_slot, ":mission", ":companion", slot_troop_current_mission),
            (try_begin),
                (le, ":days_left", 0),
                (str_store_string, s5, "str_whereabouts_unknown"),
            (else_try),
                (eq, ":days_left", 1),
                (str_store_string, s5, "str_expected_back_imminently"),
            (else_try),
                (assign, reg3, ":days_left"),
                (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
            (try_end),


            (try_begin),
                (eq, ":mission", npc_mission_kingsupport),
                (str_store_string, s8, "str_gathering_support"),
            (else_try),
                (this_or_next|eq, ":mission", npc_mission_gather_intel),
                (eq, ":mission", dplmc_npc_mission_rescue_prisoner), #new mission
                (troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
                (str_store_party_name, s9, ":town_with_contacts"),
                (try_begin),
                  (eq, ":mission", npc_mission_gather_intel),
                  (str_store_string, s8, "str_gathering_intelligence"),
                (else_try),
                  (eq, ":mission", dplmc_npc_mission_rescue_prisoner),
                  (str_store_string, s8, "str_preparing_prison_break"),
                (try_end),
            (else_try),
                (this_or_next|is_between, ":mission", npc_mission_peace_request, npc_mission_rejoin_when_possible),
                (is_between, ":mission", dplmc_npc_mission_war_request, dplmc_npc_mission_rescue_prisoner),

                (troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
                (str_store_faction_name, s9, ":faction"),
                (str_store_string, s8, "str_diplomatic_embassy_to_s9"),
            # (else_try), #diplomacy missions

            (else_try),
                (eq, ":companion", "$g_player_minister"),
                (str_store_string, s8, "str_serving_as_minister"),
                (try_begin),
                  (is_between, "$g_player_court", centers_begin, centers_end),
                  (str_store_party_name, s9, "$g_player_court"),
                  (str_store_string, s5, "str_in_your_court_at_s9"),
                (else_try),
                  (str_store_string, s5, "str_awaiting_the_capture_of_a_fortress_which_can_serve_as_your_court"),
                (try_end),
            (else_try),
                (eq, ":mission", dplmc_npc_mission_delegate_quest),
                (str_store_string, s8, "str_npc_mission_delegate_quest"),
            (else_try),
                (eq, ":mission", npc_mission_rejoin_when_possible),
                (str_store_string, s8, "str_attempting_to_rejoin_party"),
            (else_try),
                (main_party_has_troop, ":companion"),
                (str_store_string, s8, "str_under_arms"),
                (str_store_string, s5, "str_in_your_party"),
            (else_try),    #Companions who are in a center
                (troop_slot_ge, ":companion", slot_troop_cur_center, centers_begin),
                (str_store_string, s8, "str_separated_from_party"),
                (str_store_string, s5, "str_whereabouts_unknown"),
            (else_try),    #Companions who are (imprisoned) in a center
                (troop_slot_ge, ":companion", slot_troop_prisoner_of_party, centers_begin),
                (str_store_string, s8, "str_missing_after_battle"),
                (str_store_string, s5, "str_whereabouts_unknown"),
            (else_try),
                (try_begin),
                    (check_quest_active, "qst_lend_companion"),
                    (quest_slot_eq, "qst_lend_companion", slot_quest_target_troop, ":companion"),
                    (quest_get_slot, ":lord", "qst_lend_companion", slot_quest_giver_troop),
                    (str_store_troop_name, s5, ":lord"),
                    (str_store_string, s8, "str_accompanying_s5"),
                    (str_store_string, s5, "str_on_loan"),
                (else_try),
                    (check_quest_active, "qst_lend_surgeon"),
                    (quest_slot_eq, "qst_lend_surgeon", slot_quest_target_troop, ":companion"),
                    (quest_get_slot, ":lord", "qst_lend_surgeon", slot_quest_giver_troop),
                    (str_store_troop_name, s5, ":lord"),
                    (str_store_string, s8, "str_accompanying_s5"),
                    (str_store_string, s5, "str_on_loan"),
                (try_end),
            (try_end),

            (str_store_string, s0, "str_s4_s8_s5"),
        (try_end),
        ]
      ),
    #iterates through list of obtainable soldiers (and check if the player has reclassified them to a custom class > grc_cavalry)
    #instead of going through all troops globally, we check the selected center's garrison's upgraded troops
        # (try_for_range, ":troop_no", soldiers_begin, soldiers_end),
          # (neg|troop_is_hero, ":troop_no"),
          # (troop_get_class, ":class", ":troop_no"),
          # ...
        # (try_end),
    ("cf_troop_class_activated",
    [
        (store_script_param, ":grc", 1),
        (store_script_param, ":party_no", 2),
        (is_between, ":grc", grc_infantry, grc_everyone),
        (try_begin), #first 3 always available
          (le, ":grc", grc_cavalry),
          (assign, ":end", -1),
        (else_try),
          (party_get_num_companion_stacks, ":end", ":party_no"),

          (try_for_range, ":stack_no", 0, ":end"),
            (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
            (neg|troop_is_hero, ":troop_no"),
            (try_begin),
              (troop_get_upgrade_troop, ":upgrade_troop", ":troop_no", 0),
              (call_script, "script_cf_troop_is_class", ":grc", ":upgrade_troop"),
              (assign, ":end", -1),
            (try_end),
            (try_begin), #not found, check other upgrade
              (neq, ":end", -1),
              (troop_get_upgrade_troop, ":upgrade_troop", ":troop_no", 1),
              (call_script, "script_cf_troop_is_class", ":grc", ":upgrade_troop"),
              (assign, ":end", -1),
            (try_end),
          (try_end),
        (try_end),
        (eq, ":end", -1),
    ]),

    ("cf_troop_is_class",
    [
        (store_script_param, ":grc", 1),
        (store_script_param, ":troop_no", 2),
        # (is_between, ":grc", grc_infantry, grc_everyone), #usually $g_constable_training_type
        (gt, ":troop_no", 0), #this is usually obtained through troop_get_upgrade_troop, sanitize it here
        #can do some tf_guarantee flag as well but usually game engine parse is fine
        (troop_get_class, ":class_no", ":troop_no"),
        (eq, ":grc", ":class_no"),
    ]),
    #script_dplmc_npc_morale
    ("dplmc_npc_morale",
      [
        (store_script_param_1, ":npc"),
        (store_script_param_2, ":mode"),
        (try_begin), #if we actually care
          (eq, ":mode", 1),
          (call_script, "script_npc_morale", ":npc"),
        (else_try), #we just want the numbers
          (troop_get_slot, ":morality_grievances", ":npc", slot_troop_morality_penalties),
          (troop_get_slot, ":personality_grievances", ":npc", slot_troop_personalityclash_penalties),
          (party_get_morale, ":party_morale", "p_main_party"),

          (store_sub, ":troop_morale", ":party_morale", ":morality_grievances"),
          (val_sub, ":troop_morale", ":personality_grievances"),
          (val_add, ":troop_morale", 50),

          # (assign, reg8, ":troop_morale"),

          (val_mul, ":troop_morale", 3),
          (val_div, ":troop_morale", 4),
          (val_clamp, ":troop_morale", 0, 100),
          (assign, reg0, ":troop_morale"),
        (try_end),
    ]),

    #script_build_background_answer_story
    #input: sreg, other info based off global background_answer variables
    #output: story to s0, side effects are reg11, s10 through s13
    ("build_background_answer_story", [
        (store_script_param_1, ":sreg"),
        (assign, reg11, "$character_gender"),
        (store_sub, ":string", "$background_answer_4", cb4_revenge),
        (val_add, ":string", "str_story_reason_revenge"),
        (str_store_string, s13, ":string"),
        (store_sub, ":string", "$background_answer_3", dplmc_cb3_bravo),
        (val_add, ":string", "str_story_job_bravo"),
        (str_store_string, s12, ":string"),
        (store_sub, ":string", "$background_answer_2", cb2_page), #values for this start from 0
        (val_add, ":string", "str_story_childhood_page"),
        (str_store_string, s11, ":string"),
        (store_sub, ":string", "$background_type", cb_noble),
        (val_add, ":string", "str_story_parent_noble"),
        (str_store_string, s10, ":string"),
        (str_store_string, ":sreg", "str_story_all"),
    ]),

    #whenever the player does something nice, spectators cheer
    ("agents_cheer_during_training", [
      (party_get_morale, ":cur_morale", "p_main_party"),
      (assign, ":boundary", 150),
    #first aid double-stacks since it's not a battle
      (try_for_agents, ":agent_no"),
        (agent_is_active, ":agent_no"),
        (agent_is_human, ":agent_no"),
        # (agent_get_troop_id, ":troop_no", ":agent_no"), #a spectator
        (neg|agent_has_item_equipped, ":agent_no", "itm_practice_boots"),
        (store_random_in_range, ":random_no", ":cur_morale", 250),
        (gt, ":random_no", ":boundary"),
        (val_add, ":boundary", 15),
        (agent_set_animation, ":agent_no", "anim_cheer"),
        (store_random_in_range, ":random_no", 0, 100),
        (agent_set_animation_progress, ":agent_no", ":random_no"),
      (try_end),
    ]),

    #a separate trigger handles when they're actually knocked out
    ("troop_set_training_health_from_agent", [
      (party_get_skill_level, ":first_aid", "p_main_party", "skl_first_aid"),
    #first aid double-stacks since it's not a battle
      (try_for_agents, ":agent_no"),
        # (agent_is_active, ":agent_no"),
        (agent_is_human, ":agent_no"),
        (agent_get_troop_id, ":troop_no", ":agent_no"),
        (troop_is_hero, ":troop_no"),
        (store_troop_health, ":health", ":troop_no", 0), #this is not yet deducted
        (store_agent_hit_points, ":hp", ":agent_no", 0),
        (val_sub, ":hp", ":health"), #this is the difference
        (try_begin),
          (agent_is_alive, ":agent_no"),
          (store_skill_level, ":skill", "skl_first_aid", ":troop_no"),
          (val_add, ":skill", ":first_aid"),
        (else_try),
          (assign, ":skill", ":first_aid"),
        (try_end),
        (val_mul, ":skill", -5),  #as per skill description
        (val_add, ":skill", 100), # 100 - skill effect
        #apply skill effect and set health
        (val_mul, ":hp", ":skill"),
        (val_div, ":hp", 100),
        (val_add, ":hp", ":health"), #subtract modified difference
        (troop_set_health, ":troop_no", ":hp", 0),
      (try_end),
    ]),

    #script_agent_apply_training_health
    #input: player_agent, called from abm_training during melee fights, can also be used for tournament if desired
    ("agent_apply_training_health", [
      (store_script_param_1, ":agent_no"),
      # (store_script_param_2, "$current_town"),

      (party_get_skill_level, ":first_aid", "p_main_party", "skl_first_aid"),
      (party_get_slot, ":relation", "$current_town", slot_center_player_relation), #range from -100 to 100
      (store_sub, ":relation", 200, ":relation"), #300 to 100

      (store_troop_health, ":health", "trp_player", 0), #this is not yet deducted
      (store_agent_hit_points, ":hp", ":agent_no", 0),

      (val_sub, ":hp", ":health"), #this is the difference (non-positive)
      (try_begin),
        (agent_is_alive, ":agent_no"),
        (store_skill_level, ":skill", "skl_first_aid", "trp_player"),
      (else_try),
        (assign, ":skill", 0),
      (try_end),
      (val_add, ":skill", ":first_aid"),
      (val_mul, ":skill", -5),  #as per skill description
      (val_add, ":skill", 100), # 100 - skill effect
      #apply skill effect, relation effect and set health
      (val_mul, ":hp", ":skill"),
      (val_div, ":hp", 100),
      (val_mul, ":hp", ":relation"),
      (val_div, ":hp", 200),
      (val_add, ":health", ":hp"), #subtract modified difference
      (val_max, ":health", 5),
      (troop_set_health, "trp_player", ":health", 0),
    ]),

    # script_party_heal_all_members_aux, opposite of script_party_wound_all_members_aux
    # Input: arg1 = party_no
    ("party_heal_all_members_aux",
      [
        (store_script_param_1, ":party_no"),

        (party_get_num_companion_stacks, ":num_stacks",":party_no"),
        (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            # (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
            (party_stack_get_num_wounded, ":stack_size",":party_no",":i_stack"),
            (party_add_members, ":party_no", ":stack_troop", ":stack_size"),
            (party_remove_members_wounded_first, ":party_no", ":stack_troop", ":stack_size"),
          (else_try),
            (troop_set_health, ":stack_troop", 100),
          (try_end),
        (try_end),
        (party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
          (party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
          (call_script, "script_party_heal_all_members_aux", ":attached_party"),
        (try_end),
      ]
    ),

  #script_cf_village_normal_cond
  # INPUT: none
  # OUTPUT: none
  ("cf_village_normal_cond",
    [
    (store_script_param, ":party_no", 1),
    (neg|party_slot_eq, ":party_no", slot_village_state, svs_looted),
    (neg|party_slot_eq, ":party_no", slot_village_state, svs_deserted), #SB : addition here
    (neg|party_slot_eq, ":party_no", slot_village_state, svs_being_raided),
    (neg|party_slot_ge, ":party_no", slot_village_infested_by_bandits, 1),
    ]
  ),

    #script_cf_has_companion_emissary for diplomatic options
  ("cf_has_companion_emissary",
    [
    (assign, ":companion_found", companions_end),
    (try_for_range, ":emissary", companions_begin, companions_end),
      (main_party_has_troop, ":emissary"),
      (assign, ":companion_found", companions_begin),
    (try_end),
    (neq, ":companion_found", companions_end),
    ]),
    
    #script_cf_troop_can_autoloot for autoloot selection, usually companion but can be spouse as well
  ("cf_troop_can_autoloot",
    [
    (store_script_param, ":stack_troop", 1),
    (is_between, ":stack_troop", heroes_begin, heroes_end), #SB : change this range, allow spoues
    (this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":stack_troop"),
    (this_or_next|troop_slot_eq, ":stack_troop", slot_troop_spouse, "trp_player"),
    (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_player_companion),
    # (main_party_has_troop, ":stack_troop"),
    ]),

  #script_get_chest_troop fetches the appropriate placeholder for player storage
  # INPUT: center, usually $current_town
  # OUTPUT: none
  ("get_chest_troop",
  [
    (store_script_param, ":party_no", 1),
    (try_begin),
        (gt, "$g_player_chamberlain", 0),
        (assign, ":chest_troop", "trp_household_possessions"),
    (else_try), #assume troops same order as parties
        # (party_get_slot, ":chest_troop", ":party_no", slot_town_seneschal),
        (val_sub, ":party_no", towns_begin),
        (store_add, ":chest_troop", ":party_no", "trp_town_1_seneschal"),
    (try_end),
    (assign, reg0, ":chest_troop"),
  ]),

	#script_change_faction_troop_morale
	#input - faction, change, display mode
	#output - a colored message
	("change_faction_troop_morale",
	  [(store_script_param, ":faction_no", 1),
	   (store_script_param, ":morale_change", 2),
	   (store_script_param, ":display", 3),
	   (try_begin),
		 (eq, ":display", 1),
		 (neg|faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
		 (assign, ":display", 0),
	   (try_end),
	   #check if main party has troop of type before displaying
	   (try_begin),
		 (eq, ":display", 1),
		 (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
		 (try_for_range, ":stack", 1, ":num_stacks"),
		   (party_stack_get_troop_id, ":troop", "p_main_party", ":stack"),
		   (neg|troop_is_hero, ":troop"),
		   (store_troop_faction, ":fac", ":troop"),
		   (eq, ":fac", ":faction_no"),
		   (assign, ":num_stacks", 1), #break
		 (try_end),
		 (neq, ":num_stacks", 1), #none found
		 (assign, ":display", 0),
	   (try_end),
	   #effects are still applied regardless - the displayed morale is divided by 100
	   (faction_get_slot, ":morale", ":faction_no", slot_faction_morale_of_player_troops),
	   (store_div, reg1, ":morale", 100),
	   (val_add, ":morale", ":morale_change"),
	   (store_div, reg2, ":morale", 100),
	   (faction_set_slot, ":faction_no", slot_faction_morale_of_player_troops, ":morale"),

	   # (try_begin),
		 # (store_sub, ":diff", reg2, reg1),
		 # (eq, ":diff", 0), #negligible
		 # (assign, ":display", 0),
	   # (try_end),

	   #actual output
	   (try_begin),
		 (eq, ":display", 1),
         (neq, reg1, reg2), #non-zero difference
		 #set up s1
		 (faction_get_slot, ":adjective", ":faction_no", slot_faction_adjective),
		 (str_store_string, s1, ":adjective"),
		 (str_store_string, s1, "@{s1} troops"),
		 #get increase/decrease, either string will work
		 (assign, ":string", "str_troop_relation_detoriated"),
		 (try_begin),
		   (gt, ":morale_change", 0),
		   (assign, ":string", "str_troop_relation_increased"),
		 (try_end),
		 #get color
		 (faction_get_color, ":color", ":faction_no"),
		 (display_message, ":string", ":color"),
	   (try_end),
	  ]
	),

    #script_encounter_agent_draw_weapon
    #input: none, based on $g_talk_agent
    #output: none, agent wields first available weapon to show aggression
    ("encounter_agent_draw_weapon",
    [
        (store_conversation_agent, "$g_talk_agent"),
        (try_begin),
          (agent_get_item_slot, ":item_no", "$g_talk_agent", ek_item_0),
          (gt, ":item_no", 0),
          (agent_set_wielded_item, "$g_talk_agent", ":item_no"),
        (try_end),

    ]),

    #script_troop_debug_range
    #input: troop, head or tail, sreg
    #output: reg0 as head or tail, sreg holding a short description
    ("cf_troop_debug_range",
    [
        (store_script_param, ":troop_no", 1),
        (store_script_param, ":sreg", 2),
        (store_script_param, ":direction", 3),
        (assign, ":result", ":troop_no"),
        (try_begin),
          (is_between, ":troop_no", heroes_begin, heroes_end),
          (str_store_string, ":sreg", "@hero"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", heroes_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", heroes_end, ":direction"),
          (try_end),
          (try_begin),
            (is_between, ":troop_no", companions_begin, companions_end),
            (str_store_string, ":sreg", "@companion"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", companions_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", companions_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", kings_begin, kings_end),
            (str_store_string, ":sreg", "@king"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", kings_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", kings_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", lords_begin, lords_end),
            (str_store_string, ":sreg", "@lord"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", lords_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", lords_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", pretenders_begin, pretenders_end),
            (str_store_string, ":sreg", "@pretender"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", pretenders_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", pretenders_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
            (str_store_string, ":sreg", "@lady"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", kingdom_ladies_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", kingdom_ladies_end, ":direction"),
            (try_end),
          (try_end),
        (else_try),
          (is_between, ":troop_no", bandits_begin, bandits_end),
          (str_store_string, ":sreg", "@bandit"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", bandits_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", bandits_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", tavern_minstrels_begin, tavern_minstrels_end),
          (str_store_string, ":sreg", "@minstrel"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", tavern_minstrels_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", tavern_minstrels_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", tavern_booksellers_begin, tavern_booksellers_end),
          (str_store_string, ":sreg", "@bookseller"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", tavern_booksellers_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", tavern_booksellers_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", tavern_travelers_begin, tavern_travelers_end),
          (str_store_string, ":sreg", "@traveler"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", tavern_travelers_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", tavern_travelers_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", ransom_brokers_begin, ransom_brokers_end),
          (str_store_string, ":sreg", "@ransom broker"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", ransom_brokers_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", ransom_brokers_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", mercenary_troops_begin, mercenary_troops_end),
          (str_store_string, ":sreg", "@mercenary"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", mercenary_troops_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", mercenary_troops_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", multiplayer_ai_troops_begin, multiplayer_troops_end),
          (str_store_string, ":sreg", "@multiplayer troop"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", multiplayer_ai_troops_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", multiplayer_troops_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", quick_battle_troops_begin, quick_battle_troops_end),
          (str_store_string, ":sreg", "@quick battler"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", quick_battle_troops_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", quick_battle_troops_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", training_ground_trainers_begin, training_ground_trainers_end),
          (str_store_string, ":sreg", "@trainer"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", training_ground_trainers_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", training_ground_trainers_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", arena_masters_begin, arena_masters_end),
          (str_store_string, ":sreg", "@arena master"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", arena_masters_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", arena_masters_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", walkers_begin, walkers_end),
          (str_store_string, ":sreg", "@walker"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", walkers_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", walkers_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", merchants_begin, merchants_end),
          (str_store_string, ":sreg", "@merchant"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", merchants_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", merchants_end, ":direction"),
          (try_end),
          (try_begin),
            (is_between, ":troop_no", armor_merchants_begin, armor_merchants_end),
            (str_store_string, ":sreg", "@armor merchant"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", armor_merchants_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", armor_merchants_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", weapon_merchants_begin, weapon_merchants_end),
            (str_store_string, ":sreg", "@weapon merchant"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", weapon_merchants_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", weapon_merchants_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", tavernkeepers_begin, tavernkeepers_end),
            (str_store_string, ":sreg", "@tavernkeeper"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", tavernkeepers_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", tavernkeepers_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", goods_merchants_begin, goods_merchants_end),
            (str_store_string, ":sreg", "@goods merchant"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", goods_merchants_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", goods_merchants_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", horse_merchants_begin, horse_merchants_end),
            (str_store_string, ":sreg", "@horse merchant"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", horse_merchants_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", horse_merchants_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", mayors_begin, mayors_end),
            (str_store_string, ":sreg", "@guildmaster"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", mayors_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", mayors_end, ":direction"),
            (try_end),
          (else_try),
            (is_between, ":troop_no", village_elders_begin, village_elders_end),
            (str_store_string, ":sreg", "@village elder"),
            (try_begin),
              (eq, ":direction", -1),
              (assign, ":result", village_elders_begin),
            (else_try),
              (eq, ":direction", 1),
              (store_sub, ":result", village_elders_end, ":direction"),
            (try_end),
          (try_end),
        (else_try),
          (is_between, ":troop_no", startup_merchants_begin, startup_merchants_end),
          (str_store_string, ":sreg", "@startup merchant"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", startup_merchants_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", startup_merchants_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", tournament_champions_begin, tournament_champions_end),
          (str_store_string, ":sreg", "@tournament fighter"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", tournament_champions_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", tournament_champions_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", craftsman_begin, craftsman_end),
          (str_store_string, ":sreg", "@craftsman"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", craftsman_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", craftsman_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", "trp_town_1_seneschal", arena_masters_begin),
          (str_store_string, ":sreg", "@court chests"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_town_1_seneschal"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", arena_masters_begin, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", "trp_zendar_chest", "trp_local_merchant"),
          (str_store_string, ":sreg", "@chest or array"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_zendar_chest"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_local_merchant", ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", "trp_log_array_entry_type", quick_battle_troops_begin),
          (str_store_string, ":sreg", "@log array"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_log_array_entry_type"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", quick_battle_troops_begin, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", "trp_local_merchant", "trp_quick_battle_6_player"),
          (str_store_string, ":sreg", "@quest troop"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_local_merchant"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_quick_battle_6_player", ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", multiplayer_coop_class_templates_begin, multiplayer_coop_companion_equipment_sets_end),
          (str_store_string, ":sreg", "@coop troop"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", multiplayer_coop_class_templates_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", multiplayer_coop_companion_equipment_sets_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", dplmc_employees_begin, dplmc_employees_end),
          (str_store_string, ":sreg", "@court member"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", dplmc_employees_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", dplmc_employees_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", fighters_begin, fighters_end),
          (str_store_string, ":sreg", "@fighter"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", fighters_begin),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", fighters_end, ":direction"),
          (try_end),
        (else_try),
          (is_between, ":troop_no", "trp_tutorial_fighter_1", startup_merchants_begin),
          (str_store_string, ":sreg", "@tutorial fighter"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_tutorial_fighter_1"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", startup_merchants_begin, ":direction"),
          (try_end),
        (else_try), #sarranids
          (is_between, ":troop_no", "trp_sarranid_recruit", "trp_looter"),
          (str_store_string, ":sreg", "str_kingdom_6_adjective"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_sarranid_recruit"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_looter", ":direction"),
          (try_end),
        (else_try), #rhodoks
          (is_between, ":troop_no", "trp_rhodok_tribesman", "trp_sarranid_recruit"),
          (str_store_string, ":sreg", "str_kingdom_5_adjective"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_rhodok_tribesman"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_sarranid_recruit", ":direction"),
          (try_end),
        (else_try), #nords
          (is_between, ":troop_no", "trp_nord_recruit", "trp_rhodok_tribesman"),
          (str_store_string, ":sreg", "str_kingdom_4_adjective"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_nord_recruit"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_rhodok_tribesman", ":direction"),
          (try_end),
        (else_try), #khergits
          (is_between, ":troop_no", "trp_khergit_tribesman", "trp_nord_recruit"),
          (str_store_string, ":sreg", "str_kingdom_3_adjective"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_khergit_tribesman"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_nord_recruit", ":direction"),
          (try_end),
        (else_try), #vaegirs
          (is_between, ":troop_no", "trp_vaegir_recruit", "trp_khergit_tribesman"),
          (str_store_string, ":sreg", "str_kingdom_2_adjective"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_vaegir_recruit"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_khergit_tribesman", ":direction"),
          (try_end),
        (else_try), #swadians
          (is_between, ":troop_no", "trp_swadian_recruit", "trp_vaegir_recruit"),
          (str_store_string, ":sreg", "str_kingdom_1_adjective"),
          (try_begin),
            (eq, ":direction", -1),
            (assign, ":result", "trp_swadian_recruit"),
          (else_try),
            (eq, ":direction", 1),
            (store_sub, ":result", "trp_vaegir_recruit", ":direction"),
          (try_end),
        (try_end),
        (this_or_next|eq, ":direction", 0),
        (neq, ":result", ":troop_no"),
        (assign, reg0, ":result"),

    ]),

    #script_get_proficient_melee_training_weapon
    #input : troop_no
    #output : item_no as the practice weapon
    ("get_proficient_melee_training_weapon",
    [
        (store_script_param, ":troop_no", 1),
        (store_proficiency_level, ":onehands", ":troop_no", wpt_one_handed_weapon),
        (store_proficiency_level, ":twohands", ":troop_no", wpt_two_handed_weapon),
        (store_proficiency_level, ":polearms", ":troop_no", wpt_polearm),

        (assign, ":item_no", -1),
        (assign, ":item_shield", -1),
        (try_begin), #practice shield will be added automatically
          (ge, ":onehands", ":twohands"),
          (ge, ":onehands", ":polearms"),
          # (agent_equip_item, ":agent_no", "itm_practice_shield"),
          (assign, ":item_no", "itm_practice_sword"),
          (assign, ":item_shield", "itm_practice_shield"),
        (else_try),
          (ge, ":twohands", ":onehands"),
          (ge, ":twohands", ":polearms"),
          (assign, ":item_no", "itm_heavy_practice_sword"),
        (else_try),
          (ge, ":polearms", ":onehands"),
          (ge, ":polearms", ":twohands"),
          (assign, ":item_no", "itm_practice_staff"),
        (try_end),
        (assign, reg0, ":item_no"),
        (assign, reg1, ":item_shield"),
    ]),

  # script_spawn_looters
  # Input: arg1 = center_no, arg2 = number of looters to spawn
  # Output: none
  ("spawn_looters",
    [
      (store_script_param, ":center_no", 1),
      (store_script_param, ":num_looters", 2),
      # (party_set_slot, ":center_no", slot_center_is_besieged_by, -1), #clear siege
      # (call_script, "script_village_set_state",  ":center_no", 0), #clear siege flag
      (set_spawn_radius, 4),
      (try_for_range, ":unused", 0, ":num_looters"),
        (spawn_around_party, ":center_no", "pt_looters"),
        (party_set_ai_behavior, reg0, ai_bhvr_avoid_party),
        (party_set_ai_object, reg0, ":center_no"),
        (party_set_slot, reg0, slot_party_home_center, ":center_no"),
      (try_end),
    ]),

  #script_troop_transfer_gold
  ("troop_transfer_gold",
    [
      (store_script_param, ":source", 1),
      (store_script_param, ":destination", 2),
      (store_script_param, ":amount", 3),
      (store_troop_gold, ":cur_amount", ":source"),
      (try_begin),
        (gt, ":amount", 0), #0 means move all
        (val_min, ":cur_amount", ":amount"),
      (try_end),
      (troop_remove_gold, ":source", ":cur_amount"),
      # (troop_add_gold, ":destination", ":cur_amount"),
      (call_script, "script_troop_add_gold", ":destination", ":cur_amount"),
      (assign, reg0, ":cur_amount"),
    ]),
  # script_move_inventory_and_gold
  # generally this is used to move the backup to the player
  # Input: arg1 = source, arg2 = destnation
  # Output: none

  ("move_inventory_and_gold",
    [
      (store_script_param, ":source", 1),
      (store_script_param, ":destination", 2),
      (store_script_param, ":move_gold", 3),
      #assume trp_temp_troop is an available placeholder

      (troop_sort_inventory, ":source"), #order them, too lazy to maintain 2 loops
      (troop_get_inventory_capacity, ":inv_cap", ":source"),
      (troop_get_inventory_capacity, ":player_cap", ":destination"),
      (assign, ":inv_slot", ek_food + 1), #start from the bottom, skip source's equipment
      (try_for_range, ":i_slot", ek_food + 1, ":player_cap"),
        (troop_get_inventory_slot, ":cur_item", ":destination", ":i_slot"),
        (eq, ":cur_item", -1), #empty slot
        (troop_get_inventory_slot, ":item", ":source", ":inv_slot"),
        (troop_set_inventory_slot, ":destination", ":i_slot", ":item"),
        (try_begin),
          (neq, ":item", -1),
          (troop_get_inventory_slot_modifier, ":imod", ":source", ":inv_slot"),
          (troop_set_inventory_slot_modifier, ":destination", ":i_slot", ":imod"),
          (try_begin),
            (troop_inventory_slot_get_item_amount, ":amount", ":source", ":inv_slot"),
            (gt, ":amount", 0),
            (troop_inventory_slot_set_item_amount, ":destination", ":i_slot", ":amount"),
          (try_end),
        (try_end),
        (troop_set_inventory_slot, ":source", ":inv_slot", -1),
        (val_add, ":inv_slot", 1),

        (try_begin), #loop break
          (ge, ":inv_slot", ":inv_cap"),
          (assign, ":player_cap", -1),
        (try_end),
      (try_end),
      (troop_clear_inventory, ":source"), #clear off the rest if no capacity in destination
      #do gold addition
      (try_begin),
        (eq, ":move_gold", -1), #move all
        (store_troop_gold, ":cur_amount", ":source"),
        (troop_remove_gold, ":source", ":cur_amount"),
        (troop_add_gold, ":destination", ":cur_amount"),
      (else_try),
        (gt, ":move_gold", 0),  #specific amount
        (call_script, "script_troop_transfer_gold", ":source", ":destination", ":move_gold"),
      (try_end),
    ]),
   #script_get_disguise_string
   #calculate the string offset by iteratively dividing by 2
   ("get_disguise_string", [
      (store_script_param, ":cur_val", 1),
      (store_script_param, ":sreg", 2),
      (store_add, ":end_val", "str_pilgrim_disguise", num_disguises),
      (str_clear, ":sreg"),
      (try_for_range, ":string", "str_pilgrim_disguise", ":end_val"),
        (eq, ":cur_val", 1), #
        (assign, ":end_val", -1), #loop break
        (str_store_string, ":sreg", ":string"),
      (else_try),
        (val_div, ":cur_val", 2), #divide by 2, next iteration
      (try_end),
      ]),
   #script_acquire_disguise
   #lets the player use the disguise by setting the slot, shows message
   ("acquire_disguise", [
      (store_script_param, ":disguise", 1),
      (troop_get_slot, ":cur_disguise", "trp_player", slot_troop_player_disguise_sets),
      (store_and, ":has_disguise", ":cur_disguise", ":disguise"),
      (val_or, ":cur_disguise", ":disguise"),
      (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, ":cur_disguise"),
      (try_begin), #suppress
        (eq, ":has_disguise", 0),
        (call_script, "script_get_disguise_string", ":disguise", 0),
        (display_message, "@Acquired {s0}'s clothing", message_alert),
      (try_end),
      ]),
   #script_set_disguise_overide_items
   #see also start of module_mission_templates for static list of items
   #note that the override flags are not being set here
   ("set_disguise_override_items", [
      (store_script_param, ":mission_template", 1),
      (store_script_param, ":entry_no", 2),
      (store_script_param, ":with_weapon", 3),

      (mission_tpl_entry_clear_override_items, ":mission_template", ":entry_no"),
      (try_begin),
        (eq, "$sneaked_into_town", disguise_pilgrim),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_pilgrim_disguise"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_pilgrim_hood"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_wrapping_boots"),
        (try_begin),
          (eq, ":with_weapon", 1),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_practice_staff"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_throwing_daggers"),
        (try_end),
      (else_try),
        (eq, "$sneaked_into_town", disguise_farmer),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_felt_hat"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_coarse_tunic"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_nomad_boots"),
        (try_begin),
          (eq, ":with_weapon", 1),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_battle_fork"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_cleaver"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_stones"),
        (try_end),
      (else_try),
        (eq, "$sneaked_into_town", disguise_hunter),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_black_hood"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_leather_gloves"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_light_leather"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_light_leather_boots"),
        (try_begin),
          (eq, ":with_weapon", 1),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_sword_khergit_1"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_hunting_bow"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_barbed_arrows"),
        (try_end),
      (else_try),
        (eq, "$sneaked_into_town", disguise_merchant),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_leather_jacket"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_woolen_hose"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_felt_steppe_cap"),
        (try_begin),
          (eq, ":with_weapon", 1),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_dagger"),
        (try_end),
      (else_try),
        (eq, "$sneaked_into_town", disguise_guard),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_footman_helmet"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_mail_mittens"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_mail_shirt"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_leather_jerkin"), #dckplmc
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_mail_chausses"),
        (try_begin),
          (eq, ":with_weapon", 1),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_fighting_pick"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_tab_shield_round_c"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_war_spear"),
        (try_end),
      (else_try),
        (eq, "$sneaked_into_town", disguise_bard),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_linen_tunic"),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_leather_boots"),
        (try_begin),
          (eq, ":with_weapon", 1),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_winged_mace"),
          (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", "itm_lyre"),
        (try_end),
      (try_end),
   ]),

   #script_set_companion_civilian_clothing_override
   #for use in script_enter_court where they might be missing clothing
   #note that the override flags are not being set here
   ("set_companion_civilian_clothing_override", [
      (store_script_param, ":mission_template", 1),
      (store_script_param, ":entry_no", 2),
      (store_script_param, ":troop_no", 3),

      (mission_tpl_entry_clear_override_items, ":mission_template", ":entry_no"), #af_castle_lord = af_override_horse|af_override_weapons|af_require_civilian
      (try_for_range, ":slot_no", dplmc_ek_alt_items_end, dplmc_ek_alt_items_end),
        (troop_get_inventory_slot, ":item_no", ":troop_no", ":slot_no"),
        (gt, ":item_no", 0),
        # (neg|item_has_property, ":item_no", itp_civilian),
        (try_begin),
          (ge, "$cheat_mode", 1),
          (str_store_item_name, s1, ":item_no"),
          (display_message, "@adding {s1} to entry"),
        (try_end),
        (mission_tpl_entry_add_override_item, ":mission_template", ":entry_no", ":item_no"),
      (try_end),
   ]),

    ("get_dest_color_from_rgb",
    [
      (store_script_param, ":red", 1),
      (store_script_param, ":green", 2),
      (store_script_param, ":blue", 3),

      (assign, ":cur_color", 0xFF000000),
      (val_mul, ":green", 0x100),
      (val_mul, ":red", 0x10000),
      (val_add, ":cur_color", ":blue"),
      (val_add, ":cur_color", ":green"),
      (val_add, ":cur_color", ":red"),
      (assign, reg0, ":cur_color"),
    ]),

    ("convert_rgb_code_to_html_code",
    [
      (store_script_param, ":red", 1),
      (store_script_param, ":green", 2),
      (store_script_param, ":blue", 3),

      # (str_store_string, s0, "@#"),

      (store_div, ":dest_string", ":red", 0x10),
      (val_add, ":dest_string", "str_key_0"),
      (str_store_string, s11, ":dest_string"),
      (store_mod, ":dest_string", ":red", 0x10),
      (val_add, ":dest_string", "str_key_0"),
      (str_store_string, s12, ":dest_string"),
      (store_div, ":dest_string", ":green", 0x10),
      (val_add, ":dest_string", "str_key_0"),
      (str_store_string, s13, ":dest_string"),
      (store_mod, ":dest_string", ":green", 0x10),
      (val_add, ":dest_string", "str_key_0"),
      (str_store_string, s14, ":dest_string"),
      (store_div, ":dest_string", ":blue", 0x10),
      (val_add, ":dest_string", "str_key_0"),
      (str_store_string, s15, ":dest_string"),
      (store_mod, ":dest_string", ":blue", 0x10),
      (val_add, ":dest_string", "str_key_0"),
      (str_store_string, s16, ":dest_string"),
      (str_store_string, s0, "str_html_color"),
    ]),

    ("convert_slot_no_to_color",
    [
      (store_script_param, ":cur_color", 1),

      (store_mod, ":blue", ":cur_color", 6),
      (val_div, ":cur_color", 6),
      (store_mod, ":green", ":cur_color", 6),
      (val_div, ":cur_color", 6),
      (store_mod, ":red", ":cur_color", 6),
      (val_mul, ":blue", 0x33),
      (val_mul, ":green", 0x33),
      (val_mul, ":red", 0x33),
      (assign, ":dest_color", 0xFF000000),
      (val_mul, ":green", 0x100),
      (val_mul, ":red", 0x10000),
      (val_add, ":dest_color", ":blue"),
      (val_add, ":dest_color", ":green"),
      (val_add, ":dest_color", ":red"),
      (assign, reg0, ":dest_color"),
    ]),

    ("change_color",
    [
      (call_script, "script_get_dest_color_from_rgb", reg2, reg3, reg4),
      (assign, ":cur_color", reg0),
      (overlay_set_color, "$g_presentation_obj_2", ":cur_color"),
      (try_begin),
        (eq, "$g_presentation_state", recolor_kingdom),
        (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
        (faction_set_color, ":cur_faction", ":cur_color"),
      (else_try), #exclusively for player for now
        (eq, "$g_presentation_state", recolor_heraldic),
        (troop_get_slot, ":banner", "$g_player_troop", slot_troop_banner_scene_prop),
        (val_sub, ":banner", banner_scene_props_begin),
        (troop_set_slot, "trp_banner_background_color_array", ":banner", ":cur_color"),
      (else_try),
        (eq, "$g_presentation_state", recolor_groups),
        (troop_set_slot, "trp_multiplayer_data", "$temp", ":cur_color"),
      (try_end),
      (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
      (overlay_set_text, "$g_presentation_obj_9", "str_html"),
    ]),
    #INVASION MODE START
    # script_multiplayer_ccoop_prepare_spawn_wave
    # Input: none
    # Output: none
    ("multiplayer_ccoop_prepare_spawn_wave",
    [
        (try_begin),
            (multiplayer_is_server),
            (set_fixed_point_multiplier, 100),

            #generate next wave spawn points
            (store_random_in_range, ":spawn_point1", 80, 88),
            (store_random_in_range, ":spawn_point2", 80, 88),
            (try_begin),
                (eq, ":spawn_point1", ":spawn_point2"),
                (assign, ":spawn_point2", -1),
            (end_try),

            #(assign, reg0, ":spawn_point1"),
            #(assign, reg1, ":spawn_point2"),
            #(display_message, "@spawn points generated as 1: {reg0} 2: {reg1}"),

            #(store_mod, ":wave_no_mod", "$g_multiplayer_ccoop_wave_no", 10),
            (store_sub, ":wave_no_mod", "$g_multiplayer_ccoop_wave_no", "$g_mp_coop_last_king_wave"),

            #Now the script makes a calculation to decide how many enemies to spawn.

            (assign, ":num_troops_for_wave", 4),
            (assign, ":number_of_players_at_team_1", 0),
            (get_max_players, ":num_players"),
            (try_for_range, ":cur_player", 0, ":num_players"),
                (player_is_active, ":cur_player"),
                (player_get_team_no, ":player_team", ":cur_player"),
                (eq, ":player_team", 0),
                (val_add, ":number_of_players_at_team_1", 1),
            (try_end),









            (assign, reg0, ":number_of_players_at_team_1"), #debug, delete

            (val_sub, ":number_of_players_at_team_1", 1), # for simplifying the formula
            (try_for_range, ":cur_multiplier", 1, 4),
                (gt, ":number_of_players_at_team_1", 0),
                (store_mul, ":used_multiplier", ":cur_multiplier", 2),
                (val_min, ":used_multiplier", ":number_of_players_at_team_1"),
                (val_sub, ":number_of_players_at_team_1", ":used_multiplier"),
                (store_sub, ":used_multiplier_2", 5, ":cur_multiplier"),
                (store_mul, ":added_num_troops", ":used_multiplier_2", ":used_multiplier"),
                (val_add, ":num_troops_for_wave", ":added_num_troops"),
            (try_end),

            (try_begin),
                (le, "$g_multiplayer_ccoop_wave_no", 3),
                (assign, ":spawn_point2", -1), # for the first 3 waves, spawn from only 1 point
            (try_end),

            #Clear all enemy wave data slots
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 1, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 2, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 3, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 4, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 5, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 6, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 7, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 8, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 9, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 10, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 11, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 12, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 13, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 14, 0),
            (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 15, 0),






            (store_mul, ":wave_effect_on_troops", 20, ":wave_no_mod"),
            (val_add, ":wave_effect_on_troops", 80), # it will be 100, 120, 140, 160, ... beginning from wave 1.

            (val_mul, ":num_troops_for_wave", ":wave_effect_on_troops"),
            (val_div, ":num_troops_for_wave", 100),

            (try_begin),
                (ge, "$g_mp_coop_king_waves", 1), # wave++
                (val_mul, ":num_troops_for_wave", 130),
                (val_div, ":num_troops_for_wave", 100),
            (try_end),








            #Used to reset max enemy level counter for endless mode
            (store_sub, ":since_last_boss", "$g_multiplayer_ccoop_wave_no", "$g_mp_coop_last_king_wave"),

            #Restrict the level of wave troops
            (try_begin),
              (ge, ":since_last_boss", 10),
              (assign, ":max_level", 30),
            (else_try),
              (ge, ":since_last_boss", 8),
              (assign, ":max_level", 24),
            (else_try),
              (ge, ":since_last_boss", 6),
              (assign, ":max_level", 20),
            (else_try),
              (ge, ":since_last_boss", 4),
              (assign, ":max_level", 15),
            (else_try),
              (ge, ":since_last_boss", 2),
              (assign, ":max_level", 10),
            (else_try),
              (ge, ":since_last_boss", 1),
              (assign, ":max_level", 6),
            (try_end),

            (assign, ":spawn_lord", 0),








            (assign, "$g_ccoop_king_troop", -1),

            (try_begin),
              (ge, ":since_last_boss", 3),
              (store_random_in_range, ":spawn_lord_check", 0, 2),  #after wave 3, 50% chance for a lord wave
              (this_or_next|ge, ":spawn_lord_check", 1),
              (this_or_next|eq, ":since_last_boss", 3),  #always spawn a lord on wave 3
              (eq, ":since_last_boss", 10), #king always spawns on wave 10
              (val_add, "$g_mp_coop_lord_waves", 1),
              (try_begin),
                (store_mod, ":spawn_king", "$g_mp_coop_lord_waves", 5), #If 5th lord wave occurs before wave 10, it become the king wave
                (this_or_next|eq, ":spawn_king", 0),
                (eq, ":since_last_boss", 10),
                (gt, "$g_mp_coop_lord_waves", 0), #prevents first lord wave from being a king wave
                (gt, ":since_last_boss", 1), #not necessary

                (try_begin),
                  (eq, "$g_multiplayer_team_2_faction", "fac_ccoop_all_stars"),
                  (store_random_in_range, ":used_troop_no", kings_begin, kings_end), #all stars faction uses a random king!
                (else_try),
                  (eq, "$g_multiplayer_team_2_faction", "fac_outlaws"),
                  (assign, ":reusing_quick_battle_king", 1),
                  (try_for_range, ":unused", 0, 10),
                    (eq, ":reusing_quick_battle_king", 1),
                    (store_random_in_range, ":used_troop_no" ,quick_battle_troops_begin, quick_battle_troops_end), #outlaws wave uses a quick battle troop for a king
                    (neg|troop_slot_eq, ":used_troop_no", slot_troop_coop_lord_spawned, 2), #it tries 10 times not to use one of the lords but if it fails, gives up eventually, and raises one from the dead
                    (assign, ":reusing_quick_battle_king", 0),
                  (try_end),
                (else_try),
                  (try_for_range, ":cur_troop", kings_begin, kings_end), #selects the right king for the faction
                      (store_troop_faction, ":troop_faction", ":cur_troop"),
                      (eq, ":troop_faction", "$g_multiplayer_team_2_faction"),
                      (assign, ":used_troop_no", ":cur_troop"),
                  (try_end),
                (try_end),
                #(assign, ":cur_max_level", 0),
                (assign, ":spawn_lord", 1),
                (assign, "$g_ccoop_king_troop", ":used_troop_no"),





                #Reset all spawn trackers to allow any lords to spawn again for each elite tier in endless mode
                (try_for_range, ":cur_troop", lords_begin, lords_end),
                  (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 0),
                (try_end),
                (try_for_range, ":cur_troop", quick_battle_troops_begin, quick_battle_troops_end),
                  (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 0),
                (try_end),
              (else_try),
                (assign, ":spawn_lord", 1), #variable is used to keep slots safe while generating the rest of the wave

                #reset data for all possible lord troops before generating a lord

                (try_for_range, ":cur_troop", lords_begin, lords_end),
                  (neg|troop_slot_eq, ":cur_troop", slot_troop_coop_lord_spawned, 2), #if slot_troop_coop_lord_spawned = 2, lord has already spawned - do not reset data
                  (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 0),
                (try_end),

                (try_for_range, ":cur_troop", quick_battle_troops_begin, quick_battle_troops_end),
                  (neg|troop_slot_eq, ":cur_troop", slot_troop_coop_lord_spawned, 2),
                  (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 0),
                (try_end),

                (assign, ":eligible_troop_count", 0),

                #Find troops that are eligible
                (try_for_range, ":cur_troop", lords_begin, lords_end),
                    (store_troop_faction, ":troop_faction", ":cur_troop"),
                    (this_or_next|eq, ":troop_faction", "$g_multiplayer_team_2_faction"),
                    (eq, "$g_multiplayer_team_2_faction", "fac_ccoop_all_stars"), #all lords are eligible in all stars
                    (neg|troop_slot_eq, ":cur_troop", slot_troop_coop_lord_spawned, 2), #don't resurrect lords (until a king wave)
                    (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 1), #set eligible to be checked the second time around
                    (val_add, ":eligible_troop_count", 1), #increase the upper limit for the random generator
                (try_end),

                (try_for_range, ":cur_troop", quick_battle_troops_begin, quick_battle_troops_end),
                    (store_troop_faction, ":troop_faction", ":cur_troop"),
                    (this_or_next|eq, "$g_multiplayer_team_2_faction", "fac_outlaws"),
                    (eq, "$g_multiplayer_team_2_faction", "fac_ccoop_all_stars"), #all quick battle troops are eligible in all stars
                    (neg|troop_slot_eq, ":cur_troop", slot_troop_coop_lord_spawned, 2), #don't resurrect quick battle troops (until a king wave)
                    (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 1),
                    (val_add, ":eligible_troop_count", 1),
                (try_end),





                (store_random_in_range, ":randomiser", 0, ":eligible_troop_count"), #randomise a lord from the eligible troops
                (assign, ":random_checker", 0),





                (try_for_range, ":cur_troop", lords_begin, lords_end),
                  (troop_slot_eq, ":cur_troop", slot_troop_coop_lord_spawned, 1), #use this to check the troops we marked as eligible lords

                  (assign, reg0, ":cur_troop"), # debug

                  (try_begin),
                    (eq, ":random_checker", ":randomiser"), #found her/him!
                    (assign, ":used_troop_no", ":cur_troop"),
                    (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 2), #prevent our lord from spawning again
                  (try_end),
                  (val_add, ":random_checker", 1),

                (try_end),




                #continue checking all possible troops
                (try_for_range, ":cur_troop", quick_battle_troops_begin, quick_battle_troops_end),
                  (troop_slot_eq, ":cur_troop", slot_troop_coop_lord_spawned, 1),

                  (assign, reg0, ":cur_troop"), # debug

                  (try_begin),
                    (eq, ":random_checker", ":randomiser"),
                    (assign, ":used_troop_no", ":cur_troop"),
                    (troop_set_slot, ":cur_troop", slot_troop_coop_lord_spawned, 2),
                  (try_end),
                  (val_add, ":random_checker", 1),

                (try_end),
              (try_end),
              #set the wave spawn data for our leader
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 1, ":used_troop_no"),
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 2, 1), #only one leader
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 3, ":spawn_point1"), #always use spawn_point1 for simplicity
              (troop_get_slot, ":num_bot_types", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin),
              (val_add, ":num_bot_types", 2), #adding two bot types because we're about to add the guards anyway
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin, ":num_bot_types"),
              (assign, ":cur_max_level", -1),
              (store_troop_faction, ":used_troop_faction_no", ":used_troop_no"), #use guards from the same faction as the wave leader (used mainly for all stars wave)
              (try_begin),
                (eq, "$g_multiplayer_team_2_faction", "fac_outlaws"),
                (assign, ":guard_troop_no", "trp_sea_raider_leader"), #outlaws always use sea raider captains as guards
              (else_try),
                (try_for_range, ":cur_troop", soldiers_begin, soldiers_end), #check all soldiers to find a suitable guard troop
                  (store_troop_faction, ":troop_faction", ":cur_troop"),
                  (eq, ":troop_faction", ":used_troop_faction_no"), #same faction as the leader?
                  (store_character_level, ":cur_level", ":cur_troop"),
                  (gt, ":cur_level", ":cur_max_level"), #higher than previous soldiers found from our required faction?
                  (assign, ":cur_max_level", ":cur_level"),
                  (assign, ":guard_troop_no", ":cur_troop"),
                (try_end),
              (try_end),
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 4, ":guard_troop_no"), #set the troop id in the correct wave data slot
              (try_begin),
                (eq, ":spawn_king", 0), #double guards for the king! simple but creates a nice final challenge
                (gt, "$g_mp_coop_lord_waves", 0),
                (gt, ":since_last_boss", 1),
                (assign, ":guard_count", 2),
              (else_try),
                (assign, ":guard_count", 1),
              (try_end),
              (get_max_players, ":num_players"),
              (assign, ":total_players", 0),
              (try_for_range, ":cur_player", 0, ":num_players"), #find out how many players are on the defenders
                (player_is_active, ":cur_player"),
                (player_get_team_no, ":cur_team", ":cur_player"),
                (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_ccoop_return_of_the_king, "$g_ccoop_king_troop"),
                (eq, ":cur_team", 0),
                (val_add, ":total_players", 1),
              (try_end),
              (val_mul, ":guard_count", ":total_players"), #1 guard per player for lord waves; 2 for the king
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 5, ":guard_count"), #set the number
              (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 6, ":spawn_point1"), #spawn guards with the wave leader
              (val_add, ":spawn_lord", 1), #used in code below to avoid "boosting" guards when data slots are full... also prevents us legitimately "boosting" generated troops that match the guard troop, which is a shame but not critical
            (try_end),









            (assign, ":eligible_troop_count", 0), #reset this and start looking for eligible troops to fill the wave

            (try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
              (troop_set_slot, ":cur_troop", slot_troop_mp_squad_type, 0), #we use this slot to check if they are eligible - was previously used for something else in WFaS. should have been renamed really...
            (try_end),

            (try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
                (neq, ":cur_troop", "trp_mercenaries_end"),

                (store_troop_faction, ":troop_faction", ":cur_troop"),
                (this_or_next|eq, ":troop_faction", "$g_multiplayer_team_2_faction"), #right faction?
                (eq, "$g_multiplayer_team_2_faction", "fac_ccoop_all_stars"), #... or all stars?
                (store_character_level, ":troop_level", ":cur_troop"),
                (le, ":troop_level", ":max_level"), #doesn't exceed our level cap for the current wave?
                (troop_set_slot, ":cur_troop", slot_troop_mp_squad_type, 1), #eligible!
                (val_add, ":eligible_troop_count", 1), #add the count to be used by the randomiser
                (assign, reg0, ":used_troop_no"), # debug
                (display_debug_message, "@{!}used troop no is {reg0}"), # debug
            (try_end),

            (try_for_range, ":cur_bot_readying", 0, ":num_troops_for_wave"), #run this individually for every single wave bot we want to generate - not very efficient! Causes a momentary spike with a lot of players
              (assign, reg0, ":cur_bot_readying"),
              (try_begin),
                (neg|troop_slot_eq, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 13, 0), #if all data is filled (this slot is the last used for wave bot ids)
                (store_random_in_range, ":booster_slot", ":spawn_lord", 5), #pick an existing troop to "boost" - don't "boost" the wave leader or guards

                (val_mul, ":booster_slot", 3), #get to the right data slot
                (val_add, ":booster_slot", multi_data_ccoop_wave_spawn_data_begin + 1), # used troop no

                (val_add, ":booster_slot", 1), # used troop count
                (troop_get_slot, ":used_troop_count", "trp_multiplayer_data", ":booster_slot"), #get the current number spawning
                (val_add, ":used_troop_count", 1), #boost!
                (troop_set_slot, "trp_multiplayer_data", ":booster_slot", ":used_troop_count"), #rewrite the slot with the new number of that troop
              (else_try),
                #if there are still slots available (there are 5 total), we look for a troop again



                (store_random_in_range, ":randomiser", 0, ":eligible_troop_count"), #pick a number...
                (assign, ":random_checker", 0),



                (try_for_range, ":cur_troop", soldiers_begin, soldiers_end), #this covers all troops for factions, outlaws and all stars
                  (troop_slot_eq, ":cur_troop", slot_troop_mp_squad_type, 1),


                  (try_begin),
                    (eq, ":random_checker", ":randomiser"),
                    (assign, ":used_troop_no", ":cur_troop"), #found our troop!
                  (try_end),
                  (val_add, ":random_checker", 1),

                (try_end),





                (try_begin),
                  (assign, ":troop_already_spawning", 0), #found our troop! But is that troop already spawning?
                  (try_for_range, ":cur_slot", 0, 5), #check our existing data slots
                    (val_mul, ":cur_slot", 3),
                    (val_add, ":cur_slot", multi_data_ccoop_wave_spawn_data_begin + 1), #... the ones that hold our troop ids
                    (troop_get_slot, ":cur_slot_troop_no", "trp_multiplayer_data", ":cur_slot"),
                    (eq, ":cur_slot_troop_no", ":used_troop_no"), #is there a match?

                    (val_add, ":cur_slot", 1), # move our slot to the one which holds the number of that troop type which will spawn
                    (troop_get_slot, ":used_troop_count", "trp_multiplayer_data", ":cur_slot"),
                    (val_add, ":used_troop_count", 1), #and add one more
                    (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":used_troop_count"),
                    #(assign, ":used_slot", ":cur_slot"),
                    (assign, ":troop_already_spawning", 1),
                    #(display_message, "@troop already spawning!"),
                  (try_end),
                  (eq, ":troop_already_spawning", 1), #don't try else if that troop type was already spawning
                (else_try),
                  (assign, ":found_empty_slot", 0), #but if the troop wasn't already spawning..
                  (try_for_range, ":cur_slot", ":spawn_lord", 5),
                    (neq, ":found_empty_slot", 1), #find the next empty slot
                    (val_mul, ":cur_slot", 3),
                    (val_add, ":cur_slot", multi_data_ccoop_wave_spawn_data_begin + 1),

                    (troop_get_slot, ":cur_slot_troop_no", "trp_multiplayer_data", ":cur_slot"),
                    (eq, ":cur_slot_troop_no", 0), #is it empty?









                    (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":used_troop_no"), #not anymore!









                    (val_add, ":cur_slot", 1),
                    (troop_get_slot, ":used_troop_count", "trp_multiplayer_data", ":cur_slot"),
                    (val_add, ":used_troop_count", 1), #should be one anyway, since this is the first troop of that type
                    (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":used_troop_count"),

                    (troop_get_slot, ":num_bot_types", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin),
                    (val_add, ":num_bot_types", 1), #increase the number of bot types, which is sent along with the other data - used by the spawning script
                    (troop_set_slot, "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin, ":num_bot_types"),

                    (assign, ":used_slot", ":cur_slot"),
                    (assign, ":found_empty_slot", 1),
                    (store_random_in_range, ":used_entry_point", 0, 2), #randomise the entry point
                    (try_begin),
                      (this_or_next|eq, ":used_entry_point", 0),
                      (le, ":spawn_point2", 0), #and always user spawn_point1 if spawn_point2 isn't active for this wave
                      (assign, ":used_entry_point", ":spawn_point1"),
                    (else_try),
                      (assign, ":used_entry_point", ":spawn_point2"),
                    (try_end),
                    (val_add, ":used_slot", 1),
                    (troop_set_slot, "trp_multiplayer_data", ":used_slot", ":used_entry_point"),
                  (try_end),
                (try_end),
              (try_end),





            (try_end),





            (get_max_players, ":max_players"), #send data to clients so they can see what troops are spawning next
            (try_for_range, ":cur_player", 1, ":max_players"),
                (player_is_active, ":cur_player"),
                (call_script, "script_multiplayer_ccoop_send_troop_data_to_client", ":cur_player"),
            (try_end),

        (try_end),
    ]),


    # script_multiplayer_ccoop_calculate_round_duration
    # Input: none
    # Output: none
    ("multiplayer_ccoop_calculate_round_duration",
    [
        (try_begin),
            (multiplayer_is_server),
            (assign, "$g_multiplayer_ccoop_enemy_respawn_secs", 300),  #5min

            (store_sub, ":wave_no", "$g_multiplayer_ccoop_wave_no", 1),
            (val_max, ":wave_no", 0),
            (store_mod, ":mod", ":wave_no", 10),
            (val_mul, ":mod", 30),
            (val_add, "$g_multiplayer_ccoop_enemy_respawn_secs", ":mod"),

            (try_begin),
                (gt, "$g_multiplayer_ccoop_wave_no", 20),
                (val_mul, "$g_multiplayer_ccoop_enemy_respawn_secs", 2),
            (else_try),
                (gt, "$g_multiplayer_ccoop_wave_no", 10),
                (val_mul, "$g_multiplayer_ccoop_enemy_respawn_secs", 3),
                (val_div, "$g_multiplayer_ccoop_enemy_respawn_secs", 2),
            (try_end),



            (get_max_players, ":num_players"),
            (try_for_range, ":cur_player", 1, ":num_players"),
                (player_is_active, ":cur_player"),
                (assign, reg0, ":cur_player"),
                (display_debug_message, "@{!}sending message to {reg0} multiplayer_event_other_event_ccoop_count_down_invisible"),
                (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_count_down_invisible, "$g_multiplayer_ccoop_enemy_respawn_secs", "$g_multiplayer_ccoop_wave_no"),
            (try_end),
        (try_end),
    ]),



    # script_multiplayer_ccoop_send_troop_data_to_client
    # Input: client number
    # Output: none
    ("multiplayer_ccoop_send_troop_data_to_client",
    [
        (try_begin),
            (store_script_param, ":cur_player", 1),

            (troop_get_slot, ":data_1", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin),
            (troop_get_slot, ":data_2", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 1),
            (troop_get_slot, ":data_3", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 2),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_update_spawn_data_1, ":data_1", ":data_2", ":data_3"),
            (troop_get_slot, ":data_1", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 3),
            (troop_get_slot, ":data_2", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 4),
            (troop_get_slot, ":data_3", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 5),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_update_spawn_data_2, ":data_1", ":data_2", ":data_3"),
            (troop_get_slot, ":data_1", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 6),
            (troop_get_slot, ":data_2", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 7),
            (troop_get_slot, ":data_3", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 8),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_update_spawn_data_3, ":data_1", ":data_2", ":data_3"),
            (troop_get_slot, ":data_1", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 9),
            (troop_get_slot, ":data_2", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 10),
            (troop_get_slot, ":data_3", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 11),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_update_spawn_data_4, ":data_1", ":data_2", ":data_3"),
            (troop_get_slot, ":data_1", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 12),
            (troop_get_slot, ":data_2", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 13),
            (troop_get_slot, ":data_3", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 14),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_update_spawn_data_5, ":data_1", ":data_2", ":data_3"),
            (troop_get_slot, ":data_1", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 15),
            (multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_update_spawn_data_6, ":data_1"),
        (try_end),
    ]),

    # script_multiplayer_ccoop_spawn_wave
    # Input: spawn_required -> how many bots are needed
    # Output: none
    ("multiplayer_ccoop_spawn_wave",
      [
        (try_begin),
            (multiplayer_is_server),
            (set_fixed_point_multiplier, 100),

            (store_script_param, ":spawn_required", 1),



            (assign, reg0, ":spawn_required"), # debug
            (display_debug_message, "@{!}spawn required is: {reg0}"),

            (assign, ":num_troops_for_wave", 0),

            #(troop_get_slot, ":num_bot_types", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin),
            (try_for_range, ":cur_bot_type", 0, 5),
                (store_mul, ":cur_slot", ":cur_bot_type", 3),
                (val_add, ":cur_slot", multi_data_ccoop_wave_spawn_data_begin + 2),
                (troop_get_slot, ":cur_bot_count", "trp_multiplayer_data", ":cur_slot"),
                (val_add, ":num_troops_for_wave", ":cur_bot_count"),
            (try_end),

            (assign, reg0, ":num_troops_for_wave"), # debug
            (display_debug_message, "@{!}num_troops_for_wave is {reg0}"),

            (assign, ":reduced_spawn_amount", 0),
            (assign, ":reduced_spawn_amount_mod", 0),
            (try_begin),
                (gt, ":num_troops_for_wave", ":spawn_required"),
                (store_sub, ":reduced_spawn_amount", ":num_troops_for_wave", ":spawn_required"),
                #(store_mod, ":reduced_spawn_amount_mod", ":reduced_spawn_amount", ":num_bot_types"),
                #(val_div, ":reduced_spawn_amount", ":num_bot_types"),

                (assign, reg0, ":reduced_spawn_amount"), # debug
                (assign, reg1, ":reduced_spawn_amount_mod"), # debug
                (display_debug_message, "@{!}num_troops_for_wave is gt spawn_required. reduced_spawn_amount is {reg0}, reduced_spawn_amount_mod is {reg1}"),
            (try_end),




            (store_current_scene, ":cur_scene"),
            (modify_visitors_at_site, ":cur_scene"),
            (assign, ":num_troops_spawned", 0),

            #(troop_get_slot, ":leader_no", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 1),
            #(troop_get_slot, ":point_no", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin + 3),
            #(entry_point_get_position, pos60, ":point_no"),

















            (try_for_range, ":cur_bot_spawning", 0, 5),
                (store_mul, ":cur_slot", ":cur_bot_spawning", 3),
                (val_add, ":cur_slot", multi_data_ccoop_wave_spawn_data_begin + 1),
                (troop_get_slot, ":spawned_troop_no", "trp_multiplayer_data", ":cur_slot"),
                (gt, ":spawned_troop_no", 0),
                (val_add, ":cur_slot", 1),
                (troop_get_slot, ":spawned_troop_count", "trp_multiplayer_data", ":cur_slot"),
                (assign, ":original_spawned_troop_count", ":spawned_troop_count"),

                (assign, reg0, ":original_spawned_troop_count"), # debug
                (display_debug_message, "@{!}original_spawned_troop_count is {reg0}"),

                (val_add, ":cur_slot", 1),
                (troop_get_slot, ":spawned_troop_entry_point", "trp_multiplayer_data", ":cur_slot"),







                (val_sub, ":spawned_troop_count", ":reduced_spawn_amount"),
                (try_begin),
                    (lt, ":cur_bot_spawning", ":reduced_spawn_amount_mod"),
                    (val_sub, ":spawned_troop_count", 1),

                    (assign, reg0, ":cur_bot_spawning"), # debug
                    (assign, reg1, ":reduced_spawn_amount_mod"), # debug
                    (display_debug_message, "@{!}reducing spawn amount by one"),
                (try_end),

                (assign, reg0, ":cur_bot_spawning"), # debug
                (assign, reg1, ":spawned_troop_entry_point"), # debug
                (str_store_troop_name, s0, ":spawned_troop_no"), # debug
                (assign, reg2, ":spawned_troop_count"), # debug
                (display_debug_message, "@{!}spawning bot group {reg0}: {reg2} {s0} from entry point {reg1}"),

                (add_visitors_to_current_scene, ":spawned_troop_entry_point", ":spawned_troop_no", ":spawned_troop_count", 1, -1),

                (val_add, ":num_troops_spawned", ":spawned_troop_count"),
                (val_sub, ":original_spawned_troop_count", ":spawned_troop_count"),
                (store_mul, ":cur_slot", ":cur_bot_spawning", 3),
                (val_add, ":cur_slot", multi_data_ccoop_wave_spawn_data_begin + 2),
                (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":original_spawned_troop_count"),
            (try_end),

            # sync clients
            (get_max_players, ":num_players"),
            (try_for_range, ":cur_player", 1, ":num_players"),
                (player_is_active, ":cur_player"),
                (call_script, "script_multiplayer_ccoop_send_troop_data_to_client", ":cur_player"),
            (try_end),
        (try_end),
    ]),

    # script_multiplayer_ccoop_check_reinforcement
    # Input: arg1 = team 1 initial count, arg2 = team 2 initial count
    # Output: reg0 = number of players to be moved from team1 to team2 (can be negative).
    ("multiplayer_ccoop_check_reinforcement",
    [
        (try_begin),
            (multiplayer_is_server),

            (call_script, "script_multiplayer_ccoop_get_alive_enemy_count"),
            (store_sub, ":free_enemy_slots", 100, reg0), #enemy required

            (try_begin),
                (ge, ":free_enemy_slots", 50),  # if 50 or more enemy reinforcement needed

                (call_script, "script_multiplayer_ccoop_spawn_wave", ":free_enemy_slots"),
            (else_try),
                #(lt, ":free_enemy_slots", 50),
                (assign, ":num_troops_for_wave", 0),
                (troop_get_slot, ":num_bot_types", "trp_multiplayer_data", multi_data_ccoop_wave_spawn_data_begin),
                (try_for_range, ":cur_bot_type", 0, ":num_bot_types"),
                    (store_mul, ":cur_slot", ":cur_bot_type", 3),
                    (val_add, ":cur_slot", multi_data_ccoop_wave_spawn_data_begin + 2),
                    (troop_get_slot, ":cur_bot_count", "trp_multiplayer_data", ":cur_slot"),
                    (val_add, ":num_troops_for_wave", ":cur_bot_count"),
                (try_end),


                (ge, ":free_enemy_slots", ":num_troops_for_wave"),
                (call_script, "script_multiplayer_ccoop_spawn_wave", ":free_enemy_slots"),
            (try_end),
        (try_end),
    ]),

    # script_multiplayer_get_balance_dif
    # Input: arg1 = team 1 initial count, arg2 = team 2 initial count
    # Output: reg0 = number of players to be moved from team1 to team2 (can be negative).
    ("multiplayer_get_balance_dif",
      [
        (store_script_param, ":number_of_players_at_team_1", 1),
        (store_script_param, ":number_of_players_at_team_2", 2),
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 0, ":num_players"),
          (player_is_active, ":cur_player"),
          (player_get_team_no, ":player_team", ":cur_player"),
          (try_begin),
            (eq, ":player_team", 0),
            (val_add, ":number_of_players_at_team_1", 1),
          (else_try),
            (eq, ":player_team", 1),
            (val_add, ":number_of_players_at_team_2", 1),
          (try_end),
        (try_end),
        (assign, ":single_player_move_effect", 2),

        (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
        (assign, ":number_of_players_will_be_moved", 0),
        (try_begin),
          (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
          (le, ":difference_of_number_of_players", ":checked_value"),
          (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", ":single_player_move_effect"),
        (else_try),
          (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
          (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", ":single_player_move_effect"),
        (try_end),
        (assign, reg0, ":number_of_players_will_be_moved"),
      ]
    ),









  # script_multiplayer_server_play_sound_at_position
  # Input: arg1 = sound_id
  # Input: pos60 = position
  # Output: none
  ("multiplayer_server_play_sound_at_position",
   [
     (store_script_param, ":sound_id", 1),

     (try_begin),
       (this_or_next|multiplayer_is_server),
       (neg|game_in_multiplayer_mode),

       (is_between, ":sound_id", 0, "snd_sounds_end"), # Valid sound

       (try_begin),
         (neg|multiplayer_is_dedicated_server), # If a client and not a dedicated server that calls then play locally.
         (play_sound_at_position, ":sound_id", pos60),
       (try_end),



       (try_begin),
         (multiplayer_is_server), # If this is a server broadcast the sound to all players

         (set_fixed_point_multiplier, 100),
         (position_get_x,":xvalue", pos60),
         (position_get_y,":yvalue", pos60),
         (position_get_z,":zvalue", pos60),

         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active,":cur_player"),

           (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_return_sound_at_pos,":xvalue",":yvalue",":zvalue",":sound_id"),
         (try_end),
       (try_end),
     (try_end),
   ]),









    # script_mp_set_coop_companions
    ("mp_set_coop_companions",
    [
        (store_script_param, ":player_id", 1),
        (assign, ":slot_id", slot_player_companion_ids_begin),
        (player_set_slot, ":player_id", ":slot_id", "$g_presentation_obj_coop_companion_0"),
        #(str_store_troop_name, s0, "$g_presentation_obj_coop_companion_0"),
        #(troop_set_class, "$g_presentation_obj_coop_companion_0", 0),
        #(class_set_name, 0, s0),
        (val_add, ":slot_id", 1),
        (player_set_slot, ":player_id", ":slot_id", "$g_presentation_obj_coop_companion_1"),
        #(str_store_troop_name, s0, "$g_presentation_obj_coop_companion_1"),
        #(troop_set_class, "$g_presentation_obj_coop_companion_0", 1),
        #(class_set_name, 1, s0),
        (val_add, ":slot_id", 1),
        (player_set_slot, ":player_id", ":slot_id", "$g_presentation_obj_coop_companion_class_0"),
        (assign, reg0, "$g_presentation_obj_coop_companion_class_0"),
        #(display_message, "@setting companion class on client: {reg0}"),
        (val_add, ":slot_id", 1),
        (player_set_slot, ":player_id", ":slot_id", "$g_presentation_obj_coop_companion_class_1"),
    ]),









#	# script_mp_ccoop_change_map
#	#MCA: change map
#	("mp_ccoop_change_map",
#	[
#		(try_begin),
#			(multiplayer_is_dedicated_server),
#
#			# random scene
#			(store_random_in_range, ":scene_no", multiplayer_scenes_begin, multiplayer_scenes_end),
#
#			(assign, "$g_multiplayer_selected_map", ":scene_no"),
#			(team_set_faction, 0, "$g_multiplayer_next_team_1_faction"),
#			(team_set_faction, 1, "$g_multiplayer_next_team_2_faction"),
#			(call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
#			(start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 1),
#		(else_try),
#			(multiplayer_is_server),
#			(call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
#			(start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 1),
#		(try_end),
#	]
#	),

















    # script_mp_get_player_alive_troop_count
    # MCA
    # returns alive bot count for player team on reg0
    ("mp_get_player_alive_troop_count",   # parameters: 1. player_id   2. troop_id
    [
        (store_script_param, ":player_id", 1),
        (store_script_param, ":troop_id", 2),

        (player_get_team_no, ":player_team", ":player_id"),

        (assign, ":troop_count", 0),

        (try_for_agents, ":cur_agent"),
            (agent_is_human, ":cur_agent"),
            (agent_is_alive, ":cur_agent"),
            (agent_is_non_player, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),

            (try_begin),
                (eq, ":player_team", ":cur_agent_team"),
                (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
                (eq, ":troop_id", ":agent_troop_id"),

                # if agent belongs to the player
                (agent_get_group, ":agent_group", ":cur_agent"),
                (eq, ":agent_group", ":player_id"),

                (val_add, ":troop_count", 1),
            (try_end),
        (try_end),






        (assign, reg0, ":troop_count"),

        #MCA
    #	(assign, reg1, ":troop_id"),
    #	(assign, reg2, ":player_id"),
    #	(display_debug_message, "@{!}alive troop ({reg1}) count: {reg0} for player {reg2}"),
    ]),

    # script_mp_get_player_total_alive_troop_count
    # MCA
    # returns total alive bot count for player team on reg0
    ("mp_get_player_total_alive_troop_count",   # parameters: 1. player_id
    [
        (store_script_param, ":player_id", 1),

        (player_get_team_no, ":player_team", ":player_id"),

        (assign, ":troop_count", 0),

        (try_for_agents, ":cur_agent"),
            (agent_is_human, ":cur_agent"),
            (agent_is_alive, ":cur_agent"),
            (agent_is_non_player, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),

            # if agent belongs to the player
            (agent_get_group, ":agent_group", ":cur_agent"),
            (eq, ":agent_group", ":player_id"),

            (try_begin),
                (eq, ":player_team", ":cur_agent_team"),
                (val_add, ":troop_count", 1),
            (try_end),
        (try_end),






        (assign, reg0, ":troop_count"),

        #MCA
    #	(assign, reg2, ":player_id"),
    #	(display_debug_message, "@{!}total alive troop count: {reg0} for player {reg2}"),
    ]),

    # script_multiplayer_spawn_player_bot_squad_at_point
    ("multiplayer_spawn_player_bot_squad_at_point",
    [
        (store_script_param, ":player_no", 1),
        (store_script_param, ":player_team", 2),
        (store_script_param, ":point_no", 3),


        (try_begin),








            (call_script, "script_multiplayer_get_bots_count", ":player_no"),
            (assign, ":player_bot_count", reg0),









            (try_for_range, ":slot_id", slot_player_companion_ids_begin, slot_player_companion_ids_end),
                (lt, ":player_bot_count", 2),

                (player_get_slot, ":companion_id", ":player_no", ":slot_id"),
                (call_script, "script_mp_get_player_alive_troop_count", ":player_no", ":companion_id"),
                (eq, reg0, 0),
                #(try_begin),
                #  (try_for_range, ":cur_slot", slot_player_companion_ids_begin, slot_player_companion_classes_end),
                #    (assign, reg1, ":cur_slot"),
                #    (player_get_slot, reg2, ":player_no", ":cur_slot"),
                #    (multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@{!}spawning companion slot: {reg1}   value {reg2}"),
                #  (try_end),
                #(try_end),

                (call_script, "script_mp_spawn_coop_companion", ":player_no", ":companion_id", ":slot_id", ":player_team", ":point_no"),
                #(try_begin),
                #  (try_for_range, ":cur_slot", slot_player_companion_ids_begin, slot_player_companion_classes_end),
                #    (assign, reg1, ":cur_slot"),
                #    (player_get_slot, reg2, ":player_no", ":cur_slot"),
                #    (multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@{!}after spawning slot: {reg1}   value {reg2}"),
                #  (try_end),
                #(try_end),







                (val_add, ":player_bot_count", 1),
            (try_end),



        (try_end),
    ]),

    ("multiplayer_get_spawn_point_close_to_bots",
    [
       (store_script_param, ":player_no", 1),
       (player_get_team_no, ":player_team", ":player_no"),
       (assign, ":x_pos", 0),
       (assign, ":y_pos", 0),
       (assign, ":num_living_players", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_is_non_player, ":agent_no"),
         (agent_get_group, ":agent_group", ":agent_no"),
         (agent_get_team, ":agent_team", ":agent_no"),
         (try_begin),
            (eq, ":agent_group", ":player_no"),
            (eq, ":agent_team", ":player_team"),
            (agent_get_position, pos2, ":agent_no"),
            (position_get_x, ":x1", pos2),
            (position_get_y, ":y1", pos2),
            (val_add, ":x_pos", ":x1"),
            (val_add, ":y_pos", ":y1"),
            (val_add, ":num_living_players", 1),
         (try_end),
       (try_end),
       (try_begin),
         (gt, ":num_living_players", 0),
         (val_div, ":x_pos", ":num_living_players"),
         (val_div, ":y_pos", ":num_living_players"),
       (try_end),
       (position_set_x, pos0, ":x_pos"),
       (position_set_y, pos0, ":y_pos"),
       (position_set_z, pos0, 0),
       (assign, ":best_score", 0),
       (assign, ":best_point", 0),
       (try_for_range, ":i_point", 0, multi_num_valid_entry_points),
        (entry_point_get_position, pos1, ":i_point"),
        (position_set_z, pos1, 0),
        (get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1),
        (try_begin),
            (le, ":dist", multi_dist_to_capt_spawn_point),
            (val_max, ":dist", 1),
            (store_mul, ":score", multi_dist_to_capt_spawn_point, 1000),
            (val_div, ":score", ":dist"),
            (try_begin),
                (gt, ":score", ":best_score"),
                (assign, ":best_point", ":i_point"),
                (assign, ":best_score", ":score"),
            (try_end),
        (try_end),
       (try_end),
       (assign, reg0, ":best_point"),
    ]),

    # script_multiplayer_get_spawn_point_close_to_player
    # input: arg1 = player_no
    # output: reg0 = best_spawn_point
    ("multiplayer_get_spawn_point_close_to_player",
    [
       (store_script_param, ":player_no", 1),
       (player_get_agent_id, ":player_agent", ":player_no"),
       (position_set_x, pos0, 0),
       (position_set_y, pos0, 0),
       (try_begin),
         (agent_is_alive, ":player_agent"),
         (agent_get_position, pos0, ":player_agent"),
       (try_end),

       (position_set_z, pos0, 0),
       (assign, ":best_score", 0),
       (assign, ":best_point", 0),
       (try_for_range, ":i_point", 0, multi_num_valid_entry_points),
        (entry_point_get_position, pos1, ":i_point"),
        (position_set_z, pos1, 0),
        (get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1),
        (try_begin),
            (le, ":dist", multi_dist_to_capt_spawn_point),
            (val_max, ":dist", 1),
            (store_mul, ":score", multi_dist_to_capt_spawn_point, 1000),
            (val_div, ":score", ":dist"),
            (try_begin),
                (gt, ":score", ":best_score"),
                (assign, ":best_point", ":i_point"),
                (assign, ":best_score", ":score"),
            (try_end),
        (try_end),
       (try_end),
       (assign, reg0, ":best_point"),
    ]),

    ("multiplayer_get_bots_count",
    [
       (store_script_param, ":player_no", 1),
       (player_get_team_no, ":player_team", ":player_no"),
       (assign, ":num_living_players", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_is_non_player, ":agent_no"),
         (agent_get_group, ":agent_group", ":agent_no"),
         (agent_get_team, ":agent_team", ":agent_no"),
         (try_begin),
            (eq, ":agent_group", ":player_no"),
            (eq, ":agent_team", ":player_team"),
            (val_add, ":num_living_players", 1),
         (try_end),
       (try_end),
       (assign, reg0, ":num_living_players"),
    ]),

    ("multiplayer_get_selected_squad_slot_id",
    [
        (store_script_param, ":player_no", 1),
        (assign, ":cur_troop_no", slot_player_bot_type_1_wanted),
        (try_for_range, ":slot_no", slot_player_bot_type_1_wanted, slot_player_bot_type_4_wanted+1),
            (player_get_slot, ":value",  ":player_no", ":slot_no"),
            (try_begin),
                (eq, ":value", 1),
                (assign, ":cur_troop_no", ":slot_no"),
            (try_end),
        (try_end),
        (assign, reg0, ":cur_troop_no"),
    ]),









    # script_cf_multiplayer_event_team_change
    ("cf_multiplayer_event_team_change",
    [
        (store_script_param, ":player_no", 1),
        (try_begin),
            (eq, "$g_multiplayer_is_game_type_captain", 1),
            (player_get_team_no, ":player_team", ":player_no"),
            #(player_get_agent_id, ":player_agent", ":player_no"),
            (try_for_agents, ":agent_no"),
                (agent_is_human, ":agent_no"),
                (agent_is_alive, ":agent_no"),
                (agent_is_non_player, ":agent_no"),
                (agent_get_group, ":agent_group", ":agent_no"),
                (agent_get_team, ":agent_team", ":agent_no"),
                (try_begin),
                    (eq, ":agent_group", ":player_no"),
                    (eq, ":agent_team", ":player_team"),

                    ## increase player's kill count by 2 since death of each squad member will cause -2 score on team change
                    #(player_get_kill_count, ":player_kill_count", ":player_no"),
                    #(val_add, ":player_kill_count", 2),
                    #(player_set_kill_count, ":player_no", ":player_kill_count"),
                    ## also decrease death by 2 for the same reason
                    #(player_get_death_count, ":player_death_count", ":player_no"),
                    #(val_sub, ":player_death_count", 2),
                    #(player_set_death_count, ":player_no", ":player_death_count"),

                    #(call_script, "script_add_kill_death_counts", ":player_agent", ":agent_no"),
                    (remove_agent, ":agent_no"),
                (try_end),
            (try_end),
        (try_end),
    ]),























  # script_team_get_attack_readying_ranged_agent_percentage
  # Input: arg1: team_no, arg2: try for team's enemies
  # Output: reg0: percentage attack readying ranged agent,
  ("team_get_attack_readying_ranged_agent_percentage",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":negate", 2),
      (assign, ":num_ranged_agents", 0),
      (assign, ":num_readying_attack", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_alive, ":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_team, ":agent_team", ":cur_agent"),
        (assign, ":continue", 0),
        (try_begin),
          (eq, ":negate", 1),
          (teams_are_enemies, ":agent_team", ":team_no"),
          (assign, ":continue", 1),
        (else_try),
          (eq, ":agent_team", ":team_no"),
          (assign, ":continue", 1),
        (try_end),
        (eq, ":continue", 1),
        (agent_get_combat_state, ":agent_cs", ":cur_agent"),
        (agent_get_wielded_item, ":agent_wi0", ":cur_agent", 0),
        (try_begin),
          (is_between,":agent_wi0",ranged_weapons_begin,ranged_weapons_end),
          (val_add,  ":num_ranged_agents", 1),
          (try_begin),
            (eq, ":agent_cs", 1),#atkcs_readying_attack
            (val_add, ":num_readying_attack", 1),
          (try_end),
        (try_end),
      (try_end),

      (try_begin),
        (eq,  ":num_ranged_agents", 0),
        (assign,  ":num_ranged_agents", 1),
      (try_end),
      (store_mul, ":perc_readying_attack_over_rangeds", ":num_readying_attack", 100),
      (val_div, ":perc_readying_attack_over_rangeds", ":num_ranged_agents"),
      (assign, reg0, ":perc_readying_attack_over_rangeds"),
  ]),

  # script_multiplayer_get_requested_squad_count
  # Input: none
  # Output: reg0 = requested squad count
  ("multiplayer_get_requested_squad_count",
   [
        (store_script_param, ":player_id", 1),
        (assign, ":total_troop_count", 0),
        (try_for_range, ":slot_id", slot_player_companion_ids_begin, slot_player_companion_ids_end),
            (player_get_slot, ":troop_count", ":player_id", ":slot_id"),
            (val_add, ":total_troop_count", ":troop_count"),
        (try_end),








        (assign, reg0, ":total_troop_count"),
   ]),











  # script_multiplayer_update_cost_labels
  # Input: none
  # Output: none
  ("multiplayer_update_cost_labels",
    [
      (multiplayer_get_my_player, ":my_player_no"),
      (player_get_gold, ":player_gold", ":my_player_no"),
      (call_script, "script_multiplayer_calculate_cur_selected_items_cost", ":my_player_no", 1),

      (overlay_set_text, "$g_presentation_obj_item_select_12", "str_total_item_cost_reg0"),
      (try_begin),
         (ge, ":player_gold", reg0),
         (overlay_set_color, "$g_presentation_obj_item_select_12", 0xFFFFFF),
      (else_try),
         (overlay_set_color, "$g_presentation_obj_item_select_12", 0xFF0000),
      (try_end),
  ]),

    # script_multiplayer_ccoop_give_round_bonus_gold
    # Input: none
    # Output: none
    ("multiplayer_ccoop_give_round_bonus_gold",
    [
        (try_begin),
            (gt, "$g_multiplayer_ccoop_wave_no", 0),
            (store_mul, ":bonus_gold", "$g_multiplayer_ccoop_wave_no", 100),
            (val_add, ":bonus_gold", 400),

            (get_max_players, ":num_players"),
            (try_for_range, ":cur_player", 0, ":num_players"),
                (player_is_active, ":cur_player"),
                (player_get_gold, ":player_gold", ":cur_player"),
                (val_add, ":player_gold", ":bonus_gold"),
                (player_set_gold, ":cur_player", ":player_gold", multi_max_gold_that_can_be_stored),
            (try_end),
        (try_end),
    ]),

    # script_multiplayer_ccoop_destroy_prison_cart
    # Input: none
    # Output: none
    ("multiplayer_ccoop_destroy_prison_cart",
    [
        (try_begin),
            (multiplayer_is_server),

            (try_begin),
                (multiplayer_is_dedicated_server),

                (assign, "$g_prison_cart_previous_point", "$g_prison_cart_point"),
                (assign, "$g_prison_cart_point", 0),

                (scene_prop_get_instance, ":prison_cart", "spr_prison_cart", 0),
                (scene_prop_get_instance, ":prison_cart_door_left", "spr_prison_cart_door_left", 0),
                (scene_prop_get_instance, ":prison_cart_door_right", "spr_prison_cart_door_right", 0),

                (set_fixed_point_multiplier, 100),

                (prop_instance_get_position, pos1, ":prison_cart"),
                (position_set_z, pos1, -4000), #40m down
                (prop_instance_set_position, ":prison_cart", pos1),
                (prop_instance_set_position, ":prison_cart_door_left", pos1),
                (prop_instance_set_position, ":prison_cart_door_right", pos1),
            (try_end),

            (display_debug_message, "@{!}destroy prison cart"),

            # send destroy prison cart event to clients
            (get_max_players, ":max_players"),
            (try_for_range, ":cur_player", 0, ":max_players"),
                (player_is_active, ":cur_player"),
                (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_other_events,
                    multiplayer_event_other_destroy_prison_cart),
            (try_end),





        (try_end),
    ]),

    # script_multiplayer_ccoop_spawn_prison_cart
    # INPUT: none
    # OUTPUT: none
    ("multiplayer_ccoop_spawn_prison_cart",
    [
        (try_begin),
            (multiplayer_is_server),

            # get prison cart random spawn point
            (store_random_in_range, "$g_prison_cart_point", 70, 75),

            #
            (assign, reg0, "$g_prison_cart_point"),
            (display_debug_message, "@{!}spawning prison cart at point {reg0}"),
            #

            # set prison cart position
            (set_fixed_point_multiplier, 100),
            (scene_prop_get_instance, ":prison_cart", "spr_prison_cart", 0),
            (entry_point_get_position, pos1, "$g_prison_cart_point"),
            (position_move_y, pos1, -400), #4m back
            (position_set_z_to_ground_level, pos1),
            (prop_instance_set_position, ":prison_cart", pos1),

            # place left door
            (scene_prop_get_instance, ":prison_cart_door_left", "spr_prison_cart_door_left", 0),
            (init_position, pos2),
            (position_set_x, pos2, 84, 0),
            (position_set_y, pos2, -314, 0),
            (position_set_z, pos2, 121, 0),
            (position_transform_position_to_parent, pos3, pos1, pos2),
            (prop_instance_set_position, ":prison_cart_door_left", pos3),
            (scene_prop_set_hit_points, ":prison_cart_door_left", 300),

            # place right door
            (scene_prop_get_instance, ":prison_cart_door_right", "spr_prison_cart_door_right", 0),
            (init_position, pos2),
            (position_set_x, pos2, -84, 0),
            (position_set_y, pos2, -315, 0),
            (position_set_z, pos2, 123, 0),
            (position_transform_position_to_parent, pos3, pos1, pos2),
            (prop_instance_set_position, ":prison_cart_door_right", pos3),
            (scene_prop_set_hit_points, ":prison_cart_door_right", 300),

            (try_begin),
                #(neg|multiplayer_is_dedicated_server),
                (call_script, "script_multiplayer_ccoop_set_prison_cart_visibility", 1),

                # display prison cart hint message to alive players
                (get_player_agent_no, ":player_agent"),
                (ge, ":player_agent", 0),
                (display_message, "str_prison_cart_hint"),

                (start_presentation, "prsnt_multiplayer_ccoop_next_wave_time_counter"), # to display ask for help to respawn hint
            (try_end),

            # send destroy prison cart event to clients
            (get_max_players, ":max_players"),
            (try_for_range, ":cur_player", 1, ":max_players"),
                (try_begin),
                    (player_is_active, ":cur_player"),
                    (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events,
                        multiplayer_event_other_spawn_prison_cart, "$g_prison_cart_point", 300),
                (try_end),
            (try_end),
        (try_end),
    ]),

    # script_multiplayer_ccoop_get_alive_enemy_count
    # Input: none
    # Output: reg0 = alive_enemy_count
    ("multiplayer_ccoop_get_alive_enemy_count",
    [
        (assign, ":alive_enemy_count", 0),
        (try_for_agents, ":cur_agent"),
            (try_begin),
                (agent_is_active, ":cur_agent"),
                (agent_is_human, ":cur_agent"),
                (agent_is_alive, ":cur_agent"),
                (agent_get_team, ":cur_agent_team", ":cur_agent"),
                (eq, ":cur_agent_team", 1),
                (val_add, ":alive_enemy_count", 1),
            (try_end),
        (try_end),
        (assign, reg0, ":alive_enemy_count"),
    ]),









#berk
#script_add_troop_to_cur_tableau_for_multiplayer
  # INPUT: troop_no
  # OUTPUT: none
  ("add_troop_to_cur_tableau_for_multiplayer",
    [
       (store_script_param, ":troop_no",1),

       (set_fixed_point_multiplier, 100),

       (cur_tableau_clear_override_items),
       (cur_tableau_set_override_flags, af_override_fullhelm),
##       (cur_tableau_set_override_flags, af_override_head|af_override_weapons),

       (init_position, pos2),
       (cur_tableau_set_camera_parameters, 1, 8, 8, 10, 10000),

       (init_position, pos5),
       (assign, ":cam_height", 300),
#       (val_mod, ":camera_distance", 5),
       (assign, ":camera_distance", 1000),
       (assign, ":camera_yaw", -15),
       (assign, ":camera_pitch", -18),
       (assign, ":animation", anim_stand_man),

       (troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
       (try_begin),
         (gt, ":horse_item", 0),
         (cur_tableau_add_horse, ":horse_item", pos2, "anim_horse_stand", 0),
         (assign, ":animation", "anim_ride_0"),
         (assign, ":camera_pitch", -20),
         (assign, ":camera_yaw", -25),
         (assign, ":cam_height", 500),
         (assign, ":camera_distance", 1400),
         (position_move_x, pos5, 50, 0),
       (try_end),
       (position_set_z, pos5, ":cam_height"),

       # camera looks towards -z axis
       (position_rotate_x, pos5, -90),
       (position_rotate_z, pos5, 180),

       # now apply yaw and pitch
       (position_rotate_y, pos5, ":camera_yaw"),
       (position_rotate_x, pos5, ":camera_pitch"),
       (position_move_z, pos5, ":camera_distance", 0),
       (position_move_x, pos5, -120, 0),
       (position_move_y, pos5, 130, 0),

       (try_begin),
         (troop_is_hero, ":troop_no"),
         (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
       (else_try),
         (store_mul, ":random_seed", ":troop_no", 126233),
         (val_mod, ":random_seed", 1000),
         (val_add, ":random_seed", 1),
         (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
       (try_end),
       (cur_tableau_set_camera_position, pos5),

       (copy_position, pos8, pos5),
       (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
       (position_rotate_z, pos8, 30),
       (position_rotate_x, pos8, -60),
       (cur_tableau_add_sun_light, pos8, 175,150,125),
     ]),

  # script_mp_set_player_troop_id
  # Input: arg1 = player_no, arg2 = troop_id, arg3 = sync with server
  # Output: none
  ("mp_set_player_troop_id",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":troop_id", 2),
      (store_script_param, ":do_sync", 3),
      (player_set_troop_id, ":player_no", ":troop_id"),
      (try_begin),
        (eq, ":troop_id", -1),
        (call_script, "script_multiplayer_clear_player_selected_items", ":player_no"), # just to make sure
      (else_try),
        (call_script, "script_multiplayer_set_default_item_selections_for_troop", ":player_no", ":troop_id"),
      (try_end),
      # server will do the same, so no need to send the new selections
      (try_begin),
        (neq, ":do_sync", 0),
        (multiplayer_send_int_to_server, multiplayer_event_change_troop_id, ":troop_id"),
      (try_end),
  ]),

  # script_mp_set_player_team_no
  # Input: arg1 = player_no, arg2 = team_no, arg3 = sync with server
  # Output: none
  ("mp_set_player_team_no",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":team_no", 2),
      (store_script_param, ":do_sync", 3),
      (player_set_team_no, ":player_no", ":team_no"),
      (try_begin),
        (neq, ":do_sync", 0),

        #(assign, reg0, ":team_no"),
        #(display_debug_message, "@{!}multiplayer_event_change_team_no is sent with team_no: {reg0}"),

        (multiplayer_send_int_to_server, multiplayer_event_change_team_no, ":team_no"),
      (try_end),
      (call_script, "script_mp_set_player_troop_id", ":player_no", -1, 0),
      #(call_script, "script_multiplayer_reset_squad_on_team_change_for_captain_game_types", ":player_no"),
      # server will do the same, so no need to send the new selections
  ]),











    # script_multiplayer_ccoop_set_prison_cart_visibility
    # Input: arg1 = visible
    # Output: none
    ("multiplayer_ccoop_set_prison_cart_visibility",
    [
        (store_script_param, ":visibility", 1),


        (set_fixed_point_multiplier, 100),

        (try_begin),
            (scene_prop_get_instance, ":prison_cart", "spr_prison_cart", 0),
            (scene_prop_get_instance, ":prison_cart_door_left", "spr_prison_cart_door_left", 0),
            (scene_prop_get_instance, ":prison_cart_door_right", "spr_prison_cart_door_right", 0),

            (try_begin),
                (eq, ":visibility", 0), # if make invisible

                (scene_prop_fade_out, ":prison_cart", 400),
                (scene_prop_fade_out, ":prison_cart_door_left", 400),
                (scene_prop_fade_out, ":prison_cart_door_right", 400),

                (prop_instance_enable_physics, ":prison_cart", 0),
                (prop_instance_enable_physics, ":prison_cart_door_left", 0),
                (prop_instance_enable_physics, ":prison_cart_door_right", 0),

                (store_mission_timer_a, "$g_multiplayer_ccoop_move_prison_cart"),
                (val_add, "$g_multiplayer_ccoop_move_prison_cart", 5), # after 5secs (related to 400)

                (assign, "$g_prison_cart_previous_point", "$g_prison_cart_point"),
                (assign, "$g_prison_cart_point", 0),
            (else_try),
                (gt, ":visibility", 0), # if make visible

                (scene_prop_fade_in, ":prison_cart", 300),
                (scene_prop_fade_in, ":prison_cart_door_left", 300),
                (scene_prop_fade_in, ":prison_cart_door_right", 300),

                (prop_instance_enable_physics, ":prison_cart", 1),
                (prop_instance_enable_physics, ":prison_cart_door_left", 1),
                (prop_instance_enable_physics, ":prison_cart_door_right", 1),
            (try_end),
        (try_end),
    ]),

    # script_multiplayer_ccoop_spawn_player_and_bots
    # INPUT: 1. player_no
    # OUTPUT: 0 if player not spawned, 1 if player spawned on reg0
    ("multiplayer_ccoop_spawn_player_and_bots",
    [
        (store_script_param, ":player_no", 1),

        (try_begin),
            (neg|player_is_busy_with_menus, ":player_no"),
            (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
            (lt, ":player_team", multi_team_spectator),

            (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
            (ge, ":player_troop", 0),

            (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

            (troop_get_inventory_slot, ":has_horse", ":player_troop", ek_horse),
            (try_begin),
                (ge, ":has_horse", 0),
                (assign, ":is_horseman", 1),
            (else_try),
                (assign, ":is_horseman", 0),
            (try_end),

            (call_script, "script_multiplayer_get_bots_count", ":player_no"),
            (assign, ":bot_count", reg0),

            (try_begin),
                #(gt, "$g_prison_cart_point", 0),
                (gt, "$g_multiplayer_ccoop_enemy_respawn_secs", 31),

                (assign, reg0, "$g_prison_cart_previous_point"),
                (display_debug_message, "@{!}prison cart spawn at point {reg0}"),

                (player_spawn_new_agent, ":player_no", "$g_prison_cart_previous_point"),
                (call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":player_no", ":player_team", "$g_prison_cart_previous_point"),
            (else_try),
                (try_begin),
                    (gt, ":bot_count", 0),
                    (call_script, "script_multiplayer_get_spawn_point_close_to_bots", ":player_no"),
                    (player_spawn_new_agent, ":player_no", reg0),

                    # spawn requested bots
                    (call_script, "script_multiplayer_get_spawn_point_close_to_bots", ":player_no"),
                    (call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":player_no", ":player_team", reg0),
                (else_try),
                    (call_script, "script_multiplayer_find_spawn_point", ":player_team", 1, ":is_horseman"),
                    (assign, ":point_no", reg0),
                    (player_spawn_new_agent, ":player_no", ":point_no"),
                    (call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":player_no", ":player_team", ":point_no"),
                (end_try),
            (end_try),

            (try_begin),
                (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
                (gt, ":player_first_spawn", 0),
                #(player_set_slot, ":player_no", slot_player_join_time, ":player_join_time"),
                (player_set_slot, ":player_no", slot_player_first_spawn, 0),
            (try_end),








            (assign, reg0, 1),  # player spawned
        (else_try),
            (assign, reg0, 0),  # player not spawned
        (end_try),
    ]),

  # script_multiplayer_set_g_multiplayer_is_game_type_captain
  # Input: none
  # Output: none
  ("multiplayer_set_g_multiplayer_is_game_type_captain",
    [
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_coop),
        (assign, "$g_multiplayer_is_game_type_captain", 1),
     (else_try),
        (assign, "$g_multiplayer_is_game_type_captain", 0),
     (try_end),
  ]),





  # script_cf_multiplayer_can_buy_squad
  # Input: none
  # Output: reg0:can buy squad
  ("cf_multiplayer_can_buy_squad",
    [
      (assign, ":can_buy_squad", 0),
      (try_begin),
        (eq, "$g_multiplayer_is_game_type_captain", 1),
        (assign, ":can_buy_squad", 1),
      (try_end),
      # disable squad buying for second team
      # (try_begin),
        # (eq, ":can_buy_squad", 1),
        # (eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_battle),
        # (multiplayer_get_my_team, ":my_team"),
        # (eq, ":my_team", 1),
        # (assign, ":can_buy_squad", 0),
      # (try_end),
      (eq, ":can_buy_squad", 1),
  ]),

    # script_avarage_of_two_points
    # Input: pos1, pos2
    # Output: pos1
    ("avarage_of_two_points",
    [
        (position_get_x, ":x_pos1", pos1),
        (position_get_x, ":x_pos2", pos2),
        (val_add, ":x_pos1", ":x_pos2"),
        (val_div, ":x_pos1", 2),
        (position_set_x, pos1, ":x_pos1"),

        (position_get_y, ":y_pos1", pos1),
        (position_get_y, ":y_pos2", pos2),
        (val_add, ":y_pos1", ":y_pos2"),
        (val_div, ":y_pos1", 2),
        (position_set_y, pos1, ":y_pos1"),

        (position_get_z, ":z_pos1", pos1),
        (position_get_z, ":z_pos2", pos2),
        (val_add, ":z_pos1", ":z_pos2"),
        (val_div, ":z_pos1", 2),
        (position_set_z, pos1, ":z_pos1"),
    ]),

    # script_multiplayer_ccoop_start_player_and_squad_respawn_period
    # INPUT: arg1 = spawn_alive_player_squad
    # OUTPUT: none
    ("multiplayer_ccoop_start_player_and_squad_respawn_period",
    [
        (try_begin),
            (multiplayer_is_server),
            #(neq, "$g_multiplayer_ccoop_wave_no", 1),

            (store_script_param, "$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots", 1),

            # reset first spawn slot
            (get_max_players, ":max_players"),
            (try_for_range, ":player_no", 0, ":max_players"),
                (player_is_active, ":player_no"),
                #(neg|player_slot_eq, ":player_no", slot_player_first_spawn, -1),
                (try_begin),
                    (eq, "$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots", 1),
                    (player_set_slot, ":player_no", slot_player_first_spawn, 1),
                (else_try),
                    (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
                    (ge, ":player_first_spawn", 0),
                    (player_set_slot, ":player_no", slot_player_first_spawn, 1),
                (try_end),
                #(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_lock_companions, 1),
            (try_end),

            # start player&squad spawn period
            (assign, "$g_multiplayer_ccoop_spawn_player_and_squad_counter", 30),
        (try_end),
    ]),











    # script_multiplayer_upgrade_player_equipment
    # INPUT: arg1 = player_no
    # OUTPUT: none
    ("multiplayer_upgrade_player_equipment",
    [
        (store_script_param, ":player_no", 1),

        (assign, reg0, ":player_no"),
        (display_debug_message, "@{!}multiplayer_upgrade_player_equipment: {reg0}"),

        (player_get_troop_id, ":player_troop", ":player_no"),
        (player_get_agent_id, ":player_agent", ":player_no"),
        (player_get_gold, ":player_gold", ":player_no"),
        (try_for_range, ":cur_item_slot", 0, ek_horse), # don't include horse
            (store_add, ":cur_player_slot", ":cur_item_slot", slot_player_cur_selected_item_indices_begin),
            (store_add, ":cur_player_slot_i", ":cur_item_slot", slot_player_selected_item_indices_begin),
            (player_get_slot, ":cur_player_slot_i_item", ":player_no", ":cur_player_slot_i"),
            (agent_get_item_slot, ":agent_item", ":player_agent", ":cur_item_slot"),
            (try_begin),
                (this_or_next|lt, ":cur_player_slot_i_item", 0),
                (this_or_next|is_between, ":agent_item", coop_drops_begin, coop_new_items_end),
                (player_item_slot_is_picked_up, ":player_no", ":cur_item_slot"),
                (player_set_slot, ":player_no", ":cur_player_slot", -1),
                #(str_store_item_name, s0, ":agent_item"),
                #(display_message, "@setting {s0} as null"),
            (else_try),
                #(agent_get_item_slot, ":agent_item", ":player_agent", ":cur_item_slot"),
                (player_set_slot, ":player_no", ":cur_player_slot", ":agent_item"),
            (try_end),




        (try_end),
        (player_set_slot, ":player_no", slot_player_cur_selected_item_indices_begin + 8, -1), # mark horse as -1
        (call_script, "script_multiplayer_calculate_cur_selected_items_cost", ":player_no", 0),
        (assign, ":added_gold", reg0),
        #(display_message, "@gold to add: {reg0}"),
        (val_add, ":player_gold", ":added_gold"),

        (try_for_range, ":i_item", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
            (player_get_slot, ":selected_item_index", ":player_no", ":i_item"),
            (store_sub, ":i_cur_selected_item", ":i_item", slot_player_selected_item_indices_begin),
            (agent_get_item_slot, ":agent_item", ":player_agent", ":i_cur_selected_item"),
            (try_begin),
                (this_or_next|lt, ":selected_item_index", 0),
                (this_or_next|player_item_slot_is_picked_up, ":player_no", ":i_cur_selected_item"),
                (this_or_next|is_between, ":agent_item", coop_drops_begin, coop_new_items_end),
                (eq, ":i_cur_selected_item", ek_horse), # remove horse selection for this special case
                (assign, ":selected_item_index", -1),
            (try_end),
            (val_add, ":i_cur_selected_item", slot_player_cur_selected_item_indices_begin),
            (player_set_slot, ":player_no", ":i_cur_selected_item", ":selected_item_index"),
        (try_end),
        (assign, ":end_cond", 1000),









        (try_for_range, ":unused", 0, ":end_cond"),
            (call_script, "script_multiplayer_calculate_cur_selected_items_cost", ":player_no", 0),
            (assign, ":total_cost", reg0),
            (try_begin),
                (gt, ":total_cost", ":player_gold"),
                #downgrade one of the selected items
                #first normalize the prices
                #then prioritize some of the weapon classes for specific troop classes
                (call_script, "script_multiplayer_get_troop_class", ":player_troop"),
                (assign, ":player_troop_class", reg0),

                (assign, ":max_cost_value", 0),
                (assign, ":max_cost_value_index", -1),
                (try_for_range, ":i_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
                    (player_get_slot, ":item_id", ":player_no", ":i_item"),
                    (ge, ":item_id", 0), #might be -1 for horses etc.
                    (call_script, "script_multiplayer_get_item_value_for_troop", ":item_id", ":player_troop"),
                    (assign, ":item_value", reg0),
                    (store_sub, ":item_type", ":i_item", slot_player_cur_selected_item_indices_begin),
                    (try_begin), #items
                        (this_or_next|eq, ":item_type", 0),
                        (this_or_next|eq, ":item_type", 1),
                        (this_or_next|eq, ":item_type", 2),
                        (eq, ":item_type", 3),
                        (val_mul, ":item_value", 5),
                    (else_try), #head
                        (eq, ":item_type", 4),
                        (val_mul, ":item_value", 4),
                    (else_try), #body
                        (eq, ":item_type", 5),
                        (val_mul, ":item_value", 2),
                    (else_try), #foot
                        (eq, ":item_type", 6),
                        (val_mul, ":item_value", 8),
                    (else_try), #gloves
                        (eq, ":item_type", 7),
                        (val_mul, ":item_value", 8),
                    (else_try), #horse
                    #base value (most expensive)
                    (try_end),
                    (item_get_slot, ":item_class", ":item_id", slot_item_multiplayer_item_class),
                    (try_begin),
                        (eq, ":player_troop_class", multi_troop_class_infantry),
                        (this_or_next|eq, ":item_class", multi_item_class_type_sword),
                        (this_or_next|eq, ":item_class", multi_item_class_type_axe),
                        (this_or_next|eq, ":item_class", multi_item_class_type_blunt),
                        (this_or_next|eq, ":item_class", multi_item_class_type_war_picks),
                        (this_or_next|eq, ":item_class", multi_item_class_type_two_handed_sword),
                        (this_or_next|eq, ":item_class", multi_item_class_type_small_shield),
                        (eq, ":item_class", multi_item_class_type_two_handed_axe),
                        (val_div, ":item_value", 2),
                    (else_try),
                        (eq, ":player_troop_class", multi_troop_class_spearman),
                        (this_or_next|eq, ":item_class", multi_item_class_type_spear),
                        (eq, ":item_class", multi_item_class_type_large_shield),
                        (val_div, ":item_value", 2),
                    (else_try),
                        (eq, ":player_troop_class", multi_troop_class_cavalry),
                        (this_or_next|eq, ":item_class", multi_item_class_type_lance),
                        (this_or_next|eq, ":item_class", multi_item_class_type_sword),
                        (eq, ":item_class", multi_item_class_type_horse),
                        (val_div, ":item_value", 2),
                    (else_try),
                        (eq, ":player_troop_class", multi_troop_class_archer),
                        (this_or_next|eq, ":item_class", multi_item_class_type_bow),
                        (eq, ":item_class", multi_item_class_type_arrow),
                        (val_div, ":item_value", 2),
                    (else_try),
                        (eq, ":player_troop_class", multi_troop_class_crossbowman),
                        (this_or_next|eq, ":item_class", multi_item_class_type_crossbow),
                        (eq, ":item_class", multi_item_class_type_bolt),
                        (val_div, ":item_value", 2),
                    (else_try),
                        (eq, ":player_troop_class", multi_troop_class_mounted_archer),
                        (this_or_next|eq, ":item_class", multi_item_class_type_bow),
                        (this_or_next|eq, ":item_class", multi_item_class_type_arrow),
                        (eq, ":item_class", multi_item_class_type_horse),
                        (val_div, ":item_value", 2),
                    (else_try),
                        (eq, ":player_troop_class", multi_troop_class_mounted_crossbowman),
                        (this_or_next|eq, ":item_class", multi_item_class_type_crossbow),
                        (this_or_next|eq, ":item_class", multi_item_class_type_bolt),
                        (eq, ":item_class", multi_item_class_type_horse),
                        (val_div, ":item_value", 2),
                    (try_end),

                    (try_begin),
                        (gt, ":item_value", ":max_cost_value"),
                        (assign, ":max_cost_value", ":item_value"),
                        (assign, ":max_cost_value_index", ":i_item"),
                    (try_end),
                (try_end),

                #max_cost_value and max_cost_value_index will definitely be valid
                #unless no items are left (therefore some items must cost 0 gold)
                (player_get_slot, ":item_id", ":player_no", ":max_cost_value_index"),
                (call_script, "script_multiplayer_get_previous_item_for_item_and_troop", ":item_id", ":player_troop"),
                (assign, ":item_id", reg0),
                (player_set_slot, ":player_no", ":max_cost_value_index", ":item_id"),
            (else_try),


                (assign, ":end_cond", 0),
                (assign, ":total_cost", reg0),
                #(display_message, "@total_cost: {reg0}"),
                (val_sub, ":player_gold", ":total_cost"),
                (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
                (try_for_range, ":i_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
                    (player_get_slot, ":item_id", ":player_no", ":i_item"),



                    # add the item to agent
                    (try_begin),
                        (ge, ":item_id", 0),

                        (store_sub, ":item_slot", ":i_item", slot_player_cur_selected_item_indices_begin),
                        #(store_add, ":i_actual_selected_item", ":item_slot", slot_player_selected_item_indices_begin),
                        #(player_slot_ge, ":player_no", ":i_actual_selected_item", 0),
                        (agent_get_item_slot, ":agent_item", ":player_agent", ":item_slot"),
                        (neq, ":agent_item", ":item_id"),

                        (neg|is_between, ":agent_item", coop_drops_begin, coop_new_items_end),

                        (get_max_players, ":num_players"),
                        (try_begin),
                            (ge, ":agent_item", 0),

                            (agent_unequip_item, ":player_agent", ":agent_item", ":item_slot"),

                            (try_for_range, ":cur_player", 1, ":num_players"),
                                (player_is_active, ":cur_player"),
                                (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_unequip_item,
                                    ":player_agent", ":agent_item", ":item_slot"),
                            (try_end),
                        (try_end),
                        (agent_equip_item, ":player_agent", ":item_id"),

                        (try_for_range, ":cur_player", 1, ":num_players"),
                            (player_is_active, ":cur_player"),
                            (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_equip_item,
                                ":player_agent", ":item_id"),
                        (try_end),

                    (try_end),
                (try_end),
                (player_set_slot, ":player_no", slot_player_total_equipment_value, ":total_cost"),
            (try_end),
        (try_end),
    ]),

    # script_cf_multiplayer_upgrade_companion_equipment
    # INPUT: arg1 = agent_no
    # OUTPUT: none
    ("cf_multiplayer_upgrade_companion_equipment",
    [
     (store_script_param, ":agent_no", 1),
     #(agent_is_human, ":agent_no"),
     #(agent_is_alive, ":agent_no"),
     #(agent_is_non_player, ":agent_no"),
     #(agent_get_team, ":team_no", ":agent_no"),

     (agent_get_group, ":agent_group", ":agent_no"),
     (player_is_active, ":agent_group"),
     (agent_get_troop_id, ":troop_no", ":agent_no"),

     #(assign, reg0, ":troop_no"),
     #(display_message, "@troop no: {reg0}"),

     (assign, ":matching_companion_found", 0),

     (try_for_range, ":cur_slot", slot_player_companion_ids_begin, slot_player_companion_ids_end),
       (player_get_slot, ":companion_no", ":agent_group", ":cur_slot"),
       (eq, ":troop_no", ":companion_no"),
       (assign, ":matching_companion_found", 1),
       #(display_message, "@pass"),
       (val_sub, ":cur_slot", slot_player_companion_ids_begin),
       (val_add, ":cur_slot", slot_player_companion_levels_begin),
       (player_get_slot, ":companion_level", ":agent_group", ":cur_slot"),
       (val_sub, ":cur_slot", slot_player_companion_levels_begin),
       (val_add, ":cur_slot", slot_player_companion_classes_begin),
       (player_get_slot, ":companion_template", ":agent_group", ":cur_slot"),
     (try_end),

     #(try_begin),
     #  (ge, ":companion_template", 0),
     #  (str_store_troop_name, s0, ":companion_template"),
     #  (multiplayer_send_string_to_player, ":agent_group", multiplayer_event_show_server_message, "@{!}companion template identified as {s0}"),
     #(try_end),

     (eq, ":matching_companion_found", 1),

     (try_begin),
       (is_between, ":companion_template", multiplayer_coop_class_templates_begin, multiplayer_coop_class_templates_end),
       (assign, ":multiplier", 18),
     (else_try),
       (assign, ":multiplier", 16),
     (try_end),

     (try_begin),
       (lt, ":companion_level", 3),
       (store_mul, ":template_leveler", ":companion_level", ":multiplier"),
       (val_add, ":companion_template", ":template_leveler"),
     (else_try),
       (store_mul, ":template_leveler", 3, ":multiplier"), #4 is max level
       (val_add, ":companion_template", ":template_leveler"),
     (try_end),

     #(try_begin),
     #  (ge, ":companion_template", 0),
     #  (str_store_troop_name, s0, ":companion_template"),
     #  (multiplayer_send_string_to_player, ":agent_group", multiplayer_event_show_server_message, "@{!}companion template multiplied to {s0}"),
     #(try_end),

     #(assign, reg0, ":companion_template"),
     #(display_message, "@companion template: {reg0}"),

     (assign, ":has_special_melee", 0),
     (assign, ":has_special_ranged", 0),
     #(eq, ":team_no", 0),

     (troop_equip_items, ":companion_template"),
     (get_max_players, ":num_players"),

     (try_for_range, ":cur_slot", 0, 4),
       (agent_get_item_slot, ":item_id", ":agent_no", ":cur_slot"),
       (ge, ":item_id", 0),
       (try_begin),
         (is_between, ":item_id", coop_drops_begin, coop_new_items_end),
         #(assign, reg0, ":agent_no"),
         #(assign, reg1, ":cur_slot"),
         #(assign, reg2, ":item_id"),
         #(display_message, "@special item on companion! agent: {reg0} slot: {reg1} item: {reg2}"),
         (item_get_type, ":item_type", ":item_id"),
         (try_begin),
           (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
           (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
           (eq, ":item_type", itp_type_polearm),
           (assign, ":has_special_melee", 1),
         (else_try),
           (this_or_next|eq, ":item_type", itp_type_bow),
           (this_or_next|eq, ":item_type", itp_type_crossbow),
           (eq, ":item_type", itp_type_thrown),
           (assign, ":has_special_ranged", 1),
         (try_end),
       (else_try),
         (agent_unequip_item, ":agent_no", ":item_id", ":cur_slot"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_unequip_item,
             ":agent_no", ":item_id", ":cur_slot"),
         (try_end),
       (try_end),
     (try_end),

     (try_for_range, ":cur_slot", 0, 9),
       #(ge, ":item_id", 0),

       (troop_get_inventory_slot, ":cur_item", ":companion_template", ":cur_slot"),
       #(assign, reg0, ":cur_item"),
       #(display_message, "@item from template {reg0}"),
       (gt, ":cur_item", 0),
       #(str_store_item_name, s0, ":cur_item"),
       #(multiplayer_send_string_to_player, ":agent_group", multiplayer_event_show_server_message, "@{!}companion template has item {s0}"),
       (item_get_type, ":cur_item_type", ":cur_item"),
       (try_begin),
         (is_between, ":cur_item_type", itp_type_head_armor, itp_type_pistol),
         (assign, ":found_matching_armor_piece", 0),
         (try_for_range, ":cur_equipped_slot", 4, 8),
           (agent_get_item_slot, ":cur_item_equipped", ":agent_no", ":cur_equipped_slot"),
           (ge, ":cur_item_equipped", 0),
           (item_get_type, ":cur_item_equipped_type", ":cur_item_equipped"),
           (eq, ":cur_item_type", ":cur_item_equipped_type"),
           #(str_store_item_name, s1, ":cur_item_equipped"),
           (assign, ":found_matching_armor_piece", 1),
           (neq, ":cur_item_equipped", ":cur_item"),
           #(multiplayer_send_string_to_player, ":agent_group", multiplayer_event_show_server_message, "@{!}found matching armour piece {s1}"),
           #(display_message, "@found_matching_armor_piece"),
           (neg|is_between, ":cur_item_equipped", coop_drops_begin, coop_new_items_end),
           (agent_unequip_item, ":agent_no", ":cur_item_equipped", ":cur_equipped_slot"),
           (try_for_range, ":cur_player", 1, ":num_players"),
             (player_is_active, ":cur_player"),
             (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_unequip_item,
               ":agent_no", ":cur_item_equipped", ":cur_equipped_slot"),
           (try_end),
           (agent_equip_item, ":agent_no", ":cur_item"),
           #(multiplayer_send_string_to_player, ":agent_group", multiplayer_event_show_server_message, "@{!}equipping {s0}"),
           (try_for_range, ":cur_player", 1, ":num_players"),
             (player_is_active, ":cur_player"),
             (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_equip_item,
               ":agent_no", ":cur_item"),
           (try_end),
         (try_end),
         (try_begin),
           (eq, ":found_matching_armor_piece", 0),
           (agent_equip_item, ":agent_no", ":cur_item"),
           (try_for_range, ":cur_player", 1, ":num_players"),
             (player_is_active, ":cur_player"),
             (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_equip_item,
               ":agent_no", ":cur_item"),
           (try_end),
         (try_end),
       (else_try),
         (assign, ":equip_cur_item", 0),
         (try_begin),
           (this_or_next|eq, ":cur_item_type", itp_type_one_handed_wpn),
           (this_or_next|eq, ":cur_item_type", itp_type_two_handed_wpn),
           (this_or_next|eq, ":cur_item_type", itp_type_shield),
           (eq, ":cur_item_type", itp_type_polearm),
           (eq, ":has_special_melee", 0),
           (assign, ":equip_cur_item", 1),
         (else_try),
           (this_or_next|eq, ":cur_item_type", itp_type_bow),
           (this_or_next|eq, ":cur_item_type", itp_type_crossbow),
           (this_or_next|eq, ":cur_item_type", itp_type_thrown),
           (this_or_next|eq, ":cur_item_type", itp_type_bolts),
           (eq, ":cur_item_type", itp_type_arrows),
           (eq, ":has_special_ranged", 0),
           (assign, ":equip_cur_item", 1),
         (try_end),
         (eq, ":equip_cur_item", 1),
         #(multiplayer_send_string_to_player, ":agent_group", multiplayer_event_show_server_message, "@{!}equipping {s0}"),
         (agent_equip_item, ":agent_no", ":cur_item"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_equip_item,
             ":agent_no", ":cur_item"),
         (try_end),
         #(try_end),
       (try_end),
     (try_end),

    ]),

































   #script_mp_spawn_coop_companion
   ("mp_spawn_coop_companion", #this code is to make sure that companions spawn with or without their horse depending on their class/map
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":troop_no", 2),
      (store_script_param, ":slot_no", 3),
      (store_script_param, ":player_team", 4),
      (store_script_param, ":point_no", 5),

      (troop_equip_items, ":troop_no"),









      (val_add, ":slot_no", 2),
      (player_get_slot, ":class_id", ":player_no", ":slot_no"),

      (assign, ":has_horse", 0),

      (try_for_range, ":cur_slot", 0, 9), #check if the class they are spawning as is mounted (default classes/personal equipment always has a horse)
        (eq, ":has_horse", 0),
        (troop_get_inventory_slot, ":cur_item", ":class_id", ":cur_slot"),
        (gt, ":cur_item", 0),
        (item_get_type, ":cur_item_type", ":cur_item"),
        (eq, ":cur_item_type", itp_type_horse),
        (assign, ":has_horse", 1), #found a horse!
      (try_end),





      (store_current_scene, ":cur_scene"),
      (scene_get_slot, ":scene_disallow_horses", ":cur_scene", slot_scene_ccoop_disallow_horses), #this is set as 1 for all maps that should be played without horses

      (try_for_range, ":cur_slot", 0, 9),
        (troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_slot"),
        (ge, ":cur_item", 0),
        (item_get_type, ":cur_item_type", ":cur_item"),
        (troop_remove_item, ":troop_no", ":cur_item"),
        (try_begin),
          (eq, ":cur_item_type", itp_type_horse),
          (troop_set_slot, ":troop_no", slot_troop_coop_lord_spawned, ":cur_item"),
        (else_try),
          (val_add, ":cur_slot", multi_data_equipment_holder_begin),
          (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":cur_item"),
        (try_end),
      (try_end),






      (troop_clear_inventory, ":troop_no"),

      (try_for_range, ":cur_slot", multi_data_equipment_holder_begin, multi_data_equipment_holder_end),
        (troop_get_slot, ":cur_item", "trp_multiplayer_data", ":cur_slot"),
        (gt, ":cur_item", 0),
        (troop_add_item, ":troop_no", ":cur_item"),
      (try_end),







      (try_begin),
        (eq, ":scene_disallow_horses", 0),
        (eq, ":has_horse", 1),
        (troop_get_slot, ":horse_no", ":troop_no", slot_troop_coop_lord_spawned),
        (troop_add_item, ":troop_no", ":horse_no"),
        (troop_set_slot, ":troop_no", slot_troop_coop_lord_spawned, -1),
      (try_end),

      (troop_equip_items, ":troop_no"),

      (modify_visitors_at_site, ":cur_scene"),
      (add_visitors_to_current_scene, ":point_no", ":troop_no", 1, ":player_team", ":player_no"),

















     ]),

  #script_coop_generate_item_drop
  # INPUT: none
  # OUTPUT: reg0 = item_id
  ("coop_generate_item_drop",
   [
     (store_script_param, ":player_id", 1),
     #(store_script_param, ":instance_id", 1),
     #(store_script_param, ":user_id", 2),

     (store_random_in_range, "$g_ccoop_currently_dropping_item", coop_drops_begin, coop_drops_end), #change this to add variation to the items that drop - any item should work! The description will be hidden for regular items
     #(assign, "$g_ccoop_currently_dropping_item", "itm_javelin_bow"), ##DEBUG - makes chests always drop the same item - useful for testing!
     (player_set_slot, ":player_id", slot_player_coop_dropped_item, "$g_ccoop_currently_dropping_item"), #we hold the item in a slot, server-side, to prevent funny business!
     #(assign, reg0, ":dropped_item"),









     ]),

  #script_coop_drop_item
  # INPUT: arg1 = item_id
  # OUTPUT: none
  ("coop_drop_item",
   [
     (store_script_param, reg0, 1),
     (store_script_param, reg1, 2),
     (store_script_param, reg2, 3),

     #script simply starts the presentation but could have extra features added

     (start_presentation, "prsnt_coop_assign_drop_to_group_member"),









     ]),

  #try brackets for this need to be checked and rearranged
  #script_cf_coop_give_item_to_assigned_group_member
  # INPUT: arg1 = item_id, arg2 = item_id
  # OUTPUT: none
  ("cf_coop_give_item_to_assigned_group_member",
   [
     (store_script_param, ":player_no", 1),
     (store_script_param, ":assigned_agent_id", 2),
     (player_is_active, ":player_no"),

     (assign, ":cancel_drop", 0), #script can be awkward because it relies on data sent by clients!

































     (assign, ":total_to_be_equipped", 0), #we need to check how many weapon slots the player is using and drop the item if there isn't enough space

     (player_get_slot, ":item_id", ":player_no", slot_player_coop_dropped_item),
     (ge, ":item_id", 0), #we should also make sure that the item is real - this is kept server side but bad code can change slots accidentally! ehem...

     (try_begin),
       (eq, ":assigned_agent_id", 0), #this is sent as 0, when the client wants to equip the item to their own character - behaviour for players and companions is different
       (player_get_agent_id, ":assigned_agent_id", ":player_no"), #but we need the agent id anyway...
       (assign, ":group_id", ":player_no"),
       (try_begin),
         (agent_is_active, ":assigned_agent_id"),
         (agent_is_alive, ":assigned_agent_id"), #let's make sure they didn't die at a bad time!
         (assign, ":num_equipped_weapons", 0),
         (item_get_slot, ":item_has_ammo", ":item_id", slot_item_ccoop_has_ammo), #javelin bow needs two slots (one for ammo) - if the player doesn't have room for both, we just drop everything
         (val_add, ":item_has_ammo", 1), #we use this variable but a better name would be something like ":wep_slots_required" - all weapons need at least one
         (try_for_range, ":cur_slot", 0, 4),
           (agent_get_item_slot, ":cur_item", ":assigned_agent_id", ":cur_slot"),
           (ge, ":cur_item", 0),
           (val_add, ":num_equipped_weapons", 1), #count how many weapon slots they are using
         (try_end),
         (try_begin),
           (item_get_type, ":item_type", ":item_id"),
           (ge, ":item_type", itp_type_head_armor),
           (assign, ":item_has_ammo", 0), #armours always overwrite the existing item
         (try_end),

         (store_add, ":total_to_be_equipped", ":num_equipped_weapons", ":item_has_ammo"), #save the total weapon slots that would be required if we equipped this weapon
       (else_try),
         (assign, ":cancel_drop", 1),
         (player_set_slot, ":player_no", slot_player_coop_dropped_item, -1),
       (try_end),
     (else_try),
       (agent_is_active, ":assigned_agent_id"), #if the assignee isn't the player, let's make sure it's a real agent anyway
       (agent_is_alive, ":assigned_agent_id"),
       (agent_is_human, ":assigned_agent_id"),
       (agent_get_group, ":group_id", ":assigned_agent_id"), #we use this in a check below
     (else_try), #fail script
       (assign, ":cancel_drop", 1),
       (player_set_slot, ":player_no", slot_player_coop_dropped_item, -1),
     (try_end),

     (eq, ":cancel_drop", 0),





     (try_begin),
       (gt, ":total_to_be_equipped", 4), #if we don't have room, the item falls to the floor... grab it, quick!
       (assign, ":cancel_drop", 1),
       (player_set_slot, ":player_no", slot_player_coop_dropped_item, -1), #keep this slot empty while players aren't assigning an item - otherwise a script could allow them to assign it later, which is cheating!
       (agent_get_position, pos1, ":assigned_agent_id"),
       (position_move_z, pos1, 20), #prevents the item from spawning in the ground... most of the time
       (set_spawn_position, pos1),
       (spawn_item, ":item_id"),
       (str_store_string, s0, "str_ccoop_dropping_item_on_ground"),
       (multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, s0), #tell the player what's happened
       (try_begin),
         (eq, ":item_id", "itm_javelin_bow"),
         (spawn_item, "itm_javelin_bow_ammo"), #and give them the ammo from the jav bow!
       (try_end),
     (try_end),

     (eq, ":cancel_drop", 0), #are we still good?

     (get_max_players, ":num_players"), #we'll be using this in our equipping events

     (try_begin),
       (eq, ":group_id", ":player_no"), #just in case a player tries to assign a drop to someone else's companion!

       (player_is_active, ":group_id"), #let's not have an error in case they disconnected

       (item_get_type, ":item_type", ":item_id"), #different behaviour for weapons/armour etc.

       (try_begin), #for non players, remove existing weapons that are melee/ranged so they always only have one of each
         (agent_is_non_player, ":assigned_agent_id"),



         (try_begin),
           (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
           (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
           (eq, ":item_type", itp_type_polearm),
           (try_for_range, ":cur_slot", 0, 4),
             (agent_get_item_slot, ":cur_item", ":assigned_agent_id", ":cur_slot"),
             (ge, ":cur_item", 0),
             (item_get_type, ":cur_item_type", ":cur_item"),
             (this_or_next|eq, ":cur_item_type", itp_type_one_handed_wpn),
             (this_or_next|eq, ":cur_item_type", itp_type_two_handed_wpn),
             (this_or_next|eq, ":cur_item_type", itp_type_shield),
             (eq, ":cur_item_type", itp_type_polearm),
             (agent_unequip_item, ":assigned_agent_id", ":cur_item", ":cur_slot"),
             (try_for_range, ":cur_player", 0, ":num_players"),
               (player_is_active, ":cur_player"),
               (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_unequip_item,
                ":assigned_agent_id", ":cur_item", ":cur_slot"),
             (try_end),
           (try_end),
         (else_try),
           (this_or_next|eq, ":item_type", itp_type_bow),
           (this_or_next|eq, ":item_type", itp_type_crossbow),
           (eq, ":item_type", itp_type_thrown),
           (try_for_range, ":cur_slot", 0, 4),
             (agent_get_item_slot, ":cur_item", ":assigned_agent_id", ":cur_slot"),
             (ge, ":cur_item", 0),
             (item_get_type, ":cur_item_type", ":cur_item"),
             (this_or_next|eq, ":cur_item_type", itp_type_bow),
             (this_or_next|eq, ":cur_item_type", itp_type_crossbow),
             (this_or_next|eq, ":cur_item_type", itp_type_thrown),
             (this_or_next|eq, ":cur_item_type", itp_type_bolts),
             (eq, ":cur_item_type", itp_type_arrows),
             (agent_unequip_item, ":assigned_agent_id", ":cur_item", ":cur_slot"),
             (try_for_range, ":cur_player", 0, ":num_players"),
               (player_is_active, ":cur_player"),
               (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_unequip_item,
                ":assigned_agent_id", ":cur_item", ":cur_slot"),
             (try_end),
           (try_end),
         (try_end),
       (try_end),

       ##should be set as script to be called with above network messages
       (try_begin),
         (is_between, ":item_type", itp_type_head_armor, itp_type_pistol), #for armours we always replace the existing item directly
         (try_for_range, ":cur_slot", 4, 8),
           (agent_get_item_slot, ":cur_item", ":assigned_agent_id", ":cur_slot"),
           (ge, ":cur_item", 0),
           (item_get_type, ":cur_item_type", ":cur_item"),
           (eq, ":cur_item_type", ":item_type"),
           (agent_unequip_item, ":assigned_agent_id", ":cur_item"),
           (try_for_range, ":cur_player", 0, ":num_players"),
             (player_is_active, ":cur_player"),
             (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_unequip_item,
                ":assigned_agent_id", ":cur_item", ":cur_slot"),
           (try_end),
           (try_begin), #and we shouldn't forget to remove their special effects!
             (eq, ":cur_item", "itm_running_boots"),
             (agent_set_speed_modifier, ":assigned_agent_id", 100),
           (else_try),
             (eq, ":cur_item", "itm_power_gloves"),
             (agent_set_damage_modifier, ":assigned_agent_id", 100),
           (end_try),
         (try_end),
       (try_end),

       (agent_equip_item, ":assigned_agent_id", ":item_id"), #and now we're ready to equip the item
       (try_for_range, ":cur_player", 0, ":num_players"),
         (player_is_active, ":cur_player"),
         (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_equip_item,
           ":assigned_agent_id", ":item_id"),
       (try_end),

       #additional items and effects
       (try_begin),
         (eq, ":item_id", "itm_javelin_bow"),
         (agent_equip_item, ":assigned_agent_id", "itm_javelin_bow_ammo"),
         (try_for_range, ":cur_player", 0, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_equip_item,
             ":assigned_agent_id", "itm_javelin_bow_ammo"),	#don't forget to add the ammo for the javelin bow!
         (try_end),
       (else_try),
         (eq, ":item_id", "itm_running_boots"), #and add any new effects...
         (agent_set_speed_modifier, ":assigned_agent_id", 150),
       (else_try),
         (eq, ":item_id", "itm_power_gloves"),
         (agent_set_damage_modifier, ":assigned_agent_id", 150),
       (else_try),
         (eq, ":item_id", "itm_kicking_boots"),
         (agent_is_non_player, ":assigned_agent_id"),
         (agent_set_kick_allowed, ":assigned_agent_id", 1),
       (try_end),
     (try_end),

     (player_set_slot, ":player_no", slot_player_coop_dropped_item, -1), #again, prevent players from trying to equip items when they shouldn't

     ]),

  #script_add_player_to_cur_tableau_for_coop
  # INPUT: type
  # OUTPUT: none
  ("add_player_to_cur_tableau_for_coop", [ #we use this for the image of the player when assigning an item from a chest
    #(store_script_param, ":troop_no", 1),
    #(store_script_param, ":canvas_no", 2),
    (cur_tableau_set_override_flags, af_override_everything),

    (multiplayer_get_my_player, ":my_player_no"),

    (assign, ":canvas_no", "trp_coop_companion_equipment_ui_0"),

    (player_get_agent_id, ":my_agent_no", ":my_player_no"), #player is always alive so we just show their current equipment

    (try_for_range, ":cur_inv_slot", 0, 8),
      (agent_get_item_slot, ":cur_item", ":my_agent_no", ":cur_inv_slot"),
      (ge, ":cur_item", 0),
      (cur_tableau_add_override_item, ":cur_item"),
    (try_end),









    (try_begin),
      (player_get_gender , ":is_female", ":my_player_no"),
      (eq, ":is_female", 1),
      (val_add, ":canvas_no", 1),
    (try_end),

    #(assign, reg0, ":canvas_no"),
    #(display_message, "@canvas no: {reg0}"),

    (str_store_player_face_keys, s0, ":my_player_no"),
    (troop_set_face_keys, ":canvas_no", s0),

    (store_mod, ":animation", ":my_agent_no", 4),

    (val_add, ":animation", "anim_pose_1"),

















    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
    (assign, ":cam_height", 145),
    (assign, ":camera_distance", 350),
    (assign, ":camera_pitch", 2),

    (init_position, pos5),
    (position_set_z, pos5, ":cam_height"),
    # camera looks towards -z axis
    (position_rotate_x, pos5, -90),
    (position_rotate_z, pos5, 180),
    # now apply yaw and pitch
    (assign, ":camera_yaw", -50),
    (position_move_x, pos5, -10, 0),
    (position_rotate_y, pos5, ":camera_yaw"),
    (position_rotate_x, pos5, ":camera_pitch"),
    (position_move_z, pos5, ":camera_distance", 0),
    (position_move_y, pos5, 60, 0),









    (init_position, pos2),
    (cur_tableau_add_troop, ":canvas_no", pos2, ":animation", 0),
    (cur_tableau_set_camera_position, pos5),

    (copy_position, pos8, pos5),
    (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
    (position_rotate_z, pos8, 30),
    (position_rotate_x, pos8, -50),
    (cur_tableau_add_sun_light, pos8, 175,150,125),
    ]),

  #script_add_troop_to_cur_tableau_for_coop
  # INPUT: type
  # OUTPUT: none
  ("add_troop_to_cur_tableau_for_coop", [
    (store_script_param, ":troop_no", 1),
    #(store_script_param, ":canvas_no", 2),
    (cur_tableau_set_override_flags, af_override_everything),

    (multiplayer_get_my_player, ":my_player_no"),
    (assign, ":companion_alive", 0),
    (assign, ":canvas_no", "trp_coop_companion_equipment_ui_0"), #we use different troops for each companion... for simplicity
    (try_for_agents, ":cur_agent"), #lets find the agent for our companion
      (eq, ":companion_alive", 0),
      (agent_is_active, ":cur_agent"), #living companions show their current equipment, while dead companions show what they're going to spawn with next
      (agent_is_alive, ":cur_agent"),
      (agent_is_non_player, ":cur_agent"),
      (agent_get_troop_id, ":cur_troop_id", ":cur_agent"),
      (eq, ":cur_troop_id", ":troop_no"),
      (agent_get_group, ":cur_agent_group", ":cur_agent"),
      (eq, ":cur_agent_group", ":my_player_no"),
      (try_for_range, ":cur_slot", slot_player_companion_ids_begin, slot_player_companion_ids_end),
        (player_slot_eq, ":my_player_no", ":cur_slot", ":cur_troop_id"),
        (try_for_range, ":cur_inv_slot", 0, 8),
          (agent_get_item_slot, ":cur_item", ":cur_agent", ":cur_inv_slot"),
          (ge, ":cur_item", 0),
          (cur_tableau_add_override_item, ":cur_item"),
        (try_end),
        (try_begin),
          (gt, ":cur_slot", slot_player_companion_ids_begin),
          (val_add, ":canvas_no", 2),
        (try_end),
      (try_end),
      (assign, ":companion_alive", 1), #so we'll be using their current gear for the tableau
    (try_end),

    (try_begin),
      (eq, ":companion_alive", 0), #for dead companions, we check their class and level to get the right template
      (try_for_range, ":cur_slot", slot_player_companion_ids_begin, slot_player_companion_ids_end),
        (player_slot_eq, ":my_player_no", ":cur_slot", ":troop_no"), #check which companion we're using (since this isn't sent as a parameter...)
        (try_begin),
          (gt, ":cur_slot", slot_player_companion_ids_begin),
          (val_add, ":canvas_no", 2), #the second companion uses different troops
        (try_end),
        (val_add, ":cur_slot", 2),
        (player_get_slot, ":template_no", ":my_player_no", ":cur_slot"), #get their class
        (val_add, ":cur_slot", 2),
        (player_get_slot, ":level_no", ":my_player_no", ":cur_slot"), #and upgrade it for their level
        (try_begin),
          (ge, ":template_no", "trp_npc1_1"), #companion class troops come after faction class troops
          (val_mul, ":level_no", 16), #there are 16 at each level tier (one for each companion) so multiply by 16 to get to the right level
          (val_add, ":template_no", ":level_no"),
        (else_try),
          (val_mul, ":level_no", 18), #18 at each level tier for faction classes (6 factions * 3 troops, one ranged, one melee, one cav)
          (val_add, ":template_no", ":level_no"),
        (try_end),
        (try_for_range, ":cur_inv_slot", 0, 8),
          (troop_get_inventory_slot, ":cur_item", ":template_no", ":cur_inv_slot"),
          (ge, ":cur_item", 0),
          (cur_tableau_add_override_item, ":cur_item"),
        (try_end),
      (try_end),
    (try_end),


    (try_begin),
      (troop_get_type, ":is_female", ":troop_no"),
      (eq, ":is_female", 1),
      (val_add, ":canvas_no", 1), #the female blank canvas troop is directly after the male for each companion... this line could be (val_add, ":canvas_no", ":is_female"),
    (try_end),


    #(assign, reg0, ":canvas_no"),
    #(display_message, "@canvas no: {reg0}"),

    (str_store_troop_face_keys, s0, ":troop_no"),
    (troop_set_face_keys, ":canvas_no", s0), #give the right face to the canvas...

    (try_begin), #these lines just add some variety to the poses - it's not really random but that would be complicated, since it needs to be consistent when this script is run for the alpha layer
      (eq, ":companion_alive", 1),
      (store_mod, ":animation", ":cur_agent", 4), #for alive troops, it uses the agent id, which is pretty close to random
    (else_try),
      (store_mod, ":animation", ":template_no", 4), #for dead troops it's based on the class
    (try_end),







    (val_add, ":animation", "anim_pose_1"), #there are a few poses after this one, which it chooses from















    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
    (assign, ":cam_height", 145),
    (assign, ":camera_distance", 350),
    (assign, ":camera_pitch", 2),

    (init_position, pos5),
    (position_set_z, pos5, ":cam_height"),
    # camera looks towards -z axis
    (position_rotate_x, pos5, -90),
    (position_rotate_z, pos5, 180),
    # now apply yaw and pitch
    (try_begin),
      (lt, ":canvas_no", "trp_coop_companion_equipment_ui_1"), #use different camera angles for each companion because it looks cooler - also it looks a bit weird if they face towards the edge of the screen
      (assign, ":camera_yaw", -50),
      (position_move_x, pos5, -10, 0),
    (else_try),
      (assign, ":camera_yaw", -10),
      (position_move_x, pos5, 10, 0),
    (try_end),
    (position_rotate_y, pos5, ":camera_yaw"),
    (position_rotate_x, pos5, ":camera_pitch"),
    (position_move_z, pos5, ":camera_distance", 0),
    (position_move_y, pos5, 60, 0),









    (init_position, pos2),
    (cur_tableau_add_troop, ":canvas_no", pos2, ":animation", 0),
    (cur_tableau_set_camera_position, pos5),

    (copy_position, pos8, pos5),
    (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
    (position_rotate_z, pos8, 30),
    (position_rotate_x, pos8, -50),
    (cur_tableau_add_sun_light, pos8, 175,150,125),
    ]),
   #INVASION MODE END

   
   
   #SB : update script moved here from triggers, so we can call from menu
   ("dplmc_version_checker",
   [
    (assign, ":save_reg0", reg0),
    (assign, ":save_reg1", reg1),
    ##diplomacy start+
    ##Add version checking, so the corrections are only applied once.
    ##This allows for more complicated things to be added here in the future
    #SB : coop troops added Dec. 2016, no SP change but troops need to be re-appended
    (troop_get_slot, ":diplomacy_version_code", "trp_dplmc_chamberlain", dplmc_slot_troop_affiliated), #I've arbitrarily picked "when I started tracking this" as 0
    (try_begin),
      (troop_is_hero, dplmc_prev_employee), #if the older savegame had diplomacy troops already (but were pushed down)
      (troop_get_slot, ":preversion_code", dplmc_prev_employee, dplmc_slot_troop_affiliated),
      (assign, reg0, ":diplomacy_version_code"),
      (assign, reg1, ":preversion_code"),
      (val_max, ":diplomacy_version_code", ":preversion_code"), #get the actual value from savegame
      # (store_mul, ":preversion_code", DPLMC_CURRENT_VERSION_CODE),
      # (troop_set_slot, dplmc_prev_employee, dplmc_slot_troop_affiliated, ":preversion_code"), #pre-set this to be copied over
      # (display_message, "@{reg0} vs {reg1}"),
      
      
      # #We need to fix all the slot values and troops in wrong parties (recruiters etc)
      # (assign, ":troop_no", dplmc_prev_employee),
      # (try_for_range, ":new_troop", dplmc_employees_begin, dplmc_employees_end),
        # (call_script, "script_dplmc_copy_inventory", ":troop_no", ":new_troop"), #move inv over, player might want to play around with treasury
        # (try_for_range, ":slot_no", 0, dplmc_slot_troop_affiliated + 1),
          # (troop_get_slot, ":old_value", ":troop_no", ":slot_no"),
          # (troop_set_slot, ":new_troop", ":slot_no", ":old_value"),
        # (try_end),
        # (val_add, ":troop_no", 1), #move up by 1
      # (try_end),
    (try_end),

    (store_mod, ":verification", ":diplomacy_version_code", 128),

    (try_begin),
      #Detect bad values
      (neq, ":diplomacy_version_code", 0),
      (neq, ":verification", 68),
      (assign, reg0, ":diplomacy_version_code"),
      (display_message, "@{!} A slot had an unexpected value: {reg0}.  This might be because you are using an incompatible troop list, or are using a non-native strange game.  This message will repeat daily."),
      (assign, ":diplomacy_version_code", -1),
    (else_try),
      (val_div, ":diplomacy_version_code", 128),
      #Update if necessary.
      (lt, ":diplomacy_version_code", DPLMC_CURRENT_VERSION_CODE),
      (try_begin), #SB : do not block
        (ge, "$cheat_mode", 1),
        (assign, reg0, ":diplomacy_version_code"),
        (assign, reg1, DPLMC_CURRENT_VERSION_CODE),
        (display_message, "@{!} DEBUG - Detected a new version of diplomacy: previous version was {reg0}, and current version is {reg1}.  Performing updates."),
      (try_end),
      (store_mul, ":version_code", DPLMC_CURRENT_VERSION_CODE, 128),
      (val_add, ":version_code", DPLMC_VERSION_LOW_7_BITS),
      (troop_set_slot, "trp_dplmc_chamberlain", dplmc_slot_troop_affiliated, ":version_code"),
    (try_end),

    (try_begin),
      (is_between, ":diplomacy_version_code", -1, 1),#-1 or 0
      #Native behavior follows
      ##diplomacy end+

      #this to correct string errors in games started in 1.104 or before
      (party_set_name, "p_steppe_bandit_spawn_point", "str_the_steppes"),
      (party_set_name, "p_taiga_bandit_spawn_point", "str_the_tundra"),
      (party_set_name, "p_forest_bandit_spawn_point", "str_the_forests"),
      (party_set_name, "p_mountain_bandit_spawn_point", "str_the_highlands"),
      (party_set_name, "p_sea_raider_spawn_point_1", "str_the_coast"),
      (party_set_name, "p_sea_raider_spawn_point_2", "str_the_coast"),
      (party_set_name, "p_desert_bandit_spawn_point", "str_the_deserts"),

      #this to correct inappropriate home strings - Katrin to Uxkhal, Matheld to Fearichen
      # (troop_set_slot, "trp_npc11", slot_troop_home, "p_town_7"),
      (troop_set_slot, "trp_npc8", slot_troop_home, "p_village_35"),

      (troop_set_slot, "trp_npc15", slot_troop_town_with_contacts, "p_town_20"), #durquba

      #this to correct linen production at villages of durquba
      (party_set_slot, "p_village_93", slot_center_linen_looms, 0), #mazigh
      (party_set_slot, "p_village_94", slot_center_linen_looms, 0), #sekhtem
      (party_set_slot, "p_village_95", slot_center_linen_looms, 0), #qalyut
      (party_set_slot, "p_village_96", slot_center_linen_looms, 0), #tilimsal
      (party_set_slot, "p_village_97", slot_center_linen_looms, 0), #shibal zumr
      (party_set_slot, "p_village_102", slot_center_linen_looms, 0), #tamnuh
      (party_set_slot, "p_village_109", slot_center_linen_looms, 0), #habba

      (party_set_slot, "p_village_67", slot_center_fishing_fleet, 0), #Tebandra
      (party_set_slot, "p_village_5", slot_center_fishing_fleet, 15), #Kulum

      ##diplomacy start+
      #End the changes in Native
    (try_end),

   #Behavior specific to a fresh Diplomacy version
    (try_begin),
      (ge, ":diplomacy_version_code", 0),#do not run this if the code is bad
      (lt, ":diplomacy_version_code", 1),

      #Add home centers for claimants (mods not using standard NPCs or map may wish to remove this)
      (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_home, "p_town_4"),#Lady Isolle - Suno
      (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_home, "p_town_11"),#Prince Valdym - Curaw
      (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_home, "p_town_18"),#Dustum Khan - Narra
      (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_home, "p_town_12"),#Lethwin Far-Seeker - Wercheg
      (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_home, "p_town_3"),#Lord Kastor - Veluca
      (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_home, "p_town_20"),#Arwa the Pearled One - Durquba
      #add ancestral fiefs to home slots (mods not using standard NPCs or map should remove this)
      (troop_set_slot, "trp_knight_2_10", slot_troop_home, "p_castle_29"), #Nelag_Castle
      (troop_set_slot, "trp_knight_3_4", slot_troop_home, "p_castle_30"), #Asugan_Castle
      (troop_set_slot, "trp_knight_1_3", slot_troop_home, "p_castle_35"), #Haringoth_Castle
      (troop_set_slot, "trp_knight_5_11", slot_troop_home, "p_castle_33"), #Etrosq_Castle
      #Also the primary six towns (mods not using standard NPCs or map may wish to remove this)
      (troop_set_slot, "trp_kingdom_1_lord", slot_troop_home, "p_town_6"),#King Harlaus to Praven
      (troop_set_slot, "trp_kingdom_2_lord", slot_troop_home, "p_town_8"),#King Yaroglek to Reyvadin
      (troop_set_slot, "trp_kingdom_3_lord", slot_troop_home, "p_town_10"),#Sanjar Khan to Tulga
      (troop_set_slot, "trp_kingdom_4_lord", slot_troop_home, "p_town_1"),#King Ragnar to Sargoth
      (troop_set_slot, "trp_kingdom_5_lord", slot_troop_home, "p_town_5"),#King Graveth to Jelkala
      (troop_set_slot, "trp_kingdom_6_lord", slot_troop_home, "p_town_19"),#Sultan Hakim to Shariz

      (call_script, "script_dplmc_init_domestic_policy"),
       #Set the "original lord" values corresponding to the above.
      (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (this_or_next|eq, ":troop_no", "trp_knight_2_10"),#Nelag
        (this_or_next|eq, ":troop_no", "trp_knight_3_4"),#Asugan
        (this_or_next|eq, ":troop_no", "trp_knight_1_3"),#Haringoth
        (this_or_next|eq, ":troop_no", "trp_knight_5_11"),#Etrosq
        (this_or_next|is_between, ":troop_no", kings_begin, kings_end),
        (is_between, ":troop_no", pretenders_begin, pretenders_end),

        (troop_get_slot, ":center_no", ":troop_no", slot_troop_home),
        (is_between, ":center_no", centers_begin, centers_end),
        (neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
        (party_set_slot, ":center_no",  dplmc_slot_center_original_lord, ":troop_no"),

        #Also set "ex-lord"
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neg|party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
        (neg|party_slot_ge, ":center_no", dplmc_slot_center_ex_lord, 1),
        (party_set_slot, ":center_no", dplmc_slot_center_ex_lord, ":troop_no"),
      (try_end),

      #Make sure the affiliation slot is set correctly.
      (try_begin),
        (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
        (troop_get_slot, ":slot_val", "$g_player_affiliated_troop", dplmc_slot_troop_affiliated),
        (is_between, ":slot_val", 0, 3),#0 is default, 1 is asked, in previous versions there was no use of 2
        (troop_set_slot, "$g_player_affiliated_troop", dplmc_slot_troop_affiliated, 3),#3 is affiliated
      (try_end),




      #Set father/mother slots for the unmarried medium-age lords, so checking for
      #being related will work as expected.
      (try_for_range, ":troop_no", lords_begin, lords_end),
        (troop_slot_eq, ":troop_no", slot_troop_father, -1),
        (troop_slot_eq, ":troop_no", slot_troop_mother, -1),
        (store_mul, ":father", ":troop_no", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),#defined in module_constants.py
        (val_add, ":father", DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),
        (troop_set_slot, ":troop_no", slot_troop_father, ":father"),
        (store_add, ":mother", ":father", DPLMC_VIRTUAL_RELATIVE_MOTHER_OFFSET - DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),
        (troop_set_slot, ":troop_no", slot_troop_mother, ":mother"),
      (try_end),

   #Fix kingdom lady daughters having "slot_troop_mother" set to themselves.
   #The old fix was in troop_get_family_relation_to_troop, but now we can
   #just do it once here.
   (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
		(try_begin),
			(troop_slot_eq, ":troop_no", slot_troop_mother, ":troop_no"),
			(troop_get_slot, ":father", ":troop_no", slot_troop_father),
			(try_begin),
				(is_between, ":father", active_npcs_begin, active_npcs_end),
				(troop_get_slot, ":mother", ":father", slot_troop_spouse),
				(troop_set_slot, ":troop_no", slot_troop_mother, ":mother"),
				(try_begin),
					#Print a message if desired
					(ge, "$cheat_mode", 1),
					(str_store_troop_name, s0, ":troop_no"),
					(display_message, "@{!}DEBUG - Fixed slot_troop_mother for {s0}."),
				(try_end),
			(else_try),
				(troop_set_slot, ":troop_no", slot_troop_mother, -1),#better than being set to herself
				#Print a message if desired
				(ge, "$cheat_mode", 1),
				(str_store_troop_name, s0, ":troop_no"),
				(display_message, "@{!}DEBUG - When fixing slot_troop_mother for {s0}, could not find a valid mother."),
			(try_end),
	#While we're at it, also give parents to the sisters of the middle-aged lords.
		(else_try),
			(troop_slot_eq, ":troop_no", slot_troop_father, -1),
			(troop_slot_eq, ":troop_no", slot_troop_mother, -1),
			#"Guardian" here means brother
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_guardian),
			(ge, ":guardian", 1),
			#Has brother's father
			(troop_get_slot, ":father", ":guardian", slot_troop_father),
			(troop_set_slot, ":troop_no", slot_troop_father, ":father"),
			#Has brother's mother
			(troop_get_slot, ":mother", ":guardian", slot_troop_mother),
			(troop_set_slot, ":troop_no", slot_troop_mother, ":mother"),
		(try_end),
   #Also set original factions for ladies.
	   (neg|troop_slot_ge, ":troop_no", slot_troop_original_faction, 1),
		(assign, ":guardian", -1),
		(try_begin),
		   (troop_slot_ge, ":troop_no", slot_troop_father, 1),
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_father),
 	   (else_try),
		   (troop_slot_ge, ":troop_no", slot_troop_guardian, 1),
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_guardian),
		(else_try),
		   (troop_slot_ge, ":troop_no", slot_troop_spouse, 1),
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_spouse),
	   (try_end),
		(ge, ":guardian", 1),
		(troop_get_slot, ":original_faction", ":guardian", slot_troop_original_faction),
		(troop_set_slot, ":troop_no", slot_troop_original_faction, ":original_faction"),
   (try_end),

	  ##Set relations between kingdom ladies and their relatives.
	  ##Do *not* initialize their relations with anyone they aren't related to:
	  ##that is used for courtship.
	  ##  The purpose of this initialization is so if a kingdom lady gets promoted,
	  ##her relations aren't a featureless slate.  Also, it would be interesting to
	  ##further develop the idea of ladies as pursuing agendas even if they aren't
	  ##leading warbands, which would benefit from giving them relations with other
	  ##people.
	  #
	  #Because relations may already exist, only call this in instances where
	  #they are 0 or 1 (the latter just means "met" between NPCs).
     (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
		(troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),
		(troop_get_slot, ":lady_faction", ":lady", slot_troop_original_faction),
		(ge, ":lady_faction", 1),

		(try_for_range, ":other_hero", heroes_begin, heroes_end),
		   (this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
			(this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
				(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_inactive_pretender),
			(troop_slot_eq, ":other_hero", slot_troop_original_faction, ":lady_faction"),

			#Because this is not a new game: first check if relations have developed
			(call_script, "script_troop_get_relation_with_troop", ":lady", ":other_hero"),
			(is_between, reg0, 0, 2),#0 or 1

			(try_begin),
				(this_or_next|troop_slot_eq, ":lady", slot_troop_spouse, ":other_hero"),
				(troop_slot_eq, ":other_hero", slot_troop_spouse, ":lady"),
				(store_random_in_range, reg0, 0, 11),
			(else_try),
				#(call_script, "script_troop_get_family_relation_to_troop", ":lady", ":other_hero"),
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":lady", ":other_hero"),
			(try_end),

			(call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", reg0),

			#This relation change only applies between kingdom ladies.
			(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
			(is_between, ":other_hero", kingdom_ladies_begin, kingdom_ladies_end),

			(store_random_in_range, ":random", 0, 11),
			(call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", ":random"),
		(try_end),
	  (try_end),

   #Change the occupation of exiled lords (not including pretenders or kings)
   (try_for_range, ":troop_no", lords_begin, lords_end),
		(store_troop_faction, ":faction_no", ":troop_no"),
		#A lord in the outlaw faction
		(eq, ":faction_no", "fac_outlaws"),
		#Possible values for his occupation if he's an exile (but there's some overlap between these and "bandit hero")
		(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#<- The default
		(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),#<- This can happen joining the player faction
			(troop_slot_eq, ":troop_no", slot_troop_occupation, 0),#<- This gets set for prisoners
		#(Quick Check) Not leading a party or the prisoner of a party or at a center
		(neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
		(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
		(neg|troop_slot_ge, ":troop_no", slot_troop_cur_center, 1),#deliberately 1 instead of 0
		#(Slow check) Does not own any fiefs
		(assign, ":end", centers_end),
		(try_for_range, ":center_no", centers_begin, ":end"),
			(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
			(assign, ":end", ":center_no"),#stop loop, and also signal failure
		(try_end),
		#(Slow check) Explicitly verify he is not a prisoner anywhere.
		(call_script, "script_search_troop_prisoner_of_party", ":troop_no"),
		(eq, reg0, -1),
		#(Slow check) Explicitly verify he's not a member of any party
		(assign, ":member_of_party", -1),
		(try_for_parties, ":party_no"),
			(eq, ":member_of_party", -1),
			(this_or_next|eq, ":party_no", "p_main_party"),
				(ge, ":party_no", centers_begin),
			(party_count_members_of_type, ":count", ":party_no", ":troop_no"),
			(gt, ":count", 0),
			(assign, ":member_of_party", ":party_no"),
		(try_end),
		(eq, ":member_of_party", -1),
		#Finally verified that he is in exile.  Set the slot value to make
		#this easier in the future.
		(troop_set_slot, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s0, ":troop_no"),
			(display_message, "@{!}DEBUG - Changed occupation of {s0} to dplmc_slto_exile"),
		(try_end),
   (try_end),




   #Initialize histories for supported pretenders.
   (try_for_range, ":troop_no", pretenders_begin, pretenders_end),
      (neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	  (troop_slot_eq, ":troop_no", slot_troop_playerparty_history, 0),
	  (troop_set_slot, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
   (try_end),

   #Initialize histories for promoted companions
   (try_for_range, ":troop_no", companions_begin, companions_end),
	  (neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	  (neg|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
	  (troop_set_slot, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
   (try_end),

   #For all centers, update new slots
   (try_for_range, ":center_no", centers_begin, centers_end),
	  #Last attacker
	  (try_begin),
	     (party_slot_eq, ":center_no", dplmc_slot_center_last_attacker, 0),
		 (party_slot_eq, ":center_no", dplmc_slot_center_last_attacked_time, 0),
		 (party_set_slot, ":center_no", dplmc_slot_center_last_attacker, -1),
	  (try_end),

      (party_slot_eq, ":center_no", dplmc_slot_center_last_transfer_time, 0),
	  #Ex-lord
	  (try_begin),
  	     (party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, 0),
	     (party_set_slot, ":center_no", dplmc_slot_center_ex_lord, -1),
	  (try_end),
	  #Original lord
	  (try_begin),
		(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, 0),
		(neg|troop_slot_eq, "trp_player", slot_troop_home, ":center_no"),
		(party_set_slot, ":center_no", dplmc_slot_center_original_lord, -1),
	  (try_end),
   (try_end),

   #Don't bother filling in "last caravan arrival" slots with fake values.
   #Right now the scripts check and do that automatically if they aren't
   #set.

      #Perform initialization for autoloot / autosell.
      (call_script, "script_dplmc_initialize_autoloot", 1),#argument "1" forces this to make changes

      #Fix a mistake I had introduced before, where you could get the wrong
      #"marry betrothed" quest when courting a lady.
      (try_begin),
        (check_quest_active, "qst_wed_betrothed_female"),
        (quest_get_slot, ":betrothed_troop", "qst_wed_betrothed_female", slot_quest_giver_troop),
        (is_between, ":betrothed_troop", kingdom_ladies_begin, kingdom_ladies_end),
        (display_message, "@{!}FIXED PROBLEM - Cancelled erroneous version of qst_wed_betrothed_female.  You should be able to marry normally if you try again."),
        (call_script, "script_abort_quest", "qst_wed_betrothed_female", 0),#abort with type 0 "event" should give no penalties to the player
      (try_end),
    #End version-checked block.
    (try_end),

    (try_begin),
      (is_between, ":diplomacy_version_code", 1, 110615),
    #Fix a bug that was introduced in some version before 2011-06-15 that made
    #all "young unmarried lords" only have half-siblings, with either their own
    #father or mother slot uninitialized.
    (try_begin),
      (lt, 31, heroes_begin),
      (neg|troop_slot_eq, 31, 31, 0),#"slot_troop_father" was 31 in those saved games
      (troop_set_slot, 31, 31, -1),#(it still is 31 as far as I know, but this code should remain the same even if the slot value changes)
    (try_end),
    (try_begin),
      (lt, 32, heroes_begin),
      (neg|troop_slot_eq, 32,32,0),#"slot_troop_mother" was 32 in those saved games
      (troop_set_slot, 32, 32, -1),
    (try_end),
    (try_for_range, ":troop_no", lords_begin, lords_end),
      (troop_get_slot, reg0, ":troop_no", slot_troop_father),
      (troop_get_slot, reg1, ":troop_no", slot_troop_mother),
      (try_begin),
        (is_between, reg0, lords_begin, lords_end),
        (neg|is_between, reg1, kingdom_ladies_begin, kingdom_ladies_end),
        (troop_get_slot, reg1, reg0, slot_troop_spouse),
        (is_between, reg1, kingdom_ladies_begin, kingdom_ladies_end),
        (troop_set_slot, ":troop_no", slot_troop_mother, reg1),
        (call_script, "script_update_troop_notes", ":troop_no"),#Doesn't actually do anything
      (else_try),
        (is_between, reg1, kingdom_ladies_begin, kingdom_ladies_end),
        (neg|is_between, reg0, lords_begin, lords_end),
        (troop_get_slot, reg0, reg1, slot_troop_spouse),
        (is_between, reg0, lords_begin, lords_end),
        (troop_set_slot, ":troop_no", slot_troop_father, reg0),
        (call_script, "script_update_troop_notes", ":troop_no"),#Doesn't actually do anything
      (try_end),
    (try_end),

    #For old saved games, a reputation bug that was introduced in the release 2011-06-06 and was fixed on 2011-06-07.
    (eq, ":diplomacy_version_code", 1),
    (assign, reg0, 0),
    (try_for_range, ":troop_no", lords_begin, lords_end),
      (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_none),
      (store_random_in_range, reg1, lrep_none, lrep_roguish),
      (val_max, reg1, lrep_none + 1),#So there's an extra chance of getting reputation 1, which is lrep_martial
      (troop_set_slot, ":troop_no", slot_lord_reputation_type, reg1),
      (val_add, reg0, 1),
    (try_end),

    (try_begin),
      (ge, "$cheat_mode", 1),
      (store_sub, reg1, reg0, 1),
      (display_message, "@{!} Bug fix: set personality types for {reg0} {reg1?lords:lord}"),
    (try_end),

    (assign, reg0, 0),
    (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
      (neq, ":troop_no", "trp_knight_1_1_wife"),#That lady should not appear in the game
      (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_none),
      (store_random_in_range, reg1, lrep_conventional - 1, lrep_moralist + 1),
      (val_max, reg1, lrep_conventional),#So there's an extra chance of getting lrep_conventional
      (troop_set_slot, ":troop_no", slot_lord_reputation_type, reg1),
      (val_add, reg0, 1),
    (try_end),


    (try_begin),
      (ge, "$cheat_mode", 1),
      (store_sub, reg1, reg0, 1),
      (display_message, "@{!} Bug fix: set personality types for {reg0} {reg1?ladies:lady}"),
    (try_end),
  (try_end),

  #Behavior for an upgrade from Native or pre-Diplomacy 4.0 to Diplomacy 4.0
  (try_begin),
      (is_between, ":diplomacy_version_code", 0, 111001),
      #Fix: slot_faction_leader and slot_faction_marshall should not equal trp_player
      #if the player is not a member of the faction.  (This is initially true because
      #trp_player is 0, and uninitialized slots default to 0.)
      (try_for_range, ":faction_no", 0, dplmc_factions_end),
         (neq, ":faction_no", "fac_player_faction"),
         (neq, ":faction_no", "fac_player_supporters_faction"),
         (this_or_next|neq, ":faction_no", "$players_kingdom"),
         (eq, ":faction_no", 0),
         #The player is not a member of the faction:
         (try_begin),
            (faction_slot_eq, ":faction_no", slot_faction_leader, 0),
            (faction_set_slot, ":faction_no", slot_faction_leader, -1),
         (try_end),
         (try_begin),
            (faction_slot_eq, ":faction_no", slot_faction_marshall, 0),
            (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
         (try_end),
      (try_end),
      #Initialize home slots for town merchants, elders, etc.
      (try_for_range, ":center_no", centers_begin, centers_end),
         (try_for_range, ":troop_no", dplmc_slot_town_merchants_begin, dplmc_slot_town_merchants_end),
            (party_get_slot, ":troop_no", ":center_no", ":troop_no"),
            (gt, ":troop_no", walkers_end),
            (troop_is_hero, ":troop_no"),
            (troop_slot_eq, ":troop_no", slot_troop_home, 0),
            (troop_set_slot, ":troop_no", slot_troop_home, ":center_no"),
         (try_end),
      (try_end),
      #Initialize home slots for startup merchants.  (Merchant of Praven, etc.)
      #This should be done after kings have their home slots initialized.
      (try_for_range, ":troop_no", kings_begin, kings_end),
         (troop_get_slot, ":center_no", ":troop_no", slot_troop_home),
         (val_sub, ":troop_no", kings_begin),
         (val_add, ":troop_no", startup_merchants_begin),
         (is_between, ":troop_no", startup_merchants_begin, startup_merchants_end),#Right now there's a startup merchant for each faction.  Verify this hasn't unexpectedly changed.
         (neg|troop_slot_ge, ":troop_no", slot_troop_home, 1),#Verify that the home slot is not already set
         (troop_set_slot, ":troop_no", slot_troop_home, ":center_no"),
      (try_end),
      #Reset potentially bad value in "slot_troop_stance_on_faction_issue" (i.e. 153) from auto-loot
      (eq, 153, slot_troop_stance_on_faction_issue),
      (try_for_range, ":troop_no", companions_begin, companions_end),
         (try_begin),
            (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
         (else_try),
            (troop_get_slot, ":slot_val", ":troop_no", slot_troop_stance_on_faction_issue),
            (neg|is_between, ":slot_val", -1, 1),#0 or -1
            (neg|is_between, ":slot_val", heroes_begin, heroes_end),
            (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
         (try_end),
      (try_end),
   (try_end),

   #SB : new features
   (try_begin),
      (is_between, ":diplomacy_version_code", 1, 170001), #1.171 invasion patch
      (display_log_message, "@Performing 2017 updates, thank you for your patience!", message_positive),
      #set up camera keys
      (call_script, "script_setup_camera_keys"),
      (call_script, "script_dplmc_init_quest_delegate_states"),

      #re-appoint employees (usually the player can just enter court to fix this)
      (assign, ":prev_employee", dplmc_prev_employee),
      (try_begin),
        (gt, "$g_player_chamberlain", 0),
        (call_script, "script_dplmc_appoint_chamberlain"),  #fix for wrong troops after update
        (call_script, "script_dplmc_copy_inventory", ":prev_employee", "$g_player_chamberlain"), #move inv over, player might want to play around with treasury
        (try_for_range, ":slot_no", 0, dplmc_slot_troop_affiliated), #IGNORE the last slot because we want to keep latest value
          (troop_get_slot, ":old_value", ":prev_employee", ":slot_no"),
          (troop_set_slot, "$g_player_chamberlain", ":slot_no", ":old_value"),
        (try_end),
      (try_end),
      (val_add, ":prev_employee", 1),

      (try_begin),
        (gt, "$g_player_constable", 0),
        (call_script, "script_dplmc_appoint_constable"),
        (call_script, "script_dplmc_copy_inventory", ":prev_employee", "$g_player_constable"), #move inv over, player might want to play around with treasury
        (try_for_range, ":slot_no", 0, dplmc_slot_troop_affiliated + 1),
          (troop_get_slot, ":old_value", ":prev_employee", ":slot_no"),
          (troop_set_slot, "$g_player_constable", ":slot_no", ":old_value"),
        (try_end),
      (try_end),
      (val_add, ":prev_employee", 1),

      (try_begin),
        (gt, "$g_player_chancellor", 0),
        (call_script, "script_dplmc_appoint_chancellor"),
        (call_script, "script_dplmc_copy_inventory", ":prev_employee", "$g_player_chancellor"), #move inv over, player might want to play around with treasury
        (try_for_range, ":slot_no", 0, dplmc_slot_troop_affiliated + 1),
          (troop_get_slot, ":old_value", ":prev_employee", ":slot_no"),
          (troop_set_slot, "$g_player_chancellor", ":slot_no", ":old_value"),
        (try_end),
      (try_end),
      (val_add, ":prev_employee", 1),
      #replace recruiter/scouts/messenger - probably should have made them non-capturable via tf_allways_fall_dead
      (store_sub, ":troop_offset", dplmc_employees_begin, dplmc_prev_employee), #around 142
      # (assign, ":messenger_troop", dplmc_prev_employee, 3), #skip employees
      (store_add, ":recruiter_troop", ":prev_employee", 3), #933 through 936
      #got the correct offset, now replace them from (active) parties
      # (party_clear, "p_temp_party"),
      (try_for_parties, ":party_no"),
        (party_is_active, ":party_no"),
        # (party_get_template_id, ":party_template", ":party_no"),
        # (this_or_next|eq, ":party_template", "pt_dplmc_recruiter"),
        # (eq, ":party_template", "pt_messenger_party"),
        # (party_count_companions_of_type, ":troop_count", ":party_no", ":recruiter_troop"),
        # (try_begin), #probably should account for wounded but these really shouldn't be anywhere outside their party templates
          # (gt, ":troop_count", 0),
          # (party_remove_members, ":party_no", ":recruiter_troop", ":troop_count"),
          # (try_begin),  #probably fixes recruiter being stacked after the recruits
            # (eq, ":party_template", "pt_dplmc_recruiter"),
            # (party_add_leader, ":party_no", "trp_dplmc_recruiter"),
          # (else_try),
            # (party_add_members, ":party_no", "trp_dplmc_recruiter", ":troop_count"),
          # (try_end),
        # (try_end),
        # (party_count_companions_of_type, ":troop_count", ":party_no", ":messenger_troop"),
        # (try_begin),
          # (gt, ":troop_count", 0),
          # (party_remove_members, ":party_no", ":messenger_troop", ":troop_count"),
          # (try_begin),  #probably fixes messenger being stacked after the recruits
            # (eq, ":party_template", "pt_dplmc_messenger"),
            # (party_add_leader, ":party_no", "trp_dplmc_messenger"),
          # (else_try),
            # (party_add_members, ":party_no", "trp_dplmc_messenger", ":troop_count"),
          # (try_end),
        # (try_end),
        # (party_count_prisoners_of_type, ":prisoner_count", ":party_no", ":recruiter_troop"),
        # (try_begin),
          # (gt, ":prisoner_count", 0),
          # (party_remove_prisoners, ":party_no", ":recruiter_troop", ":prisoner_count"),
          # (party_add_prisoners, ":party_no", "trp_dplmc_recruiter", ":prisoner_count"),
        # (try_end),

        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (gt, ":num_stacks", 0),
        (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
          (is_between, ":troop_no", ":prev_employee", ":recruiter_troop"),
          (party_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
          (party_remove_members, ":party_no", ":troop_no", ":stack_size"),
          (val_add, ":troop_no", ":troop_offset"),
          # (try_begin),
            # (val_sub, ":stack_size", 1), #we try prepending first
            # (party_add_leader, ":party_no", ":troop_no"),
          # (try_end),
          (party_add_members, ":party_no", ":troop_no", ":stack_size"),
        (try_end),
        (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
        (gt, ":num_stacks", 0),
        (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
          (is_between, ":troop_no", ":prev_employee", ":recruiter_troop"),
          (party_prisoner_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
          (party_remove_prisoners, ":party_no", ":troop_no", ":stack_size"),
          (val_add, ":troop_no", ":troop_offset"),
          (party_add_prisoners, ":party_no", ":troop_no", ":stack_size"),
        (try_end),
      (try_end),

      #set up disguise system, disabled by default
      (assign, "$g_dplmc_player_disguise", 0),
      (try_begin),
        (assign, ":disguise", disguise_pilgrim), #always available
        #farmer, acquired from village elders
        (assign, ":villages_end", villages_end),
        (try_for_range, ":center_no", villages_begin, ":villages_end"),
          (party_slot_ge, ":center_no", slot_center_player_relation, 25),
          (val_add, ":disguise", disguise_farmer),
          (assign, ":villages_end", -1), #loop break
        (try_end),


        #hunter, acquired from background or archery skill
        (try_begin),
          (store_proficiency_level, ":cur_amount", "trp_player", wpt_archery),
          (this_or_next|ge, ":cur_amount", 250),
          (this_or_next|eq, "$background_type", cb_forester),
          (this_or_next|eq, "$background_answer_2", cb2_steppe_child),
          (eq, "$background_answer_3", cb3_poacher),
          (val_add, ":disguise", disguise_hunter),
        (try_end),
        #merchant, from background or gold count or enterprise
        (try_begin),
          (assign, ":continue", 0),
          (assign, ":villages_end", towns_end),
          (try_for_range, ":center_no", towns_begin, ":villages_end"),
            (party_slot_ge, ":center_no", slot_center_player_enterprise, 1),
            (assign, ":continue", 1),
            (assign, ":villages_end", towns_begin), #loop break
          (try_end),
          (try_begin),
            (eq, ":continue", 0),
            (store_troop_gold, ":cur_amount", "trp_player"),
            (store_skill_level, ":cur_skill", "trp_player", "skl_trade"),
            (ge, ":cur_skill", 5),
            (ge, ":cur_amount", 10000),
            (assign, ":continue", 1),
          (try_end),
          (this_or_next|gt, ":continue", 0),
          (this_or_next|eq, "$background_type", cb_merchant),
          (this_or_next|eq, "$background_answer_2", cb2_merchants_helper),
          (eq, "$background_answer_3", cb3_peddler),
          (val_add, ":disguise", disguise_merchant),
        (try_end),

        #guard, from background or weapon mastery
        (try_begin),
          (store_skill_level, ":cur_skill", "trp_player", "skl_weapon_master"),
          (this_or_next|ge, ":cur_skill", 5),
          (this_or_next|eq, "$background_type", cb_guard),
          (this_or_next|eq, "$background_answer_3", dplmc_cb3_bravo),
          (this_or_next|eq, "$background_answer_3", dplmc_cb3_merc),
          (eq, "$background_answer_3", cb3_squire),
          (val_add, ":disguise", disguise_guard),
        (try_end),

        #bard, from background or known songs
        (try_begin),
          (store_add, ":cur_amount", "$allegoric_poem_recitations", "$mystic_poem_recitations"),
          (val_add, ":cur_amount", "$tragic_poem_recitations"),
          (val_add, ":cur_amount", "$heroic_poem_recitations"),
          (val_add, ":cur_amount", "$comic_poem_recitations"),
          (this_or_next|ge, ":cur_amount", 2), #2 poems known
          (eq, "$background_answer_3", cb3_troubadour),
          (val_add, ":disguise", disguise_bard),
        (try_end),
      (try_end),
      (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, ":disguise"),

      #equip voulges
      (troop_add_item, "trp_fighter_woman", "itm_shortened_voulge"),
      (troop_add_item, "trp_swadian_sergeant", "itm_awlpike_long"),
      (troop_add_item, "trp_swadian_deserter", "itm_shortened_voulge"),
      (troop_add_item, "trp_swadian_deserter", "itm_long_voulge"),
      (troop_add_item, "trp_swadian_crossbowman", "itm_shortened_voulge"),
      (troop_add_item, "trp_swadian_sharpshooter", "itm_long_voulge"),
      (troop_add_item, "trp_vaegir_guard", "itm_two_handed_battle_axe_2"),
      (troop_add_item, "trp_vaegir_guard", "itm_long_bardiche"),
      (troop_add_item, "trp_vaegir_infantry", "itm_two_handed_battle_axe_2"),
      (troop_remove_item, "trp_vaegir_infantry", "itm_battle_axe"),

      #add coloured tunics to messengers, remove leather_jerkin
      (troop_remove_item, "trp_swadian_messenger", "itm_leather_jerkin"),
      (troop_remove_item, "trp_vaegir_messenger", "itm_leather_jerkin"),
      (troop_remove_item, "trp_vaegir_messenger", "itm_sword_medieval_b"),
      (troop_remove_item, "trp_khergit_messenger", "itm_leather_jerkin"),
      (troop_remove_item, "trp_khergit_messenger", "itm_short_bow"),
      (troop_remove_item, "trp_khergit_messenger", "itm_arrows"),
      (troop_remove_item, "trp_nord_messenger", "itm_leather_jerkin"),
      (troop_remove_item, "trp_nord_messenger", "itm_short_bow"),
      (troop_remove_item, "trp_rhodok_messenger", "itm_leather_jerkin"),
      (troop_remove_item, "trp_rhodok_messenger", "itm_short_bow"),
      (troop_remove_item, "trp_rhodok_messenger", "itm_arrows"),
      #sarranid messenger already copied from horseman
      #but we need to reassign them
      (troop_set_faction, "trp_sarranid_messenger", "fac_kingdom_6"),
      (troop_set_faction, "trp_sarranid_prison_guard", "fac_kingdom_6"),
      (troop_set_faction, "trp_sarranid_castle_guard", "fac_kingdom_6"),
      (troop_add_item, "trp_swadian_messenger", "itm_arena_tunic_red"),
      (troop_add_item, "trp_vaegir_messenger", "itm_fighting_axe"),
      (troop_add_item, "trp_vaegir_messenger", "itm_studded_leather_coat"),
      (troop_add_item, "trp_khergit_messenger", "itm_khergit_bow"),
      (troop_add_item, "trp_khergit_messenger", "itm_khergit_arrows"),
      (troop_add_item, "trp_khergit_messenger", "itm_nomad_robe"),
      (troop_add_item, "trp_nord_messenger", "itm_long_bow"),
      (troop_add_item, "trp_nord_messenger", "itm_arena_tunic_blue"),
      (troop_add_item, "trp_rhodok_messenger", "itm_light_crossbow"),
      (troop_add_item, "trp_rhodok_messenger", "itm_steel_bolts"),
      (troop_add_item, "trp_rhodok_messenger", "itm_arena_tunic_green"),

      #equip tavern drunks/assassin (could be done as easily in trigger)
      (troop_add_item, "trp_belligerent_drunk","itm_sword_medieval_a"),
      (troop_add_item, "trp_belligerent_drunk","itm_sword_khergit_1"),
      (troop_add_item, "trp_belligerent_drunk","itm_arabian_sword_a"),
      (troop_remove_item, "trp_hired_assassin","itm_sword_medieval_a"),
      (troop_add_item, "trp_hired_assassin","itm_sword_viking_3"),
      (troop_add_item, "trp_hired_assassin","itm_sword_medieval_d_long"),
      (troop_add_item, "trp_hired_assassin","itm_sword_khergit_4"),
      (troop_add_item, "trp_hired_assassin","itm_arabian_sword_d"),
      (troop_add_item, "trp_hired_assassin","itm_strange_sword"),

      #sarranid "castle" guard replace with regular troop
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_6"),
        (faction_slot_eq, ":faction_no", slot_faction_guard_troop, "trp_sarranid_castle_guard"),
        (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_sarranid_guard"),
      (try_end),
      #rivacheg strange bonus chest
      (store_random_in_range, ":imod", imod_rusty, imod_strong),
      (troop_add_item, "trp_bonus_chest_1","itm_strange_sword", ":imod"),
      (store_random_in_range, ":imod", imod_rusty, imod_strong),
      (troop_add_item, "trp_bonus_chest_1","itm_strange_great_sword", ":imod"),
      (store_random_in_range, ":imod", imod_tattered, imod_lame),
      (troop_add_item, "trp_bonus_chest_1","itm_strange_boots", ":imod"),
      (store_random_in_range, ":imod", imod_tattered, imod_lame),
      (troop_add_item, "trp_bonus_chest_1","itm_strange_helmet", ":imod"),

      (troop_add_item, "trp_bonus_chest_2","itm_bride_dress", imod_stubborn),
      (troop_add_item, "trp_bonus_chest_2","itm_bride_crown", imod_deadly),
      (troop_add_item, "trp_bonus_chest_2","itm_bride_shoes", imod_smelling),
      (troop_add_item, "trp_bonus_chest_2","itm_torch", imod_old),

      (troop_add_item, "trp_bonus_chest_3","itm_black_armor", imod_lordly),
      (troop_add_item, "trp_bonus_chest_3","itm_black_greaves", imod_lordly),
      (troop_add_item, "trp_bonus_chest_3","itm_black_helmet", imod_lordly),
      (troop_add_item, "trp_bonus_chest_3","itm_steel_shield", imod_lordly),
      (troop_add_item, "trp_bonus_chest_3","itm_charger", imod_lordly), #charger_plate_1

      #training ground variables based on global
      (try_for_range, ":npc", training_ground_trainers_begin, training_ground_trainers_end),
        #init trainer vars, global applied to all trainers instead of individual progress
        # (troop_set_slot, ":npc", slot_troop_trainer_met, 0),
        (troop_set_slot, ":npc", slot_troop_trainer_waiting_for_result, "$waiting_for_training_fight_result"),
        (troop_set_slot, ":npc", slot_troop_trainer_training_fight_won, "$training_fight_won"),
        (troop_set_slot, ":npc", slot_troop_trainer_num_opponents_to_beat, "$num_opponents_to_beat_in_a_row"),
        (troop_set_slot, ":npc", slot_troop_trainer_training_system_explained, "$training_system_explained"),
        (troop_set_slot, ":npc", slot_troop_trainer_opponent_troop, "$novicemaster_opponent_troop"),
        (troop_set_slot, ":npc", slot_troop_trainer_training_difficulty, "$novice_training_difficulty"),
        #add random equipment
        (store_random_in_range, ":item_no", "itm_practice_sword", "itm_practice_shield"),
        (troop_add_item, ":npc", ":item_no", imod_champion),
        (store_sub, ":offset", ":npc", training_ground_trainers_begin),
        #init grounds vars
        (store_add, ":grounds", ":offset", training_grounds_begin),
        (store_add, ":scene", ":offset", "scn_training_ground_ranged_melee_1"),
        (party_set_slot, ":grounds", slot_grounds_melee, ":scene"),
        (store_add, ":scene", ":offset", "scn_training_ground_horse_track_1"),
        (party_set_slot, ":grounds", slot_grounds_track, ":scene"),
        (party_set_slot, ":grounds", slot_grounds_trainer, ":npc"),
        (party_set_slot, ":grounds", slot_grounds_count, "$g_training_ground_training_count"),
        (troop_set_slot, ":npc", slot_troop_cur_center, ":grounds"),
      (try_end),


    #other tavern npc based on location
      (try_for_range, ":town_no", towns_begin, towns_end),
        (try_for_range, ":slot_no", slot_center_ransom_broker, slot_center_tavern_minstrel + 1),
          (neq, ":slot_no", slot_center_traveler_info_faction),
          (party_get_slot, ":npc", ":town_no", ":slot_no"),
          (is_between, ":npc", ransom_brokers_begin, tavern_minstrels_end),
          (troop_set_slot, ":npc", slot_troop_cur_center, ":town_no"),
        (try_end),
      (try_end),
    (try_end),
    
    (try_begin),
      (is_between, ":diplomacy_version_code", 170301, 190101),
      (display_log_message, "@Performing 2019 updates, thank you for your patience!", message_positive),
      (call_script, "script_dplmc_init_faction_gender_ratio", 0),
    (try_end),
    #Ensure $character_gender is set correctly
    (try_begin),
      (call_script, "script_cf_dplmc_troop_is_female", "trp_player"),
      (assign, "$character_gender", tf_female),
    (else_try),
      (assign, "$character_gender", tf_male),
    (try_end),
   ##diplomacy end+

   (assign, reg1, ":save_reg1"),#Revert register
   (assign, reg0, ":save_reg0"),#Revert register

   ]),
   
   #updates info_pages dynamically with DPLMC settings
   ("dplmc_update_info_settings",
   [
   (try_begin),
     (eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
     (assign, ":setting", "str_dplmc_tax_low"),
   (else_try),
     (eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
     (assign, ":setting", "str_dplmc_medium"),
   (else_try),
     (eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
     (assign, ":setting", "str_dplmc_tax_high"),
   (else_try),
     (assign, ":setting", "str_off"),
   (try_end),
   (str_store_string, s1, ":setting"),
   (add_info_page_note_from_sreg, ip_dplmc_gold_changes, 1, "str_setting_of", 0),
   
   (try_begin),
     (eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
     (assign, ":setting", "str_dplmc_tax_low"),
   (else_try),
     (eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
     (assign, ":setting", "str_dplmc_medium"),
   (else_try),
     (eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
     (assign, ":setting", "str_dplmc_tax_high"),
   (else_try),
     (assign, ":setting", "str_off"),
   (try_end),
   (str_store_string, s1, ":setting"),
   (add_info_page_note_from_sreg, ip_dplmc_ai_changes, 1, "str_setting_of", 0),
   
   # (str_store_string, s1, ":setting"), #PREJUDICE
   # (add_info_page_note_from_sreg, ip_courtship, 1, "str_setting_of", 0),
   
   # (str_store_string, s1, ":setting"), #LORD RECYCLING?
   # (add_info_page_note_from_sreg, politics, 1, "str_setting_of", 0),
   ]),
   
   #input : party_no, player's renown assuming it's past the threshold for
   #output : party_no's temp_slot_01
   ("dplmc_encounter_calculate_player_commanding",
   [
    (store_script_param, ":party_no", 1),
    (store_script_param, ":limit", 2),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (party_stack_get_troop_id, ":leader_troop_id", ":party_no", 0),

    (try_begin), #straggler parties - patrols, caravans, etc.
      (neg|is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end),
      (assign, ":continue", 0),
    (else_try), #as marshal/leader
      (eq, ":party_faction", "$players_kingdom"),
      (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
      (ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
       # (this_or_next|faction_slot_eq, ":party_faction", slot_faction_marshall, "trp_player"),
       # (faction_slot_eq, ":party_faction", slot_faction_leader, "$g_player_troop"),
      (assign, ":continue", 0),
    (else_try), #or high enough renown/relation
      (troop_slot_eq, ":leader_troop_id", slot_troop_occupation, slto_kingdom_hero),
      (assign, ":continue", -1),
      #add party affiliation/conditions here (virtual offset through relation?)
      (try_begin),
        (call_script, "script_dplmc_is_affiliated_family_member", ":leader_troop_id"),
        (this_or_next|eq, reg0, 1),
        (troop_is_wounded, ":leader_troop_id"),
        (assign, ":renown", 0), #affiliated/wounded leader = follow player
      (else_try),
        (troop_get_slot, ":renown", ":leader_troop_id", slot_troop_renown),
        (call_script, "script_troop_get_relation_with_troop", ":leader_troop_id", "$g_player_troop"),
        (val_sub, ":renown", reg0), #higher relation means less renown needed for command
      (try_end),
      (le, ":renown", ":limit"),
      (assign, ":continue", 0),
    (try_end),
    (party_set_slot, ":party_no", slot_party_temp_slot_1, ":continue"),
    (try_begin),
      (ge, "$cheat_mode", 1),
      (eq, ":continue", 0),
      # (str_store_party_name, s0, ":party_no"),
      (str_store_party_name, s0, ":party_no"),
      (faction_get_color, ":color", ":party_faction"),
      (display_message, "@{s0} will be under your command", ":color"),
    (try_end),
   ]),
   
   #script_dplmc_count_item_required_for_court
   #input : troop_no, amount to remove
   #output : reg0 and reg1
   ("dplmc_count_item_for_court",
    [
    (store_script_param, ":troop_no", 1),
    (store_script_param, ":remove_cloth", 2),
    (store_script_param, ":remove_tools", 3),
    (troop_get_inventory_capacity, ":capacity", ":troop_no"),

    (assign, ":cloth_amount", 0),
    (assign, ":tools_amount", 0),
    (try_for_range, ":inventory_slot", ek_food + 1, ":capacity"), #could also check chamberlain, castle chest etc
      (troop_get_inventory_slot, ":item", ":troop_no", ":inventory_slot"),
      (try_begin),
        (this_or_next|eq, ":item", "itm_velvet"),
        (this_or_next|eq, ":item", "itm_linen"),
        (eq, ":item", "itm_wool_cloth"),
        (val_add, ":cloth_amount", 1),
        (try_begin),
          (gt, ":remove_cloth", 0),
          (val_sub, ":remove_cloth", 1),
          (troop_set_inventory_slot, ":troop_no", ":inventory_slot", -1),
        (try_end),
      (else_try),
        (eq, ":item", "itm_tools"),
        (val_add, ":tools_amount", 1),
        (try_begin),
          (gt, ":remove_tools", 0),
          (val_sub, ":remove_tools", 1),
          (troop_set_inventory_slot, ":troop_no", ":inventory_slot", -1),
        (try_end),
      (try_end),
    (try_end),
    #return quotas if not met
    (try_begin),
      (gt, ":remove_cloth", 0),
      (assign, reg0, ":remove_cloth"),
    (else_try),
      (assign, reg0, ":cloth_amount"),
    (try_end),
    (try_begin),
      (gt, ":remove_tools", 0),
      (assign, reg1, ":remove_tools"),
    (else_try),
      (assign, reg1, ":tools_amount"),
    (try_end),
   ]),
   
  # script_dplmc_get_court_guard_troop
  # Input: arg1 = center_no
  # Output: reg0, guard troop id
  #other search term: setup_court
  ("dplmc_get_court_guard_troop",
    [
      (store_script_param_1, ":center_no"),

      (store_faction_of_party, ":center_faction", ":center_no"),
      (assign, ":guard_faction", ":center_faction"), #SB : guard faction
      (assign, ":guard_troop", "trp_hired_blade"), #default, could be parameterized
      ##diplomacy begin
      (try_begin),
         (eq, ":center_faction", "$players_kingdom"),
         (is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
         (assign, ":guard_faction", "$g_player_culture"),
      ##nested diplomacy start+
      (else_try),
         #Reflect multicultural empires.
         (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
         (gt, ":town_lord", "trp_player"),
         (troop_get_slot, ":lord_original_faction", ":town_lord", slot_troop_original_faction),
         (neq, ":lord_original_faction", ":center_faction"),
         (is_between, ":lord_original_faction", npc_kingdoms_begin, npc_kingdoms_end),
         (this_or_next|party_slot_eq, ":center_no", slot_center_original_faction, ":lord_original_faction"),
            (troop_slot_eq, ":town_lord", slot_troop_home, ":center_no"),
         (assign, ":guard_faction", ":lord_original_faction"),
      ##nested diplomacy end+
      (else_try), #SB : player customized guard troop
        (eq, "$g_player_culture", 0),
        (eq, ":town_lord", "trp_player"),
        (faction_slot_ge, ":center_faction", slot_faction_guard_troop, 1), #has set them
        (assign, ":guard_faction", "$players_kingdom"),
      (try_end),
      (faction_get_slot, ":guard_troop", ":guard_faction", slot_faction_guard_troop),
      # (try_end),
      ##diplomacy end
      (try_begin),
        (le, ":guard_troop", 0),
        (assign, ":guard_troop", "trp_hired_blade"),
      (try_end),
      (assign, reg0, ":guard_troop")
    ]),
      
  # script_dplmc_enter_court_aux
  # Input: arg1 = center_no, arg2 = party to select from (see below scripts for variation)
  # Output: none
  #other search term: setup_court
  ("dplmc_enter_court_aux",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":party_no"), #determines which

      (assign, "$talk_context", tc_court_talk),
      # (troop_set_slot, "$g_talk_troop", slot_troop_temp_decision_seed, ":party_no"),
      (set_jump_mission,"mt_visit_town_castle"),

      (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
      (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
      (modify_visitors_at_site,":castle_scene"),
      (reset_visitors),
      #Adding guards
      (call_script, "script_dplmc_get_court_guard_troop", ":center_no"),
      (assign, ":guard_troop", reg0),
      (set_visitor, 6, ":guard_troop"),
      (set_visitor, 7, ":guard_troop"),

      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
      (try_begin),
        (eq, "$g_player_court", ":center_no"),
        (assign, ":cur_pos", 17), #reserve 1
        # (assign, ":player_entry", 32),
        (val_min, ":num_stacks", 15), #1 less, unless we dynamically spawn applicants
      (else_try),
        (assign, ":cur_pos", 16),
        (val_min, ":num_stacks", 16),
        # (assign, ":player_entry", 0),
      (try_end),
      
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
        (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", ":cur_pos"),
        (call_script, "script_set_companion_civilian_clothing_override", "mt_visit_town_castle", ":cur_pos", ":stack_troop"), #SB : check equipment override
        (set_visitor, ":cur_pos", ":stack_troop"),
        (val_add,":cur_pos", 1),
      (try_end),

      #SB : todo place player at "middle" instead of doors if ruler
      (set_jump_entry, 0),
      
      (jump_to_scene,":castle_scene"),
      (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
      (change_screen_mission),
  ]),
  

  # script_enter_court_male
  # Input: arg1 = center_no
  # Output: reg0 = count of candidates, filled party
  #other search term: setup_court
  ("enter_court_male", [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":party_no_to_collect_heroes"),
      (party_clear, ":party_no_to_collect_heroes"),
      (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
        (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
        (eq, ":active_npc_faction", "fac_player_supporters_faction"),
        (this_or_next|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
        (troop_slot_eq, ":active_npc", slot_troop_occupation, dplmc_slto_exile),
        (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
        (neg|troop_slot_ge, ":active_npc", slot_troop_leaded_party, 0), #if he/she does not have a party
        # (neq, ":active_npc", "$g_player_minister"),
        (party_add_members, ":party_no_to_collect_heroes", ":active_npc", 1),
      (try_end),

     #Non-attached pretenders (TODO make sure supported_pretender works well in court convo)
     (try_for_range, ":pretender", pretenders_begin, pretenders_end),
        (neq, ":pretender", "$supported_pretender"),
        (troop_slot_eq, ":pretender", slot_troop_cur_center, ":center_no"),
        (party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
     (try_end),
     (party_get_num_companion_stacks, reg0, ":party_no_to_collect_heroes"),
  ]),
  ("enter_court_staff", [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":party_no_to_collect_heroes"),
      (party_clear, ":party_no_to_collect_heroes"),
      (try_begin),
        (gt, "$g_player_minister", 0),
        (party_add_members, ":party_no_to_collect_heroes", "$g_player_minister", 1),
      (try_end),
      (try_begin),
        (gt, "$g_player_chancellor", 0),
        (party_add_members, ":party_no_to_collect_heroes", "$g_player_chancellor", 1),
      (try_end),
      (try_begin),
        (gt, "$g_player_constable", 0),
        (party_add_members, ":party_no_to_collect_heroes", "$g_player_constable", 1),
      (try_end),
      (try_begin),
        (gt, "$g_player_chamberlain", 0),
        (party_add_members, ":party_no_to_collect_heroes", "$g_player_chamberlain", 1),
      (try_end),
  ]),
("enter_court_female", [
  (store_script_param_1, ":center_no"),
  (store_script_param_2, ":party_no_to_collect_heroes"),
  (store_faction_of_party, ":center_faction", ":center_no"),
  (party_clear, ":party_no_to_collect_heroes"),
  (try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
    (neq, ":cur_troop", "trp_knight_1_1_wife"), #The one who should not appear in game
    #(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
    (troop_slot_eq, ":cur_troop", slot_troop_cur_center, ":center_no"),

    (assign, ":lady_meets_visitors", 0),
    (try_begin),
        (this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":cur_troop"),
        (troop_slot_eq, "trp_player", slot_troop_betrothed, ":cur_troop"),
        (assign, ":lady_meets_visitors", 1),
    (else_try),
        (this_or_next|troop_slot_eq, ":cur_troop", slot_troop_spouse, "trp_player"),
        (troop_slot_eq, ":cur_troop", slot_troop_betrothed, "trp_player"),
        (assign, ":lady_meets_visitors", 1),
    (else_try), #lady is troop
        (store_faction_of_troop, ":lady_faction", ":cur_troop"),
        (neq, ":lady_faction", ":center_faction"),
        (assign, ":lady_meets_visitors", 1),
    (else_try),
        (troop_slot_ge, ":cur_troop", slot_troop_spouse, 1),
        (try_begin),
            (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
            (faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
            (assign, ":lady_meets_visitors", 0),
        (else_try),
            (assign, ":lady_meets_visitors", 1),
        (try_end),
    (else_try), #feast is in progress
        (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
        (faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
        (assign, ":lady_meets_visitors", 1),
    (else_try), #already met - awaits in private
        (troop_slot_ge, ":cur_troop", slot_troop_met, 2),
        (assign, ":lady_meets_visitors", 0),
    (else_try),
        (call_script, "script_get_kingdom_lady_social_determinants", ":cur_troop"),
        (call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", reg0, "trp_player"),
        (gt, reg0, 0),
        (assign, ":lady_meets_visitors", 1),
    (try_end),

    (eq, ":lady_meets_visitors", 1),
    (party_add_members, ":party_no_to_collect_heroes", ":cur_troop", 1),
  (try_end),
  (party_get_num_companion_stacks, reg0, ":party_no_to_collect_heroes"),
]),
    
    #input : party_no (of the recruiter), 
    #        amount to be updated (-1 for cancel, 0 for update)
    #output : s10
    ("dplmc_set_recruiter_extra_text", [
      (store_script_param_1, ":party_no"),
      (store_script_param_2, ":amount"),
      (try_begin), #do nothing
        (neg|party_slot_eq, ":party_no", slot_party_type, dplmc_spt_recruiter),
        (str_store_string, s10, "str_empty_string"),
      (else_try), #finished or ordered to return
        (eq, ":amount", -1),
        (str_store_string, s10, "@Returning"),
      (else_try),
        (try_begin), #updated, not set
          (eq, ":amount", 0),
          (party_get_num_companions, ":num_recruits", ":party_no"),
          (party_get_slot, ":num_target", ":party_no", dplmc_slot_party_recruiter_needed_recruits),
          (val_sub, ":num_recruits", 1), #ignore recruiter himself
          (store_sub, ":amount", ":num_target", ":num_recruits"),
        (try_end),
        (assign, reg10, ":amount"),
        (party_get_slot, ":recruit_faction", ":party_no", dplmc_slot_party_recruiter_needed_recruits_faction),
        (try_begin),
          (is_between, ":recruit_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (faction_get_slot, ":string", ":recruit_faction", slot_faction_adjective),
          (str_store_string, s10, ":string"),
        (else_try),
          (str_store_string, s10, "@Recruit"),
        (try_end),
        (str_store_string, s10, "@{reg10} {s10}s needed"),
      (try_end),
      (party_set_extra_text, ":party_no", s10),
    ]),
    

    #input : $current_town, page index
    ("dplmc_mayor_wealth_comparison", [
      (store_script_param_1, ":this_center"),
      (store_script_param_2, ":page_no"),
      
      # (assign, ":wealthiest_town_production", 0),
      (assign, ":poorer_centers", 0),
      (assign, ":richer_centers", 0),
      # (assign, ":equal_centers", 0), #tiebreakers?

      (party_get_slot, ":mayor_town_production", ":this_center", slot_party_temp_slot_1),
      (assign, ":wealthiest_town_production", ":mayor_town_production"),
      (assign, ":wealthiest_center", -1),
      (try_begin),
        (ge, "$cheat_mode", 1),
        (assign, reg4, ":mayor_town_production"),
        (str_store_party_name, s4, ":this_center"),
        (display_message, "@{!}DEBUG -- Total production for {s4}: {reg4}"),
      (try_end),
      (try_for_range, ":other_center", towns_begin, towns_end),
        (neq, ":other_center", ":this_center"),
        (party_get_slot, ":other_town_production", ":other_center", slot_party_temp_slot_1),
        (try_begin),
            (ge, "$cheat_mode", 1),
            (assign, reg4, ":other_town_production"),
            # (assign, reg4, ":richer_centers"),
            # (assign, reg5, ":poorer_centers"),
            (str_store_party_name, s4, ":other_center"),
            (display_message, "@{!}DEBUG -- Total production for {s4}: {reg4}"),
        (try_end),
        (try_begin),
            (gt, ":other_town_production", ":wealthiest_town_production"),
            (val_add, ":richer_centers", 1),
            (assign, ":wealthiest_center", ":other_center"),
            (assign, ":wealthiest_town_production", ":other_town_production"),
        (else_try),
            (gt, ":other_town_production", ":mayor_town_production"),
            (val_add, ":richer_centers", 1),
        (else_try),
            (val_add, ":poorer_centers", 1),
        (try_end),
      (try_end),

      #reset for next cycle
      (try_for_range, ":center_no", towns_begin, towns_end),
        (party_set_slot, ":center_no", slot_party_temp_slot_1, 0),
      (try_end),
      
      #prep strings
      (try_begin), #richest
        (eq, ":wealthiest_center", ":this_center"),
        (neq, ":wealthiest_town_production", 0),
        (try_begin), #here
          (is_between, ":page_no", 0, 2),
          (str_store_string, s2, "str_mayor_wealth_rank_3"),
        (else_try), #ourselves
          (str_store_string, s2, "str_mayor_wealth_rank_6"),
        (try_end),
      (else_try), #no data
        (eq, ":wealthiest_center", -1),
        # (eq, ":wealthiest_town_production", 0),
        (try_begin), #yet to be announced
          (is_between, ":page_no", 0, 2),
          (str_store_string, s2, "str_mayor_wealth_rank_1"),
        (else_try), #we're not sure
          (str_store_string, s2, "str_mayor_wealth_rank_4"),
        (try_end),
      (else_try), #not us
        (is_between, ":wealthiest_center", centers_begin, centers_end),
        (str_store_party_name, s2, ":wealthiest_center"),
        (try_begin), #known to be
          (is_between, ":page_no", 0, 2),
          (str_store_string, s2, "str_mayor_wealth_rank_2"),
        (else_try), #believed to 
          (str_store_string, s2, "str_mayor_wealth_rank_5"),
        (try_end),
      (try_end),
      (str_store_party_name, s3, ":this_center"),
      
      #rank doesn't mean much without data
      (try_begin),
        (eq, ":wealthiest_town_production", 0),
        (str_store_string, s1, "str_mayor_wealth_no_data"),
      (else_try),
        (assign, reg4, ":richer_centers"),
        (assign, reg5, ":poorer_centers"),
        (assign, reg6, 0),
        #build string chunks based on relative position
        (store_add, ":poorer_string", ":page_no", "str_mayor_wealth_compare_less_1"),
        (store_add, ":richer_string", ":page_no", "str_mayor_wealth_compare_more_1"),
        (try_begin), #richest, just show second part (swap)
          (eq, ":richer_centers", 0),
          (str_store_string, s4, ":richer_string"),
          (assign, reg4, ":poorer_centers"),
        (else_try), #poorest, show first chunk
          (eq, ":poorer_centers", 0),
          (str_store_string, s4, ":poorer_string"),
          (assign, reg4, ":richer_centers"),
        (else_try), #middle, show first + second chunk
          (assign, reg6, 1),
          (str_store_string, s4, ":poorer_string"),
          (str_store_string, s5, ":richer_string"),
          #Here in {s5}, we are poorer than {reg4} towns, and richer than {reg5}.
        (try_end),
        (str_store_string, s1, "str_mayor_wealth_compare"),
      (try_end),
      (store_add, ":output_string", ":page_no", "str_mayor_wealth_comparison_1"),
      (str_store_string, s0, ":output_string"),
    ]),

    #sets up a few permanent quest slots or level thresholds
    ("dplmc_init_quest_delegate_states", [
      #these are political or multi-stage? could be reserved for companion-as-lords
      (try_for_range, ":quest_no", "qst_lend_surgeon", army_quests_end),
        (quest_set_slot, ":quest_no", slot_quest_delegate_level, -1),
      (try_end), #romantic
      (try_for_range, ":quest_no", lady_quests_begin, lady_quests_end),
        (quest_set_slot, ":quest_no", slot_quest_delegate_level, -1),
      (try_end), #political
      (try_for_range, ":quest_no", "qst_visit_lady", all_quests_end),
        (quest_set_slot, ":quest_no", slot_quest_delegate_level, -1),
      (try_end),
      (quest_set_slot, "qst_escort_merchant_caravan", slot_quest_delegate_level, -1),
      (quest_set_slot, "qst_move_cattle_herd", slot_quest_delegate_level, -1),
      (quest_set_slot, "qst_lend_companion", slot_quest_delegate_level, -1),
      # (quest_set_slot, "qst_lend_surgeon", slot_quest_delegate_level, -1),
      (quest_set_slot, "qst_capture_enemy_hero", slot_quest_delegate_level, -1),
      (quest_set_slot, "qst_rescue_prisoner", slot_quest_delegate_level, -1), #different mechanic
      (quest_set_slot, "qst_persuade_lords_to_make_peace", slot_quest_delegate_level, -1),
      #these involve killing?
      (quest_set_slot, "qst_kidnapped_girl", slot_quest_delegate_level, 10),
      (quest_set_slot, "qst_capture_prisoners", slot_quest_delegate_level, 10),
      (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_delegate_level, 10),
      (quest_set_slot, "qst_kill_local_merchant", slot_quest_delegate_level, 10),
      (quest_set_slot, "qst_deal_with_bandits_at_lords_village", slot_quest_delegate_level, 15),
      (quest_set_slot, "qst_deal_with_night_bandits", slot_quest_delegate_level, 15),
      (quest_set_slot, "qst_deal_with_looters", slot_quest_delegate_level, 15),
      #these involve mass murder?
      (quest_set_slot, "qst_track_down_bandits", slot_quest_delegate_level, 20),
      (quest_set_slot, "qst_destroy_bandit_lair", slot_quest_delegate_level, 20),
      (quest_set_slot, "qst_troublesome_bandits", slot_quest_delegate_level, 20),
      (quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_delegate_level, 20),
    ]),
    
    #calculate based on # centers & game difficulty & faction sliders
    # reports {reg0} (denars lost), {reg1} (% lost, not marginal tax ineff)
    ("cf_dplmc_calculate_tax_inefficiency", [
      (store_script_param, ":num_owned", 1),
      (store_script_param, ":tax_total", 2),
      (store_script_param, ":alt_rule_faction", 3),
      (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
      (try_begin),
        (eq, ":reduce_campaign_ai", 0), #hard
        (assign, ":needed", 2),
        (assign, ":ratio", 5),
      (else_try),
        (eq, ":reduce_campaign_ai", 1), #medium
        (assign, ":needed", 4),
        (assign, ":ratio", 4),
      (else_try),
        (eq, ":reduce_campaign_ai", 2), #easy
        (assign, ":needed", 6),
        (assign, ":ratio", 3),
      (try_end),
      (try_begin),
        (gt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
        (try_begin), #SB : small boost for capital
          (is_between, "$g_player_court", walled_centers_begin, walled_centers_end),
          (store_and, ":has_capital", "$players_kingdom_name_set", rename_center), #check if it's "court" or "capital"
          (val_add, ":needed", ":has_capital"),
        (try_end),
        (try_begin),
          (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
          (is_between, ":spouse", heroes_begin, heroes_end),
          (troop_slot_eq, ":spouse", slot_troop_spouse, "trp_player"),
          (val_add, ":needed", 1),
        (try_end),
      (try_end),
      #original condition here
      (gt, ":num_owned", ":needed"),
      (gt, ":tax_total", 0),
      
      (store_sub, ":ratio_lost", ":num_owned", ":needed"),
      (val_mul, ":ratio_lost", ":ratio"),
      (val_min, ":ratio_lost", 65),
      (try_begin),
        (gt, "$g_player_chamberlain", 0),
        (assign, ":percent", 10),
      (else_try),
        (assign, ":percent", 0),
      (try_end),

      (try_begin),
        ##diplomacy start+ Handle player is co-ruler of NPC kingdom
        (gt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
        (try_begin),
          #Copy slot values
          (is_between, ":alt_rule_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),

          (faction_get_slot, reg0, ":alt_rule_faction", dplmc_slot_faction_serfdom),
          (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_serfdom,  reg0),
          (faction_get_slot, reg0, ":alt_rule_faction", dplmc_slot_faction_centralization),
          (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_centralization,  reg0),
          (faction_get_slot, reg0, ":alt_rule_faction", dplmc_slot_faction_quality),
          (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_quality,  reg0),
          (faction_get_slot, reg0, ":alt_rule_faction", dplmc_slot_faction_aristocracy),
          (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_aristocracy,  reg0),
          (faction_get_slot, reg0, ":alt_rule_faction", dplmc_slot_faction_mercantilism),
          (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_mercantilism,  reg0),
        (try_end),

        (this_or_next|is_between, ":alt_rule_faction", npc_kingdoms_begin, npc_kingdoms_end),
        ##diplomacy end+
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
        (try_begin),
          (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
          (neq, ":centralization", 0),
          (val_mul, ":centralization", 5),
          (val_add, ":percent", ":centralization"),
        (try_end),
        (try_begin),
          (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
          (neq, ":serfdom", 0),
          (val_mul, ":serfdom", 3),
          (val_add, ":percent", ":serfdom"),
        (try_end),
      (else_try),
        (gt, "$players_kingdom", 0),
        (gt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
        (faction_get_slot, ":centralization", "$players_kingdom", dplmc_slot_faction_centralization),
        (neq, ":centralization", 0),
        (val_mul, ":centralization", -5),
        (val_add, ":percent", ":centralization"),
      (try_end),
      
      (try_begin),
        (gt, ":ratio_lost", 0),
        (store_mul, ":tax_lost", ":tax_total", ":ratio_lost"),
        (store_mul, ":save", ":tax_lost", ":percent"),
        (val_div, ":save", 100),
        (val_sub, ":tax_lost", ":save"), #SB : get total not marginal savling
        (store_div, ":percent", ":tax_lost", ":tax_total"), #already x100 from above
        (val_div, ":tax_lost", 100), #do this last
      (else_try),
        (assign, ":tax_lost", 0),
        (assign, ":percent", 0),
      (try_end),
      (assign, reg0, ":tax_lost"),
      (assign, reg1, ":percent"),
    ]),
    
  ("dplmc_init_faction_gender_ratio", [
    (store_script_param, ":reset_troops", 1),
    (try_begin), #SB : reset this for non-native
      (eq, ":reset_troops", 1),
      (try_for_range, ":troop_no", regular_troops_begin, regular_troops_end),
        (is_between, ":troop_no", "trp_follower_woman", "trp_caravan_master"), #always female
        (troop_set_type, ":troop_no", tf_female),
      (else_try),
        (troop_set_type, ":troop_no", tf_male),
      (try_end),
    (try_end),
    (faction_set_slot, "fac_kingdom_1", slot_faction_gender_ratio, 20),
    (faction_set_slot, "fac_kingdom_2", slot_faction_gender_ratio, 30),
    (faction_set_slot, "fac_kingdom_3", slot_faction_gender_ratio, 50),
    (faction_set_slot, "fac_kingdom_4", slot_faction_gender_ratio, 60),
    (faction_set_slot, "fac_kingdom_5", slot_faction_gender_ratio, 40),
    (faction_set_slot, "fac_kingdom_6", slot_faction_gender_ratio, 0),

    (faction_set_slot, "fac_player_faction", slot_faction_gender_ratio, 50),
    (faction_set_slot, "fac_player_supporters_faction", slot_faction_gender_ratio, 50),
    (faction_set_slot, "fac_commoners", slot_faction_gender_ratio, 50),
    (faction_set_slot, "fac_neutral", slot_faction_gender_ratio, 100),
    (faction_set_slot, "fac_outlaws", slot_faction_gender_ratio, 10),
    ]
  ),
    # #script_cf_dplmc_disguise_evaluate_contraband
    # #input : party_no, troop_no
    # #output : reg0 (total risk), reg1 (number of contraband, marked by temp slot?)
    # ("cf_dplmc_disguise_evaluate_contraband", [
      # # (store_script_param, ":party_no", 1), #$encountered_party_faction
      # # (store_script_param, ":troop_no", 1), #should be trp_player
      # (store_script_param, ":item_no", 1),
      # (store_script_param, ":disguise_type", 2), #$sneaked_into_town
      # (assign, ":is_contraband", 0),
      # (item_set_slot, ":item_no", slot_item_temp_slot_1, 1),
      # (item_get_type, ":itp", ":item_no"),
      # (try_begin), #search
        # (eq, ":disguise_type", disguise_farmer),
        # (try_begin),
          # (eq, ":itp", itp_type_goods),
          # # (item_get_food_quality),
          
        # (try_end),
      # (try_end),
      # (eq, ":is_contraband", 1),
    # ]),
    
    # #call this once at game start?
    # #script_cf_dplmc_disguise_evaluate_equip_set
    # #input : party_no, troop_no
    # #output : all inventory item's temp slot_item_ccoop_has_ammo
    # ("cf_dplmc_disguise_parse_equip_set", [
      # # (store_script_param, ":party_no", 1), #$encountered_party_faction
      # # (store_script_param, ":troop_no", 1), #should be trp_player
      # (store_script_param, ":disguise_set", 1),
      # (store_script_param, ":troop_start", 2),
      # (store_script_param, ":troop_end", 3),
      # (assign, ":is_contraband", 0),
      # # (item_set_slot, ":item_no", slot_item_ccoop_has_ammo, 0),
      
      # (try_for_range, ":troop_no", ":troop_start", ":troop_end"), #search
        # (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
        # (try_for_range, ":item_slot", 0, ":inv_cap"),
          # (troop_get_inventory_slot, ":item_no", ":troop_no", ":item_slot"),
          # (gt, ":item_no", -1),
          # (item_get_slot, ":slot_value", ":item_no", slot_item_ccoop_has_ammo),
          # (val_or, ":slot_value", ":disguise_set"),
          # (item_set_slot, ":item_no", slot_item_ccoop_has_ammo, ":slot_value"),
        # (try_end),
      # (try_end),
    # ]),
    
    
    # #script_dplmc_disguise_evaluate_inventory
    # #input : party_no, troop_no
    # #output : reg0 (total risk), reg1 (number of contraband, marked by temp slot?)
    # ("dplmc_disguise_evaluate_inventory", [
      # (store_script_param, ":party_no", 1), #$current_town
      # (store_script_param, ":troop_no", 2), #should be trp_player
      # (store_script_param, ":disguise_type", 3), #$sneaked_into_town
      # # (store_script_param, ":enter_exit", 4), #$sneaked_into_town
      
      # #define some cutoffs
      # (try_begin),
        # (eq, ":disguise_type", disguise_pilgrim),
        # (assign, ":cutoff", 100),
        # (assign, ":max_value", 500),
      # (else_try),
        # (eq, ":disguise_type", disguise_farmer),
        # (assign, ":cutoff", 150), #price of butter
        # (assign, ":max_value", 750),
      # (else_try),
        # (eq, ":disguise_type", disguise_hunter),
        # (assign, ":cutoff", 300),
        # (assign, ":max_value", 900),
      # (else_try),
        # (eq, ":disguise_type", disguise_guard),
        # (assign, ":cutoff", 500),
        # (assign, ":max_value", 900),
      # (else_try),
        # (eq, ":disguise_type", disguise_merchant),
        # (assign, ":cutoff", 1000),
        # (assign, ":max_value", 4000),
      # (else_try),
        # (eq, ":disguise_type", disguise_bard),
        # (assign, ":cutoff", 750),
      # (else_try), #no disguise?
        # (assign, ":cutoff", 500),
        # (assign, ":max_value", 1250),
      # (try_end),
      
      # #apply skill bonus
      # (store_skill_level, ":trade", ":troop_no", "skl_trade"),
      # (store_skill_level, ":persuasion", ":troop_no", "skl_persuasion"),
      # (store_skill_level, ":inv_manage", ":troop_no", "skl_inventory_management"),
      
      # (val_mul, ":trade", 5), #bartering #0-50
      # (val_add, ":trade", ":persuasion"), # 0-60
      # (val_add, ":cutoff", ":trade"),
      
      # (val_mul, ":inv_manage", 3), #packing/hiding #0-30
      # (val_add, ":inv_manage", ":persuasion"), #0-30-40
      # (val_mul, ":max_value", 15), #0-450-600
      # (val_add, ":max_value", ":inv_manage"),
      
      # (assign, ":total_value", 0),
      # (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
      # (try_for_range, ":slot_no", 0, ":inv_cap"), #count equip
        # (troop_get_inventory_slot, ":item_no", ":troop_no", ":slot_no"),
        # (gt, ":item_no", -1),
        # (troop_get_inventory_slot_modifier, ":imod_no", ":troop_no", ":slot_no"),
        # (call_script, "script_dplmc_get_item_value_with_imod", ":item_no", ":imod_no"),
        # (val_add, ":total_value", reg0),
        # (store_div, ":item_value", reg0, 100), #scaled down
        
        # (try_begin),
        # (try_end),
      # (try_end),
      
      # (try_begin),
        # (gt, ":total_value", ":max_value"),
      # (try_end),
    # ),
    # ]),
]