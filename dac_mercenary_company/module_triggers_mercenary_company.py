from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

from compiler import *

mercenary_company_triggers = [

  (24, 0, ti_once, [
    (map_free,0),
    (troop_slot_ge, "trp_player", slot_troop_renown, 50),
  ], 
  [
    # (assign, "$player_camp_available", 1),
    (jump_to_menu, "mnu_player_camp_notification"),
  ]),
  

]