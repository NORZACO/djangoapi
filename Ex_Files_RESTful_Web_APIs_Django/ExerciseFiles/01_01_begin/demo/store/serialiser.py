from rest_framework import serializers
from store.models import Product


class ProductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'description', 'price', 'sale_start', 'sale_end')
        #Not included field('photo', # 'is_on_sale', # 'current_price', # 'get_rounded_price',)
        # read_only_fields = ('is_on_sale', 'current_price', 'get_rounded_price',)
        
        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['is_on_sale'] = instance.is_on_sale()
            data['current_price'] = instance.current_price()
            data['get_rounded_price'] = instance.get_rounded_price()
            return data
    

