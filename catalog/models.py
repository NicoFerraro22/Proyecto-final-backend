
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self): return self.name

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    tracks = models.JSONField(blank=True, null=True)
    def __str__(self): return self.name
