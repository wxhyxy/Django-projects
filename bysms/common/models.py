from django.db import models

# Create your models here.
import datetime


# Create your models here.
class Customer(models.Model):
    # 用户名，电话和地址
    user_name = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_addr = models.CharField(max_length=200)


class Medicine(models.Model):
    # 药品编号，名称，描述
    name = models.CharField(max_length=200)
    sn = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)


class Order(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    # 创建日期
    create_date = models.DateTimeField(default=datetime.datetime.now)
    # 客户
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # 订单购买药品和药品为多对多的关系
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')


class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    # 订单中的数量
    amount = models.PositiveIntegerField()

