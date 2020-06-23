# coding = utf-8
# author = '王瑞'

from django.conf.urls import url
from .views import *

urlpatterns = [
    # url('', index),
    url('customer/', listcustomer),
    url('customers/', listcustomers),
    url('customer1/', listcustustomer1)
]
