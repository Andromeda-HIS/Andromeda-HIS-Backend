"""Hospital_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# import sys
# sys.path.insert(0, 'F:/IIT Kharagpur/Third Year/6th Semester/DBMS Lab/Asgn-4/hms/Hospital_Management_System/source')
from django.contrib import admin
from django.urls import path,include
from source import urls as source_urls

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('',include(source_urls)),
]
