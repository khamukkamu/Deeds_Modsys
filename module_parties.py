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
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC TOWNS #################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################
  
### DAC French Towns  
    ("town_1","Bourges",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.92, -5.56),[], 171),                           
    ("town_2","Orléans",     icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.49, 29.31),[], 88),
    ("town_3","Tours",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.24, 3.3),[], 13),                             
    ("town_4","Poitiers",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.44, -30.13),[], 356),                     
    ("town_5","La_Rochelle",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.95, -40.81),[], 323),                   
    ("town_6","Clermont",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.97, -42.83),[], 233),
    ("town_7","Moulins",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.47, -17.53),[], 314),                         
    ("town_8","Aurillac", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.69, -103.17),[], 267),                          
    ("town_9","Lyon",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.4, -38.87),[], 100),
    ("town_10","Le_Puy",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.31, -85),[], 291),                         

    ("town_11","Cahors", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.53, -112.39),[], 68),                            
    ("town_12","Rodez",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.36, -116.77),[], 292),                            
    ("town_13","Lectoure",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.6, -126.26),[], 41),                        
    ("town_14","Tarbes",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.02, -148.18),[], 23),                        
    ("town_15","Toulouse",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.54, -130.45),[], 267),                         
    ("town_16","Carcassonne", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.32, -140.38),[], 92),                      
    ("town_17","Montpellier", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.05, -130.76),[], 20),                      
    ("town_18","Valence", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.64, -75.91),[], 102),                         
    ("town_19","Thouars", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.83, -10.32),[], 276),                         
    ("town_20","Tournai", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.21, 127.07),[], 139),                          

    ("town_21","Gien", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.02, 18.15),[], 319),                              
    ("town_22","Montargis-le-Franc", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.83, 33.71),[], 43),
    ("town_23","Albret", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.21, -122.18),[], 208),      
    ("town_24","Bergerac", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.94, -98.32),[], 335),           
    ("town_25","Périgueux", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.59, -78),[], 190),      
    ("town_26","Angoulême", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.97, -64.35),[], 240),    
    ("town_27","Limoges", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.06, -51.49),[], 269),           
    ("town_28","Angers", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.28, 13.61),[], 337),     
    ("town_29","Foix", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.59, -149),[], 280),      ### NEW           

 ### DAC English Towns
    ("town_30","Paris", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.81, 75.01),[], 318),                    
    ("town_31","Bayonne", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.8, -141.97),[], 232),  
    ("town_32","Nemours", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.63, 51.8),[], 3),                                                      
    ("town_33","Laval", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.39, 44.14),[], 217),                           
    ("town_34","Le_Mans", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.98, 39.05),[], 151),               
    ("town_35","Bordeaux", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.24, -104.72),[], 127),    
    ("town_36","Chartres", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.96, 52.74),[], 38),                          
    ("town_37","Rouen", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.02, 92.18),[], 145),                               
    ("town_38","Caen", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.72, 90.02),[], 216),                             
    ("town_39","Harfleur", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.86, 100.66),[], 303),                        
    ("town_40","Cherbourg", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.67, 118.74),[], 189),                     

    ("town_41","Bayeux", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.44, 95.73),[], 194),                           
    ("town_42","Calais", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.75, 147.18),[], 193),
    ("town_43","Alençon", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18, 55.51),[], 225),                         
    ("town_44","Argentan", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.3, 66.17),[], 225),                  
    ("town_45","Tartas", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.61, -132.04),[], 200),       
    ("town_46","Dax", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.64, -135.79),[], 256),      ### NEW           
    ("town_47","Libourne", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.63, -96.65),[], 221),      ### NEW           
    ("town_48","Saint-Lô", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.66, 92.08),[], 220),      ### NEW           
    ("town_49","Eu", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.2, 117.57),[], 48),      ### NEW           
    ("town_50","Avranches", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.46, 72.94),[], 225),      ### NEW           

    ("town_51","Coutances", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.98, 88.29),[], 271),      ### NEW           

 ### DAC Burgundian Towns
    ("town_52","Dijon", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.33, 15.28),[], 242),
    ("town_53","Besançon", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.92, 10.74),[], 132),                       
    ("town_54","Nevers", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.58, -9.08),[], 91),                            
    ("town_55","Auxerre", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.05, 20.62),[], 128),                          
    ("town_56","Troyes", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.71, 49.03),[], 302),                        
    ("town_57","Compiègne", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.38, 92),[], 12),                        
    ("town_58","Bruges", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.64, 146.38),[], 218),                         
    ("town_59","Gand", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.1, 140.47),[], 97),                             
    ("town_60","Malines", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.37, 141.87),[], 227),               

    ("town_61","Boulogne", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.99, 133.68),[], 52),                       
    ("town_62","Châlons-en-Champagne", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.62, 76.41),[], 209),           
    ("town_63","Reims", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.19, 88.61),[], 303),                            
    ("town_64","Amiens",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.44, 108.18),[],284),
    ("town_65","Péronne",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.45, 108.32),[],345),

### DAC Breton Towns
    ("town_66","Rennes", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.54, 46.77),[], 192),                          
    ("town_67","Nantes", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.76, 13.39),[], 278),                          
    ("town_68","Vannes", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.03, 29.52),[], 13),                          
    ("town_69","Kemper", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.03, 50.66),[], 211),
    ("town_70","Saint-Malo", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.75, 68.66),[], 354),          

    ("town_71","Saint-Brieuc", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.42, 66.42),[], 153),                  
    ("town_72","Saint-Pol-de-Léon", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.39, 76.05),[], 326),            
    ("town_73","Rohan", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.98, 53.81),[], 27),                          

   
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC CASTLES ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### DAC French Castles
  ("castle_1","Forteresse_de_Chinon",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.25, -3.67),[],306),        
  ("castle_2","Châteauroux",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.83, -15.04),[],56),                
  ("castle_3","Château de Niort",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.96, -35.4),[],255),
  ("castle_4","La Tour_de_Termes",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.95, -134.85),[],210),        
  ("castle_5","Château_de_Murol",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.12, -62.97),[],280),            
  ("castle_6","Château_de_Polignac",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.03, -81.04),[],30),           
  ("castle_7","Château_de_Culant",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.69, -23.41),[],3),           
  ("castle_8","Château_de_Chaumont",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.94, 15.89),[],67),        
  ("castle_9","Château_de_Boussac",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.9, -31.4),[],64),           
  ("castle_10","Yèvre-le-Châtel",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.18, 44.27),[],209),   
  
  ("castle_11","Château_de_La_Fayette",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.49, -57.99),[],285),
  ("castle_12","La_Tour_d'Auvergne",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.77, -55.36),[],269),          
  ("castle_13","Château_de_Charlus",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.55, -57.43),[],46),      ### NEW
  ("castle_14","Château_de_Sancerre",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.57, 6.35),[],268),        
  ("castle_15","Castelnau_Tursan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.55, -136.67),[],108),          
  ("castle_16","Forteresse_d'Auch",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.17, -137.73),[],7),           
  ("castle_17","Mont-St-Michel",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.16, 67.25),[],197),             
  ("castle_18","Château_de_Turenne",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.08, -99.32),[],360),          
  ("castle_19","Sévérac-le-Château",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.47, -121.12),[],302),      
  ("castle_20","Château_de_Saint_Germain_Beaupré",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.4, -33.14),[],215),       ### NEW     
  
  ("castle_21","Château_de_Virieu",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.62, -47.9),[],155),      
  ("castle_22","Château_de_La_Palice",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.9, -24.7),[],86),       ### NEW     
  ("castle_23","Château_du_Cheylard",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.99, -96.71),[],109),       ### NEW     
  ("castle_24","Château_de_Vaucouleurs",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.55, 59.08),[],337),       ### NEW     
  ("castle_25","La_Tour_de_Marmande",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.9, -15.74),[],18),       ### NEW     
 
 # ("castle_20","Château_de_Sarzay",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.49, -26.4),[],55),          
   # ("castle_13","Château_de_Val",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.96, -73.51),[],213),            

### DAC English Castles
  ("castle_26","Château_de_Castelnaud",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.36, -101.32),[],15),      
  ("castle_27","Forteresse_de_Rauzan",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.33, -103.59),[],59), 
  ("castle_28","Château_de_Montréal",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.85, -84.87),[],294),   
  ("castle_29","Château_du_Lude",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.42, 22.44),[],260),          
  ("castle_30","Château_de_Nérac",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.04, -120.4),[],14),         

  ("castle_31","Château_de_Falaise",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.07, 78.24),[],28),        
  ("castle_32","Château-Gaillard",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.21, 86.59),[],260),         
  ("castle_33","Château_de_Vendôme",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.06, 26.59),[],287),
  ("castle_34","Château_de_Beauvau",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.73, 16.73),[],260),
  ("castle_35","Château_Gontier",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.52, 28.97),[],260),
  ("castle_36","Château_de_Verneuil",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.29, 66.51),[],123),
  ("castle_37","Château_de_Mortain",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.65, 67.58),[],46),       ### NEW     
  ("castle_38","Château_de_Langoiran",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.36, -111.97),[],335),       ### NEW     
  ("castle_39","Forteresse_de_Landiras",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.3, -111.9),[],288),       ### NEW     
  ("castle_40","Château_de_Fronsac",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34, -94.45),[],66),       ### NEW     

  ("castle_41","Château_de_Montferrand",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.08, -100.6),[],275),       ### NEW     
  ("castle_42","Forteresse_de_Blaye",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.59, -83.76),[],336),       ### NEW     
  ("castle_43","Château_de_Montbray",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.35, 80.13),[],46),       ### NEW     
  ("castle_44","Château_de_Gacé",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.9, 70.4),[],21),       ### NEW     
  ("castle_45","Château_de_Sainte-Suzanne",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.34, 43.23),[],46),       ### NEW     
  ("castle_46","Château_de_Durtal",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.95, 19.07),[],46),       ### NEW     

### DAC Burgundian Castles  
  ("castle_47","Château_de_Tonerre",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.01, 24.01),[],353),
  ("castle_48","Forteresse_d'Avallon",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.24, 9.63),[],10),
  ("castle_49","Château_de_Varenne-lès-Mâcon",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.06, -30.12),[],135),
  ("castle_50","Château_de_Toulongeon",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.56, -15.55),[],114),

  ("castle_51","Château_de_Ligny-en-Barrois",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.5, 67.88),[],342),
  ("castle_52","Château_de_Jonvelle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.58, 34.5),[],217),
  ("castle_53","Forteresse_de_Noyelles",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.81, 125.36),[],45),
  ("castle_54","Château_de_Montfort",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.27, 17.37),[],81),
  ("castle_55","Forteresse_de_La_Rochepot",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.62, 2.56),[],67),
  ("castle_56","Château_de_Vergy",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.04, 9.31),[],25),
  ("castle_57","Château_de_Brimeu",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.67, 123.1),[],45),
  ("castle_58","Château_de_Bellemotte",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.6, 118.84),[],268),
  ("castle_59","Forteresse_d'Uytkerke",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.97, 152.06),[],312),
  ("castle_60","Château_de_La_Charité-sur-Loire",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.82, 0.09),[],139),

  ("castle_61","Forteresse_de_L'Isle_Adam",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.06, 81.68),[],45),
  ("castle_62","Château_de_Senlis",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.14, 85.53),[],335),
  ("castle_63","Château_de_Montcornet",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.15, 106.48),[],319),
  ("castle_64","Château_de_Chimay",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.03, 112.74),[],259),

 ### DAC Breton Castles 
  ("castle_65","Château_de_Fougères",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.11, 55.35),[],307),
  ("castle_66","Châteaubriant",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.82, 28.32),[],207),
  ("castle_67","Château_de_Dinan",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.53, 61.42),[],50),
  ("castle_68","Château_de_Clisson",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.6, 3.91),[],195),
  ("castle_69","Château_de_Josselin",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.79, 42.82),[],108),
  ("castle_70","Forteresse_de_Roch'Morvan",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.16, 62.5),[],45),
 
  ("castle_71","Château_de_Guéméné",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.16, 52.53),[],314),
  ("castle_72","Château_de_Rochefort",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.39, 33.26),[],134),
  ("castle_73","Château_de_Tonquédec",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.83, 73.75),[],233),
  ("castle_74","Château_de_Rosmadec",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.72, 54.94),[],266),
  ("castle_75","Château_de_Coëtivy",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.71, 66.68),[],109),
  ("castle_76","Château_de_Trémazan",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.13, 70.29),[],203),
  ("castle_77","Château_de_Kermoysan",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.91, 70.43),[],101),
  ("castle_78","Château_de_Coëtquen",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.26, 63.3),[],13),
  ("castle_79","Château_de_Penhoët",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.89, 66.17),[],306),

  ("castle_80","Château_de_Penmarc'h",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.67, 70.87),[],82),
  ("castle_81","Forteresse_de_Kemperlé",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.2, 45.44),[],197),
  ("castle_82","Château_d'Hen_Bont",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.59, 41.22),[],115),
  ("castle_83","Château_de_Derval",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.24, 26.19),[],45),
  ("castle_84","Château_de_Suscinio",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.38, 24.88),[],334),
  ("castle_85","Forteresse_de_Roch'an",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.35, 49.78),[],299),
  ("castle_86","Forteresse_de_Dol",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.94, 62.88),[],329),


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC VILLAGES ##############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### DAC French Villages
  
  ("village_1", "Lunery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.31, -3.39),[], 244),
  ("village_2", "Levet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.61, -8.91),[], 332),
  ("village_3", "Ardon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.5, 24.57),[], 130),
  ("village_4", "Tigy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.21, 23.86),[], 216),
  ("village_5", "Bueil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.46, 7.83),[], 203),
  ("village_6", "Chambray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.19, 0.54),[], 204),
  ("village_7", "Chasseneuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.94, -26.14),[], 12),
  ("village_8", "Chauvigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.22, -32.59),[], 302),
  ("village_9", "Puilboreau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.65, -33.14),[], 5),
  ("village_10", "Angoulins",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.86, -46.69),[], 289),
  
  ("village_11", "Montpensier",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.15, -34.65),[], 320),
  ("village_12", "Aubières",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.13, -45.09),[], 219),
  ("village_13", "Chemilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.11, -20.4),[], 83),
  ("village_14", "Montilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.41, -15.29),[], 100),
  ("village_15", "Jussac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.38, -98.16),[], 330),
  ("village_16", "Carlat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.01, -106.81),[], 220),
  ("village_17", "Dardilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.28, -36.24),[], 36),
  ("village_18", "Vienne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.79, -46.2),[], 116),
  ("village_19", "Vals",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.31, -85.05),[], 235),
  ("village_20", "Ceyssac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.92, -87.53),[], 148),
  
  ("village_21", "Le Montat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.57, -115.5),[], 135),
  ("village_22", "Vers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.11, -109.58),[], 359),
  ("village_23", "Sébazac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.67, -112.84),[], 329),
  ("village_24", "Calmont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.68, -122.18),[], 148),
  ("village_25", "Gramont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.23, -123.64),[], 319),
  ("village_26", "Terraube",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.21, -128.17),[], 130),
  ("village_27", "Muret",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.17, -132.36),[], 123),
  ("village_28", "Blagnac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.8, -126.83),[], 1),
  ("village_29", "Castres",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.61, -133.08),[], 256),
  ("village_30", "Limoux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.87, -143.9),[], 308),
  
  ("village_31", "Lattes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.44, -132.75),[], 21),
  ("village_32", "Vendargues",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.06, -129.73),[], 306),
  ("village_33", "Chabeuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.35, -72.78),[], 12),
  ("village_34", "Livron",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.51, -78.82),[], 156),
  ("village_35", "Missé",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.28, -14.61),[], 206),
  ("village_36", "Oiron",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.24, -13),[], 288),
  ("village_37", "Fourcroix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.64, 129.23),[], 221),
  ("village_38", "Bizencourt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.65, 128.37),[], 109),
  ("village_39", "Amilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.55, 31.29),[], 72),
  ("village_40", "Mormant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.3, 29.21),[], 19),
  
  ("village_41", "Saint-Gondon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.26, 17.16),[], 134),
  ("village_42", "Poilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.25, 15.29),[], 232),
  ("village_43", "Le_Breuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.94, -29.3),[], 135),
  ("village_44", "Odos",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.94, -150.46),[], 92),
  ("village_45", "Azay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.56, -2.14),[], 293),
  ("village_46", "Issoudun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.96, -10.82),[], 233),
  ("village_47", "Fontenay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.86, -30.27),[], 200),
  ("village_48", "Tasque",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.32, -137.89),[], 46),
  ("village_49", "Blanzac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.9, -79.01),[], 360),
  ("village_50", "Chélieu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.9, -45.6),[], 10),
  
  ("village_51", "La Crête",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.74, -26.97),[], 100),
  ("village_52", "Amboise",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.07, 10.38),[], 255),
  ("village_53", "Boussac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.6, -29.21),[], 100),
  ("village_54", "Yèvre",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.03, 41.21),[], 10),
  ("village_55", "Aix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.52, -60.5),[], 221),
  ("village_56", "Tauves",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.26, -53.65),[], 32),
  ("village_57", "Jalognes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.73, 2.88),[], 112),
  ("village_58", "Geaune",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.41, -138.89),[], 235),
  ("village_59", "Pavie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.37, -141),[], 212),
  ("village_60", "Le Val-Saint-Père",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.76, 69.03),[], 325),
  
  ("village_61", "Vellèches",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.85, -18.9),[], 224),
  ("village_62", "Azerables",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.75, -29.6),[], 23),
  ("village_63", "Sévérac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.96, -123.85),[], 243),
  ("village_64", "Xaintrailles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.28, -116.68),[], 80),
  ("village_65", "Domrémy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.91, 52.03),[], 269),
  ("village_66", "Barbazan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.6, -151.88),[], 233), 
  ("village_67", "Mont-de-Marsan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.32, -132.13),[], 251),
  ("village_68", "Ròcahòrt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.98, -125.15),[], 218),  
  ("village_69", "Brassac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.13, -149.42),[], 115),  
  ("village_70", "Vernajoul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.64, -146.38),[], 340),  
  
  ("village_71", "Aujac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.02, -95.26),[], 73),  
  ("village_72", "Le_Pailloux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.66, -61.23),[], 204),  
  ("village_73", "Murol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.16, -66.02),[], 181),
  ("village_74", "Brissac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.1, 7.19),[], 148),
  ("village_75", "Lembras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.94, -96.44),[], 176),   
  
### DAC English Villages 

  ("village_76", "Monbazillac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.15, -102.33),[], 36),
  ("village_77", "Chammes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.58, 40.95),[], 322),
  ("village_78", "Chancelade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.29, -76.25),[], 63),
  ("village_79", "Trélissac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8, -75.07),[], 290),
  ("village_80", "Champniers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.86, -59.57),[], 315),
  
  ("village_81", "La Couronne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.64, -67.42),[], 125),
  ("village_82", "Rochechouart",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.97, -55.21),[], 119),
  ("village_83", "Couzeix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.36, -49.9),[], 335),
  ("village_84", "Mérignac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.97, -105.03),[], 60),
  ("village_85", "Pessac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.55, -108.08),[], 135),
  ("village_86", "Vignoles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.6, -126.52),[], 22),
  ("village_87", "Blaye",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.03, -85.63),[], 295),
  ("village_88", "Anglet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.2, -139.34),[], 253),
  ("village_89", "Biarritz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.54, -144.77),[], 135),
  ("village_90", "Peyrehorade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.45, -139.62),[], 124),
  
  ("village_91", "Castets",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.61, -130.8),[], 27),
  ("village_92", "Entrammes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.97, 40.43),[], 328),
  ("village_93", "Argentré",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.02, 46.38),[], 167),
  ("village_94", "Allonnes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.38, 36.07),[], 299),
  ("village_95", "Mulsannes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.65, 35.14),[], 29),
  ("village_96", "Le Lion-d'Angers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.78, 18.89),[], 24),
  ("village_97", "Durtal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.36, 21.3),[], 230),
  ("village_98", "Chailly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.88, 62.67),[], 352),
  ("village_99", "Ury",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.1, 57.19),[], 82),
  ("village_100", "Gasville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.02, 56.15),[], 125),
  
  ("village_101", "Luisant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.76, 50.23),[], 324),
  ("village_102", "Barentin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.15, 95.14),[], 202),
  ("village_103", "Quevilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.97, 88.35),[], 31),
  ("village_104", "Rots",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.36, 89.87),[], 91),
  ("village_105", "Ifs",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.89, 86.72),[], 186),
  ("village_106", "Honfleur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.24, 94.22),[], 165),
  ("village_107", "Étretat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.66, 107.1),[], 227),
  ("village_108", "Barfleur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.36, 114.78),[], 80),
  ("village_109", "Valognes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.29, 106.44),[], 309),
  ("village_110", "Fréthun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.06, 144.86),[], 109),
  
  ("village_111", "Marck",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.89, 145.82),[], 265),
  ("village_112", "Saint-Denis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.14, 76.94),[], 329),
  ("village_113", "Evry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.09, 72.75),[], 286),
  ("village_114", "Arçonnay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.57, 52.71),[], 344),
  ("village_115", "Valframbert",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.01, 58.81),[], 174),
  ("village_116", "Nonant",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.63, 94.08),[], 239),
  ("village_117", "Balleroy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.35, 93.88),[], 131),
  ("village_118", "Bailleul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.04, 70),[], 176),
  ("village_119", "Ecouché",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.05, 63.99),[], 104),
  ("village_120", "Brive",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.77, -95.9),[], 205),
  
  ("village_121", "Ruch",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.28, -104.73),[], 340),
  ("village_122", "Mussidan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.6, -83.17),[], 32),
  ("village_123", "Le_Lude",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.36, 20.05),[], 337),
  ("village_124", "Barbaste",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.61, -118.74),[], 35),
  ("village_125", "Corny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.9, 88.58),[], 216),
  ("village_126", "Aubigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.14, 80.89),[], 202),
  ("village_127", "Bazas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.14, -113.86),[], 146),
  ("village_128", "Ménil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.26, 26.38),[], 318),
  ("village_129", "Vendôme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.43, 24.73),[], 168),
  ("village_130", "Beauvau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.3, 14.45),[], 9),
  
  ("village_131", "Langoiran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.15, -110.32),[], 23),
  ("village_132", "Mortain",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.64, 69.72),[], 150),
  ("village_133", "Lessay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.97, 94.86),[], 75),
  ("village_134", "Orval",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.04, 86.12),[], 229),
  ("village_135", "Hambye",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.95, 79.15),[], 176),
  ("village_136", "Vire",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.85, 77.93),[], 343),
  ("village_137", "Sartilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.06, 75.14),[], 49),  
  ("village_138", "Verneuil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.8, 69.23),[], 169),
  ("village_139", "L'Aigle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2, 66.05),[], 268),
  ("village_140", "Dieppe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.38, 115.95),[], 198),
  
  ("village_141", "Blangy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.47, 112.09),[], 100),
  ("village_142", "Pont-Hébert",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.47, 94.85),[], 27),
  ("village_143", "Condé",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.66, 89.85),[], 127),
  ("village_144", "Fronsac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.31, -96.15),[], 79),
  ("village_145", "Pomerol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.68, -94.37),[], 268),
  ("village_146", "Beychac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.57, -100.37),[], 187),
  ("village_147", "Ambarès",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.54, -102.19),[], 309),
  ("village_148", "Domme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.3, -103.12),[], 100),    
  
### DAC Burgundian Villages
  ("village_149", "Quetigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.6, 18.14),[], 84),
  ("village_150", "Quenne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.23, 18.71),[], 281),
  
  ("village_151", "Charbuy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.84, 23.07),[], 357),
  ("village_152", "Macey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.66, 50.93),[], 18),
  ("village_153", "Rouilly",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.67, 46.92),[], 233),
  ("village_154", "Rougemont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.41, 16.92),[], 28),
  ("village_155", "Baume-les-Dames",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.51, 12.98),[], 225),
  ("village_156", "Balleray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.74, -6.32),[], 339),
  ("village_157", "Imphy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.71, -12.11),[], 172),
  ("village_158", "Damme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.45, 149.03),[], 291),
  ("village_159", "Bourgogne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.85, 144.46),[], 112),
  ("village_160", "Audenarde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.63, 137.11),[], 166),
  
  ("village_161", "Nevele",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.6, 143.3),[], 285),
  ("village_162", "Verbrande",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.27, 138.93),[], 157),
  ("village_163", "Tisselt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.16, 144.89),[], 308),
  ("village_164", "Thourotte",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.77, 90.84),[], 74),
  ("village_165", "Jaux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.06, 94.28),[], 312),
  ("village_166", "Sarry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.37, 78.45),[], 304),
  ("village_167", "Vertus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.42, 73.47),[], 120),
  ("village_168", "Rethel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.22, 95.18),[], 313),
  ("village_169", "Epernay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.95, 85.42),[], 124),
  ("village_170", "Condette",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.63, 130.74),[], 136),
  
  ("village_171", "Wimeureux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.97, 136.72),[], 318),
  ("village_172", "Ligny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.87, 115.44),[], 302),
  ("village_173", "Picquigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.48, 105.15),[], 205),
  ("village_174", "Allaines",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.84, 107.34),[], 140),
  ("village_175", "Biaches",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.82, 105.62),[], 302),
  ("village_176", "Ancy-le-Franc",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.7, 22.39),[], 319),
  ("village_177", "Magny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.71, 8.29),[], 268),
  ("village_178", "Macôn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.7, -26.83),[], 314),
  ("village_179", "Toulongeon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.06, -13.4),[], 340),
  ("village_180", "Givrauval",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.61, 65.45),[], 190),
  
  ("village_181", "Jonvelle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.53, 32.5),[], 184),
  ("village_182", "Godault",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.95, 123.28),[], 245),
  ("village_183", "Montigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.64, 15.7),[], 225),
  ("village_184", "Beaune",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.25, -0.29),[], 202),
  ("village_185", "Reulle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.82, 6.65),[], 166),
  ("village_186", "Grigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25, 120.03),[], 240),
  ("village_187", "Arras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.49, 118.51),[], 112),
  ("village_188", "Bredene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.4, 150.18),[], 103),
  ("village_189", "Donzy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.53, 2.93),[], 342),
  ("village_190", "Mours",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.9, 83.06),[], 306),
  
  ("village_191", "Barbery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.2, 86.75),[], 165),
  ("village_192", "Montcornet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.75, 103.99),[], 201),
  ("village_193", "Beaumont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.17, 118.29),[], 19),
  ("village_194", "Chenôve",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.07, 13.93),[], 124),  
  
### DAC Breton Villages 

  ("village_195", "Blain",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.25, 21.38),[], 148),
  ("village_196", "Treillières",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.71, 15.77),[], 344),
  ("village_197", "Lohéac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.97, 39.72),[], 351),
  ("village_198", "Vitré",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.57, 48.43),[], 355),
  ("village_199", "Auray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.62, 31.33),[], 82),
  ("village_200", "Malestroit",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.58, 33.59),[], 15),
  
  ("village_201", "Aleth",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.53, 66.04),[], 246),
  ("village_202", "Dinard",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.39, 68.28),[], 100),
  ("village_203", "Roscoff",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.68, 77.55),[], 167),
  ("village_204", "Carantec",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.66, 74.16),[], 147),
  ("village_205", "Pont-l'Abbé",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.41, 48.05),[], 305),
  ("village_206", "Audierne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.87, 49.95),[], 321),
  ("village_207", "Pont-Ivy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.69, 53.92),[], 93),
  ("village_208", "Loudéac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.83, 57.04),[], 327),
  ("village_209", "Trégueux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.91, 64.48),[], 200),
  ("village_210", "Lamballe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.77, 62.74),[], 274),
  
  ("village_211", "Trémazan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.53, 71.3),[], 232),
  ("village_212", "Guérande",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.91, 14.32),[], 359),
  ("village_213", "Beaumanoir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.89, 59.78),[], 235),
  ("village_214", "Romagné",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.16, 55.72),[], 89),
  ("village_215", "Rouge",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.33, 30.98),[], 56),
  ("village_216", "Vallet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.97, 7.26),[], 20),
  ("village_217", "Hélléan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.92, 45.59),[], 318),
  ("village_218", "Landerneau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.28, 62.05),[], 196),
  ("village_219", "Lignol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.08, 51.37),[], 108),
  ("village_220", "Lannion",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.45, 75.94),[], 212),
  
  ("village_221", "Telgruc",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.22, 57.52),[], 47),
  ("village_222", "Saint-Renan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.02, -100.38),[], 257),
  ("village_223", "Kersaint",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.16, 64.56),[], 49),
  ("village_224", "Paimpol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.63, 77.2),[], 110),
  ("village_225", "Miniac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.61, 64.8),[], 72),
  ("village_226", "Morlaix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.68, 72.23),[], 236),
  ("village_227", "Plouguerneau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.52, 74.12),[], 17),
  ("village_228", "Bieuzy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.67, 48.83),[], 96),
  ("village_229", "Languidic",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.77, 42.97),[], 296),
  ("village_230", "Sarzeau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.3, 23.74),[], 356),
  
  ("village_231", "Combourg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.31, 58.28),[], 154),
  ("village_232", "Redon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.78, 27.59),[], 351),
  ("village_233", "Le_Faouët",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.09, 49.01),[], 25),
  
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

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
