from rest_framework import serializers
from .models import Employee, Product

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'job_title', 'employment_status', 'sub_unit']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'sku']

class OrderReportSerializer(serializers.Serializer):
    skus = serializers.ListField(child=serializers.CharField())
    date_range = serializers.DictField(child=serializers.DateField())
