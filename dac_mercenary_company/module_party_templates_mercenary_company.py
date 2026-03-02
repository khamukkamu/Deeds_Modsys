from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

from compiler import *

mercenary_company_party_templates = [

("mercenary_company_infantry", "Mercenary Company Infantry", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_recruit,2,6),(trp_custom_merc_footman,2,4),(trp_custom_merc_veteran,1,3),(trp_custom_merc_sergeant,1,2),(trp_custom_merc_vanguard,1,2)]),

("mercenary_company_ranged", "Mercenary Company Ranged", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_skirmisher,2,6),(trp_custom_merc_ranger,2,4),(trp_custom_merc_defender,1,2),(trp_custom_merc_marksman,1,2)]),

("mercenary_company_cavalry", "Mercenary Company Cavalry", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_scout,2,4),(trp_custom_merc_mounted_sergeant,1,3)]),

("mercenary_company_noble_infantry", "Mercenary Company Noble Infantry", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_foot_squire,1,3),(trp_custom_merc_footman_at_arms,1,2),(trp_custom_merc_dismounted_knight,1,1)]),

("mercenary_company_noble_cavalry", "Mercenary Company Noble Cavalry", 0, 0, fac_commoners, 0, 
[(trp_custom_merc_squire,1,3),(trp_custom_merc_man_at_arms,1,2),(trp_custom_merc_knight,1,1)]),

("mercenary_company_italian_infantry", "Mercenary Company Italian Infantry", 0, 0, fac_commoners, 0, 
[(trp_italian_light_infantry,2,6),(trp_italian_infantry,2,4),(trp_italian_heavy_infantry,1,2)]),

("mercenary_company_italian_ranged", "Mercenary Company Italian Ranged", 0, 0, fac_commoners, 0, 
[(trp_genoese_light_crossbowman,2,6),(trp_genoese_crossbowman,2,4),(trp_genoese_heavy_crossbowman,1,3)]),

("mercenary_company_italian_cavalry", "Mercenary Company Italian Knight", 0, 0, fac_commoners, 0, 
[(trp_italian_knight,1,3),]),

("mercenary_company_flemish_infantry", "Mercenary Company Flemish Infantry", 0, 0, fac_commoners, 0, 
[(trp_flemish_militia_pikeman,2,6),(trp_flemish_pikeman,2,4),(trp_flemish_halberdier,2,4),(trp_flemish_heavy_pikeman,1,2),(trp_flemish_heavy_halberdier,1,2)]),

("mercenary_company_flemish_ranged", "Mercenary Company Flemish Ranged", 0, 0, fac_commoners, 0, 
[(trp_flemish_peasant_crossbowman,2,6),(trp_flemish_militia_crossbowman,2,4),(trp_flemish_crossbowman,1,3),(trp_flemish_heavy_crossbowman,1,2)]),

("mercenary_company_german_knight", "Mercenary Company German Foot-Knight", 0, 0, fac_commoners, 0, 
[(trp_mercenary_german_knight,1,3),]),

("mercenary_company_german_cavalry", "Mercenary Company German Knight", 0, 0, fac_commoners, 0, 
[(trp_mercenary_german_knight,1,3),]),

]