# -*- coding: utf-8 -*-
from django.urls import path
from django.urls import include
from rest_framework.authtoken import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', include('swagger.urls')),
]
