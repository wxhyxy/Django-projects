# coding = utf-8
# author = 王瑞

from django.http import JsonResponse
from django.db.models import F
from django.db import IntegrityError, transaction

from common.models import Order, OrderMedicine

from django.db.models import F

import json


def dispatcher(request):
    # 根据session判断用户是否登陆的管理员用户
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/mgr/sign.html'},
            status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'
        }, status=302)

    # 将请求参数统一放入request的params属性中，方便后续处理
    # GET请求参数在request对象的GET属性中
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求参数从request对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_order':
        return listorder(request)
    elif action == 'add_order':
        return addorder(request)

    else:
        return JsonResponse({
            'ret': 1,
            'msg': '不支持该类型http请求'
        })


def addorder(request):
    info = request.params['data']

    # 从请求消息中 获取要添加订单信息
    # 并且插入到数据库
    # Django 实现数据库事务操作
    with transaction.atomic():
        new_order = Order.objects.create(name=info['name'], customer_id=info['customerid'])

        batch = [OrderMedicine(order_id=new_order.id, medicine_id=mid, amount=1)
                 for mid in info['medicineids']]
        OrderMedicine.objects.bulk_create(batch)

    return JsonResponse({'ret': 0, 'id': new_order.id})


def listorder(request):
    qs = Order.objects \
        .annotate(
        customer_name=F('customer__name'),
        medicines_name=F('medicines__name')
    ) \
        .values(
        'id', 'name', 'create_date', 'customer_name', 'medicines_name'
    )

    # 将QuerySet对象转化为list类型
    retlist = list(qs)

    # 可能有ID 相同，药品不同的订单记录，需要合并
    newlist = []
    id2order = {}
    for one in retlist:
        orderid = one['id']
        if orderid not in id2order:
            newlist.append(one)
            id2order[orderid] = one
        else:
            id2order[orderid]['medicines_name'] += ' | ' + one['medicines_name']

        return JsonResponse({'ret':0, 'retlist': newlist})
