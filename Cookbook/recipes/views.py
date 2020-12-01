from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Recipe, RecipeIngredient, RecipeType
# Create your views here.
def indexPageView(request):
    return render(request, 'recipes/index.html')


def createRecipePageView(request):
    return render(request, 'recipes/create_recipe.html')

def addRecipe(request):
    recipe_title = request.POST.get('recipeTitle')
    recipe_description = request.POST.get('recipeDescription')
    recipe_steps = request.POST.get('recipeSteps')
    recipe_type = request.POST.get('recipeType')
    photo = request.POST.get('photo')
    rt = RecipeType.objects.get(recipe_type_description = recipe_type)

    recipe = Recipe(recipe_name = recipe_title, recipe_description = recipe_description, recipe_steps = recipe_steps, recipe_type = rt,photo=photo)
    recipe.save()
    print(recipe.id)
    return redirect('ingredients', recipe.id)

def editRecipePageView(request):
    return render(request, 'recipes/edit_recipe.html')

def ingredientsPageView(request, recipe):
    recipe_ingredients = []
    for i in RecipeIngredient.objects.filter(recipe = recipe):
        recipe_ingredients.append(i)
    
    context = {
        'recipe' : Recipe.objects.get(id=recipe),
        'ingredients' : recipe_ingredients,

    }
    return render(request, 'recipes/add_ingredients.html', context)

def addIngredient(request, recipe):
    ingredientName = request.POST.get('IngredientName')
    measurementAmount = request.POST.get('MeasurementAmount')
    measurementType = request.POST.get('MeasurementType')
    r = Recipe.objects.get(id = recipe)
    print(recipe)
    ingredient = RecipeIngredient(ingredient_name=ingredientName,measure_amount=measurementAmount,measurement_type=measurementType, recipe=r)
    ingredient.save()

    return redirect('ingredients', recipe)

def deleteIngredient(request, recipe):
    print('----------',request.POST.get('ingredient'))
    RecipeIngredient.objects.get(id = request.POST.get('ingredient')).delete()

    return redirect('ingredients', recipe)


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
    
