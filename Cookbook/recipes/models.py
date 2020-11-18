from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    skill_level = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to = 'photos', blank=True)

class RecipeType(models.Model):
    recipe_type_description = models.CharField(max_length=50)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.CharField(max_length=1000)
    recipe_steps = models.CharField(max_length=5000)
    recipe_type = models.ForeignKey(RecipeType, on_delete=DO_NOTHING)
    user = models.ForeignKey(User, on_delete=CASCADE)

class RecipeIngredients(models.Model):
    ingredient_name = models.CharField(max_length=50)
    measure_amount = models.CharField(max_length=20)
    measurement_type = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=CASCADE)
    sequence = models.SmallIntegerField(default=0)

