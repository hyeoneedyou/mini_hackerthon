from django.urls import path
from .views import main

 
app_name ="shoes"
urlpatterns = [
    path('', main, name="main"),
]