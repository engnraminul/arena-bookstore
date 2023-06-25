from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Cart, CartItem
from book.urls import *
from book.models import Book
from .models import Cart
from book.views import book_list
from django.http import HttpResponse


# Create your views here.


def cart_form(request, id):
    book = Book.objects.get(id=id)
    context={
        'book': book,
    }
    return render(request, 'cart/cart_form.html', context)



def add_to_cart(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

        # Get the user's cart or create a new one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Check if the book is already in the cart
        cart_item, created = cart.cartitem_set.get_or_create(book=book)

        # Update the quantity of the cart item
        cart_item.quantity += quantity
        cart_item.save()

        return render(request, 'cart/cart_view.html', {'cart': cart_item})

    return render(request, 'book/book_list.html', {'book': book})

def cart_view(request):
    cart = CartItem.objects.filter(cart__user=request.user)
    return render(request, 'cart/cart_view.html', {'cart': cart})