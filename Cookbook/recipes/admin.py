from django.contrib import admin
from .models import Recipe, RecipeType, RecipeIngredient, User

 # Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeType)
admin.site.register(RecipeIngredient)
admin.site.register(User)