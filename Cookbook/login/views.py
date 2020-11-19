from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def signUpPageView(request):
    return render(request, 'login/signup.html')

def loginPageView(request):
    return render(request, 'login/login.html')


#def profilePageView(request)
#Do this if we have time