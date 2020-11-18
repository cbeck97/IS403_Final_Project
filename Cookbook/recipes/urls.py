from django.urls import path
from .views import aboutPageView, indexPageView, createRecipePageView, editRecipePageView,viewRecipePageView, aboutPageView

urlpatterns = [
    path('', indexPageView, name='Index'),
    path('create', createRecipePageView, name='create'),
    path('edit', editRecipePageView, name='edit'),
    path('view', viewRecipePageView, name='view'),
    path('about', aboutPageView, name='about'),
]
