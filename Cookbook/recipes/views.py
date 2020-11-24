from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'recipes/index.html')

def createRecipePageView(request):
    return render(request, 'recipes/create_recipe.html')

def editRecipePageView(request):
    return render(request, 'recipes/edit_recipe.html')

def viewRecipePageView(request):
    return render(request, 'recipes/view_recipe.html')

def recipesPageView(request):
    #this is hardcoded to demonstrate how many recipes can be dynamically shown on a single page
    list = []
    for i in range(6):
        list.append(i + 1)

    context = {
        'list' : list
    }
    return render(request, 'recipes/recipes.html', context)

def aboutPageView(request):
    output='about page'
    return HttpResponse(output)
    
