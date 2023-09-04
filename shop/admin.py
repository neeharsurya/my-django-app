from django.contrib import admin
from .models import Products
from .models import Order
# from .models import Order_details

# Register your models here.
admin.site.register(Products)
admin.site.register(Order)
# admin.site.register(Order_details)