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
         (try_begin),
            (eq, "$background_answer_2", 0), # DAC Kham: As Adventurer
            (jump_to_menu,"mnu_dac_start_character_background"),
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
    ("choose_scene",[],"Scene Chooser",
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
            (eq, "$character_gender", tf_male),
            (troop_raise_attribute, "trp_player",ca_strength,1),
            (troop_raise_attribute, "trp_player",ca_charisma,1),
          (else_try),
            (troop_raise_attribute, "trp_player",ca_agility,1),
            (troop_raise_attribute, "trp_player",ca_intelligence,1),
          (try_end),

          (troop_raise_attribute, "trp_player",ca_strength,1),
          (troop_raise_attribute, "trp_player",ca_agility,1),
          (troop_raise_attribute, "trp_player",ca_charisma,1),

          (troop_raise_skill, "trp_player","skl_leadership",1),
          (troop_raise_skill, "trp_player","skl_riding",1),
      
          (try_begin),
            (eq,"$background_type",cb_noble),
            (call_script, "script_start_as_noble"),
          (else_try),
            (eq,"$background_type",cb_merchant),
            (call_script, "script_start_as_merchant"),
          (else_try),
            (eq,"$background_type",cb_soldier),
            (call_script, "script_start_as_warrior"),
          (else_try),
            (eq,"$background_type",cb_hunter),
            (call_script, "script_start_as_hunter"),
          (else_try),
           (eq,"$background_type",cb_mercenary),
           (call_script, "script_start_as_merc"),
          (else_try),
           (eq,"$background_type",cb_healer),
           (call_script, "script_start_as_healer"),
          (try_end),

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
          (jump_to_menu, "mnu_dac_start_character_background"),
        (try_end),
        ]),
    ]
  ),

# DAC Seek: Added option to shorten lord titles
  ("dac_start_game_lord_name_option", mnf_disable_all_keys,
    "Mod Option^^ In Deeds of Arms and Chivalry the lords and regents carry the titles they would have held in 1429 in their names. If the long titles are inconvenient for you, you have the option to shorten the names of lords and regents or only the lords, otherwise you can keep it as it is, long and uncut. This is a one time irreversible change. For example, John Fastolf Lieutenant-general of Normandy will simply be refered as John Fastolf if you select to shorten the titles.",
    "none",
    [],
    [
      ("no",[],"Keep it as it is.", [
        (change_screen_return),
      ]),
      
      ("also_yes_kinda",[],"Shorten only the lord titles. (Keep the regent titles)", [
      
        (try_for_range, ":troop_no", lords_begin, lords_end),
            (str_store_troop_name_plural, s7, ":troop_no"),
            (troop_set_name, ":troop_no", s7),
        (try_end),
        
        (change_screen_return),
      ]),
      
      ("yes",[],"Shorten all the titles.", [
      
        (try_for_range, ":troop_no", kings_begin, lords_end),
            (str_store_troop_name_plural, s7, ":troop_no"),
            (troop_set_name, ":troop_no", s7),
        (try_end),
        
        (change_screen_return),
      ]),


    ]
  ),

]