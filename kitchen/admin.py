from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, DishType, Dish

admin.site.register(Cook, UserAdmin)

@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price","description"]
    list_filter = ["name", "dish_type", "price"]
    search_fields = ["name"]