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
("dac_attributes",                                "Attributes"),
("dac_skills",                                    "Skills"),

("dac_skill_trade",                               "Trade: {reg14}"),
("dac_skill_leadership",                          "Leadership: {reg14}"),
("dac_skill_prisoner_management",                 "Prisoner Management: {reg14}"), 
("dac_skill_reserved_1",                          "Reserved Skill 1"), 
("dac_skill_reserved_2",                          "Reserved Skill 2"), 
("dac_skill_reserved_3",                          "Reserved Skill 3"), 
("dac_skill_reserved_4",                          "Reserved Skill 4"), 
("dac_skill_persuasion",                          "Persuasion: {reg14}"),
("dac_skill_engineer",                            "Engineer: {reg14}"),
("dac_skill_first_aid",                           "First Aid: {reg14}"),
("dac_skill_surgery",                             "Surgery: {reg14}"),
("dac_skill_wound_treatment",                     "Wound Treatment: {reg14}"),
("dac_skill_inventory_management",                "Inventory Management: {reg14}"),
("dac_skill_spotting",                            "Spotting: {reg14}"),
("dac_skill_pathfinding",                         "Path-finding: {reg14}"),
("dac_skill_tactics",                             "Tactics: {reg14}"),
("dac_skill_tracking",                            "Tracking: {reg14}"),
("dac_skill_trainer",                             "Trainer: {reg14}"),
("dac_skill_reserved_5",                          "Reserved Skill 5"),
("dac_skill_reserved_6",                          "Reserved Skill 6"),
("dac_skill_reserved_7",                          "Reserved Skill 7"),
("dac_skill_reserved_8",                          "Reserved Skill 8"),
("dac_skill_looting",                             "Looting: {reg14}"),
("dac_skill_horse_archery",                       "Horse Archery: {reg14}"),
("dac_skill_riding",                              "Riding: {reg14}"),
("dac_skill_athletics",                           "Athletics: {reg14}"),
("dac_skill_shield",                              "Shield: {reg14}"),
("dac_skill_weapon_master",                       "Weapon Master: {reg14}"),
("dac_skill_reserved_9",                          "Reserved Skill 9"),
("dac_skill_reserved_10",                         "Reserved Skill 10"),
("dac_skill_reserved_11",                         "Reserved Skill 11"),
("dac_skill_reserved_12",                         "Reserved Skill 12"),
("dac_skill_reserved_13",                         "Reserved Skill 13"),
("dac_skill_power_draw",                          "Power Draw: {reg14}"),
("dac_skill_power_throw",                         "Power Throw: {reg14}"),
("dac_skill_power_strike",                        "Power Strike: {reg14}"),
("dac_skill_ironflesh",                           "Ironflesh: {reg14}"),
("dac_skill_reserved_14",                         "Reserved Skill 14"),
("dac_skill_reserved_15",                         "Reserved Skill 15"),
("dac_skill_reserved_16",                         "Reserved Skill 16"),
("dac_skill_reserved_17",                         "Reserved Skill 17"),
("dac_skill_reserved_18",                         "Reserved Skill 18"),
                
("dac_background_noble",                          "Noble"),
("dac_background_merchant",                       "Merchant"),
("dac_background_soldier",                        "Soldier"),
("dac_background_hunter",                         "Hunter"),
("dac_background_mercenary",                      "Mercenary"),
("dac_background_peasant",                        "Peasant"),
("dac_background_healer",                         "Healer"),
        
("dac_background_desc_noble",                     "As a noble you start your early life relatively wealthy in comparison to most, whilst not one from an influential family you nevertheless were afforded a decent education at court which included reading, martial skills and matters of faith ^^\
Pros: ^\
* One of Us: 20% Reduction on upkeep and recruitment costs for Knights ^\
* Tutors: Start with a decent mix of skills ^^\
Cons: ^\
* One of them: 20% upkeep penalty for regular troops, does not apply to mercenaries ^\
* Valuable target: Your ransom value is much higher should you be captured"),

("dac_background_desc_merchant",                  "As a merchant you make a living from trade, what exactly that trade entails is up to you but you are good at seizing opportunities as they arise and getting the most out of it. ^^\
Pros: ^\
* Business Minded: Start with higher trade, persuasion and inventory management skills. ^\
* Negotiator: Can use trade or persuasion skills to get out of disadvantageous situations such as getting caught by enemies or just doing business ^^\
Cons: ^\
* Not a Fighter: Start with low combat related skills and proficiencies."),

("dac_background_desc_soldier",                   "As a soldier you know well enough about combat and your fellow soldiers, their needs and wants, how logistics work and how battles are fought and won. ^^\
Pros: ^\
* Logistics: You have spent quite some time on the road, foraging, scouting and setting up camps ^\
* One of us: Commoners recognize you as one of their own, pay 20% less upkeep for regular troops ^^\
Cons: ^\
* Low Born: Nobles are reluctant to serve under your freshly earned banner, pay 20% more upkeep for noble troops"),

("dac_background_desc_hunter",                    "As a hunter you know how to move around, how to track and stalk your prey. Those skills are vital in an unforgiving world. ^^\
Pros: ^\
* Foraging: Your supplies of food last longer as your party will consume 33% less food ^\
* Scouting: Receive a notification when spotting a hostile party stronger than yours on the world map ^^\
Cons: ^\
* Keep Your Distance: You are used to eliminating threats before they can close the distance and thus are ill prepared for close combat"),

("dac_background_desc_mercenary",                 "As a mercenary your services are in high demand in these tumultuous times yet trust is hard to gain when your only alliegeance is to gold. ^^\
Pros: ^\
* Contracts and Contacts: Mercenary recruitment and upkeep is significantly reduced ^\
* Grand Company: Factions are more likely to provide you with mercenary contracts, rewards are increased ^^\
Cons: ^\
* Villainous Lot: Mercenaries are often compromising of veterans, deserters, bandits and naïve recruits who don't always go along. Base morale is lower and suffer higher morale penalties from events, such as lack of food, retreat or defeat.^\
* Lofty Ambitions: Nobles are very suspicious towards your true loyalties, requirements to join a faction are higher and should you try to form a kingdom of your own, neutral factions are likely to declare war on you."),

("dac_background_desc_peasant",                   "As a peasant your life is one of toil and survival. While there are opportunities to achieve greater deeds, it will feel like the odds are stacked against you. ^^\
Pros: ^\
* Solidarity: Can ask villages for donations, the higher the relations with the village, the better the donation ^\
* Hospitality: Can sleep for free in villages, don't overstay your welcome otherwise relations decline ^^\
Cons: ^\
* Low Born: Nobles will take some convincing before fighting for you, suffer a 20% penalty to upkeep and higher recruitment fees for nobles"),

("dac_background_desc_healer",                    "As a healer your purpose is to treat wounds of physical or spiritual nature, there is no shortage of work for your particular skills. ^^\
Pros: ^\
* Healing Hand: Start with some skills in surgery, wound treatment and first aid ^\
* Comforting Presence: It is comforting to know that someone capable of soothing pain is in your presence, start with a higher base party morale ^^\
Cons: ^\
* Pacifist: While you have knowledge of many of man's weaknesses, you have never intentionally tried to cause harm. Start with very low combat skills"),
        
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

("dac_background_class_desc_governor",            "Governors specialize in politics and administration ^^\
Pros: ^\
* Tax Master: Reduced tax inefficiency from having multiple fiefs ^\
* Courtly Manners: Faster relationship gains with lords and ladies ^\
* Builder: Cheaper building costs, also applies to workshops ^^\
Cons: ^\
* Mostly talk: Significantly lower combat stats from lack of experience"),
("dac_background_class_desc_strategist",          "Strategists specialize in leadership roles and logistics ^^\
Pros: ^\
* Tactics and leadership: Start with higher tactics and leadership skills ^\
* Logistician: Troops consume less food and you don't have an upkeep penalty for regular troops ^^\
Cons: ^\
* Leading from Behind: You let your men do most of the fighting, as a consequence your personal combat skills have been somewhat neglected"),
("dac_background_class_desc_jouster",             "Jousters specialize in single combat and tournaments ^^\
Pros: ^\
* Regular Contestant: You receive notifications when tournaments are being held ^\
* Renowned Fighter: Increased rewards from tournaments, can place higher bets ^\
* Single Combat: Increased combat stats from frequently fighting ^^\
Cons: ^\
* Lone Wolf: Not used to leading men to combat, your leadership stats and starting party size is reduced"),         
 
("dac_background_class_desc_goods_merchant",      "Goods Merchants specialize in everything related to trading from one location to another, buy low, sell high. ^^\
Pros: ^\
* Trader by Nature: Start with high trade and persuasion skills ^\
* Caravan Master: Start with a higher inventory capacity and access to a secure secret stash ^^\
Cons: ^\
* Prime Target: Bandit aggressiveness towards your party is increased"),
("dac_background_class_desc_slaver",              "Ransom Brokers specialize in reuniting families for a fee, if the men you just captured happen to have one that can afford it, otherwise there's other ways to buy back your freedom. ^^\
Pros: ^\
* Efficient Management: The number of prisoners you can capture is based on your party size, Prisoner Management skill now acts as a 5% multiplier and also affects the sale value of prisoners. ^\
* Expanded Network: You can dispose of your prisoners at taverns by speaking to Tavern Keepers, they will demand a fee in exchange. ^^\
Cons: ^\
* Noble Disdain: When done outside the rules of Chivalry, you practice is frowned upon even though many benefit from it by virtue of keeping their lives. Nobles captured by you will decrease relations further."),
("dac_background_class_desc_investor",            "Investors specialize in buying and running bussinesses, creating an ever increasing network of merchandise. ^^\
Pros: ^\
* Diverse Assets: Can have more than one workshop in a town, cannot be of the same type as the first one ^\
* Creative Accounting: Slight improvement to the profit made by workshops ^^\
Cons: ^\
* Guild Rivalry: When a town gets captured, there's a high probability that your workshop(s) get demolished, it becomes a guarantee should it be captured by a faction hostile to you."),         
      
("dac_background_class_desc_pavoisier",           "Pavoisier"),
("dac_background_class_desc_vougier",             "Vougier"),
("dac_background_class_desc_crossbow",            "Crossbowman"),
("dac_background_class_desc_archer",              "Archer"),        
      
("dac_background_class_desc_poacher",             "Poachers are huntsmen that specialize in hunting game and foraging ^^\
Pros: ^\
* Hunting Grounds: While traveling through forests on the world map there's a chance to forage meat or fruits. ^\
* Honed Skills: You are proficient in spotting, pathfinding and tracking as well as in the use of a bow. ^^\
Cons: ^\
* Lone Wolf: Not used to leading men to combat, your leadership stats and starting party size is reduced"),
("dac_background_class_desc_manhunter",           "Manhunters or Retondeurs specialize in hunting down the bandits that ravage France, unfortunately many turned to banditry themselves as it was more rewarding than risking your life taking them down. ^^\
Pros: ^\
* A Plague on the Land: Increased rewards from taking down bandit strongholds and from capturing bandits or deserters ^\
* Less Lethal: You and your troops know how to avoid lethal strikes, making it more likely to capture prisoners even when not using blunt weapons ^^\
Cons: ^\
* Reputational Damage: Increased penalties from all hostile actions that can be considered banditry, such as attacking peasants, caravans or raiding villages"),
("dac_background_class_desc_marksman",            "Marksman"),      
         
("dac_background_class_desc_condottiero",         "Condottiero"),
("dac_background_class_desc_sellsword",           "Sellsword"),
("dac_background_class_desc_pikeman",             "Pikeman"),
("dac_background_class_desc_crossbowman",         "Crossbowman"),     
      
("dac_background_class_desc_farmer",              "Farmer"),
("dac_background_class_desc_rebel",               "Rebel"),
("dac_background_class_desc_smith",               "Smith"),        

("dac_background_class_desc_surgeon",             "Surgeons specialize in handling grave injuries that require immediate attention, few things qualify as urgent as battlefield injuries. ^^\
Pros: ^\
* Battlefield Surgery: Your forces are more likely to suffer non-fatal injuries on the field, you also able to save some of your foes which results in more potential prisoners ^\
* Intervention: Once a day, can perform an intervention on one of the party's heroes that is too wounded to fight, bringing the hero back into fighting condition ^^\
Cons: ^\
* Save Yourselves: Suffer a greater morale penalty in battle should you be knocked out"),
("dac_background_class_desc_priest",              "Priest"),
("dac_background_class_desc_alchemist",           "Alchemist"),

### DAC Seek: The legendary Lorem Ipsum
("lorem_ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"),

]