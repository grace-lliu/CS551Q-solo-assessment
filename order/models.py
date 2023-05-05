from django.db import models


# class Order(models.Model):
#     user_id = models.IntegerField()
#     product_id = models.CharField(max_length=100)
#     product_name = models.CharField(max_length=100)
#     product_price = models.CharField(max_length=100)
#     product_quantity = models.IntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Order #{self.user_id} ({self.product_name} x {self.product_quantity})'

#     class Meta:
#         db_table = 'order'


class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return f'{self.user_id} has {self.product_quantity} {self.product_name}(s) in cart'

    class Meta:
        db_table = 'cart'

class Order(models.Model):
    user_id = models.IntegerField()
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.user_id} ({self.product_name} x {self.product_quantity})'

    class Meta:
        db_table = 'order'