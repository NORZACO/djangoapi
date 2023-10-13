from django.urls import path
from store.views import views, product_views_api, quizy_views_api


urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:id>", views.show, name="show-product"),
    path("cart", views.cart, name="cart"),
]


# APIS
urlpatterns += [
    path("api/v1/products/", product_views_api.ProductListAPIView.as_view()),
    # quizy
    path("api/v1/quizy/", quizy_views_api.QuizyListAPIView.as_view()),
]
