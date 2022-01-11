from django.contrib import admin

# Register your models here.

from .models import add_cust
from .models import category
from .models import Chakki
from .models import Residential_Coolers
from .models import Electrical_Appliances
from .models import RO_Spare_Parts
from .models import PVC_Pipes
from .models import Industrial_Coolers,Tubs
from .models import CustomerForm

from .models import smart
from .models import rockstar
from .models import ageneral
from .models import elegant_jr
from .models import elegant
from .models import elegant_plus
from .models import decent
from .models import freedom_wind
from .models import freedom_plus
from .models import freedom_jr
from .models import freedom
from .models import freedom_storm

from .models import magic_VC
from .models import magic_cook
from .models import super_star
from .models import super_star_plus
from .models import olive
from .models import olive_plus
from .models import olive_plus_SS
from .models import magic_plus
from .models import max_plus
from .models import smart_2hp

# from .models import base_electric
from .models import heater
from .models import Gasgeyser,motor_pump
from .models import iron,water_heater
from .models import kettle,purifier,induction
from .models import ceiling_fan,madhani
from .models import pedestal_fan,mixer_grinder
from .models import rod, chopper,blender,Hand_juicer,chimney

from .models import grinding
# from .models import gasGeyser1,gasGeyser2
# from .models import iron1,iron2,iron3,iron4
# from .models import iron1,iron2,iron3,iron4
# from .models import kettle1,kettle2,kettle3
# from .models import water_rod
# from .models import ceiling_fan1,ceiling_fan2,ceiling_fan3
# from .models import pedestal_fan1,pedestal_fan2






# from import_export.admin import ImportExportModelAdmin

admin.site.register(add_cust)

admin.site.register(category)

admin.site.register(Chakki)
admin.site.register(Residential_Coolers)
admin.site.register(Electrical_Appliances)
admin.site.register(RO_Spare_Parts)
admin.site.register(PVC_Pipes)
admin.site.register(Industrial_Coolers)
admin.site.register(Tubs)


admin.site.register(CustomerForm)


admin.site.register(smart)
admin.site.register(freedom)
admin.site.register(elegant_plus)
admin.site.register(elegant_jr)
admin.site.register(elegant)
admin.site.register(rockstar)
admin.site.register(decent)
admin.site.register(ageneral)
admin.site.register(freedom_wind)
admin.site.register(freedom_plus)
admin.site.register(freedom_jr)
admin.site.register(freedom_storm)

admin.site.register(olive)
admin.site.register(olive_plus)
admin.site.register(olive_plus_SS)
admin.site.register(magic_cook)
admin.site.register(max_plus)
admin.site.register(super_star)
admin.site.register(super_star_plus)
admin.site.register(magic_plus)
admin.site.register(magic_VC)
admin.site.register(smart_2hp)

admin.site.register(grinding)


admin.site.register(heater)
admin.site.register(Gasgeyser)
admin.site.register(iron)
admin.site.register(kettle)
admin.site.register(rod)
admin.site.register(ceiling_fan)
admin.site.register(pedestal_fan)
admin.site.register(mixer_grinder)
admin.site.register(blender)
admin.site.register(induction)
admin.site.register(madhani)
admin.site.register(Hand_juicer)
admin.site.register(water_heater)
admin.site.register(chimney)
admin.site.register(chopper)
admin.site.register(motor_pump)












# class userdata(ImportExportModelAdmin):
#      pass
