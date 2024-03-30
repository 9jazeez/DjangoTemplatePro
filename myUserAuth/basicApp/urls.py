from django.urls import path
from basicApp import views

app_name = "basicApp"

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.user_login, name='login')
]