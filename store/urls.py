from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_page'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment/', views.payment_page, name='payment_page'),
    path('update-cart/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart'),
]