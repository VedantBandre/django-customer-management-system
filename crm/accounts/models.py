from django.db import models

# Create your models here.

# Customers Table
class Customers(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # So we can display customer name in the table rather than Object
    def __str__(self):
        return self.name


# Tags
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    # So we can display tag in the table rather than Object
    def __str__(self):
        return self.name
  

# Products Table
class Products(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    # So we can display Products in the table rather than Object
    def __str__(self):
        return self.name


# Orders Table
class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    
    customer = models.ForeignKey(Customers, null=True, on_delete= models.SET_NULL)
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)