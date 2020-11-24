from django.urls import path
from .views import aboutPageView, indexPageView, createRecipePageView, editRecipePageView,viewRecipePageView, aboutPageView, recipesPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('create', createRecipePageView, name='create'),
    path('edit', editRecipePageView, name='edit'),
    path('view', viewRecipePageView, name='view'),
    path('about', aboutPageView, name='about'),
    path('recipes', recipesPageView, name='recipe')
]
