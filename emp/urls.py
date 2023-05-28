# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("home/",emp_home),
    path("login/",Login_user.as_view()),
    path("update/<int:id>/",Update.as_view()),
    path("delete/<int:id>/",delete)
]
