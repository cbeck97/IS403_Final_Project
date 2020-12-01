from django.urls import path
from .views import aboutPageView, indexPageView, createRecipePageView, editRecipePageView,viewRecipePageView, aboutPageView, recipesPageView, addIngredient, addRecipe, ingredientsPageView, deleteIngredient

urlpatterns = [
    path('create', createRecipePageView, name='create'),
    path('create/ingredients/<recipe>', ingredientsPageView, name='ingredients'),
    path('create/ingredients/delete/<recipe>', deleteIngredient, name='deleteIngredient'),
    path('edit', editRecipePageView, name='edit'),
    path('view', viewRecipePageView, name='view'),
    path('about', aboutPageView, name='about'),
    path('recipes/<cat>', recipesPageView, name='recipes'),
    path('create/addingredients/<recipe>', addIngredient, name='addIngredient'),
    path('create/add', addRecipe, name='addRecipe'),
    path('', indexPageView, name='index'),
]
