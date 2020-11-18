from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signUpPageView(request):
    output = 'sign up'
    return HttpResponse(output)

def loginPageView(request):
    output = 'login'
    return HttpResponse(output)