from django.shortcuts import render
from book.models import Book

# Create your views here.


def cart_form(request, id):
    book = Book.objects.get(id=id)
    context={
        'book': book,
    }
    return render(request, 'cart/cart_form.html', context)

def add_to_cart(request):
    pass