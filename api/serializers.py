from rest_framework import serializers
from book.models import Book
from cart.models import Cart, CartItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cartitem_set = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'