from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Style(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Color(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Size(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Package(models.Model):
    title = models.CharField(max_length=100)


class HSNCode(models.Model):
    code = models.CharField(max_length=50, default="None")  # model
    hsn_code = models.CharField(max_length=50)
    tax_perc = models.FloatField(max_length=50)
    limit_price = models.FloatField(max_length=50)
    above_limit_tax_perc = models.FloatField(max_length=50)
    description = models.CharField(max_length=250)
