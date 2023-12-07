import random
from datetime import datetime, timedelta
import string
from django.core.management.base import BaseCommand
from emp_app.models import Product, Order, LineItem

class Command(BaseCommand):
    help = 'Populate dummy orders with random products, orders, and line items.'

    def handle(self, *args, **options):
        # Create 200 random products with unique SKUs
        products = []
        for _ in range(200):
            sku = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            product = Product.objects.create(sku=sku, name=f'Product {len(products) + 1}')
            products.append(product)

        # Create 1000 random orders in the last 2 years
        orders = []
        for _ in range(1000):
            order_date = datetime.now() - timedelta(days=random.randint(0, 730))
            order = Order.objects.create(datetime=order_date)
            orders.append(order)

        # Create 20000 random line items against those products and orders
        for _ in range(20000):
            product = random.choice(products)
            order = random.choice(orders)
            quantity = random.randint(1, 10)
            LineItem.objects.create(order=order, product=product, quantity=quantity)

        self.stdout.write(self.style.SUCCESS('Dummy orders populated successfully.'))
