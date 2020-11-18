from django.contrib import admin
from .models import Recipe, RecipeType, RecipeIngredients, User

 # Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeType)
admin.site.register(RecipeIngredients)
admin.site.register(User)