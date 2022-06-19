from django.db import models

# Create your models here

class Product(models.Model):
  product_name = models.CharField(max_length=30)
  product_description_abridged = models.CharField(max_length=200, null=True)
  product_description_full = models.CharField(max_length=200, null=True)
  product_img = models.ImageField(upload_to="images/")
  product_price = models.CharField(max_length=30)

class Order(models.Model):
  ordered_product = models.CharField(max_length=30)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  address = models.CharField(max_length=50)
  city = models.CharField(max_length=40)
  zip_code = models.CharField(max_length=5)
  order_time = models.CharField(max_length=15, default='')
  fulfillment_status = models.BooleanField(null=True, default=False)