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

def editRecipePageView(request, recipeid):
    print('-------------------------------------',recipeid)
    recipe = Recipe.objects.get(id = recipeid)
    context = {
        'recipe' : recipe,
    }
    
    return render(request, 'recipes/edit_recipe.html', context)

def editRecipe(request):
    
    recipe_type = request.POST.get('recipeType')
    #photo = request.POST.get('photo')
    rt = RecipeType.objects.get(recipe_type_description = recipe_type)
    recipe_id = request.POST.get('id')
    recipe = Recipe.objects.get(id = recipe_id)
    recipe.recipe_name = request.POST.get('recipeTitle')
    recipe.recipe_description = request.POST.get('recipeDescription')
    recipe.recipe_steps = request.POST.get('recipeSteps')
    recipe.recipe_type = rt
    recipe.save()
   
    print(recipe_id)

    return redirect('ingredients', recipe_id)

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

def recipesPageView(request, cat = 'blank'):
    #this is hardcoded to demonstrate how many recipes can be dynamically shown on a single page
    list = []
    for i in Recipe.objects.all():
        if i.recipe_type.recipe_type_description == cat :
            list.append(i)
    
    ingredients = []
    for ing in RecipeIngredient.objects.all():
        ingredients.append(ing)
    context = {
        'list' : list,
        'ingredients' : ingredients,
        'category' : cat,
    }
    return render(request, 'recipes/recipes.html', context)

def deleteRecipe(request, cat):
    Recipe.objects.get(id = request.POST.get('id')).delete()
    return redirect('recipes', cat)

def searchRecipes(request):
    search = request.GET['search'].lower()
    results = []
    for recipe in Recipe.objects.filter(recipe_name__contains=search):
        results.append(recipe)
    for recipe in Recipe.objects.filter(recipe_description__contains=search):
        if recipe not in results:
            results.append(recipe)
    for recipe in Recipe.objects.filter(recipe_steps__contains=search):
        if recipe not in results:
            results.append(recipe)
    for ing in RecipeIngredient.objects.filter(ingredient_name__contains=search):
        if ing.recipe not in results:
            results.append(ing.recipe)

    context = {
        'recipes' : results,
        'search' : search,
    }

    return render(request, 'recipes/searchRecipes.html', context)
    
