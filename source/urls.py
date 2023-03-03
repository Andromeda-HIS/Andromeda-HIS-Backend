# from django.conf.urls import re_path
from django.urls import path, include
from .views import (
    LoginApiView,
)

urlpatterns = [
    path('',LoginApiView.as_view()),
]