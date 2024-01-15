from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", 'account', 'create_time', 'maintenance_time', "classification", "depart"]

class CityModelForm(BootStrapModelForm):
    class Meta:
        model = models.City
        fields = ["name", "count", "img"]

class PrettyModelForm(BootStrapModelForm):
    class Meta:
        model = models.PrettyNum
        # fields = "__all__"
        # exclude = ['level']
        fields = ["name", "mobile", 'price', 'classification', 'status']

