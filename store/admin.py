from django.contrib import admin  # noqa: F401

# Register your models here.
from store.models.products_models import Product, ShoppingCart
from store.models.quizy_models import Quiz

#product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'sale_start', 'sale_end', 'photo')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('sale_start', 'sale_end')


#shopping cart
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('address',)
    fields = ('name', 'address')



# quiz
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'description')
    ordering = ('question',)
    search_fields = ('question',)
    list_filter = ('description',)
    fields = ('question', 'description')



admin.site.register(Quiz)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)



