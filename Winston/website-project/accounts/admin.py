from django.contrib import admin

from .models import CarInfo
from .models import Viewcars
from .models import Audi
from .models import Hyundai
from .models import Kia
from .models import Mitsubishi
from .models import Toyota


admin.site.register(CarInfo)
admin.site.register(Viewcars)
admin.site.register(Audi)
admin.site.register(Hyundai)
admin.site.register(Kia)
admin.site.register(Mitsubishi)
admin.site.register(Toyota)


