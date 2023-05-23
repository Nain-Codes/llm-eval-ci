from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_index, name="main"),
    path('login', views.login_user, name="login"),
    path('register', views.register, name="register"),
]
