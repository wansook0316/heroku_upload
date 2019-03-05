# from django.contrib import admin  #### 이녀석은 여기서는 필요없겠쥬? admin관리파일
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]
