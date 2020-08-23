from django.contrib import admin
from .models import Product, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
    )
    search_fields = (
        'title',
    )

@admin.register(Review)
class RevuewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )
