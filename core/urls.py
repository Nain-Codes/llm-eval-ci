from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_index, name="main"),
    path('login', views.login_user, name="login"),
    path('register', views.register, name="register"),
    path("profitcenter/", views.profit_center, name="profitcenter"),
    path("listall/", views.list_all, name="listall"),
    path("delete/<str:pk>", views.delete_profit, name="deleteprofit"),
    path("update/<str:pk>", views.update_profit, name="updateprofit"),
]
