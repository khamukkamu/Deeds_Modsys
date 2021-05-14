from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

from compiler import *
####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(16.34, -62.88),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC TOWNS #################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################
  
### DAC French Towns  
    ("french_town_1","Bourges",  icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.92, -5.56),[], 171),                           
    ("french_town_2","Orléans",     icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.49, 29.31),[], 88),
    ("french_town_3","Tours",   icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.24, 3.3),[], 13),                             
    ("french_town_4","Poitiers",     icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.44, -30.13),[], 356),                     
    ("french_town_5","La_Rochelle",  icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.95, -40.81),[], 323),                   
    ("french_town_6","Clermont",   icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.97, -42.83),[], 233),
    ("french_town_7","Moulins",   icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.47, -17.53),[], 314),                         
    ("french_town_8","Aurillac", icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.69, -103.17),[], 267),                          
    ("french_town_9","Lyon",   icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.4, -38.87),[], 100),
    ("french_town_10","Le_Puy",   icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.31, -85),[], 291),                         

    ("french_town_11","Cahors", icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.53, -112.39),[], 68),                            
    ("french_town_12","Rodez",icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.36, -116.77),[], 292),                            
    ("french_town_13","Lectoure",  icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.6, -126.26),[], 41),                        
    ("french_town_14","Tarbes",  icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.02, -148.18),[], 23),                        
    ("french_town_15","Toulouse",  icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.54, -130.45),[], 267),                         
    ("french_town_16","Carcassonne", icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.32, -140.38),[], 92),                      
    ("french_town_17","Montpellier", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.05, -130.76),[], 20),                      
    ("french_town_18","Valence", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.64, -75.91),[], 102),                         
    ("french_town_19","Thouars", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.83, -10.32),[], 276),                         
    ("french_town_20","Tournai", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.21, 127.07),[], 139),                          

    ("french_town_21","Gien", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.02, 18.15),[], 319),                              
    ("french_town_22","Montargis-le-Franc", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.83, 33.71),[], 43),
    ("french_town_23","Albret", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.21, -122.18),[], 208),      
    ("french_town_24","Bergerac", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.94, -98.32),[], 335),           
    ("french_town_25","Périgueux", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.59, -78),[], 190),      
    ("french_town_26","Angoulême", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.97, -64.35),[], 240),    
    ("french_town_27","Limoges", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.06, -51.49),[], 269),           
    ("french_town_28","Angers", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.28, 13.61),[], 337),     
    ("french_town_29","Foix", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.59, -149),[], 280),      ### NEW           

 ### DAC English Towns
    ("english_town_1","Paris", icon_town_paris|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.81, 75.01),[], 318),                    
    ("english_town_2","Bayonne", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.8, -141.97),[], 232),  
    ("english_town_3","Nemours", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.63, 51.8),[], 3),                                                      
    ("english_town_4","Laval", icon_town_b_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.39, 44.14),[], 217),                           
    ("english_town_5","Le_Mans", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.98, 39.05),[], 151),               
    ("english_town_6","Bordeaux", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.24, -104.72),[], 127),    
    ("english_town_7","Chartres", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.96, 52.74),[], 38),                          
    ("english_town_8","Rouen", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.02, 92.18),[], 145),                               
    ("english_town_9","Caen", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.72, 90.02),[], 216),                             
    ("english_town_10","Harfleur", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.86, 100.66),[], 303),  
    
    ("english_town_11","Cherbourg", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.67, 118.74),[], 189),                     
    ("english_town_12","Bayeux", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.44, 95.73),[], 194),                           
    ("english_town_13","Calais", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.75, 147.18),[], 193),
    ("english_town_14","Alençon", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18, 55.51),[], 225),                         
    ("english_town_15","Argentan", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.3, 66.17),[], 225),                  
    ("english_town_16","Tartas", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.61, -132.04),[], 200),       
    ("english_town_17","Dax", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.64, -135.79),[], 256),      ### NEW           
    ("english_town_18","Libourne", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.63, -96.65),[], 221),      ### NEW           
    ("english_town_19","Saint-Lô", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.66, 92.08),[], 220),      ### NEW           
    ("english_town_20","Eu", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.2, 117.57),[], 48),      ### NEW           
    
    ("english_town_21","Avranches", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.46, 72.94),[], 225),      ### NEW           
    ("english_town_22","Coutances", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.98, 88.29),[], 271),      ### NEW           

 ### DAC Burgundian Towns
    ("burgundian_town_1","Dijon", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.33, 15.28),[], 242),
    ("burgundian_town_2","Besançon", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.92, 10.74),[], 132),                       
    ("burgundian_town_3","Nevers", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.58, -9.08),[], 91),                            
    ("burgundian_town_4","Auxerre", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.05, 20.62),[], 128),                          
    ("burgundian_town_5","Troyes", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.71, 49.03),[], 302),                        
    ("burgundian_town_6","Compiègne", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.38, 92),[], 12),                        
    ("burgundian_town_7","Bruges", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.64, 146.38),[], 218),                         
    ("burgundian_town_8","Gand", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.1, 140.47),[], 97),                             
    ("burgundian_town_9","Malines", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.37, 141.87),[], 227),               
    ("burgundian_town_10","Boulogne", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.99, 133.68),[], 52),        
    
    ("burgundian_town_11","Châlons-en-Champagne", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.62, 76.41),[], 209),           
    ("burgundian_town_12","Reims", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.19, 88.61),[], 303),                            
    ("burgundian_town_13","Amiens",icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.44, 108.18),[],284),
    ("burgundian_town_14","Péronne",icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.45, 108.32),[],345),

### DAC Breton Towns
    ("breton_town_1","Rennes", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.54, 46.77),[], 192),                          
    ("breton_town_2","Nantes", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.76, 13.39),[], 278),                          
    ("breton_town_3","Vannes", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.03, 29.52),[], 13),                          
    ("breton_town_4","Kemper", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.03, 50.66),[], 211),
    ("breton_town_5","Saint-Malo", icon_town_b_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.75, 68.66),[], 354),          
    ("breton_town_6","Saint-Brieuc", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.42, 66.42),[], 153),                  
    ("breton_town_7","Saint-Pol-de-Léon", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.39, 76.05),[], 326),            
    ("breton_town_8","Rohan", icon_town_b_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.98, 53.81),[], 27),                          

   
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CASTLES ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### DAC French Castles
  ("french_castle_1","Forteresse_de_Chinon",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.25, -3.67),[],306),        
  ("french_castle_2","Châteauroux",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.83, -15.04),[],56),                
  ("french_castle_3","Château de Niort",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.96, -35.4),[],255),
  ("french_castle_4","La Tour_de_Termes",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.95, -134.85),[],210),        
  ("french_castle_5","Château_de_Murol",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.12, -62.97),[],280),            
  ("french_castle_6","Château_de_Polignac",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.03, -81.04),[],30),           
  ("french_castle_7","Château_de_Culant",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.69, -23.41),[],3),           
  ("french_castle_8","Château_de_Chaumont",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.94, 15.89),[],67),        
  ("french_castle_9","Château_de_Boussac",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.9, -31.4),[],64),           
  ("french_castle_10","Yèvre-le-Châtel",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.18, 44.27),[],209),   
  
  ("french_castle_11","Château_de_La_Fayette",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.49, -57.99),[],285),
  ("french_castle_12","La_Tour_d'Auvergne",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.77, -55.36),[],269),          
  ("french_castle_13","Château_de_Charlus",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.55, -57.43),[],46),      ### NEW
  ("french_castle_14","Château_de_Sancerre",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.57, 6.35),[],268),        
  ("french_castle_15","Castelnau_Tursan",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.55, -136.67),[],108),          
  ("french_castle_16","Forteresse_d'Auch",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.17, -137.73),[],7),           
  ("french_castle_17","Mont-St-Michel",icon_town_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.16, 67.25),[],197),             
  ("french_castle_18","Château_de_Turenne",icon_castle_d_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.08, -99.32),[],360),          
  ("french_castle_19","Sévérac-le-Château",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.47, -121.12),[],302),      
  ("french_castle_20","Château_de_Saint_Germain_Beaupré",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.4, -33.14),[],215),       ### NEW     
  
  ("french_castle_21","Château_de_Virieu",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.62, -47.9),[],155),      
  ("french_castle_22","Château_de_La_Palice",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.9, -24.7),[],86),       ### NEW     
  ("french_castle_23","Château_du_Cheylard",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.99, -96.71),[],109),       ### NEW     
  ("french_castle_24","Château_de_Vaucouleurs",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.55, 59.08),[],337),       ### NEW     
  ("french_castle_25","La_Tour_de_Marmande",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.9, -15.74),[],18),       ### NEW     

### DAC English Castles
  ("english_castle_1","Château_de_Castelnaud",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.36, -101.32),[],15),      
  ("english_castle_2","Forteresse_de_Rauzan",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.33, -103.59),[],59), 
  ("english_castle_3","Château_de_Montréal",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.85, -84.87),[],294),   
  ("english_castle_4","Château_du_Lude",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.42, 22.44),[],260),          
  ("english_castle_5","Château_de_Nérac",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.04, -120.4),[],14),         
  ("english_castle_6","Château_de_Falaise",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.07, 78.24),[],28),        
  ("english_castle_7","Château-Gaillard",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.21, 86.59),[],260),         
  ("english_castle_8","Château_de_Vendôme",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.06, 26.59),[],287),
  ("english_castle_9","Château_de_Beauvau",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.73, 16.73),[],260),
  ("english_castle_10","Château_Gontier",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.52, 28.97),[],260),
  
  ("english_castle_11","Château_de_Verneuil",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.29, 66.51),[],123),
  ("english_castle_12","Château_de_Mortain",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.65, 67.58),[],46),       ### NEW     
  ("english_castle_13","Château_de_Langoiran",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.36, -111.97),[],335),       ### NEW     
  ("english_castle_14","Forteresse_de_Landiras",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.3, -111.9),[],288),       ### NEW     
  ("english_castle_15","Château_de_Fronsac",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34, -94.45),[],66),       ### NEW     
  ("english_castle_16","Château_de_Montferrand",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.08, -100.6),[],275),       ### NEW     
  ("english_castle_17","Forteresse_de_Blaye",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.59, -83.76),[],336),       ### NEW     
  ("english_castle_18","Château_de_Montbray",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.35, 80.13),[],46),       ### NEW     
  ("english_castle_19","Château_de_Gacé",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.9, 70.4),[],21),       ### NEW     
  ("english_castle_20","Château_de_Sainte-Suzanne",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.34, 43.23),[],46),       ### NEW  
  
  ("english_castle_21","Château_de_Durtal",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.95, 19.07),[],46),       ### NEW     

### DAC Burgundian Castles  
  ("burgundian_castle_1","Château_de_Tonerre",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.01, 24.01),[],353),
  ("burgundian_castle_2","Forteresse_d'Avallon",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.24, 9.63),[],10),
  ("burgundian_castle_3","Château_de_Varenne-lès-Mâcon",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.06, -30.12),[],135),
  ("burgundian_castle_4","Château_de_Toulongeon",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.56, -15.55),[],114),
  ("burgundian_castle_5","Château_de_Ligny-en-Barrois",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.5, 67.88),[],342),
  ("burgundian_castle_6","Château_de_Jonvelle",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.58, 34.5),[],217),
  ("burgundian_castle_7","Forteresse_de_Noyelles",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.81, 125.36),[],45),
  ("burgundian_castle_8","Château_de_Montfort",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.27, 17.37),[],81),
  ("burgundian_castle_9","Forteresse_de_La_Rochepot",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.62, 2.56),[],67),
  ("burgundian_castle_10","Château_de_Vergy",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.04, 9.31),[],25),
  
  ("burgundian_castle_11","Château_de_Brimeu",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.67, 123.1),[],45),
  ("burgundian_castle_12","Château_de_Bellemotte",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.6, 118.84),[],268),
  ("burgundian_castle_13","Forteresse_d'Uytkerke",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.97, 152.06),[],312),
  ("burgundian_castle_14","Château_de_La_Charité-sur-Loire",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.82, 0.09),[],139),
  ("burgundian_castle_15","Forteresse_de_L'Isle_Adam",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.06, 81.68),[],45),
  ("burgundian_castle_16","Château_de_Senlis",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.14, 85.53),[],335),
  ("burgundian_castle_17","Château_de_Montcornet",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.15, 106.48),[],319),
  ("burgundian_castle_18","Château_de_Chimay",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.03, 112.74),[],259),

 ### DAC Breton Castles 
  ("breton_castle_1","Château_de_Fougères",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.11, 55.35),[],307),
  ("breton_castle_2","Châteaubriant",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.82, 28.32),[],207),
  ("breton_castle_3","Château_de_Dinan",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.53, 61.42),[],50),
  ("breton_castle_4","Château_de_Clisson",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.6, 3.91),[],195),
  ("breton_castle_5","Château_de_Josselin",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.79, 42.82),[],108),
  ("breton_castle_6","Forteresse_de_Roch'Morvan",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.16, 62.5),[],45),
    
  ("breton_castle_7","Château_de_Guéméné",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.16, 52.53),[],314),
  ("breton_castle_8","Château_de_Rochefort",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.39, 33.26),[],134),
  ("breton_castle_9","Château_de_Tonquédec",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.83, 73.75),[],233),
  ("breton_castle_10","Château_de_Rosmadec",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.72, 54.94),[],266),
  
  ("breton_castle_11","Château_de_Coëtivy",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.71, 66.68),[],109),
  ("breton_castle_12","Château_de_Trémazan",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.13, 70.29),[],203),
  ("breton_castle_13","Château_de_Kermoysan",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.91, 70.43),[],101),
  ("breton_castle_14","Château_de_Coëtquen",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.26, 63.3),[],13),
  ("breton_castle_15","Château_de_Penhoët",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.89, 66.17),[],306),
  ("breton_castle_16","Château_de_Penmarc'h",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.67, 70.87),[],82),
  ("breton_castle_17","Forteresse_de_Kemperlé",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.2, 45.44),[],197),
  ("breton_castle_18","Château_d'Hen_Bont",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.59, 41.22),[],115),
  ("breton_castle_19","Château_de_Derval",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.24, 26.19),[],45),
  ("breton_castle_20","Château_de_Suscinio",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.38, 24.88),[],334),
  
  ("breton_castle_21","Forteresse_de_Roch'an",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.35, 49.78),[],299),
  ("breton_castle_22","Forteresse_de_Dol",icon_castle_d_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.94, 62.88),[],329),


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC VILLAGES ##############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### DAC French Villages
  
  ("french_village_1", "Lunery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.31, -3.39),[], 244),
  ("french_village_2", "Levet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.61, -8.91),[], 332),
  ("french_village_3", "Ardon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.5, 24.57),[], 130),
  ("french_village_4", "Tigy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.21, 23.86),[], 216),
  ("french_village_5", "Bueil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.46, 7.83),[], 203),
  ("french_village_6", "Chambray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.19, 0.54),[], 204),
  ("french_village_7", "Chasseneuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.94, -26.14),[], 12),
  ("french_village_8", "Chauvigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.22, -32.59),[], 302),
  ("french_village_9", "Puilboreau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.65, -33.14),[], 5),
  ("french_village_10", "Angoulins",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.86, -46.69),[], 289),
    
  ("french_village_11", "Montpensier",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.15, -34.65),[], 320),
  ("french_village_12", "Aubières",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.13, -45.09),[], 219),
  ("french_village_13", "Chemilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.11, -20.4),[], 83),
  ("french_village_14", "Montilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.41, -15.29),[], 100),
  ("french_village_15", "Jussac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.38, -98.16),[], 330),
  ("french_village_16", "Carlat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.01, -106.81),[], 220),
  ("french_village_17", "Dardilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.28, -36.24),[], 36),
  ("french_village_18", "Vienne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.79, -46.2),[], 116),
  ("french_village_19", "Vals",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.31, -85.05),[], 235),
  ("french_village_20", "Ceyssac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.92, -87.53),[], 148),
    
  ("french_village_21", "Le Montat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.57, -115.5),[], 135),
  ("french_village_22", "Vers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.11, -109.58),[], 359),
  ("french_village_23", "Sébazac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.67, -112.84),[], 329),
  ("french_village_24", "Calmont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.68, -122.18),[], 148),
  ("french_village_25", "Gramont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.23, -123.64),[], 319),
  ("french_village_26", "Terraube",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.21, -128.17),[], 130),
  ("french_village_27", "Muret",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.17, -132.36),[], 123),
  ("french_village_28", "Blagnac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.8, -126.83),[], 1),
  ("french_village_29", "Castres",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.61, -133.08),[], 256),
  ("french_village_30", "Limoux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.87, -143.9),[], 308),
    
  ("french_village_31", "Lattes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.44, -132.75),[], 21),
  ("french_village_32", "Vendargues",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.06, -129.73),[], 306),
  ("french_village_33", "Chabeuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.35, -72.78),[], 12),
  ("french_village_34", "Livron",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.51, -78.82),[], 156),
  ("french_village_35", "Missé",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.28, -14.61),[], 206),
  ("french_village_36", "Oiron",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.24, -13),[], 288),
  ("french_village_37", "Fourcroix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.64, 129.23),[], 221),
  ("french_village_38", "Bizencourt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.65, 128.37),[], 109),
  ("french_village_39", "Amilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.55, 31.29),[], 72),
  ("french_village_40", "Mormant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.3, 29.21),[], 19),
    
  ("french_village_41", "Saint-Gondon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.26, 17.16),[], 134),
  ("french_village_42", "Poilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.25, 15.29),[], 232),
  ("french_village_43", "Le_Breuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.94, -29.3),[], 135),
  ("french_village_44", "Odos",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.94, -150.46),[], 92),
  ("french_village_45", "Azay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.56, -2.14),[], 293),
  ("french_village_46", "Issoudun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.96, -10.82),[], 233),
  ("french_village_47", "Fontenay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.86, -30.27),[], 200),
  ("french_village_48", "Tasque",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.32, -137.89),[], 46),
  ("french_village_49", "Blanzac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.9, -79.01),[], 360),
  ("french_village_50", "Chélieu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.9, -45.6),[], 10),
    
  ("french_village_51", "La Crête",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.74, -26.97),[], 100),
  ("french_village_52", "Amboise",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.07, 10.38),[], 255),
  ("french_village_53", "Boussac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.6, -29.21),[], 100),
  ("french_village_54", "Yèvre",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.03, 41.21),[], 10),
  ("french_village_55", "Aix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.52, -60.5),[], 221),
  ("french_village_56", "Tauves",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.26, -53.65),[], 32),
  ("french_village_57", "Jalognes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.73, 2.88),[], 112),
  ("french_village_58", "Geaune",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.41, -138.89),[], 235),
  ("french_village_59", "Pavie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.37, -141),[], 212),
  ("french_village_60", "Le Val-Saint-Père",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.76, 69.03),[], 325),
    
  ("french_village_61", "Vellèches",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.85, -18.9),[], 224),
  ("french_village_62", "Azerables",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.75, -29.6),[], 23),
  ("french_village_63", "Sévérac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.96, -123.85),[], 243),
  ("french_village_64", "Xaintrailles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.28, -116.68),[], 80),
  ("french_village_65", "Domrémy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.91, 52.03),[], 269),
  ("french_village_66", "Barbazan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.6, -151.88),[], 233), 
  ("french_village_67", "Mont-de-Marsan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.32, -132.13),[], 251),
  ("french_village_68", "Ròcahòrt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.98, -125.15),[], 218),  
  ("french_village_69", "Brassac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.13, -149.42),[], 115),  
  ("french_village_70", "Vernajoul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.64, -146.38),[], 340),  
    
  ("french_village_71", "Aujac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.02, -95.26),[], 73),  
  ("french_village_72", "Le_Pailloux",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.66, -61.23),[], 204),  
  ("french_village_73", "Murol",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.16, -66.02),[], 181),
  ("french_village_74", "Brissac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.1, 7.19),[], 148),
  ("french_village_75", "Lembras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.94, -96.44),[], 176),   
  
### DAC English Villages 

  ("english_village_1", "Monbazillac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.15, -102.33),[], 36),
  ("english_village_2", "Chammes",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.58, 40.95),[], 322),
  ("english_village_3", "Chancelade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.29, -76.25),[], 63),
  ("english_village_4", "Trélissac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8, -75.07),[], 290),
  ("english_village_5", "Champniers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.86, -59.57),[], 315),
  ("english_village_6", "La Couronne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.64, -67.42),[], 125),
  ("english_village_7", "Rochechouart",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.97, -55.21),[], 119),
  ("english_village_8", "Couzeix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.36, -49.9),[], 335),
  ("english_village_9", "Mérignac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.97, -105.03),[], 60),
  ("english_village_10", "Pessac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.55, -108.08),[], 135),

  ("english_village_11", "Vignoles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.6, -126.52),[], 22),
  ("english_village_12", "Blaye",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.03, -85.63),[], 295),
  ("english_village_13", "Anglet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.2, -139.34),[], 253),
  ("english_village_14", "Biarritz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.54, -144.77),[], 135),
  ("english_village_15", "Peyrehorade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.45, -139.62),[], 124),
  ("english_village_16", "Castets",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.61, -130.8),[], 27),
  ("english_village_17", "Entrammes",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.97, 40.43),[], 328),
  ("english_village_18", "Argentré",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.02, 46.38),[], 167),
  ("english_village_19", "Allonnes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.38, 36.07),[], 299),
  ("english_village_20", "Mulsannes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.65, 35.14),[], 29),

  ("english_village_21", "Le Lion-d'Angers",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.78, 18.89),[], 24),
  ("english_village_22", "Durtal",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.36, 21.3),[], 230),
  ("english_village_23", "Chailly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.88, 62.67),[], 352),
  ("english_village_24", "Ury",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.1, 57.19),[], 82),
  ("english_village_25", "Gasville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.02, 56.15),[], 125),
  ("english_village_26", "Luisant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.76, 50.23),[], 324),
  ("english_village_27", "Barentin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.15, 95.14),[], 202),
  ("english_village_28", "Quevilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.97, 88.35),[], 31),
  ("english_village_29", "Rots",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.36, 89.87),[], 91),
  ("english_village_30", "Ifs",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.89, 86.72),[], 186),

  ("english_village_31", "Honfleur",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.24, 94.22),[], 165),
  ("english_village_32", "Étretat",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.66, 107.1),[], 227),
  ("english_village_33", "Barfleur",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.36, 114.78),[], 80),
  ("english_village_34", "Valognes",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.29, 106.44),[], 309),
  ("english_village_35", "Fréthun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.06, 144.86),[], 109),
  ("english_village_36", "Marck",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.89, 145.82),[], 265),
  ("english_village_37", "Saint-Denis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.14, 76.94),[], 329),
  ("english_village_38", "Evry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.09, 72.75),[], 286),
  ("english_village_39", "Arçonnay",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.57, 52.71),[], 344),
  ("english_village_40", "Valframbert",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.01, 58.81),[], 174),

  ("english_village_41", "Nonant",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.63, 94.08),[], 239),
  ("english_village_42", "Balleroy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.35, 93.88),[], 131),
  ("english_village_43", "Bailleul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.04, 70),[], 176),
  ("english_village_44", "Ecouché",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.05, 63.99),[], 104),
  ("english_village_45", "Brive",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.77, -95.9),[], 205),
  ("english_village_46", "Ruch",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.28, -104.73),[], 340),
  ("english_village_47", "Mussidan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.6, -83.17),[], 32),
  ("english_village_48", "Le_Lude",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.36, 20.05),[], 337),
  ("english_village_49", "Barbaste",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.61, -118.74),[], 35),
  ("english_village_50", "Corny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.9, 88.58),[], 216),

  ("english_village_51", "Aubigny",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.14, 80.89),[], 202),
  ("english_village_52", "Bazas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.14, -113.86),[], 146),
  ("english_village_53", "Ménil",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.26, 26.38),[], 318),
  ("english_village_54", "Vendôme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.43, 24.73),[], 168),
  ("english_village_55", "Beauvau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.3, 14.45),[], 9),
  ("english_village_56", "Langoiran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.15, -110.32),[], 23),
  ("english_village_57", "Mortain",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.64, 69.72),[], 150),
  ("english_village_58", "Lessay",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.97, 94.86),[], 75),
  ("english_village_59", "Orval",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.04, 86.12),[], 229),

  ("english_village_60", "Hambye",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.95, 79.15),[], 176),
  ("english_village_61", "Vire",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.85, 77.93),[], 343),
  ("english_village_62", "Sartilly",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.06, 75.14),[], 49),  
  ("english_village_63", "Verneuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.8, 69.23),[], 169),
  ("english_village_64", "L'Aigle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2, 66.05),[], 268),
  ("english_village_65", "Dieppe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.38, 115.95),[], 198),
  ("english_village_66", "Blangy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.47, 112.09),[], 100),
  ("english_village_67", "Pont-Hébert",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.47, 94.85),[], 27),
  ("english_village_68", "Condé",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.66, 89.85),[], 127),
  ("english_village_69", "Fronsac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.31, -96.15),[], 79),

  ("english_village_70", "Pomerol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.68, -94.37),[], 268),
  ("english_village_71", "Beychac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.57, -100.37),[], 187),
  ("english_village_72", "Ambarès",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.54, -102.19),[], 309),
  ("english_village_73", "Domme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.3, -103.12),[], 100),    

### DAC Burgundian Villages
  ("burgundian_village_1", "Quetigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.6, 18.14),[], 84),
  ("burgundian_village_2", "Quenne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.23, 18.71),[], 281),
  ("burgundian_village_3", "Charbuy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.84, 23.07),[], 357),
  ("burgundian_village_4", "Macey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.66, 50.93),[], 18),
  ("burgundian_village_5", "Rouilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.67, 46.92),[], 233),
  ("burgundian_village_6", "Rougemont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.41, 16.92),[], 28),
  ("burgundian_village_7", "Baume-les-Dames",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.51, 12.98),[], 225),
  ("burgundian_village_8", "Balleray",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.74, -6.32),[], 339),
  ("burgundian_village_9", "Imphy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.71, -12.11),[], 172),
  ("burgundian_village_10", "Damme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.45, 149.03),[], 291),
  
  ("burgundian_village_11", "Bourgogne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.85, 144.46),[], 112),
  ("burgundian_village_12", "Audenarde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.63, 137.11),[], 166),
  ("burgundian_village_13", "Nevele",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.6, 143.3),[], 285),
  ("burgundian_village_14", "Verbrande",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.27, 138.93),[], 157),
  ("burgundian_village_15", "Tisselt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.16, 144.89),[], 308),
  ("burgundian_village_16", "Thourotte",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.77, 90.84),[], 74),
  ("burgundian_village_17", "Jaux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.06, 94.28),[], 312),
  ("burgundian_village_18", "Sarry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.37, 78.45),[], 304),
  ("burgundian_village_19", "Vertus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.42, 73.47),[], 120),
  ("burgundian_village_20", "Rethel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.22, 95.18),[], 313),
  
  ("burgundian_village_21", "Epernay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.95, 85.42),[], 124),
  ("burgundian_village_22", "Condette",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.63, 130.74),[], 136),
  ("burgundian_village_23", "Wimeureux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.97, 136.72),[], 318),
  ("burgundian_village_24", "Ligny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.87, 115.44),[], 302),
  ("burgundian_village_25", "Picquigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.48, 105.15),[], 205),
  ("burgundian_village_26", "Allaines",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.84, 107.34),[], 140),
  ("burgundian_village_27", "Biaches",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.82, 105.62),[], 302),
  ("burgundian_village_28", "Ancy-le-Franc",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.7, 22.39),[], 319),
  ("burgundian_village_29", "Magny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.71, 8.29),[], 268),
  ("burgundian_village_30", "Macôn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.7, -26.83),[], 314),
  
  ("burgundian_village_31", "Toulongeon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.06, -13.4),[], 340),
  ("burgundian_village_32", "Givrauval",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.61, 65.45),[], 190),
  ("burgundian_village_33", "Jonvelle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.53, 32.5),[], 184),
  ("burgundian_village_34", "Godault",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.95, 123.28),[], 245),
  ("burgundian_village_35", "Montigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.64, 15.7),[], 225),
  ("burgundian_village_36", "Beaune",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.25, -0.29),[], 202),
  ("burgundian_village_37", "Reulle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.82, 6.65),[], 166),
  ("burgundian_village_38", "Grigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25, 120.03),[], 240),
  ("burgundian_village_39", "Arras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.49, 118.51),[], 112),
  ("burgundian_village_40", "Bredene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.4, 150.18),[], 103),
  
  ("burgundian_village_41", "Donzy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.53, 2.93),[], 342),
  ("burgundian_village_42", "Mours",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.9, 83.06),[], 306),
  ("burgundian_village_43", "Barbery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.2, 86.75),[], 165),
  ("burgundian_village_44", "Montcornet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.75, 103.99),[], 201),
  ("burgundian_village_45", "Beaumont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.17, 118.29),[], 19),
  ("burgundian_village_46", "Chenôve",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.07, 13.93),[], 124),  
  
### DAC Breton Villages 
  ("breton_village_1", "Blain",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.25, 21.38),[], 148),
  ("breton_village_2", "Treillières",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.71, 15.77),[], 344),
  ("breton_village_3", "Lohéac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.97, 39.72),[], 351),
  ("breton_village_4", "Vitré",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.57, 48.43),[], 355),
  ("breton_village_5", "Auray",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.62, 31.33),[], 82),
  ("breton_village_6", "Malestroit",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.58, 33.59),[], 15),
  ("breton_village_7", "Aleth",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.53, 66.04),[], 246),
  ("breton_village_8", "Dinard",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.39, 68.28),[], 100),
  ("breton_village_9", "Roscoff",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.68, 77.55),[], 167),
  ("breton_village_10", "Carantec",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.66, 74.16),[], 147),
  
  ("breton_village_11", "Pont-l'Abbé",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.41, 48.05),[], 305),
  ("breton_village_12", "Audierne",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.87, 49.95),[], 321),
  ("breton_village_13", "Pont-Ivy",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.69, 53.92),[], 93),
  ("breton_village_14", "Loudéac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.83, 57.04),[], 327),
  ("breton_village_15", "Trégueux",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.91, 64.48),[], 200),
  ("breton_village_16", "Lamballe",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.77, 62.74),[], 274),
  ("breton_village_17", "Trémazan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.53, 71.3),[], 232),
  ("breton_village_18", "Guérande",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.91, 14.32),[], 359),
  ("breton_village_19", "Beaumanoir",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.89, 59.78),[], 235),
  ("breton_village_20", "Romagné",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.16, 55.72),[], 89),
  
  ("breton_village_21", "Rouge",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.33, 30.98),[], 56),
  ("breton_village_22", "Vallet",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.97, 7.26),[], 20),
  ("breton_village_23", "Hélléan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.92, 45.59),[], 318),
  ("breton_village_24", "Landerneau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.28, 62.05),[], 196),
  ("breton_village_25", "Lignol",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.08, 51.37),[], 108),
  ("breton_village_26", "Lannion",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.45, 75.94),[], 212),
  ("breton_village_27", "Telgruc",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.22, 57.52),[], 47),
  ("breton_village_28", "Saint-Renan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.02, -100.38),[], 257),
  ("breton_village_29", "Kersaint",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.16, 64.56),[], 49),
  ("breton_village_30", "Paimpol",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.63, 77.2),[], 110),
  
  ("breton_village_31", "Miniac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.61, 64.8),[], 72),
  ("breton_village_32", "Morlaix",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.68, 72.23),[], 236),
  ("breton_village_33", "Plouguerneau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.52, 74.12),[], 17),
  ("breton_village_34", "Bieuzy",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.67, 48.83),[], 96),
  ("breton_village_35", "Languidic",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.77, 42.97),[], 296),
  ("breton_village_36", "Sarzeau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.3, 23.74),[], 356),
  ("breton_village_37", "Combourg",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.31, 58.28),[], 154),
  ("breton_village_38", "Redon",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.78, 27.59),[], 351),
  ("breton_village_39", "Le_Faouët",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.09, 49.01),[], 25),
  
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65, -105),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.13, -112.41),[], 207),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.64, -67.59),[], 235),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.84, 103.93),[], 231),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.97, -100.44),[], 89),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.96, 33.1),[], 230),


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.64, 27.7),[], 345),
  ("Bridge_2","{!}2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.96, -124.52),[], 67),
  ("Bridge_3","{!}3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.21, 90.5),[], 16),
  ("Bridge_4","{!}4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.6, -97.48),[], 359),
  ("Bridge_5","{!}5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.76, 62.07),[], 353),
  ("Bridge_6","{!}6",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.5, 0.71),[], 343),
  ("Bridge_7","{!}7",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.67, -7.69),[], -64),
  ("Bridge_8","{!}8",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.35, 41.27),[], 286),
  ("Bridge_9","{!}9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.31, -99.1),[], 270),
  ("Bridge_10","{!}10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.74, 4.21),[], 18),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0,(-16.92,-134.55), [], 95.0),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.59, -8.94),[], 297),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.44, 11.3),[], 356),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.03, -105.32),[], 108),

#  Bandit Spawn Points
  # ("plains_bandit_spawn_point_1"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(25.5, -48),[(trp_looter,15,0)]),
  # ("plains_bandit_spawn_point_2"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.5, -18.4),[(trp_looter,15,0)]),
  # ("steppe_bandit_spawn_point_1"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(109, -15),[(trp_looter,15,0)]),
  # ("steppe_bandit_spawn_point_2"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(152.5, 10.1),[(trp_looter,15,0)]),
  # ("taiga_bandit_spawn_point_1"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(84.3, 44.5),[(trp_looter,15,0)]),
  # ("taiga_bandit_spawn_point_2"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(87.5, 85.4),[(trp_looter,15,0)]),
  # ("forest_bandit_spawn_point_1"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  # ("forest_bandit_spawn_point_2"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-121.6, 20.4),[(trp_looter,15,0)]),
  # ("mountain_bandit_spawn_point_1","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-90, -26.8),[(trp_looter,15,0)]),
  # ("mountain_bandit_spawn_point_2","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-54, -89),[(trp_looter,15,0)]),
  # ("sea_raider_spawn_point_1"     ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.5, 110),[(trp_looter,15,0)]),
  # ("sea_raider_spawn_point_2"     ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  # ("desert_bandit_spawn_point_1"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, -105),[(trp_looter,15,0)]),
  # ("desert_bandit_spawn_point_2"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(66, -116),[(trp_looter,15,0)]),
  
### Bandit Spawn Points
# Routiers
  ("routier_bandit_spawn_point_1"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(80, 114),[(trp_looter,15,0)]),
  ("routier_bandit_spawn_point_2"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(25, -130),[(trp_looter,15,0)]),
 # Flayers
  ("flayer_bandit_spawn_point_1"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-16, -42),[(trp_looter,15,0)]),
  ("flayer_bandit_spawn_point_2"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(17, 11),[(trp_looter,15,0)]),
 # Retondeurs
  ("retondeur_bandit_spawn_point_1"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(60, 80),[(trp_looter,15,0)]),
  ("retondeur_bandit_spawn_point_2"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(90, 0),[(trp_looter,15,0)]),
 # Tard-Venus
  ("tard_venus_bandit_spawn_point_1"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(100, 36),[(trp_looter,15,0)]),
  ("tard_venus_bandit_spawn_point_2"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(120, -60),[(trp_looter,15,0)]),
 # Angry Plebs
  ("peasant_bandit_spawn_point_1"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-50, 40),[(trp_looter,15,0)]),
  ("peasant_bandit_spawn_point_2"  ,"the plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(5, 45),[(trp_looter,15,0)]),

  
  # add extra towns before this point 
  ("spawn_points_end"             ,"{!}last_spawn",pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]), 

  # Used by Warband ARray Processing
  ("warp_output"                 ,"{!}WARP_output_array",pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[]),
  ("warp_temp"                   ,"{!}WARP_temp_array",  pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[]),

## DAC Seek: Player Camp
  ("player_camp", "Mercenary Company",  icon_camp|pf_disabled|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10, -100),[], 0),
## DAC Seek: Player Camp End

  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("static_parties_end"          ,"{!}reserved",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ]
