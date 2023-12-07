from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Sum
from .models import Employee, Product, LineItem
from .serializers import EmployeeSerializer, ProductSerializer, OrderReportSerializer
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from rest_framework.views import APIView

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderReportView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        skus = serializer.validated_data['skus']
        start_date = serializer.validated_data['date_range']['start']
        end_date = serializer.validated_data['date_range']['end']

        data = []
        total_quantity = {}

        current_date = start_date
        while current_date <= end_date:
            daily_data = []
            for sku in skus:
                quantity = LineItem.objects.filter(
                    product__sku=sku,
                    order__datetime__date=current_date
                ).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

                daily_data.append({'product': sku, 'sold_quantity': quantity})

                # Accumulate total quantity for each SKU
                total_quantity[sku] = total_quantity.get(sku, 0) + quantity

            data.append({'date': current_date.strftime('%Y-%m-%d'), 'data': daily_data})
            current_date += timedelta(days=1)

        # Adding total row
        data.append({'date': 'Total', 'data': [{'product': sku, 'sold_quantity': total_quantity.get(sku, 0)} for sku in skus]})

        return Response(data, status=status.HTTP_200_OK)

