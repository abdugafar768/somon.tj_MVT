from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Prodect(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

# Create your models here.
