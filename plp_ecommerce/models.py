from django.db import models
#from products.models import Product


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=11,decimal_places=2)
    image = models.ImageField(upload_to='products/')


