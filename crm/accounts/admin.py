from django.contrib import admin

# Register your models here.

# Registering the models created in models.py
from .models import *
admin.site.register(Customers)
admin.site.register(Tag)
admin.site.register(Products)
admin.site.register(Orders)