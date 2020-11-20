from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'recipes/homepage.html')

def createRecipePageView(request):
    return render(request, 'recipes/create_recipe.html')

def editRecipePageView(request):
    return render(request, 'recipes/edit_recipe.html')

def viewRecipePageView(request):
    return render(request, 'recipes/view_recipe.html')

def aboutPageView(request):
    output='about page'
    return HttpResponse(output)
    
