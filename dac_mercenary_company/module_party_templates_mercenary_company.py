from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

from compiler import *

mercenary_company_party_templates = [

("mercenary_company_infantry", "Mercenary Company Infantry", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_recruit,2,6),(trp_custom_merc_footman,2,4),(trp_custom_merc_veteran,1,3),(trp_custom_merc_sergeant,1,2)]),

("mercenary_company_ranged", "Mercenary Company Ranged", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_skirmisher,2,6),(trp_custom_merc_ranger,2,4),(trp_custom_merc_marksman,1,3)]),

]