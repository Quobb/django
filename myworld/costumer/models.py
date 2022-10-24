
from django.db import models

# Create your models here.
class customer(models.Model):
    name =  models.CharField(max_length = 200,null=True)
    phone = models.CharField(max_length = 200,null=True)
    email = models.CharField(max_length = 200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name

class tag(models.Model):
    name =  models.CharField(max_length = 200,null=True)

    def __str__(self):
        return self.name
class product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    name = models.CharField(max_length = 200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length = 200,null=True,choices=CATEGORY)
    description =  models.CharField(max_length = 200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(tag)
   
    def __str__(self):
        return self.name
class order(models.Model):
    STATUS=(
         ('pending','pending'),
         ('out for delivery','out for delivery'),
         ('Delivered','Delivered'),
    )
    product = models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    customer = models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length = 200,null=True,choices=STATUS)
   