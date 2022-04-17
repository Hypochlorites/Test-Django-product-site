from django.db import models

# Create your models here

class Product(models.Model):
  product_name = models.CharField(max_length=30)
  product_description = models.CharField(max_length=200)
  product_img = models.ImageField(upload_to="images/")
  product_price = models.CharField(max_length=30)