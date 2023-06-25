from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart-form/<int:id>/', views.cart_form, name='cart_form'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart-sucess/', views.cart_sucess, name='cart_sucess'),

]