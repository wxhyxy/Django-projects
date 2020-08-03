# coding = utf-8
# author = 王瑞

from django.conf.urls import url
from .views import *
from .customer import *
from .sign_in_out import *

urlpatterns = [
    url('customer', dispather),
    url('signin', signin),
    url('signout', signout)
]
