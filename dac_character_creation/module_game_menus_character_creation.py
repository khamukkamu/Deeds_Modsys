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
    ("start_merc", [(eq, "$background_type", cb_merc)],
        "Discuss your options...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),

    ("start_hunter", [(eq, "$background_type", cb_forester)],
        "Discuss your options...",[
        (call_script, "script_dac_starting_quest_meeting_scene"),
      ]),
    ("start_guard", [(eq, "$background_type", cb_guard)],
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
   
    ("merc_stand_fight", [(eq, "$background_type", cb_merc)],
        "Lead your men",[
        (call_script, "script_dac_merc_init_stand_and_fight"),
        (change_screen_mission),
      ]),

    ("hunter_stand_fight", [(eq, "$background_type", cb_forester)],
        "Lead your men",[
        (call_script, "script_dac_hunter_init_stand_and_fight"),
        (change_screen_mission),
      ]),

    ("guard_stand_fight", [(eq, "$background_type", cb_guard)],
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
    "start_character_1",mnf_disable_all_keys,
    "You were born years ago, in a land far away. Your father was...",
    "none",
    [
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    (assign, reg11, "$character_gender"), #SB : every string now uses reg11 for daughter/son boy/girl etc
    ],
    [
    ("start_noble",[],"An impoverished noble.",[
        (assign,"$background_type",cb_noble),
        (str_store_string,s10,"str_story_parent_noble"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_merchant",[],"A travelling merchant.",[
        (assign,"$background_type",cb_merchant),
        (str_store_string,s10,"str_story_parent_merchant"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_guard",[],"A veteran warrior.",[
        (assign,"$background_type",cb_guard),
        (str_store_string,s10,"str_story_parent_guard"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_forester",[],"A hunter.",[
        (assign,"$background_type",cb_forester),
        (str_store_string,s10,"str_story_parent_forester"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_nomad",[],"A steppe nomad.",[
        (assign,"$background_type",cb_nomad),
        (str_store_string,s10,"str_story_parent_nomad"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_thief",[],"A thief.",[
        (assign,"$background_type",cb_thief),
        (str_store_string,s10,"str_story_parent_thief"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    #SB: could say "Your father was... The Church" instead of "A Priest/s"
    ("start_priest",[],"A fleeting memory.",[
        (assign,"$background_type",cb_priest),
        (str_store_string,s10,"str_story_parent_priest"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),
  (
    "start_character_2",0,
    "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
    "none",
    [],
    [
      ("page",[
          ],"A page at a nobleman's court.",[
            (assign,"$background_answer_2", cb2_page),
            (str_store_string,s11,"str_story_childhood_page"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("apprentice",[
          ],"A craftsman's apprentice.",[
            (assign,"$background_answer_2", cb2_apprentice),
            (str_store_string,s11,"str_story_childhood_apprentice"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("stockboy",[
          ],"A shop assistant.",[
            (assign,"$background_answer_2",cb2_merchants_helper),
            (str_store_string,s11,"str_story_childhood_stockboy"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("urchin",[
          ],"A street urchin.",[
            (assign,"$background_answer_2",cb2_urchin),
            (str_store_string,s11,"str_story_childhood_urchin"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("nomad",[
          ],"A steppe child.",[
            (assign,"$background_answer_2",cb2_steppe_child),
            (str_store_string,s11,"str_story_childhood_nomad"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),

        #SB : standardize strings as prompted
     ("mummer",[],"A mummer.",[
            (assign,"$background_answer_2",dplmc_cb2_mummer),
            (str_store_string,s11,"str_story_childhood_mummer"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
     ("courtier",[],"A courtier.",[
            (assign,"$background_answer_2",dplmc_cb2_courtier),
            (str_store_string,s11,"str_story_childhood_courtier"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
        #SB : conditional of parents being noble
     ("noble",[ #"Noble in Training" is vaguely similar to role of courtier/page, 
        #we pretend this means you were not fostered but rather educated in-situ
        (eq, "$background_type", cb_noble),
        ],"An unexpected heir.",[
            (assign,"$background_answer_2",dplmc_cb2_noble),
            (str_store_string,s11,"str_story_childhood_noble"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
     ("acolyte",[],"A cleric acolyte.",[
            (assign,"$background_answer_2",dplmc_cb2_acolyte),
            (str_store_string,s11,"str_story_childhood_acolyte"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("go_back",[],"Go back.",
     [(jump_to_menu,"mnu_start_character_1"),
    ]),
    ]
  ),
  (
    "start_character_3",mnf_disable_all_keys,
    "As a {reg11?girl:boy} growing out of childhood, {s11}^^ Then, as a young adult, life changed as it always does. You became...",
    "none",
    [],
    [
    #SB : maybe restrict these two by gender like squire?
     ("bravo",[],"A travelling bravo.",[
       (assign,"$background_answer_3",dplmc_cb3_bravo),
     (str_store_string,s12,"str_story_job_bravo"),
	(jump_to_menu,"mnu_start_character_4"),
       ]),
     ("merc",[],"A sellsword in foreign lands.",[
       (assign,"$background_answer_3",dplmc_cb3_merc),
     (str_store_string,s12,"str_story_job_merc"),
	(jump_to_menu,"mnu_start_character_4"),
       ]),

      ("squire",[(eq,"$character_gender",tf_male)],"A squire.",[
        (assign,"$background_answer_3",cb3_squire),
      (str_store_string,s12,"str_story_job_squire"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("lady",[(eq,"$character_gender",tf_female)],"A lady-in-waiting.",[
        (assign,"$background_answer_3",cb3_lady_in_waiting),
      (str_store_string,s12,"str_story_job_lady"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("troubadour",[],"A troubadour.",[
        (assign,"$background_answer_3",cb3_troubadour),
      (str_store_string,s12,"str_story_job_troubadour"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("student",[],"A university student.",[
        (assign,"$background_answer_3",cb3_student),
      (str_store_string,s12,"str_story_job_student"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("peddler",[],"A goods peddler.",[
        (assign,"$background_answer_3",cb3_peddler),
      (str_store_string,s12,"str_story_job_peddler"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("craftsman",[],"A smith.",[
        (assign,"$background_answer_3", cb3_craftsman),
      (str_store_string,s12,"str_story_job_craftsman"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("poacher",[],"A game poacher.",[
        (assign,"$background_answer_3", cb3_poacher),
      (str_store_string,s12,"str_story_job_poacher"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
     ("preacher",[],"An itinerant preacher.",[
       (assign,"$background_answer_3", dplmc_cb3_preacher),
     (str_store_string,s12,"str_story_job_preacher"),
	(jump_to_menu,"mnu_start_character_4"),
       ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_2"),
        ]
       ),
    ]
  ),

  (
    "start_character_4",mnf_disable_all_keys,
    "Though the distinction felt sudden to you, somewhere along the way you had become a {reg11?woman:man}, and the whole world seemed to change around you.\
 {s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
    #Finally, what made you decide to strike out on your own as an adventurer?",
    "none",
    [],
    [
      ("revenge",[],"Personal revenge.",[
        (assign,"$background_answer_4", cb4_revenge),
        (str_store_string,s13,"str_story_reason_revenge"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("death",[],"The loss of a loved one.",[
        (assign,"$background_answer_4",cb4_loss),
        (str_store_string,s13,"str_story_reason_death"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("wanderlust",[],"Wanderlust.",[
        (assign,"$background_answer_4",cb4_wanderlust),
        (str_store_string,s13,"str_story_reason_wanderlust"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
        #SB : condition of at least one priestly background
     ("fervor",[
        (this_or_next|eq, "$background_type", cb_priest),
        (eq, "$background_answer_2", dplmc_cb2_acolyte),
     ],"Religious fervor.",[
        (assign,"$background_answer_4",dplmc_cb4_fervor),
        (str_store_string,s13,"str_story_reason_fervor"),
        (jump_to_menu,"mnu_choose_skill"),
       ]),
      ("disown",[],"Being forced out of your home.",[
        (assign,"$background_answer_4",cb4_disown),
        (str_store_string,s13,"str_story_reason_disown"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
     ("greed",[],"Lust for money and power.",[
        (assign,"$background_answer_4",cb4_greed),
        (str_store_string,s13,"str_story_reason_greed"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_3"),
        ]
       ),
    ]
  ),


  (
    "choose_skill",mnf_disable_all_keys,
    "Only you know exactly what caused you to give up your old life and become an adventurer. {s13}",
    "none",
    [(assign,"$current_string_reg",10),
	 (assign, ":difficulty", 0),

	 (try_begin),
		(eq, "$character_gender", tf_female),
		(str_store_string, s14, "str_woman"),
		(val_add, ":difficulty", 1),
	 (else_try),
		(str_store_string, s14, "str_man"),
	 (try_end),

	 (try_begin),
        (eq,"$background_type",cb_noble),
		(str_store_string, s15, "str_noble"),
		(val_sub, ":difficulty", 1),
	 (else_try),
		(str_store_string, s15, "str_common"),
	 (try_end),

	 (try_begin),
		(eq, ":difficulty", -1),
		(str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
	 (else_try),
		(eq, ":difficulty", 0),
		(str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
	 (else_try),
		(eq, ":difficulty", 1),
		(str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
	 (try_end),
	],
    [
##      ("start_swordsman",[],"Swordsmanship.",[
##        (assign, "$starting_skill", 1),
##        (str_store_string, s14, "@You are particularly talented at swordsmanship."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_archer",[],"Archery.",[
##        (assign, "$starting_skill", 2),
##        (str_store_string, s14, "@You are particularly talented at archery."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_medicine",[],"Medicine.",[
##        (assign, "$starting_skill", 3),
##        (str_store_string, s14, "@You are particularly talented at medicine."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
      ("begin_adventuring",[],"Become an adventurer and ride to your destiny.",[
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
##           (try_begin),
##             (eq, "$starting_skill", 1),
##             (troop_raise_attribute, "trp_player",ca_agility,1),
##             (troop_raise_attribute, "trp_player",ca_strength,1),
##             (troop_raise_skill, "trp_player",skl_power_strike,2),
##             (troop_raise_proficiency, "trp_player",0,30),
##             (troop_raise_proficiency, "trp_player",1,20),
##           (else_try),
##             (eq, "$starting_skill", 2),
##             (troop_raise_attribute, "trp_player",ca_strength,2),
##             (troop_raise_skill, "trp_player",skl_power_draw,2),
##             (troop_raise_proficiency, "trp_player",3,50),
##           (else_try),
##             (troop_raise_attribute, "trp_player",ca_intelligence,1),
##             (troop_raise_attribute, "trp_player",ca_charisma,1),
##             (troop_raise_skill, "trp_player",skl_first_aid,1),
##             (troop_raise_skill, "trp_player",skl_wound_treatment,1),
##             (troop_add_item, "trp_player","itm_winged_mace",0),
##             (troop_raise_proficiency, "trp_player",0,15),
##             (troop_raise_proficiency, "trp_player",1,15),
##             (troop_raise_proficiency, "trp_player",2,15),
##           (try_end),


      (try_begin),
        (eq,"$background_type",cb_noble),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_polearm,10),

        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (call_script, "script_change_player_honor", 3),


##        (troop_add_item, "trp_player","itm_red_gambeson",imod_plain),
##        (troop_add_item, "trp_player","itm_sword",imod_plain),
##        (troop_add_item, "trp_player","itm_dagger",imod_balanced),
##        (troop_add_item, "trp_player","itm_woolen_hose",0),
##        (troop_add_item, "trp_player","itm_dried_meat",0),
##        (troop_add_item, "trp_player","itm_saddle_horse",imod_plain),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb_noble),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),

        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),

##        (troop_add_item, "trp_player","itm_dress",imod_sturdy),
##        (troop_add_item, "trp_player","itm_dagger",imod_watered_steel),
##        (troop_add_item, "trp_player","itm_woolen_hose",0),
##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
##        (troop_add_item, "trp_player","itm_bolts",0),
##        (troop_add_item, "trp_player","itm_smoked_fish",0),
##        (troop_add_item, "trp_player","itm_courser",imod_spirited),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb_merchant),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,2),
        (troop_raise_skill, "trp_player",skl_inventory_management,1),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),

##        (troop_add_item, "trp_player","itm_leather_jacket",0),
##        (troop_add_item, "trp_player","itm_leather_boots",0),
##        (troop_add_item, "trp_player","itm_fur_hat",0),
##        (troop_add_item, "trp_player","itm_dagger",0),
##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
##        (troop_add_item, "trp_player","itm_bolts",0),
##        (troop_add_item, "trp_player","itm_smoked_fish",0),
##        (troop_add_item, "trp_player","itm_saddle_horse",0),
##        (troop_add_item, "trp_player","itm_sumpter_horse",0),
##        (troop_add_item, "trp_player","itm_salt",0),
##        (troop_add_item, "trp_player","itm_salt",0),
##        (troop_add_item, "trp_player","itm_salt",0),
##        (troop_add_item, "trp_player","itm_pottery",0),
##        (troop_add_item, "trp_player","itm_pottery",0),

        (troop_add_gold, "trp_player", 250),
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
      (else_try),
        (eq,"$background_type",cb_guard),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_trainer",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_tab_shield_kite_b",imod_battered),

##        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
##        (troop_add_item, "trp_player","itm_skullcap",imod_rusty),
##        (troop_add_item, "trp_player","itm_spear",0),
##        (troop_add_item, "trp_player","itm_arming_sword",imod_chipped),
##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
##        (troop_add_item, "trp_player","itm_hunter_boots",0),
##        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
##        (troop_add_item, "trp_player","itm_bolts",0),
##        (troop_add_item, "trp_player","itm_smoked_fish",0),
##        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_gold, "trp_player", 50),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (else_try),
        (eq,"$background_type",cb_forester),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_athletics",1),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,30),
##        (troop_add_item, "trp_player","itm_short_bow",imod_bent),
##        (troop_add_item, "trp_player","itm_arrows",0),
##        (troop_add_item, "trp_player","itm_axe",imod_chipped),
##        (troop_add_item, "trp_player","itm_rawhide_coat",0),
##        (troop_add_item, "trp_player","itm_hide_boots",0),
##        (troop_add_item, "trp_player","itm_dried_meat",0),
##        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
##        (troop_add_item, "trp_player","itm_furs",0),
        (troop_add_gold, "trp_player", 30),
      (else_try),
        (eq,"$background_type",cb_nomad),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_horse_archery",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_riding",2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,30),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
##        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_rusty),
##        (troop_add_item, "trp_player","itm_nomad_armor",0),
##        (troop_add_item, "trp_player","itm_hide_boots",0),
##        (troop_add_item, "trp_player","itm_horse_meat",0),
##        (troop_add_item, "trp_player","itm_steppe_horse",0),
        (troop_add_gold, "trp_player", 15),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (else_try),
        (eq,"$background_type",cb_nomad),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_raise_skill, "trp_player","skl_first_aid",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_riding",2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,5),
        (troop_raise_proficiency, "trp_player",wpt_archery,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,5),
        (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
##        (troop_add_item, "trp_player","itm_sickle",imod_plain),
##        (troop_add_item, "trp_player","itm_nomad_armor",0),
##        (troop_add_item, "trp_player","itm_hide_boots",0),
##        (troop_add_item, "trp_player","itm_steppe_horse",0),
##        (troop_add_item, "trp_player","itm_grain",0),
        (troop_add_gold, "trp_player", 20),
      (else_try),
        (eq,"$background_type",cb_thief),
        (troop_raise_attribute, "trp_player",ca_agility,3),
        (troop_raise_skill, "trp_player","skl_athletics",2),
        (troop_raise_skill, "trp_player","skl_power_throw",1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_raise_skill, "trp_player","skl_looting",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,20),
        (troop_add_item, "trp_player","itm_throwing_knives",0),
##        (troop_add_item, "trp_player","itm_stones",0),
##        (troop_add_item, "trp_player","itm_cudgel",imod_plain),
##        (troop_add_item, "trp_player","itm_dagger",imod_rusty),
##        (troop_add_item, "trp_player","itm_shirt",imod_tattered),
##        (troop_add_item, "trp_player","itm_black_hood",imod_tattered),
##        (troop_add_item, "trp_player","itm_wrapping_boots",imod_ragged),
        (troop_add_gold, "trp_player", 25),
     (else_try), #SB : re-enable priests
       (eq,"$background_type",cb_priest),
       (troop_raise_attribute, "trp_player",ca_strength,1),
       (troop_raise_attribute, "trp_player",ca_intelligence,2),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       (troop_raise_skill, "trp_player","skl_wound_treatment",1),
       (troop_raise_skill, "trp_player","skl_leadership",1),
       (troop_raise_skill, "trp_player","skl_prisoner_management",1),
       (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
       # (troop_add_item, "trp_player","itm_robe",0),
       # (troop_add_item, "trp_player","itm_wrapping_boots",0), #SB : remove most of these, cb3 adds equipment
       # (troop_add_item, "trp_player","itm_club",0),
       (troop_add_item, "trp_player","itm_grain",imod_large_bag),
       # (troop_add_item, "trp_player","itm_sumpter_horse",0), #SB: I guess it's a donkey or something
       (troop_add_gold, "trp_player", 10),
       (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (try_end),

    (try_begin),
        (eq,"$background_answer_2",cb2_page),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,5),
    (else_try),
        (eq,"$background_answer_2",cb2_apprentice),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player","skl_engineer",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
    (else_try),
        (eq,"$background_answer_2",cb2_urchin),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_looting",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_throwing,5),
    (else_try),
        (eq,"$background_answer_2",cb2_steppe_child),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_horse_archery",1),
        (troop_raise_skill, "trp_player","skl_power_throw",1),
        (troop_raise_proficiency, "trp_player",wpt_archery,15),
        (call_script,"script_change_troop_renown", "trp_player", 5),
    (else_try),
        (eq,"$background_answer_2",cb2_merchants_helper),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_mummer),
       (troop_raise_attribute, "trp_player",ca_intelligence,1),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       # (troop_raise_skill, "trp_player",skl_leadership,1), #SB : +2 attr, +2 skill
       (troop_raise_skill, "trp_player",skl_athletics,1),
       (troop_raise_skill, "trp_player",skl_riding,1),
       (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,5),
       (troop_raise_proficiency, "trp_player",wpt_polearm,5),
       (call_script,"script_change_troop_renown", "trp_player", 15),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_courtier),
       (troop_raise_attribute, "trp_player",ca_charisma,2), #SB : lower to +2
       (troop_raise_attribute, "trp_player",ca_agility,1),
       (troop_raise_skill, "trp_player","skl_weapon_master",1),
       (troop_raise_skill, "trp_player","skl_persuasion",1), #add this I guess from page
       (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
       # (troop_raise_proficiency, "trp_player",wpt_polearm,10), #this is way too much wpt for a courtier
       (troop_raise_proficiency, "trp_player",wpt_crossbow, 5),
       (call_script,"script_change_troop_renown", "trp_player", 20),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_noble),
       (troop_raise_attribute, "trp_player",ca_intelligence,1),
       (troop_raise_attribute, "trp_player",ca_charisma,2),
       (troop_raise_skill, "trp_player","skl_leadership",1),
       (troop_raise_skill, "trp_player","skl_tactics",1),
       (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
       (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
       (call_script,"script_change_troop_renown", "trp_player", 15),
       #SB : add background renown/honor/rtr
       (val_add, "$player_right_to_rule", 1),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_acolyte),
       (troop_raise_attribute, "trp_player",ca_agility,1),
       (troop_raise_attribute, "trp_player",ca_intelligence,1),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       (troop_raise_skill, "trp_player",skl_leadership,1),
       (troop_raise_skill, "trp_player",skl_surgery,1),
       (troop_raise_skill, "trp_player",skl_first_aid,1),
       (troop_raise_proficiency, "trp_player",wpt_polearm,10),
       (call_script,"script_change_troop_renown", "trp_player", 5),
	(try_end),

	(try_begin), #SB :re-enable 3x cb3 options, adding 1x body armor and weapon + food
       (eq,"$background_answer_3",dplmc_cb3_bravo),
       (troop_raise_attribute, "trp_player",ca_strength,1),
       (troop_raise_skill, "trp_player","skl_power_strike",1),
       (troop_raise_skill, "trp_player","skl_shield",1),
       (troop_add_gold, "trp_player", 10),
       # (try_begin),
       # (this_or_next|player_has_item,"itm_sword"),
       # (troop_has_item_equipped,"trp_player","itm_sword"),
       # (troop_remove_item, "trp_player","itm_sword"),
       # (try_end),
       # (try_begin),
       # (this_or_next|player_has_item,"itm_arming_sword"),
       # (troop_has_item_equipped,"trp_player","itm_arming_sword"),
       # (troop_remove_item, "trp_player","itm_arming_sword"),
       # (try_end),
       # (troop_add_item, "trp_player","itm_short_sword",0),
       # (troop_add_item, "trp_player","itm_wooden_shield",imod_battered),
       # (store_random_in_range, ":shield_item", "itm_norman_shield_1", "itm_tab_shield_round_a"),
       # (troop_add_item, "trp_player",":shield_item",imod_heavy),
       # (store_random_in_range, ":armor_item", "itm_gambeson", "itm_tribal_warrior_outfit"),
       # (store_random_in_range, ":armor_imod", imod_tattered, imod_reinforced),
       # (troop_add_item, "trp_player",":armor_item",":armor_imod"),
       # (troop_add_item, "trp_player", "itm_ankle_boots", 0),
       #store a random sword
       # (store_random_in_range, ":weapon_item", "itm_long_voulge", "itm_mace_1"),
       # (try_begin), #2+4 offset for scimitar + sarranid swords
         # (lt, ":weapon_item", "itm_sword_medieval_a"),
         # (val_sub, ":weapon_item", "itm_long_voulge"),
         # (val_add, ":weapon_item", "itm_scimitar"),
       # (try_end),
       # (troop_add_item, "trp_player",":weapon_item"),
       (store_random_in_range, ":food_item", "itm_dried_meat", "itm_grain"),
       (troop_add_item, "trp_player",":food_item"),
       (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
       (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
   (else_try),
       (eq,"$background_answer_3",dplmc_cb3_merc),
       (troop_raise_attribute, "trp_player",ca_agility,1),
       (troop_raise_skill, "trp_player",skl_weapon_master,1),
       (troop_raise_skill, "trp_player",skl_shield,1),
       # (try_begin),
       # (this_or_next|player_has_item,"itm_hide_boots"),
       # (troop_has_item_equipped,"trp_player","itm_hide_boots"),
       # (troop_remove_item, "trp_player","itm_hide_boots"),
       # (try_end),
       #store crap gear here, this depends on Native's item ordering
       # (store_random_in_range, ":helmet_item", "itm_byzantion_helmet_a", "itm_tunic_with_green_cape"),
       # (store_random_in_range, ":weapon_item", "itm_sword_medieval_a", "itm_club_with_spike_head"),
       # (store_random_in_range, ":armor_item", "itm_leather_jerkin", "itm_lamellar_vest"),
       # (store_random_in_range, ":boots_item", "itm_hunter_boots", "itm_splinted_greaves"),
       # (store_random_in_range, ":helmet_imod", imod_tattered, imod_reinforced),
       # (store_random_in_range, ":weapon_imod", imod_crude, imod_deadly),
       # (store_random_in_range, ":armor_imod", imod_tattered, imod_reinforced),
       
       #SB : pick 1 set for each faction
       # (store_random_in_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
       # (try_begin),
         # (eq, ":faction_no", "fac_kingdom_1"),
         # (store_random_in_range, ":helmet_item", "itm_norman_helmet", "itm_kettle_hat"),
         # (store_random_in_range, ":weapon_item", "itm_awlpike", "itm_bec_de_corbin_a"),
       # (else_try),
         # (eq, ":faction_no", "fac_kingdom_2"),
         # (store_random_in_range, ":helmet_item", "itm_vaegir_fur_cap", "itm_vaegir_lamellar_helmet"),
       # (else_try),
         # (eq, ":faction_no", "fac_kingdom_3"), #original items
         # (assign, ":helmet_item", "itm_h_cerveliere_padded"),
         # (store_random_in_range, ":weapon_item", "itm_sword_khergit_1", "itm_sword_khergit_4"),
         # (assign, ":boots_item","itm_mail_chausses"),
         # (assign, ":helmet_imod", imod_crude),
       # (else_try),
         # (eq, ":faction_no", "fac_kingdom_4"), #pick axes, some are fairly expensive
         # (store_random_in_range, ":weapon_item","itm_one_handed_war_axe_a", "itm_bardiche"),
         # (assign, ":helmet_item", 0),
       # (else_try),
         # (eq, ":faction_no", "fac_kingdom_5"), #pick from the blunt range
         # (store_random_in_range, ":weapon_item","itm_military_hammer", "itm_sickle"),
       # (else_try),
         # (eq, ":faction_no", "fac_kingdom_6"), #a fairly complete set of gear
         # (troop_add_item, "trp_player","itm_sarranid_warrior_cap",imod_hardened),
         # (store_random_in_range, ":boots_item", "itm_sarranid_boots_a", "itm_sarranid_boots_d"),
         # (store_random_in_range, ":helmet_item", "itm_sarranid_felt_hat", "itm_sarranid_horseman_helmet"),
       # (try_end),
       # (try_begin),
         # (gt, ":helmet_item", 0),
         # (troop_add_item, "trp_player", ":helmet_item", ":helmet_imod"),
       # (try_end),
       # (try_begin),
         # (gt, ":weapon_item", 0),
         # (try_begin),
           # (call_script, "script_dplmc_troop_can_use_item", "trp_player", ":weapon_item", ":weapon_imod"),
           # (eq, reg0, 1),
           # (troop_add_item, "trp_player", ":weapon_item", ":weapon_imod"),
         # (else_try), #use a low-requirement common spear, or highest wpt_proficiency I guess
           # (store_random_in_range, ":weapon_item", "itm_shortened_spear", "itm_light_lance"),
           # (troop_add_item, "trp_player", ":weapon_item", ":weapon_imod"),
         # (try_end),
       # (try_end),
       # (try_begin),
         # (gt, ":armor_item", 0),
         # (try_begin),
           # (call_script, "script_dplmc_troop_can_use_item", "trp_player", ":armor_item", ":armor_imod"),
           # (eq, reg0, 1),
           # (troop_add_item, "trp_player", ":armor_item", ":armor_imod"),
         # (else_try), #use a low-requirement gambeson
           # (store_random_in_range, ":armor_item", "itm_blue_gambeson", "itm_nomad_vest"),
           # (troop_add_item, "trp_player", ":armor_item", ":armor_imod"),
         # (try_end),
       # (try_end),
       # (try_begin),
         # (gt, ":boots_item", 0),
         # (troop_add_item, "trp_player", ":boots_item", 0),
       # (try_end),
       
       (store_random_in_range, ":food_item", "itm_cattle_meat", "itm_siege_supply"),
       (troop_add_item, "trp_player",":food_item"),
       # (troop_add_gold, "trp_player", 20),
       # (troop_raise_proficiency, "trp_player",wpt_polearm,20),
       (try_for_range, ":unused", 0, 4),
         (store_random_in_range, ":wpt", wpt_one_handed_weapon, wpt_firearm),
         (troop_raise_proficiency, "trp_player",":wpt",5), #"taught you how to wield any weapon you desired"
       (try_end),
   (else_try),
        (eq,"$background_answer_3",cb3_poacher),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_athletics",1),
        (troop_add_gold, "trp_player", 10),
        (troop_raise_proficiency, "trp_player",wpt_polearm,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,35),

        # (troop_add_item, "trp_player","itm_axe",imod_chipped),
        # (troop_add_item, "trp_player","itm_rawhide_coat",0),
        # (troop_add_item, "trp_player","itm_hide_boots",0),
        # (troop_add_item, "trp_player","itm_w_hunting_bow_elm",0),
        # (troop_add_item, "trp_player","itm_barbed_arrows",0),
        # (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
        # (troop_add_item, "trp_player","itm_dried_meat",0),
        # (troop_add_item, "trp_player","itm_dried_meat",0),
        # (troop_add_item, "trp_player","itm_furs",0),
        # (troop_add_item, "trp_player","itm_furs",0),
    (else_try),
        (eq,"$background_answer_3",cb3_craftsman),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_engineer",1),
        (troop_raise_skill, "trp_player","skl_tactics",1),
        (troop_raise_skill, "trp_player","skl_trade",1),

        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_add_gold, "trp_player", 100),


        # (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        # (troop_add_item, "trp_player","itm_coarse_tunic",0),

        # (troop_add_item, "trp_player","itm_sword_medieval_b", imod_balanced),
        # (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        # (troop_add_item, "trp_player","itm_bolts",0),

        # (troop_add_item, "trp_player","itm_tools",0),
        # (troop_add_item, "trp_player","itm_saddle_horse",0),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_peddler),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),

        # (troop_add_item, "trp_player","itm_leather_gauntlet",imod_plain),
        (troop_add_gold, "trp_player", 90),
        (troop_raise_proficiency, "trp_player",wpt_polearm,15),

        # (troop_add_item, "trp_player","itm_leather_jacket",0),
        # (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        # (troop_add_item, "trp_player","itm_fur_hat",0),
        # (troop_add_item, "trp_player","itm_staff",0),
        # (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        # (troop_add_item, "trp_player","itm_bolts",0),
        # (troop_add_item, "trp_player","itm_saddle_horse",0),
        # (troop_add_item, "trp_player","itm_sumpter_horse",0),

        (troop_add_item, "trp_player","itm_linen",0),
        (troop_add_item, "trp_player","itm_pottery",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
   (else_try),
       (eq,"$background_answer_3",dplmc_cb3_preacher),
       (troop_raise_attribute, "trp_player",ca_strength,1),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       (troop_raise_skill, "trp_player","skl_shield",1),
       (troop_raise_skill, "trp_player","skl_wound_treatment",1),
       (troop_raise_skill, "trp_player","skl_first_aid",1),
       (troop_raise_skill, "trp_player","skl_surgery",1),
       # (troop_add_item, "trp_player","itm_g_leather_gloves",imod_ragged),
       (troop_add_item, "trp_player","itm_practice_staff",imod_heavy),
       #remove monk stuff, add pilgrim stuff
       # (troop_remove_item, "trp_player", "itm_robe"),
       # (troop_remove_item, "trp_player", "itm_black_hood"),
       (troop_add_item, "trp_player", "itm_pilgrim_disguise"),
       (troop_add_item, "trp_player", "itm_pilgrim_hood"),
       (troop_add_item, "trp_player", "itm_b_wrapping_boots"),
       (troop_add_item, "trp_player", "itm_cheese"), #add 1x food
       (troop_add_gold, "trp_player", 10),
       (troop_raise_proficiency, "trp_player",wpt_polearm,20),
    (else_try),
        (eq,"$background_answer_3",cb3_troubadour),
        (troop_raise_attribute, "trp_player",ca_charisma,2),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),

        (troop_add_gold, "trp_player", 80),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),

        # (troop_add_item, "trp_player","itm_tabard",imod_sturdy),
        # (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        # (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        # (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
        # (troop_add_item, "trp_player","itm_bolts", 0),
        # (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_squire),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),

        (troop_add_gold, "trp_player", 20),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_polearm,30),
        (troop_raise_proficiency, "trp_player",wpt_archery,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),

        # (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
        # (troop_add_item, "trp_player","itm_leather_boots",imod_tattered),

        # (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        # (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        # (troop_add_item, "trp_player","itm_bolts",0),
        # (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_lady_in_waiting),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),

        (troop_raise_skill, "trp_player","skl_persuasion",2),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),

        # (troop_add_item, "trp_player","itm_dagger", 0),
        # (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        # (troop_add_item, "trp_player","itm_bolts",0),
        # (troop_add_item, "trp_player","itm_courser", imod_spirited),
        # (troop_add_item, "trp_player","itm_woolen_hood",imod_sturdy),
        # (troop_add_item, "trp_player","itm_woolen_dress",imod_sturdy),
        (troop_add_gold, "trp_player", 100),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,15),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_student),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_surgery",1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),

        (troop_add_gold, "trp_player", 80),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,20),

        # (troop_add_item, "trp_player","itm_linen_tunic",imod_sturdy),
        # (troop_add_item, "trp_player","itm_woolen_hose",0),
        # (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        # (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
        # (troop_add_item, "trp_player","itm_bolts", 0),
        # (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        (store_random_in_range, ":book_no", books_begin, books_end),
        (troop_add_item, "trp_player",":book_no",0),
    (try_end),

      (try_begin),
        (eq,"$background_answer_4",cb4_revenge),
        (troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
      (else_try),
        (eq,"$background_answer_4",cb4_loss),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
      (else_try),
        (eq,"$background_answer_4",cb4_wanderlust),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
      (else_try),
        (eq,"$background_answer_4",dplmc_cb4_fervor),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10), #wait what
      (else_try),
        (eq,"$background_answer_4",cb4_disown),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
      (else_try),
        (eq,"$background_answer_4",cb4_greed),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_looting",1),
      (try_end),

      #SB : pre-allocate disguises
      (try_begin),
        (assign, ":disguise", disguise_pilgrim), #always available
        #farmer, acquired from not picking inappropriate noble/priestly options
        (try_begin),
          (neq, "$background_type", cb_noble),
          (neq, "$background_type", cb_priest),
          (neq, "$background_answer_2", cb2_page),
          (neq, "$background_answer_2", dplmc_cb2_courtier),
          (neq, "$background_answer_2", dplmc_cb2_noble),
          (neq, "$background_answer_2", dplmc_cb2_acolyte),
          (is_between, "$background_answer_3", cb3_poacher, dplmc_cb3_preacher),
          (val_add, ":disguise", disguise_farmer),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_forester),
          (this_or_next|eq, "$background_answer_2", cb2_steppe_child),
          (eq, "$background_answer_3", cb3_poacher),
          (val_add, ":disguise", disguise_hunter),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_merchant),
          (this_or_next|eq, "$background_answer_2", cb2_merchants_helper),
          (eq, "$background_answer_3", cb3_peddler),
          (val_add, ":disguise", disguise_merchant),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_guard),
          (this_or_next|eq, "$background_answer_3", dplmc_cb3_bravo),
          (this_or_next|eq, "$background_answer_3", dplmc_cb3_merc),
          (eq, "$background_answer_3", cb3_squire),
          (val_add, ":disguise", disguise_guard),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_answer_2", dplmc_cb2_mummer),
          (eq, "$background_answer_3", cb3_troubadour),
          (val_add, ":disguise", disguise_bard),
        (try_end),
      (try_end),
      (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, ":disguise"),

      #TODO parse skill bonus, split it up
      (call_script, "script_build_background_answer_story", 0),
      (add_info_page_note_from_sreg, ip_character_backgrounds, 1, s10, 0),
      (add_info_page_note_from_sreg, ip_character_backgrounds, 2, s11, 0),
      (add_info_page_note_from_sreg, ip_character_backgrounds, 3, s12, 0),
      (add_info_page_note_from_sreg, ip_character_backgrounds, 4, s13, 0),
      # (add_info_page_note_from_sreg, ip_character_backgrounds, 1, "str_s0", 0),
      (try_begin),
        (eq, "$background_type", cb_noble),
        (jump_to_menu, "mnu_auto_return"),
#normal_banner_begin
        (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#             (start_presentation, "prsnt_custom_banner"),
      (else_try),
        (change_screen_return, 0),
      (try_end),
      (set_show_messages, 1),
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu,"mnu_start_character_4"),
        ]),
    ]
  ),

  (
    "past_life_explanation",mnf_disable_all_keys,
    "{s3}",
    "none",
    [
     (try_begin),
       (gt,"$current_string_reg",14),
       (assign,"$current_string_reg",10),
     (try_end),
     (str_store_string_reg,s3,"$current_string_reg"),
     (try_begin),
       (ge,"$current_string_reg",14),
       (str_store_string,s5,"@Back to the beginning..."),
     (else_try),
       (str_store_string,s5,"@View next segment..."),
     (try_end),
     ],
    [
      ("view_next",[],"{s5}",[
        (val_add,"$current_string_reg",1),
        (jump_to_menu, "mnu_past_life_explanation"),
        ]),
      ("continue",[],"Continue...",
       [
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu, "mnu_choose_skill"),
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
        (assign,"$background_type",cb_guard),
        #(str_store_string,s10,"str_story_parent_guard"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),
    ("dac_start_hunter",[(neq, "$character_gender", tf_female)],"A hunter.",[
        (assign,"$background_type",cb_forester),
        #(str_store_string,s10,"str_story_parent_forester"),
        (jump_to_menu,"mnu_dac_choose_skill"),
    ]),
  
    ("dac_start_mercenary",[(neq, "$character_gender", tf_female)],"A rugged mercenary.",[
        (assign,"$background_type",cb_merc),
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
        (assign,"$background_type",cb_forester),
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
          #(set_show_messages, 0),
           
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
            (eq,"$background_type",cb_guard),
            (call_script, "script_start_as_warrior"),
          (else_try),
            (eq,"$background_type",cb_forester),
            (call_script, "script_start_as_hunter"),
          (else_try),
           (eq,"$background_type",cb_merc),
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
          (eq, "$background_type", cb_forester),
          (val_add, ":disguise", disguise_hunter),
        (try_end),
        (try_begin),
          (eq, "$background_type", cb_merchant),
          (val_add, ":disguise", disguise_merchant),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_guard),
          (eq, "$background_type", cb_merc),
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
      #(set_show_messages, 1),
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


]