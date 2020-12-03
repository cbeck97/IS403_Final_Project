from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Recipe, RecipeIngredient, RecipeType
# Create your views here.

#index page view for the homepage
def indexPageView(request):
    return render(request, 'recipes/index.html')

#this view routes to the create recipe form
def createRecipePageView(request):
    return render(request, 'recipes/create_recipe.html')


#this view is called once a form from the create recipe page is submitted
#a new recipe object is then created and saved to the recipe table in the postgre database
#the view redirects to the ingredients view to add ingredients
def addRecipe(request):
    recipe_title = request.POST.get('recipeTitle')
    recipe_description = request.POST.get('recipeDescription')
    recipe_steps = request.POST.get('recipeSteps')
    recipe_type = request.POST.get('recipeType')
    photo = request.FILES['photo']
    rt = RecipeType.objects.get(recipe_type_description = recipe_type)

    recipe = Recipe(recipe_name = recipe_title, recipe_description = recipe_description, recipe_steps = recipe_steps, recipe_type = rt,photo=photo)
    #recipe.photo.
    print(request.FILES['photo'])
    recipe.save()
    print(recipe.id)
    return redirect('ingredients', recipe.id)

#the edit recipe page is similar to the create recipe page view except the recipes info is pulled to automatically populate the form
# the recipe's id is also used to find and populate the recipe info
def editRecipePageView(request, recipeid):
    print('-------------------------------------',recipeid)
    recipe = Recipe.objects.get(id = recipeid)
    context = {
        'recipe' : recipe,
    }
    
    return render(request, 'recipes/edit_recipe.html', context)

#this view is called once a form from the edit recipe page is submitted
#the new data from the form is used to update the fields of the recipe whose id was passed in the edit recipe page view 
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

#the ingredients page view has a form that shows all the ingredients in a recipe and allows more ingredients to be added
#to do this the recipe info and the ingredients in the recipe are gathered and passed to the template
def ingredientsPageView(request, recipe):
    recipe_ingredients = []
    for i in RecipeIngredient.objects.filter(recipe = recipe):
        recipe_ingredients.append(i)
    
    context = {
        'recipe' : Recipe.objects.get(id=recipe),
        'ingredients' : recipe_ingredients,

    }
    return render(request, 'recipes/add_ingredients.html', context)

#this view is called when the form in the ingredients page view is submitted 
#the info creates a RecipeIngredient object which is saved into the same postgres table
#the form redirects to the same page so the user can keep adding ingredients
def addIngredient(request, recipe):
    ingredientName = request.POST.get('IngredientName')
    measurementAmount = request.POST.get('MeasurementAmount')
    measurementType = request.POST.get('MeasurementType')
    r = Recipe.objects.get(id = recipe)
    print(recipe)
    ingredient = RecipeIngredient(ingredient_name=ingredientName,measure_amount=measurementAmount,measurement_type=measurementType, recipe=r)
    ingredient.save()

    return redirect('ingredients', recipe)

#on the ingredients template there are buttons for each of the existing ingredients so they can be deleted
#this view will redirect to ingredients page view
def deleteIngredient(request, recipe):
    print('----------',request.POST.get('ingredient'))
    RecipeIngredient.objects.get(id = request.POST.get('ingredient')).delete()

    return redirect('ingredients', recipe)

#this view is our bread and butter
#when a category is selected on the index page, the name of the category is passed to this view and used to filter down the recipes to that category
#the recipes as well as all ingredients are passed to the template
def recipesPageView(request,cat):
    recipes = []
    for i in Recipe.objects.all():
        if i.recipe_type.recipe_type_description == cat :
            recipes.append(i)
    
    ingredients = []
    for ing in RecipeIngredient.objects.all():
        ingredients.append(ing)
    context = {
        'recipes' : recipes,
        'ingredients' : ingredients,
        'category' : cat,
    }
    return render(request, 'recipes/recipes.html', context)

#each recipe can be deleted from the recipes template
#once the recipe is deleted the user is redirected to the same template under the same category
def deleteRecipe(request, cat):
    Recipe.objects.get(id = request.POST.get('id')).delete()
    return redirect('recipes', cat)

#this is the search view
#when the search form is submitted, the search will be lowercased and check against all the recipe names, descriptions, steps, and ingredients.
#when a match is found it is added to the results that will be sent to the template
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
    ingredients = RecipeIngredient.objects.all()
    context = {
        'recipes' : results,
        'search' : search,
        'ingredients' : ingredients
    }

    return render(request, 'recipes/searchRecipes.html', context)
    
