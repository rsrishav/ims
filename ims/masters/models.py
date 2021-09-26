from django.db import models
from django.core import serializers
import json


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    @staticmethod
    def get_all_records():
        data = Category.objects.all()
        data = json.loads(serializers.serialize("json", data))
        return data

    @staticmethod
    def get_one(pk):
        data = Category.objects.get(pk=pk)
        data = json.loads(serializers.serialize("json", [data]))[0]
        data = {"pk": data["pk"], "title": data["fields"]["title"], "description": data["fields"]["description"]}
        return data


class Style(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    @staticmethod
    def get_all_records():
        data = Style.objects.all()
        data = json.loads(serializers.serialize("json", data))
        return data


class Color(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    @staticmethod
    def get_all_records():
        data = Color.objects.all()
        data = json.loads(serializers.serialize("json", data))
        return data


class Size(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    @staticmethod
    def get_all_records():
        data = Size.objects.all()
        data = json.loads(serializers.serialize("json", data))
        return data


class Package(models.Model):
    title = models.CharField(max_length=50)

    @staticmethod
    def get_all_records():
        data = Package.objects.all()
        data = json.loads(serializers.serialize("json", data))
        return data


class HSNCode(models.Model):
    code = models.CharField(max_length=50, default="None")  # model
    hsn_code = models.CharField(max_length=50)
    tax_perc = models.FloatField(max_length=50)
    limit_price = models.FloatField(max_length=50)
    above_limit_tax_perc = models.FloatField(max_length=50)
    description = models.CharField(max_length=250)

    @staticmethod
    def get_all_records():
        data = HSNCode.objects.all()
        data = json.loads(serializers.serialize("json", data))
        return data
