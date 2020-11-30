from django.urls import path
from .views import aboutPageView, indexPageView, createRecipePageView, editRecipePageView,viewRecipePageView, aboutPageView, recipesPageView

urlpatterns = [
    path('create', createRecipePageView, name='create'),
    path('edit', editRecipePageView, name='edit'),
    path('view', viewRecipePageView, name='view'),
    path('about', aboutPageView, name='about'),
    path('recipes/<cat>', recipesPageView, name='recipes'),
    path('', indexPageView, name='index'),
]
