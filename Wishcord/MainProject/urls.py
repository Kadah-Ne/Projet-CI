from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("groupList", views.groupList, name="groupList"),
    path("groupeView", views.groupView, name="groupView"),
    path("groupManage", views.groupManage, name="groupManage"),
    path("adminPage", views.adminPage, name="adminPage"),
]