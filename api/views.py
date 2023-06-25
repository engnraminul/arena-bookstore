from django.shortcuts import render
from rest_framework import viewsets
from book.models import Book
from .serializers import BookSerializer
from cart.models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer