# from django.conf.urls import re_path
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',LoginApiView.as_view()),
    path('admin/',Admin_Functions.as_view()),
    path('receptionist/<str:method>/',Receptionist_Functions.as_view()),
    path('doctor/<str:method>/',Doctor_Functions.as_view()),
    path('clerk/<str:method>/',Clerk_Functions.as_view()),
    path('profile/<str:usertype>/',ProfileView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)