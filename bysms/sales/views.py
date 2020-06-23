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


# 创建前端静态模板

html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>
        
        %s
        
        
        </table>
    </body>
</html>
'''


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url是否有user_phone参数
    ph = request.GET.get('user_phone', None)
    # 判断是否为空，过滤数据
    if ph:
        qs = qs.filter(user_phone=ph)

    reStr = ''
    for customer in qs:
        reStr += '<tr>'

        for name, value in customer.items():
            reStr += f'<td>{value}</td>'

        reStr += '</tr>'

    return HttpResponse(html_template % reStr)


# 使用python模板来操作

def listcustustomer1(request):
    # 返回Qureyset对象
    qs = Customer.objects.all()

    ph = request.GET.get('user_phone', None)

    if ph:
        qs = qs.filter(user_phone=ph)

    return render(request, 'index.html', context={'title': '首页', 'qs': qs})
