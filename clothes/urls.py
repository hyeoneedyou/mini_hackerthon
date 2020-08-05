from django.urls import path
from .views import main

 
app_name ="clothes"
urlpatterns = [
    path('', main, name="main"),
]