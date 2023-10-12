from django.urls import path
from store.views import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.show, name='show-product'),
    path('cart', views.cart, name='cart'),

]
