# from django.conf.urls import re_path
from django.urls import path, include
from .views import (
    LoginApiView,
    Admin_Functions,
)

urlpatterns = [
    path('login/',LoginApiView.as_view()),
    path('admin/',Admin_Functions.as_view()),
]