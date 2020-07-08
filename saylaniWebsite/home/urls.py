from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.signIn, name="SignIn"),
    path("signup/", views.signUp, name="SignUp")
    
]