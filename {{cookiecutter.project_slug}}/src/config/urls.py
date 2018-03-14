# -*- coding: utf-8 -*-
from django.urls import path
from django.urls import include
from rest_framework.authtoken import views
from django.http import HttpResponse

urlpatterns = [
    path('health-check/', lambda r: HttpResponse()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', include('swagger.urls')),
]
