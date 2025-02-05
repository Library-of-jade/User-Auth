from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('nickname_check', views.nickname_check, name='nickname_check'),
    path('email_check', views.email_check, name='email_check'),
    path('email_confirm', views.email_confirm, name='email_confirm'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('search_pw', views.search_pw, name='search_pw'),
    path('nickname_change', views.nicknamechange, name='nickname_change'),
    path('pw_change', views.pwchange, name='pwchange'),
    path('profile_pic_change', views.profile_pic_change, name='profile_pic_change'),
    path('inactive', views.inactive, name='inactive'),

    path('refresh_jwt', views.refresh_jwt, name='refresh_jwt'),
    path('remove_jwt', views.remove_jwt, name='remove_jwt')
]