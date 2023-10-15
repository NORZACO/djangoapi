
from rest_framework.renderers import JSONRenderer
import json
from store.models.products_models import ShoppingCart, ShoppingCartItem, Product
from store.serialisers.products_serialiser import ProductSerialiser



# Retrieve a product from the database
product = Product.objects.all()[0]
serialiser = ProductSerialiser()
data = serialiser.to_representation(product)
print(data)
# <Product object (1) "Mineral Water Strawberry!">

# JSONRenderer
renderer = JSONRenderer()
print(renderer.render(data))


















# -----------------------------------------------------------------------

# Import necessary modules and objects
# Retrieve a product from the database
product =  Product.objects.all().first()

# Create a shopping cart and save it
cart = ShoppingCart()
cart.save()

# Create a shopping cart item with the product and quantity, then save it
item = ShoppingCartItem(shopping_cart=cart, product=product, quantity=5)
item.save()

# Correct the typo in 'item.save()'

# Serialize the product using the correct spelling
serializer = ProductSerialiser(product)

# Print the serialized data with correct indentation
print(json.dumps(serializer.data, indent=3))
# {
#    "id": 1,
#    "name": "programming",
#    "description": "I'm sorry, I'm not sure what you want me to write about. Could you please provide me with more information or a specific topic to write about?",  # noqa: E501
#    "price": 300.0,
#    "sale_start": "2023-10-12T21:22:31Z",
#    "sale_end": "2023-10-12T21:22:33Z",
#    "is_on_sale": false,
#    "current_price": 300.0
# }

