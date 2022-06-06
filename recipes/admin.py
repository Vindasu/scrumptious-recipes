from django.contrib import admin

from recipes.models import Recipe
from recipes.models import Step
from recipes.models import Measure
from recipes.models import FoodItem

# Register your models here.
# Create a class that inherits from admin.ModelAdmin


class RecipeAdmin(admin.ModelAdmin):
    pass


class MeasureAdmin(admin.ModelAdmin):
    pass


class FoodItemAdmin(admin.ModelAdmin):
    pass


class StepAdmin(admin.ModelAdmin):
    pass


# register the class and model
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
