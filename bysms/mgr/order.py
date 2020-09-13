# coding = utf-8
# author = 王瑞

from django.http import JsonResponse
from django.db.models import F
from django.db import IntegrityError, transaction

from common.models import Order, OrderMedicine

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
        },status=302)

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