# coding = utf-8
# author = 王瑞

from django.conf.urls import url
from .views import *
from .customer import *

urlpatterns = [
    url('customer', dispather)
]
