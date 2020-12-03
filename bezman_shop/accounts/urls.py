from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('customers/',customerList,name='customers'),
    path('customers/<int:customer_id>/',getCustomer,name='customer'),
    path('customercreate/',createCustomer,name='customercreate'),
]