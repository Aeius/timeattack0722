from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("이름")
    description = models.TextField("설명")
    price = models.ImageField("가격")
    date = models.DateField("날짜")
    is_active = models.BooleanField("활성화여부")