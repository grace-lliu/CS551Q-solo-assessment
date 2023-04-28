from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating_count_tot = models.IntegerField()
    user_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.id} - {self.currency} - {self.price} - {self.rating_count_tot} - {self.user_rating}"

    class Meta:
        db_table = 'product'    

class ProductDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_bytes = models.BigIntegerField()
    rating_count_ver = models.IntegerField()
    user_rating_ver = models.DecimalField(max_digits=3, decimal_places=1)
    ver = models.CharField(max_length=20)
    cont_rating = models.CharField(max_length=10)
    prime_genre = models.CharField(max_length=50)
    sup_devices_num = models.IntegerField()
    ipadSc_urls_num = models.IntegerField()
    lang_num = models.IntegerField()
    vpp_lic = models.BooleanField()

    def __str__(self):
        return f"{self.product_id.id} - {self.size_bytes} - {self.rating_count_ver} - {self.user_rating_ver} - {self.ver} - {self.cont_rating} - {self.prime_genre} - {self.sup_devices_num} - {self.ipadSc_urls_num} - {self.lang_num} - {self.vpp_lic}"
    
    class Meta:
        db_table = 'product_detail'
