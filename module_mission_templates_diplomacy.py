from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_items import *
from header_skills import *
from module_constants import *
from module_mission_templates_form import *
from compiler import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################

##diplomacy begin

unarmed_agent_damage = (
  ti_on_agent_hit, 0, 0,
  [
    (eq, reg0, -1), #unarmed/fists damage
    (store_trigger_param_2, ":attacker"),
    (agent_get_troop_id, ":troop_no", ":attacker"),
    (troop_is_hero, ":troop_no"), #bots normally do not punch/kick
    #should probably do distance check for close-range vs delivered damage?
  ],
  [
    # (store_trigger_param_1, ":defender"),
    (store_trigger_param_2, ":attacker"),
    (store_trigger_param_3, ":damage"),
    # (gt, ":damage", 0), #not a glance
    
    # (agent_get_attack_action, ":action", ":attacker"),
    (agent_get_animation, ":animation1", ":attacker", 0), #lower body
    # (agent_get_animation, ":animation2", ":attacker",1),
    (assign, ":armor", 0), #used for the base damage
    (assign, ":weight", 0), #modifier
    (try_begin), #kicks
      (eq, ":animation1", "anim_kick_right_leg"),
      (agent_get_item_slot, ":item_no", ":attacker", ek_foot),
      (gt, ":item_no", -1),
      (item_get_leg_armor, ":armor", ":item_no"),
      (item_get_weight, ":weight", ":item_no"),
      (val_div, ":armor", 3),
      (store_div, ":offset", 500, ":weight"),
      (val_sub, ":armor", ":offset"),
    (else_try), #punches (without weapon wielded)
      (agent_get_wielded_item, ":weapon", ":attacker", 0),
      (eq, ":weapon", -1),
      (agent_get_item_slot, ":item_no", ":attacker", ek_gloves),
      (gt, ":item_no", -1),
      (item_get_body_armor, ":armor", ":item_no"),
      (item_get_weight, ":weight", ":item_no"),
      (val_sub, ":armor", 2), #leather glove base
      (val_mul, ":armor", ":weight"), #weight of 1 = 100
      (val_div, ":armor", 100),
    (try_end),
    #get item modifiers from troop?
    #add ironflesh/athletics skill bonus?
    (val_clamp, ":armor", 0, 10), #not too much damage
    (val_add, ":damage", ":armor"),
    # (assign, reg1, ":armor"),
    # (assign, reg2, ":weight"),
    # (display_message, "@{reg1} armor {reg2} weight"),
    (store_trigger_param_3, ":original_damage"),
    (neq, ":original_damage", ":damage"),
    (set_trigger_result, ":damage"),
    
  ],
)

dplmc_random_mixed_gender = (ti_on_agent_spawn, 0, 0, [
  (ge, "$g_disable_condescending_comments", 4),
],
  [
  (store_trigger_param_1, ":agent_no"),
  (agent_is_human, ":agent_no"),
  (agent_get_troop_id, ":troop_no", ":agent_no"),
  (neg|troop_is_hero, ":troop_no"),
  (neg|is_between, ":troop_no", "trp_follower_woman", "trp_caravan_master"), #always female
  #SB : check non-native troop genders

  #get individual faction chances
  (store_faction_of_troop, ":faction_no", ":troop_no"),
  (try_begin), #TODO: this affects the next agent to spawn as well if custom ratio skewed too high
    (agent_get_party_id, ":party_no", ":agent_no"),
    (party_is_active, ":party_no"),
    (store_faction_of_party, ":party_faction", ":party_no"),
    # (eq, ":party_faction", "$players_kingdom"),
    (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
    (ge, reg0, DPLMC_FACTION_STANDING_LEADER),
    (assign, ":faction_no", "fac_player_supporters_faction"),
  (try_end),
  (faction_get_slot, ":ratio", ":faction_no", slot_faction_gender_ratio),
  (store_random_in_range, ":gender", -100, ":ratio"),
  (try_begin),
    (le, ":gender", 0),
    (troop_set_type, ":troop_no", tf_male),
  (else_try),
    (troop_set_type, ":troop_no", tf_female),
  (try_end),
  
  ])

dplmc_horse_cull = [
    #sets up the spawn timer
    (ti_on_agent_spawn, 0, 0, 
      [ (this_or_next|multiplayer_is_server),
        (neg|game_in_multiplayer_mode),
        (store_trigger_param_1, ":agent_no"),
        (neg|agent_is_human, ":agent_no"), #horse agent
        ],
      [ (store_trigger_param_1, ":horse_no"),
        # (store_trigger_param_2, ":horse_no"),
     
        (agent_get_rider, ":agent_no", ":horse_no"),
        (try_begin),
          (agent_is_non_player, ":agent_no"), #default period for npcs
          (agent_set_slot, ":horse_no", slot_agent_bought_horse, 0), #default duration
        (else_try),
          (agent_set_slot, ":horse_no", slot_agent_bought_horse, 210),
        (try_end),
        # (str_store_agent_name, s1, ":agent_no"),
        # (agent_get_item_id, ":horse_id", ":horse_no"),
        # (str_store_item_name, s2, ":horse_id"),
        # (display_message, "@{s1} spawned on {s2}"),
      ]),
    #restart it when horses are mounted again
    (ti_on_agent_mount, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode)],
      [ (store_trigger_param_1, ":agent_no"),
        (store_trigger_param_2, ":horse_no"),
     
        (try_begin),
          (agent_is_non_player, ":agent_no"), #default period for npcs
          (agent_set_slot, ":horse_no", slot_agent_bought_horse, 0), #reset the timer
        (else_try),
          (agent_set_slot, ":horse_no", slot_agent_bought_horse, 210), #couple minutes longer for players
        (try_end),
        # (str_store_agent_name, s1, ":agent_no"),
        # (agent_get_item_id, ":horse_id", ":horse_no"),
        # (str_store_item_name, s2, ":horse_id"),
        # (display_message, "@{s1} mounted {s2}"),
      ]),
    #the main "workhorse" of the trigger, set to intervals of 5/10/30 or have a server setting
    (10, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode),(eq, "$g_dplmc_horse_speed", 0),],
      [
        (set_fixed_point_multiplier, 1000),
        (try_begin),
          (neg|game_in_multiplayer_mode),
          (assign, ":horse_cull", 30),
        (else_try), #re-use some global
          (assign, ":horse_cull", "$g_horses_are_avaliable"),
        (try_end),
        (try_for_agents, ":horse_no"),
          (agent_is_alive, ":horse_no"),
          (neg|agent_is_human, ":horse_no"),
          (agent_get_rider, ":rider_no", ":horse_no"),
          (lt, ":rider_no", 0),
          (agent_get_slot, ":horse_timer", ":horse_no", slot_agent_bought_horse),
          # (str_store_agent_name, s2, ":horse_no"),
          # (assign, reg2, ":horse_timer"),
          # (display_message, "@{s2} at {reg2} seconds"),
          (try_begin),
            (le, ":horse_timer", -90), #a minute and a half
            #add in a try_for_agent loop so players chasing horses won't be pissed off when it despawns
            (agent_get_position, pos1, ":horse_no"),
            (assign, ":player_agent", -1),
            #better way is to actually check player agent (SP) or iterate through all player_get_agent_id (MP)
            (try_for_agents, ":agent_no", pos1, 5000), #5 meter radius
              (neq, ":agent_no", ":horse_no"),
              (eq, ":player_agent", -1),
              (neg|agent_is_non_player, ":agent_no"),
              (agent_is_alive, ":agent_no"),
              (agent_is_human, ":agent_no"),
              (agent_get_horse, ":player_horse", ":agent_no"),
              (lt, ":player_horse", 0), #dismounted, needs a new one or just want meatshields
              (assign, ":player_agent", ":agent_no"),
            (try_end),
            (eq, ":player_agent", -1), #nobody (important) nearby
            (agent_fade_out, ":horse_no"),
          (else_try),
            (val_sub, ":horse_timer", ":horse_cull"),
            (agent_set_slot, ":horse_no", slot_agent_bought_horse, ":horse_timer"),
            (try_begin), #force runaway half-way through
              (le, ":horse_timer", -60),
              (agent_start_running_away, ":horse_no"),
            (try_end),
          (try_end),
        (try_end),
      ]),

]
dplmc_horse_speed = (
  1, 0, 0, [(eq, "$g_dplmc_horse_speed", 0),],
  [
  (try_for_agents, ":agent_no"),
    (agent_is_alive, ":agent_no"),
    (agent_is_human, ":agent_no"),
    (agent_get_horse, ":horse_agent", ":agent_no"),
    (try_begin),
      (ge, ":horse_agent", 0),
      (store_agent_hit_points, ":horse_hp",":horse_agent"),
      (store_sub, ":lost_hp", 100, ":horse_hp"),
      (try_begin),
        (le, ":lost_hp", 15),
        (val_div, ":lost_hp", 2),
        (store_add, ":speed_factor", 100, ":lost_hp"),
      (else_try),
        (val_mul, ":lost_hp", 2),
        (val_div, ":lost_hp", 3),
        (store_sub, ":speed_factor", 115, ":lost_hp"),
      (try_end),
      (agent_get_troop_id, ":agent_troop", ":agent_no"),
      (store_skill_level, ":skl_level", skl_riding, ":agent_troop"),
      (store_mul, ":speed_multi", ":skl_level", 2),
      (val_add, ":speed_multi", 100),
      (val_mul, ":speed_factor", ":speed_multi"),
      (val_div, ":speed_factor", 100),
      (agent_set_horse_speed_factor, ":agent_no", ":speed_factor"),
    (try_end),
  (try_end),
  ])

#alternate mouse camera
##BEAN BEGIN - Deathcam

common_move_deathcam = (
    0, 0, 0,
    [
        (eq, "$g_dplmc_cam_activated", camera_mouse),
        (this_or_next|game_key_is_down, gk_move_forward),
        (this_or_next|game_key_is_down, gk_move_backward),
        (this_or_next|game_key_is_down, gk_move_left),
        (this_or_next|game_key_is_down, gk_move_right),
        (this_or_next|key_is_down, "$g_cam_tilt_left"),
        (this_or_next|key_is_down, "$g_cam_tilt_right"),
        (this_or_next|key_is_down, "$g_camera_adjust_sub"),
        (this_or_next|key_is_down, "$g_camera_adjust_add"),
        (this_or_next|key_clicked, key_home),
        (game_key_is_down, gk_zoom),
    ],
    [
        (set_fixed_point_multiplier, 10000),
        (mission_cam_get_position, pos47),

        # (try_begin),
        # (key_clicked, key_home),
            # (position_set_x, pos47, "$deathcam_death_pos_x"),
            # (position_set_y, pos47, "$deathcam_death_pos_y"),
            # (position_set_z, pos47, "$deathcam_death_pos_z"),
        # (try_end),

        (assign, ":move_x", 0),
        (assign, ":move_y", 0),
        (assign, ":move_z", 0),

        (try_begin),
          (game_key_is_down, gk_move_forward),
          (val_add, ":move_y", 10),
        (else_try),
          (game_key_is_down, gk_move_backward),
          (val_add, ":move_y", -10),
        (try_end),

        (try_begin),
          (game_key_is_down, gk_move_right),
          (val_add, ":move_x", 10),
        (else_try),
          (game_key_is_down, gk_move_left),
          (val_add, ":move_x", -10),
        (try_end),

        (try_begin),
          (key_is_down, "$g_camera_adjust_add"),
          (val_add, ":move_z", 10),
        (else_try),
          (key_is_down, "$g_camera_adjust_sub"),
          (val_add, ":move_z", -10),
        (try_end),

        (try_begin),
          (game_key_is_down, gk_zoom),
          (val_mul, ":move_x", 4),
          (val_mul, ":move_y", 4),
          (val_mul, ":move_z", 2),
        (try_end),

        # (try_begin),
        # (key_is_down, key_end),
            # (try_begin),
            # (eq, "$deathcam_flip_y_multiplier", 1),
                # (assign, "$deathcam_flip_y_multiplier", -1),
                # (display_message, "@Y-Rotation Inverted"),
            # (else_try),
                # (assign, "$deathcam_flip_y_multiplier", 1),
                # (display_message, "@Y-Rotation Normal"),
            # (try_end),
        # (try_end),

        (position_move_x, pos47, ":move_x"),
        (position_move_y, pos47, ":move_y"),
        (position_move_z, pos47, ":move_z"),

        (mission_cam_set_position, pos47),

        (try_begin),
          (key_is_down, "$g_cam_tilt_left"),
          (ge, "$deathcam_sensitivity_x", 4), #Negative check.
          (ge, "$deathcam_sensitivity_y", 3),
          (val_sub, "$deathcam_sensitivity_x", 4),
          (val_sub, "$deathcam_sensitivity_y", 3),
          (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
          (store_mod, reg7, "$deathcam_sensitivity_y", 75),
          (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
            (assign, reg8, "$deathcam_sensitivity_x"),
            (assign, reg9, "$deathcam_sensitivity_y"),
            (display_message, "@Sensitivity - 25% ({reg8}, {reg9})"),
          (try_end),
        (else_try),
          (key_is_down, "$g_cam_tilt_right"),
          (val_add, "$deathcam_sensitivity_x", 4),
          (val_add, "$deathcam_sensitivity_y", 3),
          (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
          (store_mod, reg7, "$deathcam_sensitivity_y", 75),
          (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
            (assign, reg8, "$deathcam_sensitivity_x"),
            (assign, reg9, "$deathcam_sensitivity_y"),
            (display_message, "@Sensitivity + 25% ({reg8}, {reg9})"),
          (try_end),
      (try_end),
   ]
)

common_rotate_deathcam = (
    0, 0, 0,
    [
        (eq, "$g_dplmc_cam_activated", camera_mouse),
    ],
    [
        (set_fixed_point_multiplier, 10000), #Extra Precision

        (try_begin),
            (this_or_next|is_presentation_active, "prsnt_battle"), #Opened (mouse must move)
            (this_or_next|key_clicked, key_escape), #Menu
            (this_or_next|key_clicked, key_q), #Notes, etc
            (key_clicked, key_tab), #Retreat
            (eq, "$deathcam_prsnt_was_active", 0),
            (assign, "$deathcam_prsnt_was_active", 1),
            (assign, "$deathcam_mouse_last_notmoved_x", "$deathcam_mouse_notmoved_x"),
            (assign, "$deathcam_mouse_last_notmoved_y", "$deathcam_mouse_notmoved_y"),
        (try_end),

        (assign, ":continue", 0),

        (try_begin),
            (neg|is_presentation_active, "prsnt_battle"),
            (mouse_get_position, pos1), #Get and set mouse position
            (position_get_x, reg1, pos1),
            (position_get_y, reg2, pos1),

            (mission_cam_get_position, pos47),

            (try_begin),
            (neq, "$deathcam_prsnt_was_active", 1),
                (try_begin), #Check not moved
                (eq, reg1, "$deathcam_mouse_last_x"),
                (eq, reg2, "$deathcam_mouse_last_y"),
                (this_or_next|neq, reg1, "$deathcam_mouse_notmoved_x"),
                (neq, reg2, "$deathcam_mouse_notmoved_y"),
                    (val_add, "$deathcam_mouse_notmoved_counter", 1),
                    (try_begin), #Notmoved for n cycles
                    (ge, "$deathcam_mouse_notmoved_counter", 15),
                        (assign, "$deathcam_mouse_notmoved_counter", 0),
                        (assign, "$deathcam_mouse_notmoved_x", reg1),
                        (assign, "$deathcam_mouse_notmoved_y", reg2),
                    (try_end),
                (else_try), #Has moved
                    (assign, ":continue", 1),
                    (assign, "$deathcam_mouse_notmoved_counter", 0),
                (try_end),
                (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                (assign, "$deathcam_mouse_last_y", reg2),
            (else_try), #prsnt was active
                (try_begin),
                (neq, reg1, "$deathcam_mouse_last_x"), #Is moving
                (neq, reg2, "$deathcam_mouse_last_y"),
                    (store_sub, ":delta_x2", reg1, "$deathcam_mouse_last_notmoved_x"), #Store pos difference
                    (store_sub, ":delta_y2", reg2, "$deathcam_mouse_last_notmoved_y"),
                (is_between, ":delta_x2", -10, 11), #when engine recenters mouse, there is a small gap
                (is_between, ":delta_y2", -10, 11), #usually 5 pixels, but did 10 to be safe.
                    (assign, "$deathcam_prsnt_was_active", 0),
                    (assign, "$deathcam_mouse_notmoved_x", "$deathcam_mouse_last_notmoved_x"),
                    (assign, "$deathcam_mouse_notmoved_y", "$deathcam_mouse_last_notmoved_y"),
                (else_try),
                    (assign, "$deathcam_mouse_notmoved_x", reg1),
                    (assign, "$deathcam_mouse_notmoved_y", reg2),
                (try_end),
                    (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                    (assign, "$deathcam_mouse_last_y", reg2),
            (try_end),
        (try_end),

        (assign, ":delta_x", 0),
        (assign, ":delta_y", 0),
        (assign, ":rotating_horizontal", 0),
        (assign, ":rotating_vertical", 0),

        (try_begin),
          (key_is_down, "$g_camera_rot_left"),
          (try_begin),
            (ge, "$deathcam_keyboard_rotation_x", 0),
            (assign, "$deathcam_keyboard_rotation_x", -20),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_x", -1),
          (assign, ":continue", 2),
          (assign, ":rotating_horizontal", -1),
        (else_try),
          (key_is_down, "$g_camera_rot_right"),
          (try_begin),
            (le, "$deathcam_keyboard_rotation_x", 0),
            (assign, "$deathcam_keyboard_rotation_x", 20),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_x", 1),
          (assign, ":continue", 2),
          (assign, ":rotating_horizontal", 1),
        (else_try),
          (assign, "$deathcam_keyboard_rotation_x", 0),
          (assign, ":rotating_horizontal", 0),
        (try_end),

        (try_begin),
          (key_is_down, "$g_camera_rot_up"),
          (try_begin),
            (le, "$deathcam_keyboard_rotation_y", 0),
            (assign, "$deathcam_keyboard_rotation_y", 15),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_y", 1),
          (assign, ":continue", 2),
          (assign, ":rotating_vertical", 1),
        (else_try),
          (key_is_down, "$g_camera_rot_down"),
          (try_begin),
            (ge, "$deathcam_keyboard_rotation_y", 0),
            (assign, "$deathcam_keyboard_rotation_y", -15),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_y", -1),
          (assign, ":continue", 2),
          (assign, ":rotating_vertical", -1),
        (else_try),
          (assign, "$deathcam_keyboard_rotation_y", 0),
          (assign, ":rotating_vertical", 0),
        (try_end),

        (try_begin),
          (eq, ":continue", 1),
          (store_sub, ":delta_x", reg1, "$deathcam_mouse_notmoved_x"), #Store pos difference
          (store_sub, ":delta_y", reg2, "$deathcam_mouse_notmoved_y"),
        (else_try),
          (eq, ":continue", 2),
          (try_begin),
            (neq, ":rotating_horizontal", 0),
            (val_clamp, "$deathcam_keyboard_rotation_x", -80, 80),
            (assign, ":delta_x", "$deathcam_keyboard_rotation_x"),
          (try_end),

          (try_begin),
            (neq, ":rotating_vertical", 0),
            (val_clamp, "$deathcam_keyboard_rotation_y", -45, 45),
            (assign, ":delta_y", "$deathcam_keyboard_rotation_y"),
          (try_end),
        (try_end),

        (try_begin),
          (ge, ":continue", 1),
          (val_mul, ":delta_x", "$deathcam_sensitivity_x"),
          (val_mul, ":delta_y", "$deathcam_sensitivity_y"),
          # (val_mul, ":delta_y", "$deathcam_flip_y_multiplier"),

          (val_clamp, ":delta_x", -80000, 80001), #8
          (val_clamp, ":delta_y", -60000, 60001), #6

          (store_mul, ":neg_rotx", "$deathcam_total_rotx", -1),
          (position_rotate_x_floating, pos47, ":neg_rotx"), #Reset x axis to initial state

          (position_rotate_y, pos47, 90), #Barrel roll by 90 degrees to inverse x/z axis
          (position_rotate_x_floating, pos47, ":delta_x"), #Rotate simulated z axis, Horizontal
          (position_rotate_y, pos47, -90), #Reverse

          (position_rotate_x_floating, pos47, "$deathcam_total_rotx"), #Reverse

          (position_rotate_x_floating, pos47, ":delta_y"), #Vertical
          (val_add, "$deathcam_total_rotx", ":delta_y"), #Fix yaw
          (mission_cam_set_position, pos47),
        (try_end),
    ]
)
##BEAN END - Deathcam
#alternate follower camera


custom_commander_camera = (
  0, 0, 0, [
    (this_or_next|eq, "$g_dplmc_cam_activated", camera_follow),
    (neg|main_hero_fallen),
    
    # (this_or_next|main_hero_fallen),
    # (neg|is_camera_in_first_person),
  ],
  [
    (try_begin),
      (main_hero_fallen),
      (gt, "$dmod_current_agent", -1), #should be -1, but variable gets bugged
      # (agent_is_active, "$dmod_current_agent"),
      (assign, ":player_agent", "$dmod_current_agent"),
      (assign, ":duration", 500),
    (else_try),
      # (get_player_agent_no, ":player_agent"),
      (assign, ":player_agent", "$g_player_agent"),
      (assign, ":duration", 0),#instant
    (try_end),

    #compared to other deathcams these values are kept between missions
    (ge, ":player_agent", 0),
    (assign, ":continue", 0),
    (try_begin),
      (key_is_down, "$g_camera_adjust_add"),
      (val_add, "$g_camera_z", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_add, "$g_camera_rotate_y", 5),
      (try_end),
    (else_try),
      (key_is_down, "$g_camera_adjust_sub"),
      (val_sub, "$g_camera_z", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_sub, "$g_camera_rotate_y", 5),
      (try_end),
    (else_try),
      (key_is_down, "$g_camera_rot_up"),
      (val_add, "$g_camera_y", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_add, "$g_camera_rotate_x", 5),
      (try_end),
    (else_try),
      (key_is_down, "$g_camera_rot_down"),
      (val_sub, "$g_camera_y", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_sub, "$g_camera_rotate_x", 5),
      (try_end),
    (try_end),

    (try_begin),
      (key_is_down, key_left_control),
      (try_begin),
        (key_is_down, "$g_camera_rot_left"),
        (val_sub, "$g_camera_rotate_y", 5),
      (else_try),
        (key_is_down, "$g_camera_rot_right"),
        (val_add, "$g_camera_rotate_y", 5),
      (try_end),
    (try_end),
    (try_begin), #any key pressed, immediate update
      (eq, ":continue", 1),
      #no headless mode
      (set_camera_in_first_person, 0),
      (assign, ":duration", 0),
      (mission_cam_set_mode, 1),
    (try_end),

    (agent_get_look_position, pos47, ":player_agent"),
    #moving around x when following is pointless
    (position_move_z, pos47, "$g_camera_z"),
    (position_move_y, pos47, "$g_camera_y"),

    (position_rotate_z, pos47, "$g_camera_rotate_z"),
    #rot x is the only one that makes sense, other rotations tilt too much
    (position_rotate_x, pos47, "$g_camera_rotate_x"),
    (position_rotate_y, pos47, "$g_camera_rotate_y"),
    (agent_get_horse, ":horse_agent", ":player_agent"),
    (try_begin),
      (ge, ":horse_agent", 0),
      (position_move_z, pos47, 90),
      (val_div, ":duration", 2),#mounted agents need to refresh faster
    (try_end),

    #prevent clipping underground
    (position_get_distance_to_ground_level, ":height", pos47),
    (try_begin), #centimeters?
      (le, ":height", 0),
      (position_set_z_to_ground_level, pos47),
      (position_move_z, pos47, 15), #keep around knee height?
    (try_end),

    (try_begin), #if we don't cancel during first person, head disappears
      (call_script, "script_cf_cancel_camera_keys"),
      (neg|main_hero_fallen),
    (else_try),
      (gt, ":duration", 0), #if 0, won't animate at all
      # (eq, "$dmod_move_camera", 1),
      (mission_cam_animate_to_position, pos47, ":duration", 0),
    (else_try), #this allows moving with the troop every frame
      (mission_cam_set_position, pos47),
    (try_end),
  ])

deathcam_cycle_forwards = (0, 0.5, 1,[(this_or_next|key_clicked, key_mouse_scroll_up),(key_clicked, "$g_cam_tilt_left"),
        (main_hero_fallen),(eq, "$g_dplmc_cam_activated", camera_follow),
        ],
        [(call_script, "script_dmod_cycle_forwards"),])

deathcam_cycle_backwards = (0, 0.5, 1,[(this_or_next|key_clicked, key_mouse_scroll_down),(key_clicked, "$g_cam_tilt_right"),
        (main_hero_fallen),(eq, "$g_dplmc_cam_activated", camera_follow),
        ],
        [(call_script, "script_dmod_cycle_backwards"),])

#default keyboard camera
dplmc_death_camera = (
  0, 0, 0,
  [(eq, "$g_dplmc_battle_continuation", 0),
   (eq, "$g_dplmc_cam_activated", camera_keyboard),
  ],
  [
    #(agent_get_look_position, pos47, ":player_agent"),

    # (get_player_agent_no, ":player_agent"),
    # (agent_get_team, ":player_team", ":player_agent"),

    (mission_cam_get_position, pos47),

    (assign, ":camera_rotate_x", 0),
    (assign, ":camera_rotate_y", 0),
    (assign, ":camera_rotate_z", 0),
    (assign, ":camera_x", 0),
    (assign, ":camera_y", 0),
    (assign, ":camera_z", 0),

    (try_begin),
      (game_key_is_down, gk_move_left),
      (val_sub, ":camera_x", 10),
    (else_try),
      (game_key_is_down, gk_move_right),
      (val_add, ":camera_x", 10),
    (try_end),
    (position_move_x, pos47, ":camera_x"),

    (try_begin),
      (game_key_is_down, gk_move_forward),
      (val_add, ":camera_y", 10),
    (else_try),
      (game_key_is_down, gk_move_backward),
      (val_sub, ":camera_y", 10),
    (try_end),
    (position_move_y, pos47, ":camera_y"),

    (try_begin),
      (key_is_down, "$g_camera_adjust_add"),
      (val_add, ":camera_z", 10),
    (else_try),
      (key_is_down, "$g_camera_adjust_sub"),
      (val_sub, ":camera_z", 10),
    (try_end),
    (position_move_z, pos47, ":camera_z"),

    (try_begin),
      (key_is_down, "$g_camera_rot_left"),
      (val_add, ":camera_rotate_z", 1),
    (else_try),
      (key_is_down, "$g_camera_rot_right"),
      (val_sub, ":camera_rotate_z", 1),
    (try_end),
    (position_rotate_z, pos47, ":camera_rotate_z"),

    (try_begin),
      (key_is_down, "$g_cam_tilt_left"),
      (val_add, ":camera_rotate_y", 1),
    (else_try),
      (key_is_down, "$g_cam_tilt_right"),
      (val_sub, ":camera_rotate_y", 1),
    (try_end),
    (position_rotate_y, pos47, ":camera_rotate_y"),

    (try_begin),
      (key_is_down, "$g_camera_rot_up"),
      (val_add, ":camera_rotate_x", 1),
    (else_try),
      (key_is_down, "$g_camera_rot_down"),
      (val_sub, ":camera_rotate_x", 1),
    (try_end),
    (position_rotate_x, pos47, ":camera_rotate_x"),

    (try_begin),
      (call_script, "script_cf_cancel_camera_keys"),
    (else_try),
      (mission_cam_set_mode, 1),
      (mission_cam_set_position, pos47),
    (try_end),
  ])

##SB : new camera triggers
dplmc_battle_mode_triggers = [
    dplmc_random_mixed_gender,
    dplmc_horse_speed,
    common_move_deathcam, common_rotate_deathcam,
    custom_commander_camera, deathcam_cycle_forwards, deathcam_cycle_backwards,
    dplmc_death_camera,
  ]
##diplomacy end

