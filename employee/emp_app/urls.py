from django.urls import path
from .views import EmployeeListView, ProductListView, OrderReportView

urlpatterns = [
    path('api/employee/', EmployeeListView.as_view(), name='employee-list'),
     path('api/data/products/', ProductListView.as_view(), name='product-list'),
     path('api/data/order-report/', OrderReportView.as_view(), name='order-report'),
]
