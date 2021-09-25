"""Skyterest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from Service.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/',include('Service.urls'))
    path('',Skyterest_Home,name='HOME'),
    path('Service/',Skyterest_Services_View,name='SERVICE'),
    path('Service_Type/',Skyterest_Service_Tpye,name='SERVICETYPE'),
    path('Service_Type_Detail/',Skyterest_Service_Tpye_Detail,name='SERVICETYPEDETAIL'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
