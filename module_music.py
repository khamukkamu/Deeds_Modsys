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
  ("mount_and_blade_title_screen", "DAC-Title.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),


# DAC Changes Begin
# Ambush = Epic (num combatants >= 150)

  ("DAC-Battle-Epic-1", "Battle/DAC-Battle-Epic-1.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-2", "Battle/DAC-Battle-Epic-2.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-3", "Battle/DAC-Battle-Epic-3.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-4", "Battle/DAC-Battle-Epic-4.mp3", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-5", "Battle/DAC-Battle-Epic-3.mp3", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("DAC-Battle-Epic-6", "Battle/DAC-Battle-Epic-6.ogg", mtf_module_track|mtf_sit_ambushed, mtf_culture_all),

# Bandit Epic (num combatants >= 50),
  ("DAC-Battle-Bandits-1", "DAC-Battle-Bandits-1.mp3", mtf_module_track|mtf_sit_ambushed|mtf_culture_6, 0),

# DAC Generic Battle Music (Ambient Sound [for now])

  ("DAC-Battle-Generic-1", "Battle/DAC-Battle-Generic-1.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-2", "Battle/DAC-Battle-Generic-2.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-3", "Battle/DAC-Battle-Generic-3.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-4", "Battle/DAC-Battle-Generic-4.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-5", "Battle/DAC-Battle-Generic-5.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-6", "Battle/DAC-Battle-Generic-6.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-7", "Battle/DAC-Battle-Generic-7.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-8", "Battle/DAC-Battle-Generic-8.ogg", mtf_module_track|mtf_sit_fight, 0),
  ("DAC-Battle-Generic-9", "Battle/DAC-Battle-Generic-9.ogg", mtf_module_track|mtf_sit_fight, 0),

# DAC Siege Music

  ("DAC-Battle-Siege-1", "DAC-Battle-Siege-1.mp3", mtf_module_track|mtf_sit_siege, 0),
  ("DAC-Battle-Siege-2", "DAC-Battle-Siege-2.ogg", mtf_module_track|mtf_sit_siege, 0),  
  ("DAC-Battle-Siege-3", "DAC-Battle-Siege-3.ogg", mtf_module_track|mtf_sit_siege, 0),  

# DAC Travel Music
# Breton

  ("DAC-Travel-Breton-1", "Travel/Breton/DAC-Travel-Breton-1.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-2", "Travel/Breton/DAC-Travel-Breton-2.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-3", "Travel/Breton/DAC-Travel-Breton-3.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-4", "Travel/Breton/DAC-Travel-Breton-4.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-5", "Travel/Breton/DAC-Travel-Breton-5.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-6", "Travel/Breton/DAC-Travel-Breton-6.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-7", "Travel/Breton/DAC-Travel-Breton-7.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-8", "Travel/Breton/DAC-Travel-Breton-8.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Breton-9", "Travel/Breton/DAC-Travel-Breton-9.mp3", mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_travel),
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

  ("DAC-Travel-France-1", "Travel/French/DAC-Travel-France-1.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-2", "Travel/French/DAC-Travel-France-2.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-3", "Travel/French/DAC-Travel-France-3.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-4", "Travel/French/DAC-Travel-France-4.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-5", "Travel/French/DAC-Travel-France-5.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-6", "Travel/French/DAC-Travel-France-6.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-7", "Travel/French/DAC-Travel-France-7.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-8", "Travel/French/DAC-Travel-France-8.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-9", "Travel/French/DAC-Travel-France-9.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-10", "Travel/French/DAC-Travel-France-10.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-11", "Travel/French/DAC-Travel-France-11.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-12", "Travel/French/DAC-Travel-France-12.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-13", "Travel/French/DAC-Travel-France-13.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-14", "Travel/French/DAC-Travel-France-14.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-France-15", "Travel/French/DAC-Travel-France-15.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_travel),

# Burgandy

  ("DAC-Travel-Burgandy-1", "Travel/Burgandy/DAC-Travel-Burgandy-1.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-2", "Travel/Burgandy/DAC-Travel-Burgandy-2.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-3", "Travel/Burgandy/DAC-Travel-Burgandy-3.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-4", "Travel/Burgandy/DAC-Travel-Burgandy-4.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-5", "Travel/Burgandy/DAC-Travel-Burgandy-5.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-6", "Travel/Burgandy/DAC-Travel-Burgandy-6.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-7", "Travel/Burgandy/DAC-Travel-Burgandy-7.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-8", "Travel/Burgandy/DAC-Travel-Burgandy-8.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
  ("DAC-Travel-Burgandy-9", "Travel/Burgandy/DAC-Travel-Burgandy-9.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_travel),
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

# Town
  ("DAC-Town-Generic-1", "DAC-Town-Generic-1.mp3", mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-2", "DAC-Town-Generic-2.mp3", mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-3", "DAC-Town-Generic-3.mp3", mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-4", "DAC-Town-Generic-4.mp3", mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-5", "DAC-Town-Generic-5.mp3", mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),
  ("DAC-Town-Generic-6", "DAC-Town-Generic-6.mp3", mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),


# Tavern
  ("DAC-Tavern-Generic-1", "DAC-Tavern-Generic-1.mp3", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),
  ("DAC-Tavern-Generic-2", "DAC-Tavern-Generic-2.mp3", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),

# Defeat
  ("DAC-Defeat-1", "DAC-Defeat-1.ogg", mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),

# DAC Changes END

# Native Music Starts Here. Will need to be replaced

  ("arena_1", "arena_1.ogg", mtf_sit_arena, 0),
#  ("arena_2", "arena_2.ogg", mtf_looping|mtf_sit_arena, 0),
  ("armorer", "armorer.ogg", mtf_sit_travel, 0),
  
 
  ("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "defeated_by_neutral.ogg",mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished, 0),

  ("killed_by_khergit", "killed_by_khergit.ogg", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
#  ("killed_by_neutral", "killed_by_neutral.ogg", mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed, 0),
#  ("killed_by_nord", "killed_by_nord.ogg", mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed, 0),
#  ("killed_by_rhodok", "killed_by_rhodok.ogg", mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed, 0),
  ("killed_by_swadian", "killed_by_swadian.ogg", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
#  ("killed_by_vaegir", "killed_by_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed, 0),

  ("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  
  ("tavern_1", "tavern_1.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_2", "tavern_2.ogg", mtf_sit_tavern|mtf_sit_feast, 0),


  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  ("victorious_swadian", "victorious_swadian.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir", "victorious_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),



  
]
