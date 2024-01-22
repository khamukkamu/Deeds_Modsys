from header_music import *

from compiler import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [

  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen_old", "DAC-Title-Old.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0), #Old HYW Title Song
  ("mount_and_blade_title_screen", "DAC-Title.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0), #BenjaminR Deeds of Arms & Chivalry (Feb 3, 2020)

# DAC Changes Begin

# Arena (initiation of arena, tourney, and duel)
  ("DAC-Battle-Epic-26", "Battle/DAC-Battle-Epic-26.ogg", mtf_module_track|mtf_sit_arena|mtf_start_immediately, mtf_culture_all),

# Ambush = Epic (num combatants >= 150)

  ("DAC-Battle-Epic-1",  "Battle/DAC-Battle-Epic-1.ogg",  mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-2",  "Battle/DAC-Battle-Epic-2.ogg",  mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-3",  "Battle/DAC-Battle-Epic-3.ogg",  mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-4",  "Battle/DAC-Battle-Epic-4.ogg",  mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
#  ("DAC-Battle-Epic-5",  "Battle/DAC-Battle-Epic-5.ogg",  mtf_module_track|mtf_sit_ambushed, mtf_culture_all), #ijustwant2bpure i suggest dropping this one, something weird happened to the audio quality and it is kind of short but also not very loopable.
  ("DAC-Battle-Epic-6",  "Battle/DAC-Battle-Epic-6.ogg",  mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-7",  "Battle/DAC-Battle-Epic-7.ogg",  mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-8",  "Battle/DAC-Battle-Epic-8.ogg",  mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-9",  "Battle/DAC-Battle-Epic-9.ogg",  mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-10", "Battle/DAC-Battle-Epic-10.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-11", "Battle/DAC-Battle-Epic-11.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-12", "Battle/DAC-Battle-Epic-12.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-13", "Battle/DAC-Battle-Epic-13.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-14", "Battle/DAC-Battle-Epic-14.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-15", "Battle/DAC-Battle-Epic-15.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-16", "Battle/DAC-Battle-Epic-16.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
#  ("DAC-Battle-Epic-17", "Battle/DAC-Battle-Epic-17.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all), #ijustwant2bpure - i think this one is too short and not very loopable
  ("DAC-Battle-Epic-18", "Battle/DAC-Battle-Epic-18.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-19", "Battle/DAC-Battle-Epic-19.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-20", "Battle/DAC-Battle-Epic-20.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-21", "Battle/DAC-Battle-Epic-21.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-22", "Battle/DAC-Battle-Epic-22.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-23", "Battle/DAC-Battle-Epic-23.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-24", "Battle/DAC-Battle-Epic-24.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-25", "Battle/DAC-Battle-Epic-25.ogg", mtf_module_track|mtf_sit_ambushed|mtf_looping, mtf_sit_fight),
  ("DAC-Battle-Epic-27", "Battle/DAC-Battle-Epic-27.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-28", "Battle/DAC-Battle-Epic-28.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),

# Bandit Epic (num combatants >= 50),
  ("DAC-Battle-Bandits-1", "Battle/DAC-Battle-Bandits-1.mp3", mtf_module_track|mtf_sit_ambushed|mtf_culture_6, 0),
  ("DAC-Battle-Bandits-2", "Battle/DAC-Battle-Bandits-2.ogg", mtf_module_track|mtf_sit_ambushed|mtf_culture_6, 0), #BenjaminR Silver Plate (Jan 13, 2020)
  ("DAC-Battle-Bandits-3", "Battle/DAC-Battle-Bandits-3.mp3", mtf_module_track|mtf_sit_ambushed|mtf_culture_6, 0), #BenjaminR OneOSix (May 5, 2020)

# DAC Generic Battle Music (Ambient Sound [for now])

  ("DAC-Battle-Generic-1", "Battle/DAC-Battle-Generic-1.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-2", "Battle/DAC-Battle-Generic-2.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-3", "Battle/DAC-Battle-Generic-3.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-4", "Battle/DAC-Battle-Generic-4.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-5", "Battle/DAC-Battle-Generic-5.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-6", "Battle/DAC-Battle-Generic-6.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-7", "Battle/DAC-Battle-Generic-7.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-8", "Battle/DAC-Battle-Generic-8.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),
  ("DAC-Battle-Generic-9", "Battle/DAC-Battle-Generic-9.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_arena, 0),

# DAC Siege Music

  ("DAC-Battle-Siege-1",  "Battle/Siege/DAC-Battle-Siege-1.ogg",  mtf_module_track|mtf_sit_siege, 0),
  ("DAC-Battle-Siege-2",  "Battle/Siege/DAC-Battle-Siege-2.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-3",  "Battle/Siege/DAC-Battle-Siege-3.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-4",  "Battle/Siege/DAC-Battle-Siege-4.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-5",  "Battle/Siege/DAC-Battle-Siege-5.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-6",  "Battle/Siege/DAC-Battle-Siege-6.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-7",  "Battle/Siege/DAC-Battle-Siege-7.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-8",  "Battle/Siege/DAC-Battle-Siege-8.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-9",  "Battle/Siege/DAC-Battle-Siege-9.ogg",  mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-10", "Battle/Siege/DAC-Battle-Siege-10.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-11", "Battle/Siege/DAC-Battle-Siege-11.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-12", "Battle/Siege/DAC-Battle-Siege-12.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-13", "Battle/Siege/DAC-Battle-Siege-13.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-14", "Battle/Siege/DAC-Battle-Siege-14.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-15", "Battle/Siege/DAC-Battle-Siege-15.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-16", "Battle/Siege/DAC-Battle-Siege-16.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-17", "Battle/Siege/DAC-Battle-Siege-17.ogg", mtf_module_track|mtf_sit_siege, 0),  

# DAC Travel Music
# Breton

  ("DAC-Travel-Breton-1",  "Travel/Breton/DAC-Travel-Breton-1.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-2",  "Travel/Breton/DAC-Travel-Breton-2.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-3",  "Travel/Breton/DAC-Travel-Breton-3.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-4",  "Travel/Breton/DAC-Travel-Breton-4.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-5",  "Travel/Breton/DAC-Travel-Breton-5.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-6",  "Travel/Breton/DAC-Travel-Breton-6.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-7",  "Travel/Breton/DAC-Travel-Breton-7.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-8",  "Travel/Breton/DAC-Travel-Breton-8.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-9",  "Travel/Breton/DAC-Travel-Breton-9.mp3",  mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-10", "Travel/Breton/DAC-Travel-Breton-10.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-11", "Travel/Breton/DAC-Travel-Breton-11.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-12", "Travel/Breton/DAC-Travel-Breton-12.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-13", "Travel/Breton/DAC-Travel-Breton-13.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-14", "Travel/Breton/DAC-Travel-Breton-14.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-15", "Travel/Breton/DAC-Travel-Breton-15.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-16", "Travel/Breton/DAC-Travel-Breton-16.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),

# English

  ("DAC-Travel-England-1", "Travel/English/DAC-Travel-England-1.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-2", "Travel/English/DAC-Travel-England-2.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-3", "Travel/English/DAC-Travel-England-3.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-4", "Travel/English/DAC-Travel-England-4.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-5", "Travel/English/DAC-Travel-England-5.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-6", "Travel/English/DAC-Travel-England-6.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-7", "Travel/English/DAC-Travel-England-7.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-8", "Travel/English/DAC-Travel-England-8.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-England-9", "Travel/English/DAC-Travel-England-9.mp3", mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_travel),

# French

  ("DAC-Travel-France-1",  "Travel/French/DAC-Travel-France-1.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-2",  "Travel/French/DAC-Travel-France-2.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-3",  "Travel/French/DAC-Travel-France-3.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-4",  "Travel/French/DAC-Travel-France-4.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-5",  "Travel/French/DAC-Travel-France-5.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-6",  "Travel/French/DAC-Travel-France-6.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-7",  "Travel/French/DAC-Travel-France-7.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-8",  "Travel/French/DAC-Travel-France-8.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-9",  "Travel/French/DAC-Travel-France-9.mp3",  mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-10", "Travel/French/DAC-Travel-France-10.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-11", "Travel/French/DAC-Travel-France-11.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-12", "Travel/French/DAC-Travel-France-12.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-13", "Travel/French/DAC-Travel-France-13.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-14", "Travel/French/DAC-Travel-France-14.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-15", "Travel/French/DAC-Travel-France-15.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),

# Burgandy

  ("DAC-Travel-Burgandy-1",  "Travel/Burgandy/DAC-Travel-Burgandy-1.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-2",  "Travel/Burgandy/DAC-Travel-Burgandy-2.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-3",  "Travel/Burgandy/DAC-Travel-Burgandy-3.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-4",  "Travel/Burgandy/DAC-Travel-Burgandy-4.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-5",  "Travel/Burgandy/DAC-Travel-Burgandy-5.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-6",  "Travel/Burgandy/DAC-Travel-Burgandy-6.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-7",  "Travel/Burgandy/DAC-Travel-Burgandy-7.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-8",  "Travel/Burgandy/DAC-Travel-Burgandy-8.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-9",  "Travel/Burgandy/DAC-Travel-Burgandy-9.mp3",  mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-10", "Travel/Burgandy/DAC-Travel-Burgandy-10.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-11", "Travel/Burgandy/DAC-Travel-Burgandy-11.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-12", "Travel/Burgandy/DAC-Travel-Burgandy-12.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-13", "Travel/Burgandy/DAC-Travel-Burgandy-13.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-14", "Travel/Burgandy/DAC-Travel-Burgandy-14.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-15", "Travel/Burgandy/DAC-Travel-Burgandy-15.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-16", "Travel/Burgandy/DAC-Travel-Burgandy-16.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-17", "Travel/Burgandy/DAC-Travel-Burgandy-17.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-18", "Travel/Burgandy/DAC-Travel-Burgandy-18.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-19", "Travel/Burgandy/DAC-Travel-Burgandy-19.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-20", "Travel/Burgandy/DAC-Travel-Burgandy-20.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-21", "Travel/Burgandy/DAC-Travel-Burgandy-21.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-22", "Travel/Burgandy/DAC-Travel-Burgandy-22.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-23", "Travel/Burgandy/DAC-Travel-Burgandy-23.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-24", "Travel/Burgandy/DAC-Travel-Burgandy-24.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-25", "Travel/Burgandy/DAC-Travel-Burgandy-25.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-26", "Travel/Burgandy/DAC-Travel-Burgandy-26.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-27", "Travel/Burgandy/DAC-Travel-Burgandy-27.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-28", "Travel/Burgandy/DAC-Travel-Burgandy-28.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),

# Court
  ("DAC-Court-Generic-1", "DAC-Court-Generic-1.mp3", mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("DAC-Court-Generic-2", "DAC-Court-Generic-2.ogg", mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all), 

# Town
  ("DAC-Town-Generic-1",  "Town/DAC-Town-Generic-1.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-2",  "Town/DAC-Town-Generic-2.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-3",  "Town/DAC-Town-Generic-3.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-4",  "Town/DAC-Town-Generic-4.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-5",  "Town/DAC-Town-Generic-5.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-6",  "Town/DAC-Town-Generic-6.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-7",  "Town/DAC-Town-Generic-7.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-8",  "Town/DAC-Town-Generic-8.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-9",  "Town/DAC-Town-Generic-9.ogg",  mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night), 
  ("DAC-Town-Generic-10", "Town/DAC-Town-Generic-10.ogg", mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night), 
  ("DAC-Town-Generic-11", "Town/DAC-Town-Generic-11.ogg", mtf_module_track|mtf_sit_town, mtf_sit_town|mtf_sit_tavern|mtf_sit_night), 

# Tavern
  ("DAC-Tavern-Generic-1", "Tavern/DAC-Tavern-Generic-1.ogg", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),
  ("DAC-Tavern-Generic-2", "Tavern/DAC-Tavern-Generic-2.ogg", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),
  ("DAC-Tavern-Generic-3", "Tavern/DAC-Tavern-Generic-3.ogg", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0), 
  ("DAC-Tavern-Generic-4", "Tavern/DAC-Tavern-Generic-4.ogg", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0), 
  ("DAC-Tavern-Generic-5", "Tavern/DAC-Tavern-Generic-5.ogg", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0), 

# Feast
  ("DAC-Feast-Generic-1", "DAC-Feast-Generic-1.ogg", mtf_module_track|mtf_sit_feast, 0), 

# Defeat
  ("DAC-Defeat-1", "Defeat/DAC-Defeat-1.ogg", mtf_module_track|mtf_sit_killed, mtf_sit_travel),
  ("DAC-Defeat-2", "Defeat/DAC-Defeat-2.ogg", mtf_module_track|mtf_sit_killed, mtf_sit_travel),
  ("DAC-Defeat-3", "Defeat/DAC-Defeat-3.ogg", mtf_module_track|mtf_sit_killed, mtf_sit_travel),
  ("DAC-Defeat-4", "Defeat/DAC-Defeat-4.ogg", mtf_module_track|mtf_sit_killed, mtf_sit_travel),
  ("DAC-Defeat-5", "Defeat/DAC-Defeat-5.ogg", mtf_module_track|mtf_sit_killed, mtf_sit_travel),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished|mtf_sit_killed, 0), # Native

# Infiltration

  ("calm_night_2", "calm_night_2.ogg", mtf_sit_town_infiltrate, 0), #Native

# Victory
  ("victorious_evil",  "victorious_evil.ogg",          mtf_sit_victorious, 0),
  ("escape",           "escape.ogg",                   mtf_sit_victorious, 0),
  
  ("DAC-Victorious-1", "Victory/DAC-Victorious-1.ogg", mtf_module_track|mtf_sit_victorious, mtf_sit_travel),
  ("DAC-Victorious-2", "Victory/DAC-Victorious-2.ogg", mtf_module_track|mtf_sit_victorious, mtf_sit_travel),
  ("DAC-Victorious-3", "Victory/DAC-Victorious-3.ogg", mtf_module_track|mtf_sit_victorious, mtf_sit_travel),
  ("DAC-Victorious-4", "Victory/DAC-Victorious-4.ogg", mtf_module_track|mtf_sit_victorious, mtf_sit_travel),
  ("DAC-Victorious-5", "Victory/DAC-Victorious-5.ogg", mtf_module_track|mtf_sit_victorious, mtf_sit_travel),

# DAC Changes END

# Native Music Starts Here. Will need to be replaced  
 
  #("defeated_by_neutral", "defeated_by_neutral.ogg",mtf_persist_until_finished|mtf_sit_killed, 0),
  #("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  #("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  #("killed_by_khergit", "killed_by_khergit.ogg", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
#  ("killed_by_neutral", "killed_by_neutral.ogg", mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed, 0),
#  ("killed_by_nord", "killed_by_nord.ogg", mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed, 0),
#  ("killed_by_rhodok", "killed_by_rhodok.ogg", mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed, 0),
  #("killed_by_swadian", "killed_by_swadian.ogg", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
#  ("killed_by_vaegir", "killed_by_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed, 0),

  #("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  #("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  #("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  #("victorious_swadian", "victorious_swadian.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  #("victorious_vaegir", "victorious_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  #("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),


  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),


## BenjaminR Tracks NOT YET Added
# Across the Eight Hills (Jan 25, 2020) - Kham: Maybe victory music?
# CeF (Feb 4, 2020) - Kham: Sounds East Asian?
# 18.2 (Feb 18, 2020) - Kham: bit too fan-fareish? Could be feast music
# Victory 3 (Feb 19, 2020) - Kham: cuts too short? too long?
# Battle Music (Feb 21, 2020) - Kham: Prolonged version of Victory 2 to become battle music
# For Glory (Apr 26, 2020) - Kham: Might be too epic lol
# TenFiveTwo... (May 10, 2020) - Kham: Not sure where to put this... Sounds like battle / travel. Gives a feel of adventure, definitely.
# Tsueseki (May 31, 2020) - Kham: Had a good beginning, then became too crazy for us :D
# A Spring March in the Orleans Forest (Jun 10, 2020) - Kham - Bit too fan-fareish again.
# Thieves and Beggards (Jun 11, 2020) - Kham - Was OK in the beginning, good epic bandit music, then became too bouncy at the end 
# Royal Oak (Jun 11, 2020) - Kham - Tavern or feast music, but got too fast for me :O
# Paramount (Jul 4, 2020) - Kham - Not for us
# 4.7 test (Jul 4, 2020) - Kham - too vocal
# test 10 (Jul 10, 2020) - Kham - Epic battle? Siege?
# Revised music (except travel), added tracks from BenjaminR (Jan 6, 2023) - Seek

]
