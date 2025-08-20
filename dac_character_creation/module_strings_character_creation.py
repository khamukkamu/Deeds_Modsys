# -*- coding: cp1254 -*-
from module_skills import * 
from compiler import *

character_creation_strings = [

# DAC Starting Quest Strings  

("dac_start_quest_generic", "^^You continue your journey towards France..."),
("dac_start_quest_mercenary", "^^Your head is heavy and your throat is dry, you can feel the ground beneath you and the sound of men arguing in the distance. After a sudden rush of emotions it takes you a moment to gather yourself and to remember you're {playername}, a mercenary working for the War Brethren Company. You were hired to deal with a band routiers that were pillaging the countryside. It was supposed to be a quick and easy contract, no more than a dozen crudely armed men that were no match for your armed band. However this wasn't the case, as at least twenty good men were waiting for your company and you stepped right into an ambush. You think that someone must have tipped them off, perhaps a rival company or one of the noble houses that still owes you payment. ^^It doesn't matter now, what matters is that you are still alive and you would rather stay that way. You can hear steps coming your way, you open your eyes to catch a glimpse of whoever it might be, but the sun blinds you temporarily. You blink a few times to adjust to the light and manage to recognize some of the faces that now surround you. ^^You..."),
("dac_start_quest_forester", "^^You were hunting in the forest when you ran into another group. You find out that these are poachers and do not have the appropriate paperwork to hunt in these grounds..."),
("dac_start_quest_guard", "^^You were patrolling your lord's grounds when you ran into some disgruntled farmers, plotting to burn the lord's manor..."),
("dac_start_quest_merchant", "^^A primary competitor of the town you are visiting has sent a group of thugs to intimidate you to leave immediately.."),
("dac_start_quest_noble", "^^A minor lord felt insulted by what you said to another group of lords, so he has challenged you to a duel..."),

# DAC Start as Lord

("sel_lord_fac_adj_0", "All Factions"),
("sel_lord_fac_adj_1", "Kingdom of France"),
("sel_lord_fac_adj_2", "Kingdom of England"),
("sel_lord_fac_adj_3", "Duchy of Burgundy"),
("sel_lord_fac_adj_4", "Duchy of Brittany"),

# String for character creation presentation
("dac_select_background",                         "Select Your Background"),
("dac_select_class",                              "Select Your Class"),
("dac_class",                                     "Class"),
                
("dac_background_noble",                          "Noble"),
("dac_background_merchant",                       "Merchant"),
("dac_background_soldier",                        "Soldier"),
("dac_background_hunter",                         "Hunter"),
("dac_background_mercenary",                      "Mercenary"),
("dac_background_peasant",                        "Peasant"),
("dac_background_healer",                         "Healer"),
        
("dac_background_desc_noble",                     "As a noble you start your early life relatively wealthy in comparison to most, whilst not one from an influential family you nevertheless were afforded a decent education at court which included reading, martial skills and matters of faith. ^^Pros: ^*One of Us: 20% Reduction on upkeep and recruitment costs for Knights ^*Combat Training: Start with decent combat stats ^^Cons: ^*One of them: 20% upkeep penalty for regular troops, does not apply to mercenaries ^*Valuable target: Your ransom value is much higher should you be captured"),
("dac_background_desc_merchant",                  "As a merchant you make a living from trade, what exactly that trade entails is up to you but you are good at seizing opportunities as they arise and getting the most out of it."),
("dac_background_desc_soldier",                   "As a soldier you know well enough about combat and your fellow soldiers, their needs and wants, how logistics work and how battles are fought and won."),
("dac_background_desc_hunter",                    "As a hunter you know how to move around, how to track and stalk your prey. Those skills are vital in an unforgiving world."),
("dac_background_desc_mercenary",                 "As a mercenary your services are in high demand in these tumultuous times."),
("dac_background_desc_peasant",                   "As a peasant your life is one of toil and survival"),
("dac_background_desc_healer",                    "As a healer you keep death at bay"),
        
("dac_background_class_governor",                 "Governor"),
("dac_background_class_strategist",               "Strategist"),
("dac_background_class_jouster",                  "Jouster"),          
("dac_background_class_goods_merchant",           "Goods Merchant"),
("dac_background_class_slaver",                   "Ransom Broker"),
("dac_background_class_investor",                 "Investor"),               
("dac_background_class_pavoisier",                "Pavoisier"),
("dac_background_class_vougier",                  "Vougier"),
("dac_background_class_crossbow",                 "Crossbowman"),
("dac_background_class_archer",                   "Archer"),              
("dac_background_class_poacher",                  "Poacher"),
("dac_background_class_manhunter",                "Manhunter"),
("dac_background_class_marksman",                 "Marksman"),               
("dac_background_class_condottiero",              "Condottiero"),
("dac_background_class_sellsword",                "Sellsword"),
("dac_background_class_pikeman",                  "Pikeman"),
("dac_background_class_crossbowman",              "Crossbowman"),           
("dac_background_class_farmer",                   "Farmer"),
("dac_background_class_rebel",                    "Rebel"),
("dac_background_class_smith",                    "Smith"),        
("dac_background_class_surgeon",                  "Surgeon"),
("dac_background_class_priest",                   "Priest"),
("dac_background_class_alchemist",                "Alchemist"),

("dac_background_class_desc_governor",            "Governors specialize in politics and administration ^^Pros: ^*Tax Master: Reduced tax inefficiency from having multiple fiefs ^*Courtly: Faster relationship gains ^*Builder: Cheaper building costs, also applies to workshops ^^Cons: ^*Mostly talk: Significantly lower combat stats from lack of experience"),
("dac_background_class_desc_strategist",          "Strategists specialize in leadership roles and logistics ^^Pros: ^*Tactics and leadership: Start with higher tactics and leadership skills ^*Logistician: Troops consume less food and you don't have an upkeep penalty for regular troops ^^Cons: ^*Leading from Behind: You let your men do most of the fighting, as a consequence your personal combat skills have been neglected"),
("dac_background_class_desc_jouster",             "Jousters specialize in single combat and tournaments ^^Pros: ^*Regular Contestant: You receive notifications when tournaments are being held ^*Renowned Fighter: Increased rewards from tournaments, can place higher bets ^*Single Combat: Increased combat stats from frequently fighting ^^Cons: ^*Lone Wolf: Not used to leading men to combat, your leadership stats and starting party size is reduced"),         
 
("dac_background_class_desc_goods_merchant",      "Goods Merchants specialize in everything related to trading from one location to another, buy low, sell high. ^^Pros: ^*Trader by Nature: Start with high trade and persuasion skills ^*Caravan Master: Start with a higher inventory capacity and access to a secure secret stash ^^Cons: ^*"),
("dac_background_class_desc_slaver",              "Ransom Broker"),
("dac_background_class_desc_investor",            "Investor"),         
      
("dac_background_class_desc_pavoisier",           "Pavoisier"),
("dac_background_class_desc_vougier",             "Vougier"),
("dac_background_class_desc_crossbow",            "Crossbowman"),
("dac_background_class_desc_archer",              "Archer"),        
      
("dac_background_class_desc_poacher",             "Poacher"),
("dac_background_class_desc_manhunter",           "Manhunter"),
("dac_background_class_desc_marksman",            "Marksman"),      
         
("dac_background_class_desc_condottiero",         "Condottiero"),
("dac_background_class_desc_sellsword",           "Sellsword"),
("dac_background_class_desc_pikeman",             "Pikeman"),
("dac_background_class_desc_crossbowman",         "Crossbowman"),     
      
("dac_background_class_desc_farmer",              "Farmer"),
("dac_background_class_desc_rebel",               "Rebel"),
("dac_background_class_desc_smith",               "Smith"),        

("dac_background_class_desc_surgeon",             "Surgeon"),
("dac_background_class_desc_priest",              "Priest"),
("dac_background_class_desc_alchemist",           "Alchemist"),

### DAC Seek: The legendary Lorem Ipsum
("lorem_ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"),

]