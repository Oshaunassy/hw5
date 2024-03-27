from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(i for i in range(1,6))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return self.product.title

