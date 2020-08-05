from django.urls import path
from .views import main

 
app_name ="food"
urlpatterns = [
    path('', main, name="main"),
]