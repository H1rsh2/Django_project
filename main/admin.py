from django.contrib import admin
from .models import Stock
from .models import Provider
from .models import Status
from .models import Type
from .models import Food
from .models import Dish
from .models import Ingredient


admin.site.register(Status)


admin.site.register(Type)


admin.site.register(Food)


admin.site.register(Stock)


admin.site.register(Provider)


admin.site.register(Dish)


admin.site.register(Ingredient)

