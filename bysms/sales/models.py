from django.db import models


# Create your models here.
class Customer(models.Model):
    # 用户名，电话和地址
    user_name = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_addr = models.CharField(max_length=200)

