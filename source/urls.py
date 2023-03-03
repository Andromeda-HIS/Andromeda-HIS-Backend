# from django.conf.urls import re_path
from django.urls import path, include
from .views import (
    AdminApiView,
)

urlpatterns = [
    path('adminlogin', AdminApiView.as_view()),
]