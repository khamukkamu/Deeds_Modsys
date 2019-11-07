from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

from compiler import *
####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW VILLAGE TEMPLATES #####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),
  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW BANDITS TEMPLATES #####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,5,50)]),
  # ("plains_bandits","Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_bandit,4,58)]),
  # ("steppe_bandits","Steppe Bandits",icon_khergit_horseman_b|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,58)]),
### Routiers  
  ("routier_bandits","Routiers",icon_dac_routier|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_routier_knight,1,1),(trp_routier_crossbowman,4,12),(trp_routier_mounted_sergeant,4,12),(trp_routier_sergeant,2,10),(trp_routier_voulgier,4,12),(trp_routier_footman,8,24)]),
### Flayers
  ("flayer_bandits","Flayers",icon_dac_flayer|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_flayer_captain,1,1),(trp_flayer_infantry,6,18),(trp_flayer_fauchard,4,12),(trp_flayer_archer,2,8)]),
### Retondeurs
  ("retondeur_bandits","Retondeurs",icon_dac_retondeur|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_retondeur_horseman,2,12),(trp_retondeur_maceman,6,18),(trp_retondeur_crossbowman,2,8)]),
### Tard-Venus
  ("tard_venu_bandits","Tard-Venus",icon_dac_tard_venu|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_tard_venu_militia,8,24),(trp_tard_venu_pikeman,6,18),(trp_tard_venu_archer,4,12)]),
### Angry Plebs 
  ("peasant_bandits","Rebellious Peasants",icon_dac_rebel_peasants|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_disgruntled_farmer,8,24),(trp_irrate_hunter,4,12),(trp_furious_lumberjack,1,6)]),

### Native
  # ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58)]),
  # ("desert_bandits","Desert Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58)]),
  # ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,4,52)]),
  # ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,60)]),
  # ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,5,50)]),
  ("deserters","Deserters",icon_dac_deserter|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
### Quest Related	
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  	
### Bandit Lairs	
  # ("plains_bandit_lair" ,"Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_bandit,15,58)]),
  # ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  # ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  # ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  # ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  # ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  # ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
 ### New Lairs
  ("routier_lair","Routier Stronghold",icon_castle_e|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_routier_knight,1,1),(trp_routier_crossbowman,4,12),(trp_routier_mounted_sergeant,2,12),(trp_routier_sergeant,1,4),(trp_routier_voulgier,2,6),(trp_routier_footman,4,12)]),
  ("flayer_lair","Flayer Camp",icon_camp|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_flayer_captain,1,1),(trp_flayer_infantry,4,12),(trp_flayer_fauchard,2,8),(trp_flayer_archer,2,8)]),
  ("retondeur_lair","Retondeur Camp",icon_camp|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_retondeur_horseman,2,8),(trp_retondeur_maceman,4,12),(trp_retondeur_crossbowman,2,8)]),
  ("tard_venu_lair","Tard-Venu Occupied Village",icon_village_a|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_tard_venu_militia,4,20),(trp_tard_venu_pikeman,4,12),(trp_tard_venu_archer,2,8)]),
  ("angry_pleb_lair","Rebellious Village",icon_village_a|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_disgruntled_farmer,4,20),(trp_irrate_hunter,4,12),(trp_furious_lumberjack,4,12)]),

 
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_looter,15,50)]),


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW MISC TEMPLATES #####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################
  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),
  ("merchant_caravan","Merchant Caravan",icon_mule|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("spy_partners", "Unremarkable Travellers", icon_player_horseman|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_player_horseman|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW FACTION TEMPLATES #####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),
  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_dac_routier|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_flagbearer_b|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",icon_vaegir_knight,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),
  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  ("center_reinforcements","Reinforcements", icon_axeman|pf_show_faction|carries_goods(4),0,fac_commoners,escorted_merchant_personality,[]),

# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_french_peasant,1,5),(trp_french_militia,1,5),(trp_french_militia_voulgier,1,4),(trp_french_peasant_archer,1,3),(trp_french_peasant_crossbowman,1,3)]),
("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_french_crossbowman,1,3),(trp_french_infantry,2,7),(trp_french_voulgier,1,4),(trp_french_militia,1,3),(trp_french_militia_voulgier,1,3),(trp_french_man_at_arms,1,2)] ),
("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_genoese_crossbowman,1,2),(trp_french_pavisier,1,3),(trp_french_heavy_infantry,2,5),(trp_french_heavy_voulgier,1,3),(trp_french_heavy_man_at_arms,1,2),(trp_french_sergeant,1,1)] ),
("kingdom_1_reinforcements_d", "kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_french_captain,1,4),(trp_french_squire,2,6),(trp_french_chevalier_bachelier_a_pied,1,3),(trp_french_knight_bachelier,1,3),(trp_french_chevalier_banneret_a_pied,1,3),(trp_french_chevalier_banneret,1,3)] ),

("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_english_peasant,1,5),(trp_english_levy_spearman,1,5),(trp_english_yeoman,1,4),(trp_english_peasant_archer,1,4),(trp_english_yeoman_archer,1,2)]),
("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_english_yeoman_archer,1,3),(trp_english_infantry,1,6),(trp_english_militia_billman,1,4),(trp_english_spearman,1,3),(trp_english_longbowman,1,3),(trp_english_levy_spearman,1,2)] ),
("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_english_longbowman_captain,1,1),(trp_english_retinue_longbowman,1,3),(trp_english_heavy_spearman,2,5),(trp_english_billman,1,4),(trp_english_heavy_infantry,1,4),(trp_english_sergeant,1,1)] ),
("kingdom_2_reinforcements_d", "kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_english_captain,2,6),(trp_english_squire,1,4),(trp_english_dismounted_knight,1,3),(trp_english_knight,1,3),(trp_three_lions_guard,1,1),(trp_english_heavy_knight,1,3)] ),

("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_burgundian_peasant,1,5),(trp_burgundian_militia_pikeman,1,5),(trp_burgundian_militia,1,4),(trp_burgundian_militia_archer,1,3),(trp_burgundian_militia_crossbowman,1,3)]),
("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_burgundian_crossbowman,1,3),(trp_burgundian_infantry,1,6),(trp_burgundian_pikeman,1,4),(trp_burgundian_halberdier,1,3),(trp_burgundian_militia_pikeman,1,3),(trp_burgundian_archer,1,2)] ),
("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_flemish_heavy_pikeman,1,2),(trp_burgundian_longbowman,1,3),(trp_burgundian_heavy_pikeman,2,5),(trp_burgundian_heavy_infantry,1,4),(trp_burgundian_heavy_halberdier,1,4),(trp_burgundian_sergeant,1,1)] ),
("kingdom_3_reinforcements_d", "kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_burgundian_captain,1,4),(trp_burgundian_squire,2,6),(trp_burgundian_mounted_crossbowman_captain,1,3),(trp_burgundian_guard,1,3),(trp_burgundian_knight,1,3),(trp_burgundian_heavy_knight,1,3)] ),

("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_breton_peasant,1,5),(trp_breton_militia,1,5),(trp_breton_fauchard,1,4),(trp_breton_peasant_archer,1,6)]),
("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_breton_militia_archer,1,3),(trp_breton_infantry,2,7),(trp_breton_poleaxeman,1,4),(trp_breton_man_at_arms,1,3),(trp_breton_militia,1,3),(trp_breton_militia_crossbowman,1,2)] ),
("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_breton_archer,1,3),(trp_breton_crossbowman,1,2),(trp_breton_heavy_infantry,2,6),(trp_breton_heavy_poleaxeman,1,4),(trp_breton_heavy_man_at_arms,1,4),(trp_breton_sergeant,1,1)] ),
("kingdom_4_reinforcements_d", "kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_breton_captain,1,4),(trp_breton_squire,2,6),(trp_breton_knight,1,3),(trp_breton_dismounted_noble,1,3),(trp_breton_noble_swordsman,1,3),(trp_breton_heavy_knight,1,3)] ),



   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman_b|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_flagbearer_b|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
]
