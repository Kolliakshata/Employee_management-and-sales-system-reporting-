from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.CharField(max_length=20, choices=[("Active", "Active"), ("Retired", "Retired"), ("Internship", "Internship")], blank=True, null=True)
    sub_unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()