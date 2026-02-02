from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path("", views.home, name="soil_cam_home"),
    path("analyze/", views.analyze, name="soil_cam_analyze"),
    path("result/", lambda r: render(r, "soil_cam/result.html"), name="soil_cam_result"),
]
