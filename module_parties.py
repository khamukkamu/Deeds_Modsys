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
    ("french_town_1","Bourges",  icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.41, -1.14),[], 171),                            
    ("french_town_2","Orléans",     icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.68, 35.97),[], 2),            
    ("french_town_3","Tours",   icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.49, 14.79),[], 354),                             
    ("french_town_4","Poitiers",     icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.59, -18.76),[], 356),                      
    ("french_town_5","La_Rochelle",  icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.34, -35.85),[], 323),                   
    ("french_town_6","Clermont",   icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.48, -58.31),[], 233),   
    ("french_town_7","Moulins",   icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.19, -27.06),[], 314),                          
    ("french_town_8","Aurillac", icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.32, -93.57),[], 267),                        
    ("french_town_9","Lyon",   icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.88, -61.22),[], 330),     
    ("french_town_10","Le_Puy",   icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.5, -87.12),[], 291),                          

    ("french_town_11","Cahors", icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.45, -109.61),[], 68),                           
    ("french_town_12","Rodez",icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.97, -116.27),[], 292),                            
    ("french_town_13","Lectoure",  icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.11, -134.03),[], 41),                         
    ("french_town_14","Tarbes",  icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.36, -165.67),[], 302),                        
    ("french_town_15","Toulouse",  icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.06, -146.77),[], 267),                          
    ("french_town_16","Carcassonne", icon_town_b_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.81, -166.46),[], 153),                       
    ("french_town_17","Montpellier", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.98, -150.31),[], 20),                       
    ("french_town_18","Valence", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.11, -97.04),[], 352),                          
    ("french_town_19","Thouars", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.01, -3.02),[], 276),                          
    ("french_town_20","Tournai", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.38, 147.42),[], 139),                          

    ("french_town_21","Gien", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.9, 26.17),[], 319),                               
    ("french_town_22","Montargis-le-Franc", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.12, 39.01),[], 43),      
    ("french_town_23","Nîmes", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.92, -142),[], 208),       
    ("french_town_24","Bergerac", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.35, -92.52),[], 335),            
    ("french_town_25","Périgueux", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.98, -79.61),[], 190),       
    ("french_town_26","Angoulême", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.09, -61.05),[], 240),     
    ("french_town_27","Limoges", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.1, -52.62),[], 269),            
    ("french_town_28","Angers", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.3, 20.91),[], 337),     
    ("french_town_29","Foix", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.68, -175.63),[], 147),         

 ### DAC English Towns
    ("english_town_1","Paris", icon_town_paris|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.14, 77.38),[], 331),                     
    ("english_town_2","Bayonne", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.59, -147.81),[], 232),   
    ("english_town_3","Nemours", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.05, 55.72),[], 3),      
    ("english_town_4","Laval", icon_town_b_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.93, 48.03),[], 82),          
    ("english_town_5","Le_Mans", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.87, 43.46),[], 151),              
    ("english_town_6","Bordeaux", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.04, -91.63),[], 38),  
    ("english_town_7","Chartres", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.26, 62.05),[], 38),    
    ("english_town_8","Rouen", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.24, 103.08),[], 145),     
    ("english_town_9","Caen", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.38, 95.59),[], 31),                  
    ("english_town_10","Harfleur", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.26, 109.01),[], 303),  
    
    ("english_town_11","Cherbourg", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.54, 115.27),[], 8),            
    ("english_town_12","Bayeux", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.93, 100.48),[], 17),              
    ("english_town_13","Calais", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.88, 167.23),[], 193),
    ("english_town_14","Alençon", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.41, 64.57),[], 18),              
    ("english_town_15","Argentan", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.23, 74.57),[], 25),             
    ("english_town_16","Tartas", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.11, -128.63),[], 200), 
    ("english_town_17","Dax", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.75, -134.41),[], 40),     
    ("english_town_18","Libourne", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.91, -88.17),[], 325),
    ("english_town_19","Saint-Lô", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.03, 88.08),[], 220),      
    ("english_town_20","Eu", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.79, 133.73),[], 48),      
    
    ("english_town_21","Avranches", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.63, 70.15),[], 225),   
    ("english_town_22","Coutances", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.07, 92.79),[], 17),    

 ### DAC Burgundian Towns
    ("burgundian_town_1","Dijon", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125.39, 14.07),[], 242),     
    ("burgundian_town_2","Besançon", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156.25, -0.21),[], 2),  
    ("burgundian_town_3","Nevers", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.5, -6.3),[], 91),      
    ("burgundian_town_4","Auxerre", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.02, 29.22),[], 128),  
    ("burgundian_town_5","Troyes", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.07, 57.03),[], 51),   
    ("burgundian_town_6","Compiègne", icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.03, 97.44),[], 12),   
    ("burgundian_town_7","Bruges", icon_town_b_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.61, 179.65),[], 218),  
    ("burgundian_town_8","Gand", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.54, 172.32),[], 97),     
    ("burgundian_town_9","Malines", icon_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.12, 165.7),[], 227),            
    ("burgundian_town_10","Boulogne", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.95, 155.54),[], 52),
    
    ("burgundian_town_11","Châlons-en-Champagne", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.79, 82.32),[], 209),           
    ("burgundian_town_12","Reims", icon_town_a_southern_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.02, 94.75),[], 303),                            
    ("burgundian_town_13","Amiens",icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.15, 124.68),[],329),               
    ("burgundian_town_14","Péronne",icon_town_a_southern|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.42, 126.62),[],345),
    ("burgundian_town_15","Provins", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78, 65),[], 200),   
    
### DAC Breton Towns
    ("breton_town_1","Rennes", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.68, 51.24),[], 192),                          
    ("breton_town_2","Nantes", icon_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.05, 12.7),[], 278),                           
    ("breton_town_3","Vannes", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.39, 33.41),[], 13),                          
    ("breton_town_4","Kemper", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.03, 50.07),[], 211),
    ("breton_town_5","Saint-Malo", icon_town_b_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.93, 73.9),[], 354),          
    ("breton_town_6","Saint-Brieuc", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.15, 72.52),[], 153),                  
    ("breton_town_7","Saint-Pol-de-Léon", icon_town_a_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.96, 77.55),[], 326),            
    ("breton_town_8","Rohan", icon_town_b_breton|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.05, 53.68),[], 27),                          

   
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CASTLES ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### DAC French Castles
  ("french_castle_1","Forteresse_de_Chinon",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.75, 6.88),[],306),        
  ("french_castle_2","Châteauroux",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.51, -21.01),[],56),                
  ("french_castle_3","Château de Niort",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.43, -31.82),[],255),   
  ("french_castle_4","La Tour_de_Termes",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.22, -136.68),[],210),         
  ("french_castle_5","Château_de_Murol",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.16, -71.59),[],280),            
  ("french_castle_6","Château_de_Polignac",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.52, -80.1),[],30),           
  ("french_castle_7","Château_de_Culant",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.11, -23.49),[],3),            
  ("french_castle_8","Château_de_Montrichard",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.93, 10.15),[],84),         
  ("french_castle_9","Château_de_Boussac",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.38, -27.81),[],64),            
  ("french_castle_10","Yèvre-le-Châtel",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.36, 45.67),[],209),    
  
  ("french_castle_11","Château_de_La_Fayette",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.43, -76.38),[],285), 
  ("french_castle_12","La_Tour_d'Auvergne",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.19, -76.3),[],269),           
  ("french_castle_13","Château_de_Charlus",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.29, -87.72),[],46),      
  ("french_castle_14","Château_de_Sancerre",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.77, 17.73),[],268),         
  ("french_castle_15","Château_de_Tiffauges",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.02, 2.22),[],108),           
  ("french_castle_16","Forteresse_d'Auch",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.46, -143.81),[],7),            
  ("french_castle_17","Mont-St-Michel",icon_mont_st_michel|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.46, 74.82),[],220),              
  ("french_castle_18","Château_de_Turenne",icon_castle_d_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.61, -91.15),[],360),           
  ("french_castle_19","Sévérac-le-Château",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.73, -115.63),[],302),       
  ("french_castle_20","Château-Guillaume",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.27, -29.59),[],215),       
  
  ("french_castle_21","Château_de_Virieu",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.18, -67.61),[],155),      
  ("french_castle_22","Château_de_La_Palice",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.24, -41.12),[],86),       
  ("french_castle_23","Château_du_Cheylard",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.65, -94.54),[],109),       
  ("french_castle_24","Château_de_Loches",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.95, -1.4),[],337),       
  ("french_castle_25","La_Tour_de_Marmande",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.28, -1.08),[],18),       
  ("french_castle_26","Château_de_Amboise",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.71, 15.69),[],274),       
  ("french_castle_27","Château_de_Vaujours",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.46, 19.97),[],134), 
  ("french_castle_28","Château_de_Lusignan",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.08, -28.31),[],219), 
  ("french_castle_29","Château_de_Sully-sure-Loire",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.79, 28),[],219),  
  ("french_castle_30","Château_de_Montaner",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.41, -154.45),[],219),  

  ("french_castle_31","Château_de_Albret",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.13, -118.43),[],219),   
  ("french_castle_32","Château_de_Najac",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23, -120),[],219),   

### DAC English Castles
  ("english_castle_1","Château_de_Castelnaud",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.04, -97.49),[],15),       #[swycartographr] prev. coords: (29.77, -87.69) #[swycartographr] prev. coords: (-1.36, -101.32) #[swycartographr] prev. coords: (37.6, -100.17) #[swycartographr] prev. coords: (17.22, -96.14)
  ("english_castle_2","Forteresse_de_Rauzan",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.65, -98.99),[],59),  #[swycartographr] prev. coords: (-25.33, -103.59)
  ("english_castle_3","Château_de_Montréal",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.37, -83.04),[],294),    #[swycartographr] prev. coords: (-21.39, -80.52) #[swycartographr] prev. coords: (-4.69, -78.33)
  ("english_castle_4","Château_du_Gisors",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33, 100.22),[],260),           #[swycartographr] prev. coords: (-11.48, 25.86)
  ("english_castle_5","Château_de_Nérac",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.32, -121.11),[],14),          #[swycartographr] prev. coords: (-23.66, -125.08) #[swycartographr] prev. coords: (-28.04, -120.4) #[swycartographr] prev. coords: (-30.7, -121.96)
  ("english_castle_6","Château_de_Falaise",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.69, 84.1),[],28),        
  ("english_castle_7","Château-Gaillard",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.36, 97.71),[],260),         
  ("english_castle_8","Château_de_Vendôme",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.21, 36.08),[],287), #[swycartographr] prev. coords: (10.06, 40.4)
  ("english_castle_9","Château_de_Royan",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.49, -61.25),[],260), #[swycartographr] prev. coords: (-28, 21.67)
  ("english_castle_10","Bastille_Saint-Antoine",icon_castle_bastille|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.31, 78.76),[],347), #[swycartographr] prev. coords: (48.2, 78.59) rot: 260 #[swycartographr] prev. coords: (-44.28, 29.67) #[swycartographr] prev. coords: (48.56, 78.38) rot: 332
  
  ("english_castle_11","Château_de_Verneuil",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.32, 76.97),[],34),  #[swycartographr] prev. coords: (9.32, 76.97) rot: 123
  ("english_castle_12","Château_de_Mortain",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.14, 68.03),[],46),       ### NEW     
  ("english_castle_13","Château_de_Langoiran",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.88, -106.64),[],335),       ### NEW      #[swycartographr] prev. coords: (-30.36, -111.97)
  ("english_castle_14","Forteresse_de_Landiras",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.88, -105.54),[],288),       ### NEW      #[swycartographr] prev. coords: (-42.3, -111.9)
  ("english_castle_15","Château_de_Fronsac",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.31, -83.32),[],66),       ### NEW      #[swycartographr] prev. coords: (-34, -94.45) #[swycartographr] prev. coords: (-34.89, -81.62)
  ("english_castle_16","Château_de_Montferrand",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.97, -97.94),[],275),       ### NEW     
  ("english_castle_17","Château des Rudel",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.93, -77.39),[],336),       ### NEW      #[swycartographr] prev. coords: (-45.17, -71)
  ("english_castle_18","Château_de_Montbray",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.76, 81.46),[],46),       ### NEW      #[swycartographr] prev. coords: (-53.35, 80.13)
  ("english_castle_19","Château_de_Gacé",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.98, 78.27),[],21),       ### NEW     
  ("english_castle_20","Château_de_Sainte-Suzanne",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.03, 50.66),[],46),       ### NEW   #[swycartographr] prev. coords: (-28.73, 49.13)
  
  ("english_castle_21","Château_de_Durtal",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.6, 26.36),[],46),       ### NEW     
  ("english_castle_22","Château_de_Vincennes",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.32, 77.63),[],232),       ### NEW      #[swycartographr] prev. coords: (31.66, 72.39) #[swycartographr] prev. coords: (49.78, 77.94) #[swycartographr] prev. coords: (50.53, 77.9) #[swycartographr] prev. coords: (51.95, 77.27) rot: 46 #[swycartographr] prev. coords: (51.95, 77.27) rot: 212
  ("english_castle_23","Château_de_Harcourt",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.34, 92.12),[],45), #[swycartographr] prev. coords: (-73.59, 31.3) #[swycartographr] prev. coords: (0.49, 91.89)
  ("english_castle_24","Château_d'Arques-la-Bataille",icon_castle_d_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.02, 122.06),[],45),  #[swycartographr] prev. coords: (0.49, 91.89) #[swycartographr] prev. coords: (15.87, 122.11)
  ("english_castle_25","Château_de_Saint-Jean",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.61, 55.46),[],45),   #[swycartographr] prev. coords: (15.87, 122.11)

### DAC Burgundian Castles  
  ("burgundian_castle_1","Château_d'Étaples",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.81, 148.33),[],353), #[swycartographr] prev. coords: (100.35, 41.61) #[swycartographr] prev. coords: (95.01, 24.01) #[swycartographr] prev. coords: (95.34, 38.04) #[swycartographr] prev. coords: (96.78, 32.15)
  ("burgundian_castle_2","Château_de_Chastellux",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.6, 12.85),[],10), #[swycartographr] prev. coords: (84.24, 9.63) #[swycartographr] prev. coords: (93.3, 16.54)
  ("burgundian_castle_3","Château_de_Varenne-lès-Mâcon",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.63, -32.39),[],135), #[swycartographr] prev. coords: (108.06, -30.12)
  ("burgundian_castle_4","Château_de_Toulongeon",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.34, -21.95),[],114), #[swycartographr] prev. coords: (96.56, -15.55)
  ("burgundian_castle_5","Château_de_Ligny-en-Barrois",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.85, 75.16),[],342),
  ("burgundian_castle_6","Château_de_Jonvelle",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.44, 40.28),[],217),
  ("burgundian_castle_7","Forteresse_de_Noyelles",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.98, 138.33),[],45),
  ("burgundian_castle_8","Château_de_Montfort",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.33, 27.44),[],81), #[swycartographr] prev. coords: (97.27, 17.37) #[swycartographr] prev. coords: (110.04, 26.47) #[swycartographr] prev. coords: (109.1, 35.95)
  ("burgundian_castle_9","Forteresse_de_La_Rochepot",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.64, -12.09),[],67), #[swycartographr] prev. coords: (101.62, 2.56) #[swycartographr] prev. coords: (111.32, -7.39)
  ("burgundian_castle_10","Château_de_Vergy",icon_castle_c_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.26, 4.02),[],25), #[swycartographr] prev. coords: (108.04, 9.31) #[swycartographr] prev. coords: (119.95, 13.16)
  
  ("burgundian_castle_11","Château_de_Brimeu",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.31, 144.54),[],45), #[swycartographr] prev. coords: (43.25, 142.71)
  ("burgundian_castle_12","Château_de_Bellemotte",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.92, 148.59),[],268),
  ("burgundian_castle_13","Château_du_Pellegrin",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.87, 171.97),[],312),
  ("burgundian_castle_14","Château_de_La_Charité-sur-Loire",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.63, -13.72),[],139), #[swycartographr] prev. coords: (61.82, 0.09)
  ("burgundian_castle_15","Château_de_Coucy",icon_castle_coucy|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.53, 102.16),[],293), #[swycartographr] prev. coords: (27.24, 87.48) #[swycartographr] prev. coords: (73.55, 102.2) rot: 45 #[swycartographr] prev. coords: (73.55, 102.2)
  ("burgundian_castle_16","Château_de_Senlis",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.09, 89.17),[],335), #[swycartographr] prev. coords: (57, 90.32)
  ("burgundian_castle_17","Château_de_Montcornet",icon_castle_a_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.03, 113.01),[],319),
  ("burgundian_castle_18","Château_de_Chimay",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.78, 141.69),[],259),
  ("burgundian_castle_19","Château_de_Pierrefonds",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.52, 90.62),[],293), #[swycartographr] prev. coords: (27.24, 87.48) #[swycartographr] prev. coords: (73.55, 102.2) rot: 45 #[swycartographr] prev. coords: (73.55, 102.2) #[swycartographr] prev. coords: (64.75, 90.77)
  ("burgundian_castle_20","Château_de_Dourdan",icon_castle_c_southern_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.48, 66.22),[],293), #[swycartographr] prev. coords: (27.24, 87.48) #[swycartographr] prev. coords: (73.55, 102.2) rot: 45 #[swycartographr] prev. coords: (73.55, 102.2) #[swycartographr] prev. coords: (64.75, 90.77)
  ("burgundian_castle_21","Château_d'Étampes",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.13, 56.7),[],293), #[swycartographr] prev. coords: (27.24, 87.48) #[swycartographr] prev. coords: (73.55, 102.2) rot: 45 #[swycartographr] prev. coords: (73.55, 102.2) #[swycartographr] prev. coords: (64.75, 90.77)
  ("burgundian_castle_22","Château_de_Brancion",icon_castle_b_southern|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125.89, -9.84),[],293),  #[swycartographr] prev. coords: (43.13, 56.7)

 ### DAC Breton Castles 
  ("breton_castle_1","Château_de_Fougères",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.65, 59.29),[],307),
  ("breton_castle_2","Châteaubriant",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.3, 33.66),[],207),
  ("breton_castle_3","Château_de_Dinan",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.53, 58.22),[],50),
  ("breton_castle_4","Château_de_Clisson",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.09, 7.17),[],195),
  ("breton_castle_5","Château_de_Josselin",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.96, 43.51),[],108),
  ("breton_castle_6","Forteresse_de_Roch'Morvan",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.53, 70.92),[],45),
    
  ("breton_castle_7","Château_de_Guéméné",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.37, 52.68),[],314),
  ("breton_castle_8","Château_de_Rochefort",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.51, 36.42),[],54), #[swycartographr] prev. coords: (-78.4, 36.32) rot: 134
  ("breton_castle_9","Château_de_Tonquédec",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.96, 78.63),[],233),
  ("breton_castle_10","Château_de_Rosmadec",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.11, 58.98),[],266),
  
  ("breton_castle_11","Château_de_Coëtivy",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.56, 74.62),[],109),
  ("breton_castle_12","Château_de_Trémazan",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.61, 72.31),[],203),
  ("breton_castle_13","Château_de_Kermoysan",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.53, 77.43),[],101),
  ("breton_castle_14","Château_de_Montmuran",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.98, 55.45),[],13), #[swycartographr] prev. coords: (-80.37, 55.55)
  ("breton_castle_15","Château_de_Penhoët",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.59, 69.39),[],306),
  ("breton_castle_16","Château_de_Penmarc'h",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.08, 70.22),[],82),
  ("breton_castle_17","Forteresse_de_Kemperlé",icon_castle_b_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.8, 45.99),[],197),
  ("breton_castle_18","Château_d'Hen_Bont",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.44, 38.74),[],115),
  ("breton_castle_19","Château_de_Derval",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.59, 31.3),[],45),
  ("breton_castle_20","Château_de_Suscinio",icon_castle_a_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.75, 26.75),[],334),
  
  ("breton_castle_21","Château_de_Saint_Mesmin",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.11, -8.35),[],299), #[swycartographr] prev. coords: (-102.51, 48.43) #[swycartographr] prev. coords: (-47.06, -8.52)
  ("breton_castle_22","Château_de_Vitré",icon_castle_c_breton|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.76, 48.37),[],329), #[swycartographr] prev. coords: (-71.55, 71.19)


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC VILLAGES ##############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### DAC French Villages
  
  ("french_village_1", "Lunery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.35, -6.44),[], 244),         #[swycartographr] prev. coords: (30.31, -3.39)
  ("french_village_2", "Levet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.16, -6.31),[], 332),          #[swycartographr] prev. coords: (33.61, -8.91)
  ("french_village_3", "Ardon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.4, 28.61),[], 130),           #[swycartographr] prev. coords: (26.5, 24.57)
  ("french_village_4", "Tigy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.56, 28.72),[], 216),           #[swycartographr] prev. coords: (32.21, 23.86)
  ("french_village_5", "Bueil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.34, 24.52),[], 203),          #[swycartographr] prev. coords: (-1.73, 18.96)
  ("french_village_6", "Chambray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.46, 6.44),[], 204),         #[swycartographr] prev. coords: (-10.19, 0.54) #[swycartographr] prev. coords: (-0.44, 12.92) #[swycartographr] prev. coords: (2.68, 8.12)
  ("french_village_7", "Chasseneuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.91, -12.83),[], 12),   #[swycartographr] prev. coords: (-31.94, -26.14) #[swycartographr] prev. coords: (-15.33, -13.11)
  ("french_village_8", "Chauvigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.97, -13.99),[], 302),     #[swycartographr] prev. coords: (-26.22, -32.59) #[swycartographr] prev. coords: (-8.24, -22.01) #[swycartographr] prev. coords: (8.72, -14.98)
  ("french_village_9", "Puilboreau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.37, -32.51),[], 5),     #[swycartographr] prev. coords: (-53.3, -29.47)
  ("french_village_10", "Angoulins",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.33, -37.59),[], 289),    #[swycartographr] prev. coords: (-51.36, -38.89) #[swycartographr] prev. coords: (-57.84, -36.9)
    
  ("french_village_11", "Montpensier",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.53, -48.08),[], 320),  #[swycartographr] prev. coords: (56.15, -34.65)
  ("french_village_12", "Aubières",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.56, -61.5),[], 219),     #[swycartographr] prev. coords: (56.24, -45.05)
  ("french_village_13", "Chemilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.66, -35.62),[], 83),      #[swycartographr] prev. coords: (58.11, -20.4)
  ("french_village_14", "Montilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.41, -23.74),[], 100),     #[swycartographr] prev. coords: (53.41, -15.29)
  ("french_village_15", "Jussac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.42, -85.68),[], 330),      #[swycartographr] prev. coords: (29.38, -98.16) #[swycartographr] prev. coords: (28.63, -102.45)
  ("french_village_16", "Carlat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.18, -101.57),[], 220),      #[swycartographr] prev. coords: (32.96, -110.92) #[swycartographr] prev. coords: (30.01, -106.81) #[swycartographr] prev. coords: (46.25, -109.65)
  ("french_village_17", "Dardilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.65, -55.13),[], 36),     #[swycartographr] prev. coords: (113.28, -36.24) #[swycartographr] prev. coords: (117.61, -56.14)
  ("french_village_18", "Vienne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.5, -72.23),[], 116),      #[swycartographr] prev. coords: (117.79, -46.2) #[swycartographr] prev. coords: (118.98, -66.27)
  ("french_village_19", "Vals",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.9, -88.79),[], 235),          #[swycartographr] prev. coords: (81.31, -85.05)
  ("french_village_20", "Ceyssac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.52, -85.06),[], 148),      #[swycartographr] prev. coords: (83.92, -87.53) #[swycartographr] prev. coords: (83.13, -86.76)
    
  ("french_village_21", "Le Montat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14, -116.13),[], 135),   #[swycartographr] prev. coords: (0.57, -115.5) #[swycartographr] prev. coords: (13.82, -118.25) #[swycartographr] prev. coords: (13.85, -117.1)
  ("french_village_22", "Vers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.16, -109.67),[], 359),        #[swycartographr] prev. coords: (2.11, -109.58) #[swycartographr] prev. coords: (24.23, -109.46)
  ("french_village_23", "Sébazac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.74, -112.54),[], 329),    #[swycartographr] prev. coords: (28.65, -113.99)
  ("french_village_24", "Castelnaudary",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.9, -160.47),[], 148),     #[swycartographr] prev. coords: (15.71, -155.77) #[swycartographr] prev. coords: (25.68, -122.18) #[swycartographr] prev. coords: (16.89, -155.63)
  ("french_village_25", "Gramont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.35, -134.16),[], 319),     #[swycartographr] prev. coords: (-9.23, -123.64)
  ("french_village_26", "Agen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.65, -121.26),[], 130),   #[swycartographr] prev. coords: (-13.21, -128.17) #[swycartographr] prev. coords: (-13.77, -134.44)
  ("french_village_27", "Muret",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.27, -152.43),[], 123),        #[swycartographr] prev. coords: (5.09, -151.93) #[swycartographr] prev. coords: (3.17, -132.36) #[swycartographr] prev. coords: (8.04, -148.07)
  ("french_village_28", "Sauveterre",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.64, -121.62),[], 1),        #[swycartographr] prev. coords: (6.68, -144.94) #[swycartographr] prev. coords: (3.8, -126.83) #[swycartographr] prev. coords: (11.52, -144.7) #[swycartographr] prev. coords: (7.15, -141.86)
  ("french_village_29", "Castres",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.12, -145.26),[], 256),     #[swycartographr] prev. coords: (33.93, -147.44) #[swycartographr] prev. coords: (26.61, -133.08)
  ("french_village_30", "Limoux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.88, -172.03),[], 308),      #[swycartographr] prev. coords: (23.87, -143.9)
    
  ("french_village_31", "Lattes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.27, -153.17),[], 21),       #[swycartographr] prev. coords: (54.44, -132.75)
  ("french_village_32", "Agde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.96, -161.95),[], 306),  #[swycartographr] prev. coords: (58.06, -129.73) #[swycartographr] prev. coords: (89.64, -149.05)
  ("french_village_33", "Chabeuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.44, -99.6),[], 12),      #[swycartographr] prev. coords: (120.35, -85.14)
  ("french_village_34", "Tiffauges",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.01, 0.1),[], 156),     #[swycartographr] prev. coords: (115.14, -86.83) #[swycartographr] prev. coords: (114.87, -103.07)
  ("french_village_35", "Missé",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.55, -1.23),[], 206),       #[swycartographr] prev. coords: (-31.36, -6.31) #[swycartographr] prev. coords: (-48.28, -14.61)
  ("french_village_36", "Oiron",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.16, -4.43),[], 288),        #[swycartographr] prev. coords: (-25.92, -6.5) #[swycartographr] prev. coords: (-41.24, -13)
  ("french_village_37", "Fourcroix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.53, 152.32),[], 221),
  ("french_village_38", "Bizencourt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.97, 141.11),[], 109),
  ("french_village_39", "Amilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.55, 38.08),[], 72),         #[swycartographr] prev. coords: (62.77, 42.55) #[swycartographr] prev. coords: (54.55, 31.29) #[swycartographr] prev. coords: (64.53, 41.41)
  ("french_village_40", "Mormant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.99, 34.99),[], 19),        #[swycartographr] prev. coords: (57.77, 39.35) #[swycartographr] prev. coords: (49.3, 29.21) #[swycartographr] prev. coords: (59.66, 38.54) #[swycartographr] prev. coords: (60.32, 69.53)
    
  ("french_village_41", "La Bussière",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.16, 29.26),[], 134),   #[swycartographr] prev. coords: (49.01, 26.43) #[swycartographr] prev. coords: (39.26, 17.16) #[swycartographr] prev. coords: (49.93, 25.1) #[swycartographr] prev. coords: (62.64, 29.91)
  ("french_village_42", "Saint-Brisson-sur-Loire",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.7, 18.18),[], 232),        #[swycartographr] prev. coords: (52.12, 24.03) #[swycartographr] prev. coords: (42.25, 15.29) #[swycartographr] prev. coords: (53.74, 23.26)
  ("french_village_43", "Le_Breuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.16, -41.95),[], 135),    #[swycartographr] prev. coords: (66.94, -29.3)
  ("french_village_44", "Odos",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.72, -163.77),[], 92),        #[swycartographr] prev. coords: (-30.94, -150.46) #[swycartographr] prev. coords: (-27.26, -166.76)
  ("french_village_45", "Azay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.67, 10.22),[], 293),             #[swycartographr] prev. coords: (-12.56, -2.14) #[swycartographr] prev. coords: (5.2, 2.36)
  ("french_village_46", "Issoudun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.29, -13.28),[], 233),      #[swycartographr] prev. coords: (22.96, -10.82) #[swycartographr] prev. coords: (36.49, -5.43)
  ("french_village_47", "Fontenay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.84, -27.83),[], 200),    #[swycartographr] prev. coords: (-46.86, -30.27)
  ("french_village_48", "Tasque",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.89, -140.78),[], 46),      #[swycartographr] prev. coords: (-11.32, -137.89) #[swycartographr] prev. coords: (-22.65, -140.74)
  ("french_village_49", "Blanzac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.57, -74.52),[], 360),      #[swycartographr] prev. coords: (79.36, -78.98)
  ("french_village_50", "Chélieu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.91, -64.24),[], 10),     #[swycartographr] prev. coords: (124.9, -45.6)
    
  ("french_village_51", "La Crête",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.74, -26.97),[], 100),
  ("french_village_52", "Pontlevoy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.18, 11.65),[], 255),       #[swycartographr] prev. coords: (1.07, 10.38) #[swycartographr] prev. coords: (10.13, 16.22) #[swycartographr] prev. coords: (18.66, 12.79) #[swycartographr] prev. coords: (24.65, 12.19) #[swycartographr] prev. coords: (31.28, 11.43)
  ("french_village_53", "Boussac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.03, -27.42),[], 100),      #[swycartographr] prev. coords: (34.98, -28.63)
  ("french_village_54", "Yèvre",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.1, 44.5),[], 10),           #[swycartographr] prev. coords: (32.03, 41.21)
  ("french_village_55", "Aix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.22, -71.3),[], 221),           #[swycartographr] prev. coords: (85.52, -60.5)
  ("french_village_56", "Tauves",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.78, -74.49),[], 32),        #[swycartographr] prev. coords: (44.58, -53.16) #[swycartographr] prev. coords: (48.43, -73.97) #[swycartographr] prev. coords: (32.94, -72.92) #[swycartographr] prev. coords: (52.79, -70.65) #[swycartographr] prev. coords: (48.43, -74.25)
  ("french_village_57", "Jalognes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.77, 8.48),[], 112),      #[swycartographr] prev. coords: (63, 3.97) #[swycartographr] prev. coords: (47.73, 2.88) #[swycartographr] prev. coords: (69.11, 15.58) #[swycartographr] prev. coords: (62.91, 9.22)
  ("french_village_58", "Tursan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.95, -143.51),[], 235),        #[swycartographr] prev. coords: (-38.15, -136.94) #[swycartographr] prev. coords: (-31.41, -138.89) #[swycartographr] prev. coords: (-34.77, -142) #[swycartographr] prev. coords: (-36.27, -140.21)
  ("french_village_59", "Pavie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.27, -150.39),[], 212),      #[swycartographr] prev. coords: (1.37, -141)
  ("french_village_60", "Le Val-Saint-Père",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.39, 69.05),[], 325),
    
  ("french_village_61", "Vellèches",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.28, -4.6),[], 224),        #[swycartographr] prev. coords: (-19.85, -18.9) #[swycartographr] prev. coords: (5, -11.3) #[swycartographr] prev. coords: (-8.36, -5.81)
  ("french_village_62", "Montmorillon",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.57, -31.48),[], 23),     #[swycartographr] prev. coords: (12.06, -29.9) #[swycartographr] prev. coords: (14.75, -29.6) #[swycartographr] prev. coords: (14.94, -27.64)
  ("french_village_63", "Sévérac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.75, -117.99),[], 243),   #[swycartographr] prev. coords: (40.96, -123.85)
  ("french_village_64", "Xaintrailles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.44, -115.64),[], 80), #[swycartographr] prev. coords: (-23.19, -120.15) #[swycartographr] prev. coords: (-35.28, -116.68) #[swycartographr] prev. coords: (-22.6, -121.21) #[swycartographr] prev. coords: (-28.92, -116.83) #[swycartographr] prev. coords: (-23.73, -118.75)
  ("french_village_65", "Orval",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.07, -20.68),[], 269),        #[swycartographr] prev. coords: (133.81, 62.2)
  ("french_village_66", "Barbazan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.19, -170.74),[], 233),   #[swycartographr] prev. coords: (-24.6, -151.88)
  ("french_village_67", "Le Lion-d'Angers",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.02, 26.62),[], 4), #[swycartographr] prev. coords: (-42.32, -132.13) #[swycartographr] prev. coords: (-36.22, -130.81) #[swycartographr] prev. coords: (-39.33, -129.13) #[swycartographr] prev. coords: (-37.73, -126.35) #[swycartographr] prev. coords: (-38.28, -127.77) rot: 251
  ("french_village_68", "Alès",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.71, -126.63),[], 218),   #[swycartographr] prev. coords: (-38.98, -125.15) #[swycartographr] prev. coords: (-40.62, -123.59) #[swycartographr] prev. coords: (-34.83, -123.91) #[swycartographr] prev. coords: (103.27, -133.38)
  ("french_village_69", "Brassac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.59, -174.98),[], 115),     #[swycartographr] prev. coords: (27.96, -171.11) #[swycartographr] prev. coords: (-2.13, -149.42)
  ("french_village_70", "Vernajoul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.85, -169.67),[], 340),   #[swycartographr] prev. coords: (13.07, -169.75) #[swycartographr] prev. coords: (6.64, -146.38)
    
  ("french_village_71", "Aujac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.51, -100.29),[], 73),       #[swycartographr] prev. coords: (103.02, -95.26)
  ("french_village_72", "Le_Pailloux",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46, -64.44),[], 204),     #[swycartographr] prev. coords: (32.53, -63.51)
  ("french_village_73", "Murol",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.11, -71.97),[], 181),        #[swycartographr] prev. coords: (49.61, -64.97) #[swycartographr] prev. coords: (55.93, -62.04) #[swycartographr] prev. coords: (57.19, -70.32) #[swycartographr] prev. coords: (54.4, -62.54) #[swycartographr] prev. coords: (57.52, -69.66)
  ("french_village_74", "Brissac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.8, 12.46),[], 148),       #[swycartographr] prev. coords: (-45.1, 7.19)
  ("french_village_75", "Lembras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.13, -90.54),[], 176),      #[swycartographr] prev. coords: (18.57, -93.34) #[swycartographr] prev. coords: (-9.94, -96.44) #[swycartographr] prev. coords: (18.57, -88.96) #[swycartographr] prev. coords: (-2.34, -90.71)
  ("french_village_76", "Amboise",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.9, 15.31),[], 176),        #[swycartographr] prev. coords: (-2.34, -90.71) #[swycartographr] prev. coords: (7.99, 14.81)
  ("french_village_77", "Le Lude",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.22, 21.92),[], 47),      #[swycartographr] prev. coords: (-140.22, 57.52) #[swycartographr] prev. coords: (-143.26, 64.83) #[swycartographr] prev. coords: (-146.5, 60.68) #[swycartographr] prev. coords: (-145.49, 60.78) #[swycartographr] prev. coords: (-17.38, 21.55)
  ("french_village_78", "Lusignan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.84, -29.19),[], 47),      #[swycartographr] prev. coords: (-17.38, 21.55) #[swycartographr] prev. coords: (-22.85, -29.79) #[swycartographr] prev. coords: (-24.09, -28.67)
  ("french_village_79", "Sully-sur-Loire",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.18, 26.38),[], 47),      
  ("french_village_80", "Uzès",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.61, -131.8),[], 218),   
  ("french_village_81", "Najac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24, -121),[], 218),   
  ("french_village_82", "La Ferté",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.61, -131.8),[], 218),  

### DAC English Villages 

  ("english_village_1", "Monbazillac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.94, -99.21),[], 36),  #[swycartographr] prev. coords: (-14.15, -102.33) #[swycartographr] prev. coords: (18.18, -101.13)
  ("english_village_2", "Chammes",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.44, 48.94),[], 322),      #[swycartographr] prev. coords: (-31.95, 49.05)
  ("english_village_3", "Chancelade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.45, -78.68),[], 63),    #[swycartographr] prev. coords: (-18.29, -76.25) #[swycartographr] prev. coords: (-6.94, -76.59)
  ("english_village_4", "Trélissac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.89, -78.48),[], 290),    #[swycartographr] prev. coords: (-8, -75.07) #[swycartographr] prev. coords: (1.99, -78.39)
  ("english_village_5", "Champniers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.47, -53.84),[], 315),  #[swycartographr] prev. coords: (-35.86, -59.57)
  ("english_village_6", "La Couronne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.54, -62.11),[], 125), #[swycartographr] prev. coords: (-39.64, -67.42)
  ("english_village_7", "Rochechouart",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.81, -52.99),[], 119),  #[swycartographr] prev. coords: (-8.97, -55.21)
  ("english_village_8", "Couzeix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.01, -48.23),[], 335),       #[swycartographr] prev. coords: (-3.52, -48.47)
  ("english_village_9", "Mérignac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.88, -91.4),[], 60),    #[swycartographr] prev. coords: (-48.97, -105.03) #[swycartographr] prev. coords: (-50.53, -90.37)
  ("english_village_10", "Pessac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.21, -95.08),[], 135),      #[swycartographr] prev. coords: (-47.93, -87.02) #[swycartographr] prev. coords: (-49.31, -95.2)

  ("english_village_11", "Vignoles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.12, -122.1),[], 22),   #[swycartographr] prev. coords: (-52.6, -126.52) #[swycartographr] prev. coords: (-50.97, -125.76) #[swycartographr] prev. coords: (-51, -126.13) #[swycartographr] prev. coords: (-30.37, -64.6) #[swycartographr] prev. coords: (-49.17, -122.33) #[swycartographr] prev. coords: (-47.71, -120.98)
  ("english_village_12", "Blaye",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.24, -79.79),[], 295),      #[swycartographr] prev. coords: (-45.64, -72.23)
  ("english_village_13", "Anglet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.99, -149.54),[], 253),    #[swycartographr] prev. coords: (-73.56, -139.32) #[swycartographr] prev. coords: (-74.95, -147.41)
  ("english_village_14", "Biarritz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.1, -147.62),[], 114),  #[swycartographr] prev. coords: (-76.35, -140.18) #[swycartographr] prev. coords: (-78.87, -148.83) rot: 135
  ("english_village_15", "Peyrehorade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.45, -143.18),[], 124), #[swycartographr] prev. coords: (-60.45, -139.62)
  ("english_village_16", "Castets",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.96, -124.79),[], 27),    #[swycartographr] prev. coords: (-59.78, -121.39) #[swycartographr] prev. coords: (-61.54, -131.09) #[swycartographr] prev. coords: (-61.77, -131.28)
  ("english_village_17", "Entrammes",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.38, 42.12),[], 328),
  ("english_village_18", "Argentré",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.42, 49.19),[], 167),
  ("english_village_19", "Allonnes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.38, 36.07),[], 299),
  ("english_village_20", "Mulsannes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.65, 35.14),[], 29),

  ("english_village_21", "Mont-de-Marsan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.15, -128.22),[], 268), #[swycartographr] prev. coords: (-45.75, 27.05) rot: 24 #[swycartographr] prev. coords: (-38.31, -128)
  ("english_village_22", "Durtal",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.11, 28.09),[], 230),
  ("english_village_23", "Chailly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.32, 65.29),[], 352),      #[swycartographr] prev. coords: (54.88, 62.67)
  ("english_village_24", "Melun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.77, 65.95),[], 307),           #[swycartographr] prev. coords: (53.1, 57.19) #[swycartographr] prev. coords: (53.41, 59.99) rot: 82
  ("english_village_25", "Gasville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.85, 65.34),[], 125),
  ("english_village_26", "Luisant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.61, 61.12),[], 212),      #[swycartographr] prev. coords: (19.69, 61.59) rot: 324
  ("english_village_27", "Barentin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.68, 108.6),[], 202),
  ("english_village_28", "Quevilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.97, 100.27),[], 31),
  ("english_village_29", "Rots",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.48, 99.02),[], 91),
  ("english_village_30", "Ifs",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.41, 90.39),[], 186),

  ("english_village_31", "Honfleur",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.59, 102.13),[], 165),
  ("english_village_32", "Étretat",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.36, 114.35),[], 227),
  ("english_village_33", "Barfleur",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.27, 116.06),[], 80),
  ("english_village_34", "Valognes",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.2, 109.32),[], 309),
  ("english_village_35", "Fréthun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.17, 163.91),[], 109),
  ("english_village_36", "Marck",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.13, 166.79),[], 265),
  ("english_village_37", "Saint-Denis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.75, 81.54),[], 84),   #[swycartographr] prev. coords: (47.71, 82.89) rot: 329
  ("english_village_38", "Saint-Marcel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.48, 74.63),[], 286), #[swycartographr] prev. coords: (44.89, 72.32)
  ("english_village_39", "Arçonnay",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.72, 59.65),[], 344),
  ("english_village_40", "Valframbert",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.92, 67.54),[], 174),

  ("english_village_41", "Nonant",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.9, 96.54),[], 239),
  ("english_village_42", "Balleroy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.75, 97.05),[], 131),    #[swycartographr] prev. coords: (-61.87, 93.21)
  ("english_village_43", "Bailleul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.47, 80.32),[], 176),
  ("english_village_44", "Ecouché",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.8, 73.05),[], 104),     #[swycartographr] prev. coords: (-27.06, 72.71)
  ("english_village_45", "Brive",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.79, -85.24),[], 205),        #[swycartographr] prev. coords: (13.77, -95.9) #[swycartographr] prev. coords: (45.3, -95.45)
  ("english_village_46", "Ruch",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.87, -99.19),[], 340),        #[swycartographr] prev. coords: (-11.91, -97.74) #[swycartographr] prev. coords: (-23.28, -104.73) #[swycartographr] prev. coords: (-11.6, -98.31)
  ("english_village_47", "Mussidan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19, -83.11),[], 32),     #[swycartographr] prev. coords: (-27.64, -78.77) #[swycartographr] prev. coords: (-16.83, -84.4)
  ("english_village_48", "Beauvais",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.93, 106.79),[], 337),    #[swycartographr] prev. coords: (-14.02, 24.18)
  ("english_village_49", "Barbaste",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.06, -118.74),[], 35),    #[swycartographr] prev. coords: (-29.61, -118.74) #[swycartographr] prev. coords: (-27.2, -120.22) #[swycartographr] prev. coords: (-29.93, -120.89)
  ("english_village_50", "Corny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.73, 100.98),[], 216),

  ("english_village_51", "Falaise",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.76, 85.96),[], 202),     #[swycartographr] prev. coords: (-32.23, 86.47)
  ("english_village_52", "Bazas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.43, -109.41),[], 146),     #[swycartographr] prev. coords: (-39.14, -113.86)
  ("english_village_53", "Saint-Antoine",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.3, 78.63),[], 23),   #[swycartographr] prev. coords: (49.77, 78.72) #[swycartographr] prev. coords: (-44.49, 24.98) #[swycartographr] prev. coords: (55.68, 82) rot: 318 #[swycartographr] prev. coords: (50.3, 79.05)
  ("english_village_54", "Vendôme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.42, 38.62),[], 168),     #[swycartographr] prev. coords: (8.33, 40.19)
  ("english_village_55", "Beauvau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.73, 21.49),[], 9),
  ("english_village_56", "Langoiran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.54, -106.16),[], 23),  #[swycartographr] prev. coords: (-32.15, -110.32)
  ("english_village_57", "Mortain",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.09, 67.55),[], 150),
  ("english_village_58", "Lessay",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.28, 99.84),[], 75),
  ("english_village_59", "Orval",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.58, 85.97),[], 229),
  ("english_village_60", "Hambye",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.49, 80.98),[], 176),

  ("english_village_61", "Vire",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.09, 80.04),[], 343),        #[swycartographr] prev. coords: (-47.85, 77.93)
  ("english_village_62", "Sartilly",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.55, 78.39),[], 49),  
  ("english_village_63", "Verneuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.62, 76.69),[], 169),
  ("english_village_64", "L'Aigle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.03, 77.42),[], 268),
  ("english_village_65", "Dieppe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.59, 123.77),[], 198),
  ("english_village_66", "Blangy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28, 129.09),[], 100),
  ("english_village_67", "Pons",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.93, -62.84),[], 27),        #[swycartographr] prev. coords: (-58.39, 97.19)
  ("english_village_68", "Condé",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.6, 89.65),[], 127),       #[swycartographr] prev. coords: (-55.66, 89.85)
  ("english_village_69", "Fronsac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.06, -85.08),[], 79),     #[swycartographr] prev. coords: (-33.31, -96.15) #[swycartographr] prev. coords: (-33.41, -79.24)
  ("english_village_70", "Pomerol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.51, -86.4),[], 268),     #[swycartographr] prev. coords: (-27.68, -94.37)

  ("english_village_71", "Beychac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.83, -93.14),[], 187),    #[swycartographr] prev. coords: (-30.57, -100.37)
  ("english_village_72", "Ambarès",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.75, -88.09),[], 309),   #[swycartographr] prev. coords: (-37.54, -102.19)
  ("english_village_73", "Domme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.63, -97.51),[], 100),       #[swycartographr] prev. coords: (31.9, -89.64) #[swycartographr] prev. coords: (3.3, -103.12) #[swycartographr] prev. coords: (19.93, -97.67) #[swycartographr] prev. coords: (37.37, -93.83)
  ("english_village_74", "Vincennes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.7, 78.96),[], 100),     #[swycartographr] prev. coords: (32.8, 73.4) #[swycartographr] prev. coords: (52.25, 78.63) #[swycartographr] prev. coords: (53.32, 78.24)
  ("english_village_75", "Pont-Audemer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.3, 97.18),[], 46),      #[swycartographr] prev. coords: (-11.32, -137.89) #[swycartographr] prev. coords: (-22.65, -140.74)
  ("english_village_76", "Saint Hélène d'Estang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.71, -81.96),[], 269),   #[swycartographr] prev. coords: (-5.3, 93.18) rot: 46 #[swycartographr] prev. coords: (-56.84, -82.03)
  ("english_village_77", "Nogent-le-Rotrou",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.03, 54.94),[], 269),   #[swycartographr] prev. coords: (-5.3, 93.18) rot: 46 #[swycartographr] prev. coords: (-56.84, -82.03)
  ("english_village_78", "Saint Germain",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.03, 54.94),[], 269),  

### DAC Burgundian Villages
  ("burgundian_village_1", "Dole",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.92, -4.44),[], 84),   #[swycartographr] prev. coords: (110.6, 18.14) #[swycartographr] prev. coords: (128.52, 13.34)
  ("burgundian_village_2", "Cravant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.65, 24.15),[], 281),     #[swycartographr] prev. coords: (85.23, 18.71) #[swycartographr] prev. coords: (88.07, 24.43) #[swycartographr] prev. coords: (89.06, 30.37)
  ("burgundian_village_3", "Charbuy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.9, 32.23),[], 357),     #[swycartographr] prev. coords: (80.84, 23.07)
  ("burgundian_village_4", "Macey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.12, 54.56),[], 18),       #[swycartographr] prev. coords: (89.08, 59.12)
  ("burgundian_village_5", "Chaumont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128.35, 47.05),[], 233),    #[swycartographr] prev. coords: (106.14, 59.96) #[swycartographr] prev. coords: (81.88, 66.85)
  ("burgundian_village_6", "Rougemont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.51, 9.61),[], 28),  #[swycartographr] prev. coords: (149.41, 16.92) #[swycartographr] prev. coords: (158.18, 24.78)
  ("burgundian_village_7", "Gray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.16, 21),[], 225), #[swycartographr] prev. coords: (152.51, 12.98) #[swycartographr] prev. coords: (140.17, 16.89) #[swycartographr] prev. coords: (156.27, 18.92) #[swycartographr] prev. coords: (164.76, 3.52)
  ("burgundian_village_8", "Balleray",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77, 0.17),[], 339),       #[swycartographr] prev. coords: (75.74, -6.32)
  ("burgundian_village_9", "Imphy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.88, -14.11),[], 172),     #[swycartographr] prev. coords: (75.71, -12.11) #[swycartographr] prev. coords: (80.12, -12.48)
  ("burgundian_village_10", "Damme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.82, 182.51),[], 291),
  

  ("burgundian_village_11", "Bourgogne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.03, 160.82),[], 112), #[swycartographr] prev. coords: (63.85, 144.46)
  ("burgundian_village_12", "Audenarde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.04, 161.34),[], 166), #[swycartographr] prev. coords: (81.63, 137.11)
  ("burgundian_village_13", "Nevele",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.67, 170.97),[], 285),   #[swycartographr] prev. coords: (86.6, 143.3)
  ("burgundian_village_14", "Verbrande",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.9, 168.72),[], 157), #[swycartographr] prev. coords: (100.27, 138.93)
  ("burgundian_village_15", "Tisselt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.87, 174.43),[], 308), #[swycartographr] prev. coords: (104.16, 144.89)
  ("burgundian_village_16", "Thourotte",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.9, 106.04),[], 74),  #[swycartographr] prev. coords: (44.77, 90.84)
  ("burgundian_village_17", "Jaux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.83, 98.67),[], 312),      #[swycartographr] prev. coords: (54.06, 94.28)
  ("burgundian_village_18", "Sarry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.32, 79.3),[], 304),     #[swycartographr] prev. coords: (108.37, 78.45)
  ("burgundian_village_19", "Vertus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.4, 80.83),[], 120),    #[swycartographr] prev. coords: (101.42, 73.47) #[swycartographr] prev. coords: (98.16, 78.95)
  ("burgundian_village_20", "Rethel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.97, 100.55),[], 313),   #[swycartographr] prev. coords: (93.22, 95.18) #[swycartographr] prev. coords: (116.24, 89.29)
  
  ("burgundian_village_21", "Epernay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.66, 87.92),[], 124),   #[swycartographr] prev. coords: (77.95, 85.42) #[swycartographr] prev. coords: (90.33, 92.31)
  ("burgundian_village_22", "Étaples",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.99, 147.71),[], 136),  #[swycartographr] prev. coords: (17.63, 130.74) #[swycartographr] prev. coords: (31.74, 147.35) #[swycartographr] prev. coords: (25.8, 139.89) #[swycartographr] prev. coords: (32.61, 152.16)
  ("burgundian_village_23", "Wimeureux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.69, 157.91),[], 318), #[swycartographr] prev. coords: (20.97, 136.72) #[swycartographr] prev. coords: (25.72, 152.46)
  ("burgundian_village_24", "Ligny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.67, 136.74),[], 302),    #[swycartographr] prev. coords: (37.87, 115.44) #[swycartographr] prev. coords: (46.66, 133.92) #[swycartographr] prev. coords: (43.32, 147.11) #[swycartographr] prev. coords: (47.04, 136.18)
  ("burgundian_village_25", "Picquigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.03, 126.26),[], 205), #[swycartographr] prev. coords: (41.48, 105.15) #[swycartographr] prev. coords: (37.93, 121.07)
  ("burgundian_village_26", "Allaines",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.44, 134.45),[], 140), #[swycartographr] prev. coords: (58.84, 107.34)
  ("burgundian_village_27", "Biaches",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.42, 123.93),[], 302),  #[swycartographr] prev. coords: (65.82, 105.62)
  ("burgundian_village_28", "Ancy-le-Franc",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.48, 32.67),[], 319), #[swycartographr] prev. coords: (97.7, 22.39) #[swycartographr] prev. coords: (111.36, 42.23)
  ("burgundian_village_29", "Avallon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.41, 16.49),[], 268),     #[swycartographr] prev. coords: (87.71, 8.29) #[swycartographr] prev. coords: (95.96, 14.71)
  ("burgundian_village_30", "Macôn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.45, -26.19),[], 314),  #[swycartographr] prev. coords: (109.7, -26.83)
  
  ("burgundian_village_31", "Toulongeon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.69, -19.82),[], 340), #[swycartographr] prev. coords: (98.06, -13.4)
  ("burgundian_village_32", "Domrémy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.81, 62.2),[], 269),
  ("burgundian_village_33", "Jonvelle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.98, 40.51),[], 184), #[swycartographr] prev. coords: (140.53, 32.5)
  ("burgundian_village_34", "Godault",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.41, 138.57),[], 245),  #[swycartographr] prev. coords: (65.36, 153.3) #[swycartographr] prev. coords: (54.95, 123.28)
  ("burgundian_village_35", "Hesdin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.89, 141.21),[], 225),   #[swycartographr] prev. coords: (111.8, 24.53) #[swycartographr] prev. coords: (99.64, 15.7) #[swycartographr] prev. coords: (60.11, 5.59)
  ("burgundian_village_36", "Autun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.04, -10.55),[], 202),   #[swycartographr] prev. coords: (103.25, -0.29) #[swycartographr] prev. coords: (115.33, -0.25)
  ("burgundian_village_37", "Reulle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.91, 6.13),[], 166),   #[swycartographr] prev. coords: (107.82, 6.65) #[swycartographr] prev. coords: (119.82, 16.71)
  ("burgundian_village_38", "Grigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.01, 153.25),[], 240),   #[swycartographr] prev. coords: (25, 120.03)
  ("burgundian_village_39", "Arras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.56, 144.83),[], 112),    #[swycartographr] prev. coords: (52.49, 118.51)
  ("burgundian_village_40", "Bredene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.97, 179.6),[], 103),   #[swycartographr] prev. coords: (58.4, 150.18)
  
  ("burgundian_village_41", "Donzy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.48, 15.4),[], 342),     #[swycartographr] prev. coords: (63.53, 2.93) #[swycartographr] prev. coords: (63.64, -9.74)
  ("burgundian_village_42", "Coucy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.6, 103.07),[], 306),         #[swycartographr] prev. coords: (29.9, 83.06) #[swycartographr] prev. coords: (24.2, 89) #[swycartographr] prev. coords: (76.23, 102.76)
  ("burgundian_village_43", "Senlis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.46, 86.86),[], 165),   #[swycartographr] prev. coords: (48.2, 86.75) #[swycartographr] prev. coords: (60.27, 91.01)
  ("burgundian_village_44", "Montcornet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.76, 110.91),[], 201), #[swycartographr] prev. coords: (89.75, 103.99) #[swycartographr] prev. coords: (93.31, 107.05)
  ("burgundian_village_45", "Beaumont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.33, 146.71),[], 19), #[swycartographr] prev. coords: (92.17, 118.29)
  ("burgundian_village_46", "Pontailler-sur-Saône",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.03, 12.77),[], 124),   #[swycartographr] prev. coords: (107.07, 13.93) #[swycartographr] prev. coords: (123.96, 10.3) #[swycartographr] prev. coords: (136.5, 11.06) #[swycartographr] prev. coords: (124.02, 10.46)
  ("burgundian_village_47", "Vez",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.06, 83.76),[], 124),   #[swycartographr] prev. coords: (107.07, 13.93) #[swycartographr] prev. coords: (123.96, 10.3) #[swycartographr] prev. coords: (68.45, 83.65)
  ("burgundian_village_48", "Rambouillet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.55, 71.73),[], 124),   #[swycartographr] prev. coords: (107.07, 13.93) #[swycartographr] prev. coords: (123.96, 10.3) #[swycartographr] prev. coords: (68.45, 83.65)
  ("burgundian_village_49", "Angerville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.45, 51.45),[], 124),   #[swycartographr] prev. coords: (107.07, 13.93) #[swycartographr] prev. coords: (123.96, 10.3) #[swycartographr] prev. coords: (68.45, 83.65)
  ("burgundian_village_50", "Provins_village_1",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69, 69),[], 124),   #[swycartographr] prev. coords: (107.07, 13.93) #[swycartographr] prev. coords: (123.96, 10.3) #[swycartographr] prev. coords: (68.45, 83.65)

  ("burgundian_village_51", "Provins_village_2",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90, 70),[], 124),   #[swycartographr] prev. coords: (107.07, 13.93) #[swycartographr] prev. coords: (123.96, 10.3) #[swycartographr] prev. coords: (68.45, 83.65)
  ("burgundian_village_52", "Beaune",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.37, -2.41),[], 124),   #[swycartographr] prev. coords: (38.45, 51.45)

### DAC Breton Villages 
  ("breton_village_1", "Blain",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.25, 21.38),[], 148),
  ("breton_village_2", "Treillières",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.71, 15.77),[], 344),
  ("breton_village_3", "Lohéac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.66, 39.1),[], 351),       #[swycartographr] prev. coords: (-68.97, 39.72) #[swycartographr] prev. coords: (-80.35, 40.46)
  ("breton_village_4", "Vitré",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.78, 46.56),[], 355),        #[swycartographr] prev. coords: (-58.81, 48.52) #[swycartographr] prev. coords: (-55.57, 48.43) #[swycartographr] prev. coords: (-59.03, 48.22)
  ("breton_village_5", "Auray",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.15, 33.77),[], 82),         #[swycartographr] prev. coords: (-97.62, 31.33) #[swycartographr] prev. coords: (-113.48, 36.13) #[swycartographr] prev. coords: (-110.13, 35.35) #[swycartographr] prev. coords: (-104.25, 32.17) #[swycartographr] prev. coords: (-95.47, 20.88)
  ("breton_village_6", "Malestroit",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.58, 39.14),[], 15),     #[swycartographr] prev. coords: (-84.58, 33.59) #[swycartographr] prev. coords: (-97.32, 40.37) #[swycartographr] prev. coords: (-84.12, 44.22)
  ("breton_village_7", "Aleth",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.36, 65.59),[], 246),         #[swycartographr] prev. coords: (-79.53, 66.04)
  ("breton_village_8", "Dinard",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.61, 74.59),[], 100),        #[swycartographr] prev. coords: (-86.39, 68.28)
  ("breton_village_9", "Roscoff",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.84, 80.33),[], 167),      #[swycartographr] prev. coords: (-131.68, 77.55) #[swycartographr] prev. coords: (-132.16, 77.46) #[swycartographr] prev. coords: (-135.43, 83.76)
  ("breton_village_10", "Carantec",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.41, 80.13),[], 147),    #[swycartographr] prev. coords: (-123.66, 74.16) #[swycartographr] prev. coords: (-129.03, 83.87)
  
  ("breton_village_11", "Pont-l'Abbé",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.37, 43.98),[], 305), #[swycartographr] prev. coords: (-138.41, 48.05) #[swycartographr] prev. coords: (-140.17, 45.33) #[swycartographr] prev. coords: (-145.63, 44.09)
  ("breton_village_12", "Audierne",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.64, 52.01),[], 321),    #[swycartographr] prev. coords: (-146.87, 49.95) #[swycartographr] prev. coords: (-143.84, 51.66) #[swycartographr] prev. coords: (-152.17, 56.23) #[swycartographr] prev. coords: (-156.72, 52.23)
  ("breton_village_13", "Pont-Ivy",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.88, 55.56),[], 93),     #[swycartographr] prev. coords: (-108.75, 55.82) #[swycartographr] prev. coords: (-105.69, 53.92)
  ("breton_village_14", "Loudéac",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.73, 53.35),[], 327),      #[swycartographr] prev. coords: (-98.83, 57.04) #[swycartographr] prev. coords: (-97.03, 61.4) #[swycartographr] prev. coords: (-92.3, 57.77)
  ("breton_village_15", "Trégueux",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.23, 68.97),[], 200),   #[swycartographr] prev. coords: (-94.91, 64.48)
  ("breton_village_16", "Lamballe",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.81, 70.57),[], 274),     #[swycartographr] prev. coords: (-90.77, 62.74) #[swycartographr] prev. coords: (-91.03, 65.76)
  ("breton_village_17", "Trémazan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.93, 73.82),[], 232),   #[swycartographr] prev. coords: (-147.53, 71.3) #[swycartographr] prev. coords: (-148.58, 70.04) #[swycartographr] prev. coords: (-156.16, 77.39)
  ("breton_village_18", "Guérande",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.44, 18.59),[], 359),    #[swycartographr] prev. coords: (-83.91, 14.32) #[swycartographr] prev. coords: (-88.74, 19.88)
  ("breton_village_19", "Beaumanoir",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.44, 54.27),[], 235),   #[swycartographr] prev. coords: (-81.89, 59.78)
  ("breton_village_20", "Romagné",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.14, 60.23),[], 89),      #[swycartographr] prev. coords: (-59.16, 55.72)
  
  ("breton_village_21", "Rouge",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.25, 37.41),[], 56),         #[swycartographr] prev. coords: (-59.33, 30.98)
  ("breton_village_22", "Vallet",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.97, 7.26),[], 20),
  ("breton_village_23", "Hélléan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.78, 35.22),[], 318),    #[swycartographr] prev. coords: (-83.92, 45.59) #[swycartographr] prev. coords: (-91.68, 46.43) #[swycartographr] prev. coords: (-81.78, 46.09) #[swycartographr] prev. coords: (-91.46, 45.58) #[swycartographr] prev. coords: (-85.06, 43.87)
  ("breton_village_24", "Landerneau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.86, 70.05),[], 196),  #[swycartographr] prev. coords: (-137.28, 62.05) #[swycartographr] prev. coords: (-137.44, 60.95) #[swycartographr] prev. coords: (-143.29, 73.85) #[swycartographr] prev. coords: (-146.96, 69.99)
  ("breton_village_25", "Lignol",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.62, 56.06),[], 108),       #[swycartographr] prev. coords: (-116.08, 51.37) #[swycartographr] prev. coords: (-117.33, 53.8)
  ("breton_village_26", "Lannion",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.79, 82.14),[], 212),       #[swycartographr] prev. coords: (-110.45, 75.94) #[swycartographr] prev. coords: (-113.4, 76.8)
  ("breton_village_27", "Telgruc",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.49, 60.78),[], 47),      #[swycartographr] prev. coords: (-140.22, 57.52) #[swycartographr] prev. coords: (-143.26, 64.83) #[swycartographr] prev. coords: (-146.5, 60.68)
  ("breton_village_28", "Saint-Renan",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.24, -109.68),[], 257), #[swycartographr] prev. coords: (122.02, -100.38) #[swycartographr] prev. coords: (122.79, -99.11)
  ("breton_village_29", "Kersaint",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-149.7, 77.82),[], 49),      #[swycartographr] prev. coords: (-138.01, 66.46) #[swycartographr] prev. coords: (-139.16, 64.56) #[swycartographr] prev. coords: (-154.04, 73.69) #[swycartographr] prev. coords: (-144.5, 66.73) #[swycartographr] prev. coords: (-150.16, 78.45)
  ("breton_village_30", "Paimpol",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.13, 83.25),[], 110),     #[swycartographr] prev. coords: (-102.63, 77.2) #[swycartographr] prev. coords: (-104.46, 74.72)
  
  ("breton_village_31", "Commequiers",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.06, -9.36),[], 72),        #[swycartographr] prev. coords: (-84.61, 64.8) #[swycartographr] prev. coords: (-80.54, 69.43)
  ("breton_village_32", "Morlaix",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.63, 74.51),[], 236),     #[swycartographr] prev. coords: (-119.68, 72.23) #[swycartographr] prev. coords: (-121.63, 71.03) #[swycartographr] prev. coords: (-132.69, 76.32) #[swycartographr] prev. coords: (-130.12, 79.04)
  ("breton_village_33", "Plouguerneau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.97, 79.65),[], 17), #[swycartographr] prev. coords: (-140.52, 74.12) #[swycartographr] prev. coords: (-144.12, 73.82) #[swycartographr] prev. coords: (-152.44, 78.07) #[swycartographr] prev. coords: (-142.47, 77.95)
  ("breton_village_34", "Bieuzy",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.95, 44.46),[], 96),       #[swycartographr] prev. coords: (-107.67, 48.83) #[swycartographr] prev. coords: (-104.53, 48.04)
  ("breton_village_35", "Languidic",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.61, 42.97),[], 296),    #[swycartographr] prev. coords: (-113.09, 40.99) #[swycartographr] prev. coords: (-102.77, 42.97) #[swycartographr] prev. coords: (-92.43, 37.39)
  ("breton_village_36", "Sarzeau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.47, 26.77),[], 356),       #[swycartographr] prev. coords: (-92.3, 23.74) #[swycartographr] prev. coords: (-94.86, 27.5)
  ("breton_village_37", "Combourg",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.02, 63.08),[], 154),     #[swycartographr] prev. coords: (-71.31, 58.28) #[swycartographr] prev. coords: (-67.21, 59.39)
  ("breton_village_38", "Redon",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.2, 31.65),[], 351),         #[swycartographr] prev. coords: (-76.53, 30.99) #[swycartographr] prev. coords: (-76.78, 27.59)
  ("breton_village_39", "Le_Faouët",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.88, 54.79),[], 25),   #[swycartographr] prev. coords: (-120.09, 49.01) #[swycartographr] prev. coords: (-121.01, 55.76)
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65, -105),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.93, -130.08),[], 207), #[swycartographr] prev. coords: (16.13, -112.41) #[swycartographr] prev. coords: (18.45, -117.04)
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.42, -52.76),[], 235), #[swycartographr] prev. coords: (-44.64, -67.59) #[swycartographr] prev. coords: (-52.03, -53.43)
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.9, 114.9),[], 231), #[swycartographr] prev. coords: (15.84, 103.93)
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.59, -109.3),[], 89), #[swycartographr] prev. coords: (134.97, -100.44) #[swycartographr] prev. coords: (131.2, -105.93) #[swycartographr] prev. coords: (-59.14, -113.94)
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.95, 50.33),[], 230), #[swycartographr] prev. coords: (-23.96, 33.1)


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.31, 30.17),[], 36),  #[swycartographr] prev. coords: (-84.23, 30.18) rot: 33
  ("Bridge_2","{!}2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.93, -132.45),[], 264),  #[swycartographr] prev. coords: (112.74, -133.54)
  ("Bridge_3","{!}3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.89, 84.51),[], 288),
  ("Bridge_4","{!}4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.3, -79.07),[], 104),  #[swycartographr] prev. coords: (-48.33, -78.99)
  ("Bridge_5","{!}5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.15, 83.78),[], 57),  #[swycartographr] prev. coords: (42.15, 83.78) rot: 60
  ("Bridge_6","{!}6",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.42, 26.58),[], 67), 
  ("Bridge_7","{!}7",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.94, 45.03),[], 84),  #[swycartographr] prev. coords: (-22.96, 45.16) rot: 85 #[swycartographr] prev. coords: (-22.96, 45.02) rot: 74
  ("Bridge_8","{!}8",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.81, 61.29),[], 23), 
  ("Bridge_9","{!}9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.75, -97.19),[], 69), #[swycartographr] prev. coords: (115.58, -97.91)
  ("Bridge_10","{!}10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.15, 75.64),[], 275), 
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.93,-136.58),[], 121),  #[swycartographr] prev. coords: (-32.92, -136.52) rot: 95 #[swycartographr] prev. coords: (-12.34, -143.4) #[swycartographr] prev. coords: (-32.93, -136.58) rot: 95 #[swycartographr] prev. coords: (-32.93, -136.58) rot: 95 #[swycartographr] prev. coords: (-32.93, -136.58) rot: 95
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.13, 24.98),[], 323), #[swycartographr] prev. coords: (55.4, 25.41) rot: 328
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.01, 8.09),[], 278),  #[swycartographr] prev. coords: (-76.65, 10.91) rot: 356
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.66, 21.92),[], 34),  #[swycartographr] prev. coords: (-28.86, -93.49) rot: 175 #[swycartographr] prev. coords: (-28.86, -93.49) rot: 353
  ("Bridge_15","{!}15",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.92, 82.05),[], 320), 
  ("Bridge_16","{!}16",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.46, 10.85),[], 11), 
  ("Bridge_17","{!}17",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.6, 64.79),[], 30), 
  ("Bridge_18","{!}18",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.52, 46.27),[], 308), 
  ("Bridge_19","{!}19",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.04, -83.71),[], 301),  #[swycartographr] prev. coords: (115.24, -84.03)
  ("Bridge_20","{!}20",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.13, 62.46),[], 15), 
  ("Bridge_21","{!}21",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.01, 57.16),[], 86), 
  ("Bridge_22","{!}22",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.94, -118.42),[], 341),  
  ("Bridge_23","{!}23",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.52, 95.26),[], 249),  #[swycartographr] prev. coords: (-29.1, 94.77) rot: 253
  ("Bridge_24","{!}24",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.78, -94.01),[], 345),  
  ("Bridge_25","{!}25",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.47, -19.87),[], 138),  #[swycartographr] prev. coords: (51.85, 76.34) rot: 43
  ("Bridge_26","{!}26",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.14, 50.83),[], 29), 
  ("Bridge_27","{!}27",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.76, 65.53),[], 37), 
  ("Bridge_28","{!}28",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.03, 54.86),[], 307),
  ("Bridge_29","{!}29",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.04, -104.42),[], 343), 
  ("Bridge_30","{!}30",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.9, 50),[], 5), 
  ("Bridge_31","{!}31",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.88, 34.07),[], 6),  #[swycartographr] prev. coords: (36.19, 34.29) rot: 354
  ("Bridge_32","{!}32",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.2, -123.48),[], 360),   #[swycartographr] prev. coords: (107.03, -123.62) rot: 334
  ("Bridge_33","{!}33",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.59, 101.64),[], 311),  
  ("Bridge_34","{!}34",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.82, -91.71),[], 99),   #[swycartographr] prev. coords: (-44.88, -90.54) rot: 131 #[swycartographr] prev. coords: (-44.79, -91.63) #[swycartographr] prev. coords: (-44.79, -91.62) #[swycartographr] prev. coords: (-44.91, -90.55)
  ("Bridge_35","{!}35",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.25, 76.09),[], 43),  #[swycartographr] prev. coords: (51.85, 76.34) #[swycartographr] prev. coords: (52.12, 76.53)
  ("Bridge_36","{!}36",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.62, 18.41),[], 1),  
  ("Bridge_37","{!}37",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.61, -6.42),[], 279),  
  ("Bridge_38","{!}38",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.03, 54.86),[], 307),  
  ("Bridge_39","{!}39",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.04, -104.42),[], 343), 
  ("Bridge_40","{!}40",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.09, 133.58),[], 331),   #[swycartographr] prev. coords: (-1.12, 16.82) rot: 18 #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (33.86, 133.3)
  ("Bridge_41","{!}41",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.11,-139.27),[], 353), #[swycartographr] prev. coords: (-63.11, -139.27) rot: 95
  ("Bridge_42","{!}42",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.17,-146.47),[], 349), #[swycartographr] prev. coords: (-72.65, -146.62) rot: 95 #[swycartographr] prev. coords: (-72.65, -146.62) rot: 358
  ("Bridge_43","{!}43",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.72,-145.24),[], 353), #[swycartographr] prev. coords: (-63.72, -145.24) rot: 95
  ("Bridge_44","{!}44",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.06,-144.9),[], 126), #[swycartographr] prev. coords: (-48.06, -144.9) rot: 95
  ("Bridge_45","{!}45",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.98,-134.04),[], 233), #[swycartographr] prev. coords: (-56.05, -134.05) rot: 95
  ("Bridge_46","{!}46",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.66,-164.88),[], 95), #[swycartographr] prev. coords: (-33.66, -164.88) rot: 95
  ("Bridge_47","{!}47",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.47,-165.34),[], 95),
  ("Bridge_48","{!}48",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.8,-153.52),[], 64), #[swycartographr] prev. coords: (6.8, -153.52) rot: 95
  ("Bridge_49","{!}49",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.74,-166.46),[], 4), #[swycartographr] prev. coords: (-19.75, -166.46) rot: 95 #[swycartographr] prev. coords: (-19.75, -166.46) rot: 34
  ("Bridge_50","{!}50",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.98,-146.47),[], 88), #[swycartographr] prev. coords: (9.98, -146.47) rot: 95
  ("Bridge_51","{!}51",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.49,-119.29),[], 126), #[swycartographr] prev. coords: (-19.49, -119.29) rot: 95
  ("Bridge_52","{!}52",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.14,-111.32),[], 7), #[swycartographr] prev. coords: (-10.41, -111.31) rot: 95
  ("Bridge_53","{!}53",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.08,-110.98),[], 350), #[swycartographr] prev. coords: (14.08, -110.98) rot: 95
  ("Bridge_54","{!}54",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11,-132.61),[], 74), #[swycartographr] prev. coords: (-11, -132.61) rot: 95
  ("Bridge_55","{!}55",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.92,-136.94),[], 24), #[swycartographr] prev. coords: (21.92, -136.94) rot: 95
  ("Bridge_56","{!}56",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.26,-130.76),[], 145), #[swycartographr] prev. coords: (9.27, -130.85) rot: 95
  ("Bridge_57","{!}57",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.31,-143.36),[], 90), #[swycartographr] prev. coords: (-12.31, -143.36) rot: 95
  ("Bridge_58","{!}58",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.07, 99.81),[], 31),   #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_59","{!}59",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.7, 113.45),[], 25),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_60","{!}60",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.75, 81.49),[], 315),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_61","{!}61",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.09, -53.36),[], 306),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_62","{!}62",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.9, -105.65),[], 330),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (-52.9, -105.65) rot: 337
  ("Bridge_63","{!}63",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.22, -53.87),[], 91),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_64","{!}64",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.24, 6.63),[], 155),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284 #[swycartographr] prev. coords: (-17.75, 6.86) rot: 165 #[swycartographr] prev. coords: (-17.38, 6.74) rot: 140
  ("Bridge_65","{!}65",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.56, -29.8),[], 253),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_66","{!}66",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.77, -38.35),[], 27),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_67","{!}67",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.93, -51.26),[], 300),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_68","{!}68",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.91, -54.01),[], 134),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_69","{!}69",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.26, -94.67),[], 354),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (17.22, -94.73) rot: 360
  ("Bridge_70","{!}70",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.45, -73.89),[], 58),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (69.76, -59.67)
  ("Bridge_71","{!}71",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.72, -48.75),[], 70),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_72","{!}72",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.76, -26.79),[], 98),    #[swycartographr] prev. coords: (74.85, -26.88) rot: 13 #[swycartographr] prev. coords: (-1.29, 16.85)
  ("Bridge_73","{!}73",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.12, -86.42),[], 44),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_74","{!}74",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.64, -127.11),[], 48),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_75","{!}75",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.16, -108.41),[], 24),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_76","{!}76",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.88, 57.09),[], 357),    #[swycartographr] prev. coords: (60.82, 57.14) rot: 13 #[swycartographr] prev. coords: (-1.29, 16.85) #[swycartographr] prev. coords: (61.49, 57.05) #[swycartographr] prev. coords: (60.86, 57.08)
  ("Bridge_77","{!}77",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.53, 26.89),[], 277),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_78","{!}78",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.45, 17.16),[], 300),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_79","{!}79",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.13, 53.1),[], 257),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_80","{!}80",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.01, 12.97),[], 13),    #[swycartographr] prev. coords: (-1.29, 16.85) #[swycartographr] prev. coords: (150.27, 12.99)
  ("Bridge_81","{!}81",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.42, 23.33),[], 104),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_82","{!}82",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(147.29, -5.37),[], 2),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (147.64, -5.3)
  ("Bridge_83","{!}83",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128.31, -13.1),[], 36),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (128.05, -13.36)
  ("Bridge_84","{!}84",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.79, -8.33),[], 281),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_85","{!}85",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.21, -35.42),[], 280),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_86","{!}86",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.91, -29.61),[], 4),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_87","{!}87",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.65, -23.11),[], 300),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_88","{!}88",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.4, -30.65),[], 25),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_89","{!}89",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.36, -61.06),[], 343),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (122.88, -60.78) rot: 331
  ("Bridge_90","{!}90",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.44, -45.95),[], 77),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (117.38, -46.1) #[swycartographr] prev. coords: (117.56, -46.11)
  ("Bridge_91","{!}91",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.41, -76.42),[], 35),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_92","{!}92",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.41, 12.97),[], 341),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_93","{!}93",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.85, -55.72),[], 316),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284 #[swycartographr] prev. coords: (20.85, -55.72) rot: 294
  ("Bridge_94","{!}94",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.82, -43.48),[], 271),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284
  ("Bridge_95","{!}95",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.38, -15.31),[], 263),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284
  ("Bridge_96","{!}96",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.88, -30.68),[], 317),    #[swycartographr] prev. coords: (19.49, -19.92) rot: 284 #[swycartographr] prev. coords: (-5.66, -20.53) rot: 307
  ("Bridge_97","{!}97",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.59, -114.9),[], 257),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284
  ("Bridge_98","{!}98",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.05, -93.82),[], 352),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284 #[swycartographr] prev. coords: (-14.08, -93.73) rot: 351 #[swycartographr] prev. coords: (-14.08, -93.73) rot: 5
  ("Bridge_99","{!}99",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.1, -88.94),[], 318),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284 #[swycartographr] prev. coords: (-37.06, -88.89) rot: 331 #[swycartographr] prev. coords: (-37.1, -88.94) rot: 317
  ("Bridge_100","{!}100",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.75, -58.37),[], 41),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284 #[swycartographr] prev. coords: (-53.42, -149.18) rot: 316 #[swycartographr] prev. coords: (-53.34, -149.28) rot: 311
  ("Bridge_101","{!}101",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.52, -76.09),[], 284),    #[swycartographr] prev. coords: (-5.66, -20.53)
  ("Bridge_102","{!}102",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.65, -20.54),[], 271),    #[swycartographr] prev. coords: (-5.66, -20.53) rot: 284 #[swycartographr] prev. coords: (-5.66, -20.46)
  ("Bridge_103","{!}103",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.11, -114.13),[], 80),   #[swycartographr] prev. coords: (69.76, -59.67) rot: 58
  ("Bridge_104","{!}104",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.76, -59.67),[], 58),  
  ("Bridge_105","{!}105",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.37, 7.11),[], 2),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13
  ("Bridge_106","{!}106",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.03, 4.13),[], 348),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (39.03, 4.13) rot: 4
  ("Bridge_107","{!}107",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.42, 117.46),[], 69),    #[swycartographr] prev. coords: (-1.29, 16.85) rot: 13 #[swycartographr] prev. coords: (-1.33, 16.86) rot: 10
  ("Bridge_108","{!}108",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.55, 90.06),[], 105),   #[swycartographr] prev. coords: (-1.33, 16.86) rot: 10
  ("Bridge_109","{!}109",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.33, 16.86),[], 10),  

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
