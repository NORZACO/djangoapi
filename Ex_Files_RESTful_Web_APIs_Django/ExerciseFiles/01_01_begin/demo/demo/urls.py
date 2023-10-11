from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.views
import store.api_views


urlpatterns = [
    path('ap/v1/products/', store.api_views.ProductListView.as_view(), name='products'),
] 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
