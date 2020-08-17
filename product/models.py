from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length= 50, null=False)
    content = models.TextField()
    price = models.CharField(max_length= 50, null=False)
    stock = models.CharField(max_length= 50, null=False)
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)


class Review(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


