from rest_framework import serializers
from store.models.products_models import Product, ShoppingCartItem



class CartItemSerializer(serializers.ModelSerializer):
    # DEFINE WHAT FIELDS WE WANT TO SERIALIZE FROM THE PRODUCT MODEL
    # the attributes that we set in the two representation method and refactor them using serializer fields.  # noqa: E501
    # """work like a to_representation method in the Product model class"""
    class Meta:
        model = ShoppingCartItem
        fields = (
            "quantity",
            "product",
        )


class ProductSerialiser(serializers.ModelSerializer):
    #DEFINE WHAT FIELDS WE WANT TO SERIALIZE FROM THE PRODUCT MODEL
    # the attributes that we set in the two representation method and refactor them using serializer fields.  # noqa: E501
    # """work like a to_representation method in the Product model class"""
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    # photo = serializers.ImageField(default=None, max_length=None, allow_empty_file=True, use_url=True)  # noqa: E501
    # cart_items = serializers.SerializerMethodField()

    class Meta:
        model = Product
        # fields = ("id", "name", "description", "price", "sale_start", "sale_end", "is_on_sale", "current_price", "cart_items")  # noqa: E501
        fields = ("id", "name", "description", "price", "sale_start", "sale_end", "is_on_sale", "current_price")  # noqa: E501

        # AttributeError: 'ProductSerialiser' object has no attribute 'get_cart_items'
        def get_cart_items(self, instance):
            items = ShoppingCartItem.objects.filter(product=instance)
            # many=True because we want to return a list of items
            # many=False because we want to return a single item
            return CartItemSerializer(items, many=True).data 

        # Not included field('photo', # 'is_on_sale', # 'current_price', # 'get_rounded_price',)  # noqa: E501
        # def get_cart_items(self, instance):
        #     items = ShoppingCartItem.objects.filter(product=instance)
        #     return CartItemSerializer(items, many=True).data

        # Not included field('photo', # 'is_on_sale', # 'current_price', # 'get_rounded_price',)  # noqa: E501
        # read_only_fields = ('is_on_sale', 'current_price', 'get_rounded_price',)

        # def to_representation(self, instance):
        #     data = super().to_representation(instance)
        #     data["is_on_sale"] = instance.is_on_sale()
        #     data["current_price"] = instance.current_price()
        #     data["get_rounded_price"] = instance.get_rounded_price()
        #     return data

        # AttributeError: 'ProductSerialiser' object has no attribute 'get_cart_items'
