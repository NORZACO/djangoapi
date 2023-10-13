from store.models import Product
from rest_framework.renderers import JSONRenderer

product = Product.objects.all()[0]

from store.serialisers.products_serialiser import ProductSerialiser

serialiser = ProductSerialiser()
data = serialiser.to_representation(product)
print(data)
# <Product object (1) "Mineral Water Strawberry!">

# JSONRenderer
renderer = JSONRenderer()
print(renderer.render(data))
