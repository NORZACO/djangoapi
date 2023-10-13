from rest_framework.generics import ListAPIView, CreateAPIView
# RetrieveAPIView, UpdateAPIView, DestroyAPIView
from store.serialisers.products_serialiser import ProductSerialiser
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
    serializer_class = ProductSerialiser
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
    serializer_class = ProductSerialiser
    # create method
    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get("price")
            if price is not None and float(price) <= 0.0:
                raise ValidationError({"price": "Must be above $0.00"})
        except ValueError:
            raise ValidationError({"price": "A valid number is required"})
        return super().create(request, *args, **kwargs)
    