from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # RetrieveAPIView,
    UpdateAPIView,
    # DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)

# response
from rest_framework.response import Response
from store.serialisers.products_serialiser import (
    ProductSerializer,
    ProductStateSerializer,
)
from store.models.products_models import Product

# filter
from django_filters.rest_framework import DjangoFilterBackend

# search
from rest_framework.filters import SearchFilter

# paginantion
from rest_framework.pagination import LimitOffsetPagination

# validation
from rest_framework.exceptions import ValidationError


# product pagination
class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter
    filterset_fields = ["name", "description"]
    # search
    search_fields = ["name", "description"]
    # pagination
    pagination_class = ProductPagination

    def get_queryset(self):
        on_sale = self.request.query_params.get("on_sale", None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == "true":
            from django.utils import timezone

            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset


# creaye product
class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer

    # create method
    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get("price")
            if price is not None and float(price) <= 0.0:
                raise ValidationError({"price": "Must be above $0.00"})
        except ValueError:
            raise ValidationError({"price": "A valid number is required"})
        return super().create(request, *args, **kwargs)


# destroy product version 1
# class ProductDestroyAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiser
#     lookup_field = "id"

#     # delete method
#     def delete(self, request, *args, **kwargs):
#         product_id = request.data.get("id")
#         response = super().delete(request, *args, **kwargs)
#         if response.status_code == 204:
#             # delete cache based on product id
#             from django.core.cache import cache
#             cache.delete("product_data_{}".format(product_id))
#         return response


# product retrieve update and destroy version 2
class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    # delete method
    def delete(self, request, *args, **kwargs):
        product_id = request.data.get("id")
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            # delete cache based on product id
            from django.core.cache import cache

            cache.delete("product_data_{}".format(product_id))
        return response

    # update method || Creating an UpdateAPIView subclass
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            # delete cache based on product id
            from django.core.cache import cache

            product = response.data
            cache.set(
                "product_data_{}".format(product["id"]),
                {
                    # STORE INFOTMATION IN CACHE
                    "name": product["name"],
                    "description": product["description"],
                    "price": product["price"],
                },
            )
        return response


# update product
class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    # update method
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            # delete cache based on product id
            from django.core.cache import cache

            product = response.data
            cache.set(
                "product_data_{}".format(product["id"]),
                {
                    "name": product["name"],
                    "description": product["description"],
                    "price": product["price"],
                },
            )
        return response


# product state
class ProductStatsAPIView(GenericAPIView):
    lookup_field = "id"
    serializer_class = ProductStateSerializer
    queryset = Product.objects.all()

    def get(self, request, format=None, id=None):
        obj = self.get_object()  # noqa: F841
        serializer = ProductStateSerializer(
            {
                "stats": {
                    "2019-01-01": [
                        4, 7, 12
                    ],
                    "2019-01-02": [
                        6, 8, 11
                    ],
                    "2019-01-03": [
                        5, 6, 13
                    ],
                }
            }
        )
        return Response(serializer.data)
