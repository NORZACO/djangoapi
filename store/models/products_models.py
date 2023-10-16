from django.utils import timezone
from django.db import models


class Product(models.Model):
    DISCOUNT_RATE = 0.10
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True, default=None, upload_to="products")



    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()
    
    #  get_price
    def get_price(self):
        return self.current_price()

    def __repr__(self):
        return '<Product object ({}) "{}">'.format(self.id, self.name)
    

    # def __str__(self):
    #     return self.name


class ShoppingCart(models.Model):
    TAX_RATE = 0.13

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def subtotal(self):
        amount = 0.0
        for item in self.shopping_cart_items:
            amount += item.quantity * item.product.get_price()
        return round(amount, 2)

    def taxes(self):
        return round(self.TAX_RATE * self.subtotal(), 2)

    def total(self):
        return round(self.subtotal() * self.taxes(), 2)

    def __repr__(self):
        name = self.name or "[Guest]"
        address = self.address or "[No Address]"
        return '<ShoppingCart object ({}) "{}" "{}">'.format(self.id, name, address)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey( ShoppingCart, related_name="items", related_query_name="item", on_delete=models.CASCADE,)  # noqa: E501
    product = models.ForeignKey(Product, related_name="+", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart_items = models.ForeignKey(ShoppingCart, related_name="shopping_cart_items", related_query_name="shopping_cart_item", on_delete=models.CASCADE,)  # noqa: E501)

    def total(self):
        return round(self.quantity * self.product.current_price())

    def __repr__(self):
        return '<ShoppingCartItem object ({}) {}x "{}">'.format(
            self.id, self.quantity, self.product.name
        )
    


    # address model associated with the shopping cart model
    # class Address(models.Model):
    #     street = models.CharField(max_length=200)
    #     city = models.CharField(max_length=200)
    #     state = models.CharField(max_length=200)
    #     zip_code = models.CharField(max_length=200)
    #     country = models.CharField(max_length=200)
    #     shopping_cart = models.OneToOneField(
    #         ShoppingCart, on_delete=models.CASCADE, related_name="address"
    #     )

    #     def __repr__(self):
    #         return '<Address object ({}) "{} {}">'.format(
    #             self.id, self.street, self.city
    #         )

    #     def __str__(self):
    #         return self.street

