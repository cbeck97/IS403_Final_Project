from django.urls import path
from .views import signUpPageView, loginPageView

urlpatterns = [
    path('signup', signUpPageView, name='signup'),
    path('', loginPageView, name='login'),
]