from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#sign up view
#just routes to the sign up page
def signUpPageView(request):
    return render(request, 'login/signup.html')

#log in view
#just routes to the log in page
def loginPageView(request):
    return render(request, 'login/login.html')


#def profilePageView(request)
#Do this if we have time