from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_index, name="main"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path("profitcenter/", views.profit_center, name="profitcenter"),
    path("listall/", views.list_all, name="listall"),
    path("delete/<str:pk>", views.delete_profit, name="deleteprofit"),
    path("update/<str:pk>", views.update_profit, name="updateprofit"),

    path("businessobjective/", views.business_objective, name="businessobjective"),
    path("businesslist/", views.business_objective_list, name="listbusiness"),
    path("businessdelete/<str:pk>", views.delete_business_objective, name="deletebusiness"),
    path("business_update/<str:pk>", views.update_business_objective, name="updatebusiness"),

    path("bizneed/", views.bizneed, name="bizneed"),
    path("listbizneed/", views.list_bizneed, name="listbizneed"),
    path("bizneeddelete/<str:pk>", views.delete_bizneed, name="deletebizneed"),
    path("bizneed_update/<str:pk>", views.update_bizneed, name="updatebizneed"),
]
