from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    color = models.CharField(max_length=20)
    
    image_front = models.ImageField(upload_to='product_pics')
    image_side = models.ImageField(upload_to='product_pics')


    price = models.CharField(max_length=10)
    left = models.IntegerField()


