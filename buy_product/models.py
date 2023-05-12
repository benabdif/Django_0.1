from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

#    This is the modle for the products


# this is the first models data
class Addproduct2(models.Model):
    price = models.IntegerField(default=1, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)
    
   
    
    
    def __str__(self):
        return self.name
    
    


class Addproduct(models.Model):
    price = models.IntegerField()
    num_bath = models.IntegerField()
    num_bed = models.IntegerField()
    title_app = models.CharField(max_length=100)
    dates_posted =  models.DateTimeField(default=timezone.now)
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.price
    

class test_t(models.Model):
    product = models.CharField(max_length=50)
    
    def __str__(self):
        return self.product
    
    