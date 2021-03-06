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
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    view_count = models.IntegerField(default = 0, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name="like_user_set", through="Like")

    @property
    def like_count(self):
        return self.like_user_set.count()


class Review(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'product'))







