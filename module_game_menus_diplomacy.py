from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
#SB : optional menu toggles
# from header_sounds import sf_vol_1
from ID_info_pages import *
from header_triggers import key_left_shift, key_right_shift
from module_constants import *
from compiler import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
# Also, 2, 4, 5 and 7 must be "start_phase_2", "tutorial", "reports" and "custom_battle_end"
####################################################################################################################

diplomacy_game_menus = [

  ##diplomacy begin
########################################################
# Autoloot Game Menus Begin
########################################################

	##########################################################
	# Inventory allocation / Loot allocation Game Menu  -  by Fisheye
	# Parameters:
	# $return_menu : return to this menu after managing loot.  0 if this menu is called via random encounter
	##diplomacy start+
	#Added "return_menu", renaming it to "$dplmc_return_menu"
	##diplomacy end+
	("dplmc_manage_loot_pool", mnf_enable_hot_keys,
		"{s10}^{s30}",
		"none",
		[
			##diplomacy start+
			#Use a different troop!
			#(assign, "$pool_troop", "trp_dplmc_chamberlain"),
			(assign, "$pool_troop", "trp_temp_troop"),
			#Make sure things are initialized
			(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
			##diplomacy end+
			(assign, reg20,0),
			(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
			(try_for_range, ":i_slot", 0, ":inv_cap"),
				(troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
				(ge, ":item_id", 0),
				(neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
				(val_add, reg20, 1),
			(try_end),
			# reg20 now contains number of items in loot pool
			(try_begin),
				(eq, reg20, 0),
				(str_store_string, s10, "str_dplmc_item_pool_no_items"),
				(str_store_string, s20, "str_dplmc_item_pool_leave"),
			(else_try),
				(eq, reg20, 1),
				(str_store_string, s10, "str_dplmc_item_pool_one_item"),
				(str_store_string, s20, "str_dplmc_item_pool_abandon"),
			(else_try),
				(str_store_string, s10, "str_dplmc_item_pool_many_items"),
				(str_store_string, s20, "str_dplmc_item_pool_abandon"),
			(try_end),
		  ## CC
			(try_begin), #only show when we don't have equipment logs
              (str_is_empty, dplmc_loot_string),
			  (set_fixed_point_multiplier, 100),
              (position_set_x, pos0, 20),
              (position_set_y, pos0, 30),
              (position_set_z, pos0, 80),
			  (set_game_menu_tableau_mesh, "tableau_game_character_sheet", "$lord_selected", pos0),
			(try_end),
		  ## CC
          
          #SB : str30 shows items looted after script_dplmc_auto_loot_troop was called
          # (try_begin),
            # (neg|str_is_empty, dplmc_loot_string),
            # (str_store_string, s10, "@{s10}^^{s30}"),
          # (try_end),
		],
		[
			("dplmc_auto_loot",
				[
					(eq, "$inventory_menu_offset",0),
					(store_free_inventory_capacity, ":space", "$pool_troop"),
					(ge, ":space", 10),
					(gt, reg20, 0),
				],
				##diplomacy start+
				#"Let your heroes select gear from the item pool.",
				"Let your heroes select gear from the items on the ground.",
				##diplomacy end+
				[
					# (set_player_troop, "trp_player"),
					# (assign, "$lord_selected", "trp_player"),
					##diplomacy start+
					(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
					##diplomacy end+
					(jump_to_menu, "mnu_dplmc_auto_loot")
				]
			),
			("dplmc_auto_loot_no",
				[
					(eq, "$inventory_menu_offset",0),
					(store_free_inventory_capacity, ":space", "$pool_troop"),
					(lt, ":space", 10),
					(disable_menu_option)
				],
				"Insufficient item pool space for auto-upgrade.",
				[]
			),
			("dplmc_loot",
				[],
				##diplomacy start+
				#"Access the item pool.",
				"Access the items on the ground.",
				##diplomacy end+
				[
					(change_screen_loot, "$pool_troop"),
				]
			),

            #SB : improve usability, if only change_screen_loot worked with the player
			("dplmc_loot_player",
				[(is_between, "$lord_selected", companions_begin, companions_end),],
				"Access the captain's inventory.",
                #can't use honorific, since the player troop is the companion and strings will be malformed
				[
					(set_player_troop, "trp_player"),
					(change_screen_equip_other, "$lord_selected"),
					(assign, "$lord_selected", "trp_player"),
				]
			),
            
            #SB : improve usability, if only change_screen_loot worked with the player
			("dplmc_loot_spouse",
				[
                 (neq, "$lord_selected", "trp_player"),
                 (this_or_next|troop_slot_eq, "$lord_selected", slot_troop_spouse, "trp_player"),
                 (troop_slot_eq, "trp_player", slot_troop_spouse, "$lord_selected"),
                ],
				"Access your spouse's inventory.",
                #can't use honorific, since the player troop is the companion and strings will be malformed
				[
					(set_player_troop, "trp_player"),
					(change_screen_equip_other, "$lord_selected"),
					(assign, "$lord_selected", "trp_player"),
				]
			),
      ("dplmc_auto_loot_upgrade_management", [],
##diplomacy start+
#        "Upgrade management of the NPC's equipments.",
         "Update management of NPC equipment.", #SB : just use acronym
##diplomacy end+
        [
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          ##nested diplomcy start+ Add error check.
          
          ##nested diplomacy end+
          (try_begin),
            (is_between, "$lord_selected", companions_begin, companions_end),
            (assign, "$temp", "$lord_selected"),
          (else_try),
            (assign, "$temp", -1),  
            (try_for_range, ":stack_no", 0, ":num_stacks"),
              (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
              (is_between, ":stack_troop", companions_begin, companions_end),
              (assign, "$temp", ":stack_troop"),
              (assign, ":num_stacks", 0),
            (try_end),
          (try_end),
          ##nested diplomacy start+   Add error check.
          (call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
          (try_begin),#<- dplmc+ added
            (ge, "$temp", 1),#<- dplmc+ added
            (assign, "$temp_2", -1), #SB : other globals
            (try_for_range, ":item_slot", ek_item_0, ek_food),
              (troop_set_slot, "trp_stack_selection_ids", ":item_slot", 0),
            (try_end),
            (str_clear, dplmc_loot_string),
            (start_presentation, "prsnt_dplmc_autoloot_upgrade_management"),
          (try_end),
          ##nested diplomacy end+
        ]
      ),
      
      #all other options will reset player eventually, this is for convenience
      ("dplmc_auto_loot_reset_player", [(neq, "$lord_selected", "trp_player")],
         "Reset current troop to the player",
        [
          (assign, "$lord_selected", "trp_player"),
          (set_player_troop, "$lord_selected"),
        ]
      ),
			("dplmc_leave",
				[],
				"{s20}",
				[
				##diplomacy start+
				#Actually abandon the lost loot
				(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
				(try_for_range, ":i_slot", 10, ":inv_cap"),
					(troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					(ge, ":item_id", 0),
					(neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
					(troop_set_inventory_slot, "$pool_troop", ":i_slot", -1), #delete it
					(troop_inventory_slot_set_item_amount, "$pool_troop", ":i_slot", 0),
				(try_end),

				#(jump_to_menu, "mnu_camp"),
				(set_player_troop, "trp_player"),
				(jump_to_menu, "$dplmc_return_menu"),
				(assign, "$pool_troop", -1), #mark ending
				##diplomacy end+
				]
			),
			##nested diplomacy start+
			#Leave & take everything you can
			("dplmc_leave_and_take_a",
				[
				(store_free_inventory_capacity, ":space", "trp_player"),
				(lt, ":space", reg20),
				(gt, reg20, 0),
				(gt, ":space", 0),
				(assign, reg0, ":space"),
				],
				"Gather {reg0} of the {reg20} items on the ground and leave.",
				[
					(store_free_inventory_capacity, ":space", "trp_player"),
					#Take remaining items for player
					(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
					(troop_sort_inventory, "$pool_troop"),
					(try_for_range, ":i_slot", 10, ":inv_cap"),
					    (gt, ":space", 0),
					    (troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					    (ge, ":item_id", 0),
					    (neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
					    (troop_get_inventory_slot_modifier, ":imod", "$pool_troop", ":i_slot"),
					    (troop_add_item, "trp_player", ":item_id", ":imod"),#give item to player
					    (val_sub, ":space", 1),
					    (troop_set_inventory_slot, "$pool_troop", ":i_slot", -1), #remove item from pool
					    (troop_inventory_slot_set_item_amount, "$pool_troop", ":i_slot", 0),
					(try_end),
					#(jump_to_menu, "mnu_camp"),
					(set_player_troop, "trp_player"),
					(jump_to_menu, "$dplmc_return_menu"),
					(assign, "$pool_troop", -1), #mark ending
				]
			),
			("dplmc_leave_and_take_b",
				[
				(store_free_inventory_capacity, ":space", "trp_player"),
				(ge, ":space", reg20),
				(gt, reg20, 0),#don't show if nothing is on the ground
				(store_sub, reg0, reg20, 1),
				],
				"Gather the remaining {reg20} {reg0?items:item} on the ground and leave.",
				[
					(store_free_inventory_capacity, ":space", "trp_player"),
					#Take remaining items for player
					(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
					(try_for_range, ":i_slot", 10, ":inv_cap"),
					    (gt, ":space", 0),
					    (troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					    (ge, ":item_id", 0),
					    (neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
					    (troop_get_inventory_slot_modifier, ":imod", "$pool_troop", ":i_slot"),
					    (troop_add_item, "trp_player", ":item_id", ":imod"),#give item to player
					    (val_sub, ":space", 1),
					    (troop_set_inventory_slot, "$pool_troop", ":i_slot", -1), #remove item frlom pool
					    (troop_inventory_slot_set_item_amount, "$pool_troop", ":i_slot", 0),
					(try_end),
					(set_player_troop, "trp_player"),
					(jump_to_menu, "$dplmc_return_menu"),
					(assign, "$pool_troop", -1), #mark ending
				]
			),
			("dplmc_leave_and_take_c",
				[
				(store_free_inventory_capacity, ":space", "trp_player"),
				(eq, ":space", 0),
				(gt, reg20, 0),#don't show if nothing is on the ground
				(disable_menu_option),
				],
				"There is no space left in your bags.",
				[
				]
			),
			##nested diplomacy end+
		]
	),

	("dplmc_auto_loot",
		0,
##diplomacy start+
		"Your heroes will automatically grab items from the loot pool based on their pre-selected upgrade options. Heroes listed first in the party order will have first pick. Any equipment no longer needed will be dropped back into the loot pool. Any items in the loot pool will be lost when you leave.^ Are you sure you wish to do this?",
##diplomacy end+
		"none",
		[],
		[
			("dplmc_autoloot_no",
				[],
				"No, I've changed my mind.",
				[
					(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
				]
			),
			("dplmc_autoloot_yes",
				[],
				"Yes, perform the upgrading.",
				[
					##diplomacy start+
					(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
					(assign, "$pool_troop", "trp_temp_troop"),
					#SB : reset variables
					(set_player_troop, "trp_player"),
					(assign, "$lord_selected", "trp_player"),
					##diplomacy end+
					(call_script, "script_dplmc_auto_loot_all", "trp_temp_troop", dplmc_loot_string),
					(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
				]
			),
            
            #SB : individual looting
			("dplmc_autoloot_personal",
				[(is_between, "$lord_selected", companions_begin, companions_end),(str_store_troop_name, s1, "$lord_selected")],
				"Yes, only upgrade {s1}.",
				[
					##diplomacy start+
					(assign, "$pool_troop", "trp_temp_troop"),
					(call_script, "script_dplmc_auto_loot_troop", "$lord_selected", "$pool_troop", dplmc_loot_string),
					##diplomacy end+
					(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
				]
			),
		]
	),


  (
    "dplmc_notification_alliance_declared",0,
    "Alliance Agreement^^{s1} and {s2} have formed an alliance!^{s57}",
    "none",
    [

	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_defensive_declared",0,
    "Defensive Pact^^{s1} and {s2} have agreed to a defensive pact!^{s57}",
    "none",
    [

	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_trade_declared",0,
    "Trade Agreement^^{s1} and {s2} have signed a trade agreement!^{s57}",
    "none",
    [

	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_nonaggression_declared",0,
    "Non-aggression Treaty^^{s1} and {s2} have concluded a non-aggression treaty!^{s57}",
    "none",
    [
	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_alliance_offer",0,
    "You Receive an Alliance Offer^^The {s1} wants to form an alliance with you. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_alliance_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_alliance_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_alliance_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_defensive_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a defensive pact. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_defensive_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_defensive_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_defensive_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_trade_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a trade pact. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_trade_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_trade_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_nonaggression_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a non-aggression treaty. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_nonaggression_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_nonaggression_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_nonaggression_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_alliance_expired",0,
    "Alliance Has Expired^^The alliance between {s1} and {s2} has expired and was degraded to a defensive pact.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_defensive_expired",0,
    "Defensive Pact Has Expired^^The defensive pact between {s1} and {s2} has expired and was degraded to a trade agreement.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),


  (
    "dplmc_notification_trade_expired",0,
    "Trade Agreement Has Expired^^The trade agreement between {s1} and {s2} has expired and was degraded to a non-aggression treaty.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),

  ("dplmc_dictate_terms",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Dictate your peace terms.",
    "none",
    [(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),],
    [
      ("dplmc_demand_4000",[(gt, "$g_player_chamberlain", 0),],"Demand 4000 denars",
      [
        (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
        (assign, ":goodwill", reg0),
        (store_random_in_range, ":random", 0, 4),

        (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -3),
        (try_begin),
          (le, ":random", ":goodwill"),
          (call_script, "script_dplmc_pay_into_treasury", 4000),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
          (change_screen_return),
        (else_try),
          (jump_to_menu,"mnu_dplmc_deny_terms"),
        (try_end),
      ]),
      ("dplmc_demand_8000",[(gt, "$g_player_chamberlain", 0),],"Demand 8000 denars",
       [
         (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
         (assign, ":goodwill", reg0),
         (val_mul, ":goodwill", 2),
				 (store_random_in_range, ":random", 0, 10),

         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
				 (try_begin),
				   (le, ":random", ":goodwill"),
           (call_script, "script_dplmc_pay_into_treasury", 8000),
           (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
           (change_screen_return),
         (else_try),
             (jump_to_menu,"mnu_dplmc_deny_terms"),
         (try_end),
       ]),
      ("dplmc_demand_castle",[
        (assign, ":distance", 100),
        (assign, "$demanded_castle", -1),
        ##diplomacy start+ Handle player is co-ruler of NPC kingdom
        (assign, ":alt_faction", "fac_player_supporters_faction"),
        (try_begin),
            (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
            (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
            (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
            (assign, ":alt_faction", "$players_kingdom"),
        (try_end),
        ##diplomacy end+
        (try_for_range, ":castle", castles_begin, castles_end),
          (store_faction_of_party, ":castle_faction", ":castle"),
          (eq, ":castle_faction", "$g_notification_menu_var1"),
          (try_for_range, ":center", centers_begin, centers_end),
            (store_faction_of_party, ":center_faction", ":center"),
            ##diplomacy start+
            (this_or_next|eq, ":alt_faction", ":center_faction"),
            ##diplomacy end+
            (eq, ":center_faction", "fac_player_supporters_faction"),
            (store_distance_to_party_from_party, ":tmp_distance", ":center", ":castle"),

            (lt, ":tmp_distance", ":distance"),
            (assign, ":distance", ":tmp_distance"),
            (assign, "$demanded_castle", ":castle"),
            (str_store_party_name, s2, ":castle"),
          (try_end),
        (try_end),
        (is_between, "$demanded_castle", castles_begin,castles_end),
      ],"Demand {s2}.",
       [
        (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
        (assign, ":goodwill", reg0),
        (val_mul, ":goodwill", 2),
        (store_random_in_range, ":random", 0, 12),

        (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -6),
        (try_begin),
          (le, ":random", ":goodwill"),
			 ##diplomacy start+
			 #Chance of veto based on ownership and difficulty setting.
			 (assign, ":did_veto", 0),
			 (try_begin),
					 (party_get_slot, ":castle_lord", "$demanded_castle", slot_town_lord),
					 (ge, ":castle_lord", 1),
					 (neg|troop_slot_ge, ":castle_lord", slot_troop_prisoner_of_party, 0),
					 (try_begin),
								(this_or_next|troop_slot_eq, ":castle_lord", slot_troop_home, "$demanded_castle"),
								(party_slot_eq, "$demanded_castle", dplmc_slot_center_original_lord, ":castle_lord"),
								(store_random_in_range, ":random", 0, 24),
								(assign, ":did_veto", 1),
								(le, ":random", ":goodwill"),
								(assign, ":did_veto", 0),
 					 (else_try),
								(troop_get_slot, ":castle_lord_original_faction", ":castle_lord", slot_troop_original_faction),
								(party_slot_eq, "$demanded_castle", slot_center_original_faction, ":castle_lord_original_faction"),
								(store_random_in_range, ":random", 0, 12),
								(assign, ":did_veto", 1),
								(le, ":random", ":goodwill"),
								(assign, ":did_veto", 0),
					 (try_end),
			 (try_end),
			 (eq, ":did_veto", 0),
		  ##Handle player is co-ruler of NPC kingdom
          ##OLD:
          #(call_script, "script_give_center_to_faction", "$demanded_castle", "fac_player_supporters_faction"),
          #(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
		  ##NEW:
		  (assign, ":player_kingdom", "fac_player_supporters_faction"),
		  (try_begin),
		        (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
				(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
				(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
				(assign, ":player_kingdom", "$players_kingdom"),
		  (try_end),
		  (call_script, "script_give_center_to_faction", "$demanded_castle", ":player_kingdom"),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", ":player_kingdom", 1),
		  ##diplomacy end+
          (change_screen_return),
        (else_try),
          (jump_to_menu,"mnu_dplmc_deny_terms"),
        (try_end),        ]
       ),
	  ("dplmc_go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_question_peace_offer"),
       ]),
    ]
  ),

  ("dplmc_deny_terms",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The {s1} refuses your terms and is breaking off of negotiations.",
    "none",
    [(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),],
    [
	  ("dplmc_continue",[],"Continue",
       [
       (change_screen_return),
       ]),
    ]
  ),

  (
    "dplmc_village_riot_result",mnf_scale_picture,
    "{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_dplmc_village_riot_removed"),
     (else_try),
       (set_background_mesh, "mesh_pic_villageriot"),
       (str_store_string, s9, "@Try as you might, you could not defeat the rebelling village."),
     (try_end),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (call_script, "script_change_troop_renown", "trp_player", -5), #SB : renown loss highest here
        (jump_to_menu, "mnu_village"),]),
    ],
  ),

  (
    "dplmc_village_riot_removed",mnf_disable_all_keys,
    "In bloody battle you and your men slaughter the rebels and regain control over the village. But there is not much left you can control.",
    "none",
    [
     (set_background_mesh, "mesh_pic_looted_village"),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (call_script, "script_village_set_state",  "$current_town", svs_looted),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (jump_to_menu, "mnu_village"),
       ]),
    ],
  ),

  (
    "dplmc_town_riot_removed",mnf_disable_all_keys,
    "In bloody battle you and your men slaughter the rebels and regain control over the town.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (assign, "$new_encounter", 1),
        (try_begin),
          (party_get_slot, ":town_lord","$g_encountered_party", slot_town_lord),
          (troop_get_slot, ":cur_banner", ":town_lord", slot_troop_banner_scene_prop),
          (gt, ":cur_banner", 0),
          (val_sub, ":cur_banner", banner_scene_props_begin),
          (val_add, ":cur_banner", banner_map_icons_begin),
          (party_set_banner_icon, "$g_encountered_party", ":cur_banner"),
        (try_end),
        (jump_to_menu, "mnu_castle_outside"),
       ]),
    ],
  ),

  (
    "dplmc_riot_negotiate",mnf_disable_all_keys,
    "You approach the angry crowd and begin negotiations. The leader of the riot demands {reg0} denars. He agrees to lay down arms if you are willing to pay.",
    "none",
    [
      (party_get_slot, ":center_relation", "$g_encountered_party", slot_center_player_relation),
      (val_min, ":center_relation", 0),
      (try_begin),
        (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
        (val_sub, ":center_relation", 75),
        (set_background_mesh, "mesh_pic_townriot"),
      (else_try),
        (val_sub, ":center_relation", 50),
        (set_background_mesh, "mesh_pic_villageriot"),
      (try_end),

      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (val_add, ":center_relation", ":persuasion_level"),
      (val_mul, ":center_relation", ":center_relation"),
      (assign, reg0, ":center_relation"),
    ],
    [
      ("dplmc_pay_riot_treasury",
      [
        (gt, "$g_player_chamberlain", 0),
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", reg0),
      ],"Induce your chamberlain to pay the money from the treasury.",
       [
        (call_script, "script_dplmc_withdraw_from_treasury", reg0),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (try_begin),  #SB : swap menu order for castles
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_castle_outside"),
        (try_end),
        
        #SB TODO : remove the townsman/watchman added from riot

       ]),
       ("dplmc_pay_riot_cash",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", reg0),
      ],"Pay cash.",
       [
        (troop_remove_gold, "trp_player", reg0),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (try_begin), #SB : swap menu order for castles
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_castle_outside"),
        (try_end),

       ]),

      ("dplmc_back",[],"Back...",
       [
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
       ]),
    ],
  ),

  (
    "dplmc_notification_riot",0,
    "The peasants of {s1} launched a riot against you! In a surprise attack, men loyal to you have been slain. The remainder joined the angry crowd.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (try_begin),
        (party_slot_eq, "$g_notification_menu_var1", slot_party_type, spt_town),
        (set_background_mesh, "mesh_pic_townriot"),
      (else_try),
        (set_background_mesh, "mesh_pic_villageriot"),
      (try_end),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_appoint_chamberlain",0,
    #SB : your court
    "As a lord of a fief you can now appoint a chamberlain who resides at your court for a weekly salary of "+str(dplmc_chamberlain_salary)+" denars. He will handle all financial affairs like collecting and determining taxes, paying wages and managing your estate. In addition he supervises money transfers between kingdoms giving you more diplomatic options.",
    "none",
    [
    #SB : tableau notes
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "trp_dplmc_chamberlain", pos0),
    ],
    [

      ("dplmc_appoint_default",[],"Appoint a prominent nobleman from the area.",
       [
        (call_script, "script_dplmc_appoint_chamberlain"),
        (jump_to_menu, "mnu_dplmc_chamberlain_confirm"),
        ]),
      ("dplmc_continue",[],"Proceed without chamberlain.",
       [
         (assign, "$g_player_chamberlain", -1), #denied
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_chamberlain_confirm",0,
    "Your chamberlain can be found at your court. You should consult him if you want to give him any financial advice or if you need greater amounts of money. You should always make sure that there is enough money in the treasury to pay for political affairs.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_appoint_constable",0,
    #SB : your court, also walled center clarification
    "As a lord of a fortified center you can now appoint a constable who resides at your court for a weekly salary of "+str(dplmc_constable_salary)+" denars. He will recruit new troops and provide information about your army.",
    "none",
    [
    #SB : tableau notes
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "trp_dplmc_constable", pos0),
    ],
    [

      ("dplmc_appoint_default",[],"Appoint a prominent nobleman from the area.",
       [
        (call_script, "script_dplmc_appoint_constable"),
        (jump_to_menu, "mnu_dplmc_constable_confirm"),
        ]),
      ("dplmc_continue",[],"Proceed without constable.",
       [
         (assign, "$g_player_constable", -1), #denied
         (assign, "$g_constable_training_center", -1),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_constable_confirm",0,
    "Your constable can be found at your court. You should consult him if you want to recruit new troops or get detailed information about your standing army.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),



  (
    "dplmc_notification_appoint_chancellor",0,
    #SB : your court, fief->city
    "As a lord of a realm and owner of a city you can now appoint a chancellor who resides at your court for a weekly salary of "+str(dplmc_chancellor_salary)+" denars. He will be the keeper of your seal and conduct the correspondence between you and other important persons.",
    "none",
    [
    #SB : tableau notes
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "trp_dplmc_chancellor", pos0),
    ],
    [

      ("dplmc_appoint_default",[],"Appoint a prominent nobleman from the area.",
       [
        (call_script, "script_dplmc_appoint_chancellor"),
        (jump_to_menu, "mnu_dplmc_chancellor_confirm"),
        ]),
      ("dplmc_continue",[],"Proceed without chancellor.",
       [
         (assign, "$g_player_chancellor", -1), #denied
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_chancellor_confirm",0,
    "Your chancellor can be found at your court. You should consult him if you want to send messages or gifts.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),


  (
    "dplmc_deserters",0,
    "Some of your men don't believe that you will pay their wages and desert. Overall you lose: {s11} men.",
    "none",
    [
      (set_background_mesh, "mesh_pic_deserters"),
      (store_random_in_range, ":random", 1,  "$g_notification_menu_var1"),
      (call_script, "script_dplmc_player_troops_leave", ":random"),
      (str_store_string, s11, "@{reg0}"),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_negotiate_besieger",0,
    "You appear with a white flag at the top of the wall. After a while a negotiator of {s11} approaches you. He demands {s6} and all associated villages as well as {reg0} denars for safe conduct.",
    "none",
    [
      (party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
      (party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
      (str_store_troop_name, s11, ":enemy_party_leader"),
      (store_faction_of_troop, ":besieger_faction", ":enemy_party_leader"),

      ##diplomacy start+
	  #1) Support promoted kingdom ladies, mercenary parties, etc.
	  #2) Fix mistake with potentially not counting besieger party in the size calculation!
	  ##OLD:
	  #(assign, ":besieger_size", 0),
      #(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
      #  (store_faction_of_troop, ":lord_faction", ":lord"),
      #  (eq, ":lord_faction", ":besieger_faction"),
      #  (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
      ##NEW:
      (party_get_num_companions, ":besieger_size", ":besieger"),

	  (try_for_parties, ":led_party"),
        (ge, ":led_party", spawn_points_end),
        (neq, ":led_party", ":besieger"),#don't double count
        (store_faction_of_party, ":party_faction", ":led_party"),
        (eq, ":party_faction", ":besieger_faction"),
	  ##diplomacy end+
        (party_is_active, ":led_party"),

        (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
        (party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),

        (party_is_active, ":besieger"),
        (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
        (lt, ":distance_to_marshal", 25),
        (party_get_num_companions, ":party_size", ":led_party"),
        (val_add, ":besieger_size", ":party_size"),
      (try_end),

      (assign, ":garrison_size", 0),
      (party_get_num_companion_stacks, ":num_stacks", "$current_town"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size", "$current_town", ":i_stack"),
        (val_add, ":garrison_size", ":stack_size"),
      (try_end),
      (val_sub, ":besieger_size", ":garrison_size"),

      (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
      (val_mul, ":player_persuasion_skill", 10),
      (store_sub, "$diplomacy_var", ":besieger_size", ":player_persuasion_skill"),
      (val_mul, "$diplomacy_var", 4),
      ##diplomacy start+ : include ransom cost in calculation
      (call_script, "script_calculate_ransom_amount_for_troop", "trp_player"),
      (val_add, "$diplomacy_var", reg0),
      ##diplomacy end+
      (val_max,"$diplomacy_var",500),
      (val_div, "$diplomacy_var", 100),
      (val_mul, "$diplomacy_var", 100),
      (assign, reg0, "$diplomacy_var"),

      (str_store_party_name, s6, "$current_town"),

    ],
      [
      ("dplmc_comply_treasury",
      [
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", "$diplomacy_var"),
      ],"Comply and induce your chamberlain to pay the money from the treasury.",
      [
        (call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
		##diplomacy start+ when the player pays, give the gold to the lord
		(party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
		(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", "$diplomacy_var", ":enemy_party_leader"),
		##diplomacy end+
        (call_script, "script_dplmc_player_center_surrender", "$current_town"),
        (change_screen_return),
      ]),

      ("dplmc_comply",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", "$diplomacy_var"),
      ],"Comply and pay the gold.",
      [
        (troop_remove_gold, "trp_player", "$diplomacy_var"),
		##diplomacy start+ when the player pays, give the gold to the lord
		(party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
		(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", "$diplomacy_var", ":enemy_party_leader"),
		##diplomacy end+
        (call_script, "script_dplmc_player_center_surrender", "$current_town"),
        (change_screen_return),
      ]),

      ("dplmc_break_off",[],"Break off negotiations.",
       [
          (jump_to_menu, "mnu_town"),
        ]),
     ]
  ),


  (
    "dplmc_messenger",0,
##nested diplomacy start+ "His" to "{reg4?Her:His}"
    "Sire, I found {s10} and delivered your message. {reg4?Her:His} answer was {s11}.",
##nested diplomacy end+
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (str_store_troop_name, s10, "$g_notification_menu_var1"),
        (try_begin),
          (eq, "$g_notification_menu_var2", 1),
          (str_store_string, s11, "@positive"),
        (else_try),
          (str_store_string, s11, "@negative"),
        (try_end),
        ##nested diplomacy start+
        (try_begin),
           (call_script, "script_cf_dplmc_troop_is_female", "$g_notification_menu_var1"),
           (assign, reg4, 1),
        (else_try),
           (assign, reg4, 0),
        (try_end),
        ##nested diplomacy end+
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_scout",0,
    "Your spy returned from {s10}^^{s11}{s12}",
    "none",
    [
    (set_background_mesh, "mesh_pic_messenger"),
    (str_store_party_name, s10, "$g_notification_menu_var1"),

    (call_script, "script_game_get_center_note", "$g_notification_menu_var1", 0),
    (str_store_string, s11, "@{!}{s0}"),
    (try_begin),
      (this_or_next|is_between, "$g_notification_menu_var1", towns_begin, towns_end),
      (is_between, "$g_notification_menu_var1", castles_begin, castles_end),
      (party_get_slot, ":center_food_store", "$g_notification_menu_var1", slot_party_food_store),
      (call_script, "script_center_get_food_consumption", "$g_notification_menu_var1"),
      (assign, ":food_consumption", reg0),
      (store_div, reg6, ":center_food_store", ":food_consumption"),
      (store_party_size, reg5, "$g_notification_menu_var1"),
      (str_store_string, s11, "@{s11}^^ The current garrison consists of {reg5} men.^The food stock lasts for {reg6} days."),
    (try_end),

    (str_clear, s12),
    (party_get_num_attached_parties, ":num_attached_parties", "$g_notification_menu_var1"),
    (try_begin),#<- dplmc+ unclosed try_begin!
      (gt, ":num_attached_parties", 0),
      (str_store_string, s12, "@^^Additional the following parties are currently inside:^"),
    (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
      (party_get_attached_party_with_rank, ":attached_party", "$g_notification_menu_var1", ":attached_party_rank"),
      (str_store_party_name, s3, ":attached_party"),
      (store_party_size, reg1, ":attached_party"),
      (str_store_string, s12, "@{s12} {s3} with {reg1} troops.^"),
    (try_end),
	##diplomacy start+
	#Add missing try-end for (gt, ":num_attached_parties", 0),
	(try_end),
	##diplomacy end+

    (call_script, "script_update_center_recon_notes", "$g_notification_menu_var1"),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_domestic_policy",0,
    "You can now shape the domestic policy of your kingdom. Do you want to change your policy now?",
    "none",
    [
      (try_begin),
          (eq, "$g_players_policy_set", 1),
          (change_screen_return),
      (try_end),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
    ],
    [
      ("dplmc_yes",[],"Yes, I want to change the domestic policy.",
       [
         (assign, "$g_faction_selected", "fac_player_supporters_faction"),
         (start_presentation, "prsnt_dplmc_policy_management"), #SB : reassign global
        ]),
      ("dplmc_no",[],"No, I don't want to change the domestic policy.",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_affiliate_end",0,
    "{!}{s11}",
    "none",
    [
      (set_background_mesh, "mesh_pic_messenger"),

      (str_store_troop_name, s9, "$g_notification_menu_var1"),
      (try_begin),
        ##nested diplomacy start+ (1) Fix a bug from the Diplomacy 3.3.2 version of this menu by getting your ex-affiliate
	    #from "$g_notification_menu_var2" instead of "$g_player_affiliated_troop".
        ##OLD: #(eq, "$g_player_affiliated_troop", "$g_notification_menu_var1"),
        (eq, "$g_notification_menu_var2", "$g_notification_menu_var1"),
        ##nested diplomacy end+
        #SB : some fixes
        (str_store_string, s11, "@{playername}, ^^I always knew you were a bad egg, since the day you have pledged allegiance to my clan. ^Did you really think you could set my family against me? You've dropped your mask, you snake! You are an infliction, and I will not bear it anymore. ^Hereby, I disown and ban you from my house. I have urged my family to fight you, and I will warn all Calradian lords of your infamy. ^Tremble with fear, for now you have a deadly enemy! ^^{s9}."),
      (else_try),
        ##nested diplomacy start+ (2) Fix a bug from the Diplomacy 3.3.2 version of this menu by getting your ex-affiliate
	    #from "$g_notification_menu_var2" instead of "$g_player_affiliated_troop".
        ##OLD:
		#(is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
        #(str_store_troop_name, s10, "$g_player_affiliated_troop"),
		##NEW:
		(ge, "$g_notification_menu_var2", walkers_end),
        (troop_is_hero, "$g_notification_menu_var2"),
		(str_store_troop_name, s10, "$g_notification_menu_var2"),
        ##### (3) Make the next line use correct pronouns, and correct term for king/queen.  TODO: Change some of the funny wording.
		##OLD:
        #(str_store_string, s11, "@{playername},^^ I've received a letter from {s9}, telling me about your disgracefull jiggery-pokery. In the present circumstances, {s9} could not provide evidence. But unlike you, {he/she} is a distinguished member of my family; and since all these years, I never had any reason to distrust {him/her}. I take {his/her} charges for granted. ^Hopefully, you failed to breakup my family unit. Hereby I reject your pledge : you are no longer related to my house. Each membership will retaliate against you in all conscience... ^I would be ashamed to confess how you maliciously fooled me, so I will not challenge you, to not be accountable for your death to my King. However I'm not used to report him every rat I crush while in wilderness, someday I may find you there ! ^^{s10}"),
		##NEW:
		(call_script, "script_dplmc_store_troop_is_female", "$g_notification_menu_var1"),
		(assign, reg1, reg0),#Move to reg1, because reg0 will be overwritten below
        (store_faction_of_troop, ":faction_var", "$g_notification_menu_var2"),
		(try_begin),
		   (gt, ":faction_var", 0),
		   (faction_get_slot, ":faction_var", ":faction_var", slot_faction_leader),
		   (gt, ":faction_var", 0),
		   (call_script, "script_dplmc_store_troop_is_female", ":faction_var"),
		   (eq, reg0, 1),
		   (call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_notification_menu_var2", DPLMC_CULTURAL_TERM_KING_FEMALE, s11),
		   (assign, reg1, 1),#make sure the above didn't do anything funny with the register
		(else_try),
		   (call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_notification_menu_var2", DPLMC_CULTURAL_TERM_KING, s11),
		   (assign, reg1, 0),#if there was no faction leader, reg0 might not have been initialized in the first place
		(try_end),
		#Aside from making the next line use the correct gender for the pronoun,
		#I made the wording a tiny bit less strange (although I left in "jiggery-pokery").
        #SB : some fixes (him->his)
        (str_store_string, s11, "@{playername},^^ I've received a letter from {s9}, telling me about your disgraceful jiggery-pokery. In the present circumstances, {s9} could not provide evidence. But unlike you, {reg1?she:he} is a distinguished member of my family; and in all these years, I've never had any reason to distrust {reg1?her:him}. I therefore take {reg1?her:his} charges for granted. ^Hopefully, you failed to break-up my family unit. Hereby I reject your pledge : you are no longer related to my house. Each member shall retaliate against you in all conscience... ^I would be ashamed to confess how you maliciously deceived me, so I will not challenge you, so as to not be held accountable for your death by my {s11}. However I've no need to tell {reg0?her:him} about every rat I crush in the wilderness, and someday I may find you there ! ^^{s10}"),
        ##nested diplomacy end+
      (try_end),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_preferences",0,
	##diplomacy start+ alter for PBOD
    "Diplomacy "+DPLMC_DIPLOMACY_VERSION_STRING+" Preferences{s0}",##"Diplomacy preferences",
	##diplomacy end+
    "none",
    [
	##diplomacy start+
    #SB : do verification and update script here as well
	(troop_get_slot, reg0, "trp_dplmc_chamberlain", dplmc_slot_troop_affiliated),
    (call_script, "script_dplmc_version_checker"),
	(str_clear, s0),
	(try_begin),
		#Print a warning message for bad version numbers
		(neq, reg0, 0),
		(store_mod, ":verify", reg0, 128),
		(this_or_next|lt, reg0, 0),
			(neq, ":verify", DPLMC_VERSION_LOW_7_BITS),
		(str_store_string, s0, "@{!}{s0}^^ WARNING: Unexpected version value in slot dplmc_slot_troop_affiliated in trp_dplmc_chamberlain: {reg0}"),
	(else_try),
		#In cheat mode, print the diplomacy+ version
		(ge, "$cheat_mode", 1),
		(val_div, reg0, 128),
		(str_store_string, s0, "@{!}{s0}^^ DEBUG: Internal update code for current saved game is {reg0}.^Update code for the current release is "+str(DPLMC_CURRENT_VERSION_CODE)+"."),
	(try_end),
	##diplomacy end+
    
    ##SB : enable presentation to be launched again
    (try_begin),
      (eq, "$g_presentation_next_presentation", "prsnt_redefine_keys"),
      (start_presentation, "$g_presentation_next_presentation"),
    (try_end),
    ],
    [
      ("dplmc_presentation",[],"Presentation",
       [
           # (jump_to_menu, "mnu_dplmc_preferences"),
           (start_presentation, "prsnt_adv_diplomacy_preferences"),
           (assign, "$g_presentation_next_presentation", -1),
        ]),
    #SB : adjust menu options
      ("dplmc_cheat_mode",[(assign, reg0, "$cheat_mode")],"{reg0?Dis:En}able cheat mode.",
       [
           (store_sub, "$cheat_mode", 1, "$cheat_mode"),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
        #value = 0 is on by default
      ("dplmc_horse_speed",[(assign, reg0, "$g_dplmc_horse_speed"),],"{reg0?En:Dis}able Diplomacy horse speed and culling.",
       [
           (store_sub, "$g_dplmc_horse_speed", 1, "$g_dplmc_horse_speed"),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      # ("dplmc_enable_horse_speed",[(eq, "$g_dplmc_horse_speed", 1),],"Enable Diplomacy horse speed.",
       # [
           # (assign, "$g_dplmc_horse_speed", 0),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        # ]),
        #value = 0 is on by default
      ("dplmc_battle_continuation",[(assign, reg0, "$g_dplmc_battle_continuation"),],"{reg0?En:Dis}able Diplomacy battle continuation.",
       [
           (val_clamp, "$g_dplmc_battle_continuation", 0, 2), #in case of other values
           (store_sub, "$g_dplmc_battle_continuation", 1, "$g_dplmc_battle_continuation"),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      #SB : new option
      ("dplmc_player_disguise",[(assign, reg0, "$g_dplmc_player_disguise"),],"{reg0?Dis:En}able disguise system.",
       [
           (store_sub, "$g_dplmc_player_disguise", 1, "$g_dplmc_player_disguise"),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),

      ## sb : charge + deathcam
      ("dplmc_charge_when_dead",[ (eq, "$g_dplmc_battle_continuation", 0),(assign, reg0, "$g_dplmc_charge_when_dead"),],
        "{reg0?Dis:En}able troops charging upon battle continuation.",
       [
           (store_sub, "$g_dplmc_charge_when_dead", 1, "$g_dplmc_charge_when_dead"),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
        
      ("dplmc_deathcam_keys",[ (eq, "$g_dplmc_battle_continuation", 0),],"Redefine camera keys.",
       [
           (assign, "$g_presentation_next_presentation", "prsnt_redefine_keys"),
           (start_presentation, "prsnt_redefine_keys"),
        ]),
        
      ##diplomacy start+
      #toggle terrain advantage
      ("dplmc_disable_terrain_advantage",[(eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),],"Disable terrain advantage in Autocalc battles (currently Enabled).",
       [
           (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      ("dplmc_enable_terrain_advantage",[
		(eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),],"Enable terrain advantage in Autocalc battles (currently Disabled).",
       [
           (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      ("dplmc_reset_terrain_advantage",[
		(neq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),
		(neq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
		(assign, reg0, "$g_dplmc_terrain_advantage")
		],"You used a saved game from another mod: g_dplmc_terrain_advantage = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_terrain_advantage", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#toggle lord recycling
	  ("dplmc_toggle_lord_recycling_a",[
		(eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE),
		],"Enable lords returning from exile and spawning without homes (currently disabled)",
       [
           (assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
        ]),
	  ("dplmc_toggle_lord_recycling_b",[
		(this_or_next|eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_FREQUENT),#currently this setting is not distinct
		(eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
		],"Disable lords returning from exile and spawning without homes (currently enabled)",
       [
	 	   (assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE),
        ]),
      ("dplmc_toggle_lord_recycling_reset",
		[(neq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE), #SB : fix const
 		 (neq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
		 (neq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_FREQUENT),
		 (assign, reg0, "$g_dplmc_lord_recycling"),],
			"You used a saved game from another mod: g_dplmc_lord_recycling = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_lord_recycling", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#toggle AI changes
	  ("dplmc_toggle_ai_changes_a",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
		],"Enable AI changes (currently disabled)",
       [
           (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
        ]),
	  ("dplmc_toggle_ai_changes_b",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
		],"Increase AI changes (currently low)",
       [
	 	   (assign, "$g_dplmc_ai_changes",DPLMC_AI_CHANGES_MEDIUM),
        ]),

	  ("dplmc_toggle_ai_changes_c",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
		],"Increase AI changes (currently medium)",
       [
	 	   (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
        ]),
	  ("dplmc_toggle_ai_changes_d",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
		],"Disable AI changes (currently high/experimental)",
       [
	 	   (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
        ]),
      ("dplmc_reset_ai_changes",
		[(neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
 		 (neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
		 (neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
		 (neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
		 (assign, reg0, "$g_dplmc_ai_changes"),],
			"You used a saved game from another mod: g_dplmc_ai_changes = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_ai_changes", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#toggle economics changes
	  ("dplmc_toggle_gold_changes_a",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
		],"Set economic & behavioral changes to low (current mode: disabled)",
       [
           (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
        ]),
	  ("dplmc_toggle_gold_changes_b",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		],"Set economic & behavioral changes to medium (current mode: low)",
       [
	 	   (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
        ]),
	  ("dplmc_toggle_gold_changes_c",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		],"Set economic & behavioral changes to high/experimental (current mode: medium)",
       [
	 	   (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
        ]),
	  ("dplmc_toggle_gold_changes_d",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
		],"Disable economic & behavioral changes (current mode: high/experimental)",
       [
	 	   (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
        ]),
      ("dplmc_reset_gold_changes",
		[(neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
 		 (neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		 (neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		 (neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
		 (assign, reg0, "$g_dplmc_gold_changes"),],
			"You used a saved game from another mod: g_dplmc_gold_changes = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_gold_changes", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#Toggle the default anti-woman prejudice.  This uses the already-existing
	#global variable "$g_disable_condescending_comments", and gives it additional
	#meaning.
		("dplmc_switch_woman_prejudice_1", [
			(this_or_next|eq, "$g_disable_condescending_comments", 0),
			(eq, "$g_disable_condescending_comments", 1)],
			"Change prejudice level (current level is default)",
			[(val_add, "$g_disable_condescending_comments", 2),
			(jump_to_menu, "mnu_dplmc_preferences"),]),
		("dplmc_switch_woman_prejudice_2", [
			(this_or_next|eq, "$g_disable_condescending_comments", 2),
			(eq, "$g_disable_condescending_comments", 3)],
			"Change prejudice level (current level is off)",
			[(val_sub, "$g_disable_condescending_comments", 4),
			(jump_to_menu, "mnu_dplmc_preferences"),]),
		("dplmc_switch_woman_prejudice_3", [
			(this_or_next|eq, "$g_disable_condescending_comments", -1),
			(eq, "$g_disable_condescending_comments", -2)],
			"Change prejudice level (current level is high)",
			[(val_add, "$g_disable_condescending_comments", 2),
			(jump_to_menu, "mnu_dplmc_preferences"),]),
      #SB : companion complaints
      ("dplmc_player_disguise",[(assign, reg0, "$disable_npc_complaints"),],"{reg0?En:Dis}able NPC complaints.",
       [
           (store_sub, "$disable_npc_complaints", 1, "$disable_npc_complaints"),
        ]),
##diplomacy end+
      ("dplmc_back",[],"Back...",
       [
           (jump_to_menu, "mnu_camp"),
           #SB : add blurb to info pages
           (call_script, "script_dplmc_update_info_settings"),
        ]),
     ]
  ),

  ##diplomacy end
##diplomacy start+
  ("dplmc_affiliated_family_report",0,
   "{s0}",
   "none",
   [
    (str_clear, s0),
	(str_clear, s1),
	(try_for_range, ":troop_no", active_npcs_including_player_begin, heroes_end),
		(try_begin),
			(eq, ":troop_no", active_npcs_including_player_begin),
			(assign, ":troop_no", "trp_player"),
		(try_end),
		(call_script, "script_dplmc_store_troop_is_eligible_for_affiliate_messages", ":troop_no"),
		(this_or_next|eq, ":troop_no", "trp_player"),
           (ge, reg0, 1),

		(str_clear, s1),
		(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add blank line to start

		#show name; (non-player) also show location
		(try_begin),
			(eq, ":troop_no", "trp_player"),
			(str_store_string, s1, "@{playername}"),
		(else_try),
			(call_script, "script_get_information_about_troops_position", ":troop_no", 0),#s1 = String, reg0 = knows-or-not
		(try_end),
		(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add line

		#(non-player) show relation
		(try_begin),
			(neq, "trp_player", ":troop_no"),
			(call_script, "script_troop_get_player_relation", ":troop_no"),
			(assign, reg1, reg0) ,
			(str_store_string, s1, "str_relation_reg1"),
			(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add line
		(try_end),

		#(non-prisoner) show party size
		(try_begin),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
			(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
            (this_or_next|eq, ":led_party", 0),
			   (ge, ":led_party", spawn_points_end),
			(this_or_next|eq, ":troop_no", "trp_player"),
			   (neq, ":led_party", "p_main_party"),
			(party_is_active, ":led_party"),
			(assign, reg0, 0),
			(party_get_num_companions, reg1, ":led_party"),#number of troops
            (str_store_string, s1, "@Troops: {reg1}"),
			(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add line
		(try_end),

	(try_end),
    ],
    [
	  ("lord_relations",[],"View list of all known lords by relation.",
       [
		(jump_to_menu, "mnu_lord_relations"),
        ]
       ),
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("dplmc_start_select_prejudice",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "In the traditional medieval society depicted in the game, war and politics are usually dominated by male members of the nobility.  Beacuse of this, a female character can face initial prejudice, and some opportunities open to men will not be available (although a woman will also have some opportunities a man will not).  Some players might find distasteful, so if you want you can ignore that aspect of society in Calradia.^^You can later change your mind through the options in the Camp menu.",
    "none",
    [],
    [
      ("dplmc_start_prejudice_yes",[],"I do not mind encountering sexism.",
       [
         (assign, "$g_disable_condescending_comments", 0),#Default value
         (jump_to_menu,"mnu_start_character_1"),
        ]
       ),
      ("dplmc_start_prejudice_no",[],"I would prefer not to encounter as much sexism.",
       [
         (assign, "$g_disable_condescending_comments", 2),#Any value 2 or higher shuts off sexist setting elements
         (jump_to_menu, "mnu_start_character_1"),
       ]
       ),
       #SB : enable dplmc_random_mixed_gender mission triggers
      ("dplmc_start_prejudice_mixed",[],"I would also like to see female presence on the field of battle.",
       [
         (assign, "$g_disable_condescending_comments", 4),
         (jump_to_menu, "mnu_start_character_1"),
       ]
       ),
	  ("go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_start_game_1"),
       ]),
    ]
  ),
  
  ##Economic report, currently just for debugging purposes
  ("dplmc_economic_report",0,
   "{s0}",
   "none",
   [
    (str_clear, s0),
    (str_clear, s1),
    (assign, reg0, 0),
    (str_store_string, s0, "@Prosperity Report^"),

    #Show average prosperity for each faction
    (try_for_range, ":faction", 0, kingdoms_end),
       (this_or_next|eq, ":faction", 0),
       (is_between, ":faction", kingdoms_begin, kingdoms_end),

       (this_or_next|eq, ":faction", 0),
       (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
       
       (try_begin),
          (eq, ":faction", 0),
          (str_store_string, s1, "@Total"),
       (else_try),
          (faction_get_slot, reg0, ":faction", slot_faction_adjective),
          (gt, reg0, 0),
          (str_store_string, s1, reg0),
       (else_try),
          (str_store_faction_name, s1, ":faction"),
       (try_end),

       ##(1) Faction Prosperity, towns
       (assign, ":sum", 0),
       (assign, ":q_5", 0),
       (assign, ":q_4", 0),
       (assign, ":q_3", 0),
       (assign, ":q_2", 0),
       (assign, ":q_1", 0),
       (assign, ":num", 0),
       
       (try_for_range, ":center_no", towns_begin, towns_end),
          (store_faction_of_party, reg0, ":center_no"),
          (this_or_next|eq, ":faction", 0),
          (eq, reg0, ":faction"),
          (val_add, ":num", 1),
          (party_get_slot, reg0, ":center_no", slot_town_prosperity),
          (val_add, ":sum", reg0),
          (try_begin),
             (lt, reg0, 20),
             (val_add, ":q_1", 1),
          (else_try),
             (lt, reg0, 40),
             (val_add, ":q_2", 1),
          (else_try),
             (lt, reg0, 60),
             (val_add, ":q_3", 1),
          (else_try),
             (lt, reg0, 80),
             (val_add, ":q_4", 1),
          (else_try),
             (val_add, ":q_5", 1),
          (try_end),
       (try_end),
       
       (assign, reg0, ":num"),
       (val_max, reg0, 1),
       (store_div, reg0, ":sum", reg0),
       (str_store_string, s0, "@{s0}^{s1} Average Town Prosperity: {reg0}"),
       (assign, reg0, ":q_5"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 80-100: {reg0}"),
       (try_end),
       (assign, reg0, ":q_4"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 60-79: {reg0}"),
       (try_end),
       (assign, reg0, ":q_3"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 40-59: {reg0}"),
       (try_end),
       (assign, reg0, ":q_2"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 20-39: {reg0}"),
       (try_end),
       (assign, reg0, ":q_1"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 0-19: {reg0}"),
       (try_end),
       
       (str_store_string, s0, "@{!}{s0}^"),

       ##(2) Faction Prosperity, villages
       (assign, ":sum", 0),
       (assign, ":q_5", 0),
       (assign, ":q_4", 0),
       (assign, ":q_3", 0),
       (assign, ":q_2", 0),
       (assign, ":q_1", 0),
       (assign, ":num", 0),
       
       (try_for_range, ":center_no", villages_begin, villages_end),
          (store_faction_of_party, reg0, ":center_no"),
          (this_or_next|eq, ":faction", 0),
          (eq, reg0, ":faction"),
          (val_add, ":num", 1),
          (party_get_slot, reg0, ":center_no", slot_town_prosperity),
          (val_add, ":sum", reg0),
          (try_begin),
             (lt, reg0, 20),
             (val_add, ":q_1", 1),
          (else_try),
             (lt, reg0, 40),
             (val_add, ":q_2", 1),
          (else_try),
             (lt, reg0, 60),
             (val_add, ":q_3", 1),
          (else_try),
             (lt, reg0, 80),
             (val_add, ":q_4", 1),
          (else_try),
             (val_add, ":q_5", 1),
          (try_end),
       (try_end),
       
       (assign, reg0, ":num"),
       (val_max, reg0, 1),
       (store_div, reg0, ":sum", reg0),
       (str_store_string, s0, "@{s0}^{s1} Average Village Prosperity: {reg0}"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_5", 0),
          (assign, reg0, ":q_5"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 80-100: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_4", 0),
          (assign, reg0, ":q_4"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 60-79: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_3", 0),
          (assign, reg0, ":q_3"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 40-59: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_2", 0),
          (assign, reg0, ":q_2"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 20-39: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_1", 0),
          (assign, reg0, ":q_1"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 0-19: {reg0}"),
       (try_end),
       (str_store_string, s0, "@{!}{s0}^"),
    (try_end),
    ],
    [
      ("dplmc_back",[],"Continue...",
       [
           (jump_to_menu, "mnu_reports"),
        ]),
      ]
  ),
##diplomacy end+

#SB : secondary cheat menu

  (
    "town_cheats",0,
    "Select an option to interact with the town here",
    "none",[(call_script, "script_set_town_picture"),],
    [
      ("page",
      [],
      "Next Page.",
      [
        (jump_to_menu, "mnu_town_cheats_2"),
      ]),
      
      ("debug",
      [],
      "Party Cheats.",
      [
        (jump_to_menu, "mnu_party_cheat"),
      ]),
      ("host_tournament",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),],
      "Host a tournament",
      [
           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           (jump_to_menu, "mnu_town_tournament"),
      ]),

      ("camp_cheat_gather",[(party_slot_eq, "$current_town", slot_party_type, spt_town),],"Gather all inactive NPCs.",
       [ (assign, "$npc_to_rejoin_party", -1),
         (try_for_range, ":troop_no", companions_begin, companions_end),
           (neg|main_party_has_troop, ":troop_no"),
           (troop_slot_eq, ":troop_no", slot_troop_days_on_mission, 0),
           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
            # (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
           (troop_set_slot, ":troop_no", slot_troop_cur_center, "$current_town"),
           (troop_set_slot, ":troop_no", slot_troop_turned_down_twice, 0),
         (try_end),
         # (jump_to_menu, "mnu_camp_cheat"),
        ]
        ),

      # ("camp_cheat_gather",[(party_slot_eq, "$current_town", slot_party_type, spt_town),],"Gather all NPCs not in main party (cancel missions).",
       # [ (assign, "$npc_to_rejoin_party", -1),
         # (try_for_range, ":troop_no", companions_begin, companions_end),
            # (neg|main_party_has_troop, ":troop_no"),
            # (call_script, "script_remove_troop_from_prison", ":troop_no"),
            # (try_for_range, ":slots", slot_troop_days_on_mission, slot_troop_recruit_price),
              # (troop_set_slot, ":troop_no", ":slots", 0),
            # (try_end),
            # (troop_set_slot, ":troop_no", slot_troop_cur_center, "$current_town"),
         # (try_end),
        # ]
        # ),

      ("summon_drunk",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),
       # (troop_get_slot, ":town", "trp_belligerent_drunk", slot_troop_cur_center),
       (try_begin),
         # (is_between, ":town", towns_begin, towns_end),
         (troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$current_town"),
         (assign, reg10, 1),
       (else_try),
         (assign, reg10, 0),
       (try_end),
       ],
      "{reg10?Dismiss:Get} a drunkard.",
      [
        (try_begin),
          (eq, reg10, 1),
          (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, -1),
        (else_try),
          (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "$current_town"),
        (try_end),
      ]),


      ("summon_ass",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),
       (try_begin),
         # (is_between, ":town", towns_begin, towns_end),
         (troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$current_town"),
         (assign, reg11, 1),
       (else_try),
         (assign, reg11, 0),
       (try_end),
      ],
      "{reg11?Scare away:Hire} an assassin.",
      [
        (try_begin),
          (eq, reg11, 1),
          (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
        (else_try),
          (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, "$current_town"),
        (try_end),
      ]),

      ("summon_bandit",
      [
       (neg|party_slot_eq, "$current_town", slot_party_type, spt_castle),
       (party_get_slot, reg12, "$current_town", slot_center_has_bandits),
       # (try_begin),
         # (party_slot_ge, "$current_town", slot_center_has_bandits, 1),
         # (assign, reg12, 1),
       # (else_try),
         # (assign, reg12, 0),
       # (try_end).
       (try_begin), #none present
         (eq, reg12, 0),
         (str_store_string, s12, "str_bandits"),
       (else_try),
         (str_store_troop_name_plural, s12, reg12),
       (try_end),
      ],
      "{reg12?Kick out:Get ambushed by} some {s12}.",
      [
       (try_begin), #cleanse
         (party_slot_ge, "$current_town", slot_center_has_bandits, 1),
         (party_set_slot, "$current_town", slot_center_has_bandits, 0),
       (else_try), #ambush
         (store_random_in_range, ":bandit", bandits_begin, bandits_end),
         (party_set_slot, "$current_town", slot_center_has_bandits, ":bandit"),
         (assign, "$town_nighttime", 1),
         (assign, "$sneaked_into_town", 0),
         (assign, "$g_defending_against_siege", 0),
         (call_script, "script_cf_enter_center_location_bandit_check"),
         # (assign, "$town_nighttime", 1),
       (try_end),
      ]),
      
      ("summon_village_bandit",
      [
       (party_slot_eq, "$current_town", slot_party_type, spt_village),
       (party_get_slot, reg13, "$current_town", slot_village_infested_by_bandits),
       (try_begin),
         (le, reg13, 0),
         (str_store_troop_name_plural, s13, "trp_bandit"),
       (else_try),
         (str_store_troop_name_plural, s13, reg13),
       (try_end),
      ],
      "{reg13?Cleanse:Infest} the village {reg13?of:with} {s13}.",
      [
        (try_begin), #cleanse
          (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_set_slot, "$current_town", slot_village_infested_by_bandits, 0),
        (else_try), #infest
          (call_script, "script_center_get_bandits", "$current_town", 0),
          (party_set_slot, "$current_town", slot_village_infested_by_bandits, reg0),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]),
      
      ("summon_insurgent",
      [ (party_slot_eq, "$current_town", slot_village_infested_by_bandits, 0),
      ],
      "Spearhead a peasant revolution.",
      [
        (party_set_slot, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),

        #add additional troops
        (store_character_level, ":player_level", "trp_player"),
        (store_div, ":player_leveld2", ":player_level", 2),
        (store_mul, ":player_levelx2", ":player_level", 2),
        (try_begin),
          (is_between, "$current_town", villages_begin, villages_end),
          (store_random_in_range, ":random",0, ":player_level"),
          (party_add_members, "$current_town", "trp_mercenary_swordsman", ":random"),
          (store_random_in_range, ":random", 0, ":player_leveld2"),
          (party_add_members, "$current_town", "trp_hired_blade", ":random"),
        (else_try),
          (party_set_banner_icon, "$current_town", 0),
          (party_get_num_companion_stacks, ":num_stacks","$current_town"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_size, ":stack_size","$current_town",":i_stack"),
            (val_div, ":stack_size", 2),
            (party_stack_get_troop_id, ":troop_id", "$current_town", ":i_stack"),
            (party_remove_members, "$current_town", ":troop_id", ":stack_size"),
          (try_end),
          (store_random_in_range, ":random",":player_leveld2", ":player_levelx2"),
          (party_add_members, "$current_town", "trp_townsman", ":random"),
          (store_random_in_range, ":random",0, ":player_level"),
          (party_add_members, "$current_town", "trp_watchman", ":random"),
        (try_end),
      ]),

      ("center_refresh",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),],
      "Refresh merchants (global).",
      [
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_weaponsmith),
        (call_script, "script_refresh_center_weaponsmiths"),
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_armorer),
        (call_script, "script_refresh_center_armories"),
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_horse_merchant),
        (call_script, "script_refresh_center_stables"),
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_merchant),
        (call_script, "script_refresh_center_inventories"),
        # (assign, g.selected_troop, -1),
      ]),
      
      ("village_refresh",
      [(party_slot_eq, "$current_town", slot_party_type, spt_village),],
      "Refresh village goods.",
      [
        (call_script, "script_refresh_village_merchant_inventory", "$current_town"),
      ]),

      ("village_recruits",
      [(party_slot_eq, "$current_town", slot_party_type, spt_village),],
      "Refresh recruits.",
      [
        (call_script, "script_update_volunteer_troops_in_village", "$current_town"),
      ]),
      ("center_recruits",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),],
      "Refresh mercenaries.",
      [
        (store_random_in_range, ":troop_no", mercenary_troops_begin, mercenary_troops_end),
        (party_set_slot, "$current_town", slot_center_mercenary_troop_type, ":troop_no"),
        (store_random_in_range, ":amount", 3, 8),
        (try_begin),
          (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
          (store_character_level, ":level", "trp_player"), #increase limits a little bit as the game progresses.
          (store_add, ":level_factor", 80, ":level"),
          (val_mul, ":amount", ":level_factor"),
          (val_div, ":amount", 80),
        (try_end),
        (party_set_slot, "$current_town", slot_center_mercenary_troop_amount, ":amount"),
      ]),

      ("go_back",
      [(neg|party_slot_eq,"$current_town",slot_party_type, spt_village),],
      "Go Back.",
      [
        (jump_to_menu,"mnu_town"),
      ]),

      ("continue",
      [(party_slot_eq,"$current_town",slot_party_type, spt_village),],
      "Continue.",
      [
        (jump_to_menu,"mnu_village"),
      ]),
    ]),
    
  (
    "town_cheats_2",0,
    "Select an option to interact with the center itself. Prosperity is {reg1}, Relation is {reg2}, there are {reg3} parties in town.",
    "none",[
        (call_script, "script_set_town_picture"),
        (party_get_slot, reg1, "$current_town", slot_town_prosperity),
        (party_get_slot, reg2, "$current_town", slot_center_player_relation),
        
        (assign, ":count", 0),
        (try_for_parties, ":party_no"),
          (party_is_active, ":party_no"),
          (party_is_in_town, ":party_no", "$current_town"),
          (val_add, ":count", 1),
        (try_end),
        (assign, reg3, ":count"),
      ],
      [
          ("page",
          [],
          "Previous Page.",
          [
            (jump_to_menu, "mnu_town_cheats"),
          ]),

          ("toggle_state",
          [(party_slot_eq, "$current_town", slot_party_type, spt_village),
           (party_get_slot, reg1, "$current_town", slot_village_state),],
          "{reg1?Restore:Raze} this village.",
          [
            (try_begin),
              (party_slot_eq, "$current_town", slot_village_state, svs_normal),
              (call_script, "script_village_set_state", "$current_town", svs_looted),
            (else_try),
              (call_script, "script_village_set_state", "$current_town", svs_normal),
            (try_end),
          ]),

          ("village_manage",
          [], "Manage this center.",
          [
           (assign, "$g_next_menu", "mnu_town_cheats_2"),
           (jump_to_menu, "mnu_center_manage"),
          ]),
          ("increase_rel",
          [],
          "Increase Relation.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_player_relation_with_center", "$current_town", 1),
            (else_try),
              (call_script, "script_change_player_relation_with_center", "$current_town", 5),
            (try_end),
          ]),

          ("decrease_rel",
          [],
          "Decrease Relation.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_player_relation_with_center", "$current_town", -1),
            (else_try),
              (call_script, "script_change_player_relation_with_center", "$current_town", -5),
            (try_end),
          ]),

          ("increase_prosp",
          [],
          "Increase Prosperity.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_center_prosperity", "$current_town", 1),
            (else_try),
              (call_script, "script_change_center_prosperity", "$current_town", 5),
            (try_end),
          ]),

          ("decrease_prosp",
          [],
          "Decrease Prosperity.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_center_prosperity", "$current_town", -1),
            (else_try),
              (call_script, "script_change_center_prosperity", "$current_town", -5),
            (try_end),
          ]),

          ("castle_cheat_interior",
          [(neg|party_slot_eq, "$current_town", slot_party_type, spt_village)],
          "{!}Interior.",
          [
            (set_jump_mission,"mt_ai_training"),
            (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
            (jump_to_scene,":castle_scene"),
            (change_screen_mission),
          ]),

          ("castle_cheat_town_exterior",
          [],
          "{!}Exterior.",
          [
            # (try_begin),
              # (party_slot_eq, "$current_town",slot_party_type, spt_castle),
              # (party_get_slot, ":scene", "$current_town", slot_castle_exterior),
            # (else_try),
              # (party_get_slot, ":scene", "$current_town", slot_town_center),
            # (try_end),
            (party_get_slot, ":scene", "$current_town", slot_town_center),
            (set_jump_mission,"mt_ai_training"),
            (jump_to_scene,":scene"),
            (change_screen_mission),
          ]),

          ("castle_cheat_dungeon",
          [(neg|party_slot_eq, "$current_town", slot_party_type, spt_village)],
          "{!}Prison.",
          [
            (set_jump_mission,"mt_ai_training"),
            (party_get_slot, ":castle_scene", "$current_town", slot_town_prison),
            (jump_to_scene,":castle_scene"),
            (change_screen_mission),
          ]),

          ("castle_cheat_town_walls",
          [
            (party_slot_eq,"$current_town",slot_party_type, spt_town),
          ],
          "{!}Town Walls.",
          [
            (party_get_slot, ":scene", "$current_town", slot_town_walls),
            (set_jump_mission,"mt_ai_training"),
            (jump_to_scene,":scene"),
            (change_screen_mission),
          ]),

          ("cheat_town_start_siege",
          [ (neg|party_slot_eq, "$current_town", slot_party_type, spt_village),
            (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
            (lt, "$g_encountered_party_2", 1),
            # (call_script, "script_party_count_fit_for_battle","p_main_party"),
            # (gt, reg(0), 1),
            # (try_begin),
              # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
              # (assign, reg6, 1),
            # (else_try),
              # (assign, reg6, 0),
            # (try_end),
          ],
          "Besiege the center...",
          [
            (assign,"$g_player_besiege_town","$g_encountered_party"),
            (jump_to_menu, "mnu_castle_besiege"),
          ]),

          ("center_reports",
          [],
          "Show reports.",
          [
            (jump_to_menu,"mnu_center_reports"),
          ]),

          ("sail_from_port",
          [
            (party_slot_eq,"$current_town",slot_party_type, spt_town),
            (party_get_position, pos1, "$current_town"),
            (map_get_water_position_around_position, pos2, pos1, 6),
            (get_distance_between_positions, ":dist", pos1, pos2),
            (lt, ":dist", 6),
            # (party_set_position, "p_main_party", pos2),
            (ge, "$cheat_mode", 1),
            #(party_slot_eq,"$current_town",slot_town_near_shore, 1),
          ],
          "{!}Sail from port.",
          [
            (assign, "$g_player_icon_state", pis_ship),
            (party_set_flags, "p_main_party", pf_is_ship, 1),
            # (party_get_position, pos1, "p_main_party"),
            # (map_get_water_position_around_position, pos2, pos1, 6),
            (party_set_position, "p_main_party", pos2),
            (assign, "$g_main_ship_party", -1),
            (change_screen_return),
          ]),
          
          
          ("go_back",
          [(neg|party_slot_eq,"$current_town",slot_party_type, spt_village),],
          "Go Back.",
          [
            (jump_to_menu,"mnu_town"),
          ]),

          ("continue",
          [(party_slot_eq,"$current_town",slot_party_type, spt_village),],
          "Continue.",
          [
            (jump_to_menu,"mnu_village"),
          ]),
      ]
    ),
  
  #rename_court to set a capital
  (
    "rename_court",0,
    "{!}This menu jumps to the rename presentation",
    "none",
    [
    # (call_script, "script_change_player_right_to_rule", 1), #handled in dialogues
    (try_begin),
      (store_and, ":name_set", "$players_kingdom_name_set", rename_center),
      (gt, ":name_set", 0),
      (change_screen_return),
    (else_try),
      (assign, "$g_presentation_state", rename_center),
      (start_presentation, "prsnt_name_kingdom"),
      (call_script, "script_add_log_entry", logent_player_renamed_capital, "trp_player", "$g_player_court", -1, -1),
    (try_end),
    ],
    []),

  ( #export/import from prsnt_companion_overview
    "export_import", mnf_enable_hot_keys,
    "Press C to access {s1}'s character screen and then the statistics button on the bottom left.",
    "none",
    [
    (set_background_mesh, "mesh_pic_mb_warrior_1"),
    # # (set_player_troop, "trp_player"),
    # (change_screen_view_character),
    # # (change_screen_return),
    # (assign, "$talk_context", tc_town_talk),
    # (start_map_conversation, "$g_player_troop"),
    (set_player_troop, "$g_player_troop"),
    (str_store_troop_name_plural, s1, "$g_player_troop"),
    ],
    [
      ("rename",
      [],
      "I never liked the name {s1}...",
      [
        (assign, "$g_presentation_state", rename_companion),
        (start_presentation, "prsnt_name_kingdom"),
      ]),
      
      ("display_slots",
      [(ge, "$cheat_mode", 1)], "Show me all your secrets...",
      [ 
        (assign, "$g_talk_troop", "$g_player_troop"),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      ("continue",
      [],
      "Continue...",
      [ 
        (set_player_troop, "trp_player"),
        (jump_to_menu, "$g_next_menu"),
      ]),
    ]
  ),
  
  ( #helper menu to show all slots
    "display_party_slots", menu_text_color(0xFF990000),
    "{s1}",
    "none",
    [
    (set_background_mesh, "mesh_pic_messenger"),
    (str_store_party_name, s1, "$g_encountered_party"),
    (assign, reg1, "$g_encountered_party"),
    (assign, "$pout_party", -1),
    (try_for_parties, ":party_no"),
      # (assign, "$pout_party", ":party_no"),
      (party_is_active, ":party_no"),
      (gt, ":party_no", "$pout_party"),
      (assign, "$pout_party", ":party_no"),
    (try_end),
    (assign, reg2, "$pout_party"),
    (str_store_string, s1, "@{reg1}/{reg2}: {s1}"),
    #There's probably too many slots (and conflicting ones) to actually output the slot names to string
    (try_for_range, reg1, 0, 1000), #slot_town_trade_good_productions_begin
      (party_get_slot, reg0, "$g_encountered_party", reg1),
      (neq, reg0, 0), #if there's a value in here
      (str_store_string, s1, "@{s1}^{reg1}: {reg0}"),
    (try_end),
    
    # Process the prev and next parties
    # (assign, "$diplomacy_var",  "$g_encountered_party"),
    # (assign, "$diplomacy_var2", "$g_encountered_party"),
    # (try_for_parties, ":party_no"),
      # (party_is_active, ":party_no"),
      # (eq, "$diplomacy_var2", "$g_encountered_party"),
      # (try_begin), #find last party before current one
        # (lt, ":party_no", "$g_encountered_party"),
        # (assign, "$diplomacy_var", ":party_no"),
      # (else_try), #find first party after current one
        # (gt, ":party_no", "$g_encountered_party"),
        # (assign, "$diplomacy_var2", ":party_no"),
      # (try_end),
    # (try_end),
    (store_sub, "$diplomacy_var",  "$g_encountered_party", 1),
    (store_add, "$diplomacy_var2", "$g_encountered_party", 1),
    (try_begin), #find first
      (neg|party_is_active, "$diplomacy_var"),
      (assign, "$diplomacy_var", 0),
      (assign, ":end", "$g_encountered_party"),
      (try_for_range_backwards, ":party_no", 0, ":end"),
        (party_is_active, ":party_no"),
        (lt, ":party_no", "$g_encountered_party"),
        (gt, ":party_no", "$diplomacy_var"),
        (assign, "$diplomacy_var", ":party_no"),
        (assign, ":end", 0),
      (try_end),
    (try_end),
    # (val_max, "$diplomacy_var", "p_main_party"), #lock as first party
    
    (try_begin), #look for next
      (neg|party_is_active, "$diplomacy_var2"),
      (assign, "$diplomacy_var2", "$pout_party"), #this was previous checked as highest party
      (assign, ":end", "$pout_party"),
      (try_for_range, ":party_no", "$g_encountered_party", ":end"),
        (party_is_active, ":party_no"),
        (gt, ":party_no", "$g_encountered_party"),
        (le, ":party_no", "$diplomacy_var2"),
        (assign, "$diplomacy_var2", ":party_no"),
        (assign, ":end", "$g_encountered_party"),
      (try_end),
    (try_end),
    
    ],
    [
    
      ("notes",
      [(is_between, "$g_encountered_party", centers_begin, centers_end),],
      "View Notes.",
      [
        (change_screen_notes, 3, "$g_encountered_party"),
      ]),
      ("previous",
      [
        (ge, "$diplomacy_var", "p_main_party"),
        (lt, "$diplomacy_var", "$g_encountered_party"),
        (party_is_active, "$diplomacy_var"),
        (str_store_party_name, s2, "$diplomacy_var"),
      ],
      "Previous Party ({s2}).",
      [
        # (jump_to_menu, "mnu_party_cheat"),
        (assign, "$g_encountered_party", "$diplomacy_var"),
      ]),
      
      ("next",
      [
        (le, "$diplomacy_var2", "$pout_party"),
        (gt, "$diplomacy_var2", "$g_encountered_party"),
        (party_is_active, "$diplomacy_var2"),
        (str_store_party_name, s2, "$diplomacy_var2"),
      ],
      "Next Party ({s2}).",
      [
        (assign, "$g_encountered_party", "$diplomacy_var2"),
      ]),
      
      
      ("change",
      [],
      "Modify slots.",
      [
        (assign, "$g_presentation_state", 0), #start off at first slot
        (assign, "$g_presentation_input", rename_center),
        (start_presentation, "prsnt_modify_slots"),
      ]),
    
      ("continue",
      [],
      "Continue.",
      [
        # (jump_to_menu, "mnu_party_cheat"),
        (assign, "$new_encounter", 2),
        (set_encountered_party, "$g_encountered_party"),
        (call_script, "script_game_event_party_encounter", "$g_encountered_party", -1),
        # (change_screen_map),
        # (start_encounter, "$g_encountered_party"),
      ]),
    ]
  ),
  ( #exchange cheat from cmenu_encounter
    "party_cheat",0,
    "{!}{s10} is a {reg10?holding:member} of {s11} with relation {reg11}{reg6? (player relation {reg6}):} at ({reg8},{reg9}) {reg7} km away.^\
 It has {reg12}/{reg13} soldiers {reg13?in {reg14} stacks:}{reg15? and {reg15} prisoners in {reg16} stacks:{reg17? and {reg17} attached parties:}.^\
 AI Behaviour is {s13}{reg18? (currently {s14}):}, Object is {s15}{reg19? (currently {s16}):} at ({reg20},{reg21})",
    "none",
    [
    (assign, "$new_encounter", 0), #this undoes the cheat toggle global immediately
    (set_fixed_point_multiplier, 1000),
    #basic world info first line
    (str_store_party_name, s10, "$g_encountered_party"),
    (str_store_faction_name, s11, "$g_encountered_party_faction"),
    (try_begin),
      (this_or_next|is_between, "$g_encountered_party", centers_begin, centers_end),
      (is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
      (assign, reg10, 1),
      (party_get_slot, reg6, "$g_encountered_party", slot_center_player_relation),
    (else_try),
      (assign, reg10, 0),
      (try_begin),
        (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
        (troop_is_hero, ":leader_troop"),
        (call_script, "script_troop_get_relation_with_troop", ":leader_troop", "trp_player"),
        (assign, reg6, reg0),
      (try_end),
    (try_end),
    (party_get_position, pos1, "$g_encountered_party"),
    (position_get_x, reg8, pos1),
    (position_get_y, reg9, pos1),
    (assign, reg11, "$g_encountered_party_relation"),
    (store_distance_to_party_from_party, reg7, "$g_encountered_party", "p_main_party"),
    
    #party composition second line
    (call_script, "script_party_count_fit_for_battle", "$g_encountered_party"),
    (assign, reg12, reg0),
    (party_get_num_companions, reg13, "$g_encountered_party"),
    (party_get_num_companion_stacks, reg14, "$g_encountered_party"),
    (party_get_num_prisoners, reg15, "$g_encountered_party"),
    (party_get_num_prisoner_stacks, reg16, "$g_encountered_party"),
    (party_get_num_attached_parties, reg17, "$g_encountered_party"),
    
    #AI info third line
    (get_party_ai_behavior, ":behaviour", "$g_encountered_party"),
    (val_add, ":behaviour", "str_ai_bhvr_hold"),
    (str_store_string, s13, ":behaviour"),
    (get_party_ai_current_behavior, ":cur_behaviour", "$g_encountered_party"),
    (val_add, ":cur_behaviour", "str_ai_bhvr_hold"),
    (try_begin),
      (neq, ":cur_behaviour", ":behaviour"),
      (str_store_string, s14, ":cur_behaviour"),
      (assign, reg18, 1),
    (else_try),
      (str_clear, s14),
      (assign, reg18, 0),
    (try_end),
    
    (get_party_ai_object, ":object", "$g_encountered_party"),
    (try_begin),
      (this_or_next|le, ":object", 0),
      (neg|party_is_active, ":object"),
      (str_store_string, s15, "str_dplmc_none"),
    (else_try),
      (str_store_party_name, s15, ":object"),
    (try_end),
    (get_party_ai_current_object, ":cur_object", "$g_encountered_party"),
    (assign, reg19, 1),
    (try_begin),
      (eq, ":cur_object", ":object"),
      (assign, reg19, 0), #disable display
    (else_try),
      (this_or_next|le, ":cur_object", 0),
      (neg|party_is_active, ":cur_object"),
      (str_store_string, s16, "str_dplmc_none"),
    (else_try),
      (str_store_party_name, s16, ":cur_object"),
    (try_end),
    
    (party_get_ai_target_position, pos2, "$g_encountered_party"),
    (position_get_x, reg20, pos2),
    (position_get_y, reg21, pos2),

    #grab the background mesh stuff
    (try_begin),
      (is_between, "$g_encountered_party", centers_begin, centers_end),
      (assign, "$current_town", "$g_encountered_party"),
      (call_script, "script_set_town_picture"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_looters"),
      (set_background_mesh, "mesh_pic_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
      (set_background_mesh, "mesh_pic_mountain_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
      (set_background_mesh, "mesh_pic_steppe_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_taiga_bandits"),
      (set_background_mesh, "mesh_pic_steppe_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_sea_raiders"),
      (set_background_mesh, "mesh_pic_sea_raiders"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_forest_bandits"),
      (set_background_mesh, "mesh_pic_forest_bandits"),
    (else_try),
      (this_or_next|eq, "$g_encountered_party_template", "pt_deserters"),
      (eq, "$g_encountered_party_template", "pt_routed_warriors"),
      (set_background_mesh, "mesh_pic_deserters"),
    #SB : dplmc party templates
    (else_try),
      (eq, "$g_encountered_party_template", "pt_center_reinforcements"),
      (set_background_mesh, "mesh_pic_recruits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
      (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
      (ge, ":leader_troop", 1),
      (troop_get_slot, ":leader_troop_faction", ":leader_troop", slot_troop_original_faction),
      (try_begin),
        (eq, ":leader_troop_faction", fac_kingdom_1),
        (set_background_mesh, "mesh_pic_swad"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_2),
        (set_background_mesh, "mesh_pic_vaegir"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_3),
        (set_background_mesh, "mesh_pic_khergit"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_4),
        (set_background_mesh, "mesh_pic_nord"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_5),
        (set_background_mesh, "mesh_pic_rhodock"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_6),
        (set_background_mesh, "mesh_pic_sarranid_encounter"),
      (try_end),
    (try_end),
    ],
    [
    
      ("talk",
      [],
      "Encounter the party (Shift to goto).",
      [
        (try_begin),
          (this_or_next|key_is_down, key_left_shift),
          (key_is_down, key_right_shift),
          (party_get_position, pos1, "$g_encountered_party"),
          (party_set_position, "p_main_party", pos1),
          (change_screen_map),
        (else_try),
          (call_script, "script_game_event_party_encounter", "$g_encountered_party", -1),
        (try_end),
      ]),
      
      ("slots",
      [],
      "Dump all slot values.",
      [ #g_encountered_party is the input
        (jump_to_menu, "mnu_display_party_slots"),
      ]),

      
      ("reinf",
      [],
      "Reinforce party.",
      [
      
      (try_begin),
        (is_between, "$g_encountered_party", villages_begin, villages_end),
        # (party_add_template, "$g_encountered_party", "pt_village_defenders"),
        (call_script, "script_refresh_village_defenders", "$g_encountered_party"),
      (else_try),
        (is_between, "$g_encountered_party_faction", kingdoms_begin, kingdoms_end),
        (call_script, "script_cf_reinforce_party", "$g_encountered_party"),
      (else_try), #if the above falls through by not reinforcing we grab a random template
        (this_or_next|eq, "$g_encountered_party_faction", "fac_deserters"),
        (is_between, "$g_encountered_party_faction", npc_kingdoms_begin, kingdoms_end),
        (party_stack_get_troop_id, ":troop_id", "$g_encountered_party", 0),
        (store_faction_of_troop, "$g_encountered_party_faction", ":troop_id"),
        (store_random_in_range, ":slot_no", slot_faction_reinforcements_a, slot_faction_num_armies),
        (faction_get_slot, ":party_template", "$g_encountered_party_faction", ":slot_no"),
        (party_add_template, "$g_encountered_party", ":party_template"),
      (else_try),
        # (this_or_next|eq, "$g_encountered_party_faction", "fac_outlaws"),
        # (is_between, "$g_encountered_party_faction", bandit_factions_begin, bandit_factions_end),
        (party_get_template_id, ":party_template", "$g_encountered_party"),
        (party_add_template, "$g_encountered_party", ":party_template"),
      (try_end),
      ]),
      
    ("exp",
      [],
      "Upgrade party.",
      [
        (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
        (party_clear, "p_temp_party"),
         (try_for_range_backwards, ":stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":id", "$g_encountered_party", ":stack"),
            (try_begin),
              (party_stack_get_size, ":size", "$g_encountered_party", ":stack"),
              # (call_script, "script_game_get_upgrade_xp", ":id"),
              # (store_mul, ":xp", reg0, ":size"),
              (try_begin),
                (troop_is_hero, ":id"),
                (store_character_level, ":level", ":id"),
                (assign, ":end", 100),
                (try_begin), #assign block of exp
                  (le, ":level", 10),
                  (assign, ":xp", 100),
                (else_try),
                  (le, ":level", 25),
                  (assign, ":xp", 1000),
                (else_try), #most people stop before level 30
                  (le, ":level", 35),
                  (assign, ":xp", 10000),
                (else_try),
                  (le, ":level", 50),
                  (assign, ":xp", 30000),
                (else_try),
                  (le, ":level", 60),
                  (assign, ":xp", 1000000),
                (else_try), #good luck, level caps at 63
                  (assign, ":xp", 10000000),
                (try_end),
                (try_for_range, ":unused", 0, ":end"),
                  (party_add_xp_to_stack, "$g_encountered_party", ":stack", ":xp"),
                  (add_xp_to_troop, 1, ":id"), #this actually upgrades the level
                  # (add_xp_as_reward, ":xp"),
                  (store_character_level, ":cur_level", ":id"),
                  (lt, ":level", ":cur_level"), #done
                  (assign, ":end", 0),
                (try_end),
              (else_try),
                (troop_get_upgrade_troop, ":upgrade_troop", ":id", 0),
                (gt, ":upgrade_troop", 0),
                (troop_get_upgrade_troop, ":upgrade_2", ":id", 1),
                (try_begin),
                  (gt, ":upgrade_2", 0),
                  (store_random_in_range, ":random_no", 0, 2),
                  (eq, ":random_no", 0),
                  (assign, ":upgrade_troop", ":upgrade_2"),
                (try_end),
                (party_add_members, "p_temp_party", ":upgrade_troop", ":size"),
                (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":stack"),
                (party_wound_members, "p_temp_party", ":upgrade_troop", ":num_wounded"),
                (party_remove_members, "$g_encountered_party", ":id", ":size"),
                # (party_add_xp_to_stack, "$g_encountered_party", ":stack", ":xp"),
              (try_end),
            (try_end),
         (try_end),
         (call_script, "script_party_add_party_companions", "$g_encountered_party", "p_temp_party"),
      ]),

      ("wound",
      [],
      "Wound party.",
      [
        (call_script, "script_party_wound_all_members", "$g_encountered_party"),
      ]),
    ("heal",
      [],
      "Heal party.",
      [
        (call_script, "script_party_heal_all_members_aux", "$g_encountered_party"),
      ]),

     ("rename",[],"Rename party.",
       [(assign, "$g_presentation_state", rename_party),
       # (assign, "$g_encountered_party", "p_main_party"),
       (start_presentation, "prsnt_name_kingdom"),
       ]
       ),
      ("exchange",
      [],
      "Exchange with party.",
      [
        (change_screen_exchange_members,1),
      ]),
      
      ("bandits",
      [(is_between, "$g_encountered_party", centers_begin, centers_end),],
      "Spawn bandits nearby.",
      [
      (set_spawn_radius, 25),
      (try_for_range, ":unused", 0, 10),
        (store_random_in_range, ":party_template", bandit_party_templates_begin, bandit_party_templates_end),
        (spawn_around_party, "$g_encountered_party", ":party_template"),
      (try_end),
      ]),
      
      ("leave",[],"Leave.",
       [
        (assign, "$g_leave_encounter", 1),
        (change_screen_return),
       ]
      ),
    ]
  ),
  

  ( #helper menu to show all troop slots
    "display_troop_slots", menu_text_color(0xFF009900),
    "{s1}^{s2}",
    "none",
    [
    # (set_background_mesh, "mesh_pic_cattle"),
    (assign, reg1, "$g_talk_troop"),
    (str_store_troop_name, s1, "$g_talk_troop"),
    (str_store_troop_name_plural, s2, "$g_talk_troop"),
    (store_troop_faction, ":faction_no", "$g_talk_troop"),
    (str_store_faction_name, s3, ":faction_no"),
    (troop_get_class, ":class", "$g_talk_troop"),
    (str_store_class_name, s4, ":class"),
    (store_character_level, reg2, "$g_talk_troop"),
    (str_store_string, s1, "@{reg1}: {s1}, {s2} classified as level {reg2} {s3} {s4}"),
    (try_begin), #upgrades
      (neg|troop_is_hero, "$g_talk_troop"),
      (try_begin),
        (troop_get_upgrade_troop, ":upgrade_0", "$g_talk_troop", 0),
        (gt, ":upgrade_0", 0),
        (str_store_troop_name_plural, s2, ":upgrade_0"),
        (str_store_string, s1, "@{s1}^becomes {s2}"),
        (troop_get_upgrade_troop, ":upgrade_1", "$g_talk_troop", 1),
        (gt, ":upgrade_1", 0),
        (str_store_troop_name_plural, s2, ":upgrade_1"),
        (str_store_string, s1, "@{s1} and {s2}"),
      (try_end),
      
      (call_script, "script_game_get_upgrade_xp", "$g_talk_troop"),
      (assign, reg10, reg0),
      (call_script, "script_game_get_upgrade_cost", "$g_talk_troop"),
      (assign, reg11, reg0),
      (str_store_string, s1, "@{s1}^costs {reg11} to upgrade with {reg10} xp"),
      
      (call_script, "script_game_get_troop_wage", "$g_talk_troop", -1),
      (assign, reg12, reg0),
      (call_script, "script_game_get_join_cost", "$g_talk_troop"),
      (assign, reg13, reg0),
      
      #this is because this script ties a global to the price
      (assign, ":troop_no", "$g_talk_troop"),
      (assign, "$g_talk_troop", ransom_brokers_begin),
      (call_script, "script_game_get_prisoner_price", ":troop_no"),
      (assign, reg14, reg0),
      (assign, "$g_talk_troop", ":troop_no"),
      
      (str_store_string, s1, "@{s1}^wage of {reg12}, buy costs {reg13} sell costs {reg14}"),
    (else_try),
      (troop_is_hero, "$g_talk_troop"),
      (str_store_string, s2, "@hero"),
      (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s2, 0),
      (str_store_string, s1, "@{s1} is a {s2}"),
      (try_begin),
        (store_troop_gold, ":gold", "$g_talk_troop"),
        (gt, ":gold", 0),
        (assign, reg1, ":gold"),
        (str_store_string, s1, "@{s1} with {reg1} gold"),
      (try_end),
      # (try_begin),
        # (store_partner_quest, ":quest_no"),
        # (ge, ":quest_no", 0),
        # (str_store_quest_name, s2, ":quest_no"),
        # (str_store_string, s1, "@{s1} tasking you with {s2}"),
      # (try_end),
    (try_end),
    
    (str_clear, s2),
    (try_for_range, reg1, 0, 1000),
      (troop_get_slot, reg0, "$g_talk_troop", reg1),
      (neq, reg0, 0), #if there's a value in here
      (str_store_string, s2, "@{s2}^{reg1}: {reg0}"),
    (try_end),
    
    (set_fixed_point_multiplier, 100),
    (init_position, pos0),
    (try_begin),
      (str_is_empty, s2),
      (position_set_x, pos0, 17),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 100),
    (else_try),
      (position_set_x, pos0, 60),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
    (try_end),
    (store_mul, ":troop_no", "$g_talk_troop", 2),
    (set_game_menu_tableau_mesh, "tableau_game_party_window", ":troop_no", pos0),
    ],
    [
    
    #So apparently this one needs to re-jump to the menu
      ("notes",
      [(is_between, "$g_talk_troop", heroes_begin, heroes_end),],
      "View Notes.",
      [
        (change_screen_notes, 1, "$g_talk_troop"),
      ]),

      ("prev_range",
      [
        (gt, "$g_talk_troop", "trp_player"),
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s3, -1),
        (str_store_troop_name, s3, reg0),
      ],
      "Head ({s3}).",
      [
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s0, -1),
        (assign, "$g_talk_troop", reg0),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("next_range",
      [
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s3, 1),
        (str_store_troop_name, s3, reg0),
      ],
      "Tail ({s3}).",
      [
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s0, 1),
        (assign, "$g_talk_troop", reg0),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("prev",
      [
        (gt, "$g_talk_troop", "trp_player"),
        (store_sub, ":troop_no", "$g_talk_troop", 1),
        (str_store_troop_name, s2, ":troop_no"),
      ],
      "Previous Troop ({s2}).",
      [
        (val_sub, "$g_talk_troop", 1),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("next",
      [
        (lt, "$g_talk_troop", "trp_dplmc_recruiter"), #last troop apparently
        (store_add, ":troop_no", "$g_talk_troop", 1),
        (str_store_troop_name, s2, ":troop_no"),
      ],
      "Next Troop ({s2}).",
      [
        (val_add, "$g_talk_troop", 1),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("rename",
      [],
      "Rename.",
      [
        (assign, "$g_player_troop", "$g_talk_troop"),
        (assign, "$g_presentation_state", rename_companion),
        (start_presentation, "prsnt_name_kingdom"),
      ]),
      
      ("change",
      [],
      "Modify slots.",
      [
        (assign, "$g_presentation_state", 0), #start off at first slot
        (assign, "$g_presentation_input", rename_companion),
        (start_presentation, "prsnt_modify_slots"),
      ]),
      
      ("encounter",
      [
        (troop_is_hero, "$g_talk_troop"),
        (party_get_slot, ":party", "$g_talk_troop", slot_troop_leaded_party),
        (party_is_active, ":party"),
      ],
      "Find leaded party.",
      [
        (party_get_slot, "$g_encountered_party", "$g_talk_troop", slot_troop_leaded_party),
        (jump_to_menu, "mnu_party_cheat"),
      ]),
      
      ("inventory",
      [],
      "Modify inventory (Shift for Equip).",
      [
        (try_begin),
          (this_or_next|key_is_down, key_left_shift),
          (key_is_down, key_right_shift),
          (change_screen_equip_other, "$g_talk_troop"),
        (else_try),
          (change_screen_loot, "$g_talk_troop"),
        (try_end),
      ]),
    
       ("gender",[], "Toggle gender.",
         [
           (try_begin),
             (eq, "$g_talk_troop", "trp_player"),
             (store_sub, "$character_gender", tf_female, "$character_gender"),
             (troop_set_type, "trp_player", "$character_gender"),
           (else_try),
             (troop_get_type, ":gender", "$g_talk_troop"),
             (store_sub, ":gender", tf_female, ":gender"),
             (troop_set_type, "$g_talk_troop", ":gender"),
             (try_begin),
               (this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
               (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
               (store_troop_faction, ":faction_no", "$g_talk_troop"),
               (call_script, "script_troop_set_title_according_to_faction", "$g_talk_troop", ":faction_no"),
             (try_end),
           (try_end),
           
         ]
       ),
       
       ("recruit",[
          (this_or_next|troops_can_join, 1),
          (troops_can_join_as_prisoner, 1),
          (try_begin),
            (troop_is_hero, "$g_talk_troop"),
            (store_troop_count_prisoners, ":count", "$g_talk_troop", "p_main_party"),
            (this_or_next|gt, ":count", 0),
            (main_party_has_troop, "$g_talk_troop"),
            (disable_menu_option),
          (try_end),
          ], "Add to party (Shift for prisoner).",
         [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (party_add_prisoners, "p_main_party", "$g_talk_troop", 1),
            (else_try),
              (try_begin),
                (troop_is_hero, "$g_talk_troop"),
                (call_script, "script_recruit_troop_as_companion", "$g_talk_troop"),
              (else_try),
                (party_add_members, "p_main_party", "$g_talk_troop", 1),
              (try_end),
            (try_end),
         ]
       ),
       

      ("continue",
      [],
      "Continue.",
      [
        (change_screen_map),
      ]),
    ]
  ),
  
  (
    "dplmc_choose_disguise", 0,
    "You are about to sneak into {s1}. Make sure you don't bring suspicious items or excess denars that might be confiscated. {s2}",
    "none",
    [
        
        (str_store_party_name, s1, "$current_town"),
        #build text
        (try_begin),
          (eq, "$sneaked_into_town", disguise_none),
          (str_store_string, s2, "@Select a suitable disguise for this occasion."),
          (assign, "$temp", 0),
        (else_try),
          (eq, "$sneaked_into_town", disguise_pilgrim),
          (str_store_string, s2, "@As a poor pilgrim with a stout stick and a few tricks up your sleeve, you will be able to blend in with the crowds but not bring much of value with you."),
          (assign, "$temp", 6),
        (else_try),
          (eq, "$sneaked_into_town", disguise_farmer),
          (str_store_string, s2, "@As a farmer, you will be able to a wrangle livestock and smuggle articles of food through."),
          (assign, "$temp", 15),
        (else_try),
          (eq, "$sneaked_into_town", disguise_hunter),
          (str_store_string, s2, "@As a hunter, provisions and raw goods are expected as well as horseflesh."),
          (assign, "$temp", 12),
        (else_try),
          (eq, "$sneaked_into_town", disguise_guard),
          (str_store_string, s2, "@As a caravan guard, you will be able to bear weapons but bring only a few personal belongings."),
          (assign, "$temp", 6),
        (else_try),
          (eq, "$sneaked_into_town", disguise_merchant),
          (str_store_string, s2, "@As a merchant, you will be able to bring any assortment of goods."),
          (assign, "$temp", 32),
        (else_try),
          (eq, "$sneaked_into_town", disguise_bard),
          (str_store_string, s2, "@As a bard, you will be allowed some personal possessions and your instrument."),
          (assign, "$temp", 9),
        (try_end),
        (set_fixed_point_multiplier, 100),
        (init_position, pos0),
        (try_begin),
          (str_is_empty, s2),
          (position_set_x, pos0, 17),
          (position_set_y, pos0, 30),
          (position_set_z, pos0, 100),
        (else_try),
          (position_set_x, pos0, 60),
          (position_set_y, pos0, 20),
          (position_set_z, pos0, 100),
        (try_end),
        (set_game_menu_tableau_mesh, "tableau_game_inventory_window", "trp_player", pos0),
        (troop_get_slot, "$temp_2", "trp_player", slot_troop_player_disguise_sets),
    ],
    [
      ("continue",
      [(gt, "$temp", 0),
       (assign, reg1, "$temp"),],
      "Choose up to {reg1} items to bring.",
      [
        (change_screen_loot, "trp_random_town_sequence"),
      ]),
      
      ("continue",
      [(neq, "$sneaked_into_town", disguise_none)],
      "Select how much gold to carry.",
      [
        (assign, "$pool_troop", "trp_random_town_sequence"),
        (start_presentation, "prsnt_deposit_withdraw_money"),
      ]),
      
      ("continue",
      [(neq, "$sneaked_into_town", disguise_none)],
      "Attempt to sneak in...",
      [
        (set_show_messages, 0),
        #do inventory placeholder
        (troop_clear_inventory, "trp_temp_troop"),
        (call_script, "script_dplmc_copy_inventory", "trp_player", "trp_temp_troop"),
        (call_script, "script_dplmc_copy_inventory", "trp_random_town_sequence", "trp_player"),
        (call_script, "script_dplmc_copy_inventory", "trp_temp_troop", "trp_random_town_sequence"),
        #do gold swap
        (store_troop_gold, ":cur_amount", "trp_random_town_sequence"),
        (store_troop_gold, ":cur_gold", "trp_player"),
        (troop_remove_gold, "trp_player", ":cur_gold"),
        (troop_remove_gold, "trp_random_town_sequence", ":cur_amount"),
        (troop_add_gold, "trp_player", ":cur_amount"),
        (troop_add_gold, "trp_random_town_sequence", ":cur_gold"),
        (set_show_messages, 1),
        
        #replicate Native chances
        (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
        (party_get_num_companions, ":num_men", "p_main_party"),
        (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
        (val_add, ":num_men", ":num_prisoners"),
        (val_mul, ":num_men", 2),
        (val_div, ":num_men", 3),
        (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
        (store_random_in_range, ":random_chance", 0, 100),
        (try_begin),
          (this_or_next|ge, "$cheat_mode", 1),
          (this_or_next|ge, ":random_chance", ":get_caught_chance"),
          (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
          (assign, "$g_last_defeated_bandits_town", 0),
          # (assign, "$sneaked_into_town", disguise_pilgrim),
          (assign, "$town_entered", 1),
          (jump_to_menu,"mnu_sneak_into_town_suceeded"),
          (assign, "$g_mt_mode", tcm_disguised),
        (else_try),
          (jump_to_menu,"mnu_sneak_into_town_caught"),
        (try_end),
        # (jump_to_menu, "mnu_sneak_into_town_suceeded"),
      ]),
      
      ("disguise_pilgrim",
      [
        (neq, "$sneaked_into_town", disguise_pilgrim),
      ], "Don the robes of a poor pilgrim.",
      [ 
        (assign, "$sneaked_into_town", disguise_pilgrim),
      ]),
      
      #SB : todo, add peasant woman variant
      ("disguise_farmer",
      [(store_and, ":disguise", "$temp_2", disguise_farmer),
       (eq, ":disguise", disguise_farmer),
       (neq, "$sneaked_into_town", disguise_farmer),], 
      "Accept your fate as a downtrodden farmer.",
      [ 
        (assign, "$sneaked_into_town", disguise_farmer),
      ]),
      ("disguise_hunter",
      [(store_and, ":disguise", "$temp_2", disguise_hunter),
       (eq, ":disguise", disguise_hunter),
       (neq, "$sneaked_into_town", disguise_hunter),], 
      "Disguise yourself as a skilled {huntsman/huntress}.",
      [ 
        (assign, "$sneaked_into_town", disguise_hunter),
      ]),
      ("disguise_guard",
      [(store_and, ":disguise", "$temp_2", disguise_guard),
       (eq, ":disguise", disguise_guard),
       (neq, "$sneaked_into_town", disguise_guard),], 
      "Pass yourself off as a caravan guard.",
      [ 
        (assign, "$sneaked_into_town", disguise_guard),
      ]),
      ("disguise_merchant",
      [(store_and, ":disguise", "$temp_2", disguise_merchant),
       (eq, ":disguise", disguise_merchant),
       (neq, "$sneaked_into_town", disguise_merchant),], 
      "Adopt the guise of a trader.",
      [ 
        (assign, "$sneaked_into_town", disguise_merchant),
      ]),
      ("disguise_bard",
      [(store_and, ":disguise", "$temp_2", disguise_bard),
       (eq, ":disguise", disguise_bard),
       (neq, "$sneaked_into_town", disguise_bard),], 
      "Try your luck as a bard.",
      [ 
        (assign, "$sneaked_into_town", disguise_bard),
      ]),

      ("back",
      [],
      "Never mind...",
      [ 
        #put stuff back
        (set_show_messages, 0), #move all gold
        (call_script, "script_move_inventory_and_gold", "trp_random_town_sequence", "trp_player", -1),
        (set_show_messages, 1),
        
        (assign, "$sneaked_into_town", disguise_none),
        (jump_to_menu, "mnu_castle_outside"),
      ]),
    ]
  ),
  

  # (
    # "debug_registers", 0,
    # "{s1}",
    # "none",
    # [
    # (str_clear, s1),
    # ]+
    # [
    # (str_store_string, s1, "@index"+str(x)+":{reg"+str(x)+"}^"),
    # ]
    # for x in range (0, 64),
    # [
      # ("back",
      # [],
      # "Never mind...",
      # [ 
        # (change_screen_return),
      # ]),
    # ]
  # ),
  
  # (
    # "debug_preg", 0,
    # "{s1}",
    # "none",
    # [
    # (str_clear, s1),
    # ]+
    # [
    # (position_get_x, reg1, x),
    # (position_get_y, reg2, x),
    # (position_get_z, reg3, x),
    # (str_store_string, s1, "@{s1}^index"+str(x)+":({reg1},{reg2},{reg3})"),
    
    # ]
    # for x in range (0, pos_belfry_begin),
    # [
      # ("back",
      # [],
      # "Never mind...",
      # [ 
        # (change_screen_return),
      # ]),
    # ]
  # ),
  

  # (
    # "debug_sreg", 0,
    # "{s67}",
    # "none",
    # # [
    # # #need to be careful or string will be built too long
    # # # (str_clear, s67), #use last string
    # # ]+
    # [
    # (str_store_string, s67, "@index"+str(x)+":({reg1},{reg2},{reg3})"),
    
    # ]
    # for x in range (s0, s67),
    # [
      # ("back",
      # [],
      # "Never mind...",
      # [ 
        # (change_screen_return),
      # ]),
    # ]
  # ),
 ]