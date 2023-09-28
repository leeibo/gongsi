from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # 自动增长的产品ID
    name = models.CharField(max_length=255)  # 产品名称，最大长度为255个字符
    specification = models.CharField(max_length=255)  # 产品规格，最大长度为255个字符
    level = models.CharField(max_length=50)  # 产品级别，最大长度为50个字符
    weight = models.DecimalField(max_digits=10, decimal_places=2)  # 产品重量，最多10位数字和2位小数
    kind = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

