from store.models.products_models import Product
from rest_framework.test import APITestCase

# ProductCreateTestCase
class ProductCreateTestCase(APITestCase):
    def test_create_products(self):
        initial_products_count = Product.objects.count()
        product_attrs = {
            "name": "Test product",
            "description": "Test description",
            "price": "100.00",
        }
        response = self.client.post("/api/v1/products/create", product_attrs)
        if response.status_code != 201:
            print(response.data)

        self.assertEqual(
            Product.objects.count(),
            initial_products_count + 1,
        )

        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

        self.assertEqual(response.data["is_on_sale"], False)
        self.assertEqual(
            float(response.data["current_price"]), float(product_attrs["price"])
        )
