# coding = utf-8
# author = 王瑞
import json
from django.http import JsonResponse
from ..sales.models import *


def dispather(request):
    # 将请求参数放入request的params属性中，根据请求方式获得属性
    if request.method == 'GET':
        request.params = request.method

    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    # 根据action来对函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return listcustomers(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型HTTP请求'})


def listcustomers(request):
    # 返回QuerySet对象，包含所有表记录
    qs = Customer.objects.values()
    # 将QuerySet对象转化为list类型
    retlist = list(qs)
    # 否则不能被转化为JSON字符串
    return JsonResponse({'ret': 0, 'retlist': retlist})


# 添加客户
def addcustomer(request):
    info = request.params['data']
    # 从请求中获取客户信息插入数据库
    record = Customer.objects.create(user_name=info['name'],
                                     user_phone=info['phonenumber'],
                                     user_addr=info['address'])

    return JsonResponse({'ret': 0, 'id': record.id})


# 修改客户信息
def modifycustomer(request):
    # 获取到客户信息，并进行修改操作
    customerid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据ID从数据库找到客户信息
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为%s的客户不存在' % customerid
        }

    if 'name' in newdata:
        customer.user_name = newdata['name']

    if 'phonenumber' in newdata:
        customer.user_phone = newdata['phonenumber']

    if 'address' in newdata:
        customer.user_addr = newdata['address']

    customer.save()

    return JsonResponse({'ret': 0})


# 删除客户
def deletecustomer(request):
    customerid = request.params['id']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为%s的客户不存在'
        }

    customer.delete()

    return JsonResponse({'reg': 0})

