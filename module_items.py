from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

from compiler import *
####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

def heraldic(item_tableau):
  return (ti_on_init_item, [
  (store_trigger_param_1, ":agent_no"),
  (store_trigger_param_2, ":troop_no"),
  (call_script, "script_shield_item_set_banner", item_tableau, ":agent_no", ":troop_no")
  ])
  
def add_meshes(item_meshes):
  cur_meshes = [(store_trigger_param_1, ":agent_no"),(ge, ":agent_no", 0)]
  for mesh in item_meshes if not isinstance(item_meshes, basestring) else [item_meshes]:
    cur_meshes.append((str_store_string, s1, mesh))
    cur_meshes.append((cur_item_add_mesh, s1))
  return (ti_on_init_item, cur_meshes)
  
def add_mesh(item_mesh):
  return (ti_on_init_item, [
  (str_store_string, s1, item_mesh),
  (cur_item_add_mesh, s1),
  ])
  
def reskin(item_material, mesh_no):
  return (ti_on_init_item, [
  (str_store_string, s1, item_material),
  (cur_item_set_material, s1, mesh_no, 0),
  ])
  
def add_mesh_reskin(item_mesh, item_material, mesh_no):
  return (ti_on_init_item, [
  (str_store_string, s1, item_mesh),
  (str_store_string, s2, item_material),
  (cur_item_add_mesh, s1),
  (cur_item_set_material, s2, mesh_no, 0),
  ])
  
def add_mesh_vertex(item_mesh, vertex_colour):
  return (ti_on_init_item, [
  (str_store_string, s1, item_mesh),
  (str_store_string, s2, vertex_colour),
  (cur_item_add_mesh, s1, 0, 0, s2),
  ])
  
def custom_reskin(item):
  return (ti_on_init_item, [
    # (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    (store_trigger_param_2, ":troop_no"),
    (str_clear, s1),
    (item_get_slot, ":start", item, slot_item_materials_begin),
    (item_get_slot, ":end", item, slot_item_materials_end),
    
    (item_get_slot, ":france_start", item, slot_item_france_materials_begin),
    (item_get_slot, ":france_end", item, slot_item_france_materials_end),
    
    (item_get_slot, ":english_start", item, slot_item_english_materials_begin),
    (item_get_slot, ":english_end", item, slot_item_english_materials_end),
    
    (item_get_slot, ":burgundy_start", item, slot_item_burgundy_materials_begin),
    (item_get_slot, ":burgundy_end", item, slot_item_burgundy_materials_end),
    
    (item_get_slot, ":breton_start", item, slot_item_breton_materials_begin),
    (item_get_slot, ":breton_end", item, slot_item_breton_materials_end),
	 
    (item_get_slot, ":flemish_start", item, slot_item_flemish_materials_begin),
    (item_get_slot, ":flemish_end", item, slot_item_flemish_materials_end),	 

    (item_get_slot, ":mercenary_start", item, slot_item_mercenary_materials_begin),
    (item_get_slot, ":mercenary_end", item, slot_item_mercenary_materials_end),	 	  
	 
    (store_troop_faction, ":faction", ":troop_no"),
	 
    (store_sub, ":total", ":end", ":start"),
    (gt, ":total", 0),
	 
    (try_begin),
      (gt, ":troop_no", -1),
      (troop_is_hero, ":troop_no"),
      (item_get_slot, ":value", item, slot_item_player_color),
      (neq, ":value", -1),
      (val_mod, ":value", ":total"),
      (val_add, ":value", ":start"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_1"),
    	(store_random_in_range, ":value", ":france_start", ":france_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_2"),
    	(store_random_in_range, ":value", ":english_start", ":english_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_3"),
    	(store_random_in_range, ":value", ":burgundy_start", ":burgundy_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_4"),
    	(store_random_in_range, ":value", ":breton_start", ":breton_end"),
    (else_try),
    	(eq, ":faction", "fac_flemish_mercenaries"),
    	(store_random_in_range, ":value", ":flemish_start", ":flemish_end"),	
    (else_try),
    	(eq, ":faction", "fac_neutral"),
    	(store_random_in_range, ":value", ":mercenary_start", ":mercenary_end"),	
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 1),
        (store_random_in_range, ":value", ":france_start", ":france_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 2),
        (store_random_in_range, ":value", ":english_start", ":english_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 3),
        (store_random_in_range, ":value", ":burgundy_start", ":burgundy_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 4),
        (store_random_in_range, ":value", ":breton_start", ":breton_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 5),
        (store_random_in_range, ":value", ":flemish_start", ":flemish_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 6),
        (store_random_in_range, ":value", ":mercenary_start", ":mercenary_end"), 
    (else_try),
      (store_random_in_range, ":value", ":start", ":end"), #Anyone else gets a random mix of everything
    (try_end),
    (try_begin),
      (eq, ":value", "str_no_string"),
      (store_random_in_range, ":value", ":start", ":end"), #Anyone else gets a random mix of everything
    (try_end),
    (try_begin),
      (str_store_string, s1, ":value"),
      (cur_item_set_material, s1, 0),
    (try_end),
    ])	 
	 
def custom_remodel(item):
  return (ti_on_init_item, [
    # (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    (store_trigger_param_2, ":troop_no"),
    (str_clear, s1),
    (item_get_slot, ":start", item, slot_item_materials_begin),
    (item_get_slot, ":end", item, slot_item_materials_end),
    
    (item_get_slot, ":france_start", item, slot_item_france_materials_begin),
    (item_get_slot, ":france_end", item, slot_item_france_materials_end),
    
    (item_get_slot, ":english_start", item, slot_item_english_materials_begin),
    (item_get_slot, ":english_end", item, slot_item_english_materials_end),
    
    (item_get_slot, ":burgundy_start", item, slot_item_burgundy_materials_begin),
    (item_get_slot, ":burgundy_end", item, slot_item_burgundy_materials_end),
    
    (item_get_slot, ":breton_start", item, slot_item_breton_materials_begin),
    (item_get_slot, ":breton_end", item, slot_item_breton_materials_end),
	 
    (item_get_slot, ":flemish_start", item, slot_item_flemish_materials_begin),
    (item_get_slot, ":flemish_end", item, slot_item_flemish_materials_end),		 
	 
    (item_get_slot, ":mercenary_start", item, slot_item_mercenary_materials_begin),
    (item_get_slot, ":mercenary_end", item, slot_item_mercenary_materials_end),	 	 

    (store_troop_faction, ":faction", ":troop_no"),
	 
    (store_sub, ":total", ":end", ":start"),
    (gt, ":total", 0),
	 
    (try_begin),
      (gt, ":troop_no", -1),
      (troop_is_hero, ":troop_no"),
      (item_get_slot, ":value", item, slot_item_player_color),
      (neq, ":value", -1),
      (val_mod, ":value", ":total"),
      (val_add, ":value", ":start"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_1"),
    	(store_random_in_range, ":value", ":france_start", ":france_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_2"),
    	(store_random_in_range, ":value", ":english_start", ":english_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_3"),
    	(store_random_in_range, ":value", ":burgundy_start", ":burgundy_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_4"),
    	(store_random_in_range, ":value", ":breton_start", ":breton_end"),
    (else_try),
    	(eq, ":faction", "fac_flemish_mercenaries"),
    	(store_random_in_range, ":value", ":flemish_start", ":flemish_end"),	
    (else_try),
    	(eq, ":faction", "fac_neutral"),
    	(store_random_in_range, ":value", ":mercenary_start", ":mercenary_end"),	
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 1),
        (store_random_in_range, ":value", ":france_start", ":france_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 2),
        (store_random_in_range, ":value", ":english_start", ":english_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 3),
        (store_random_in_range, ":value", ":burgundy_start", ":burgundy_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 4),
        (store_random_in_range, ":value", ":breton_start", ":breton_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 5),
        (store_random_in_range, ":value", ":flemish_start", ":flemish_end"), 
    (else_try),
    	(eq, ":faction", "fac_player_faction"),
        (eq, "$player_camp_troop_color_scheme", 6),
        (store_random_in_range, ":value", ":mercenary_start", ":mercenary_end"), 
    (else_try),
      (store_random_in_range, ":value", ":start", ":end"), #Anyone else gets a random mix of everything
    (try_end),
    (try_begin),
      (eq, ":value", "str_no_string"),
      (store_random_in_range, ":value", ":start", ":end"), #Anyone else gets a random mix of everything
    (try_end),
    (try_begin),
      (str_store_string, s1, ":value"),
      (cur_item_add_mesh, s1, 0),
    (try_end),
    ])	
    
    
def aketon_patch():
  return (ti_on_init_item, [
    # (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    (store_trigger_param_2, ":troop_no"),
    (str_clear, s1),
    
    (assign, ":value", "str_a_patch_invisible"),

    (try_begin),
        (gt, ":troop_no", -1),
        (neg|troop_is_hero, ":troop_no"),
        (store_troop_faction, ":faction", ":troop_no"),
            (try_begin),
                (eq, ":faction", "fac_kingdom_1"),
                (store_random_in_range, ":value", "str_a_patch_french_1", "str_a_patch_english_1"),
            (else_try),
                (eq, ":faction", "fac_kingdom_2"),
                (store_random_in_range, ":value", "str_a_patch_english_1", "str_a_patch_burgundy_1"),
            (else_try),
                (eq, ":faction", "fac_kingdom_3"),
                (store_random_in_range, ":value", "str_a_patch_burgundy_1", "str_a_patch_brittany_1"),
            (else_try),
                (eq, ":faction", "fac_kingdom_4"),
                (store_random_in_range, ":value", "str_a_patch_brittany_1", "str_a_patch_invisible"),
            (else_try),
                (assign, ":value", "str_a_patch_invisible"), #invisible string
            (try_end),
    (try_end),

    (try_begin),
      (eq, ":value", "str_no_string"),
      (assign, ":value", "str_a_patch_invisible"),
    (try_end),
    (try_begin),
        (str_store_string, s1, ":value"),
        (cur_item_set_material, s1, 0),
        # (display_message, "@Material is {s1}"),
    (try_end),
    ])	 
    
def add_pants():
  return (ti_on_init_item, [
    (store_trigger_param_1, ":agent_no"), 
    # (store_trigger_param_2, ":troop_no"),
    (str_clear, s1),
    (str_clear, s2),

    (try_begin),
        (gt, ":agent_no", -1),
        (try_begin),
            (agent_get_item_slot, ":footwear", ":agent_no", 6),
            (gt, ":footwear", -1),
            
            (try_begin),
                (try_begin),
                    (is_between, ":footwear", "itm_b_turnshoes_1", "itm_b_low_boots_1"),
                    (assign, ":model", "@b_turnshoes"),
                    (try_begin),
                        (eq, ":footwear", "itm_b_turnshoes_1"),	  
                        (assign, ":string", "@b_hose_1"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_2"),	  
                        (assign, ":string", "@b_hose_2"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_3"),	  
                        (assign, ":string", "@b_hose_3"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_4"),	  
                        (assign, ":string", "@b_hose_4"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_5"),	  
                        (assign, ":string", "@b_hose_5"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_6"),	  
                        (assign, ":string", "@b_hose_6"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_7"),	  
                        (assign, ":string", "@b_hose_7"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_8"),	  
                        (assign, ":string", "@b_hose_8"),
                    (else_try),
                        (eq, ":footwear", "itm_b_turnshoes_9"),	  
                        (assign, ":string", "@b_hose_9"),
                    (try_end),
                (else_try),
                    (is_between, ":footwear", "itm_b_low_boots_1", "itm_b_poulaines_1"),
                    (assign, ":model", "@b_poulaines"),
                    (try_begin),
                        (eq, ":footwear", "itm_b_poulaines_1"),	  
                        (assign, ":string", "@b_hose_1"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_2"),	  
                        (assign, ":string", "@b_hose_2"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_3"),	  
                        (assign, ":string", "@b_hose_3"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_4"),	  
                        (assign, ":string", "@b_hose_4"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_5"),	  
                        (assign, ":string", "@b_hose_5"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_6"),	  
                        (assign, ":string", "@b_hose_6"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_7"),	  
                        (assign, ":string", "@b_hose_7"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_8"),	  
                        (assign, ":string", "@b_hose_8"),
                    (else_try),
                        (eq, ":footwear", "itm_b_poulaines_9"),	  
                        (assign, ":string", "@b_hose_9"),
                    (try_end),
                (else_try),    
                    (is_between, ":footwear", "itm_b_high_boots_1", "itm_b_high_boots_folded_1"),
                    (assign, ":model", "@b_high_boots"),
                    (try_begin),
                        (eq, ":footwear", "itm_b_high_boots_1"),	  
                        (assign, ":string", "@b_hose_1"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_2"),	  
                        (assign, ":string", "@b_hose_2"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_3"),	  
                        (assign, ":string", "@b_hose_3"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_4"),	  
                        (assign, ":string", "@b_hose_4"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_5"),	  
                        (assign, ":string", "@b_hose_5"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_6"),	  
                        (assign, ":string", "@b_hose_6"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_7"),	  
                        (assign, ":string", "@b_hose_7"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_8"),	  
                        (assign, ":string", "@b_hose_8"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_9"),	  
                        (assign, ":string", "@b_hose_9"),
                    (try_end),
                (else_try),    
                    (is_between, ":footwear", "itm_b_high_boots_folded_1", "itm_g_leather_gauntlet"),
                    (assign, ":model", "@b_high_boots_folded"),
                    (try_begin),
                        (eq, ":footwear", "itm_b_high_boots_folded_1"),	  
                        (assign, ":string", "@b_hose_1"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_2"),	  
                        (assign, ":string", "@b_hose_2"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_3"),	  
                        (assign, ":string", "@b_hose_3"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_4"),	  
                        (assign, ":string", "@b_hose_4"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_5"),	  
                        (assign, ":string", "@b_hose_5"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_6"),	  
                        (assign, ":string", "@b_hose_6"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_7"),	  
                        (assign, ":string", "@b_hose_7"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_8"),	  
                        (assign, ":string", "@b_hose_8"),
                    (else_try),
                        (eq, ":footwear", "itm_b_high_boots_folded_9"),	  
                        (assign, ":string", "@b_hose_9"),
                    (try_end),
                (try_end),
            (try_end),
            
        (else_try),
            (assign, ":model", "@b_turnshoes"),
            (assign, ":string", "@b_hose_1"),
        (try_end),
    (try_end),
    
    

    (try_begin),
      (eq, ":string", "str_no_string"),
      (assign, ":model", "@b_turnshoes"),
      (assign, ":string", "@b_hose_1"),
    (try_end),
    
    (try_begin),
        (str_store_string, s1, ":model"),
        (str_store_string, s2, ":string"),
        (cur_item_add_mesh, s1),
        (cur_item_set_material, s2, 1, 0),
    (try_end),
    ])	 
	
# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_balanced | imodbit_masterwork
imodbits_sword_alt   = imodbit_rusty | imodbit_masterwork
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered | imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive)
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_no_blur|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["tutorial_spear", "Spear", [("w_spear_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itc_spear_upstab|itcf_carry_spear, 134, weight(1.1)|difficulty(0)|spd_rtng(99)|weapon_length(107)|swing_damage(37,pierce)|thrust_damage(37,pierce), imodbits_polearm ],
["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["tutorial_battle_axe", "Battle Axe", [("w_twohanded_war_axe_01",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_arrows","Arrows", [("w_arrow_blunt",0),("w_arrow_blunt",ixmesh_flying_ammo),("w_arrow_quiver_blunt", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,blunt)|max_ammo(20),imodbits_missile],
["tutorial_bolts","Bolts", [("w_bolt_triangular",0),("w_bolt_triangular",ixmesh_flying_ammo),("w_bolt_quiver_triangular", ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(1,blunt)|max_ammo(18),imodbits_missile],
["tutorial_short_bow", "Short Bow", [("w_hunting_bow_ash",0),("w_hunting_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,90, weight(0.8)|difficulty(1)|spd_rtng(90)|shoot_speed(45)|thrust_damage(15,pierce), imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("w_crossbow_medium",0)], itp_type_crossbow |itp_primary|itp_no_blur|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary|itp_no_blur ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
["tutorial_saddle_horse", "Saddle Horse", [("ho_sumpter_1",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
["tutorial_sword", "Sword", [("w_regular_onehanded_sword_squire",0),("w_regular_onehanded_sword_squire_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["tutorial_axe", "Axe", [("w_onehanded_war_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, ~221 , weight(1.5)|difficulty(9)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_dagger","Dagger", [("w_regular_dagger_pikeman",0)], itp_type_one_handed_wpn|itp_primary|itp_no_blur|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],

# Items before this point are hardwired and their order should not be changed!
["practice_sword","Practice Sword", [("w_regular_onehanded_sword_squire",0),("w_regular_onehanded_sword_squire_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , blunt) | thrust_damage(27 ,  blunt),imodbits_sword_high ],
["heavy_practice_sword","Heavy Practice Sword", [("w_regular_onehanded_sword_squire",0),("w_regular_onehanded_sword_squire_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , blunt) | thrust_damage(27 ,  blunt),imodbits_sword_high ],
["practice_dagger","Practice Dagger", [("w_regular_dagger_pikeman",0)], itp_type_one_handed_wpn|itp_primary|itp_no_blur|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,122 , weight(0.7)|difficulty(0)|spd_rtng(108) | weapon_length(41)|swing_damage(28 , blunt) | thrust_damage(27 ,  blunt),imodbits_sword ],
["practice_axe", "Practice Axe", [("w_onehanded_war_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 221 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , blunt) | thrust_damage(0 ,  blunt),imodbits_axe ],
["arena_axe", "Axe", [("w_onehanded_war_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 221 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , blunt) | thrust_damage(0 ,  blunt),imodbits_axe ],
["arena_sword", "Sword",[("w_regular_onehanded_sword_squire",0),("w_regular_onehanded_sword_squire_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , blunt) | thrust_damage(27 ,  blunt),imodbits_sword_high ],
["arena_sword_two_handed",  "Two Handed Sword", [("w_regular_twohanded_sword_talhoffer",0),("w_regular_twohanded_sword_talhoffer_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  998 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(115)|swing_damage(40 , blunt) | thrust_damage(35 ,  blunt),imodbits_sword_high ], 
["arena_lance",         "Lance", [("w_native_spear_b",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise| itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry, itc_pike_upstab, 214 , weight(2.5)|difficulty(0)|spd_rtng(88) | weapon_length(175)|swing_damage(0 , blunt) | thrust_damage(27 ,  blunt),imodbits_polearm ],

["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
["practice_lance","Practice Lance", [("w_native_spear_b",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise| itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry, itc_pike_upstab, 214 , weight(2.5)|difficulty(0)|spd_rtng(88) | weapon_length(175)|swing_damage(0 , blunt) | thrust_damage(27 ,  blunt),imodbits_polearm ],
["practice_shield","Practice Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
["practice_bow","Practice Bow", [("w_hunting_bow_ash",0),("w_hunting_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back, 90, weight(0.8)|difficulty(1)|spd_rtng(90)|shoot_speed(45)|thrust_damage(21,blunt), imodbits_bow ],
["practice_crossbow", "Practice Crossbow", [("w_crossbow_medium",0)], itp_type_crossbow |itp_primary|itp_no_blur|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver", ixmesh_carry)], itp_type_thrown |itp_primary|itp_no_blur|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary|itp_no_blur ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary|itp_no_blur ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
["practice_spear","Practice Spear",[("w_native_spear_b",0)], itp_type_polearm|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],

["practice_horse","Practice Horse", [("ho_sumpter_1",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
["practice_arrows","Practice Arrows", [("w_arrow_blunt",0),("w_arrow_blunt",ixmesh_flying_ammo),("w_arrow_quiver_blunt", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
["practice_bolts","Practice Bolts", [("w_bolt_triangular",0),("w_bolt_triangular",ixmesh_flying_ammo),("w_bolt_quiver_triangular", ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
["practice_arrows_10_amount","Practice Arrows", [("w_arrow_blunt",0),("w_arrow_blunt",ixmesh_flying_ammo),("w_arrow_quiver_blunt", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
["practice_arrows_100_amount","Practice Arrows", [("w_arrow_blunt",0),("w_arrow_blunt",ixmesh_flying_ammo),("w_arrow_quiver_blunt", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
["practice_bolts_9_amount","Practice Bolts", [("w_bolt_triangular",0),("w_bolt_triangular",ixmesh_flying_ammo),("w_bolt_quiver_triangular", ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
["practice_boots", "Practice Boots", [("b_turnshoes_2",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],

["red_tourney_armor","Red Tourney Armor", [("a_simple_gambeson_red_1",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["blue_tourney_armor","Blue Tourney Armor", [("a_simple_gambeson_blue_1",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["green_tourney_armor","Green Tourney Armor", [("a_simple_gambeson_green_1",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["gold_tourney_armor","Gold Tourney Armor", [("a_simple_gambeson_white_1",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["red_tourney_helmet","Red Tourney Helmet",[("h_hood_red",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
["blue_tourney_helmet","Blue Tourney Helmet",[("h_hood_blue",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
["green_tourney_helmet","Green Tourney Helmet",[("h_hood_green",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
["gold_tourney_helmet","Gold Tourney Helmet",[("h_hood_yellow",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("a_simple_gambeson_white_1",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("a_simple_gambeson_red_1",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor],
["arena_armor_blue", "Arena Armor Blue", [("a_simple_gambeson_blue_1",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor],
["arena_armor_green", "Arena Armor Green", [("a_simple_gambeson_green_1",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor],
["arena_armor_yellow", "Arena Armor Yellow", [("a_simple_gambeson_white_4",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor],
["arena_tunic_white", "Arena Tunic White ", [("a_simple_gambeson_white_1",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("a_simple_gambeson_red_1",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth],
["arena_tunic_blue", "Arena Tunic Blue", [("a_simple_gambeson_blue_1",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth],
["arena_tunic_green", "Arena Tunic Green", [("a_simple_gambeson_green_1",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth],
["arena_tunic_yellow", "Arena Tunic Yellow", [("a_simple_gambeson_white_4",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_red", 0, 0),])]],
["arena_helmet_blue", "Arena Helmet Blue", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_blue", 0, 0),])]],
["arena_helmet_green", "Arena Helmet Green", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_green", 0, 0),])]],
["arena_helmet_yellow", "Arena Helmet Yellow", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_brown", 0, 0),])]],
["steppe_helmet_white", "Arena Helmet White", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_white", 0, 0),])]],
["steppe_helmet_red", "Arena Helmet Red", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_cervelliere", 0, 0),(cur_item_set_material, "@h_hood_narf_red", 0, 0),])]],
["steppe_helmet_blue", "Arena Helmet Blue", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_cervelliere", 0, 0),(cur_item_set_material, "@h_hood_narf_blue", 0, 0),])]],
["steppe_helmet_green", "Arena Helmet Green", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_cervelliere", 0, 0),(cur_item_set_material, "@h_hood_narf_green", 0, 0),])]],
["steppe_helmet_yellow", "Arena Helmet Yellow", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_cervelliere", 0, 0),(cur_item_set_material, "@h_hood_narf_brown", 0, 0),])]],

["tourney_helm_white", "Tourney Helm White", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_white", 0, 0),])]],
["tourney_helm_red", "Tourney Helm Red", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_red", 0, 0),])]],
["tourney_helm_blue", "Tourney Helm Blue", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_blue", 0, 0),])]],
["tourney_helm_green", "Tourney Helm Green", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_green", 0, 0),])]],
["tourney_helm_yellow", "Tourney Helm Yellow", [("o_hood_narf_base",0)], itp_type_head_armor|itp_attach_armature,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),(cur_item_set_material, "@h_hood_narf_brown", 0, 0),])]],
["arena_turban_red", "Arena Hood", [("h_hood_red",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Hood", [("h_hood_blue",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Hood", [("h_hood_green",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Hood", [("h_hood_yellow",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

# Common trade goods

["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbit_fine|imodbit_large_bag|imodbit_exquisite],
["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbit_fine|imodbit_large_bag],
["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbit_cracked|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_rough|imodbit_sturdy],
["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite],
["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy],
["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite],
["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy],
["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbit_fine|imodbit_exquisite],
["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],
["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],
["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],
["tools","Tools", [("w_warhammer_1",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbit_rusty|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_sturdy|imodbit_hardened],
["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],
["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy|imodbit_thick],
["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],

# Drinking consumables

["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_strong],
["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_strong|imodbit_lordly],

# Food consumables

["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for imodbit_cheap|imodbit_fine|imodbit_exquisite
["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for imodbit_cheap|imodbit_fine|imodbit_exquisite
["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_exquisite|imodbit_large_bag],
["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],


# Misc Native leftovers

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_no_blur ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(45 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 # [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_two_handed, 0,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_secondary, 0,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 1259 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_armor ],
["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor|itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor   ,0, 824 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["keys", "Ring of Keys", [("w_archer_hatchet",0)], itp_type_one_handed_wpn |itp_primary|itp_no_blur|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("w_hunting_bow_ash",0), ("w_hunting_bow_ash_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_no_blur|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("w_arrow_blunt",0),("w_arrow_blunt",ixmesh_flying_ammo),("w_arrow_quiver_blunt", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],


["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("a_churburg_13_asher_base",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor],
["mail_boots_for_tableau", "Mail Boots", [("b_high_boots_3",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW HORSES ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["ho_sumpter_1", "Sumpter Horse", [("ho_sumpter_1",0)], itp_type_horse|itp_merchandise, 0, 299, abundance(100)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(36)|horse_maneuver(42)|horse_charge(10)|horse_scale(100), imodbits_horse_basic ],
["ho_sumpter_2", "Sumpter Horse", [("ho_sumpter_2",0)], itp_type_horse|itp_merchandise, 0, 299, abundance(100)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(36)|horse_maneuver(42)|horse_charge(10)|horse_scale(100), imodbits_horse_basic ],

["ho_rouncey_1", "Rouncey Horse", [("ho_rouncey_1",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_2", "Rouncey Horse", [("ho_rouncey_2",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_3", "Rouncey Horse", [("ho_rouncey_3",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_4", "Rouncey Horse", [("ho_rouncey_4",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_5", "Rouncey Horse", [("ho_rouncey_5",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_6", "Rouncey Horse", [("ho_rouncey_6",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],

["ho_courser_1", "Courser", [("ho_courser_1",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_2", "Courser", [("ho_courser_2",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_3", "Courser", [("ho_courser_3",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_4", "Courser", [("ho_courser_4",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_5", "Courser", [("ho_courser_5",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_6", "Courser", [("ho_courser_6",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_7", "Courser", [("ho_courser_7",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_8", "Courser", [("ho_courser_8",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],

["ho_hunting_horse_france", "French Hunter", [("ho_hunting_horse_france",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(70)|hit_points(120)|body_armor(14)|difficulty(2)|horse_speed(44)|horse_maneuver(42)|horse_charge(20)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_hunting_horse_england", "English Hunter", [("ho_hunting_horse_england",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(70)|hit_points(120)|body_armor(14)|difficulty(2)|horse_speed(44)|horse_maneuver(42)|horse_charge(20)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_horse_barded_black", "Barded Horse", [("ho_horse_barded_black",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_blue", "Barded Horse", [("ho_horse_barded_blue",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_brown", "Barded Horse", [("ho_horse_barded_brown",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_green", "Barded Horse", [("ho_horse_barded_green",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_red", "Barded Horse", [("ho_horse_barded_red",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_white", "Barded Horse", [("ho_horse_barded_white",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_horse_barded_black_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_black_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_blue_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_blue_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_brown_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_brown_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_green_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_green_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_red_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_red_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_white_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_white_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_war_horse_blue", "War Horse", [("ho_war_horse_blue",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_black", "War Horse", [("ho_war_horse_black",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_brown", "War Horse", [("ho_war_horse_brown",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_green", "War Horse", [("ho_war_horse_green",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_red", "War Horse", [("ho_war_horse_red",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_white", "War Horse", [("ho_war_horse_white",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_charger_black", "Charger", [("ho_charger_black",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_blue", "Charger", [("ho_charger_blue",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_brown", "Charger", [("ho_charger_brown",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_green", "Charger", [("ho_charger_green",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_red", "Charger", [("ho_charger_red",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_white", "Charger", [("ho_charger_white",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["sumpter_horse", "Sumpter Horse", [("sumpter_horse",0)], itp_type_horse|itp_merchandise, 0, 254, abundance(90)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100), imodbits_horse_basic ],
["saddle_horse", "Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 360, abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],

["ho_tournament_horse_barded_white_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_white_chamfrom",0)], itp_type_horse, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(0)|horse_speed(42)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_tournament_horse_barded_black_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_black_chamfrom",0)], itp_type_horse, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(0)|horse_speed(42)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

### Animals
["animal_chicken", "Chicken", [("animal_chicken",0)], itp_type_animal|itp_disable_agent_sounds, 0, 
50, abundance(0)|hit_points(50)|body_armor(0)|difficulty(11)|horse_speed(8)|horse_maneuver(42)|horse_charge(1)|horse_scale(15), imodbits_none, [], [fac_no_faction] ],
["animal_cow", "Cow", [("animal_cow",0)], itp_type_animal|itp_disable_agent_sounds, 0, 
300, abundance(0)|hit_points(300)|body_armor(8)|difficulty(11)|horse_speed(8)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none, [], [fac_no_faction] ],
["animal_horse_light_a", "Horse", [("animal_horse_light_a",0)], itp_type_animal, 0, 
150, abundance(0)|hit_points(100)|body_armor(2)|difficulty(11)|horse_speed(40)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none, [], [fac_no_faction] ],
["animal_horse_light_b", "Horse", [("animal_horse_light_b",0)], itp_type_animal, 0, 
150, abundance(0)|hit_points(100)|body_armor(2)|difficulty(11)|horse_speed(40)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none, [], [fac_no_faction] ],
["animal_horse_light_c", "Horse", [("animal_horse_light_c",0)], itp_type_animal, 0, 
150, abundance(0)|hit_points(100)|body_armor(2)|difficulty(11)|horse_speed(40)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none, [], [fac_no_faction] ],
["animal_old_horse_a", "Pack Horse", [("animal_old_horse_a",0)], itp_type_animal, 0, 
150, abundance(0)|hit_points(100)|body_armor(2)|difficulty(11)|horse_speed(40)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none, [], [fac_no_faction] ],
["animal_pig", "Pig", [("animal_pig",0)], itp_type_animal|itp_disable_agent_sounds, 0, 
50, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(20)|horse_maneuver(42)|horse_charge(1)|horse_scale(65), imodbits_none, [], [fac_no_faction] ],
["animal_sheep_a", "Sheep", [("animal_sheep_a",0)], itp_type_animal|itp_disable_agent_sounds, 0, 
50, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(20)|horse_maneuver(42)|horse_charge(1)|horse_scale(50), imodbits_none, [], [fac_no_faction] ],
["animal_sheep_b", "Sheep", [("animal_sheep_b",0)], itp_type_animal|itp_disable_agent_sounds, 0, 
50, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(20)|horse_maneuver(42)|horse_charge(1)|horse_scale(50), imodbits_none, [], [fac_no_faction] ],




##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW HELMETS ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################
# ["h_english_great_bascinet_houndskull_closed", "English Great Bascinet with Gorget", [("h_english_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor |itp_covers_head| itp_attach_armature  ,0, 
# 1800 , weight(3)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[(ti_on_init_item,[(cur_item_add_mesh, "@h_english_great_bascinet_closed", 0, 0),(cur_item_add_mesh, "@o_circlet_red_chapel_2_3", 0, 0),])]],
# ["h_english_great_bascinet_houndskull_open", "English Great Bascinet with Gorget", [("h_english_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor | itp_attach_armature  ,0, 
# 1800 , weight(3)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[(ti_on_init_item,[(cur_item_add_mesh, "@h_english_great_bascinet_open", 0, 0),])]],
# ["h_english_great_bascinet_houndskull_closed_deco", "English Great Bascinet with Gorget", [("h_english_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor |itp_covers_head| itp_attach_armature  ,0, 
# 1800 , weight(3)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[(ti_on_init_item,[(cur_item_add_mesh, "@h_english_great_bascinet_closed", 0, 0),(cur_item_set_material, "@h_english_great_bascinet_deco", 0, 0),(cur_item_set_material, "@h_english_great_bascinet_deco", 1, 0),(cur_item_add_mesh, "@o_circlet_black_chapel_4", 0, 0),])]],
# ["h_english_great_bascinet_houndskull_open_deco", "English Great Bascinet with Gorget", [("h_english_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor | itp_attach_armature  ,0, 
# 1800 , weight(3)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[(ti_on_init_item,[(cur_item_add_mesh, "@h_english_great_bascinet_open", 0, 0),(cur_item_set_material, "@h_english_great_bascinet_deco", 0, 0),(cur_item_set_material, "@h_english_great_bascinet_deco", 1, 0),])]],
# ["h_english_great_bascinet_houndskull_closed_blackened", "English Great Bascinet with Gorget", [("h_english_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor |itp_covers_head| itp_attach_armature  ,0, 
# 1800 , weight(3)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[(ti_on_init_item,[(cur_item_set_material, "@h_english_great_bascinet_blackened", 0, 0),(cur_item_add_mesh, "@h_english_great_bascinet_closed", 0, 0),(cur_item_set_material, "@h_english_great_bascinet_blackened", 1, 0),(cur_item_add_mesh, "@o_circlet_black_chapel_4", 0, 0),(cur_item_add_mesh, "@o_feather_large_left", 0, 0),])]],
# ["h_english_great_bascinet_houndskull_open_blackened", "English Great Bascinet with Gorget", [("h_english_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor | itp_attach_armature  ,0, 
# 1800 , weight(3)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[(ti_on_init_item,[(cur_item_set_material, "@h_english_great_bascinet_blackened", 0, 0),(cur_item_add_mesh, "@h_english_great_bascinet_open", 0, 0),(cur_item_set_material, "@h_english_great_bascinet_blackened", 1, 0),])]],

["h_great_bascinet_english_1410", "English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate],
["h_great_bascinet_english_1410_visor", "English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1410_visor"),],],
["h_great_bascinet_english_1410_visor_open", "English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1410_visor_open"),],],

["h_great_bascinet_english_1410_gilded", "Gilded English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[reskin("@h_great_bascinet_english_1410_gilded", 0),],],
["h_great_bascinet_english_1410_visor_gilded", "Gilded English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1410_visor"),reskin("@h_great_bascinet_english_1410_gilded", 0),],],
["h_great_bascinet_english_1410_visor_open_gilded", "Gilded English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1410_visor_open"),reskin("@h_great_bascinet_english_1410_gilded", 0),],],

["h_great_bascinet_english_1410_blued", "Blued English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[reskin("@h_great_bascinet_english_1410_blued", 0),reskin("@h_great_bascinet_english_1410_blued", 1),],],
["h_great_bascinet_english_1410_visor_blued", "Blued English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1410_visor"),reskin("@h_great_bascinet_english_1410_blued", 0),reskin("@h_great_bascinet_english_1410_blued", 1),reskin("@h_great_bascinet_english_1410_blued", 2),],],
["h_great_bascinet_english_1410_visor_open_blued", "Blued English Great Bascinet (1410)", [("h_great_bascinet_english_1410",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1410_visor_open"),reskin("@h_great_bascinet_english_1410_blued", 0),reskin("@h_great_bascinet_english_1410_blued", 1),reskin("@h_great_bascinet_english_1410_blued", 2),],],

["h_great_bascinet_english_1430", "English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate],
["h_great_bascinet_english_1430_visor", "English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1430_visor"),],],
["h_great_bascinet_english_1430_visor_open", "English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1430_visor_open"),],],

["h_great_bascinet_english_1430_gilded", "Gilded English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[reskin("@h_great_bascinet_english_1430_gilded", 0),],],
["h_great_bascinet_english_1430_visor_gilded", "Gilded English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1430_visor"),reskin("@h_great_bascinet_english_1430_gilded", 0),],],
["h_great_bascinet_english_1430_visor_open_gilded", "Gilded English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1430_visor_open"),reskin("@h_great_bascinet_english_1430_gilded", 0),],],

["h_great_bascinet_english_1430_blued", "Blued English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[reskin("@h_great_bascinet_english_1430_blued", 0),reskin("@h_great_bascinet_english_1430_blued", 1),],],
["h_great_bascinet_english_1430_visor_blued", "Blued English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1430_visor"),reskin("@h_great_bascinet_english_1430_blued", 0),reskin("@h_great_bascinet_english_1430_blued", 1),reskin("@h_great_bascinet_english_1430_blued", 2),],],
["h_great_bascinet_english_1430_visor_open_blued", "Blued English Great Bascinet (1430)", [("h_great_bascinet_english_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_english_1430_visor_open"),reskin("@h_great_bascinet_english_1430_blued", 0),reskin("@h_great_bascinet_english_1430_blued", 1),reskin("@h_great_bascinet_english_1430_blued", 2),],],

["h_great_bascinet_continental_1430", "Great Bascinet (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate],
["h_great_bascinet_continental_1430_visor", "Great Bascinet with Visor (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor"),],],
["h_great_bascinet_continental_1430_visor_open", "Great Bascinet with Visor (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor_open"),],],

["h_great_bascinet_continental", "Great Bascinet", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate],
["h_great_bascinet_continental_roundels", "Great Bascinet with Roundels", [("h_great_bascinet_continental_roundels",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate],
["h_great_bascinet_continental_visor_a", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_a"),],],
["h_great_bascinet_continental_visor_a_open", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_a_open"),],],
["h_great_bascinet_continental_visor_b", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_b"),],],
["h_great_bascinet_continental_visor_b_open", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_b_open"),],],
["h_great_bascinet_continental_visor_c", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_c"),],],
["h_great_bascinet_continental_visor_c_open", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_c_open"),],],
["h_great_bascinet_continental_visor_c_gilded", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_c_gilded"),],],
["h_great_bascinet_continental_visor_c_gilded_open", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_c_gilded_open"),],],
["h_great_bascinet_continental_visor_c_strip", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_c_strip"),],],
["h_great_bascinet_continental_visor_c_strip_open", "Great Bascinet with Visor", [("h_great_bascinet_continental",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_visor_c_strip_open"),],],

# ["h_great_bascinet_continental_1430_plume", "Great Bascinet with Plume (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_plume"),],],
# ["h_great_bascinet_continental_1430_plume_visor", "Great Bascinet with Plume (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor"),add_mesh("@h_great_bascinet_continental_1430_plume"),],],
# ["h_great_bascinet_continental_1430_plume_visor_open", "Great Bascinet with Plume (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor_open"),add_mesh("@h_great_bascinet_continental_1430_plume"),],],

["h_great_bascinet_continental_1430_visor_gilded", "Gilded Great Bascinet (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor"),reskin("@h_great_bascinet_continental_1430_gilded", 2),],],
["h_great_bascinet_continental_1430_visor_open_gilded", "Gilded Great Bascinet (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor_open"),reskin("@h_great_bascinet_continental_1430_gilded", 2),],],

["h_armet_savoy", "Savoyard Armet", [("h_armet_savoy_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate],
["h_armet_savoy_visor_a", "Savoyard Armet with Visor", [("h_armet_savoy_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_armet_savoy_visor_a"),],],
["h_armet_savoy_visor_b", "Savoyard Armet with Visor", [("h_armet_savoy_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_armet_savoy_visor_b"),],],

# ["h_great_bascinet_continental_1430_plume_visor_gilded", "Gilded Great Bascinet with Plume (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_head   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor"),add_mesh("@h_great_bascinet_continental_1430_plume"),reskin("@h_great_bascinet_continental_1430_gilded", 2),],],
# ["h_great_bascinet_continental_1430_plume_visor_open_gilded", "Gilded Great Bascinet with Plume (1430)", [("h_great_bascinet_continental_1430",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_continental_1430_visor_open"),add_mesh("@h_great_bascinet_continental_1430_plume"),reskin("@h_great_bascinet_continental_1430_gilded", 2),],],

# ["h_great_bascinet_1", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_1"),add_mesh("@h_great_bascinet_hinges"),],],
# ["h_great_bascinet_2", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_2"),add_mesh("@h_great_bascinet_hinges"),],],
# ["h_great_bascinet_1_trim", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_1"),add_mesh("@h_great_bascinet_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_trim_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_2_trim", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_2"),add_mesh("@h_great_bascinet_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_trim_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_1_brass", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_1"),add_mesh("@h_great_bascinet_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_brass_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_2_brass", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_2"),add_mesh("@h_great_bascinet_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_brass_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],

# ["h_great_bascinet_1_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_1"),add_mesh("@h_great_bascinet_open_hinges"),],],
# ["h_great_bascinet_2_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_2"),add_mesh("@h_great_bascinet_open_hinges"),],],
# ["h_great_bascinet_1_trim_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_1"),add_mesh("@h_great_bascinet_open_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_trim_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_2_trim_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_2"),add_mesh("@h_great_bascinet_open_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_trim_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_1_brass_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_1"),add_mesh("@h_great_bascinet_open_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_brass_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_2_brass_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_2"),add_mesh("@h_great_bascinet_open_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_brass_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],


# ["h_great_bascinet_venetian", "Venetian Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_venetian"),add_mesh("@h_great_bascinet_hinges"),],],
# ["h_great_bascinet_venetian_trim", "Venetian Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_venetian"),add_mesh("@h_great_bascinet_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_trim_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_venetian_brass", "Venetian Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_venetian"),add_mesh("@h_great_bascinet_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_brass_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],

# ["h_great_bascinet_venetian_open", "Venetian Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_venetian"),add_mesh("@h_great_bascinet_open_hinges"),],],
# ["h_great_bascinet_venetian_trim_open", "Venetian Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_venetian"),add_mesh("@h_great_bascinet_open_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_trim_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],
# ["h_great_bascinet_venetian_brass_open", "Venetian Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_venetian"),add_mesh("@h_great_bascinet_open_hinges"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_brass_visors",1),reskin("@h_great_bascinet_houndskull_brass",2),],],


# ["h_great_bascinet_houndskull", "Great Bascinet", [("h_great_bascinet_houndskull_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_houndskull"),],],
# ["h_great_bascinet_houndskull_brass", "Brass Great Bascinet", [("h_great_bascinet_houndskull_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_visor_houndskull"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_houndskull_brass",1),],],

# ["h_great_bascinet_houndskull_open", "Great Bascinet", [("h_great_bascinet_houndskull_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_houndskull"),],],
# ["h_great_bascinet_houndskull_brass_open", "Brass Great Bascinet", [("h_great_bascinet_houndskull_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1800 , weight(2.8)|abundance(100)|head_armor(58)|body_armor(6)|leg_armor(0)|difficulty(10) ,imodbits_plate,[add_mesh("@h_great_bascinet_open_visor_houndskull"),reskin("@h_great_bascinet_trim",0),reskin("@h_great_bascinet_houndskull_brass",1),],],


# ["h_great_bascinet_open_trim", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1100 , weight(2.8)|abundance(100)|head_armor(48)|body_armor(6)|leg_armor(0)|difficulty(8) ,imodbits_plate,[reskin("@h_great_bascinet_trim",0),],],
# ["h_great_bascinet_open", "Great Bascinet", [("h_great_bascinet_base",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 
# 1056 , weight(2.8)|abundance(100)|head_armor(48)|body_armor(6)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

# Klappvisier Bascinet Base: 42; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; scale aventail: 12,10; mail collar with bevor: 14,12;
["h_pigface_klappvisor", "Pigface Klappvisor Bascinet", [("h_pigface_klappvisor",0)], itp_merchandise| itp_type_head_armor|itp_covers_head| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(54)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_ogival", 0, 0),])]],
["h_pigface_klappvisor_open", "Open Pigface Klappvisor Bascinet", [("h_pigface_klappvisor_open",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(54)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_ogival", 0, 0),])]],

# Zitta Bascinet Base: 40; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; scale aventail: 12,10; mail collar with bevor: 14,12;
["h_zitta_bascinet", "Zitta Bascinet", [("h_zitta_bascinet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_zitta", 0, 0),])]],
["h_zitta_bascinet_open", "Open Zitta Bascinet", [("h_zitta_bascinet_open",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_zitta", 0, 0),])]],

# Wespe Bascinet Base: 40; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; scale aventail: 12,10; mail collar with bevor: 14,12;
["h_wespe_bascinet_a", "German Bascinet", [("h_wespe_bascinet_a",0)], itp_merchandise| itp_type_head_armor|itp_covers_head| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_wespe", 0, 0),])]],
["h_wespe_bascinet_a_open", "Open German Bascinet", [("h_wespe_bascinet_a_open",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_wespe", 0, 0),])]],

["h_wespe_bascinet_b", "German Bascinet", [("h_wespe_bascinet_b",0)], itp_merchandise| itp_type_head_armor|itp_covers_head| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_wespe", 0, 0),])]],
["h_wespe_bascinet_b_open", "Open German Bascinet", [("h_wespe_bascinet_b_open",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_wespe", 0, 0),])]],

["h_wespe_bascinet_c", "German Bascinet", [("h_wespe_bascinet_c",0)], itp_merchandise| itp_type_head_armor|itp_covers_head| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_wespe", 0, 0),])]],
["h_wespe_bascinet_c_open", "Open German Bascinet", [("h_wespe_bascinet_c_open",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
630 , weight(1.75)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_scale_aventail_wespe", 0, 0),])]],

# Barbuta Base: 36;
["h_barbuta_1_mail_collar", "Barbuta with Mail Collar", [("h_barbuta_1",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_barbuta_1_nasal_mail_collar", "Barbuta with Mail Collar", [("h_barbuta_1_nasal",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(46)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_barbuta_1_mail_collar_bevor", "Barbuta with Mail Collar and Bevor", [("h_barbuta_1",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(50)|body_armor(10)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar_bevor", 0, 0),])]],
["h_barbuta_1_nasal_mail_collar_bevor", "Barbuta with Mail Collar and Bevor", [("h_barbuta_1_nasal",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar_bevor", 0, 0),])]],
["h_barbuta_2_mail_collar", "Barbuta with Mail Collar", [("h_barbuta_2",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_barbuta_2_nasal_mail_collar", "Barbuta with Mail Collar", [("h_barbuta_2_nasal",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(46)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_barbuta_2_mail_collar_bevor", "Barbuta with Mail Collar and Bevor", [("h_barbuta_2",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(50)|body_armor(10)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar_bevor", 0, 0),])]],
["h_barbuta_2_nasal_mail_collar_bevor", "Barbuta with Mail Collar and Bevor", [("h_barbuta_2_nasal",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(52)|body_armor(10)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar_bevor", 0, 0),])]],

["h_barbuta_nooxy_1_mail_collar", "Barbuta with Mail Collar", [("h_barbuta_nooxy_1",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_barbuta_nooxy_2_mail_collar", "Barbuta with Mail Collar", [("h_barbuta_nooxy_2",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_barbuta_nooxy_3", "Barbuta", [("h_barbuta_nooxy_3",0)],  itp_type_head_armor| itp_attach_armature   ,0, 
478 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(6)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

# Bascinet Base: 34; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; scale aventail: 12,10; mail collar with bevor: 14,12;
["h_bascinet_1_mail_aventail", "Bascinet with Aventail", [("h_bascinet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),],],
["h_bascinet_1_visor_1_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),add_mesh("@h_bascinet_1_visor_1"),],],
["h_bascinet_1_visor_1_open_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),add_mesh("@h_bascinet_1_visor_1_open"),],],
["h_bascinet_1_visor_5_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_1",0)], itp_covers_head|itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),add_mesh("@h_bascinet_1_visor_5"),],],
["h_bascinet_1_visor_5_open_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),add_mesh("@h_bascinet_1_visor_5_open"),],],
["h_bascinet_1_hundsgugel_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_1",0)], itp_covers_head|itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),add_mesh("@h_hundsgugel_1"),],],
["h_bascinet_1_hundsgugel_open_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_1_aventail"),add_mesh("@h_hundsgugel_1_open"),],],

["h_bascinet_2_mail_aventail", "Bascinet with Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),],],
["h_bascinet_2_visor_1_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_bascinet_2_visor_1_open_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_bascinet_2_visor_5_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_covers_head|itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_bascinet_2_visor_5_open_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_bascinet_2_hundsgugel_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_covers_head|itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_hundsgugel_2"),],],
["h_bascinet_2_hundsgugel_open_mail_aventail", "Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_hundsgugel_2_open"),],],

["h_bascinet_2_gilded_mail_aventail", "Gilded Bascinet with Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),reskin("@h_bascinets_gilded", 0),],],
["h_bascinet_2_gilded_visor_1_mail_aventail", "Gilded Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_1"),reskin("@h_bascinets_gilded", 0),],],
["h_bascinet_2_gilded_visor_1_open_mail_aventail", "Gilded Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_1_open"),reskin("@h_bascinets_gilded", 0),],],
["h_bascinet_2_gilded_visor_5_mail_aventail", "Gilded Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_covers_head|itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_5"),reskin("@h_bascinets_gilded", 0),reskin("@h_bascinets_gilded", 2),],],
["h_bascinet_2_gilded_visor_5_open_mail_aventail", "Gilded Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_bascinet_2_visor_5_open"),reskin("@h_bascinets_gilded", 0),reskin("@h_bascinets_gilded", 2),],],
["h_bascinet_2_gilded_hundsgugel_mail_aventail", "Gilded Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_covers_head|itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_hundsgugel_2"),reskin("@h_bascinets_gilded", 0),],],
["h_bascinet_2_gilded_hundsgugel_open_mail_aventail", "Gilded Bascinet with Visor and Aventail", [("h_bascinet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_bascinet_2_aventail"),add_mesh("@h_hundsgugel_2_open"),reskin("@h_bascinets_gilded", 0),],],

# Sallet Base: 34; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; scale aventail: 12,10; mail collar with bevor: 14,12;
["h_transitional_sallet_1_bascinet_visor_1_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_transitional_sallet_1_bascinet_visor_1_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_transitional_sallet_1_bascinet_visor_1_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_1"),],],

["h_transitional_sallet_2_bascinet_visor_1_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_transitional_sallet_2_bascinet_visor_1_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_transitional_sallet_2_bascinet_visor_1_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_1"),],],

["h_transitional_sallet_3_bascinet_visor_1_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_transitional_sallet_3_bascinet_visor_1_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_1"),],],
["h_transitional_sallet_3_bascinet_visor_1_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_1"),],],

["h_transitional_sallet_1_bascinet_visor_1_open_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_transitional_sallet_1_bascinet_visor_1_open_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_transitional_sallet_1_bascinet_visor_1_open_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_1_open"),],],

["h_transitional_sallet_2_bascinet_visor_1_open_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_transitional_sallet_2_bascinet_visor_1_open_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_transitional_sallet_2_bascinet_visor_1_open_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_1_open"),],],

["h_transitional_sallet_3_bascinet_visor_1_open_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_transitional_sallet_3_bascinet_visor_1_open_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_1_open"),],],
["h_transitional_sallet_3_bascinet_visor_1_open_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_1_open"),],],

["h_transitional_sallet_1_bascinet_visor_5_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_transitional_sallet_1_bascinet_visor_5_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_transitional_sallet_1_bascinet_visor_5_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_5"),],],

["h_transitional_sallet_2_bascinet_visor_5_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_transitional_sallet_2_bascinet_visor_5_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_transitional_sallet_2_bascinet_visor_5_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_5"),],],

["h_transitional_sallet_3_bascinet_visor_5_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_transitional_sallet_3_bascinet_visor_5_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_5"),],],
["h_transitional_sallet_3_bascinet_visor_5_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_5"),],],

["h_transitional_sallet_1_bascinet_visor_5_open_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_transitional_sallet_1_bascinet_visor_5_open_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_transitional_sallet_1_bascinet_visor_5_open_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_5_open"),],],

["h_transitional_sallet_2_bascinet_visor_5_open_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_transitional_sallet_2_bascinet_visor_5_open_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_transitional_sallet_2_bascinet_visor_5_open_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_5_open"),],],

["h_transitional_sallet_3_bascinet_visor_5_open_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_transitional_sallet_3_bascinet_visor_5_open_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_bascinet_2_visor_5_open"),],],
["h_transitional_sallet_3_bascinet_visor_5_open_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_bascinet_2_visor_5_open"),],],

["h_transitional_sallet_1_transitional_visor_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_transitional_sallet_visor"),],],
["h_transitional_sallet_1_transitional_visor_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_transitional_sallet_visor"),],],
["h_transitional_sallet_1_transitional_visor_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_transitional_sallet_visor"),],],

["h_transitional_sallet_2_transitional_visor_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_transitional_sallet_visor"),],],
["h_transitional_sallet_2_transitional_visor_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_transitional_sallet_visor"),],],
["h_transitional_sallet_2_transitional_visor_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_transitional_sallet_visor"),],],

["h_transitional_sallet_3_transitional_visor_mail_collar", "Transitional Sallet Helmet with Visor and Mail Collar", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),add_mesh("@h_transitional_sallet_visor"),],],
["h_transitional_sallet_3_transitional_visor_mail_aventail", "Transitional Sallet Helmet with Visor and Mail Aventail", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),add_mesh("@h_transitional_sallet_visor"),],],
["h_transitional_sallet_3_transitional_visor_mail_collar_bevor", "Transitional Sallet Helmet with Visor and Bevor", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),add_mesh("@h_transitional_sallet_visor"),],],


["h_transitional_sallet_1_mail_collar", "Transitional Sallet Helmet with Mail Collar", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),],],
["h_transitional_sallet_1_mail_aventail", "Transitional Sallet Helmet with Mail Aventail", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),],],
["h_transitional_sallet_1_mail_collar_bevor", "Transitional Sallet Helmet with Bevor", [("h_transitional_sallet_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),],],

["h_transitional_sallet_2_mail_collar", "Transitional Sallet Helmet with Mail Collar", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),],],
["h_transitional_sallet_2_mail_aventail", "Transitional Sallet Helmet with Mail Aventail", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),],],
["h_transitional_sallet_2_mail_collar_bevor", "Transitional Sallet Helmet with Bevor", [("h_transitional_sallet_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),],],

["h_transitional_sallet_3_mail_collar", "Transitional Sallet Helmet with Mail Collar", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),],],
["h_transitional_sallet_3_mail_aventail", "Transitional Sallet Helmet with Mail Aventail", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_transitional_sallet_aventail"),],],
["h_transitional_sallet_3_mail_collar_bevor", "Transitional Sallet Helmet with Bevor", [("h_transitional_sallet_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),],],


# ["h_sallet_padded", "Sallet Helmet with Padded Cloth", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 630 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@o_padded_coif_narf"),],],
["h_sallet_mail_collar", "Sallet Helmet with Mail Collar", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar"),],],
["h_sallet_mail_aventail", "Sallet Helmet with Mail Aventail", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_aventail_chinstrap_asher"),],],
["h_sallet_mail_collar_bevor", "Sallet Helmet with Bevor", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[add_mesh("@h_mail_collar_bevor"),],],

# ["h_sallet_curved_padded", "Sallet Helmet with Padded Cloth", [("h_sallet_curved",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 630 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_sallet_curved_mail_collar", "Sallet Helmet with Mail Collar", [("h_sallet_curved",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
836 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar", 0, 0),])]],
["h_sallet_curved_mail_aventail", "Sallet Helmet with Mail Aventail", [("h_sallet_curved",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
942 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],
["h_sallet_curved_mail_collar_bevor", "Sallet Helmet with Bevor", [("h_sallet_curved",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
1056 , weight(2)|abundance(100)|head_armor(48)|body_armor(12)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_collar_bevor", 0, 0)])]],

# Eyeslot Kettlehat Base: 30; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
# ["h_eyeslot_kettlehat_1_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_eyeslot_kettlehat_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_eyeslot_kettlehat_1_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_eyeslot_kettlehat_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_eyeslot_kettlehat_1_raised_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_eyeslot_kettlehat_1_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_eyeslot_kettlehat_1_raised_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_eyeslot_kettlehat_1_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_eyeslot_kettlehat_2_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_eyeslot_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_eyeslot_kettlehat_2_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_eyeslot_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_eyeslot_kettlehat_2_raised_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_eyeslot_kettlehat_2_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_eyeslot_kettlehat_2_raised_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_eyeslot_kettlehat_2_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_eyeslot_kettlehat_3_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_eyeslot_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_eyeslot_kettlehat_3_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_eyeslot_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_oliphant_eyeslot_kettlehat_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_oliphant_eyeslot_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_oliphant_eyeslot_kettlehat_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_oliphant_eyeslot_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_oliphant_eyeslot_kettlehat_raised_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_oliphant_eyeslot_kettlehat_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_oliphant_eyeslot_kettlehat_raised_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_oliphant_eyeslot_kettlehat_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_martinus_kettlehat_3_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_martinus_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_martinus_kettlehat_3_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_martinus_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_martinus_kettlehat_3_raised_padded", "Eyeslot Kettle Helmet with Padded Cloth", [("h_martinus_kettlehat_3_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_martinus_kettlehat_3_raised_mail_aventail", "Eyeslot Kettle Helmet with Mail Aventail", [("h_martinus_kettlehat_3_raised",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],


# Oliphant Kettlehat Base: 28; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
# ["h_oliphant_kettlehat_padded", "Oliphant Kettle Helmet with Padded Cloth", [("h_oliphant_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_oliphant_kettlehat_mail_aventail", "Oliphant Kettle Helmet with Mail Aventail", [("h_oliphant_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],


# Martinus Kettlehat Base: 26; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
# ["h_martinus_kettlehat_1_padded", "Kettle Helmet with Padded Cloth", [("h_martinus_kettlehat_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_martinus_kettlehat_1_mail_aventail", "Kettle Helmet with Mail Aventail", [("h_martinus_kettlehat_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_martinus_kettlehat_2_padded", "Kettle Helmet with Padded Cloth", [("h_martinus_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 664 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_martinus_kettlehat_2_mail_aventail", "Kettle Helmet with Mail Aventail", [("h_martinus_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
876 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],


# Chapel de Fer Base: 24; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
# ["h_chapel_de_fer_padded", "Chapel de Fer with Padded Cloth", [("h_chapel_de_fer",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_chapel_de_fer_mail_aventail", "Chapel de Fer with Mail Aventail", [("h_chapel_de_fer",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],


# German Kettlehat Base: 24; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
# ["h_german_kettlehat_1_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_1_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_german_kettlehat_2_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_2_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_german_kettlehat_3_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_3_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_german_kettlehat_4_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_4_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_german_kettlehat_5_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_5",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_5_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_5",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_german_kettlehat_6_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_6",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_6_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_6",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# ["h_german_kettlehat_7_padded", "German Kettle Hat with Padded Cloth", [("h_german_kettlehat_7",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 564 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_german_kettlehat_7_mail_aventail", "German Kettle Hat with Mail Aventail", [("h_german_kettlehat_7",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
756 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],


# Cerveliere Base: 20; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
# ["h_cervelliere_padded", "Cerveliere with Padded Cloth", [("h_cervelliere",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
# 614 , weight(1.5)|abundance(100)|head_armor(26)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_cervelliere_mail_aventail", "Cervelliere with Mail Coif", [("h_cervelliere",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
816 , weight(1.5)|abundance(100)|head_armor(30)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

# Skullcap Base: 18; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_simple_cervelliere_mail_aventail", "Cervelliere with Mail Aventail", [("h_simple_cervelliere",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
518 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],

["h_skullcap_mail_aventail", "Skullcap with Mail Aventail", [("h_skullcap",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
518 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(8)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@h_mail_aventail_chinstrap_asher", 0, 0),])]],


# ["h_mail_coif_full", "Mail Coif", [("h_mail_coif_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature|itp_covers_beard   ,0, 
# 320 , weight(1.25)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
# ["h_mail_coif_balaclava", "Mail Coif", [("h_mail_coif_balaclava",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature|itp_covers_beard   ,0, 
# 292 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
# ["h_mail_coif", "Mail Coif", [("h_mail_coif",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature   ,0, 
# 266 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW HOODS | HATS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################
# Light headgear
["h_arming_cap", "Arming Cap", [("h_arming_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 38 , weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_simple_coif", "Arming Cap", [("h_simple_coif",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 4, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_simple_coif_black", "Arming Cap", [("h_simple_coif_black",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 4, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_simple_coif_brown", "Arming Cap", [("h_simple_coif_brown",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 4, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_leather_cap", "Leather Cap", [("h_leather_cap",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_mitre", "Mitre", [("h_mitre",0)],  itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_straw_hat", "Straw Hat", [("h_straw_hat",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

["h_straw_hat_1", "Peasant Straw Hat", [("h_straw_hat_1",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_straw_hat_2", "Noble Straw Hat", [("h_straw_hat_2",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_straw_hat_3", "Priest's Straw Hat", [("h_straw_hat_3",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# Leather Hats
["h_leather_hat", "Leather Hat", [("h_leather_hat",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_leather_hat_b", "Leather Hat", [("h_leather_hat_b",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_leather_hat_c", "Leather Hat", [("h_leather_hat_c",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 13, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_leather_hat_c_black", "Leather Hat", [("h_leather_hat_c",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 13, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(cur_item_set_material, "@h_leather_hats_2_black", 0, 0),])]],
["h_leather_hat_d", "Leather Hat", [("h_leather_hat_d",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 13, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_leather_hat_d_black", "Leather Hat", [("h_leather_hat_d",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 13, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(cur_item_set_material, "@h_leather_hats_2_black", 0, 0),])]],

# Women headgear
["h_court_barbette", "Barbette", [("h_court_barbette",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_court_lady_hood", "Lady's Hood", [("h_court_lady_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_court_wimple_1", "Wimple", [("h_court_wimple_1",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_court_wimple_2", "Wimple", [("h_court_wimple_2",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# Woolen Cap
["h_woolen_cap_black", "Woolen Cap", [("h_woolen_cap_black",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_blue", "Woolen Cap", [("h_woolen_cap_blue",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_brown", "Woolen Cap", [("h_woolen_cap_brown",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_green", "Woolen Cap", [("h_woolen_cap_green",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_red", "Woolen Cap", [("h_woolen_cap_red",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_white", "Woolen Cap", [("h_woolen_cap_white",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_yellow", "Woolen Cap", [("h_woolen_cap_yellow",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# Felt Hats
["h_felt_hat_b_black", "Felt Hat", [("h_felt_hat_b_black",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_blue", "Felt Hat", [("h_felt_hat_b_blue",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_brown", "Felt Hat", [("h_felt_hat_b_brown",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_green", "Felt Hat", [("h_felt_hat_b_green",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_red", "Felt Hat", [("h_felt_hat_b_red",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_white", "Felt Hat", [("h_felt_hat_b_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_yellow", "Felt Hat", [("h_felt_hat_b_yellow",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["h_felt_hat_black", "Felt Hat", [("h_felt_hat_black",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_blue", "Felt Hat", [("h_felt_hat_blue",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_brown", "Felt Hat", [("h_felt_hat_brown",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_green", "Felt Hat", [("h_felt_hat_green",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_red", "Felt Hat", [("h_felt_hat_red",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_white", "Felt Hat", [("h_felt_hat_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_yellow", "Felt Hat", [("h_felt_hat_yellow",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# Berets
["h_highlander_beret_black", "Beret", [("h_highlander_beret_black",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_blue", "Beret", [("h_highlander_beret_blue",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_brown", "Beret", [("h_highlander_beret_brown",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_green", "Beret", [("h_highlander_beret_green",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_red", "Beret", [("h_highlander_beret_red",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_white", "Beret", [("h_highlander_beret_white",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_yellow", "Beret", [("h_highlander_beret_yellow",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],

["h_highlander_beret_black_2", "Beret with plume", [("h_highlander_beret_black_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_blue_2", "Beret with plume", [("h_highlander_beret_blue_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_brown_2", "Beret with plume", [("h_highlander_beret_brown_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_green_2", "Beret with plume", [("h_highlander_beret_green_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_red_2", "Beret with plume", [("h_highlander_beret_red_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_white_2", "Beret with plume", [("h_highlander_beret_white_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_yellow_2", "Beret with plume", [("h_highlander_beret_yellow_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],

# Hoods
["h_hood_black", "Hood", [("h_hood_black",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_green", "Hood", [("h_hood_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# Padded Coifs
["h_padded_coif_black", "Padded Coif", [("h_padded_coif_black",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_blue", "Padded Coif", [("h_padded_coif_blue",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_brown", "Padded Coif", [("h_padded_coif_brown",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_green", "Padded Coif", [("h_padded_coif_green",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_red", "Padded Coif", [("h_padded_coif_red",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_white", "Padded Coif", [("h_padded_coif_white",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_yellow", "Padded Coif", [("h_padded_coif_yellow",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


############################################################################################################################################################################################################################################
###################################################################################################### HYW CLOTHES | DRESSES  ##############################################################################################################
############################################################################################################################################################################################################################################

# Peasants
["a_tavern_keeper_shirt", "Shirt", [("a_tavern_keeper_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["a_commoner_apron", "Leather Apron", [("a_commoner_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["a_merchant_outfit", "Merchant Outfit", [("a_merchant_outfit",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["a_peasant_tunic", "Peasant Tunic", [("a_peasant_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_farmer_tunic", "Tunic with vest", [("a_farmer_tunic",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["a_peasant_coat", "Coat", [("a_peasant_coat",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

# Church
["a_priest_robe", "Priest Robe", [("a_priest_robe",0)],  itp_type_body_armor  |itp_covers_legs ,0, 69 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["a_monk_robe_black", "Monk Robe", [("a_monk_robe_black",0)],  itp_type_body_armor  |itp_covers_legs ,0, 66 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["a_monk_robe_brown", "Monk Robe", [("a_monk_robe_brown",0)],  itp_type_body_armor  |itp_covers_legs ,0, 66 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["a_monk_robe_white", "Monk Robe", [("a_monk_robe_white",0)],  itp_type_body_armor  |itp_covers_legs ,0, 66 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["a_surgeon_dress", "Surgeon Robe", [("a_surgeon_dress",0)],  itp_type_body_armor  |itp_covers_legs ,0, 69 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

# Nobles
["a_noble_shirt_black", "Shirt", [("a_noble_shirt_black",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_blue", "Shirt", [("a_noble_shirt_blue",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_brown", "Shirt", [("a_noble_shirt_brown",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_green", "Shirt", [("a_noble_shirt_green",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_red", "Shirt", [("a_noble_shirt_red",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_white", "Shirt", [("a_noble_shirt_white",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

["a_tabard", "Tabard", [("a_tabard",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["a_leather_jerkin", "Leather Jerkin", [("a_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["a_houpelande_a_1", "Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_1", 0),]],
["a_houpelande_a_2", "Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_2", 0),]],
["a_houpelande_a_3", "Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_3", 0),]],
["a_houpelande_a_4", "Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_4", 0),]],
["a_houpelande_a_5", "Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_5", 0),]],

["a_houpelande_b_1", "Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_1", 0),]],
["a_houpelande_b_2", "Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_2", 0),]],
["a_houpelande_b_3", "Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_3", 0),]],
["a_houpelande_b_4", "Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_4", 0),]],
["a_houpelande_b_5", "Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_5", 0),]],

["a_haincelin_1", "Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_1", 0),]],
["a_haincelin_2", "Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_2", 0),]],
["a_haincelin_3", "Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_3", 0),]],
["a_haincelin_4", "Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_4", 0),]],
["a_haincelin_5", "Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_5", 0),]],

["a_houpelande_decorated_a_1", "Decorated Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_1", 0),]],
["a_houpelande_decorated_a_2", "Decorated Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_2", 0),]],
["a_houpelande_decorated_a_3", "Decorated Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_3", 0),]],
["a_houpelande_decorated_a_4", "Decorated Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_4", 0),]],
["a_houpelande_decorated_a_5", "Decorated Houpelande", [("a_houpelande_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_5", 0),]],

["a_houpelande_decorated_b_1", "Decorated Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_1", 0),]],
["a_houpelande_decorated_b_2", "Decorated Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_2", 0),]],
["a_houpelande_decorated_b_3", "Decorated Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_3", 0),]],
["a_houpelande_decorated_b_4", "Decorated Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_4", 0),]],
["a_houpelande_decorated_b_5", "Decorated Houpelande", [("a_houpelande_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_5", 0),]],

["a_haincelin_decorated_1", "Decorated Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_1", 0),]],
["a_haincelin_decorated_2", "Decorated Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_2", 0),]],
["a_haincelin_decorated_3", "Decorated Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_3", 0),]],
["a_haincelin_decorated_4", "Decorated Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_4", 0),]],
["a_haincelin_decorated_5", "Decorated Haincelin", [("a_haincelin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_houpelande_decorated_5", 0),]],

["a_huque_1", "Huque", [("a_huque",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_huque_1", 0),]],
["a_huque_2", "Huque", [("a_huque",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_huque_2", 0),]],

["a_huque_decorated_1", "Decorated Huque", [("a_huque",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_huque_decorated_1", 0),]],
["a_huque_decorated_2", "Decorated Huque", [("a_huque",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_huque_decorated_2", 0),]],
["a_huque_decorated_3", "Decorated Huque", [("a_huque",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_huque_decorated_3", 0),]],
["a_huque_decorated_4", "Decorated Huque", [("a_huque",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [reskin("@a_huque_decorated_4", 0),]],

# ["a_cotehardie_blue", "Cotehardie", [("a_cotehardie_belt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(str_clear, s1),(str_store_string, s1, "@0xd38c70"),add_mesh_vertex("@a_cotehardie_cloth", s1),]],
# ["a_cotehardie_brown", "Cotehardie", [("a_cotehardie_belt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [add_mesh("@a_cotehardie_cloth"),]],

# Robes
["a_woman_court_dress_1", "Noblewoman Dress", [("a_woman_court_dress_1",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_2", "Noblewoman Dress", [("a_woman_court_dress_2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_3", "Noblewoman Dress", [("a_woman_court_dress_3",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_4", "Noblewoman Dress", [("a_woman_court_dress_4",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_5", "Noblewoman Dress", [("a_woman_court_dress_5",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_6", "Noblewoman Dress", [("a_woman_court_dress_6",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW ARMORS ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# Gambesons
# ["a_gambeson_black", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_black", 0, 0),])]],
# ["a_gambeson_blue", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_blue", 0, 0),])]],
# ["a_gambeson_brown", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_brown", 0, 0),])]],
# ["a_gambeson_green", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_green", 0, 0),])]],
# ["a_gambeson_red", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_red", 0, 0),])]],
# ["a_gambeson_white", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],

# Asher's Aketons
# Base version
# ["a_aketon_asher_beige_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 # [aketon_patch(),add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),],],
# ["a_aketon_asher_beige_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 # [aketon_patch(),add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_2"),],],

# ["a_aketon_asher_white_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 # [add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),aketon_patch(),reskin("@a_aketon_asher_white",1),reskin("@a_aketon_asher_arms_white",2),],],
# ["a_aketon_asher_white_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 # [add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_2"),aketon_patch(),reskin("@a_aketon_asher_white",1),reskin("@a_aketon_asher_arms_white",2),],],

["a_aketon_asher_blue_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_1"),aketon_patch(),reskin("@a_aketon_asher_blue",1),reskin("@a_aketon_asher_arms_blue",2),],],
["a_aketon_asher_blue_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_1"),aketon_patch(),reskin("@a_aketon_asher_blue",1),reskin("@a_aketon_asher_arms_blue",2),],],

["a_aketon_asher_green_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_green",1),reskin("@a_aketon_asher_arms_green",2),aketon_patch(),],],
["a_aketon_asher_green_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_green",1),reskin("@a_aketon_asher_arms_green",2),aketon_patch(),],],

# Vandyked
["a_aketon_asher_vandyked_blue_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_vandyked"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_vandyked_blue",1),reskin("@a_aketon_asher_arms_blue",2),aketon_patch(),],],
["a_aketon_asher_vandyked_blue_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_vandyked"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_vandyked_blue",1),reskin("@a_aketon_asher_arms_blue",2),aketon_patch(),],],

["a_aketon_asher_vandyked_red_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_vandyked"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_vandyked_red",1),reskin("@a_aketon_asher_arms_red",2),aketon_patch(),],],
["a_aketon_asher_vandyked_red_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_vandyked"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_vandyked_red",1),reskin("@a_aketon_asher_arms_red",2),aketon_patch(),],],

# Dagged
["a_aketon_asher_dagged_beige_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_dagged_beige",1),reskin("@a_aketon_asher_arms_beige",2),aketon_patch(),],],
["a_aketon_asher_dagged_beige_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_dagged_beige",1),reskin("@a_aketon_asher_arms_beige",2),aketon_patch(),],],

["a_aketon_asher_dagged_white_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_dagged_white",1),reskin("@a_aketon_asher_arms_white",2),aketon_patch(),],],
["a_aketon_asher_dagged_white_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_dagged_white",1),reskin("@a_aketon_asher_arms_white",2),aketon_patch(),],],

["a_aketon_asher_dagged_blue_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_4"),reskin("@a_aketon_asher_dagged_blue",1),reskin("@a_aketon_asher_arms_blue",2),aketon_patch(),],],
["a_aketon_asher_dagged_blue_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_5"),reskin("@a_aketon_asher_dagged_blue",1),reskin("@a_aketon_asher_arms_blue",2),aketon_patch(),],],

["a_aketon_asher_dagged_green_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_4"),reskin("@a_aketon_asher_dagged_green",1),reskin("@a_aketon_asher_arms_green",2),aketon_patch(),],],
["a_aketon_asher_dagged_green_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_3"),reskin("@a_aketon_asher_dagged_green",1),reskin("@a_aketon_asher_arms_green",2),aketon_patch(),],],

["a_aketon_asher_dagged_red_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_dagged_red",1),reskin("@a_aketon_asher_arms_red",2),aketon_patch(),],],
["a_aketon_asher_dagged_red_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_3"),reskin("@a_aketon_asher_dagged_red",1),reskin("@a_aketon_asher_arms_red",2),aketon_patch(),],],

["a_aketon_asher_dagged_thick_beige_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_dagged_thick_beige",1),reskin("@a_aketon_asher_arms_beige",2),aketon_patch(),],],
["a_aketon_asher_dagged_thick_beige_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_4"),reskin("@a_aketon_asher_dagged_thick_beige",1),reskin("@a_aketon_asher_arms_beige",2),aketon_patch(),],],

["a_aketon_asher_dagged_thick_white_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_5"),reskin("@a_aketon_asher_dagged_thick_white",1),reskin("@a_aketon_asher_arms_white",2),aketon_patch(),],],
["a_aketon_asher_dagged_thick_white_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_4"),reskin("@a_aketon_asher_dagged_thick_white",1),reskin("@a_aketon_asher_arms_white",2),aketon_patch(),],],

["a_aketon_asher_dagged_thick_blue_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_dagged_thick_blue",1),reskin("@a_aketon_asher_arms_blue",2),aketon_patch(),],],
["a_aketon_asher_dagged_thick_blue_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_3"),reskin("@a_aketon_asher_dagged_thick_blue",1),reskin("@a_aketon_asher_arms_blue",2),aketon_patch(),],],

["a_aketon_asher_dagged_thick_red_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_4"),reskin("@a_aketon_asher_dagged_thick_red",1),reskin("@a_aketon_asher_arms_red",2),aketon_patch(),],],
["a_aketon_asher_dagged_thick_red_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_5"),reskin("@a_aketon_asher_dagged_thick_red",1),reskin("@a_aketon_asher_arms_red",2),aketon_patch(),],],

["a_aketon_asher_dagged_thick_black_1", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_a"),add_mesh("@a_aketon_asher_sleeve_2"),reskin("@a_aketon_asher_dagged_thick_black",1),reskin("@a_aketon_asher_arms_black",2),aketon_patch(),],],
["a_aketon_asher_dagged_thick_black_2", "Aketon", [("a_aketon_asher_patch",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
 [add_mesh("@a_aketon_asher_dagged"),add_mesh("@a_aketon_asher_arms_b"),add_mesh("@a_aketon_asher_sleeve_1"),reskin("@a_aketon_asher_dagged_thick_black",1),reskin("@a_aketon_asher_arms_black",2),aketon_patch(),],],

### Pistoia Line
["a_pistoia_mail_a_mail_sleeves_short", "Short-sleeved Mail Hauberk", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_short"),]],
["a_pistoia_mail_b_mail_sleeves_short", "Short-sleeved Mail Hauberk", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_short"),]],

["a_pistoia_mail_a_mail_sleeves_short_plate_1", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_mail_b_mail_sleeves_short_plate_1", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_mail_a_mail_sleeves_short_plate_2", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_mail_b_mail_sleeves_short_plate_2", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_mail_a_mail_sleeves_short_plate_3", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_3"),]],
["a_pistoia_mail_b_mail_sleeves_short_plate_3", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_short"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_mail_a_mail_sleeves", "Long-sleeved Mail Hauberk", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],
["a_pistoia_mail_b_mail_sleeves", "Long-sleeved Mail Hauberk", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],

["a_pistoia_mail_a_mail_sleeves_jackchains", "Long-sleeved Mail Hauberk with Jack Chains", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],
["a_pistoia_mail_b_mail_sleeves_jackchains", "Long-sleeved Mail Hauberk with Jack Chains", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],

["a_pistoia_mail_a_mail_sleeves_over_plate", "Long-sleeved Mail Hauberk", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_plate"),]],
["a_pistoia_mail_b_mail_sleeves_over_plate", "Long-sleeved Mail Hauberk", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_plate"),]],

["a_pistoia_mail_a_mail_sleeves_plate_1", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_medium"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_mail_b_mail_sleeves_plate_1", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_medium"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_mail_a_mail_sleeves_plate_2", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_medium"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_mail_b_mail_sleeves_plate_2", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_medium"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_mail_a_mail_sleeves_plate_3", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_medium"),add_mesh("@a_pistoia_couters_3"),]],
["a_pistoia_mail_b_mail_sleeves_plate_3", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_medium"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_mail_a_mail_sleeves_plate_spaulders_1", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_mail_b_mail_sleeves_plate_spaulders_1", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_mail_a_mail_sleeves_plate_spaulders_2", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_mail_b_mail_sleeves_plate_spaulders_2", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_mail_a_mail_sleeves_plate_spaulders_3", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],
["a_pistoia_mail_b_mail_sleeves_plate_spaulders_3", "Short-sleeved Mail Hauberk with Plate Arm Harness", [("a_pistoia_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_breastplate_half_mail_sleeves", "Demi Breastplate over Mail", [("a_pistoia_breastplate_half",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],

["a_pistoia_breastplate_half_mail_sleeves_jackchain", "Demi Breastplate with Jack Chains", [("a_pistoia_breastplate_half",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],

["a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_1", "Demi Breastplate with Plate Arm Harness", [("a_pistoia_breastplate_half",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_2", "Demi Breastplate with Plate Arm Harness", [("a_pistoia_breastplate_half",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_breastplate_half_mail_sleeves_plate_spaulders_3", "Demi Breastplate with Plate Arm Harness", [("a_pistoia_breastplate_half",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_breastplate_mail_sleeves", "Breastplate over Mail", [("a_pistoia_breastplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],

["a_pistoia_breastplate_mail_sleeves_jackchain", "Breastplate with Jack Chains", [("a_pistoia_breastplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],

["a_pistoia_breastplate_mail_sleeves_plate_spaulders_1", "Breastplate with Plate Arm Harness", [("a_pistoia_breastplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_breastplate_mail_sleeves_plate_spaulders_2", "Breastplate with Plate Arm Harness", [("a_pistoia_breastplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_breastplate_mail_sleeves_plate_spaulders_3", "Breastplate with Plate Arm Harness", [("a_pistoia_breastplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_breastplate_2_mail_sleeves", "Breastplate over Mail", [("a_pistoia_breastplate_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],

["a_pistoia_breastplate_2_mail_sleeves_jackchain", "Breastplate with Jack Chains", [("a_pistoia_breastplate_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],

["a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_1", "Breastplate with Plate Arm Harness", [("a_pistoia_breastplate_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_2", "Breastplate with Plate Arm Harness", [("a_pistoia_breastplate_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_breastplate_2_mail_sleeves_plate_spaulders_3", "Breastplate with Plate Arm Harness", [("a_pistoia_breastplate_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_kastenbrust_a_mail_sleeves", "Kastenbrust over Mail", [("a_pistoia_kastenbrust_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],

["a_pistoia_kastenbrust_a_mail_sleeves_jackchain", "Kastenbrust with Jack Chains", [("a_pistoia_kastenbrust_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],

["a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_1", "Kastenbrust with Plate Arm Harness", [("a_pistoia_kastenbrust_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_2", "Kastenbrust with Plate Arm Harness", [("a_pistoia_kastenbrust_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_kastenbrust_a_mail_sleeves_plate_spaulders_3", "Kastenbrust with Plate Arm Harness", [("a_pistoia_kastenbrust_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

["a_pistoia_kastenbrust_b_mail_sleeves", "Kastenbrust over Mail", [("a_pistoia_kastenbrust_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),]],
                        
["a_pistoia_kastenbrust_b_mail_sleeves_jackchain", "Kastenbrust with Jack Chains", [("a_pistoia_kastenbrust_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),]],
                        
["a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_1", "Kastenbrust with Plate Arm Harness", [("a_pistoia_kastenbrust_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_2", "Kastenbrust with Plate Arm Harness", [("a_pistoia_kastenbrust_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_pistoia_kastenbrust_b_mail_sleeves_plate_spaulders_3", "Kastenbrust with Plate Arm Harness", [("a_pistoia_kastenbrust_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

### Padded over Plate
["a_padded_over_plate_sleeved_deco_1", "Decorated Longsleeved Padded over Plate", [("a_padded_over_plate_sleeved_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [reskin("@a_padded_over_plate_deco_1",0),],],
["a_padded_over_plate_sleeveless_deco_1", "Decorated Sleeveless Padded over Plate", [("a_padded_over_plate_sleeveless_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [reskin("@a_padded_over_plate_deco_1",0),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_padded_over_plate_sleeved_deco_2", "Decorated Longsleeved Padded over Plate", [("a_padded_over_plate_sleeved_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [reskin("@a_padded_over_plate_deco_2",0),],],
["a_padded_over_plate_sleeveless_deco_2", "Decorated Sleeveless Padded over Plate", [("a_padded_over_plate_sleeveless_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [reskin("@a_padded_over_plate_deco_2",0),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],

### Continental Plate
["a_continental_plate_a", "Plate Armour", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_continental_plate_b", "Plate Armour", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_continental_plate_c", "Plate Armour", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

### Kastenbrust Plate
["a_plate_kastenbrust_a", "Kastenbrust Plate Armour", [("a_plate_kastenbrust",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_plate_kastenbrust_b", "Kastenbrust Plate Armour", [("a_plate_kastenbrust",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_plate_kastenbrust_c", "Kastenbrust Plate Armour", [("a_plate_kastenbrust",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

### English Plate Armour
# 1415 Version
["a_english_plate_1415_a", "English Plate Armour (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),]],
["a_english_plate_1415_b", "English Plate Armour (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),]],

["a_english_plate_1415_a_besagews_round", "English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),add_mesh("@a_arm_harness_english_1415_besagews_round"),]],
["a_english_plate_1415_b_besagews_round", "English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),add_mesh("@a_arm_harness_english_1415_besagews_round"),]],

["a_english_plate_1415_a_besagews_square", "English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),add_mesh("@a_arm_harness_english_1415_besagews_square"),]],
["a_english_plate_1415_b_besagews_square", "English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),add_mesh("@a_arm_harness_english_1415_besagews_square"),]],

["a_english_plate_1415_a_gilded", "Gilded English Plate Armour (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),reskin("@a_english_plate_1415_gilded", 0),reskin("@a_arm_harness_english_1415_gilded", 1),]],
["a_english_plate_1415_b_gilded", "Gilded English Plate Armour (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),reskin("@a_english_plate_1415_gilded", 0),reskin("@a_arm_harness_english_1415_gilded", 1),]],

["a_english_plate_1415_a_gilded_besagews_round", "Gilded English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),add_mesh("@a_arm_harness_english_1415_besagews_round"),reskin("@a_english_plate_1415_gilded", 0),reskin("@a_arm_harness_english_1415_gilded", 1),reskin("@a_arm_harness_english_1415_gilded", 2),]],
["a_english_plate_1415_b_gilded_besagews_round", "Gilded English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),add_mesh("@a_arm_harness_english_1415_besagews_round"),reskin("@a_english_plate_1415_gilded", 0),reskin("@a_arm_harness_english_1415_gilded", 1),reskin("@a_arm_harness_english_1415_gilded", 2),]],

["a_english_plate_1415_a_gilded_besagews_square", "Gilded English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),add_mesh("@a_arm_harness_english_1415_besagews_square"),reskin("@a_english_plate_1415_gilded", 0),reskin("@a_arm_harness_english_1415_gilded", 1),reskin("@a_arm_harness_english_1415_gilded", 2),]],
["a_english_plate_1415_b_gilded_besagews_square", "Gilded English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),add_mesh("@a_arm_harness_english_1415_besagews_square"),reskin("@a_english_plate_1415_gilded", 0),reskin("@a_arm_harness_english_1415_gilded", 1),reskin("@a_arm_harness_english_1415_gilded", 2),]],

["a_english_plate_1415_a_blued", "Blued English Plate Armour (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),reskin("@a_english_plate_1415_blued", 0),reskin("@a_arm_harness_english_1415_blued", 1),]],
["a_english_plate_1415_b_blued", "Blued English Plate Armour (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),reskin("@a_english_plate_1415_blued", 0),reskin("@a_arm_harness_english_1415_blued", 1),]],

["a_english_plate_1415_a_blued_besagews_round", "Blued English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),add_mesh("@a_arm_harness_english_1415_besagews_round"),reskin("@a_english_plate_1415_blued", 0),reskin("@a_arm_harness_english_1415_blued", 1),reskin("@a_arm_harness_english_1415_blued", 2),]],
["a_english_plate_1415_b_blued_besagews_round", "Blued English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),add_mesh("@a_arm_harness_english_1415_besagews_round"),reskin("@a_english_plate_1415_blued", 0),reskin("@a_arm_harness_english_1415_blued", 1),reskin("@a_arm_harness_english_1415_blued", 2),]],

["a_english_plate_1415_a_blued_besagews_square", "Blued English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_a"),add_mesh("@a_arm_harness_english_1415_besagews_square"),reskin("@a_english_plate_1415_blued", 0),reskin("@a_arm_harness_english_1415_blued", 1),reskin("@a_arm_harness_english_1415_blued", 2),]],
["a_english_plate_1415_b_blued_besagews_square", "Blued English Plate Armour with Besagews (1415)", [("a_english_plate_1415",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1415_b"),add_mesh("@a_arm_harness_english_1415_besagews_square"),reskin("@a_english_plate_1415_blued", 0),reskin("@a_arm_harness_english_1415_blued", 1),reskin("@a_arm_harness_english_1415_blued", 2),]],

# 1430 - 1445 Version
["a_english_plate_1430_1445", "English Plate Armour (1430)", [("a_english_plate_1430_1445",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1430_1445"),]],
["a_english_plate_1430_1445_gilded", "Gilded English Plate Armour (1430)", [("a_english_plate_1430_1445",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1430_1445"),reskin("@a_english_plate_1430_1445_gilded", 0),reskin("@a_arm_harness_english_1430_1450_gilded", 1),]],

# 1435 - 1450 Version
["a_english_plate_1435_1450", "English Plate Armour (1435)", [("a_english_plate_1435_1450",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1430_1450"),]],
["a_english_plate_1435_1450_gilded", "Gilded English Plate Armour (1435)", [("a_english_plate_1435_1450",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1430_1450"),reskin("@a_english_plate_1435_1450_gilded", 0),reskin("@a_arm_harness_english_1430_1450_gilded", 1),]],

# 1440 - 1450 Version
["a_english_plate_1445_1450", "English Plate Armour (1440)", [("a_english_plate_1445_1450",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1440"),]],
["a_english_plate_1445_1450_gilded", "Gilded English Plate Armour (1440)", [("a_english_plate_1445_1450",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[add_mesh("@a_arm_harness_english_1440"),reskin("@a_english_plate_1445_1450_gilded", 0),reskin("@a_arm_harness_english_1440_gilded", 1),]],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### DAC HERALDIC ITEMS ########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### Heraldic Armors
# ["heraldic_brigandine_native", "Heraldic Brigandine", [("heraldic_brigandine_native",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 # 2230 , weight(20)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(10) ,imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_native", ":agent_no", ":troop_no")])]],
 
# ["heraldic_brigandine_narf_padded_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1120 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],
# ["heraldic_brigandine_narf_padded_jackchain_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1200 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

# ["heraldic_brigandine_narf_padded_plate_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2270 , weight(22)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],
# ["heraldic_brigandine_narf_padded_plate_disc_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2270 , weight(23)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_plate_disc", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],
# ["heraldic_brigandine_narf_mail_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2270 , weight(24)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],], 

# ["heraldic_brigandine_narf_plate_mail_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2370 , weight(26)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],
# ["heraldic_brigandine_narf_plate_disc_mail_full_plate_hose_custom", "Heraldic Brigandine", [("heraldic_brigandine_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2430 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_brigandine_narf", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

# ["heraldic_tunic_new", "Heraldic Tunic", [("heraldic_tunic_new",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 # 1940 , weight(20)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(10) ,imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_short_tunic_new", ":agent_no", ":troop_no")])]],

# ["heraldic_mail_tabard", "Heraldic Tabard with Mail", [("tabard_b_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_mail_tabard", ":agent_no", ":troop_no")])]],

# ["heraldic_churburg_13_tabard", "Heraldic Churburg Armor", [("heraldic_churburg_13_tabard",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4250, weight(27)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(20)|difficulty(8), imodbits_plate, 
# [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_churburg_13_tabard",":agent_no",":troop_no"),])] ],
# ["heraldic_churburg_13_brass_tabard", "Heraldic Brass Churburg Armor", [("heraldic_churburg_13_brass_tabard",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4430, weight(27)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(20)|difficulty(8), imodbits_plate, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_churburg_13_brass_tabard",":agent_no",":troop_no"),])] ],

# ["heraldic_jupon", "Heraldic jupon", [("a_churburg_jupon_heraldic",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 # 5400, weight(28)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_plate  , [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_jupon",":agent_no",":troop_no"),])] ],

# ["heraldic_plate", "Heraldic Plate Harness", [("heraldic_plate",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 # 6550, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_plate  , [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_plate",":agent_no",":troop_no"),])] ],

# ["a_heraldic_cuirass", "Heraldic Cuirass", [("a_heraldic_cuirass",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 # 6550, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_plate  , [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_plate_cuirass",":agent_no",":troop_no"),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),])] ],

# ["a_english_plate_mail_heraldic", "Heraldic English Plate Armour", [("a_english_plate_mail_heraldic",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 # 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_english_plate_mail", ":agent_no", ":troop_no")])]],
# ["a_english_plate_heraldic", "Heraldic English Plate Armour", [("a_english_plate_heraldic",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 # 6540, weight(29)|abundance(100)|head_armor(0)|body_armor(64)|leg_armor(24)|difficulty(9), imodbits_armor,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_english_plate", ":agent_no", ":troop_no")])]],

# ["a_tabard_heraldic", "Heraldic Tabard", [("a_tabard_heraldic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 # 147 , weight(2)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(7) ,imodbits_cloth,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_tabard", ":agent_no", ":troop_no")])]],

["a_english_plate_1415_heraldic", "Heraldic Covered Plate", [("a_english_plate_1415_heraldic",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[heraldic("tableau_a_english_plate_1415_heraldic"),add_mesh("@a_arm_harness_english_1415_b"),reskin("@a_arm_harness_english_1415_gilded", 1),]],

["a_jupon_heraldic", "Heraldic Jupon", [("a_jupon_heraldic",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[heraldic("tableau_a_jupon_heraldic"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],

["a_jupon_heraldic_belt_1", "Heraldic Jupon", [("a_jupon_heraldic_belt_1",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[heraldic("tableau_a_jupon_heraldic"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],
["a_jupon_heraldic_belt_2", "Heraldic Jupon", [("a_jupon_heraldic_belt_1",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[heraldic("tableau_a_jupon_heraldic"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],
["a_jupon_heraldic_belt_3", "Heraldic Jupon", [("a_jupon_heraldic_belt_1",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[heraldic("tableau_a_jupon_heraldic"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],
["a_jupon_heraldic_belt_4", "Heraldic Jupon", [("a_jupon_heraldic_belt_1",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0,
 5550, weight(29)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_armor,[heraldic("tableau_a_jupon_heraldic"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),]],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW BOOTS | SHOES | LEG ARMOR #############################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# ["b_wrapping_boots", "Wrapping Boots", [("b_wrapping_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
# ["b_ankle_boots", "Ankle Boots", [("b_ankle_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
# ["b_leather_boots", "Leather Boots", [("b_leather_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0, 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
# ["b_mail_chausses", "Mail Chausses", [("b_mail_chausses",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
# ["b_mail_boots", "Mail Boots", [("b_mail_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 880 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
# ["b_steel_greaves", "Steel Greaves", [("b_steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
# ["b_splinted_greaves_nospurs", "Splinted Greaves", [("b_splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
# ["b_splinted_greaves_spurs", "Splinted Greaves with Spurs", [("b_splinted_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
# ["b_shynbaulds", "Shynbaulds", [("b_shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1329 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_plate ],
# ["b_steel_greaves_full", "Shynbaulds", [("b_shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1329 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_plate ],

["b_turnshoes_1",  "Turnshoes", [("b_turnshoes_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_2",  "Turnshoes", [("b_turnshoes_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_3",  "Turnshoes", [("b_turnshoes_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_4",  "Turnshoes", [("b_turnshoes_4",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_5",  "Turnshoes", [("b_turnshoes_5",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_6",  "Turnshoes", [("b_turnshoes_6",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_7",  "Turnshoes", [("b_turnshoes_7",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_8",  "Turnshoes", [("b_turnshoes_8",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_9",  "Turnshoes", [("b_turnshoes_9",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_turnshoes_lined_1", "Turnshoes", [("b_turnshoes_lined_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_lined_2", "Turnshoes", [("b_turnshoes_lined_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_turnshoes_lined_3", "Turnshoes", [("b_turnshoes_lined_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_low_boots_1",  "Low Boots", [("b_low_boots_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_2",  "Low Boots", [("b_low_boots_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_3",  "Low Boots", [("b_low_boots_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_4",  "Low Boots", [("b_low_boots_4",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_5",  "Low Boots", [("b_low_boots_5",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_6",  "Low Boots", [("b_low_boots_6",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_7",  "Low Boots", [("b_low_boots_7",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_8",  "Low Boots", [("b_low_boots_8",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_9",  "Low Boots", [("b_low_boots_9",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_low_boots_lined_1", "Low Boots", [("b_low_boots_lined_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_lined_2", "Low Boots", [("b_low_boots_lined_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_low_boots_lined_3", "Low Boots", [("b_low_boots_lined_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_poulaines_1",  "Poulaines", [("b_poulaines_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_2",  "Poulaines", [("b_poulaines_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_3",  "Poulaines", [("b_poulaines_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_4",  "Poulaines", [("b_poulaines_4",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_5",  "Poulaines", [("b_poulaines_5",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_6",  "Poulaines", [("b_poulaines_6",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_7",  "Poulaines", [("b_poulaines_7",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_8",  "Poulaines", [("b_poulaines_8",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_9",  "Poulaines", [("b_poulaines_9",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_poulaines_lined_1", "Poulaines", [("b_poulaines_lined_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_lined_2", "Poulaines", [("b_poulaines_lined_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_poulaines_lined_3", "Poulaines", [("b_poulaines_lined_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_high_boots_1",  "High Boots", [("b_high_boots_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_2",  "High Boots", [("b_high_boots_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_3",  "High Boots", [("b_high_boots_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_4",  "High Boots", [("b_high_boots_4",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_5",  "High Boots", [("b_high_boots_5",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_6",  "High Boots", [("b_high_boots_6",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_7",  "High Boots", [("b_high_boots_7",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_8",  "High Boots", [("b_high_boots_8",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_9",  "High Boots", [("b_high_boots_9",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_high_boots_lined_1", "High Boots", [("b_high_boots_lined_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_lined_2", "High Boots", [("b_high_boots_lined_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_lined_3", "High Boots", [("b_high_boots_lined_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_high_boots_folded_1",  "Folded High Boots", [("b_high_boots_folded_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_2",  "Folded High Boots", [("b_high_boots_folded_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_3",  "Folded High Boots", [("b_high_boots_folded_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_4",  "Folded High Boots", [("b_high_boots_folded_4",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_5",  "Folded High Boots", [("b_high_boots_folded_5",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_6",  "Folded High Boots", [("b_high_boots_folded_6",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_7",  "Folded High Boots", [("b_high_boots_folded_7",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_8",  "Folded High Boots", [("b_high_boots_folded_8",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_9",  "Folded High Boots", [("b_high_boots_folded_9",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_high_boots_folded_lined_1", "Folded High Boots", [("b_high_boots_folded_lined_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_lined_2", "Folded High Boots", [("b_high_boots_folded_lined_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["b_high_boots_folded_lined_3", "Folded High Boots", [("b_high_boots_folded_lined_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 12 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["b_leg_harness_1",  "Leg Harness with Leather Sabatons", [("b_leg_harness_1",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_2",  "Leg Harness with Leather Sabatons", [("b_leg_harness_2",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_3",  "Leg Harness with Leather Sabatons", [("b_leg_harness_3",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_4",  "Leg Harness with Plate Sabatons", [("b_leg_harness_4",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_5",  "Leg Harness with Mail Sabatons", [("b_leg_harness_5",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_6",  "Leg Harness with Coloured Sabatons", [("b_leg_harness_6",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_7",  "Leg Harness with Plate Sabatons", [("b_leg_harness_7",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_8",  "Leg Harness with Scale Sabatons", [("b_leg_harness_8",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_9",  "Leg Harness with Plate Sabatons", [("b_leg_harness_9",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_10", "Leg Harness with Plate Sabatons", [("b_leg_harness_10",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],

["b_leg_harness_1_gilded",  "Gilded Leg Harness with Leather Sabatons", [("b_leg_harness_1_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_2_gilded",  "Gilded Leg Harness with Leather Sabatons", [("b_leg_harness_2_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_3_gilded",  "Gilded Leg Harness with Leather Sabatons", [("b_leg_harness_3_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_4_gilded",  "Gilded Leg Harness with Plate Sabatons", [("b_leg_harness_4_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_5_gilded",  "Gilded Leg Harness with Mail Sabatons", [("b_leg_harness_5_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_6_gilded",  "Gilded Leg Harness with Coloured Sabatons", [("b_leg_harness_6_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_7_gilded",  "Gilded Leg Harness with Plate Sabatons", [("b_leg_harness_7_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_8_gilded",  "Gilded Leg Harness with Scale Sabatons", [("b_leg_harness_8_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_9_gilded",  "Gilded Leg Harness with Plate Sabatons", [("b_leg_harness_9_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_10_gilded", "Gilded Leg Harness with Plate Sabatons", [("b_leg_harness_10_gilded",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],

["b_leg_harness_english_1415",  "English Leg Harness (1415)", [("b_leg_harness_english_1415",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1420",  "English Leg Harness (1420)", [("b_leg_harness_english_1420",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1430",  "English Leg Harness (1430)", [("b_leg_harness_english_1430",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1435",  "English Leg Harness (1435)", [("b_leg_harness_english_1435",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1440",  "English Leg Harness (1440)", [("b_leg_harness_english_1440",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],

["b_leg_harness_english_1415_gilded",  "Gilded English Leg Harness (1415)", [("b_leg_harness_english_1415_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1420_gilded",  "Gilded English Leg Harness (1420)", [("b_leg_harness_english_1420_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1430_gilded",  "Gilded English Leg Harness (1430)", [("b_leg_harness_english_1430_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1435_gilded",  "Gilded English Leg Harness (1435)", [("b_leg_harness_english_1435_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["b_leg_harness_english_1440_gilded",  "Gilded English Leg Harness (1440)", [("b_leg_harness_english_1440_gilded",0)],  itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW GLOVES | GAUNTLETS | POWER GAUNTLETS ##################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["g_leather_gauntlet","Leather Gloves", [("g_leather_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["g_demi_gauntlets","Demi Gauntlets", [("g_demi_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["g_finger_gauntlets","Finger Gauntlets", [("g_finger_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],

["g_gauntlets_mailed","Mailed Gauntlets", [("g_gauntlets_mailed_L",0)], itp_merchandise|itp_type_hand_armor,0, 1100, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["g_gauntlets_segmented_a","Segmented Gauntlets", [("g_gauntlets_segmented_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 1240, weight(1.0)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],
["g_gauntlets_segmented_b","Segmented Gauntlets", [("g_gauntlets_segmented_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 1240, weight(1.0)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],

["g_gauntlets_gilded_mailed","Gilded Mailed Gauntlets", [("g_gauntlets_gilded_mailed_L",0)], itp_merchandise|itp_type_hand_armor,0, 1100, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["g_gauntlets_gilded_segmented_a","Gilded Segmented Gauntlets", [("g_gauntlets_gilded_segmented_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 1240, weight(1.0)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],
["g_gauntlets_gilded_segmented_b","Gilded Segmented Gauntlets", [("g_gauntlets_gilded_segmented_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 1240, weight(1.0)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],
 

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW CUSTOMIZABLE ITEMS ####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# Seek & Destroy Item variants with Kham's Armor customization
# Material Switch

### Custom Hoods for helmets
### The custom helmets are inside a loop for the color assignment, don't change their position without changing the loop boundaries 
# Sallet Base: 34; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_sallet_hood_custom", "Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
526 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_sallet_hood_custom"),add_mesh("@h_sallet")]],
["h_sallet_hood_curved_custom", "Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
526 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_sallet_hood_curved_custom"),add_mesh("@h_sallet_curved")]],

["h_transitional_sallet_1_hood_custom", "Transitional Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
526 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_transitional_sallet_1_hood_custom"),add_mesh("@h_transitional_sallet_1")]],
["h_transitional_sallet_2_hood_custom", "Transitional Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
526 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_transitional_sallet_2_hood_custom"),add_mesh("@h_transitional_sallet_2")]],
["h_transitional_sallet_3_hood_custom", "Transitional Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
526 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_transitional_sallet_3_hood_custom"),add_mesh("@h_transitional_sallet_3")]],

["h_transitional_sallet_gilded_1_hood_custom", "Gilded Transitional Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
582 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_transitional_sallet_gilded_1_hood_custom"),add_mesh("@h_transitional_sallet_1"),reskin("@h_bascinets_gilded", 1),]],
["h_transitional_sallet_gilded_2_hood_custom", "Gilded Transitional Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
582 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_transitional_sallet_gilded_2_hood_custom"),add_mesh("@h_transitional_sallet_2"),reskin("@h_bascinets_gilded", 1),]],
["h_transitional_sallet_gilded_3_hood_custom", "Gilded Transitional Sallet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
582 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[custom_reskin("itm_h_transitional_sallet_gilded_3_hood_custom"),add_mesh("@h_transitional_sallet_3"),reskin("@h_bascinets_gilded", 1),]],

# Eyeslot Kettlehat Base: 30; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_eyeslot_kettlehat_1_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_1_hood_custom"),add_mesh("@h_eyeslot_kettlehat_1"),]],
["h_eyeslot_kettlehat_1_raised_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_1_raised_hood_custom"),add_mesh("@h_eyeslot_kettlehat_1_raised"),]],

["h_eyeslot_kettlehat_2_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_2_hood_custom"),add_mesh("@h_eyeslot_kettlehat_2"),]],
["h_eyeslot_kettlehat_2_raised_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_2_raised_hood_custom"),add_mesh("@h_eyeslot_kettlehat_2_raised"),]],

["h_eyeslot_kettlehat_3_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_3_hood_custom"),add_mesh("@h_eyeslot_kettlehat_3"),]],

["h_oliphant_eyeslot_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_oliphant_eyeslot_hood_custom"),add_mesh("@h_oliphant_eyeslot_kettlehat"),]],
["h_oliphant_eyeslot_raised_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_oliphant_eyeslot_raised_hood_custom"),add_mesh("@h_oliphant_eyeslot_kettlehat_raised"),]],

["h_martinus_kettlehat_3_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_3_hood_custom"),add_mesh("@h_martinus_kettlehat_3"),]],
["h_martinus_kettlehat_3_raised_hood_custom", "Eyeslot Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_3_raised_hood_custom"),add_mesh("@h_martinus_kettlehat_3_raised"),]],


# Oliphant Kettlehat Base: 28; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_oliphant_kettlehat_hood_custom", "Oliphant Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_oliphant_kettlehat_hood_custom"),add_mesh("@h_oliphant_kettlehat"),]],

# Martinus Kettlehat Base: 26; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_martinus_kettlehat_1_hood_custom", "Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_1_hood_custom"),add_mesh("@h_martinus_kettlehat_1"),]],
["h_martinus_kettlehat_2_hood_custom", "Kettle Helmet with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_2_hood_custom"),add_mesh("@h_martinus_kettlehat_2"),]],

# Chapel de Fer Base: 24; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_chapel_de_fer_hood_custom", "Chapel de Fer with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_chapel_de_fer_hood_custom"),add_mesh("@h_chapel_de_fer"),]],

# German Kettlehat Base: 24; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_german_kettlehat_1_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_1_hood_custom"),add_mesh("@h_german_kettlehat_1"),]],
["h_german_kettlehat_2_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_2_hood_custom"),add_mesh("@h_german_kettlehat_2"),]],
["h_german_kettlehat_3_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_3_hood_custom"),add_mesh("@h_german_kettlehat_3"),]],
["h_german_kettlehat_4_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_4_hood_custom"),add_mesh("@h_german_kettlehat_4"),]],
["h_german_kettlehat_5_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_5_hood_custom"),add_mesh("@h_german_kettlehat_5"),]],
["h_german_kettlehat_6_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_6_hood_custom"),add_mesh("@h_german_kettlehat_6"),]],
["h_german_kettlehat_7_hood_custom", "German Kettle Hat with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_7_hood_custom"),add_mesh("@h_german_kettlehat_7"),]],

# Cervelliere Base: 20; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_cervelliere_hood_custom", "Cervelliere with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
438 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_cervelliere_hood_custom"),add_mesh("@h_cervelliere"),]],

# Skullcap Base: 18; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_simple_cervelliere_hood_custom", "Cervelliere with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
292 , weight(1.75)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_skullcap_hood_custom"),add_mesh("@h_simple_cervelliere"),]],

["h_skullcap_hood_custom", "Skullcap with Hood", [("h_hood_square_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
292 , weight(1.75)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_skullcap_hood_custom"),add_mesh("@h_skullcap"),]],

### Seek: Don't put items between h_sallet_hood_custom and a_peasant_man_custom without editing the script



### Liripipe Hoods, also in a loop!
# Eyeslot Kettlehat Base: 30; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_eyeslot_kettlehat_1_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_1_liripipe_hood_custom"),add_mesh("@h_eyeslot_kettlehat_1"),]],
["h_eyeslot_kettlehat_1_liripipe_raised_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_1_liripipe_raised_hood_custom"),add_mesh("@h_eyeslot_kettlehat_1_raised"),]],

["h_eyeslot_kettlehat_2_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_2_liripipe_hood_custom"),add_mesh("@h_eyeslot_kettlehat_2"),]],
["h_eyeslot_kettlehat_2_liripipe_raised_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_2_liripipe_raised_hood_custom"),add_mesh("@h_eyeslot_kettlehat_2_raised"),]],

["h_eyeslot_kettlehat_3_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_eyeslot_kettlehat_3_liripipe_hood_custom"),add_mesh("@h_eyeslot_kettlehat_3"),]],

["h_oliphant_eyeslot_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_oliphant_eyeslot_liripipe_hood_custom"),add_mesh("@h_oliphant_eyeslot_kettlehat"),]],
["h_oliphant_eyeslot_raised_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_oliphant_eyeslot_raised_liripipe_hood_custom"),add_mesh("@h_oliphant_eyeslot_kettlehat_raised"),]],

["h_martinus_kettlehat_3_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_3_liripipe_hood_custom"),add_mesh("@h_martinus_kettlehat_3"),]],
["h_martinus_kettlehat_3_raised_liripipe_hood_custom", "Eyeslot Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_3_raised_liripipe_hood_custom"),add_mesh("@h_martinus_kettlehat_3_raised"),]],


# Oliphant Kettlehat Base: 28; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_oliphant_kettlehat_liripipe_hood_custom", "Oliphant Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_oliphant_kettlehat_liripipe_hood_custom"),add_mesh("@h_oliphant_kettlehat"),]],

# Martinus Kettlehat Base: 26; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_martinus_kettlehat_1_liripipe_hood_custom", "Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_1_liripipe_hood_custom"),add_mesh("@h_martinus_kettlehat_1"),]],
["h_martinus_kettlehat_2_liripipe_hood_custom", "Kettle Helmet with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_martinus_kettlehat_2_liripipe_hood_custom"),add_mesh("@h_martinus_kettlehat_2"),]],

# Chapel de Fer Base: 24; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_chapel_de_fer_liripipe_hood_custom", "Chapel de Fer with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
478 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_chapel_de_fer_liripipe_hood_custom"),add_mesh("@h_chapel_de_fer"),]],

# German Kettlehat Base: 24; Hood: 4,2; Padding: 6,4; mail collar: 8,6; mail aventail: 10,8; mail collar with bevor: 14,12;
["h_german_kettlehat_1_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_1_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_1"),]],
["h_german_kettlehat_2_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_2_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_2"),]],
["h_german_kettlehat_3_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_3_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_3"),]],
["h_german_kettlehat_4_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_4_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_4"),]],
["h_german_kettlehat_5_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_5_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_5"),]],
["h_german_kettlehat_6_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_6_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_6"),]],
["h_german_kettlehat_7_liripipe_hood_custom", "German Kettle Hat with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
400 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_german_kettlehat_7_liripipe_hood_custom"),add_mesh("@h_german_kettlehat_7"),]],

["h_simple_cervelliere_hood_liripipe_custom", "Cervelliere with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
292 , weight(1.75)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_skullcap_hood_liripipe_custom"),add_mesh("@h_simple_cervelliere"),]],

["h_skullcap_hood_liripipe_custom", "Skullcap with Liripipe Hood", [("h_hood_big_liripipe_half",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
292 , weight(1.75)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_skullcap_hood_liripipe_custom"),add_mesh("@h_skullcap"),]],

["h_hood_big_liripipe_full_custom", "Large Liripipe Hood", [("h_hood_big_liripipe_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
180 , weight(1.75)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[custom_reskin("itm_h_hood_big_liripipe_full_custom"),]],

["h_hood_square_liripipe_full_custom", "Liripipe Hood", [("h_hood_square_liripipe_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
160 , weight(1.75)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[custom_reskin("itm_h_hood_square_liripipe_full_custom"),]],

["h_hood_square_full_custom", "Hood", [("h_hood_square_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
160 , weight(1.75)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[custom_reskin("itm_h_hood_square_full_custom"),]],

["h_hood_big_liripipe_fancy_full_custom", "Fancy Large Liripipe Hood", [("h_hood_big_liripipe_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
180 , weight(1.75)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[custom_reskin("itm_h_hood_big_liripipe_fancy_full_custom"),]],

["h_hood_square_liripipe_fancy_full_custom", "Fancy Liripipe Hood", [("h_hood_square_liripipe_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
160 , weight(1.75)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[custom_reskin("itm_h_hood_square_liripipe_fancy_full_custom"),]],

["h_hood_square_fancy_full_custom", "Fancy Hood", [("h_hood_square_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 
160 , weight(1.75)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[custom_reskin("itm_h_hood_square_fancy_full_custom"),]],

### Armors
["a_peasant_man_custom", "Peasant Tunic", [("a_peasant_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_peasant_man_custom")]], 
["a_woman_common_dress_1_custom", "Dress", [("a_woman_common_dress_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_woman_common_dress_1_custom")]], 
["a_woman_common_dress_2_custom", "Dress", [("a_woman_common_dress_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_woman_common_dress_2_custom")]], 
["a_peasant_cote_custom", "Peasant Cote", [("a_peasant_cote",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_peasant_cote_custom")]], 
["a_peasant_cotehardie_custom", "Peasant Cotehardie", [("a_cotehardie",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_peasant_cotehardie_custom")]], 
["a_tailored_cotehardie_custom", "Tailored Cotehardie", [("a_cotehardie",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_tailored_cotehardie_custom")]], 
["a_hunter_coat_custom", "Pelt Coat", [("a_hunter_coat",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_hunter_coat_custom")]], 
["a_nobleman_court_outfit_custom", "Noble Outfit", [("a_nobleman_court_outfit_base",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_nobleman_court_outfit_custom")]], 

["h_peasant_bycocket_1_custom", "Peasant Bycocket", [("h_bycocket_1",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[custom_reskin("itm_h_peasant_bycocket_1_custom")]], 
["h_peasant_bycocket_2_custom", "Peasant Bycocket", [("h_bycocket_2",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[custom_reskin("itm_h_peasant_bycocket_2_custom")]], 

["h_bycocket_1_custom", "Tailored Bycocket", [("h_bycocket_1",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[custom_reskin("itm_h_bycocket_1_custom")]], 
["h_bycocket_2_custom", "Tailored Bycocket", [("h_bycocket_2",0)],itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[custom_reskin("itm_h_bycocket_2_custom")]], 


["a_light_gambeson_short_sleeves_custom", "Light Gambeson", [("a_light_gambeson_short_sleeves",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_short_sleeves_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_aketon_asher_sleeve_2", 0, 0),])]], 
["a_light_gambeson_short_sleeves_diamond_custom", "Light Gambeson", [("a_light_gambeson_short_sleeves",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_short_sleeves_diamond_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_aketon_asher_sleeve_2", 0, 0),])]], 

["a_light_gambeson_long_sleeves_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_custom")]], 
["a_light_gambeson_long_sleeves_diamond_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_diamond_custom")]],

["a_light_gambeson_long_sleeves_alt_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves_alt",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_alt_custom")]],

["a_light_gambeson_long_sleeves_3_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves_alt",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_3_custom")]],
["a_light_gambeson_long_sleeves_6_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves_alt",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_6_custom")]],

["a_light_gambeson_long_sleeves_8_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves_8",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_8_custom")]],
["a_light_gambeson_long_sleeves_8_alt_custom", "Light Gambeson", [("a_light_gambeson_long_sleeves_8",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_light_gambeson_long_sleeves_8_alt_custom")]],

["a_simple_gambeson_custom", "Gambeson", [("mesh_none",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_remodel("itm_a_simple_gambeson_custom")]],

["a_gambeson_asher_regular_custom", "Gambeson", [("mesh_none",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_remodel("itm_a_gambeson_asher_regular_custom")]],
["a_gambeson_asher_belt_custom", "Gambeson", [("mesh_none",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_remodel("itm_a_gambeson_asher_belt_custom")]],

### Seek: Beware of the code loops!
["a_padded_over_mail_1_custom", "Padded Armour", [("a_padded_over_mail_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_1_custom"),add_mesh("@a_pistoia_arming_cote_arms"),]], 
["a_padded_over_mail_2_custom", "Padded Armour", [("a_padded_over_mail_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_2_custom"),add_mesh("@a_pistoia_arming_cote_arms_short"),]], 
["a_padded_over_mail_3_custom", "Padded Over Mail", [("a_padded_over_mail_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_3_custom"),add_mesh("@a_pistoia_mail_arms"),]], 
["a_padded_over_mail_4_custom", "Padded Over Mail with Plate Arm Harness", [("a_padded_over_mail_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_4_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_2"),]], 
["a_padded_over_mail_5_custom", "Padded Over Mail with Plate Arm Harness", [("a_padded_over_mail_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_5_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_2"),]], 

["a_padded_over_mail_alt_1_custom", "Padded Armour", [("a_padded_over_mail_alt_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_alt_1_custom"),add_mesh("@a_pistoia_arming_cote_arms"),]], 
["a_padded_over_mail_alt_2_custom", "Padded Armour", [("a_padded_over_mail_alt_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_alt_2_custom"),add_mesh("@a_pistoia_arming_cote_arms_short"),]], 
["a_padded_over_mail_alt_3_custom", "Padded Over Mail", [("a_padded_over_mail_alt_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_alt_3_custom"),add_mesh("@a_pistoia_mail_arms"),]], 
["a_padded_over_mail_alt_4_custom", "Padded Over Mail with Plate Arm Harness", [("a_padded_over_mail_alt_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_alt_4_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_2"),]], 
["a_padded_over_mail_alt_5_custom", "Padded Over Mail with Plate Arm Harness", [("a_padded_over_mail_alt_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_alt_5_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_2"),]], 

["a_padded_over_mail_heavy_1_custom", "Heavy Gambeson", [("a_padded_over_mail_heavy_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_heavy_1_custom"),],], 
["a_padded_over_mail_heavy_2_custom", "Heavy Gambeson", [("a_padded_over_mail_heavy_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_heavy_2_custom"),],], 
["a_padded_over_mail_heavy_3_custom", "Heavy Gambeson", [("a_padded_over_mail_heavy_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_heavy_3_custom"),],], 
["a_padded_over_mail_heavy_4_custom", "Heavy Gambeson", [("a_padded_over_mail_heavy_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_heavy_4_custom"),],], 

["a_gambeson_crossbowman_custom", "Heavy Gambeson", [("a_gambeson_crossbowman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_gambeson_crossbowman_custom"),],], 
## Code Loop End
["a_gambeson_crossbowman_heavy_custom", "Crossbowman's Gambeson over Mail", [("a_gambeson_crossbowman_heavy",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_gambeson_crossbowman_heavy_custom"),],], 

["a_padded_jack_custom", "Padded Jack Over Mail", [("a_padded_jack",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_jack_custom"),]], 
["a_padded_jack_cross_custom", "Padded Jack Over Mail", [("a_padded_jack",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_jack_cross_custom"),]], 
["a_padded_jack_surcoat_custom", "Padded Jack Over Mail", [("a_padded_jack_surcoat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_jack_surcoat_custom")]], 


### Seek: Beware of the code loops!
["a_brigandine_asher_a_custom", "Brigandine Over Mail", [("a_brigandine_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(20)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_a_custom"),add_mesh("@a_pistoia_arming_cote_arms_short"),add_mesh("@a_pistoia_mail_arms_short"),],], 

["a_brigandine_asher_a_mail_custom", "Brigandine Over Mail", [("a_brigandine_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_a_mail_custom"),add_mesh("@a_pistoia_mail_arms"),],],
["a_brigandine_asher_a_mail_jackchain_custom", "Brigandine Over Mail with Jack Chains", [("a_brigandine_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_a_mail_custom"),add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),],],

["a_brigandine_asher_a_plate_1_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_a_plate_1_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_brigandine_asher_a_plate_2_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_a_plate_2_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_2"),add_mesh("@a_pistoia_spaulders"),],],
["a_brigandine_asher_a_plate_3_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_a_plate_3_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_3"),add_mesh("@a_pistoia_spaulders"),],],

["a_brigandine_asher_b_custom", "Brigandine Over Mail", [("a_brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(20)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_b_custom"),add_mesh("@a_pistoia_arming_cote_arms_short"),add_mesh("@a_pistoia_mail_arms_short"),],], 
                     
["a_brigandine_asher_b_mail_custom", "Brigandine Over Mail", [("a_brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_b_mail_custom"),add_mesh("@a_pistoia_mail_arms"),],],
["a_brigandine_asher_b_mail_jackchain_custom", "Brigandine Over Mail with Jack Chains", [("a_brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_b_mail_custom"),add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),],],
                     
["a_brigandine_asher_b_plate_1_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_b_plate_1_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_brigandine_asher_b_plate_2_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_b_plate_2_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_2"),add_mesh("@a_pistoia_spaulders"),],],
["a_brigandine_asher_b_plate_3_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_b_plate_3_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_3"),add_mesh("@a_pistoia_spaulders"),],],

["a_brigandine_asher_parti_custom", "Brigandine Over Mail", [("a_brigandine_parti",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(20)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_parti_custom"),add_mesh("@a_pistoia_arming_cote_arms_short"),add_mesh("@a_pistoia_mail_arms_short"),],], 
                     
["a_brigandine_asher_parti_mail_custom", "Brigandine Over Mail", [("a_brigandine_parti",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_parti_mail_custom"),add_mesh("@a_pistoia_mail_arms"),],],
["a_brigandine_asher_parti_mail_jackchain_custom", "Brigandine Over Mail with Jack Chains", [("a_brigandine_parti",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_parti_mail_custom"),add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_pistoia_jack_chains"),],],
                     
["a_brigandine_asher_parti_plate_1_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_parti",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_parti_plate_1_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_brigandine_asher_parti_plate_2_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_parti",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_parti_plate_2_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_2"),add_mesh("@a_pistoia_spaulders"),],],
["a_brigandine_asher_parti_plate_3_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_parti",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_parti_plate_3_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_3"),add_mesh("@a_pistoia_spaulders"),],],

### Seek: Beware of the code loops!
["a_brigandine_asher_custom", "Brigandine", [("a_brigandine_asher_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(20)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_custom"),add_mesh("@a_pistoia_arming_cote_arms"),],], 

["a_brigandine_asher_mail_custom", "Brigandine Over Mail", [("a_brigandine_asher_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_mail_custom"),add_mesh("@a_pistoia_mail_arms"),add_mesh("@a_mail_skirt_narf"),],],

["a_brigandine_asher_plate_1_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_asher_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_plate_1_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_mail_skirt_narf"),],],
["a_brigandine_asher_plate_2_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_asher_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_plate_2_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_2"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_mail_skirt_narf"),],],
["a_brigandine_asher_plate_3_custom", "Brigandine with Plate Arm Harness", [("a_brigandine_asher_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_asher_plate_3_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_3"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_mail_skirt_narf"),],],

["a_churburg_13_asher_plain_custom", "Churburg Plate", [("a_churburg_13_asher_base",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1460, weight(20)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(18)|difficulty(8), imodbits_armor , [custom_reskin("itm_a_churburg_13_asher_plain_custom"),],],
# End of loop
["a_churburg_13_asher_brass_custom", "Churburg Brass Plate", [("a_churburg_13_asher_base",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1680, weight(27)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(18)|difficulty(8), imodbits_armor , [custom_reskin("itm_a_churburg_13_asher_brass_custom"),],],

["a_corrazina_hohenaschau_mail_custom", "Hohenaschau Corrazina over Mail", [("a_corrazina_hohenaschau_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_corrazina_hohenaschau_mail_custom"),add_mesh("@a_pistoia_arming_cote_arms_short"),],],

["a_corrazina_hohenaschau_custom", "Hohenaschau Corrazina", [("a_corrazina_hohenaschau_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_corrazina_hohenaschau_custom"),add_mesh("@a_arm_harness_english_1415_b"),],],

["a_corrazina_spina_custom", "Corrazina", [("a_corrazina_spina_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_corrazina_spina_custom"),add_mesh("@a_arm_harness_english_1415_b"),],],

["a_corrazina_capwell_custom", "Corrazina", [("a_corrazina_capwell_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_corrazina_capwell_custom"),add_mesh("@a_arm_harness_english_1415_b"),],],

# Start of loop
["a_padded_over_plate_sleeved_1_custom", "Longsleeved Padded over Plate", [("a_padded_over_plate_sleeved_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_sleeved_1_custom"),],],
["a_padded_over_plate_sleeved_2_custom", "Longsleeved Padded over Plate", [("a_padded_over_plate_sleeved_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_sleeved_2_custom"),],],

["a_padded_over_plate_shortsleeved_1_custom", "Shortsleeved Padded over Plate", [("a_padded_over_plate_shortsleeved_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_shortsleeved_1_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),],],
["a_padded_over_plate_shortsleeved_2_custom", "Shortsleeved Padded over Plate", [("a_padded_over_plate_shortsleeved_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_shortsleeved_2_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),],],
["a_padded_over_plate_shortsleeved_3_custom", "Shortsleeved Padded over Plate", [("a_padded_over_plate_shortsleeved_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_shortsleeved_3_custom"),add_mesh("@a_pistoia_arming_cote_arms_plate_short"),add_mesh("@a_pistoia_couters_1"),],],

["a_padded_over_plate_sleeveless_1_custom", "Sleeveless Padded over Plate", [("a_padded_over_plate_sleeveless_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_sleeveless_1_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_padded_over_plate_sleeveless_2_custom", "Sleeveless Padded over Plate", [("a_padded_over_plate_sleeveless_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_sleeveless_2_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_padded_over_plate_sleeveless_3_custom", "Sleeveless Padded over Plate", [("a_padded_over_plate_sleeveless_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_sleeveless_3_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],
["a_padded_over_plate_sleeveless_4_custom", "Sleeveless Padded over Plate", [("a_padded_over_plate_sleeveless_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_padded_over_plate_sleeveless_4_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_couters_1"),add_mesh("@a_pistoia_spaulders"),],],

["a_plate_german_covered_fauld_custom", "German Plate with Covered Fauld", [("a_plate_german_covered_fauld",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5400, weight(28)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(9), imodbits_plate  ,[custom_reskin("itm_a_plate_german_covered_fauld_custom"),add_mesh("@a_arm_harness_english_1415_b"),],], 
# End of loop
["h_hood_custom", "Hood", [("mesh_none",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[custom_remodel("itm_h_hood_custom")]], 
["h_hood_fi_custom", "Hood", [("mesh_none",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[custom_remodel("itm_h_hood_fi_custom")]], 

### Giornea over Plate
# Start of loop
["a_giornea_over_plate_a_custom", "Giornea over Plate Armour", [("mesh_none",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[custom_remodel("itm_a_giornea_over_plate_a_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_1"),]],
["a_giornea_over_plate_b_custom", "Giornea over Plate Armour", [("mesh_none",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[custom_remodel("itm_a_giornea_over_plate_a_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_2"),]],
["a_giornea_over_plate_c_custom", "Giornea over Plate Armour", [("mesh_none",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[custom_remodel("itm_a_giornea_over_plate_a_custom"),add_mesh("@a_pistoia_mail_arms_light"),add_mesh("@a_pistoia_spaulders"),add_mesh("@a_pistoia_couters_3"),]],

##diplomacy begin
["dplmc_coat_of_plates_red_constable", "Constable Coat of Plates", [("a_churburg_13_asher_base",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], []],
# End of Loop
##diplomacy end

 
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW SWORDS | DAGGERS | GREATSWORDS ########################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# Daggers
["w_dagger_baselard", "Baselard Dagger", 
[("w_regular_dagger_baselard",0),("w_rusty_dagger_baselard",imodbit_rusty),("w_masterwork_dagger_baselard",imodbit_masterwork),
("w_regular_dagger_baselard_scabbard", ixmesh_carry),("w_rusty_dagger_baselard_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_dagger_baselard_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_secondary|itp_has_upper_stab, itc_dagger_new|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
99 , weight(0.5)|difficulty(0)|spd_rtng(104) | weapon_length(48)|swing_damage(24 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_alt ],
["w_dagger_bollock", "Bollock Dagger", 
[("w_regular_dagger_bollock",0),("w_rusty_dagger_bollock",imodbit_rusty),("w_masterwork_dagger_bollock",imodbit_masterwork),
("w_regular_dagger_bollock_scabbard", ixmesh_carry),("w_rusty_dagger_bollock_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_dagger_bollock_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_secondary|itp_has_upper_stab, itc_dagger_new|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
73 , weight(0.5)|difficulty(0)|spd_rtng(105) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],
["w_dagger_italian", "Italian Dagger", 
[("w_regular_dagger_italian",0),("w_rusty_dagger_italian",imodbit_rusty),("w_masterwork_dagger_italian",imodbit_masterwork),
("w_regular_dagger_italian_scabbard", ixmesh_carry),("w_rusty_dagger_italian_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_dagger_italian_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_secondary|itp_has_upper_stab, itc_dagger_new|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
136 , weight(0.6)|difficulty(0)|spd_rtng(105) | weapon_length(45)|swing_damage(25 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_alt ],
["w_dagger_pikeman", "Pikeman Dagger", 
[("w_regular_dagger_pikeman",0),("w_rusty_dagger_pikeman",imodbit_rusty),("w_masterwork_dagger_pikeman",imodbit_masterwork),
("w_regular_dagger_pikeman_scabbard", ixmesh_carry),("w_rusty_dagger_pikeman_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_dagger_pikeman_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_secondary|itp_has_upper_stab, itc_dagger_new|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
122 , weight(0.7)|difficulty(0)|spd_rtng(108) | weapon_length(41)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_alt ],
["w_dagger_quillon", "Quillon Dagger", 
[("w_regular_dagger_quillon",0),("w_rusty_dagger_quillon",imodbit_rusty),("w_masterwork_dagger_quillon",imodbit_masterwork),
("w_regular_dagger_quillon_scabbard", ixmesh_carry),("w_rusty_dagger_quillon_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_dagger_quillon_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_secondary|itp_has_upper_stab, itc_dagger_new|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
122 , weight(0.7)|difficulty(0)|spd_rtng(108) | weapon_length(42)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_alt ],
["w_dagger_rondel", "Rondel Dagger", 
[("w_regular_dagger_rondel",0),("w_rusty_dagger_rondel",imodbit_rusty),("w_masterwork_dagger_rondel",imodbit_masterwork),
("w_regular_dagger_rondel_scabbard", ixmesh_carry),("w_rusty_dagger_rondel_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_dagger_rondel_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_secondary|itp_has_upper_stab, itc_dagger_new|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
122 , weight(0.7)|difficulty(0)|spd_rtng(108) | weapon_length(43)|swing_damage(20 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_alt ],

# Albion Onehanded Swords
["w_onehanded_falchion_italian", "Italian Falchion", 
[("w_regular_onehanded_falchion_italian",0),("w_rusty_onehanded_falchion_italian",imodbit_rusty),("w_masterwork_onehanded_falchion_italian",imodbit_masterwork),
("w_regular_onehanded_falchion_italian_scabbard", ixmesh_carry),("w_rusty_onehanded_falchion_italian_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_falchion_italian_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
325 , weight(1.2)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_flemish", "Flemish Arming Sword", 
[("w_regular_onehanded_sword_flemish",0),("w_rusty_onehanded_sword_flemish",imodbit_rusty),("w_masterwork_onehanded_sword_flemish",imodbit_masterwork),
("w_regular_onehanded_sword_flemish_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_flemish_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_flemish_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
582 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(28 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_italian", "Italian Arming Sword", 
[("w_regular_onehanded_sword_italian",0),("w_rusty_onehanded_sword_italian",imodbit_rusty),("w_masterwork_onehanded_sword_italian",imodbit_masterwork),
("w_regular_onehanded_sword_italian_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_italian_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_italian_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
506 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(98)|swing_damage(32 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_alt ],

# ["w_onehanded_sword_irish", "Irish Arming Sword", 
# [("w_regular_onehanded_sword_irish",0),("w_rusty_onehanded_sword_irish",imodbit_rusty),("w_masterwork_onehanded_sword_irish",imodbit_masterwork),
# ("w_regular_onehanded_sword_irish_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_irish_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_irish_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 670 , weight(1.6)|difficulty(0)|spd_rtng(97) | weapon_length(107)|swing_damage(28 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_longbowman", "Longbowman Side Sword", 
[("w_regular_onehanded_sword_longbowman",0),("w_rusty_onehanded_sword_longbowman",imodbit_rusty),("w_masterwork_onehanded_sword_longbowman",imodbit_masterwork),
("w_regular_onehanded_sword_longbowman_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_longbowman_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_longbowman_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(83)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_messer", "Lange Messer", 
[("w_regular_onehanded_sword_messer",0),("w_rusty_onehanded_sword_messer",imodbit_rusty),("w_masterwork_onehanded_sword_messer",imodbit_masterwork),
("w_regular_onehanded_sword_messer_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_messer_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_messer_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
415 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(36 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_milanese", "Milanese Short Arming Sword", 
[("w_regular_onehanded_sword_milanese",0),("w_rusty_onehanded_sword_milanese",imodbit_rusty),("w_masterwork_onehanded_sword_milanese",imodbit_masterwork),
("w_regular_onehanded_sword_milanese_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_milanese_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_milanese_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
402 , weight(1.3)|difficulty(0)|spd_rtng(103) | weapon_length(74)|swing_damage(28 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_scottish", "Scottish Short Arming Sword", 
[("w_regular_onehanded_sword_scottish",0),("w_rusty_onehanded_sword_scottish",imodbit_rusty),("w_masterwork_onehanded_sword_scottish",imodbit_masterwork),
("w_regular_onehanded_sword_scottish_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_scottish_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_scottish_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(81)|swing_damage(26 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],

["w_onehanded_falchion_peasant", "Peasant Falchion", 
[("w_regular_onehanded_falchion_peasant",0),("w_rusty_onehanded_falchion_peasant",imodbit_rusty),("w_masterwork_onehanded_falchion_peasant",imodbit_masterwork),
("w_regular_onehanded_falchion_peasant_scabbard", ixmesh_carry),("w_rusty_onehanded_falchion_peasant_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_falchion_peasant_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
252 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(76)|swing_damage(31 , cut),imodbits_sword_alt ],

["w_onehanded_falchion_peasant_b", "Peasant Falchion", 
[("w_regular_onehanded_falchion_peasant_b",0),("w_rusty_onehanded_falchion_peasant_b",imodbit_rusty),("w_masterwork_onehanded_falchion_peasant_b",imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_scimitar|itcf_carry_sword_left_hip, 
234 , weight(1.3)|difficulty(0)|spd_rtng(98) | weapon_length(61)|swing_damage(33 , cut),imodbits_sword_alt ],

["w_onehanded_falchion_a", "Falchion", 
[("w_regular_onehanded_falchion_a",0),("w_rusty_onehanded_falchion_a",imodbit_rusty),("w_masterwork_onehanded_falchion_a",imodbit_masterwork),
("w_regular_onehanded_falchion_a_scabbard", ixmesh_carry),("w_rusty_onehanded_falchion_a_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_falchion_a_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
555 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(88)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_alt ],

["w_onehanded_falchion_b", "Falchion", 
[("w_regular_onehanded_falchion_b",0),("w_rusty_onehanded_falchion_b",imodbit_rusty),("w_masterwork_onehanded_falchion_b",imodbit_masterwork),
("w_regular_onehanded_falchion_b_scabbard", ixmesh_carry),("w_rusty_onehanded_falchion_b_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_falchion_b_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
555 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(88)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_alt ],

# Native Onehanded
["w_onehanded_sword_a", "Arming Sword", 
[("w_regular_onehanded_sword_a",0),("w_rusty_onehanded_sword_a",imodbit_rusty),("w_masterwork_onehanded_sword_a",imodbit_masterwork),
("w_regular_onehanded_sword_a_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_a_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_a_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
488 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_a_long", "Long Arming Sword", 
[("w_regular_onehanded_sword_a_long",0),("w_rusty_onehanded_sword_a_long",imodbit_rusty),("w_masterwork_onehanded_sword_a_long",imodbit_masterwork),
("w_regular_onehanded_sword_a_long_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_a_long_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_a_long_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
572 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(101)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_c", "Arming Sword", 
[("w_regular_onehanded_sword_c",0),("w_rusty_onehanded_sword_c",imodbit_rusty),("w_masterwork_onehanded_sword_c",imodbit_masterwork),
("w_regular_onehanded_sword_c_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_c_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_c_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
400 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_c_long", "Long Arming Sword", 
[("w_regular_onehanded_sword_c_long",0),("w_rusty_onehanded_sword_c_long",imodbit_rusty),("w_masterwork_onehanded_sword_c_long",imodbit_masterwork),
("w_regular_onehanded_sword_c_long_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_c_long_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_c_long_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
572 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(101)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_c_small", "Short Arming Sword", 
[("w_regular_onehanded_sword_c_small",0),("w_rusty_onehanded_sword_c_small",imodbit_rusty),("w_masterwork_onehanded_sword_c_small",imodbit_masterwork),
("w_regular_onehanded_sword_c_small_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_c_small_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_c_small_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
533 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_d", "Arming Sword", 
[("w_regular_onehanded_sword_d",0),("w_rusty_onehanded_sword_d",imodbit_rusty),("w_masterwork_onehanded_sword_d",imodbit_masterwork),
("w_regular_onehanded_sword_d_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_d_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_d_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
496 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(27 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_d_long", "Long Arming Sword", 
[("w_regular_onehanded_sword_d_long",0),("w_rusty_onehanded_sword_d_long",imodbit_rusty),("w_masterwork_onehanded_sword_d_long",imodbit_masterwork),
("w_regular_onehanded_sword_d_long_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_d_long_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_d_long_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
594 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(107)|swing_damage(28 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],



["w_onehanded_sword_monarch", "Monarch Arming Sword", 
[("w_regular_onehanded_sword_monarch",0),("w_rusty_onehanded_sword_monarch",imodbit_rusty),("w_masterwork_onehanded_sword_monarch",imodbit_masterwork),
("w_regular_onehanded_sword_monarch_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_monarch_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_monarch_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
487 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(94)|swing_damage(26 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_caithness", "Caithness Arming Sword", 
[("w_regular_onehanded_sword_caithness",0),("w_rusty_onehanded_sword_caithness",imodbit_rusty),("w_masterwork_onehanded_sword_caithness",imodbit_masterwork),
("w_regular_onehanded_sword_caithness_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_caithness_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_caithness_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
582 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_defiant", "Defiant Arming Sword", 
[("w_regular_onehanded_sword_defiant",0),("w_rusty_onehanded_sword_defiant",imodbit_rusty),("w_masterwork_onehanded_sword_defiant",imodbit_masterwork),
("w_regular_onehanded_sword_defiant_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_defiant_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_defiant_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
577 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(27 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_knight", "Knight Arming Sword", 
[("w_regular_onehanded_sword_knight",0),("w_rusty_onehanded_sword_knight",imodbit_rusty),("w_masterwork_onehanded_sword_knight",imodbit_masterwork),
("w_regular_onehanded_sword_knight_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_knight_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_knight_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
491 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(29 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_laird", "Laird Arming Sword", 
[("w_regular_onehanded_sword_laird",0),("w_rusty_onehanded_sword_laird",imodbit_rusty),("w_masterwork_onehanded_sword_laird",imodbit_masterwork),
("w_regular_onehanded_sword_laird_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_laird_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_laird_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
491 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_poitiers", "Poitiers Arming Sword", 
[("w_regular_onehanded_sword_poitiers",0),("w_rusty_onehanded_sword_poitiers",imodbit_rusty),("w_masterwork_onehanded_sword_poitiers",imodbit_masterwork),
("w_regular_onehanded_sword_poitiers_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_poitiers_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_poitiers_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
497 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(92)|swing_damage(27 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_prince", "Prince Arming Sword", 
[("w_regular_onehanded_sword_prince",0),("w_rusty_onehanded_sword_prince",imodbit_rusty),("w_masterwork_onehanded_sword_prince",imodbit_masterwork),
("w_regular_onehanded_sword_prince_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_prince_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_prince_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
505 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(96)|swing_damage(31 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_forsaken", "Forsaken Arming Sword", 
[("w_regular_onehanded_sword_forsaken",0),("w_rusty_onehanded_sword_forsaken",imodbit_rusty),("w_masterwork_onehanded_sword_forsaken",imodbit_masterwork),
("w_regular_onehanded_sword_forsaken_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_forsaken_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_forsaken_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
570 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_sovereign", "Sovereign Short Arming Sword", 
[("w_regular_onehanded_sword_sovereign",0),("w_rusty_onehanded_sword_sovereign",imodbit_rusty),("w_masterwork_onehanded_sword_sovereign",imodbit_masterwork),
("w_regular_onehanded_sword_sovereign_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_sovereign_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_sovereign_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(83)|swing_damage(32 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_squire", "Squire Arming Sword", 
[("w_regular_onehanded_sword_squire",0),("w_rusty_onehanded_sword_squire",imodbit_rusty),("w_masterwork_onehanded_sword_squire",imodbit_masterwork),
("w_regular_onehanded_sword_squire_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_squire_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_squire_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_alt ],

["w_onehanded_sword_martyr", "Martyr Arming Sword", 
[("w_regular_onehanded_sword_martyr",0),("w_rusty_onehanded_sword_martyr",imodbit_rusty),("w_masterwork_onehanded_sword_martyr",imodbit_masterwork),
("w_regular_onehanded_sword_martyr_scabbard", ixmesh_carry),("w_rusty_onehanded_sword_martyr_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_onehanded_sword_martyr_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
577 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_alt ],

# Bastard Swords with Scabbards
["w_bastard_sword_a", "Bastard Sword", 
[("w_regular_bastard_sword_a",0),("w_rusty_bastard_sword_a",imodbit_rusty),("w_masterwork_bastard_sword_a",imodbit_masterwork),
("w_regular_bastard_sword_a_scabbard", ixmesh_carry),("w_rusty_bastard_sword_a_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_a_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
294, weight(2.0)|difficulty(9)|spd_rtng(98)|weapon_length(99)|swing_damage(35,cut)|thrust_damage(26,pierce), imodbits_sword_alt ],

["w_bastard_sword_b", "Bastard Sword", 
[("w_regular_bastard_sword_b",0),("w_rusty_bastard_sword_b",imodbit_rusty),("w_masterwork_bastard_sword_b",imodbit_masterwork),
("w_regular_bastard_sword_b_scabbard", ixmesh_carry),("w_rusty_bastard_sword_b_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_b_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
526, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(104)|swing_damage(37,cut)|thrust_damage(27,pierce), imodbits_sword_alt ],

["w_bastard_sword_c", "Bastard Sword", 
[("w_regular_bastard_sword_c",0),("w_rusty_bastard_sword_c",imodbit_rusty),("w_masterwork_bastard_sword_c",imodbit_masterwork),
("w_regular_bastard_sword_c_scabbard", ixmesh_carry),("w_rusty_bastard_sword_c_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_c_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
548, weight(2.5)|difficulty(9)|spd_rtng(97)|weapon_length(104)|swing_damage(38,cut)|thrust_damage(27,pierce), imodbits_sword_alt ],

["w_bastard_sword_d", "Bastard Sword", 
[("w_regular_bastard_sword_d",0),("w_rusty_bastard_sword_d",imodbit_rusty),("w_masterwork_bastard_sword_d",imodbit_masterwork),
("w_regular_bastard_sword_d_scabbard", ixmesh_carry),("w_rusty_bastard_sword_d_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_d_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
698, weight(2.25)|difficulty(9)|spd_rtng(98)|weapon_length(99)|swing_damage(38,cut)|thrust_damage(31,pierce), imodbits_sword_alt ],

["w_bastard_sword_english", "English Bastard Sword", 
[("w_regular_bastard_sword_english",0),("w_rusty_bastard_sword_english",imodbit_rusty),("w_masterwork_bastard_sword_english",imodbit_masterwork),
("w_regular_bastard_sword_english_scabbard", ixmesh_carry),("w_rusty_bastard_sword_english_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_english_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
676, weight(2)|difficulty(9)|spd_rtng(99)|weapon_length(101)|swing_damage(37,cut)|thrust_damage(33,pierce), imodbits_sword_alt ],

["w_bastard_sword_german", "German Bastard Sword", 
[("w_regular_bastard_sword_german",0),("w_rusty_bastard_sword_german",imodbit_rusty),("w_masterwork_bastard_sword_german",imodbit_masterwork),
("w_regular_bastard_sword_german_scabbard", ixmesh_carry),("w_rusty_bastard_sword_german_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_german_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
724, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(106)|swing_damage(38,cut)|thrust_damage(33,pierce), imodbits_sword_alt ],

["w_bastard_sword_italian", "Italian Bastard Sword", 
[("w_regular_bastard_sword_italian",0),("w_rusty_bastard_sword_italian",imodbit_rusty),("w_masterwork_bastard_sword_italian",imodbit_masterwork),
("w_regular_bastard_sword_italian_scabbard", ixmesh_carry),("w_rusty_bastard_sword_italian_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_italian_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
638, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(107)|swing_damage(36,cut)|thrust_damage(35,pierce), imodbits_sword_alt ],


["w_bastard_sword_agincourt", "Agincourt Bastard Sword", 
[("w_regular_bastard_sword_agincourt",0),("w_rusty_bastard_sword_agincourt",imodbit_rusty),("w_masterwork_bastard_sword_agincourt",imodbit_masterwork),
("w_regular_bastard_sword_agincourt_scabbard", ixmesh_carry),("w_rusty_bastard_sword_agincourt_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_agincourt_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
892, weight(2.75)|difficulty(9)|spd_rtng(96)|weapon_length(111)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_sword_alt ],

["w_bastard_sword_baron", "Baron Bastard Sword", 
[("w_regular_bastard_sword_baron",0),("w_rusty_bastard_sword_baron",imodbit_rusty),("w_masterwork_bastard_sword_baron",imodbit_masterwork),
("w_regular_bastard_sword_baron_scabbard", ixmesh_carry),("w_rusty_bastard_sword_baron_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_baron_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
831, weight(2.5)|difficulty(9)|spd_rtng(96)|weapon_length(110)|swing_damage(41,cut)|thrust_damage(30,pierce), imodbits_sword_alt ],

["w_bastard_sword_castellan", "Castelan Bastard Sword", 
[("w_regular_bastard_sword_castellan",0),("w_rusty_bastard_sword_castellan",imodbit_rusty),("w_masterwork_bastard_sword_castellan",imodbit_masterwork),
("w_regular_bastard_sword_castellan_scabbard", ixmesh_carry),("w_rusty_bastard_sword_castellan_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_castellan_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
808 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(36 ,  pierce),imodbits_sword_alt ],

["w_bastard_sword_constable", "Constable Bastard Sword", 
[("w_regular_bastard_sword_constable",0),("w_rusty_bastard_sword_constable",imodbit_rusty),("w_masterwork_bastard_sword_constable",imodbit_masterwork),
("w_regular_bastard_sword_constable_scabbard", ixmesh_carry),("w_rusty_bastard_sword_constable_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_constable_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
814 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(99)|swing_damage(31 , cut) | thrust_damage(36 ,  pierce),imodbits_sword_alt ],

["w_bastard_sword_count", "Count Bastard Sword", 
[("w_regular_bastard_sword_count",0),("w_rusty_bastard_sword_count",imodbit_rusty),("w_masterwork_bastard_sword_count",imodbit_masterwork),
("w_regular_bastard_sword_count_scabbard", ixmesh_carry),("w_rusty_bastard_sword_count_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_count_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
784, weight(2)|difficulty(9)|spd_rtng(98)|weapon_length(100)|swing_damage(40,cut)|thrust_damage(29,pierce), imodbits_sword_alt ],

["w_bastard_sword_crecy", "Crecy Bastard Sword", 
[("w_regular_bastard_sword_crecy",0),("w_rusty_bastard_sword_crecy",imodbit_rusty),("w_masterwork_bastard_sword_crecy",imodbit_masterwork),
("w_regular_bastard_sword_crecy_scabbard", ixmesh_carry),("w_rusty_bastard_sword_crecy_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_crecy_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
938, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(107)|swing_damage(40,cut)|thrust_damage(34,pierce), imodbits_sword_alt ],

["w_bastard_sword_duke", "Duke Bastard Sword", 
[("w_regular_bastard_sword_duke",0),("w_rusty_bastard_sword_duke",imodbit_rusty),("w_masterwork_bastard_sword_duke",imodbit_masterwork),
("w_regular_bastard_sword_duke_scabbard", ixmesh_carry),("w_rusty_bastard_sword_duke_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_duke_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
822, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(106)|swing_damage(42,cut)|thrust_damage(26,pierce), imodbits_sword_alt ],

["w_bastard_sword_landgraf", "Landgraf Bastard Sword", 
[("w_regular_bastard_sword_landgraf",0),("w_rusty_bastard_sword_landgraf",imodbit_rusty),("w_masterwork_bastard_sword_landgraf",imodbit_masterwork),
("w_regular_bastard_sword_landgraf_scabbard", ixmesh_carry),("w_rusty_bastard_sword_landgraf_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_landgraf_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
798, weight(2.2)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(37,cut)|thrust_damage(34,pierce), imodbits_sword_alt ],

["w_bastard_sword_mercenary", "Mercenary Bastard Sword", 
[("w_regular_bastard_sword_mercenary",0),("w_rusty_bastard_sword_mercenary",imodbit_rusty),("w_masterwork_bastard_sword_mercenary",imodbit_masterwork),
("w_regular_bastard_sword_mercenary_scabbard", ixmesh_carry),("w_rusty_bastard_sword_mercenary_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_mercenary_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
760, weight(2)|difficulty(9)|spd_rtng(98)|weapon_length(101)|swing_damage(36,cut)|thrust_damage(33,pierce), imodbits_sword_alt ],

["w_bastard_sword_regent", "Regent Bastard Sword", 
[("w_regular_bastard_sword_regent",0),("w_rusty_bastard_sword_regent",imodbit_rusty),("w_masterwork_bastard_sword_regent",imodbit_masterwork),
("w_regular_bastard_sword_regent_scabbard", ixmesh_carry),("w_rusty_bastard_sword_regent_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_regent_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
885, weight(2.25)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(39,cut)|thrust_damage(34,pierce), imodbits_sword_alt ],

["w_bastard_sword_sempach", "Sempach Bastard Sword", 
[("w_regular_bastard_sword_sempach",0),("w_rusty_bastard_sword_sempach",imodbit_rusty),("w_masterwork_bastard_sword_sempach",imodbit_masterwork),
("w_regular_bastard_sword_sempach_scabbard", ixmesh_carry),("w_rusty_bastard_sword_sempach_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_sword_sempach_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
873, weight(2.25)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(38,cut)|thrust_damage(35,pierce), imodbits_sword_alt ],

["w_bastard_falchion", "Hand-and-a-half Falchion", 
[("w_regular_bastard_falchion",0),("w_rusty_bastard_falchion",imodbit_rusty),("w_masterwork_bastard_falchion",imodbit_masterwork),
("w_regular_bastard_falchion_scabbard", ixmesh_carry),("w_rusty_bastard_falchion_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_bastard_falchion_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
912, weight(2.1)|difficulty(10)|spd_rtng(97)|weapon_length(97)|swing_damage(43,cut)|thrust_damage(28,pierce), imodbits_sword_alt ],


################ Twohanded Swords
["w_twohanded_sword_messer", "Kriegsmesser", 
[("w_regular_twohanded_sword_messer",0),("w_rusty_twohanded_sword_messer",imodbit_rusty),("w_masterwork_twohanded_sword_messer",imodbit_masterwork),
("w_regular_twohanded_sword_messer_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_messer_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_messer_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
920 , weight(2.2)|difficulty(10)|spd_rtng(99) | weapon_length(93)|swing_damage(44 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_alt ],

["w_twohanded_sword_messer_b", "Kriegsmesser", 
[("w_regular_twohanded_sword_messer_b",0),("w_rusty_twohanded_sword_messer_b",imodbit_rusty),("w_masterwork_twohanded_sword_messer_b",imodbit_masterwork),
("w_regular_twohanded_sword_messer_b_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_messer_b_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_messer_b_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1166 , weight(2.5)|difficulty(11)|spd_rtng(97) | weapon_length(105)|swing_damage(45 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_alt ],

["w_twohanded_sword_claymore", "Claidheamh-Mòr", 
[("w_regular_twohanded_sword_claymore",0),("w_rusty_twohanded_sword_claymore",imodbit_rusty),("w_masterwork_twohanded_sword_claymore",imodbit_masterwork),
("w_regular_twohanded_sword_claymore_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_claymore_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_claymore_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1290 , weight(3.3)|difficulty(12)|spd_rtng(96) | weapon_length(108)|swing_damage(43 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_claymore_halfswording", "Claidheamh-Mòr", 
# [("w_regular_twohanded_sword_claymore",0),("w_rusty_twohanded_sword_claymore",imodbit_rusty),("w_masterwork_twohanded_sword_claymore",imodbit_masterwork),
# ("w_regular_twohanded_sword_claymore_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_claymore_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_claymore_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 1290 , weight(3.3)|difficulty(12)|spd_rtng(96) | weapon_length(108)|swing_damage(43 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_claymore_mordhau", "Claidheamh-Mòr", 
[("w_regular_twohanded_sword_claymore",0),("w_rusty_twohanded_sword_claymore",imodbit_rusty),("w_masterwork_twohanded_sword_claymore",imodbit_masterwork),
("w_regular_twohanded_sword_claymore_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_claymore_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_claymore_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1290 , weight(3.3)|difficulty(12)|spd_rtng(96) | weapon_length(108)|swing_damage(35 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

["w_twohanded_sword_claymore_b", "Claidheamh-Mòr", 
[("w_regular_twohanded_sword_claymore_b",0),("w_rusty_twohanded_sword_claymore_b",imodbit_rusty),("w_masterwork_twohanded_sword_claymore_b",imodbit_masterwork),
("w_regular_twohanded_sword_claymore_b_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_claymore_b_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_claymore_b_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1290 , weight(3.3)|difficulty(12)|spd_rtng(96) | weapon_length(108)|swing_damage(43 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_claymore_b_halfswording", "Claidheamh-Mòr", 
# [("w_regular_twohanded_sword_claymore_b",0),("w_rusty_twohanded_sword_claymore_b",imodbit_rusty),("w_masterwork_twohanded_sword_claymore_b",imodbit_masterwork),
# ("w_regular_twohanded_sword_claymore_b_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_claymore_b_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_claymore_b_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 1290 , weight(3.3)|difficulty(12)|spd_rtng(96) | weapon_length(108)|swing_damage(43 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_claymore_b_mordhau", "Claidheamh-Mòr", 
[("w_regular_twohanded_sword_claymore_b",0),("w_rusty_twohanded_sword_claymore_b",imodbit_rusty),("w_masterwork_twohanded_sword_claymore_b",imodbit_masterwork),
("w_regular_twohanded_sword_claymore_b_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_claymore_b_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_claymore_b_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1290 , weight(3.3)|difficulty(12)|spd_rtng(96) | weapon_length(108)|swing_damage(35 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

["w_twohanded_sword_danish", "Danish Greatsword", 
[("w_regular_twohanded_sword_danish",0),("w_rusty_twohanded_sword_danish",imodbit_rusty),("w_masterwork_twohanded_sword_danish",imodbit_masterwork),
("w_regular_twohanded_sword_danish_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_danish_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_danish_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1344 , weight(3.2)|difficulty(12)|spd_rtng(94) | weapon_length(114)|swing_damage(42 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_danish_halfswording", "Danish Greatsword", 
# [("w_regular_twohanded_sword_danish",0),("w_rusty_twohanded_sword_danish",imodbit_rusty),("w_masterwork_twohanded_sword_danish",imodbit_masterwork),
# ("w_regular_twohanded_sword_danish_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_danish_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_danish_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 1344 , weight(3.2)|difficulty(12)|spd_rtng(94) | weapon_length(114)|swing_damage(42 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_danish_mordhau", "Danish Greatsword", 
[("w_regular_twohanded_sword_danish",0),("w_rusty_twohanded_sword_danish",imodbit_rusty),("w_masterwork_twohanded_sword_danish",imodbit_masterwork),
("w_regular_twohanded_sword_danish_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_danish_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_danish_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1344 , weight(3.2)|difficulty(12)|spd_rtng(94) | weapon_length(114)|swing_damage(34 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

["w_twohanded_sword_steward", "Steward Greatsword", 
[("w_regular_twohanded_sword_steward",0),("w_rusty_twohanded_sword_steward",imodbit_rusty),("w_masterwork_twohanded_sword_steward",imodbit_masterwork),
("w_regular_twohanded_sword_steward_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_steward_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_steward_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1036 , weight(2.25)|difficulty(11)|spd_rtng(96) | weapon_length(99)|swing_damage(41 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_steward_halfswording", "Steward Greatsword", 
# [("w_regular_twohanded_sword_steward",0),("w_rusty_twohanded_sword_steward",imodbit_rusty),("w_masterwork_twohanded_sword_steward",imodbit_masterwork),
# ("w_regular_twohanded_sword_steward_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_steward_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_steward_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
# 1036 , weight(2.25)|difficulty(11)|spd_rtng(96) | weapon_length(99)|swing_damage(41 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_steward_mordhau", "Steward Greatsword", 
[("w_regular_twohanded_sword_steward",0),("w_rusty_twohanded_sword_steward",imodbit_rusty),("w_masterwork_twohanded_sword_steward",imodbit_masterwork),
("w_regular_twohanded_sword_steward_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_steward_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_steward_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1036 , weight(2.25)|difficulty(11)|spd_rtng(96) | weapon_length(99)|swing_damage(33 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

["w_twohanded_sword_talhoffer", "Talhoffer Greatsword", 
[("w_regular_twohanded_sword_talhoffer",0),("w_rusty_twohanded_sword_talhoffer",imodbit_rusty),("w_masterwork_twohanded_sword_talhoffer",imodbit_masterwork),
("w_regular_twohanded_sword_talhoffer_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_talhoffer_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_talhoffer_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
998 , weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(115)|swing_damage(40 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_talhoffer_halfswording", "Talhoffer Greatsword", 
# [("w_regular_twohanded_sword_talhoffer",0),("w_rusty_twohanded_sword_talhoffer",imodbit_rusty),("w_masterwork_twohanded_sword_talhoffer",imodbit_masterwork),
# ("w_regular_twohanded_sword_talhoffer_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_talhoffer_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_talhoffer_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
# 998 , weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(115)|swing_damage(40 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_talhoffer_mordhau", "Talhoffer Greatsword", 
[("w_regular_twohanded_sword_talhoffer",0),("w_rusty_twohanded_sword_talhoffer",imodbit_rusty),("w_masterwork_twohanded_sword_talhoffer",imodbit_masterwork),
("w_regular_twohanded_sword_talhoffer_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_talhoffer_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_talhoffer_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
998 , weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(115)|swing_damage(32 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

["w_twohanded_sword_munich", "Munich Greatsword", 
[("w_regular_twohanded_sword_munich",0),("w_rusty_twohanded_sword_munich",imodbit_rusty),("w_masterwork_twohanded_sword_munich",imodbit_masterwork),
("w_regular_twohanded_sword_munich_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_munich_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_munich_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1468 , weight(2.7)|difficulty(12)|spd_rtng(92) | weapon_length(123)|swing_damage(41 , cut) | thrust_damage(36 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_munich_halfswording", "Munich Greatsword", 
# [("w_regular_twohanded_sword_munich",0),("w_rusty_twohanded_sword_munich",imodbit_rusty),("w_masterwork_twohanded_sword_munich",imodbit_masterwork),
# ("w_regular_twohanded_sword_munich_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_munich_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_munich_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
# 1468 , weight(2.7)|difficulty(12)|spd_rtng(92) | weapon_length(123)|swing_damage(41 , cut) | thrust_damage(36 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_munich_mordhau", "Munich Greatsword", 
[("w_regular_twohanded_sword_munich",0),("w_rusty_twohanded_sword_munich",imodbit_rusty),("w_masterwork_twohanded_sword_munich",imodbit_masterwork),
("w_regular_twohanded_sword_munich_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_munich_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_munich_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1468 , weight(2.7)|difficulty(12)|spd_rtng(92) | weapon_length(123)|swing_damage(31 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

["w_twohanded_sword_earl", "Earl Greatsword", 
[("w_regular_twohanded_sword_earl",0),("w_rusty_twohanded_sword_earl",imodbit_rusty),("w_masterwork_twohanded_sword_earl",imodbit_masterwork),
("w_regular_twohanded_sword_earl_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_earl_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_earl_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab|itp_next_item_as_melee, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1274 , weight(2.4)|difficulty(11)|spd_rtng(94) | weapon_length(111)|swing_damage(42 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_alt ],
# ["w_twohanded_sword_earl_halfswording", "Earl Greatsword", 
# [("w_regular_twohanded_sword_earl",0),("w_rusty_twohanded_sword_earl",imodbit_rusty),("w_masterwork_twohanded_sword_earl",imodbit_masterwork),
# ("w_regular_twohanded_sword_earl_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_earl_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_earl_scabbard", ixmesh_carry|imodbit_masterwork),], 
# itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_has_upper_stab, itc_halfswording|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
# 1274 , weight(2.4)|difficulty(11)|spd_rtng(94) | weapon_length(111)|swing_damage(42 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_alt ],
["w_twohanded_sword_earl_mordhau", "Earl Greatsword", 
[("w_regular_twohanded_sword_earl",0),("w_rusty_twohanded_sword_earl",imodbit_rusty),("w_masterwork_twohanded_sword_earl",imodbit_masterwork),
("w_regular_twohanded_sword_earl_scabbard", ixmesh_carry),("w_rusty_twohanded_sword_earl_scabbard", ixmesh_carry|imodbit_rusty),("w_masterwork_twohanded_sword_earl_scabbard", ixmesh_carry|imodbit_masterwork),], 
itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_no_blur|itp_offset_musket, itc_voulge|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1274 , weight(2.4)|difficulty(11)|spd_rtng(94) | weapon_length(111)|swing_damage(32 , blunt),imodbits_sword_alt, [], [fac_no_faction] ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW AXES | BARDICHES ######################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_archer_hatchet", "Archer Hatchet", [("w_archer_hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
71 , weight(1.25)|difficulty(7)|spd_rtng(98) | weapon_length(46)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_archer_hatchet_brown", "Archer Hatchet", [("w_archer_hatchet_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
71 , weight(1.25)|difficulty(7)|spd_rtng(98) | weapon_length(46)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_archer_hatchet_red", "Archer Hatchet", [("w_archer_hatchet_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
71 , weight(1.25)|difficulty(7)|spd_rtng(98) | weapon_length(46)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

### War Axes

["w_onehanded_war_axe_01", "Onehanded War Axe", [("w_onehanded_war_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
221 , weight(1.5)|difficulty(9)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_01_brown", "Onehanded War Axe", [("w_onehanded_war_axe_01_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
221 , weight(1.5)|difficulty(9)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_01_red", "Onehanded War Axe", [("w_onehanded_war_axe_01_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
221 , weight(1.5)|difficulty(9)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_onehanded_war_axe_02", "Onehanded War Axe", [("w_onehanded_war_axe_02",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
87 , weight(1.5)|difficulty(9)|spd_rtng(96) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_02_brown", "Onehanded War Axe", [("w_onehanded_war_axe_02_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
87 , weight(1.5)|difficulty(9)|spd_rtng(96) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_02_red", "Onehanded War Axe", [("w_onehanded_war_axe_02_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
87 , weight(1.5)|difficulty(9)|spd_rtng(96) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_onehanded_war_axe_03", "Onehanded War Axe", [("w_onehanded_war_axe_03",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
142 , weight(2)|difficulty(9)|spd_rtng(95) | weapon_length(71)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_03_brown", "Onehanded War Axe", [("w_onehanded_war_axe_03_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
142 , weight(2)|difficulty(9)|spd_rtng(95) | weapon_length(71)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_03_red", "Onehanded War Axe", [("w_onehanded_war_axe_03_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
142 , weight(2)|difficulty(9)|spd_rtng(95) | weapon_length(71)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_onehanded_war_axe_04", "Onehanded War Axe", [("w_onehanded_war_axe_04",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
190 , weight(1.75)|difficulty(9)|spd_rtng(96) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_04_brown", "Onehanded War Axe", [("w_onehanded_war_axe_04_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
190 , weight(1.75)|difficulty(9)|spd_rtng(96) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_04_red", "Onehanded War Axe", [("w_onehanded_war_axe_04_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
190 , weight(1.75)|difficulty(9)|spd_rtng(96) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

### Horsemen axes

["w_onehanded_horseman_axe_01", "Horseman Axe", [("w_onehanded_horseman_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_01_alt", "Horseman Axe", [("w_onehanded_horseman_axe_01_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_horseman_axe_01_brown", "Horseman Axe", [("w_onehanded_horseman_axe_01_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_01_alt_brown", "Horseman Axe", [("w_onehanded_horseman_axe_01_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_horseman_axe_01_red", "Horseman Axe", [("w_onehanded_horseman_axe_01_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_01_alt_red", "Horseman Axe", [("w_onehanded_horseman_axe_01_alt_red",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_onehanded_horseman_axe_02", "Horseman Axe", [("w_onehanded_horseman_axe_02",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_02_alt", "Horseman Axe", [("w_onehanded_horseman_axe_02_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_horseman_axe_02_brown", "Horseman Axe", [("w_onehanded_horseman_axe_02_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_02_alt_brown", "Horseman Axe", [("w_onehanded_horseman_axe_02_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_horseman_axe_02_red", "Horseman Axe", [("w_onehanded_horseman_axe_02_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_02_alt_red", "Horseman Axe", [("w_onehanded_horseman_axe_02_alt_red",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_onehanded_horseman_axe_03", "Horseman Axe", [("w_onehanded_horseman_axe_03",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_03_alt", "Horseman Axe", [("w_onehanded_horseman_axe_03_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(20 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_horseman_axe_03_brown", "Horseman Axe", [("w_onehanded_horseman_axe_03_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_03_alt_brown", "Horseman Axe", [("w_onehanded_horseman_axe_03_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(20 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_horseman_axe_03_red", "Horseman Axe", [("w_onehanded_horseman_axe_03_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_horseman_axe_03_alt_red", "Horseman Axe", [("w_onehanded_horseman_axe_03_alt_red",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(20 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

### Knight Axes
["w_onehanded_knight_axe_01", "Knight Axe", [("w_onehanded_knight_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
337 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(80)|swing_damage(33 , cut) | thrust_damage(26 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_01_alt", "Knight Axe", [("w_onehanded_knight_axe_01_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
337 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(80)|swing_damage(28 , pierce) | thrust_damage(26 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_01_brown", "Knight Axe", [("w_onehanded_knight_axe_01_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
337 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(80)|swing_damage(33 , cut) | thrust_damage(26 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_01_alt_brown", "Knight Axe", [("w_onehanded_knight_axe_01_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
337 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(80)|swing_damage(28 , pierce) | thrust_damage(26 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_01_ebony", "Knight Axe", [("w_onehanded_knight_axe_01_ebony",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
337 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(80)|swing_damage(33 , cut) | thrust_damage(26 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_01_alt_ebony", "Knight Axe", [("w_onehanded_knight_axe_01_alt_ebony",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
337 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(80)|swing_damage(28 , pierce) | thrust_damage(26 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_onehanded_knight_axe_02", "Knight Axe", [("w_onehanded_knight_axe_02",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
314 , weight(3.2)|difficulty(9)|spd_rtng(95) | weapon_length(89)|swing_damage(34 , cut) | thrust_damage(28 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_02_alt", "Knight Axe", [("w_onehanded_knight_axe_02_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
314 , weight(3.2)|difficulty(9)|spd_rtng(95) | weapon_length(89)|swing_damage(28 , pierce) | thrust_damage(27 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_02_brown", "Knight Axe", [("w_onehanded_knight_axe_02_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
314 , weight(3.2)|difficulty(9)|spd_rtng(95) | weapon_length(89)|swing_damage(34 , cut) | thrust_damage(28 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_02_alt_brown", "Knight Axe", [("w_onehanded_knight_axe_02_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
314 , weight(3.2)|difficulty(9)|spd_rtng(95) | weapon_length(89)|swing_damage(28 , pierce) | thrust_damage(27 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_02_ebony", "Knight Axe", [("w_onehanded_knight_axe_02_ebony",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
314 , weight(3.2)|difficulty(9)|spd_rtng(95) | weapon_length(89)|swing_damage(34 , cut) | thrust_damage(28 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_02_alt_ebony", "Knight Axe", [("w_onehanded_knight_axe_02_alt_ebony",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
314 , weight(3.2)|difficulty(9)|spd_rtng(95) | weapon_length(89)|swing_damage(28 , pierce) | thrust_damage(27 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_onehanded_knight_axe_german_01", "German Knight Axe", [("w_onehanded_knight_axe_german_01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(35 , cut) | thrust_damage(25 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_german_01_alt", "German Knight Axe", [("w_onehanded_knight_axe_german_01_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(27 , pierce) | thrust_damage(25 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_german_01_brown", "German Knight Axe", [("w_onehanded_knight_axe_german_01_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(35 , cut) | thrust_damage(25 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_german_01_alt_brown", "German Knight Axe", [("w_onehanded_knight_axe_german_01_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(27 , pierce) | thrust_damage(25 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_german_01_ebony", "German Knight Axe", [("w_onehanded_knight_axe_german_01_ebony",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(35 , cut) | thrust_damage(25 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_german_01_alt_ebony", "German Knight Axe", [("w_onehanded_knight_axe_german_01_alt_ebony",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(27 , pierce) | thrust_damage(25 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_onehanded_knight_axe_german_02", "German Knight Axe", [("w_onehanded_knight_axe_german_02",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_german_02_alt", "German Knight Axe", [("w_onehanded_knight_axe_german_02_alt",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_german_02_brown", "German Knight Axe", [("w_onehanded_knight_axe_german_02_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_german_02_alt_brown", "German Knight Axe", [("w_onehanded_knight_axe_german_02_alt_brown",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_onehanded_knight_axe_german_02_ebony", "German Knight Axe", [("w_onehanded_knight_axe_german_02_ebony",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_knight_axe_german_02_alt_ebony", "German Knight Axe", [("w_onehanded_knight_axe_german_02_alt_ebony",0)], itp_type_one_handed_wpn| itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

### Twohanded Axes
["w_twohanded_knight_battle_axe_01", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_01",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
371 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(78)|swing_damage(40 , cut) | thrust_damage(24 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_01_alt", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_01_alt",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
371 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(78)|swing_damage(32 , pierce) | thrust_damage(24 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_knight_battle_axe_01_brown", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_01_brown",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
371 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(78)|swing_damage(40 , cut) | thrust_damage(24 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_01_alt_brown", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_01_alt_brown",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
371 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(78)|swing_damage(32 , pierce) | thrust_damage(24 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_knight_battle_axe_01_ebony", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_01_ebony",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
371 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(78)|swing_damage(40 , cut) | thrust_damage(24 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_01_alt_ebony", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_01_alt_ebony",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
371 , weight(3)|difficulty(9)|spd_rtng(96) | weapon_length(78)|swing_damage(32 , pierce) | thrust_damage(24 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_twohanded_knight_battle_axe_02", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_02",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
428 , weight(3.4)|difficulty(10)|spd_rtng(94) | weapon_length(85)|swing_damage(38 , cut) | thrust_damage(33 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_02_alt", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_02_alt",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
428 , weight(3.4)|difficulty(10)|spd_rtng(94) | weapon_length(85)|swing_damage(32 , blunt) | thrust_damage(33 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_knight_battle_axe_02_brown", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_02_brown",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
428 , weight(3.4)|difficulty(10)|spd_rtng(94) | weapon_length(85)|swing_damage(38 , cut) | thrust_damage(33 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_02_alt_brown", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_02_alt_brown",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
428 , weight(3.4)|difficulty(10)|spd_rtng(94) | weapon_length(85)|swing_damage(32 , blunt) | thrust_damage(33 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_knight_battle_axe_02_ebony", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_02_ebony",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
428 , weight(3.4)|difficulty(10)|spd_rtng(94) | weapon_length(85)|swing_damage(38 , cut) | thrust_damage(33 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_02_alt_ebony", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_02_alt_ebony",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
428 , weight(3.4)|difficulty(10)|spd_rtng(94) | weapon_length(85)|swing_damage(32 , blunt) | thrust_damage(33 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_twohanded_knight_battle_axe_03", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_03",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
399 , weight(3.3)|difficulty(10)|spd_rtng(96) | weapon_length(78)|swing_damage(39 , cut) | thrust_damage(29 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_03_alt", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_03_alt",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
399 , weight(3.3)|difficulty(10)|spd_rtng(96) | weapon_length(78)|swing_damage(34 , blunt) | thrust_damage(29 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_knight_battle_axe_03_brown", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_03_brown",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
399 , weight(3.3)|difficulty(10)|spd_rtng(96) | weapon_length(78)|swing_damage(39 , cut) | thrust_damage(29 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_03_alt_brown", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_03_alt_brown",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
399 , weight(3.3)|difficulty(10)|spd_rtng(96) | weapon_length(78)|swing_damage(34 , blunt) | thrust_damage(29 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_knight_battle_axe_03_ebony", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_03_ebony",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
399 , weight(3.3)|difficulty(10)|spd_rtng(96) | weapon_length(78)|swing_damage(39 , cut) | thrust_damage(29 ,  pierce),imodbits_axe ],
["w_twohanded_knight_battle_axe_03_alt_ebony", "Knight Battle Axe", [("w_twohanded_knight_battle_axe_03_alt_ebony",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
399 , weight(3.3)|difficulty(10)|spd_rtng(96) | weapon_length(78)|swing_damage(34 , blunt) | thrust_damage(29 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

["w_twohanded_war_axe_01", "Twohanded War Axe", [("w_twohanded_war_axe_01",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
236, weight(3.5)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(41,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_01_brown", "Twohanded War Axe", [("w_twohanded_war_axe_01_brown",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
236, weight(3.5)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(41,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_01_red", "Twohanded War Axe", [("w_twohanded_war_axe_01_red",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
236, weight(3.5)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(41,cut)|thrust_damage(0,blunt), imodbits_axe ],

["w_twohanded_war_axe_02", "Twohanded War Axe", [("w_twohanded_war_axe_02",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
287, weight(4)|difficulty(10)|spd_rtng(94)|weapon_length(98)|swing_damage(43,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_02_brown", "Twohanded War Axe", [("w_twohanded_war_axe_02_brown",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
287, weight(4)|difficulty(10)|spd_rtng(94)|weapon_length(98)|swing_damage(43,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_02_red", "Twohanded War Axe", [("w_twohanded_war_axe_02_red",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
287, weight(4)|difficulty(10)|spd_rtng(94)|weapon_length(98)|swing_damage(43,cut)|thrust_damage(0,blunt), imodbits_axe ],

["w_twohanded_war_axe_03", "Twohanded War Axe", [("w_twohanded_war_axe_03",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(44,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_03_alt", "Twohanded War Axe", [("w_twohanded_war_axe_03_alt",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(30,pierce), imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_war_axe_03_brown", "Twohanded War Axe", [("w_twohanded_war_axe_03_brown",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(44,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_03_alt_brown", "Twohanded War Axe", [("w_twohanded_war_axe_03_alt_brown",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(30,pierce), imodbits_axe, [], [fac_no_faction] ],
["w_twohanded_war_axe_03_red", "Twohanded War Axe", [("w_twohanded_war_axe_03_red",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(44,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_03_alt_red", "Twohanded War Axe", [("w_twohanded_war_axe_03_alt_red",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(30,pierce), imodbits_axe, [], [fac_no_faction] ],

### Gallowglass Axe
# ["w_gallowglass_axe", "Gallowglass Axe", [("w_gallowglass_axe",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
# 304 , weight(4)|difficulty(10)|spd_rtng(90) | weapon_length(156)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["w_gallowglass_axe_brown", "Gallowglass Axe", [("w_gallowglass_axe_brown",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
# 304 , weight(4)|difficulty(10)|spd_rtng(90) | weapon_length(156)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["w_gallowglass_axe_red", "Gallowglass Axe", [("w_gallowglass_axe_red",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
# 304 , weight(4)|difficulty(10)|spd_rtng(90) | weapon_length(156)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

### Bardiches
["w_bardiche_1",  "Bardiche", [("w_bardiche_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
539 , weight(5.75)|difficulty(10)|spd_rtng(86) | weapon_length(140)|swing_damage(51 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_1_brown",  "Bardiche", [("w_bardiche_1_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
539 , weight(5.75)|difficulty(10)|spd_rtng(86) | weapon_length(140)|swing_damage(51 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_1_red",  "Bardiche", [("w_bardiche_1_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
539 , weight(5.75)|difficulty(10)|spd_rtng(86) | weapon_length(140)|swing_damage(51 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_2",  "Bardiche", [("w_bardiche_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
628 , weight(6)|difficulty(10)|spd_rtng(85) | weapon_length(155)|swing_damage(52 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_2_brown",  "Bardiche", [("w_bardiche_2_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
628 , weight(6)|difficulty(10)|spd_rtng(85) | weapon_length(155)|swing_damage(52 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_2_red",  "Bardiche", [("w_bardiche_2_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
628 , weight(6)|difficulty(10)|spd_rtng(85) | weapon_length(155)|swing_damage(52 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_3",  "Bardiche", [("w_bardiche_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
334 , weight(5)|difficulty(10)|spd_rtng(89) | weapon_length(107)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_3_brown",  "Bardiche", [("w_bardiche_3_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
334 , weight(5)|difficulty(10)|spd_rtng(89) | weapon_length(107)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_3_red",  "Bardiche", [("w_bardiche_3_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
334 , weight(5)|difficulty(10)|spd_rtng(89) | weapon_length(107)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_4",  "Bardiche", [("w_bardiche_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
306 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(103)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_4_brown",  "Bardiche", [("w_bardiche_4_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
306 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(103)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_4_red",  "Bardiche", [("w_bardiche_4_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
306 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(103)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_5",  "Bardiche", [("w_bardiche_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
368 , weight(5.25)|difficulty(10)|spd_rtng(90) | weapon_length(106)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_5_brown",  "Bardiche", [("w_bardiche_5_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
368 , weight(5.25)|difficulty(10)|spd_rtng(90) | weapon_length(106)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_5_red",  "Bardiche", [("w_bardiche_5_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
368 , weight(5.25)|difficulty(10)|spd_rtng(90) | weapon_length(106)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_6",  "Bardiche", [("w_bardiche_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
399 , weight(5.25)|difficulty(10)|spd_rtng(89) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_6_brown",  "Bardiche", [("w_bardiche_6_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
399 , weight(5.25)|difficulty(10)|spd_rtng(89) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_6_red",  "Bardiche", [("w_bardiche_6_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
399 , weight(5.25)|difficulty(10)|spd_rtng(89) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_7",  "Bardiche", [("w_bardiche_7",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
291 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(106)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_7_brown",  "Bardiche", [("w_bardiche_7_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
291 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(106)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_7_red",  "Bardiche", [("w_bardiche_7_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
291 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(106)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_8",  "Bardiche", [("w_bardiche_8",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
498 , weight(5.5)|difficulty(10)|spd_rtng(88) | weapon_length(105)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_8_brown",  "Bardiche", [("w_bardiche_8_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
498 , weight(5.5)|difficulty(10)|spd_rtng(88) | weapon_length(105)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_8_red",  "Bardiche", [("w_bardiche_8_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
498 , weight(5.5)|difficulty(10)|spd_rtng(88) | weapon_length(105)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_9",  "Bardiche", [("w_bardiche_9",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
464 , weight(5.5)|difficulty(10)|spd_rtng(89) | weapon_length(101)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_9_brown",  "Bardiche", [("w_bardiche_9_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
464 , weight(5.5)|difficulty(10)|spd_rtng(89) | weapon_length(101)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_9_red",  "Bardiche", [("w_bardiche_9_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_bardiche, 
464 , weight(5.5)|difficulty(10)|spd_rtng(89) | weapon_length(101)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW MACES | CLUBS | HAMMERS ###############################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_wooden_stick",         "Wooden Stick", [("w_wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip,
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],

["w_archers_maul",         "Archer Maul", [("w_archers_maul",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip,
77 , weight(2)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["w_archers_maul_brown",         "Archer Maul", [("w_archers_maul_brown",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip,
77 , weight(2)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["w_archers_maul_red",         "Archer Maul", [("w_archers_maul_red",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip,
77 , weight(2)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],

["w_warhammer_1",         "Warhammer", [("w_warhammer_1",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_1_alt",         "Warhammer", [("w_warhammer_1_alt",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_warhammer_1_brown",         "Warhammer", [("w_warhammer_1_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_1_alt_brown",         "Warhammer", [("w_warhammer_1_alt_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_warhammer_1_red",         "Warhammer", [("w_warhammer_1_red",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_1_alt_red",         "Warhammer", [("w_warhammer_1_alt_red",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],

["w_warhammer_2",         "Warhammer", [("w_warhammer_2",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_2_alt",         "Warhammer", [("w_warhammer_2_alt",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_warhammer_2_brown",         "Warhammer", [("w_warhammer_2_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_2_alt_brown",         "Warhammer", [("w_warhammer_2_alt_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_warhammer_2_red",         "Warhammer", [("w_warhammer_2_red",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_2_alt_red",         "Warhammer", [("w_warhammer_2_alt_red",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],

["w_knight_warhammer_1",         "Spiked Knight Warhammer", [("w_knight_warhammer_1",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
372 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(76)|swing_damage(33 , blunt) | thrust_damage(19,  pierce),imodbits_mace ],
["w_knight_warhammer_1_alt",         "Spiked Knight Warhammer", [("w_knight_warhammer_1_alt",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
372 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(76)|swing_damage(26 , pierce) | thrust_damage(19,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_knight_warhammer_1_brown",         "Spiked Knight Warhammer", [("w_knight_warhammer_1_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
372 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(76)|swing_damage(33 , blunt) | thrust_damage(19,  pierce),imodbits_mace ],
["w_knight_warhammer_1_alt_brown",         "Spiked Knight Warhammer", [("w_knight_warhammer_1_alt_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
372 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(76)|swing_damage(26 , pierce) | thrust_damage(19,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_knight_warhammer_1_ebony",         "Spiked Knight Warhammer", [("w_knight_warhammer_1_ebony",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
372 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(76)|swing_damage(33 , blunt) | thrust_damage(19,  pierce),imodbits_mace ],
["w_knight_warhammer_1_alt_ebony",         "Spiked Knight Warhammer", [("w_knight_warhammer_1_alt_ebony",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
372 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(76)|swing_damage(26 , pierce) | thrust_damage(19,  pierce),imodbits_mace, [], [fac_no_faction] ],

["w_knight_warhammer_2",         "Knight Warhammer", [("w_knight_warhammer_2",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_knight_warhammer_2_alt",         "Knight Warhammer", [("w_knight_warhammer_2_alt",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_knight_warhammer_2_brown",         "Knight Warhammer", [("w_knight_warhammer_2_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_knight_warhammer_2_alt_brown",         "Knight Warhammer", [("w_knight_warhammer_2_alt_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_knight_warhammer_2_ebony",         "Knight Warhammer", [("w_knight_warhammer_2_ebony",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_knight_warhammer_2_alt_ebony",         "Knight Warhammer", [("w_knight_warhammer_2_alt_ebony",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],

["w_knight_warhammer_3",         "Knight Warhammer", [("w_knight_warhammer_3",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
365 , weight(2.2)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(34 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_knight_warhammer_3_alt",         "Knight Warhammer", [("w_knight_warhammer_3_alt",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
365 , weight(2.2)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(34 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_knight_warhammer_3_brown",         "Knight Warhammer", [("w_knight_warhammer_3_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
365 , weight(2.2)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(34 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_knight_warhammer_3_alt_brown",         "Knight Warhammer", [("w_knight_warhammer_3_alt_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
365 , weight(2.2)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(34 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_knight_warhammer_3_ebony",         "Knight Warhammer", [("w_knight_warhammer_3_ebony",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
365 , weight(2.2)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(34 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_knight_warhammer_3_alt_ebony",         "Knight Warhammer", [("w_knight_warhammer_3_alt_ebony",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
365 , weight(2.2)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(34 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],

["w_great_hammer", "Greathammer", [("w_great_hammer",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
422 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_great_hammer_brown", "Greathammer", [("w_great_hammer_brown",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
422 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_great_hammer_red", "Greathammer", [("w_great_hammer_red",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
422 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_kriegshammer", "Kriegshammer", [("w_kriegshammer",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_greatsword|itcf_carry_spear,
512 , weight(4.5)|difficulty(12)|spd_rtng(82) | weapon_length(83)|swing_damage(42, blunt) | thrust_damage(32 ,  pierce),imodbits_mace ],
["w_kriegshammer_alt", "Kriegshammer", [("w_kriegshammer_alt",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_greatsword|itcf_carry_spear,
512 , weight(4.5)|difficulty(12)|spd_rtng(82) | weapon_length(83)|swing_damage(38, pierce) | thrust_damage(32 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_kriegshammer_brown", "Kriegshammer", [("w_kriegshammer_brown",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_greatsword|itcf_carry_spear,
512 , weight(4.5)|difficulty(12)|spd_rtng(82) | weapon_length(83)|swing_damage(42, blunt) | thrust_damage(32 ,  pierce),imodbits_mace ],
["w_kriegshammer_alt_brown", "Kriegshammer", [("w_kriegshammer_alt_brown",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_greatsword|itcf_carry_spear,
512 , weight(4.5)|difficulty(12)|spd_rtng(82) | weapon_length(83)|swing_damage(38, pierce) | thrust_damage(32 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["w_kriegshammer_ebony", "Kriegshammer", [("w_kriegshammer_ebony",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_greatsword|itcf_carry_spear,
512 , weight(4.5)|difficulty(12)|spd_rtng(82) | weapon_length(83)|swing_damage(42, blunt) | thrust_damage(32 ,  pierce),imodbits_mace ],
["w_kriegshammer_alt_ebony", "Kriegshammer", [("w_kriegshammer_alt_ebony",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_greatsword|itcf_carry_spear,
512 , weight(4.5)|difficulty(12)|spd_rtng(82) | weapon_length(83)|swing_damage(38, pierce) | thrust_damage(32 ,  pierce),imodbits_mace, [], [fac_no_faction] ],

["w_knight_winged_mace", "Knight Winged Mace", [("w_knight_winged_mace",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
336, weight(4)|difficulty(0)|spd_rtng(96)|weapon_length(69)|swing_damage(28,blunt), imodbits_mace ],
["w_knight_flanged_mace", "Knight Flanged Mace", [("w_knight_flanged_mace",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
344, weight(4.2)|difficulty(0)|spd_rtng(96)|weapon_length(72)|swing_damage(29,blunt), imodbits_mace ],

["w_mace_english", "English Mace", [("w_mace_english",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
262, weight(3.25)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(26,blunt), imodbits_mace ],
["w_mace_english_brown", "English Mace", [("w_mace_english_brown",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
262, weight(3.25)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(26,blunt), imodbits_mace ],
["w_mace_english_ebony", "English Mace", [("w_mace_english_ebony",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
262, weight(3.25)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(26,blunt), imodbits_mace ],

["w_mace_german", "German Mace", [("w_mace_german",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
278, weight(3.4)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(27,blunt), imodbits_mace ],
["w_mace_german_brown", "German Mace", [("w_mace_german_brown",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
278, weight(3.4)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(27,blunt), imodbits_mace ],
["w_mace_german_ebony", "German Mace", [("w_mace_german_ebony",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
278, weight(3.4)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(27,blunt), imodbits_mace ],

["w_spiked_club",         "Spiked Club", [("w_spiked_club",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3.25)|difficulty(0)|spd_rtng(96) | weapon_length(75)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_spiked_club_brown",         "Spiked Club", [("w_spiked_club_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3.25)|difficulty(0)|spd_rtng(96) | weapon_length(75)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_spiked_club_dark",         "Spiked Club", [("w_spiked_club_dark",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3.25)|difficulty(0)|spd_rtng(96) | weapon_length(75)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_mace_knobbed",         "Knobbed_Mace", [("w_mace_knobbed",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_knobbed_brown",         "Knobbed_Mace", [("w_mace_knobbed_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_knobbed_red",         "Knobbed_Mace", [("w_mace_knobbed_red",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_mace_spiked",         "Spiked Mace", [("w_mace_spiked",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(71)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_spiked_brown",         "Spiked Mace", [("w_mace_spiked_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(71)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_spiked_red",         "Spiked Mace", [("w_mace_spiked_red",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(71)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_mace_winged",         "Winged_Mace", [("w_mace_winged",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
212 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(71)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_winged_brown",         "Winged_Mace", [("w_mace_winged_brown",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
212 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(71)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_winged_red",         "Winged_Mace", [("w_mace_winged_red",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
212 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(71)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW POLEARMS ##############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_awlpike_1", "Short Pike", [("w_awlpike_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
278 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(185)|thrust_damage(34 ,  pierce),imodbits_polearm ],
["w_awlpike_2", "Short Pike", [("w_awlpike_2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
283 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(188)|thrust_damage(35 ,  pierce),imodbits_polearm ],
["w_awlpike_3", "Short Pike", [("w_awlpike_3",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
280 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(188)|thrust_damage(33 ,  pierce),imodbits_polearm ],
["w_awlpike_4", "Short Pike", [("w_awlpike_4",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
275 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(187)|thrust_damage(36 ,  pierce),imodbits_polearm ],
["w_awlpike_5", "Short Pike", [("w_awlpike_5",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
273 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(181)|thrust_damage(35 ,  pierce),imodbits_polearm ],
["w_awlpike_6", "Short Pike", [("w_awlpike_6",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
275 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(193)|thrust_damage(31 ,  pierce),imodbits_polearm ],
["w_awlpike_7", "Short Pike", [("w_awlpike_7",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
336 , weight(3.0)|difficulty(0)|spd_rtng(82) | weapon_length(246)|thrust_damage(35,pierce),imodbits_polearm ],

["w_pike_1", "Pike", [("w_pike_1",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
497 , weight(3.5)|difficulty(0)|spd_rtng(78) | weapon_length(450)|thrust_damage(30,pierce),imodbits_polearm ],
["w_pike_swiss_1", "Swiss Pike", [("w_pike_swiss_1",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
344 , weight(3.0)|difficulty(0)|spd_rtng(82) | weapon_length(255)|thrust_damage(33,pierce),imodbits_polearm ],
["w_pike_swiss_2", "Swiss Pike", [("w_pike_swiss_2",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab|itp_is_pike, itc_pike_upstab, 
336 , weight(3.0)|difficulty(0)|spd_rtng(82) | weapon_length(246)|thrust_damage(35,pierce),imodbits_polearm ],

["w_bill_1", "Bill", [("w_bill_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
424, weight(4)|difficulty(9)|spd_rtng(85)|weapon_length(191)|swing_damage(38,cut)|thrust_damage(29,pierce), imodbits_polearm ],
["w_bill_2", "Bill", [("w_bill_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
455, weight(4.1)|difficulty(9)|spd_rtng(85)|weapon_length(207)|swing_damage(44,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_bill_3", "Bill", [("w_bill_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
480, weight(4.3)|difficulty(9)|spd_rtng(85)|weapon_length(233)|swing_damage(46,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_bill_4", "Bill", [("w_bill_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
505, weight(4.5)|difficulty(9)|spd_rtng(85)|weapon_length(246)|swing_damage(45,cut)|thrust_damage(37,pierce), imodbits_polearm ],

["w_fauchard_1", "Fauchard", [("w_fauchard_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itc_voulge, 
170, weight(2.5)|difficulty(9)|spd_rtng(87)|weapon_length(151)|swing_damage(34,cut), imodbits_polearm ],
["w_fauchard_2", "Fauchard", [("w_fauchard_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itc_voulge, 
257, weight(2.3)|difficulty(9)|spd_rtng(88)|weapon_length(130)|swing_damage(32,cut), imodbits_polearm ],
["w_fauchard_3", "Fauchard", [("w_fauchard_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itc_voulge, 
196, weight(3)|difficulty(9)|spd_rtng(84)|weapon_length(196)|swing_damage(35,cut), imodbits_polearm ],

["w_fork_1", "Pitch Fork", [("w_fork_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_has_upper_stab, itc_spear_upstab, 
87, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(135)|thrust_damage(22,pierce), imodbits_polearm ],
["w_fork_2", "Pitch Fork", [("w_fork_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_has_upper_stab, itc_spear_upstab, 
83, weight(1.4)|difficulty(0)|spd_rtng(88)|weapon_length(126)|thrust_damage(22,pierce), imodbits_polearm ],

["w_glaive_1", "Glaive", [("w_glaive_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
265, weight(1.9)|difficulty(9)|spd_rtng(92)|weapon_length(160)|swing_damage(37,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_glaive_1_brown", "Glaive", [("w_glaive_1_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
265, weight(1.9)|difficulty(9)|spd_rtng(92)|weapon_length(160)|swing_damage(37,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_glaive_1_red", "Glaive", [("w_glaive_1_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
265, weight(1.9)|difficulty(9)|spd_rtng(92)|weapon_length(160)|swing_damage(37,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_glaive_2", "Glaive", [("w_glaive_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
312, weight(2.5)|difficulty(9)|spd_rtng(84)|weapon_length(228)|swing_damage(36,cut)|thrust_damage(31,pierce), imodbits_polearm ],
["w_glaive_2_brown", "Glaive", [("w_glaive_2_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
312, weight(2.5)|difficulty(9)|spd_rtng(84)|weapon_length(228)|swing_damage(36,cut)|thrust_damage(31,pierce), imodbits_polearm ],
["w_glaive_2_red", "Glaive", [("w_glaive_2_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
312, weight(2.5)|difficulty(9)|spd_rtng(84)|weapon_length(228)|swing_damage(36,cut)|thrust_damage(31,pierce), imodbits_polearm ],
["w_glaive_3", "Glaive", [("w_glaive_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
255, weight(2)|difficulty(9)|spd_rtng(91)|weapon_length(164)|swing_damage(31,cut)|thrust_damage(22,pierce), imodbits_polearm ],
["w_glaive_3_brown", "Glaive", [("w_glaive_3_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
255, weight(2)|difficulty(9)|spd_rtng(91)|weapon_length(164)|swing_damage(31,cut)|thrust_damage(22,pierce), imodbits_polearm ],
["w_glaive_3_red", "Glaive", [("w_glaive_3_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
255, weight(2)|difficulty(9)|spd_rtng(91)|weapon_length(164)|swing_damage(31,cut)|thrust_damage(22,pierce), imodbits_polearm ],
["w_glaive_4", "Glaive", [("w_glaive_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
275, weight(2.2)|difficulty(9)|spd_rtng(90)|weapon_length(175)|swing_damage(33,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_glaive_4_brown", "Glaive", [("w_glaive_4_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
275, weight(2.2)|difficulty(9)|spd_rtng(90)|weapon_length(175)|swing_damage(33,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_glaive_4_ebony", "Glaive", [("w_glaive_4_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
275, weight(2.2)|difficulty(9)|spd_rtng(90)|weapon_length(175)|swing_damage(33,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_glaive_5", "Glaive", [("w_glaive_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
300, weight(2.4)|difficulty(9)|spd_rtng(86)|weapon_length(212)|swing_damage(32,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_glaive_5_brown", "Glaive", [("w_glaive_5_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
300, weight(2.4)|difficulty(9)|spd_rtng(86)|weapon_length(212)|swing_damage(32,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_glaive_5_red", "Glaive", [("w_glaive_5_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
300, weight(2.4)|difficulty(9)|spd_rtng(86)|weapon_length(212)|swing_damage(32,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_glaive_6", "Glaive", [("w_glaive_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
269, weight(2.3)|difficulty(9)|spd_rtng(92)|weapon_length(164)|swing_damage(36,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_glaive_6_brown", "Glaive", [("w_glaive_6_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
269, weight(2.3)|difficulty(9)|spd_rtng(92)|weapon_length(164)|swing_damage(36,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_glaive_6_red", "Glaive", [("w_glaive_6_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
269, weight(2.3)|difficulty(9)|spd_rtng(92)|weapon_length(164)|swing_damage(36,cut)|thrust_damage(35,pierce), imodbits_polearm ],

["w_goedendag",  "Goedendag", [("w_goedendag",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back, 
200 , weight(2.5)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],
["w_goedendag_burgundy",  "Burgundian Goedendag", [("w_goedendag_burgundy",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_no_blur|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back, 
372 , weight(2.8)|difficulty(9)|spd_rtng(93) | weapon_length(125)|swing_damage(36 , blunt) | thrust_damage(28 ,  pierce),imodbits_mace ],

["w_halberd_1", "Halberd", [("w_halberd_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
313, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_1_alt", "Halberd", [("w_halberd_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
313, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_halberd_1_brown", "Halberd", [("w_halberd_1_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
313, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_1_brown_alt", "Halberd", [("w_halberd_1_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
313, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_halberd_2", "Halberd", [("w_halberd_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
308, weight(3.0)|difficulty(9)|spd_rtng(80)|weapon_length(181)|swing_damage(37,cut)|thrust_damage(33,pierce), imodbits_polearm ],
["w_halberd_2_alt", "Halberd", [("w_halberd_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
308, weight(3.0)|difficulty(9)|spd_rtng(80)|weapon_length(181)|swing_damage(37,cut)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_halberd_2_brown", "Halberd", [("w_halberd_2_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
308, weight(3.0)|difficulty(9)|spd_rtng(80)|weapon_length(181)|swing_damage(37,cut)|thrust_damage(33,pierce), imodbits_polearm ],
["w_halberd_2_brown_alt", "Halberd", [("w_halberd_2_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
308, weight(3.0)|difficulty(9)|spd_rtng(80)|weapon_length(181)|swing_damage(37,cut)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_halberd_3", "Halberd", [("w_halberd_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
309, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(182)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_halberd_3_alt", "Halberd", [("w_halberd_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
309, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(182)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_halberd_3_brown", "Halberd", [("w_halberd_3_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
309, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(182)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_halberd_3_brown_alt", "Halberd", [("w_halberd_3_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
309, weight(3.1)|difficulty(9)|spd_rtng(79)|weapon_length(182)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_halberd_4", "Halberd", [("w_halberd_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
313, weight(3.3)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_4_alt", "Halberd", [("w_halberd_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
313, weight(3.3)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_halberd_4_brown", "Halberd", [("w_halberd_4_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
313, weight(3.3)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_4_brown_alt", "Halberd", [("w_halberd_4_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
313, weight(3.3)|difficulty(9)|spd_rtng(79)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_halberd_5", "Halberd", [("w_halberd_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
321, weight(3.5)|difficulty(9)|spd_rtng(76)|weapon_length(193)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_halberd_5_alt", "Halberd", [("w_halberd_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
321, weight(3.5)|difficulty(9)|spd_rtng(76)|weapon_length(193)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_halberd_5_brown", "Halberd", [("w_halberd_5_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
321, weight(3.5)|difficulty(9)|spd_rtng(76)|weapon_length(193)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_halberd_5_brown_alt", "Halberd", [("w_halberd_5_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
321, weight(3.5)|difficulty(9)|spd_rtng(76)|weapon_length(193)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_halberd_6", "Halberd", [("w_halberd_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
315, weight(3.3)|difficulty(9)|spd_rtng(78)|weapon_length(186)|swing_damage(37,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["w_halberd_6_alt", "Halberd", [("w_halberd_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
315, weight(3.3)|difficulty(9)|spd_rtng(78)|weapon_length(186)|swing_damage(37,cut)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_halberd_6_brown", "Halberd", [("w_halberd_6_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_next_item_as_melee, itc_poleaxe, 
315, weight(3.3)|difficulty(9)|spd_rtng(78)|weapon_length(186)|swing_damage(37,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["w_halberd_6_brown_alt", "Halberd", [("w_halberd_6_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike|itp_has_upper_stab, itc_halberd_upstab, 
315, weight(3.3)|difficulty(9)|spd_rtng(78)|weapon_length(186)|swing_damage(37,cut)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_scythe_1", "Scythe", [("w_scythe_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itc_voulge, 
213, weight(3.5)|difficulty(0)|spd_rtng(85)|weapon_length(133)|swing_damage(39,cut), imodbits_polearm ],

["w_spear_1", "Spear", [("w_spear_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
134, weight(1.1)|difficulty(0)|spd_rtng(99)|weapon_length(107)|thrust_damage(37,pierce), imodbits_polearm ],
["w_spear_1_alt", "Spear", [("w_spear_1",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
134 , weight(1.1)|difficulty(0)|spd_rtng(98) | shoot_speed(20) | thrust_damage(47, pierce)|max_ammo(1)|weapon_length(107),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_2", "Spear", [("w_spear_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
144, weight(1.3)|difficulty(0)|spd_rtng(97)|weapon_length(128)|thrust_damage(36,pierce), imodbits_polearm ],
["w_spear_2_alt", "Spear", [("w_spear_2",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
144 , weight(1.3)|difficulty(0)|spd_rtng(97) | shoot_speed(20) | thrust_damage(46, pierce)|max_ammo(1)|weapon_length(128),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_3", "Spear", [("w_spear_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
146, weight(1.3)|difficulty(0)|spd_rtng(97)|weapon_length(132)|thrust_damage(36,pierce), imodbits_polearm ],
["w_spear_3_alt", "Spear", [("w_spear_3",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
146 , weight(1.3)|difficulty(0)|spd_rtng(97) | shoot_speed(20) | thrust_damage(46, pierce)|max_ammo(1)|weapon_length(132),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_4", "Spear", [("w_spear_4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
165, weight(1.4)|difficulty(0)|spd_rtng(96)|weapon_length(142)|thrust_damage(35,pierce), imodbits_polearm ],
["w_spear_4_alt", "Spear", [("w_spear_4",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
165 , weight(1.4)|difficulty(0)|spd_rtng(96) | shoot_speed(20) | thrust_damage(45, pierce)|max_ammo(1)|weapon_length(142),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_5", "Spear", [("w_spear_5",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
166, weight(1.4)|difficulty(0)|spd_rtng(96)|weapon_length(144)|thrust_damage(35,pierce), imodbits_polearm ],
["w_spear_5_alt", "Spear", [("w_spear_5",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
166 , weight(1.4)|difficulty(0)|spd_rtng(96) | shoot_speed(20) | thrust_damage(45, pierce)|max_ammo(1)|weapon_length(144),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_6", "Spear", [("w_spear_6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
168, weight(1.5)|difficulty(0)|spd_rtng(95)|weapon_length(149)|thrust_damage(34,pierce), imodbits_polearm ],
["w_spear_6_alt", "Spear", [("w_spear_6",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
168 , weight(1.5)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(44, pierce)|max_ammo(1)|weapon_length(149),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_7", "Spear", [("w_spear_7",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
229, weight(2)|difficulty(0)|spd_rtng(90)|weapon_length(204)|thrust_damage(31,pierce), imodbits_polearm ],
["w_spear_7_alt", "Spear", [("w_spear_7",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
229 , weight(2)|difficulty(0)|spd_rtng(90) | shoot_speed(20) | thrust_damage(41, pierce)|max_ammo(1)|weapon_length(204),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_8", "Spear", [("w_spear_8",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
117, weight(1)|difficulty(0)|spd_rtng(100)|weapon_length(95)|thrust_damage(38,pierce), imodbits_polearm ],
["w_spear_8_alt", "Spear", [("w_spear_8",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
117 , weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(20) | thrust_damage(48, pierce)|max_ammo(1)|weapon_length(95),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_9", "Spear", [("w_spear_9",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
164, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(120)|thrust_damage(35,pierce), imodbits_polearm ],
["w_spear_9_alt", "Spear", [("w_spear_9",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
164 , weight(2.5)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(48, pierce)|max_ammo(1)|weapon_length(120),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_10", "Spear", [("w_spear_10",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(134)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_10_alt", "Spear", [("w_spear_10",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
140 , weight(2.5)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(46, pierce)|max_ammo(1)|weapon_length(134),imodbits_thrown, [], [fac_no_faction] ],
["w_spear_11", "Spear", [("w_spear_11",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur|itp_has_upper_stab, itc_spear_upstab, 
140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(150)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_11_alt", "Spear", [("w_spear_11",0)], itp_type_thrown|itp_primary|itp_no_blur ,itcf_throw_javelin, 
140 , weight(2.5)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(44, pierce)|max_ammo(1)|weapon_length(150),imodbits_thrown, [], [fac_no_faction] ],

["w_pollaxe_blunt_01_french_ash", "French Pollaxe", [("w_pollaxe_blunt_01_french_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1047, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(33,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_01_french_ash", "French Pollaxe", [("w_pollaxe_blunt_alt_01_french_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1047, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(35,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_01_french_brown", "French Pollaxe", [("w_pollaxe_blunt_01_french_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1047, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(33,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_01_french_brown", "French Pollaxe", [("w_pollaxe_blunt_alt_01_french_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1047, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(35,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_01_french_red", "French Pollaxe", [("w_pollaxe_blunt_01_french_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1047, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(33,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_01_french_red", "French Pollaxe", [("w_pollaxe_blunt_alt_01_french_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1047, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(35,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_02_french_ash", "French Pollaxe", [("w_pollaxe_blunt_02_french_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1142, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(36,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_02_french_ash", "French Pollaxe", [("w_pollaxe_blunt_alt_02_french_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1142, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(35,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_02_french_ebony_trim", "French Pollaxe", [("w_pollaxe_blunt_02_french_ebony_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1142, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(36,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_02_french_ebony_trim", "French Pollaxe", [("w_pollaxe_blunt_alt_02_french_ebony_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1142, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(35,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_02_french_red_trim", "French Pollaxe", [("w_pollaxe_blunt_02_french_red_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1142, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(36,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_02_french_red_trim", "French Pollaxe", [("w_pollaxe_blunt_alt_02_french_red_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1142, weight(2.3)|difficulty(12)|spd_rtng(90)|weapon_length(148)|swing_damage(35,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_03_ash", "Pollaxe", [("w_pollaxe_blunt_03_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_03_ash", "Pollaxe", [("w_pollaxe_blunt_alt_03_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_03_brown", "Pollaxe", [("w_pollaxe_blunt_03_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_03_brown", "Pollaxe", [("w_pollaxe_blunt_alt_03_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_03_ebony_trim", "Pollaxe", [("w_pollaxe_blunt_03_ebony_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_03_ebony_trim", "Pollaxe", [("w_pollaxe_blunt_alt_03_ebony_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_03_red_trim", "Pollaxe", [("w_pollaxe_blunt_03_red_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_03_red_trim", "Pollaxe", [("w_pollaxe_blunt_alt_03_red_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1070, weight(2.2)|difficulty(12)|spd_rtng(91)|weapon_length(141)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_04_english_ash", "English Pollaxe", [("w_pollaxe_blunt_04_english_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_04_english_ash", "English Pollaxe", [("w_pollaxe_blunt_alt_04_english_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_04_english_brown_trim", "English Pollaxe", [("w_pollaxe_blunt_04_english_brown_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_04_english_brown_trim", "English Pollaxe", [("w_pollaxe_blunt_alt_04_english_brown_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_04_english_dark", "English Pollaxe", [("w_pollaxe_blunt_04_english_dark",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_04_english_dark", "English Pollaxe", [("w_pollaxe_blunt_alt_04_english_dark",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_04_english_red_trim", "English Pollaxe", [("w_pollaxe_blunt_04_english_red_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_04_english_red_trim", "English Pollaxe", [("w_pollaxe_blunt_alt_04_english_red_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
990, weight(2.0)|difficulty(12)|spd_rtng(93)|weapon_length(124)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_05_ash", "Pollaxe", [("w_pollaxe_blunt_05_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1343, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(159)|swing_damage(38,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_05_ash", "Pollaxe", [("w_pollaxe_blunt_alt_05_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1343, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(159)|swing_damage(38,pierce)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_05_brown", "Pollaxe", [("w_pollaxe_blunt_05_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1343, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(159)|swing_damage(38,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_05_brown", "Pollaxe", [("w_pollaxe_blunt_alt_05_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1343, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(159)|swing_damage(38,pierce)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_05_ebony", "Pollaxe", [("w_pollaxe_blunt_05_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1343, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(159)|swing_damage(38,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_05_ebony", "Pollaxe", [("w_pollaxe_blunt_alt_05_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1343, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(159)|swing_damage(38,pierce)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_06_italian_ash", "Italian Pollaxe", [("w_pollaxe_blunt_06_italian_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1052, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(159)|swing_damage(32,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_06_italian_ash", "Italian Pollaxe", [("w_pollaxe_blunt_alt_06_italian_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1052, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(159)|swing_damage(39,pierce)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_06_italian_brown", "Italian Pollaxe", [("w_pollaxe_blunt_06_italian_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1052, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(159)|swing_damage(32,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_06_italian_brown", "Italian Pollaxe", [("w_pollaxe_blunt_alt_06_italian_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1052, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(159)|swing_damage(39,pierce)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_06_italian_red", "Italian Pollaxe", [("w_pollaxe_blunt_06_italian_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1052, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(159)|swing_damage(32,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_06_italian_red", "Italian Pollaxe", [("w_pollaxe_blunt_alt_06_italian_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1052, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(159)|swing_damage(39,pierce)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_07_ash", "Pollaxe", [("w_pollaxe_blunt_07_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1125, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(144)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_07_ash", "Pollaxe", [("w_pollaxe_blunt_alt_07_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1125, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(144)|swing_damage(38,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_07_brown", "Pollaxe", [("w_pollaxe_blunt_07_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1125, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(144)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_07_brown", "Pollaxe", [("w_pollaxe_blunt_alt_07_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1125, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(144)|swing_damage(38,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_07_ebony", "Pollaxe", [("w_pollaxe_blunt_07_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1125, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(144)|swing_damage(35,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_07_ebony", "Pollaxe", [("w_pollaxe_blunt_alt_07_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1125, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(144)|swing_damage(38,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_08_ash", "Pollaxe", [("w_pollaxe_blunt_08_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1333, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_08_ash", "Pollaxe", [("w_pollaxe_blunt_alt_08_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1333, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(38,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_08_brown", "Pollaxe", [("w_pollaxe_blunt_08_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1333, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_08_brown", "Pollaxe", [("w_pollaxe_blunt_alt_08_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1333, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(38,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_08_red", "Pollaxe", [("w_pollaxe_blunt_08_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1333, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_08_red", "Pollaxe", [("w_pollaxe_blunt_alt_08_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1333, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(38,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_09_ash", "Pollaxe", [("w_pollaxe_blunt_09_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1253, weight(2.6)|difficulty(12)|spd_rtng(84)|weapon_length(164)|swing_damage(35,blunt)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_09_ash", "Pollaxe", [("w_pollaxe_blunt_alt_09_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1253, weight(2.6)|difficulty(12)|spd_rtng(84)|weapon_length(164)|swing_damage(39,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_09_brown", "Pollaxe", [("w_pollaxe_blunt_09_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1253, weight(2.6)|difficulty(12)|spd_rtng(84)|weapon_length(164)|swing_damage(35,blunt)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_09_brown", "Pollaxe", [("w_pollaxe_blunt_alt_09_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1253, weight(2.6)|difficulty(12)|spd_rtng(84)|weapon_length(164)|swing_damage(39,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_09_ebony", "Pollaxe", [("w_pollaxe_blunt_09_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1253, weight(2.6)|difficulty(12)|spd_rtng(84)|weapon_length(164)|swing_damage(35,blunt)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_09_ebony", "Pollaxe", [("w_pollaxe_blunt_alt_09_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1253, weight(2.6)|difficulty(12)|spd_rtng(84)|weapon_length(164)|swing_damage(39,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_10_ash", "Pollaxe", [("w_pollaxe_blunt_10_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1138, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(155)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_10_ash", "Pollaxe", [("w_pollaxe_blunt_alt_10_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1138, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(155)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_10_brown", "Pollaxe", [("w_pollaxe_blunt_10_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1138, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(155)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_10_brown", "Pollaxe", [("w_pollaxe_blunt_alt_10_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1138, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(155)|swing_damage(34,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_11_ash", "Pollaxe", [("w_pollaxe_blunt_11_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1227, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(154)|swing_damage(38,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_11_ash", "Pollaxe", [("w_pollaxe_blunt_alt_11_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1227, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(154)|swing_damage(37,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_11_ebony", "Pollaxe", [("w_pollaxe_blunt_11_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1227, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(154)|swing_damage(38,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_11_ebony", "Pollaxe", [("w_pollaxe_blunt_alt_11_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1227, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(154)|swing_damage(37,pierce)|thrust_damage(33,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_blunt_12_brown", "Pollaxe", [("w_pollaxe_blunt_12_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1313, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(151)|swing_damage(37,blunt)|thrust_damage(37,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_12_brown", "Pollaxe", [("w_pollaxe_blunt_alt_12_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1313, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(151)|swing_damage(35,pierce)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_blunt_12_ash", "Pollaxe", [("w_pollaxe_blunt_12_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1313, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(151)|swing_damage(37,blunt)|thrust_damage(37,pierce), imodbits_polearm ],
["w_pollaxe_blunt_alt_12_ash", "Pollaxe", [("w_pollaxe_blunt_alt_12_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1313, weight(2.4)|difficulty(12)|spd_rtng(88)|weapon_length(151)|swing_damage(35,pierce)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],

### Axe-bladed pollaxes
["w_pollaxe_cut_01_burgundian_ash", "Burgundian Pollaxe", [("w_pollaxe_cut_01_burgundian_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(42,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_01_burgundian_ash", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_01_burgundian_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_01_burgundian_brown_trim", "Burgundian Pollaxe", [("w_pollaxe_cut_01_burgundian_brown_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(42,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_01_burgundian_brown_trim", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_01_burgundian_brown_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_01_burgundian_dark", "Burgundian Pollaxe", [("w_pollaxe_cut_01_burgundian_dark",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(42,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_01_burgundian_dark", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_01_burgundian_dark",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_01_burgundian_ebony_trim", "Burgundian Pollaxe", [("w_pollaxe_cut_01_burgundian_ebony_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(42,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_01_burgundian_ebony_trim", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_01_burgundian_ebony_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1332, weight(2.3)|difficulty(12)|spd_rtng(91)|weapon_length(142)|swing_damage(34,blunt)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_02_french_ash", "French Pollaxe", [("w_pollaxe_cut_02_french_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1288, weight(2.4)|difficulty(12)|spd_rtng(90)|weapon_length(145)|swing_damage(38,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_02_french_ash", "French Pollaxe", [("w_pollaxe_cut_alt_02_french_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1288, weight(2.4)|difficulty(12)|spd_rtng(90)|weapon_length(145)|swing_damage(35,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_02_french_spiked_dark", "French Pollaxe", [("w_pollaxe_cut_02_french_spiked_dark",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1288, weight(2.4)|difficulty(12)|spd_rtng(90)|weapon_length(145)|swing_damage(38,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_02_french_spiked_dark", "French Pollaxe", [("w_pollaxe_cut_alt_02_french_spiked_dark",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1288, weight(2.4)|difficulty(12)|spd_rtng(90)|weapon_length(145)|swing_damage(35,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_02_french_spiked_red", "French Pollaxe", [("w_pollaxe_cut_02_french_spiked_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1288, weight(2.4)|difficulty(12)|spd_rtng(90)|weapon_length(145)|swing_damage(38,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_02_french_spiked_red", "French Pollaxe", [("w_pollaxe_cut_alt_02_french_spiked_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1288, weight(2.4)|difficulty(12)|spd_rtng(90)|weapon_length(145)|swing_damage(35,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_03_ash", "Pollaxe", [("w_pollaxe_cut_03_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(41,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_03_ash", "Pollaxe", [("w_pollaxe_cut_alt_03_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(35,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_03_brown", "Pollaxe", [("w_pollaxe_cut_03_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(41,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_03_brown", "Pollaxe", [("w_pollaxe_cut_alt_03_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(35,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_03_red", "Pollaxe", [("w_pollaxe_cut_03_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(41,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_03_red", "Pollaxe", [("w_pollaxe_cut_alt_03_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(35,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_03_red_trim", "Pollaxe", [("w_pollaxe_cut_03_red_trim",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(41,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_03_red_trim", "Pollaxe", [("w_pollaxe_cut_alt_03_red_trim",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1207, weight(2.3)|difficulty(12)|spd_rtng(93)|weapon_length(129)|swing_damage(35,pierce)|thrust_damage(34,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_04_english_ash", "English Pollaxe", [("w_pollaxe_cut_04_english_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1648, weight(2.6)|difficulty(12)|spd_rtng(82)|weapon_length(148)|swing_damage(46,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_04_english_ash", "English Pollaxe", [("w_pollaxe_cut_alt_04_english_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1648, weight(2.6)|difficulty(12)|spd_rtng(82)|weapon_length(148)|swing_damage(36,blunt)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_04_english_brown", "English Pollaxe", [("w_pollaxe_cut_04_english_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1648, weight(2.6)|difficulty(12)|spd_rtng(82)|weapon_length(148)|swing_damage(46,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_04_english_brown", "English Pollaxe", [("w_pollaxe_cut_alt_04_english_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1648, weight(2.6)|difficulty(12)|spd_rtng(82)|weapon_length(148)|swing_damage(36,blunt)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_04_english_ebony", "English Pollaxe", [("w_pollaxe_cut_04_english_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1648, weight(2.6)|difficulty(12)|spd_rtng(82)|weapon_length(148)|swing_damage(46,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_04_english_ebony", "English Pollaxe", [("w_pollaxe_cut_alt_04_english_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1648, weight(2.6)|difficulty(12)|spd_rtng(82)|weapon_length(148)|swing_damage(36,blunt)|thrust_damage(35,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_05_ash", "Pollaxe", [("w_pollaxe_cut_05_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1403, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_05_ash", "Pollaxe", [("w_pollaxe_cut_alt_05_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1403, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(36,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_05_brown", "Pollaxe", [("w_pollaxe_cut_05_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1403, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_05_brown", "Pollaxe", [("w_pollaxe_cut_alt_05_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1403, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(36,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_05_red", "Pollaxe", [("w_pollaxe_cut_05_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1403, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_05_red", "Pollaxe", [("w_pollaxe_cut_alt_05_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1403, weight(2.5)|difficulty(12)|spd_rtng(86)|weapon_length(157)|swing_damage(36,pierce)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_06_ash", "Pollaxe", [("w_pollaxe_cut_06_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1594, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(44,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_06_ash", "Pollaxe", [("w_pollaxe_cut_alt_06_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1594, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_06_ebony", "Pollaxe", [("w_pollaxe_cut_06_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1594, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(44,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_06_ebony", "Pollaxe", [("w_pollaxe_cut_alt_06_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1594, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_06_red", "Pollaxe", [("w_pollaxe_cut_06_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1594, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(44,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_06_red", "Pollaxe", [("w_pollaxe_cut_alt_06_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1594, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_07_ash", "Pollaxe", [("w_pollaxe_cut_07_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1558, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(43,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_07_ash", "Pollaxe", [("w_pollaxe_cut_alt_07_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1558, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_07_brown", "Pollaxe", [("w_pollaxe_cut_07_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1558, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(43,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_07_brown", "Pollaxe", [("w_pollaxe_cut_alt_07_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1558, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_07_red", "Pollaxe", [("w_pollaxe_cut_07_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1558, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(43,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_07_red", "Pollaxe", [("w_pollaxe_cut_alt_07_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1558, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(166)|swing_damage(38,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_08_burgundian_ash", "Burgundian Pollaxe", [("w_pollaxe_cut_08_burgundian_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1657, weight(2.8)|difficulty(12)|spd_rtng(82)|weapon_length(172)|swing_damage(44,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_08_burgundian_ash", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_08_burgundian_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1657, weight(2.8)|difficulty(12)|spd_rtng(82)|weapon_length(172)|swing_damage(38,blunt)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_08_burgundian_brown", "Burgundian Pollaxe", [("w_pollaxe_cut_08_burgundian_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1657, weight(2.8)|difficulty(12)|spd_rtng(82)|weapon_length(172)|swing_damage(44,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_08_burgundian_brown", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_08_burgundian_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1657, weight(2.8)|difficulty(12)|spd_rtng(82)|weapon_length(172)|swing_damage(38,blunt)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_08_burgundian_red", "Burgundian Pollaxe", [("w_pollaxe_cut_08_burgundian_red",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1657, weight(2.8)|difficulty(12)|spd_rtng(82)|weapon_length(172)|swing_damage(44,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_08_burgundian_red", "Burgundian Pollaxe", [("w_pollaxe_cut_alt_08_burgundian_red",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1657, weight(2.8)|difficulty(12)|spd_rtng(82)|weapon_length(172)|swing_damage(38,blunt)|thrust_damage(37,pierce), imodbits_polearm, [], [fac_no_faction] ],

["w_pollaxe_cut_09_ash", "Pollaxe", [("w_pollaxe_cut_09_ash",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1620, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(165)|swing_damage(45,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_09_ash", "Pollaxe", [("w_pollaxe_cut_alt_09_ash",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1620, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(165)|swing_damage(37,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_09_brown", "Pollaxe", [("w_pollaxe_cut_09_brown",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1620, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(165)|swing_damage(45,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_09_brown", "Pollaxe", [("w_pollaxe_cut_alt_09_brown",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1620, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(165)|swing_damage(37,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],
["w_pollaxe_cut_09_ebony", "Pollaxe", [("w_pollaxe_cut_09_ebony",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1620, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(165)|swing_damage(45,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_pollaxe_cut_alt_09_ebony", "Pollaxe", [("w_pollaxe_cut_alt_09_ebony",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_is_pike, itc_poleaxe, 
1620, weight(2.7)|difficulty(12)|spd_rtng(84)|weapon_length(165)|swing_damage(37,blunt)|thrust_damage(36,pierce), imodbits_polearm, [], [fac_no_faction] ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW LANCES ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################


["w_light_lance",         "Light Lance", [("w_light_lance",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
285 , weight(3)|difficulty(9)|spd_rtng(84) | weapon_length(250)|thrust_damage(25 ,  pierce),imodbits_polearm ],
["w_native_spear_b",         "Light Lance", [("w_native_spear_b",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
214 , weight(2.5)|difficulty(9)|spd_rtng(88) | weapon_length(175)|thrust_damage(27 ,  pierce),imodbits_polearm ],
["w_native_spear_f",         "Light Lance", [("w_native_spear_f",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
224 , weight(2.4)|difficulty(9)|spd_rtng(86) | weapon_length(190)|thrust_damage(29 ,  pierce),imodbits_polearm ],

["w_lance_1", "Lance", [("w_lance_1",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
320, weight(4.4)|difficulty(12)|spd_rtng(82)|weapon_length(267)|swing_damage(35,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_lance_2", "Lance", [("w_lance_2",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
286, weight(4)|difficulty(12)|spd_rtng(85)|weapon_length(226)|swing_damage(31,cut)|thrust_damage(31,pierce), imodbits_polearm ],
["w_lance_3", "Lance", [("w_lance_3",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
307, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(253)|swing_damage(32,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_lance_4", "Lance", [("w_lance_4",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
307, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(253)|swing_damage(32,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_lance_5", "Lance", [("w_lance_5",0)],itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_lance_6", "Lance", [("w_lance_6",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
296, weight(4.3)|difficulty(12)|spd_rtng(83)|weapon_length(241)|swing_damage(30,cut)|thrust_damage(30,pierce), imodbits_polearm ],

["w_lance_colored_english_1", "English Lance", [("w_lance_colored_english_1",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_lance_colored_english_2", "English Lance", [("w_lance_colored_english_2",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_lance_colored_english_3", "English Lance", [("w_lance_colored_english_3",0)],itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
320, weight(4.4)|difficulty(12)|spd_rtng(82)|weapon_length(267)|swing_damage(35,cut)|thrust_damage(35,pierce), imodbits_polearm ],

["w_lance_colored_french_1", "French Lance", [("w_lance_colored_french_1",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_lance_colored_french_2", "French Lance", [("w_lance_colored_french_2",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_lance_colored_french_3", "French Lance", [("w_lance_colored_french_3",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm ],

["w_native_spear_b_custom", "Light Lance with Pennon", [("w_native_spear_b",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
214 , weight(2.5)|difficulty(9)|spd_rtng(88) | weapon_length(175)|thrust_damage(27 ,  pierce),imodbits_polearm,[custom_remodel("itm_w_native_spear_b_custom")]], 
["w_native_spear_f_custom", "Light Lance with Pennon", [("w_native_spear_f",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
224 , weight(2.4)|difficulty(9)|spd_rtng(86) | weapon_length(190)|thrust_damage(29 ,  pierce),imodbits_polearm,[custom_remodel("itm_w_native_spear_f_custom")]], 
["w_light_lance_custom", "Light Lance with Pennon", [("w_light_lance",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
285 , weight(3)|difficulty(9)|spd_rtng(84) | weapon_length(250)|thrust_damage(25 ,  pierce),imodbits_polearm,[custom_remodel("itm_w_light_lance_custom")]], 
### DAC Seek: Some of these lances are in a try-for-range, don't change their order
["w_lance_1_custom", "Lance with Pennon", [("w_lance_1",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
320, weight(4.4)|difficulty(12)|spd_rtng(82)|weapon_length(267)|thrust_damage(35,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_1_custom")]], 
["w_lance_2_custom", "Lance with Pennon", [("w_lance_2",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
286, weight(4)|difficulty(12)|spd_rtng(85)|weapon_length(226)|thrust_damage(31,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_2_custom")]], 
["w_lance_3_custom", "Lance with Pennon", [("w_lance_3",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
307, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(253)|thrust_damage(32,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_3_custom")]], 
["w_lance_4_custom", "Lance with Pennon", [("w_lance_4",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
307, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(253)|thrust_damage(32,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_4_custom")]], 
["w_lance_5_custom", "Lance with Pennon", [("w_lance_5",0)],itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|thrust_damage(34,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_5_custom")]], 
["w_lance_6_custom", "Lance with Pennon", [("w_lance_6",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
296, weight(4.3)|difficulty(12)|spd_rtng(83)|weapon_length(241)|thrust_damage(30,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_6_custom")]], 
["w_lance_colored_english_1_custom", "English Lance with Pennon", [("w_lance_colored_english_1",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|thrust_damage(34,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_colored_english_1_custom")]], 
["w_lance_colored_english_2_custom", "English Lance with Pennon", [("w_lance_colored_english_2",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|thrust_damage(34,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_colored_english_2_custom")]], 
["w_lance_colored_english_3_custom", "English Lance with Pennon", [("w_lance_colored_english_3",0)],itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
320, weight(4.4)|difficulty(12)|spd_rtng(82)|weapon_length(267)|thrust_damage(35,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_colored_english_3_custom")]], 
["w_lance_colored_french_1_custom", "French Lance with Pennon", [("w_lance_colored_french_1",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|thrust_damage(34,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_colored_french_1_custom")]], 
["w_lance_colored_french_2_custom", "French Lance with Pennon", [("w_lance_colored_french_2",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|thrust_damage(34,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_colored_french_2_custom")]], 
["w_lance_colored_french_3_custom", "French Lance with Pennon", [("w_lance_colored_french_3",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|thrust_damage(34,pierce), imodbits_polearm,[custom_remodel("itm_w_lance_colored_french_3_custom")]], 
# DAC Seek: Don't Add items between w_lance_colored_french_3_custom and w_light_lance_heraldic without editing the ranges first

### Heraldic Weapons
["w_light_lance_heraldic",         "Light Lance", [("o_lance_penon_b",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
285 , weight(3)|difficulty(9)|spd_rtng(84) | weapon_length(250)|swing_damage(0 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_light_lance", 0, 0),])]],
["w_native_spear_b_heraldic",         "Light Lance", [("o_lance_penon_c",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
214 , weight(2.5)|difficulty(9)|spd_rtng(88) | weapon_length(175)|swing_damage(0 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_native_spear_b", 0, 0),])]],
["w_native_spear_f_heraldic",         "Light Lance", [("o_lance_penon_c",0)], itp_couchable|itp_type_polearm|itp_has_upper_stab|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry|itp_offset_lance, itc_lance_upstab, 
224 , weight(2.4)|difficulty(9)|spd_rtng(86) | weapon_length(190)|swing_damage(0 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_native_spear_f", 0, 0),])]],

["w_lance_1_heraldic", "Heraldic Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
320, weight(4.4)|difficulty(12)|spd_rtng(82)|weapon_length(267)|swing_damage(35,cut)|thrust_damage(35,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_1", 0, 0),])]],
["w_lance_2_heraldic", "Heraldic Lance", [("o_lance_penon_b",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
286, weight(4)|difficulty(12)|spd_rtng(85)|weapon_length(226)|swing_damage(31,cut)|thrust_damage(31,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_2", 0, 0),])]],
["w_lance_3_heraldic", "Heraldic Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
307, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(253)|swing_damage(32,cut)|thrust_damage(32,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_3", 0, 0),])]],
["w_lance_4_heraldic", "Heraldic Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
307, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(253)|swing_damage(32,cut)|thrust_damage(32,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_4", 0, 0),])]],
["w_lance_5_heraldic", "Heraldic Lance", [("o_lance_penon",0)],itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_5", 0, 0),])]],
["w_lance_6_heraldic", "Heraldic Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
296, weight(4.3)|difficulty(12)|spd_rtng(83)|weapon_length(241)|swing_damage(30,cut)|thrust_damage(30,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_6", 0, 0),])]],

["w_lance_colored_english_1_heraldic", "Heraldic English Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_colored_english_1", 0, 0),])]],
["w_lance_colored_english_2_heraldic", "Heraldic English Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_colored_english_2", 0, 0),])]],
["w_lance_colored_english_3_heraldic", "Heraldic English Lance", [("o_lance_penon",0)],itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
320, weight(4.4)|difficulty(12)|spd_rtng(82)|weapon_length(267)|swing_damage(35,cut)|thrust_damage(35,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_colored_english_3", 0, 0),])]],

["w_lance_colored_french_1_heraldic", "Heraldic French Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_colored_french_1", 0, 0),])]],
["w_lance_colored_french_2_heraldic", "Heraldic French Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_colored_french_2", 0, 0),])]],
["w_lance_colored_french_3_heraldic", "Heraldic French Lance", [("o_lance_penon",0)], itp_couchable|itp_type_polearm|itp_merchandise|itp_is_pike| itp_primary|itp_no_blur|itp_wooden_parry, itc_greatlance, 
308, weight(4.2)|difficulty(12)|spd_rtng(83)|weapon_length(252)|swing_damage(34,cut)|thrust_damage(34,pierce), imodbits_polearm, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_penon", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@w_lance_colored_french_3", 0, 0),])]],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW RANGED ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_short_bow_ash", "Ash Short Bow", [("w_short_bow_ash",0),("w_short_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 42, weight(0.5)|difficulty(0)|spd_rtng(95)|shoot_speed(40)|accuracy(90)|thrust_damage(7,pierce), imodbits_bow ],
["w_short_bow_elm", "Elm Short Bow", [("w_short_bow_elm",0),("w_short_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 50, weight(0.6)|difficulty(0)|spd_rtng(94)|shoot_speed(42)|accuracy(90)|thrust_damage(8,pierce), imodbits_bow ],
["w_short_bow_oak", "Oak Short Bow", [("w_short_bow_oak",0),("w_short_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 58, weight(0.7)|difficulty(1)|spd_rtng(93)|shoot_speed(44)|accuracy(91)|thrust_damage(9,pierce), imodbits_bow ],
["w_short_bow_yew", "Yew Short Bow", [("w_short_bow_yew",0),("w_short_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 66, weight(0.7)|difficulty(1)|spd_rtng(92)|shoot_speed(45)|accuracy(92)|thrust_damage(10,pierce), imodbits_bow ],

["w_hunting_bow_ash", "Ash Hunting Bow", [("w_hunting_bow_ash",0),("w_hunting_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 90, weight(0.8)|difficulty(1)|spd_rtng(90)|shoot_speed(45)|accuracy(92)|thrust_damage(13,pierce), imodbits_bow ],
["w_hunting_bow_elm", "Elm Hunting Bow", [("w_hunting_bow_elm",0),("w_hunting_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 102, weight(0.9)|difficulty(1)|spd_rtng(89)|shoot_speed(48)|accuracy(92)|thrust_damage(14,pierce), imodbits_bow ],
["w_hunting_bow_oak", "Oak Hunting Bow", [("w_hunting_bow_oak",0),("w_hunting_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 124, weight(0.9)|difficulty(2)|spd_rtng(88)|shoot_speed(51)|accuracy(93)|thrust_damage(15,pierce), imodbits_bow ],
["w_hunting_bow_yew", "Yew Hunting Bow", [("w_hunting_bow_yew",0),("w_hunting_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 136, weight(1)|difficulty(2)|spd_rtng(87)|shoot_speed(54)|accuracy(94)|thrust_damage(16,pierce), imodbits_bow ],

["w_war_bow_ash", "Ash War Bow", [("w_war_bow_ash",0),("w_war_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 140, weight(1.2)|difficulty(3)|spd_rtng(85)|shoot_speed(71)|accuracy(95)|thrust_damage(18,pierce), imodbits_bow ],
["w_war_bow_elm", "Elm War Bow", [("w_war_bow_elm",0),("w_war_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 154, weight(1.3)|difficulty(3)|spd_rtng(84)|shoot_speed(76)|accuracy(95)|thrust_damage(19,pierce), imodbits_bow ],
["w_war_bow_oak", "Oak War Bow", [("w_war_bow_oak",0),("w_war_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 168, weight(1.3)|difficulty(3)|spd_rtng(83)|shoot_speed(82)|accuracy(96)|thrust_damage(20,pierce), imodbits_bow ],
["w_war_bow_yew", "Yew War Bow", [("w_war_bow_yew",0),("w_war_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 184, weight(1.4)|difficulty(3)|spd_rtng(82)|shoot_speed(89)|accuracy(97)|thrust_damage(21,pierce), imodbits_bow ],

["w_long_bow_ash", "Ash Long Bow", [("w_long_bow_ash",0),("w_long_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 220, weight(1.4)|difficulty(4)|spd_rtng(80)|shoot_speed(96)|accuracy(97)|thrust_damage(23,pierce), imodbits_bow ],
["w_long_bow_elm", "Elm Long Bow", [("w_long_bow_elm",0),("w_long_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 235, weight(1.5)|difficulty(4)|spd_rtng(79)|shoot_speed(104)|accuracy(97)|thrust_damage(24,pierce), imodbits_bow ],
["w_long_bow_oak", "Oak Long Bow", [("w_long_bow_oak",0),("w_long_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 250, weight(1.5)|difficulty(5)|spd_rtng(78)|shoot_speed(115)|accuracy(97)|thrust_damage(25,pierce), imodbits_bow ],
["w_long_bow_yew", "Yew Long Bow", [("w_long_bow_yew",0),("w_long_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_bow|itcf_carry_bow_back,
 265, weight(1.6)|difficulty(5)|spd_rtng(77)|shoot_speed(121)|accuracy(96)|thrust_damage(26,pierce), imodbits_bow ],

["w_crossbow_hunting", "Hunting Crossbow", [("w_crossbow_hunting",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
88, weight(2.25)|difficulty(0)|spd_rtng(78)|shoot_speed(81)|accuracy(93)|thrust_damage(44,pierce)|max_ammo(1), imodbits_crossbow ],
["w_crossbow_light", "Light Crossbow", [("w_crossbow_light",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
132, weight(2.5)|difficulty(8)|spd_rtng(74)|shoot_speed(92)|accuracy(94)|thrust_damage(48,pierce)|max_ammo(1), imodbits_crossbow ],
["w_crossbow_cavalry", "Cavalry Crossbow", [("w_crossbow_cavalry",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
184, weight(2.5)|difficulty(8)|spd_rtng(72)|shoot_speed(96)|accuracy(95)|thrust_damage(50,pierce)|max_ammo(1), imodbits_crossbow ],
["w_crossbow_medium", "Crossbow", [("w_crossbow_medium",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
218, weight(3)|difficulty(9)|spd_rtng(70)|shoot_speed(112)|accuracy(96)|thrust_damage(54,pierce)|max_ammo(1), imodbits_crossbow ],
["w_crossbow_heavy", "Heavy Crossbow", [("w_crossbow_heavy",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
349, weight(3.5)|difficulty(10)|spd_rtng(66)|shoot_speed(125)|accuracy(97)|thrust_damage(56,pierce)|max_ammo(1), imodbits_crossbow ],
["w_crossbow_siege", "Siege Crossbow", [("w_crossbow_siege",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_no_blur, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683, weight(3.75)|difficulty(11)|spd_rtng(60)|shoot_speed(128)|accuracy(98)|thrust_damage(62,pierce)|max_ammo(1), imodbits_crossbow ],


["w_handgonne_1", "Handgonne", [("w_handgonne_1",0)], itp_type_musket|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
1850, weight(4.5)|abundance(90)|difficulty(0)|spd_rtng(16)|shoot_speed(160)|thrust_damage(100,pierce)|max_ammo(1)|accuracy(95), imodbits_none, [(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,95),(particle_system_burst,"psys_pistol_smoke",pos1,15),(particle_system_burst,"psys_pistol_fire",pos1,15)])] ],
["w_handgonne_2", "Handgonne", [("w_handgonne_2",0)], itp_type_musket|itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
2230, weight(3.8)|abundance(90)|difficulty(0)|spd_rtng(20)|shoot_speed(180)|thrust_damage(120,pierce)|max_ammo(1)|accuracy(98), imodbits_none, [(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,107),(particle_system_burst,"psys_pistol_smoke",pos1,15),(particle_system_burst,"psys_pistol_fire",pos1,15)])] ],

# Piercing Arrows
["w_arrow_triangular", "Arrows", [("w_arrow_triangular",0),("w_arrow_triangular",ixmesh_flying_ammo),("w_arrow_quiver_triangular",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back_right, 
72, weight(3)|abundance(100)|weapon_length(102)|thrust_damage(12,pierce)|max_ammo(30), imodbits_missile ],
["w_arrow_triangular_large", "Large Arrows", [("w_arrow_triangular_large",0),("w_arrow_triangular_large",ixmesh_flying_ammo),("w_arrow_quiver_triangular_large",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back_right, 
104, weight(3.5)|abundance(100)|weapon_length(104)|thrust_damage(16,pierce)|max_ammo(30), imodbits_missile ],
["w_arrow_bodkin", "Bodkin Arrows", [("w_arrow_bodkin",0),("w_arrow_bodkin",ixmesh_flying_ammo),("w_arrow_quiver_bodkin",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back_right, 
162, weight(3)|abundance(80)|weapon_length(104)|thrust_damage(20,pierce)|max_ammo(30), imodbits_missile ],
# Cutting Arrows
["w_arrow_broadhead", "Broadhead Arrows", [("w_arrow_broadhead",0),("w_arrow_broadhead",ixmesh_flying_ammo),("w_arrow_quiver_broadhead",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 
98, weight(4)|abundance(100)|weapon_length(103)|thrust_damage(14,cut)|max_ammo(30), imodbits_missile ],
["w_arrow_broadhead_large", "Large Broadhead Arrows", [("w_arrow_broadhead_large",0),("w_arrow_broadhead_large",ixmesh_flying_ammo),("w_arrow_quiver_broadhead_large",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 
146, weight(4.5)|abundance(100)|weapon_length(104)|thrust_damage(18,cut)|max_ammo(30), imodbits_missile ],
# Blunt Arrows
["w_arrow_blunt", "Blunt Arrows", [("w_arrow_blunt",0),("w_arrow_blunt",ixmesh_flying_ammo),("w_arrow_quiver_blunt",ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back, 
86, weight(5)|abundance(100)|weapon_length(98)|thrust_damage(12,blunt)|max_ammo(30), imodbits_missile ],

# Piercing Bolts
["w_bolt_triangular", "Bolts", [("w_bolt_triangular",0),("w_bolt_triangular",ixmesh_flying_ammo),("w_bolt_quiver_triangular",ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,
 64, weight(2.25)|abundance(90)|weapon_length(73)|thrust_damage(10,pierce)|max_ammo(30), imodbits_missile ],
["w_bolt_triangular_large", "Bolts", [("w_bolt_triangular_large",0),("w_bolt_triangular_large",ixmesh_flying_ammo),("w_bolt_quiver_triangular_large",ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,
 100, weight(2.25)|abundance(90)|weapon_length(75)|thrust_damage(14,pierce)|max_ammo(28), imodbits_missile ],
["w_bolt_bodkin", "Bodkin Bolts", [("w_bolt_bodkin",0),("w_bolt_bodkin",ixmesh_flying_ammo),("w_bolt_quiver_bodkin",ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,
 125, weight(2.25)|abundance(90)|weapon_length(74)|thrust_damage(18,pierce)|max_ammo(25), imodbits_missile ],
# Cutting Bolts
["w_bolt_boar", "Boar Bolts", [("w_bolt_boar",0),("w_bolt_boar",ixmesh_flying_ammo),("w_bolt_quiver_boar",ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,
 92, weight(3)|abundance(90)|weapon_length(73)|thrust_damage(12,cut)|max_ammo(24), imodbits_missile ],
["w_bolt_broadhead", "Broadhead Bolts", [("w_bolt_broadhead",0),("w_bolt_broadhead",ixmesh_flying_ammo),("w_bolt_quiver_broadhead",ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,
 118, weight(3)|abundance(90)|weapon_length(73)|thrust_damage(16,cut)|max_ammo(22), imodbits_missile ],


["cartridges","Bullets", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_no_blur ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],
["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_no_blur ,itcf_throw_knife, 76 , weight(3.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_no_blur ,itcf_throw_knife, 193 , weight(3.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],

["dedal_kufel","Kufel",[("dedal_kufelL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lutnia","Lutnia",[("dedal_lutniaL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lira","Lira",[("dedal_liraL",0)],		itp_type_hand_armor,0,0,weight(1),0],
["torch_hands","Torch",[("torch_hands_L",0)],		itp_type_hand_armor,0,0,weight(1),0],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW SHIELDS ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### Regular shields
### Tall Pavises
["s_tall_pavise_french_1", "Pavise Shield",   [("s_tall_pavise_french_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_french_2", "Pavise Shield",   [("s_tall_pavise_french_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_french_3", "Pavise Shield",   [("s_tall_pavise_french_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_french_4", "Pavise Shield",   [("s_tall_pavise_french_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_french_5", "Pavise Shield",   [("s_tall_pavise_french_5" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

["s_tall_pavise_genoese_1", "Pavise Shield",   [("s_tall_pavise_genoese_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_genoese_2", "Pavise Shield",   [("s_tall_pavise_genoese_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

["s_tall_pavise_breton_1", "Pavise Shield",   [("s_tall_pavise_breton_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_breton_2", "Pavise Shield",   [("s_tall_pavise_breton_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_breton_3", "Pavise Shield",   [("s_tall_pavise_breton_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

["s_tall_pavise_burgundian_1", "Pavise Shield",   [("s_tall_pavise_burgundian_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_burgundian_2", "Pavise Shield",   [("s_tall_pavise_burgundian_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_burgundian_3", "Pavise Shield",   [("s_tall_pavise_burgundian_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_burgundian_4", "Pavise Shield",   [("s_tall_pavise_burgundian_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_burgundian_5", "Pavise Shield",   [("s_tall_pavise_burgundian_5" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

["s_tall_pavise_german_1", "Pavise Shield",   [("s_tall_pavise_german_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_german_2", "Pavise Shield",   [("s_tall_pavise_german_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_tall_pavise_german_3", "Pavise Shield",   [("s_tall_pavise_german_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

# Pavises
["s_pavise_native_french_1", "Pavise Shield",   [("s_pavise_native_french_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_pavise_native_french_2", "Pavise Shield",   [("s_pavise_native_french_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_pavise_native_french_3", "Pavise Shield",   [("s_pavise_native_french_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_pavise_native_french_4", "Pavise Shield",   [("s_pavise_native_french_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

["s_pavise_native_burgundian_1", "Pavise Shield",   [("s_pavise_native_burgundian_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_pavise_native_burgundian_2", "Pavise Shield",   [("s_pavise_native_burgundian_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_pavise_native_burgundian_3", "Pavise Shield",   [("s_pavise_native_burgundian_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],
["s_pavise_native_burgundian_4", "Pavise Shield",   [("s_pavise_native_burgundian_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield],

["s_pavise_native_breton_1", "Pavise Shield",   [("s_pavise_native_breton_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(100),imodbits_shield],
["s_pavise_native_breton_2", "Pavise Shield",   [("s_pavise_native_breton_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(100),imodbits_shield],
["s_pavise_native_breton_3", "Pavise Shield",   [("s_pavise_native_breton_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(100),imodbits_shield],

["s_pavise_native_genoese_1", "Pavise Shield",   [("s_pavise_native_genoese_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
550 , weight(4.5)|hit_points(660)|body_armor(10)|spd_rtng(82)|shield_width(55)|shield_height(100),imodbits_shield],


["s_pavise_french_1", "Pavise Shield",   [("s_pavise_french_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_french_2", "Pavise Shield",   [("s_pavise_french_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_french_3", "Pavise Shield",   [("s_pavise_french_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_french_4", "Pavise Shield",   [("s_pavise_french_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],

["s_pavise_burgundian_1", "Pavise Shield",   [("s_pavise_burgundian_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_burgundian_2", "Pavise Shield",   [("s_pavise_burgundian_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_burgundian_3", "Pavise Shield",   [("s_pavise_burgundian_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_burgundian_4", "Pavise Shield",   [("s_pavise_burgundian_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],

["s_pavise_flemish_1", "Pavise Shield",   [("s_pavise_flemish_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_flemish_2", "Pavise Shield",   [("s_pavise_flemish_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_flemish_3", "Pavise Shield",   [("s_pavise_flemish_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_flemish_4", "Pavise Shield",   [("s_pavise_flemish_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],

["s_pavise_breton_1", "Pavise Shield",   [("s_pavise_breton_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_breton_2", "Pavise Shield",   [("s_pavise_breton_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_pavise_breton_3", "Pavise Shield",   [("s_pavise_breton_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],


["s_hand_pavise_french_1", "Hand-Pavise Shield",   [("s_hand_pavise_a_04" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_french_2", "Hand-Pavise Shield",   [("s_hand_pavise_a_05" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_french_3", "Hand-Pavise Shield",   [("s_hand_pavise_a_06" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],

["s_hand_pavise_burgundian_1", "Hand-Pavise Shield",   [("s_hand_pavise_a_01" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_burgundian_2", "Hand-Pavise Shield",   [("s_hand_pavise_a_02" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_burgundian_3", "Hand-Pavise Shield",   [("s_hand_pavise_a_03" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],

["s_hand_pavise_breton_1", "Hand-Pavise Shield",   [("s_hand_pavise_a_07" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_breton_2", "Hand-Pavise Shield",   [("s_hand_pavise_a_08" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_breton_3", "Hand-Pavise Shield",   [("s_hand_pavise_a_09" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],

["s_hand_pavise_german_1", "Hand-Pavise Shield",   [("s_hand_pavise_a_10" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],
["s_hand_pavise_german_2", "Hand-Pavise Shield",   [("s_hand_pavise_a_11" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
420 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield],


#################################### Heater Shields
["s_heraldic_shield_french_1", "Heraldic Shield",   [("s_heraldic_shield_french_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_french_2", "Heraldic Shield",   [("s_heraldic_shield_french_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_french_3", "Heraldic Shield",   [("s_heraldic_shield_french_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_french_4", "Heraldic Shield",   [("s_heraldic_shield_french_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_french_5", "Heraldic Shield",   [("s_heraldic_shield_french_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_french_6", "Heraldic Shield",   [("s_heraldic_shield_french_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_french_7", "Heraldic Shield",   [("s_heraldic_shield_french_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],

["s_heraldic_shield_english_1", "Heraldic Shield",   [("s_heraldic_shield_english_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_english_2", "Heraldic Shield",   [("s_heraldic_shield_english_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_english_3", "Heraldic Shield",   [("s_heraldic_shield_english_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_english_4", "Heraldic Shield",   [("s_heraldic_shield_english_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_english_5", "Heraldic Shield",   [("s_heraldic_shield_english_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_english_6", "Heraldic Shield",   [("s_heraldic_shield_english_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_english_7", "Heraldic Shield",   [("s_heraldic_shield_english_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],

["s_heraldic_shield_burgundian_1", "Heraldic Shield",   [("s_heraldic_shield_burgundian_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_burgundian_2", "Heraldic Shield",   [("s_heraldic_shield_burgundian_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_burgundian_3", "Heraldic Shield",   [("s_heraldic_shield_burgundian_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_burgundian_4", "Heraldic Shield",   [("s_heraldic_shield_burgundian_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_burgundian_5", "Heraldic Shield",   [("s_heraldic_shield_burgundian_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_burgundian_6", "Heraldic Shield",   [("s_heraldic_shield_burgundian_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_burgundian_7", "Heraldic Shield",   [("s_heraldic_shield_burgundian_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],

["s_heraldic_shield_breton_1", "Heraldic Shield",   [("s_heraldic_shield_breton_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_breton_2", "Heraldic Shield",   [("s_heraldic_shield_breton_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_breton_3", "Heraldic Shield",   [("s_heraldic_shield_breton_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_breton_4", "Heraldic Shield",   [("s_heraldic_shield_breton_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_breton_5", "Heraldic Shield",   [("s_heraldic_shield_breton_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_breton_6", "Heraldic Shield",   [("s_heraldic_shield_breton_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_breton_7", "Heraldic Shield",   [("s_heraldic_shield_breton_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],

["s_heraldic_shield_german_1", "Heraldic Shield",   [("s_heraldic_shield_german_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_german_2", "Heraldic Shield",   [("s_heraldic_shield_german_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_german_3", "Heraldic Shield",   [("s_heraldic_shield_german_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_german_4", "Heraldic Shield",   [("s_heraldic_shield_german_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_german_5", "Heraldic Shield",   [("s_heraldic_shield_german_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_german_6", "Heraldic Shield",   [("s_heraldic_shield_german_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],
["s_heraldic_shield_german_7", "Heraldic Shield",   [("s_heraldic_shield_german_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
340 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield],


["s_heater_shield_french_1", "Heater Shield",   [("s_heater_shield_french_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_2", "Heater Shield",   [("s_heater_shield_french_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_3", "Heater Shield",   [("s_heater_shield_french_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_4", "Heater Shield",   [("s_heater_shield_french_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_5", "Heater Shield",   [("s_heater_shield_french_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_6", "Heater Shield",   [("s_heater_shield_french_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_7", "Heater Shield",   [("s_heater_shield_french_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_french_8", "Heater Shield",   [("s_heater_shield_french_8" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_1", "Heater Shield",   [("s_heater_shield_english_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_2", "Heater Shield",   [("s_heater_shield_english_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_3", "Heater Shield",   [("s_heater_shield_english_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_4", "Heater Shield",   [("s_heater_shield_english_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_5", "Heater Shield",   [("s_heater_shield_english_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_6", "Heater Shield",   [("s_heater_shield_english_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_7", "Heater Shield",   [("s_heater_shield_english_7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_english_8", "Heater Shield",   [("s_heater_shield_english_8" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_burgundian_1", "Heater Shield",   [("s_heater_shield_burgundian_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_burgundian_2", "Heater Shield",   [("s_heater_shield_burgundian_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_burgundian_3", "Heater Shield",   [("s_heater_shield_burgundian_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_burgundian_4", "Heater Shield",   [("s_heater_shield_burgundian_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_burgundian_5", "Heater Shield",   [("s_heater_shield_burgundian_5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_burgundian_6", "Heater Shield",   [("s_heater_shield_burgundian_6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_breton_1", "Heater Shield",   [("s_heater_shield_breton_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_breton_2", "Heater Shield",   [("s_heater_shield_breton_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_breton_3", "Heater Shield",   [("s_heater_shield_breton_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],
["s_heater_shield_breton_4", "Heater Shield",   [("s_heater_shield_breton_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
220 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield],

["s_steel_buckler", "Steel Buckler", [("s_steel_buckler",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  
180 , weight(1.1)|hit_points(115)|body_armor(40)|spd_rtng(100)|shield_width(33),imodbits_shield ],
["s_steel_buckler_2", "Steel Buckler", [("s_steel_buckler_2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  
195 , weight(1.2)|hit_points(135)|body_armor(40)|spd_rtng(100)|shield_width(30)|shield_height(45),imodbits_shield ],

### Heraldic Shields
["s_heraldic_shield_heater", "Heraldic Heater Shield",   [("s_heraldic_shield_heater" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
260 , weight(1.6)|hit_points(400)|body_armor(22)|spd_rtng(94)|shield_width(48)|shield_height(85),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_heraldic", ":agent_no", ":troop_no")])]],

["s_heraldic_shield_bouche", "Heraldic Bouche Shield",   [("s_heraldic_shield_bouche" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
440 , weight(2)|hit_points(260)|body_armor(26)|spd_rtng(90)|shield_width(40)|shield_height(65),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_shield_bouche", ":agent_no", ":troop_no")])]],

["s_heraldic_shield_leather", "Heraldic Shield",   [("s_heraldic_shield_leather" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
380 , weight(2.2)|hit_points(350)|body_armor(25)|spd_rtng(92)|shield_width(50)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_shield_leather", ":agent_no", ":troop_no")])]],
["s_heraldic_shield_metal", "Heraldic Shield",   [("s_heraldic_shield_metal" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
420 , weight(2.4)|hit_points(350)|body_armor(28)|spd_rtng(91)|shield_width(50)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_shield_metal", ":agent_no", ":troop_no")])]],

["s_heraldic_shield_pavise", "Heraldic Pavise Shield",   [("s_heraldic_shield_pavise" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
460 , weight(3.5)|hit_points(380)|body_armor(30)|spd_rtng(86)|shield_width(45)|shield_height(85),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_shield_pavise", ":agent_no", ":troop_no")])]],

["s_heraldic_shield_pavise_native", "Heraldic Pavise Shield",   [("s_heraldic_shield_pavise_native" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
590 , weight(4.5)|hit_points(660)|body_armor(32)|spd_rtng(82)|shield_width(55)|shield_height(120),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_shield_pavise_native", ":agent_no", ":troop_no")])]],

["heraldic_banner", "Heraldic Banner", [("heraldic_banner" ,0),("heraldic_banner_inventory", ixmesh_inventory)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
1500 , weight(3)|hit_points(999)|body_armor(4)|spd_rtng(88)|shield_width(1)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_banner", ":agent_no", ":troop_no"),(cur_item_add_mesh, "@heraldic_banner_base", 0, 0),])]],

#SB : replace items_end to fit invasion items
["items_end", "Items End", [("w_war_bow_ash",0)], 0, 0, 1, 0, 0],

# Special Items
# TLD Chains
["feet_chains","Feet Chains",[("chains_full",0)],itp_type_foot_armor|itp_attach_armature,0,200,weight(10)|leg_armor(0)|difficulty(0),imodbits_none],

["a_plate_joan", "Jeanne's Plate Armour", [("a_kastenbrust_mail",0)], itp_type_body_armor|itp_covers_legs, 0, 9000, weight(29)|abundance(100)|head_armor(0)|body_armor(70)|leg_armor(28)|difficulty(12), imodbits_armor ],


]
