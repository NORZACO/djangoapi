from rest_framework.generics import ListAPIView
from store.serialisers.quizy_serialiser import QuizySerialiser
from store.models.quizy_models import Quiz
# filter
from django_filters.rest_framework import DjangoFilterBackend
# search
from rest_framework.filters import SearchFilter
# paginantion
from rest_framework.pagination import LimitOffsetPagination



# product pagination
class QuizyPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class QuizyListAPIView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizySerialiser
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter
    filterset_fields = ["question", "description"]
    # search
    search_fields = ["name", "description"]
    # pagination
    pagination_class = QuizyPagination


    # def get_queryset(self):
    #     return Product.objects.all()
    # def get_serializer_class(self):
    #     return ProductSerialiser
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
