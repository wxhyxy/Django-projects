# coding = utf-8

# 登录接口，使用Django auth库里面的方法校验账号，密码，获取参数，判断账号密码，实现登录接口

from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate


def sigin(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 连接Django数据库校验
    user = authenticate(username=userName, passWord=passWord)

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请用管理员账号登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已被禁用'})
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或密码错误'})


def signout(request):
    logout(request)
    return JsonResponse({'ret': 0})