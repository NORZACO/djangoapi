from django.contrib import admin  # noqa: F401

# Register your models here.
from store.models import Product, ShoppingCart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'sale_start', 'sale_end', 'photo')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('sale_start', 'sale_end')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('address',)
    fields = ('name', 'address')


admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)



