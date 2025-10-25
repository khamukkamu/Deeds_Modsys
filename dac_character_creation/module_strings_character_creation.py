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
("dac_weapon_proficiencies",                      "Weapon Proficiencies"),
("dac_wpt_onehanded",                             "Onehanded"),
("dac_wpt_twohanded",                             "Twohanded"),
("dac_wpt_polearms",                              "Polearms"),
("dac_wpt_archery",                               "Bows"),
("dac_wpt_crossbow",                              "Crossbows"),
("dac_wpt_throwing",                              "Throwing"),
("dac_wpt_firearm",                               "Firearm"),

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
» One of Us: ^\
20% Reduction on upkeep and recruitment costs for Knights ^\
» Tutors: ^\
Start with a decent mix of skills ^^\
Cons: ^\
» One of them: ^\
20% upkeep penalty for regular troops, does not apply to mercenaries ^\
» Valuable target: ^\
Your ransom value is much higher should you be captured"),

("dac_background_desc_merchant",                  "As a merchant you make a living from trade, what exactly that trade entails is up to you but you are good at seizing opportunities as they arise and getting the most out of it. ^^\
Pros: ^\
» Business Minded: ^\
Start with higher trade, persuasion and inventory management skills. ^\
» Negotiator: ^\
Can use trade or persuasion skills to get out of disadvantageous situations such as getting caught by enemies or just doing business ^^\
Cons: ^\
» Not a Fighter: ^\
Start with low combat related skills and proficiencies."),

("dac_background_desc_soldier",                   "As a soldier you know well enough about combat and your fellow soldiers, their needs and wants, how logistics work and how battles are fought and won. ^^\
Pros: ^\
» Logistics: ^\
You have spent quite some time on the road, foraging, scouting and setting up camps ^\
» One of us: ^\
Commoners recognize you as one of their own, pay 20% less upkeep for regular troops ^^\
Cons: ^\
» Low Born: ^\
Nobles are reluctant to serve under your freshly earned banner, pay 20% more upkeep for noble troops"),

("dac_background_desc_hunter",                    "As a hunter you know how to move around, how to track and stalk your prey. Those skills are vital in an unforgiving world. ^^\
Pros: ^\
» Foraging: ^\
Your supplies of food last longer as your party will consume 33% less food ^\
» Scouting: ^\
Receive a notification when spotting a hostile party stronger than yours on the world map ^^\
Cons: ^\
» Keep Your Distance: ^\
You are used to eliminating threats before they can close the distance and thus are ill prepared for close combat"),

("dac_background_desc_mercenary",                 "As a mercenary your services are in high demand in these tumultuous times yet trust is hard to gain when your only alliegeance is to gold. ^^\
Pros: ^\
» Contracts and Contacts: ^\
Mercenary recruitment and upkeep is significantly reduced ^\
» Grand Company: ^\
Factions are more likely to provide you with mercenary contracts, rewards are increased ^^\
Cons: ^\
» Villainous Lot: ^\
Mercenaries are often compromising of veterans, deserters, bandits and naïve recruits who don't always go along. Base morale is lower and suffer higher morale penalties from events, such as lack of food, retreat or defeat.^\
» Lofty Ambitions: ^\
Nobles are very suspicious towards your true loyalties, requirements to join a faction are higher and should you try to form a kingdom of your own, neutral factions are likely to declare war on you."),

("dac_background_desc_peasant",                   "As a peasant your life is one of toil and survival. While there are opportunities to achieve greater deeds, it will feel like the odds are stacked against you. ^^\
Pros: ^\
» Solidarity: ^\
Can ask villages for donations, the higher the relations with the village, the better the donation ^\
» Hospitality: ^\
Can sleep for free in villages, don't overstay your welcome otherwise relations decline ^^\
Cons: ^\
» Low Born: ^\
Nobles will take some convincing before fighting for you, suffer a 20% penalty to upkeep and higher recruitment fees for nobles"),

("dac_background_desc_healer",                    "As a healer your purpose is to treat wounds of physical or spiritual nature, there is no shortage of work for your particular skills. ^^\
Pros: ^\
» Healing Hand: ^\
Start with some skills in surgery, wound treatment and first aid ^\
» Comforting Presence: ^\
It is comforting to know that someone capable of soothing pain is in your presence, start with a higher base party morale ^^\
Cons: ^\
» Pacifist: ^\
While you have knowledge of many of man's weaknesses, you have never intentionally tried to cause harm. Start with very low combat skills"),
        
("dac_background_class_governor",                 "Governor"),
("dac_background_class_strategist",               "Strategist"),
("dac_background_class_jouster",                  "Jouster"),          
("dac_background_class_goods_merchant",           "Goods Merchant"),
("dac_background_class_slaver",                   "Ransom Broker"),
("dac_background_class_investor",                 "Investor"),               
("dac_background_class_scout",                    "Scout"),
("dac_background_class_quartermaster",            "Quartermaster"),
("dac_background_class_cook",                     "Cook"),
("dac_background_class_sergeant",                 "Sergeant"),              
("dac_background_class_poacher",                  "Poacher"),
("dac_background_class_manhunter",                "Manhunter"),
("dac_background_class_marksman",                 "Marksman"),               
("dac_background_class_condottiero",              "Condottiero"),
("dac_background_class_flemish",                  "Flemish Mercenary"),
("dac_background_class_scottish",                 "Scottish Noble"),        
("dac_background_class_farmer",                   "Farmer"),
("dac_background_class_rebel",                    "Rebel"),
("dac_background_class_smith",                    "Smith"),        
("dac_background_class_surgeon",                  "Surgeon"),
("dac_background_class_priest",                   "Priest"),
("dac_background_class_alchemist",                "Alchemist"),

("dac_background_class_desc_governor",            "Governors specialize in politics and administration ^^\
Pros: ^\
» Tax Master: ^\
Reduced tax inefficiency from having multiple fiefs, +2 to the number of fiefs required until tax inefficiency takes effect, 20% penalty reduction on tax loss and tax loss capped at 50% instead of 65% of tax income ^\
» Courtly Manners: ^\
Faster relationship gains with lords and ladies, extra points awarded whenever relationship is earned ^\
» Builder: ^\
Cheaper building costs, also applies to workshops ^^\
Cons: ^\
» Mostly talk: ^\
Significantly lower combat stats from lack of experience"),
("dac_background_class_desc_strategist",          "Strategists specialize in leadership roles and logistics ^^\
Pros: ^\
» Tactics and leadership: ^\
Start with higher tactics, leadership skills and base party size^\
» Logistician: ^\
Troops consume less food and you don't have an upkeep penalty for regular troops ^^\
Cons: ^\
» Leading from Behind: ^\
You let your men do most of the fighting, as a consequence your personal combat skills have been somewhat neglected"),
("dac_background_class_desc_jouster",             "Jousters specialize in single combat and tournaments ^^\
Pros: ^\
» Regular Contestant: ^\
You receive notifications when tournaments are being held ^\
» Renowned Fighter: ^\
You can participate in tournaments from the start, increased rewards from tournaments and can place higher bets ^\
» Single Combat: ^\
Increased combat stats from frequently fighting ^^\
Cons: ^\
» Lone Wolf: ^\
Not used to leading men to combat, your leadership stats and starting party size is reduced"),         
 
("dac_background_class_desc_goods_merchant",      "Goods Merchants specialize in everything related to trading from one location to another, buy low, sell high. ^^\
Pros: ^\
» Trader by Nature: ^\
Start with high trade and persuasion skills ^\
» Caravan Master: ^\
Start with a higher inventory capacity and access to a secure upgradeable secret stash accessible from the camp menu under 'Take an Action' ^^\
Cons: ^\
» Prime Target: ^\
Bandit aggressiveness towards your party is doubled, aggressiveness is based on your wealth and quantity of goods carried"),
("dac_background_class_desc_slaver",              "Ransom Brokers specialize in reuniting families for a fee, if the men you just captured happen to have one that can afford it, otherwise there's other ways to buy back your freedom. ^^\
Pros: ^\
» Efficient Management: ^\
The number of prisoners you can capture is based on your party size, Prisoner Management skill now acts as a 5% multiplier and also affects the sale value of prisoners. ^\
» Expanded Network: ^\
You can dispose of your prisoners at taverns by speaking to Tavern Keepers, they will demand a fee in exchange. ^^\
Cons: ^\
» Noble Disdain: ^\
Increased relation penalties from capturing nobles."),
("dac_background_class_desc_investor",            "Investors specialize in buying and running bussinesses, creating an ever increasing network of merchandise. ^^\
Pros: ^\
» Diverse Assets: ^\
Can have more than one workshop in a town, cannot be of the same type as the first one ^\
» Creative Accounting: ^\
Slight improvement to the profit made by workshops ^^\
Cons: ^\
» Guild Rivalry: ^\
When a town gets captured, there's a high probability that your workshop(s) get demolished, it becomes a guarantee should it be captured by a faction hostile to you."),         
      
("dac_background_class_desc_scout",                 "Scouts specialize in traversing terrain and quickly identifying threats at a distance ^^\
Pros: ^\
» Scouting: ^\
Receive a notification when spotting a hostile party stronger than yours on the world map while quick-traveling (Ctrl + Space)^\
» Wayfarer: ^\
Traversing forests on the world map doesn't slow you down as much ^^\
» On the Double: ^\
Increased speed bonus from forced march, press 'Left Shift' on the world map to force march, press again to cancel ^\
Cons: ^\
» Travel Light: ^\
Suffer increased penalties from inventory encumbrance which is capped at 20% of your party speed, can be offset by having horses in your inventory"),
("dac_background_class_desc_quartermaster",         "Quartermasters specialize in keeping the army well supplied ^^\
Pros: ^\
» Ammo Reserves: ^\
Can resupply ranged troops ammo during battles ^\
» Supply Master: ^\
Start with a higher inventory capacity and access to a secure upgradeable secret stash accessible from the camp menu under 'Take an Action' ^^\
Cons: ^\
» Hoarder: You tend to collect useless junk, just in case, slowing your movement on the campaign map by 6% (equal to 2 levels of pathfinding skill)"),
("dac_background_class_desc_cook",                  "Cooks specialize in keeping the troops happy and well-fed ^^\
Pros: ^\
» Master Chef: ^\
Get a variety of new bonuses from food ^\
» Enticing Odour: ^\
Higher probability of success when attempting to recruit prisoners, captured enemy lords are less likely to escape ^^\
Cons: ^\
» Glutons: ^\
Negates the food consumption reduction from the soldier class, the party instead consumes more food"),
("dac_background_class_desc_sergeant",              "Sergeants specialize in keeping the troops drilled and motivated ^^\
Pros: ^\
» Marching Songs: ^\
Reduced morale penalty from forced march, press 'Left Shift' on the world map to force march, press again to cancel ^\
» Motivational Speeches: ^\
Troops are emboldened by your speeches, and curses, you start with higher base morale for your party ^^\
Cons: ^\
» Save Yourselves: ^\
Suffer a greater morale penalty in battle should you be knocked out"),        
      
("dac_background_class_desc_poacher",             "Poachers are huntsmen that specialize in hunting game and foraging ^^\
Pros: ^\
» Hunting Grounds: ^\
While traveling through forests on the world map there's a chance to forage meat or fruits. ^\
» Honed Skills: ^\
You are proficient in spotting, pathfinding and tracking as well as in the use of a bow. ^^\
Cons: ^\
» Lone Wolf: ^\
Not used to leading men to combat, your leadership stats and starting party size is reduced"),
("dac_background_class_desc_manhunter",           "Manhunters or Retondeurs specialize in hunting down the bandits that ravage France, unfortunately many turned to banditry themselves as it was more rewarding than risking your life taking them down. ^^\
Pros: ^\
» Bounty Hunters: ^\
Kill bandits and collect bounties with Guildmasters, increased rewards from destroying bandit strongholds ^\
» Restraint: ^\
You and your troops know how to avoid lethal strikes, making it more likely to capture prisoners even when not using blunt weapons ^^\
Cons: ^\
» Reputational Damage: ^\
Increased penalties from all hostile actions that can be considered banditry, such as attacking peasants, caravans or raiding villages"),
("dac_background_class_desc_marksman",            "Marksmen are professionals that earn a living showing off their skills in ranged weaponry ^^\
Pros: ^\
» Showoff: ^\
Gain renown when landing difficult shots in battle ^\
» Skilled: ^\
Start with good stats on everything related to ranged weapons ^^\
Cons : ^\
» Not a Warrior: ^\
Start with bad stats on everything related to close combat"),      
         
("dac_background_class_desc_condottiero",         "Condottieri are prized mercenary leaders who earned their fame from selling their services in Italy ^^\
Pros: ^\
» Established Company: ^\
Start with an already built tier 2 mercenary camp ^\
» Italian Ties: ^\
Can recruit Italian mercenaries in your camp ^^\
Cons: ^\
» Expensive Tastes: ^\
Your troops have acquired some expensive tastes while campaigning in Italy and demand to have wine and a diverse food regiment or suffer morale penalties"),
("dac_background_class_desc_flemish",             "Flemish mercenaries start venturing into France as the French lead some reprisal campaigns and as the Duchy of Burgundy expands ^^\
Pros: ^\
» Close Knit: ^\
Flemish mercenaries have increased combat stats ^\
» Flemish Ties: ^\
Can recruit Flemish mercenaries in your camp ^^\
Cons: ^\
» Noble Disdain: ^\
You didn't offer any quarters in the past and none will be offered to you in the present, impossible to negotiate your way out of a battle"),
("dac_background_class_desc_scottish",            "[WIP] ^\
The Scottish were one of the main allies of France during the Hundred Years War, united by common hatred of the English crown, many have fallen fighting to the bitter end in France. ^^\
Pros: ^\
» Auld Alliance: ^\
Start with good relations with the Kingdom of France and negates the effects of Villainous Lot ^\
[WIP] » Kinsmen: ^\
Can recruit Scottish troops at a special location, enhanced stats for Scottish troops ^^\
Cons: ^\
» Last Stand: ^\
Scottish troops fight to the bitter end, should you retreat from a battle, they will be wiped out ^\
» Bitter Enemies: ^\
Start with bad relations with the Kingdom of England"),   
      
("dac_background_class_desc_farmer",              "Farmers are simple folk that live off the land, toiling away to feed themselves, their family and the real. War comes even to those that bother none, turmoil has reached and razed your village. Bandits, nobles, doesn't matter, you have nothing left here and must start life anew. ^^\
Pros: ^\
» Life of Toil: ^\
Can work in villages in exchange for a wage and produce ^\
» Happy Camper: ^\
Morale bonus from food diversity is increased ^^\
Cons: ^\
» Starting Over: ^\
You own very little other than the clothes on your back"),
("dac_background_class_desc_rebel",               "Rebels are those that have lost everything and lash out against the world enacting mob justice on those they consider to have wronged them ^^\
Pros: ^\
» We Are Legion: ^\
Party size increased, can recruit rebellious peasant parties to your cause ^\
» Takeover: ^\
Instead of destroying bandit camps, you can chose to take over them ^^\
Cons: ^\
» Bellum Omnium Contra Omnes: ^\
All factions start hostile towards you."),
("dac_background_class_desc_smith",               "Smiths are one of the cornerstones of society, crafting and mending tools necessary for the other professions to perform well ^^\
Pros: ^\
» Repairs: ^\
Can repair and mend weapons and armour back to regular condition ^\
» Crafty: ^\
Research and costs are reduced when producing items for your personal troops at your camp ^^\
Cons: ^\
Noxious Fumes: ^\
Years of working the forge has had a toll on your health, you can suffer decreased stats after being knocked down"),        

("dac_background_class_desc_surgeon",             "Surgeons specialize in handling grave injuries that require immediate attention, few things qualify as urgent as battlefield injuries. ^^\
Pros: ^\
» Battlefield Surgery: ^\
Your forces are more likely to suffer non-fatal injuries on the field, you also able to save some of your foes which results in more potential prisoners ^\
» Intervention: ^\
Once a day, can perform an intervention on one of the party's heroes that is too wounded to fight, bringing the hero back into fighting condition ^^\
Cons: ^\
» Save Yourselves: ^\
Suffer a greater morale penalty in battle should you be knocked out"),
("dac_background_class_desc_priest",              "Priests specialize in the salvation of the eternal soul. You have your own interpretation on how this is to be achieved, going on a personal crusade but beware not to lose yours on the way. ^^\
Pros: ^\
» Zealots: ^\
Troops under your command fight to the bitter end ^\
» Man of the Cloth: ^\
Your foes are more likely to release you unnarmed ^^\
Cons: ^\
» Heresy: ^\
You are sworn not to kill by your own hand and to protect the innocent, breaking those vows will have you branded as a heretic and will have dire consequences"),
("dac_background_class_desc_alchemist",           "Alchemists specialize in the arcane and esoteric studies, whilst many are consumed by the search for the elusive philosopher's stone you personally focus on experiments that provide more immediate results and can be repeated. ^^\
Pros: ^\
» Potions And Draughts: ^\
Can craft a few potions and draughts that can heal you or provide bonuses during battles ^\
» Artefact Of Antioch: ^\
Look for the fabled Holy Hand Grenade of Antioch ^^\
Cons: ^\
» Dangerous Experiments: ^\
There is always a chance for your experiments to backfire, causing you harm"),

### DAC Seek: The legendary Lorem Ipsum
("lorem_ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"),

### DAC Seek: Descriptions for feature toggle option
("dac_noble_jouster_toggle_on", "[Jouster] Enable invitations to tournaments"),
("dac_noble_jouster_toggle_off", "[Jouster] Disable invitations to tournaments"),
("dac_soldier_scout_toggle_on", "[Scout] Enable party scouting"),
("dac_soldier_scout_toggle_off", "[Scout] Disable party scouting"),
("dac_hunter_toggle_on", "[Hunter] Enable party scouting"),
("dac_hunter_toggle_off", "[Hunter] Disable party scouting"),

### DAC Seek: Hidden Player Chest
("dac_chest_no_item", "There are currently zero items"),
("dac_chest_one_item", "There is one item"),
("dac_chest_many_items", "There are {reg3} items"),

### DAC Lock Tournaments
("dac_tournament", "You are not renowned enough to participate in a tournament yet, 160 renown required"),

### DAC Forage
("dac_successfully_foraged_s1", "You successfully foraged some {s1}"),
### DAC Mercenaries Happiness
("dac_mercs_happy", "Your party is content with the wine and food content"),
("dac_mercs_sad", "Your party is discontent with the lack of wine and/or food variety"),
]