from django.db import models
from masters import models as master_models


# Create your models here.
class AddProduct(models.Model):
    code = models.CharField(max_length=50)
    product_id = models.IntegerField()
    category = models.ForeignKey(master_models.Category, on_delete=models.CASCADE)  # model
    article = models.CharField(max_length=50, default="NA")  # model
    hsn_code = models.ForeignKey(master_models.HSNCode, on_delete=models.CASCADE)  # model
    description = models.CharField(max_length=250)
    product_type = models.CharField(max_length=50)
    bar_code = models.CharField(max_length=50)
    sup_price = models.FloatField(max_length=50)
    cust_price = models.FloatField(max_length=50)
    disc_per = models.FloatField(max_length=50)
    disc_amount = models.FloatField(max_length=50)
    color = models.ForeignKey(master_models.Color, on_delete=models.CASCADE)  # model
    style = models.ForeignKey(master_models.Style, on_delete=models.CASCADE)  # model
    ex_date = models.DateField(max_length=50)
    qty = models.IntegerField()
