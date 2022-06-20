"""Checklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls, name='django_admin'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework_auth'),
    path('api/', include('api.urls'), name='check_list_api_end_points'),
    path('auth/', include('user.urls'), name='authentication'),
    path('openapi', get_schema_view(
        title="Google Keep Clone API",
        description="API Docs!",
        version="2.0.0"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

]
