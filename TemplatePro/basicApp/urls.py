from django.urls import path
from basicApp import views

app_name = "basicApp"

urlpatterns = [
    path('home', views.home, name='home'),
    path('base', views.base, name="base"),
    path('help', views.help, name='help')
]