from django.urls import path
from django.urls import re_path
from . import views
from .views import RegistrationAPIView
from .views import LoginAPIView

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('users/add/', views.AddUsers, name='add_users'),
    path('users/', views.GetUsers, name='get_users'),
    path('users/del/', views.DelUser, name = 'del_user'),
    path('user/', views.FindUser, name="find_user"),
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]