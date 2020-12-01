from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, RecipeIngredient
# Create your views here.
def indexPageView(request):
    return render(request, 'recipes/index.html')


def createRecipePageView(request):
    return render(request, 'recipes/create_recipe.html')

def editRecipePageView(request):
    return render(request, 'recipes/edit_recipe.html')

def viewRecipePageView(request):
    return render(request, 'recipes/view_recipe.html')

def recipesPageView(request, query = Recipe.objects.all(), ingred = RecipeIngredient.objects.all(), cat = 'blank'):
    #this is hardcoded to demonstrate how many recipes can be dynamically shown on a single page
    list = []
    for i in query:
        if i.recipe_type.recipe_type_description == cat :
            list.append(i)
    
    ingredients = []
    for ing in ingred:
        ingredients.append(ing)
    context = {
        'list' : list,
        'ingredients' : ingredients,
        'category' : cat,
    }
    return render(request, 'recipes/recipes.html', context)

#we can probably get rid of this
def aboutPageView(request):
    output='about page'
    return HttpResponse(output)
    
