from django.urls import path
from .views import indexPageView, createRecipePageView, editRecipePageView,viewRecipePageView, recipesPageView, addIngredient, addRecipe, ingredientsPageView, deleteIngredient, deleteRecipe, editRecipe, searchRecipes

urlpatterns = [
    path('create', createRecipePageView, name='create'),
    path('create/ingredients/<recipe>', ingredientsPageView, name='ingredients'),
    path('create/ingredients/delete/<recipe>', deleteIngredient, name='deleteIngredient'),
    path('edit/<recipeid>', editRecipePageView, name='edit'),
    path('edit_recipe', editRecipe, name='editRecipe'),
    path('view', viewRecipePageView, name='view'),
    path('recipes/<cat>', recipesPageView, name='recipes'),
    path('delete_recipe/<cat>', deleteRecipe, name='deleteRecipe'),
    path('create/addingredients/<recipe>', addIngredient, name='addIngredient'),
    path('create/add', addRecipe, name='addRecipe'),
    path('search', searchRecipes, name='search'),
    path('', indexPageView, name='index'),
]
