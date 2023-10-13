from rest_framework import serializers
from store.models.products_models import Product, ShoppingCartItem





class CartItemSerialiser(serializers.Serializer):
    class Meta:
        model = ShoppingCartItem
        fields = ("id", "quantity", "product")




class ProductSerialiser(serializers.ModelSerializer):
    # the attributes that we set in the two representation method and refactor them using serializer fields.  # noqa: E501
    """work like a to_representation method in the Product model class"""
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    # get_rounded_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    # carrt items


    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "sale_start",
            "sale_end",
            "is_on_sale",
            # "get_rounded_price",
            "current_price",
        ) 

        # def  get cart items
        def get_cart_items(self, instance):
            items = ShoppingCartItem.objects.filter(product=instance)
            return CartItemSerialiser(items, many=True).data
        


        # Not included field('photo', # 'is_on_sale', # 'current_price', # 'get_rounded_price',)  # noqa: E501
        # read_only_fields = ('is_on_sale', 'current_price', 'get_rounded_price',)

        # def to_representation(self, instance):
        #     data = super().to_representation(instance)
        #     data["is_on_sale"] = instance.is_on_sale()
        #     data["current_price"] = instance.current_price()
        #     data["get_rounded_price"] = instance.get_rounded_price()
        #     return data
