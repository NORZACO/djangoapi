# Description: Products Serialiser
from rest_framework import serializers
from store.models.products_models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    # only 100 product can needed
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ("product", "quantity")


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # put_anything = serializers.SerializerMethodField()
    photo = serializers.ImageField(default=None)
    price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00,
        max_value=100000,
        max_digits=None,
        decimal_places=2,
    )

    sale_start = serializers.DateTimeField(
        # test
        required=False,
        input_formats=["%I:%M %p %d %B %Y"],
        format=None,
        allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={"input_type": "text", "placeholder": "12:01 AM 28 July 2019"},
    )
    sale_end = serializers.DateTimeField(
         required=False,
        input_formats=["%I:%M %p %d %B %Y"],
        format=None,
        allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={"input_type": "text", "placeholder": "12:01 AM 28 July 2019"},
    )

    warranty = serializers.FileField(write_only=True, default=None)

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
            "current_price",
            "cart_items",
            # "put_anything",
            "photo",
            "warranty",
        )

    # get_cart_items
    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

    # get_put_anything
    # def get_put_anything(self, instance):
    #     items = ShoppingCartItem.objects.filter(product=instance)
    #     return CartItemSerializer(items, many=True).data

    # validate
    # def validate(self, instance, validated_data):
    #     if validated_data.get("warranty", None):
    #         instance.description += "\n\nWarranty information:\n"
    #         instance.description += b"; ".join(
    #             validated_data["warranty"].readlines()
    #         ).decode()
    #     return instance
    

    # create
    def create(self, validated_data):
        validated_data.pop("warranty")
        return Product.objects.create(**validated_data)
    


    # Validate method with 'attrs' argument
    def validate(self, attrs):
        if attrs.get("warranty", None):
            # Modify 'instance' if needed using 'attrs'
            attrs["description"] += "\n\nWarranty information:\n"
            attrs["description"] += b"; ".join(attrs["warranty"].readlines()).decode()
        return attrs


# product state serializer
class ProductStateSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        )
    )



