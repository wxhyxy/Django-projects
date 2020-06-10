from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import hashlib


# Create your views here.
def index(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    reStr = ''

    for customer in qs:
        for name, value in customer.items():
            reStr += f'{name}:{value}'

        reStr += '<br>'

    return HttpResponse(reStr)


def listcustomer(request):
    # 返回QuerSet对象，查询参数phonenumber字段返回值,根据字段过滤
    qs = Customer.objects.values()

    ph = request.GET.get('user_phone', None)

    if ph:
        qs = qs.filter(user_phone=ph)

    reStr = ''
    for customer in qs:
        for name, value in customer.items():
            reStr += f'{name}:{value} |'

        reStr += '<br>'

    return HttpResponse(reStr)
