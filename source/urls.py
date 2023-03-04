# from django.conf.urls import re_path
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/',LoginApiView.as_view()),
    path('admin/',Admin_Functions.as_view()),
    path('receptionist/<str:method>/',Receptionist_Functions.as_view())
]