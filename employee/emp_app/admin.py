from django.contrib import admin
from .models import Employee,Product, Order, LineItem

admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(LineItem)
