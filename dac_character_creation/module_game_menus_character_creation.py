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

character_creation_menus = [

####################################################################################################################
# DAC - Starting Quest Menus
####################################################################################################################

# DAC - This menu automatically populates the intro depending on the character's background
("dac_start_quest", 0, 
  "{s10}", "none",[
    (call_script, "script_dac_get_start_quest_intro_strings"),
  ],
  
  [

# DAC - Choices depending on character background appear here.
# Note: Dialogues can be found by searching "Start Quest Dialogues" in module_dialogs.py 
    ("start_merc", [(eq, "$background_type", cb_mercenary)],
        "Discuss your options...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),

    ("start_hunter", [(eq, "$background_type", cb_hunter)],
        "Discuss your options...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),
    ("start_guard", [(eq, "$background_type", cb_soldier)],
        "Discuss your options...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),
    ("start_merchant", [(eq, "$background_type", cb_merchant)],
        "Discuss your options...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),
    ("start_noble", [(eq, "$background_type", cb_noble)],
        "Speak to the angry man...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),
    ("start_generic", [],
      "Skip Intro Quest...",[
      (change_screen_return),
    ]),

  ]
),

# DAC - MERC Stand and Fight Option After Meeting
("dac_stand_fight", 0, 
  "You and your men prepare for the attack...", "none",[],
  
  [
   
    ("merc_stand_fight", [(eq, "$background_type", cb_mercenary)],
        "Lead your men",[
        (call_script, "script_dac_merc_init_stand_and_fight"),
        (change_screen_mission),
      ]),

    ("hunter_stand_fight", [(eq, "$background_type", cb_hunter)],
        "Lead your men",[
        (call_script, "script_dac_hunter_init_stand_and_fight"),
        (change_screen_mission),
      ]),

    ("guard_stand_fight", [(eq, "$background_type", cb_soldier)],
        "Lead your men",[
        (call_script, "script_dac_guard_init_stand_and_fight"),
        (change_screen_mission),
      ]),

    ("guard_stand_fight", [(eq, "$background_type", cb_merchant)],
        "Lead your men",[
        (call_script, "script_dac_merchant_init_stand_and_fight"),
        (change_screen_mission),
      ]),

    ("noble_stand_fight", [(eq, "$background_type", cb_noble)],
        "Duel",[
        (call_script, "script_dac_noble_init_stand_and_fight"),
        (rest_for_hours,3,1000,0),
        (change_screen_mission),
      ]),
  ]
),

# DAC - MERC Start Quest Victory Menu 
# TO DO: Might have to use this for all other options, which means changing up the script to accomodate - Kham

("starting_quest_victory_merc",0, 
  "{s10}", "none",[
    (call_script, "script_dac_start_quest_merc_init_victory_menu", 0),],
  [
    ("end_merc_quest", [],
      "Continue...",[
      (call_script, "script_dac_start_quest_merc_init_victory_menu", 1), # DAC - Consequences = 1 to use the script in the consequences block
      (change_screen_map),
    ]),

  ]
),



####################################################################################################################
# [ Z02 ] - Character Generation
####################################################################################################################
  

  ("start_game_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Select your character's gender.",
    "none",
##diplomacy start+ Reset prejudice preferences
    [
        (assign, "$g_disable_condescending_comments", 0),
    ],
##diplomacy end+
    [
      ("start_male",[],"Male",
       [
         (troop_set_type,"trp_player", 0),
         (assign,"$character_gender", tf_male),
         
        (str_store_troop_face_keys, s57, "trp_male_face_keys", 0),
        (str_store_troop_face_keys, s58, "trp_male_face_keys", 1),
        (troop_set_face_keys, "trp_player", s57, 0),
        (troop_set_face_keys, "trp_player", s58, 1),
        
         (try_begin),
            (eq, "$background_answer_2", 0), # DAC Kham: As Adventurer
            # (jump_to_menu,"mnu_dac_start_character_background"),
            (assign, "$background_type", 1),
            (assign, "$class_type", 1),
            (start_presentation, "prsnt_dac_select_background"), 
         (else_try),
            (eq, "$background_answer_2", 1), #DAC Kham: As Vassal
            #(jump_to_menu,"mnu_start_as_vassal_choose_faction"),
            (start_presentation, "prsnt_faction_selection"),
         (try_end),
        ]
       ),
      ("start_female",[],"Female",
       [
        (troop_set_type, "trp_player", 1),
        (assign, "$character_gender", tf_female),
         
        (str_store_troop_face_keys, s57, "trp_female_face_keys", 0),
        (str_store_troop_face_keys, s58, "trp_female_face_keys", 1),
        (troop_set_face_keys, "trp_player", s57, 0),
        (troop_set_face_keys, "trp_player", s58, 1),
##diplomacy start+
#Jump to the prejudice-level menu instead
#         (jump_to_menu, "mnu_start_character_1"),
         (jump_to_menu, "mnu_dplmc_start_select_prejudice"),
##diplomacy end+
       ]
       ),
	  ("go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_start_game_0"),
       ]),
    ]
  ),

  (
    "auto_return",0,
    "{!}This menu automatically returns to caller.",
    "none",
    [(change_screen_return, 0)],
    [
    ]
  ),


### DAC Character Creation
(
    "dac_start_character_background",mnf_disable_all_keys,
    "Choose Your Background",
    "none",
    [
    (assign, reg11, "$character_gender"), #SB : every string now uses reg11 for daughter/son boy/girl etc
    ],
    [
    ("dac_start_noble",[(neq, "$character_gender", tf_female)],"An impoverished noble.",[
        (assign,"$background_type",cb_noble),
        #(str_store_string,s10,"str_story_parent_noble"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),
    ("dac_start_merchant",[(neq, "$character_gender", tf_female)],"A travelling merchant.",[
        (assign,"$background_type",cb_merchant),
        #(str_store_string,s10,"str_story_parent_merchant"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),
    ("dac_start_soldier",[(neq, "$character_gender", tf_female)],"A veteran soldier.",[
        (assign,"$background_type",cb_soldier),
        #(str_store_string,s10,"str_story_parent_guard"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),
    ("dac_start_hunter",[(neq, "$character_gender", tf_female)],"A hunter.",[
        (assign,"$background_type",cb_hunter),
        #(str_store_string,s10,"str_story_parent_forester"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),
  
    ("dac_start_mercenary",[(neq, "$character_gender", tf_female)],"A rugged mercenary.",[
        (assign,"$background_type",cb_mercenary),
        #(str_store_string,s10,"str_story_parent_priest"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),

# DAC - Female Options

    ("dac_start_noblewoman",[(eq, "$character_gender", tf_female)],"An impoverished noblewoman, dealing with the death of her father during the war.",[
        (assign,"$background_type",cb_noble),
        #(str_store_string,s10,"str_story_parent_noble"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),

    ("dac_start_peasant",[(eq, "$character_gender", tf_female)],"a Peasant, inspired by the tales of Jeanne, La Pucelle d'Orléans.",[
        (assign,"$background_type",cb_peasant),
        #(str_store_string,s10,"str_story_parent_forester"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),

    ("dac_start_craftswoman",[(eq, "$character_gender", tf_female)],"a Craftswoman, supporting the war efforts.",[
        (assign,"$background_type",cb_merchant),
        #(str_store_string,s10,"str_story_parent_merchant"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),

    ("dac_start_healer",[(eq, "$character_gender", tf_female)],"a Healer, tending to the wounded during the war.",[
        (assign,"$background_type",cb_healer),
        #(str_store_string,s10,"str_story_parent_merchant"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),

    #DAC-Kham: Quick Scene Chooser for Dev
    ("choose_scene",[(is_edit_mode_enabled),],"Scene Chooser",
      [(jump_to_menu, "mnu_choose_scenes_0"),]
    ),

    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),

# DAC Kham: KAOS Start as Vassal BEGIN Part 2

  ("start_as_vassal_choose_faction", mnf_disable_all_keys,
    "Select your character's faction.",
    "none",
    [],
    [
      ("fac1",[],"Kingdom of France", [
         (assign, "$background_answer_3", "fac_kingdom_1"),
         (jump_to_menu, "mnu_dac_choose_skill"),
      ]),
      
      ("fac2",[],"Kingdom of England", [
         (assign, "$background_answer_3", "fac_kingdom_2"),
         (jump_to_menu, "mnu_dac_choose_skill"),
      ]),

      ("fac3",[],"Duchy of Burgundy", [
         (assign, "$background_answer_3", "fac_kingdom_3"),
         (jump_to_menu, "mnu_dac_choose_skill"),
      ]),

      ("fac4",[],"Duchy of Brittany", [
         (assign, "$background_answer_3", "fac_kingdom_4"),
         (jump_to_menu, "mnu_dac_choose_skill"),
      ]),

      ("go_back",[],"Go back", [ 
          (try_begin),
            (eq, "$character_gender", tf_female),
            (jump_to_menu,"mnu_dplmc_start_select_prejudice"), 
          (else_try),
            (jump_to_menu, "mnu_start_game_1"),
          (try_end)
      ]),
    ]
  ),

# DAC Kham: KAOS Start as Vassal END Part 2

(
    "dac_choose_skill",mnf_disable_all_keys,
    "Onwards, to France!",
    "none",
    [], #DAC-Kham: We may need to fill up the Description above based on the choice player makes.
        #DAC-Kham: See "choose_skill" to see how it is done on Native
    [
##      
      ("begin_adventuring",[(eq, "$background_answer_2", 0)],"Become an adventurer and ride to your destiny.",[
      
        (set_show_messages, 0),
        
        (try_begin),
            (this_or_next|eq, "$class_type", cc_peasant_farmer),
            (this_or_next|eq, "$class_type", cc_peasant_smith),
            (eq, "$class_type", cc_soldier_sergeant),
            (assign, "$class_type_feature_active", 0),
        (else_try),
            (assign, "$class_type_feature_active", 1),
        (try_end),       
        
        (try_begin),
            (this_or_next|eq, "$class_type", cc_peasant_farmer),
            (eq, "$class_type", cc_peasant_smith),
            (troop_set_slot, "trp_player", slot_troop_player_workday_rest, -1),
            (troop_set_slot, "trp_player", slot_troop_player_workday_hours, -1),
            (troop_set_slot, "trp_player", slot_troop_player_workday_payment, -1),
            (troop_set_slot, "trp_player", slot_troop_player_workday_total, -1),
        (try_end),
        
        (try_begin),
            (eq, "$background_type", cb_mercenary),
            (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
                (faction_set_slot, ":faction_no", slot_faction_last_mercenary_offer_time, 0),
            (try_end),
        (try_end),
        
        (try_begin),
            (eq, "$class_type", cc_mercenary_scottish),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 40),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", -40),
        (try_end),
           
          # (try_begin),
            # (eq, "$character_gender", tf_male),
            # (troop_raise_attribute, "trp_player",ca_strength,1),
            # (troop_raise_attribute, "trp_player",ca_charisma,1),
          # (else_try),
            # (troop_raise_attribute, "trp_player",ca_agility,1),
            # (troop_raise_attribute, "trp_player",ca_intelligence,1),
          # (try_end),

          # (troop_raise_attribute, "trp_player",ca_strength,1),
          # (troop_raise_attribute, "trp_player",ca_agility,1),
          # (troop_raise_attribute, "trp_player",ca_charisma,1),

          # (troop_raise_skill, "trp_player","skl_leadership",1),
          # (troop_raise_skill, "trp_player","skl_riding",1),
      
          # (try_begin),
            # (eq,"$background_type",cb_noble),
            # (call_script, "script_start_as_noble"),
          # (else_try),
            # (eq,"$background_type",cb_merchant),
            # (call_script, "script_start_as_merchant"),
          # (else_try),
            # (eq,"$background_type",cb_soldier),
            # (call_script, "script_start_as_warrior"),
          # (else_try),
            # (eq,"$background_type",cb_hunter),
            # (call_script, "script_start_as_hunter"),
          # (else_try),
           # (eq,"$background_type",cb_mercenary),
           # (call_script, "script_start_as_merc"),
          # (else_try),
           # (eq,"$background_type",cb_healer),
           # (call_script, "script_start_as_healer"),
          # (try_end),

      #SB : pre-allocate disguises
      (try_begin),
        (assign, ":disguise", disguise_pilgrim), #always available
        #farmer, acquired from not picking inappropriate noble/priestly options
        (try_begin),
          (neq, "$background_type", cb_noble),
          (val_add, ":disguise", disguise_farmer),
        (try_end),
        (try_begin),
          (eq, "$background_type", cb_hunter),
          (val_add, ":disguise", disguise_hunter),
        (try_end),
        (try_begin),
          (eq, "$background_type", cb_merchant),
          (val_add, ":disguise", disguise_merchant),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_soldier),
          (eq, "$background_type", cb_mercenary),
          (val_add, ":disguise", disguise_guard),
        (try_end),
        (try_begin),
          (eq, "$background_answer_2", cb_noble),
          (val_add, ":disguise", disguise_bard),
        (try_end),
      (try_end),
      (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, ":disguise"),

      (try_begin),
        (eq, "$background_type", cb_noble),
        (jump_to_menu, "mnu_auto_return"),
#normal_banner_begin
        (start_presentation, "prsnt_banner_selection"),
      (else_try),
        (change_screen_return, 0),
      (try_end),
      
      (set_show_messages, 1),
        ]),

  #DAC Kham: KAOS Start as Ruler / Lord / Vassal BEGIN      

      ("begin_ruling", [(eq, "$background_answer_2", 2),], "Become a ruler during the Hundred Years War",
        [
          (call_script, "script_kaos_start_as_king_or_lord", "$dac_selected_lord"),        
          (change_screen_return, 0),
        ],
      ),

      ("begin_serving", [(eq, "$background_answer_2", 1),], "Become a vassal during the Hundred Years War",
        [
          (call_script, "script_kaos_start_as_vassal", "$background_answer_3"),
          (jump_to_menu, "mnu_auto_return"),
          (start_presentation, "prsnt_banner_selection"),
        ],
      ),

("go_back_dot",[],"Go back.",[        
    (try_begin),
        (eq, "$background_answer_2", 1),
        #(jump_to_menu,"mnu_dac_start_character_background"),
        (start_presentation, "prsnt_faction_selection"),
    (else_try),
        (eq, "$background_answer_2", 2),
        (assign, "$character_info_id", -1),
        (assign, "$background_answer_2", 2), 
        (start_presentation, "prsnt_dac_select_lord_or_king"), 
    (else_try),
        (assign, "$background_type", 1),
        (assign, "$background_class", 1),
        (call_script, "script_dac_clear_player_equipment"),
        (call_script, "script_dac_clear_player_attributes"),
        (start_presentation, "prsnt_dac_select_background"), 
    (try_end),
        ]),
    ]
  ),

# DAC Seek: Added option to shorten lord titles
  ("dac_start_game_lord_name_option", mnf_disable_all_keys,
    "Mod Option^^ In Deeds of Arms and Chivalry the lords and regents carry the titles they would have held in 1429 in their names. If the long titles are inconvenient for you, you have the option to shorten the names of lords and regents or only the lords, otherwise you can keep it as it is, long and uncut. This is a one time irreversible change. For example, John Fastolf Lieutenant-general of Normandy will simply be refered as John Fastolf if you select to remove the titles.",
    "none",
    [],
    [
      ("no",[],"Keep it as it is.", [
        (change_screen_return),
      ]),
      
      ("also_yes_kinda",[],"Remove only the lord titles. (Keep the regent titles)", [
      
        (try_for_range, ":troop_no", lords_begin, lords_end),
            (str_store_troop_name_plural, s7, ":troop_no"),
            (troop_set_name, ":troop_no", s7),
        (try_end),
        
        (change_screen_return),
      ]),
      
      ("yes",[],"Remove all the titles.", [
      
        (try_for_range, ":troop_no", kings_begin, lords_end),
            (str_store_troop_name_plural, s7, ":troop_no"),
            (troop_set_name, ":troop_no", s7),
        (try_end),
        
        (change_screen_return),
      ]),


    ]
  ),
  
### DAC Seek: Hidden Stash Management:
  ("manage_hidden_chest", mnf_disable_all_keys,
    "You discreetely make your way to your hidden stash... ^\
    {s10} out of a maximum of {reg4} items ^\
    You stored {reg5} crowns out of a maximum of {reg6} ^\
    Current Stash Level: {reg7}/10",
    "none",
    [
    (assign, reg3,0),
    (troop_get_inventory_capacity, ":inv_cap", "trp_hidden_chest"),
    (assign, reg4, ":inv_cap"),
    (try_for_range, ":i_slot", 0, ":inv_cap"),
        (troop_get_inventory_slot, ":item_id", "trp_hidden_chest", ":i_slot"),
        (ge, ":item_id", 0),
        (neg|troop_has_item_equipped, "trp_hidden_chest", ":item_id"),
        (val_add, reg3, 1),
    (try_end),
    # reg3 now contains number of items in loot pool
    (try_begin),
        (eq, reg3, 0),
        (str_store_string, s10, "str_dac_chest_no_item"),
    (else_try),
        (eq, reg3, 1),
        (str_store_string, s10, "str_dac_chest_one_item"),
    (else_try),
        (str_store_string, s10, "str_dac_chest_many_items"),
    (try_end),
    
    (store_troop_gold, ":current_gold", "trp_hidden_chest"),
    (assign, reg5, ":current_gold"),
    
    (store_skill_level, ":inventory_management_skill", skl_inventory_management, "trp_hidden_chest"),
    (try_begin),
        (lt, skl_inventory_management, 5),
        (store_mul, ":gold_limit", ":inventory_management_skill", 500),
    (else_try),
        (store_mul, ":gold_limit", ":inventory_management_skill", 1000),
    (try_end),
    (assign, reg6, ":gold_limit"),
    (assign, reg7, ":inventory_management_skill"),
    ],
    [
      ("access_stash_items",[],"Open the Stash", [
        (change_screen_loot, "trp_hidden_chest"),
      ]),
      ("upgrade_stash",[(lt, reg7, 10),
      (store_troop_gold, ":current_gold", "trp_player"),
      (ge, ":current_gold", reg6),      
      ],"Upgrade the Stash: {reg6} Crowns", [
        (troop_remove_gold, "trp_player", reg6),
        (troop_raise_skill, "trp_hidden_chest", skl_inventory_management, 1),
      ]),
      ("deposit_500_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (le, ":current_gold", reg6 - 500),
        (store_troop_gold, ":player_gold", "trp_player"),      
        (ge, ":player_gold", 500),  
      ],
      "Deposit 500 Crowns", [
        (troop_remove_gold, "trp_player", 500),
        (troop_add_gold, "trp_hidden_chest", 500),
      ]),
      ("deposit_200_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (le, ":current_gold", reg6 - 200),
        (store_troop_gold, ":player_gold", "trp_player"),      
        (ge, ":player_gold", 200),  
      ],
      "Deposit 200 Crowns", [
        (troop_remove_gold, "trp_player", 200),
        (troop_add_gold, "trp_hidden_chest", 200),
      ]),
      ("deposit_100_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (le, ":current_gold", reg6 - 100),
        (store_troop_gold, ":player_gold", "trp_player"),      
        (ge, ":player_gold", 100),  
      ],
      "Deposit 100 Crowns", [
        (troop_remove_gold, "trp_player", 100),
        (troop_add_gold, "trp_hidden_chest", 100),
      ]),
      ("withdraw_all_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (gt, ":current_gold", 0),
      ],
      "Withdraw All Crowns", [
        (troop_remove_gold, "trp_hidden_chest", reg5),
        (troop_add_gold, "trp_player", reg5),
      ]),
     ("withdraw_500_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (ge, ":current_gold", 500),
      ],
      "Withdraw 500 Crowns", [
        (troop_remove_gold, "trp_hidden_chest", 500),
        (troop_add_gold, "trp_player", 500),
      ]),
      ("withdraw_200_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (ge, ":current_gold", 200),
      ],
      "Withdraw 200 Crowns", [
        (troop_remove_gold, "trp_hidden_chest", 200),
        (troop_add_gold, "trp_player", 200),
      ]),
      ("withdraw_100_crowns",[
        (store_troop_gold, ":current_gold", "trp_hidden_chest"),
        (ge, ":current_gold", 100),
      ],
      "Withdraw 100 Crowns", [
        (troop_remove_gold, "trp_hidden_chest", 100),
        (troop_add_gold, "trp_player", 100),
      ]),
      ("go_back",[],"Go back", [(jump_to_menu, "mnu_camp_action"),
      ]),
    ]
  ),

### DAC Seek: Work in towns or villages
  (
    "dac_work_town_village",mnf_disable_all_keys,
    "As a {s1} you can expect to find work {s2}.^With your current attributes required by the job [{s3}: {reg1}] you would earn {reg3} per hour. ^\
    {s4}",
    "none",
    [
    (try_begin),
        (eq, "$class_type", cc_peasant_farmer),
        (str_store_string, s1, "str_dac_background_class_farmer"),
        (str_store_string, s2, "@in the fields"),
        (str_store_string, s3, "@STRENGHT"),
        (store_attribute_level, ":attribute", "trp_player", ca_strength),
    (else_try),
        (eq, "$class_type", cc_peasant_smith),
        (str_store_string, s1, "str_dac_background_class_smith"),
        (str_store_string, s2, "@at the smithy"),
        (str_store_string, s3, "@AGILITY"),
        (store_attribute_level, ":attribute", "trp_player", ca_agility),
    (else_try),
        (str_store_string, s1, "@work hand"),
        (str_store_string, s2, "@performing various tasks"),    
        (str_store_string, s3, "@STRENGHT"),
        (store_attribute_level, ":attribute", "trp_player", ca_strength),
    (try_end),
    
    (assign, reg1, ":attribute"),
    (store_attribute_level, ":charisma", "trp_player", ca_charisma),
    (assign, reg2, ":charisma"),
    
    (store_mul, ":payment", ":attribute", 3),
    (val_div, ":payment", 4),
    (assign, reg3, ":payment"),
    (troop_set_slot, "trp_player", slot_troop_player_workday_payment, ":payment"),
    
    (store_skill_level, ":persuasion", skl_persuasion, "trp_player"),
    (store_skill_level, ":trade", skl_trade, "trp_player"),
    
    (try_begin),
        (this_or_next|gt, ":persuasion", 0),
        (gt, ":trade", 0),
        
        (try_begin),
            (ge, ":persuasion", ":trade"),
            (str_store_string, s5, "@PERSUASION"),
            (assign, reg4, ":persuasion"),
            (store_add, ":skill", ":persuasion", 1),
        (else_try),
            (str_store_string, s5, "@TRADE"), 
            (assign, reg4, ":trade"),
            (store_add, ":skill", ":trade", 1),
        (try_end),
        
        (store_mul, ":new_payment", ":skill", 3),
        (val_div, ":new_payment", 2),
        (store_add, ":new_payment", ":payment", ":new_payment"),
        (assign, reg5, ":new_payment"),
        (str_store_string, s4, "@which you negotiate to {reg5} crowns thanks to your [CHARISMA: {reg2}] and [{s5}: {reg4}] skills."),
        (troop_set_slot, "trp_player", slot_troop_player_workday_payment, ":new_payment"),
    (try_end),
    
    
     ],
    [
      ("start_working_full", [], "Start a full day of work (10 Hours).",
       [
        (assign, "$class_type_feature_active", 1),
        (troop_set_slot, "trp_player", slot_troop_player_workday_hours, 10),
        (troop_set_slot, "trp_player", slot_troop_player_workday_total, 10),
        (rest_for_hours, 1000, 5, 0), #rest while not attackable
        (assign,"$auto_enter_town","$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (change_screen_return),
        ]),
      ("start_working_half", [], "Start a half day of work (5 Hours).",
       [
        (assign, "$class_type_feature_active", 1),
        (troop_set_slot, "trp_player", slot_troop_player_workday_hours, 5),
        (troop_set_slot, "trp_player", slot_troop_player_workday_total, 5),
        (rest_for_hours, 1000, 5, 0), #rest while not attackable
        (assign,"$auto_enter_town","$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (change_screen_return),
        ]),
      ("work_later", [], "Put it off until later.",
       [(try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
        ]),
    ]
  ),
  
  
  (
    "dac_work_town_village_complete",mnf_disable_all_keys,
    "You've made {reg3} crowns from you work day. ^You will need proper rest for a few hours before you can work again, either at your camp, or somewhere indoors.",
    ##diplomacy end+
    "none",
    [
        (troop_get_slot, ":payment", "trp_player", slot_troop_player_workday_payment),
        (troop_get_slot, ":work_hours", "trp_player", slot_troop_player_workday_total),
        (store_mul, reg3, ":work_hours", ":payment"),
        
        (store_div, ":rest", ":work_hours", 2),
        (troop_set_slot, "trp_player", slot_troop_player_workday_rest, ":rest"),
        
     ],
    [
      ("continue", [], "Continue...",
       [(change_screen_return),
        ]),
    ]
  ),
]