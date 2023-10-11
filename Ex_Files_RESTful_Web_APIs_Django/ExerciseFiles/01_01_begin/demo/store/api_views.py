from rest_framework.generics import ListAPIView
from store.models import Product
from store.serialiser import ProductSerialiser


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser
    