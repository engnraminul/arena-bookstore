from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart-form/<int:id>/', views.cart_form, name='cart_form'),
]