from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    output='Home Page'
    return HttpResponse(output)

def signUpPageView(request):
    output = 'sign up'
    return HttpResponse(output)

def loginPageView(request):
    output = 'login'
    return HttpResponse(output)

def createRecipePageView(request):
    output = 'Create Recipe'
    return HttpResponse(output)

def editRecipePageView(request):
    output = 'edit'
    return HttpResponse(output)

def viewRecipePageView(request):
    output = 'view recipe'
    return HttpResponse(output)

def aboutPageView(request):
    output='about page'
    return HttpResponse(output)
    
