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
    path("api/v1/products/create", product_views_api.ProductCreateAPIView.as_view()),
    # path(
    #     "api/v1/products/<int:id>/destroy",
    #     product_views_api.ProductDestroyAPIView.as_view(),
    # ),
    path(
        "api/v1/products/<int:id>/",
        product_views_api.ProductRetrieveUpdateDestroyAPIView.as_view(),
    ),
    # stats
    path(
        "api/v1/products/<int:id>/stats/",
        product_views_api.ProductStatsAPIView.as_view(),
    ),
    # quizy
    path("api/v1/quizy/", quizy_views_api.QuizyListAPIView.as_view()),
]
