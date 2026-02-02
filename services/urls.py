from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    # This path takes the name of the service as a parameter
    path('contact/<str:service_name>/', views.service_contact, name='service_contact'),
]