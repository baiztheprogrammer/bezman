from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('customers/',customerList,name='customer'),
    path('customers/<int:customer_id>/',getCustomer,name='customer'),
    path('register/',register,name='register'),
    path('login/',auth,name='login'),
    path('logout/',logout_page,name='logout')
]