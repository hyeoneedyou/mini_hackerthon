from django.urls import path
from .views import *

 
app_name ="product"
urlpatterns = [
    path('', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('<int:product_id>/create_review', create_review, name="create_review"),
]    