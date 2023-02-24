from django.shortcuts import get_object_or_404, render
from .models import Book

def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    return


def lib(request):
    return render(request, 'dashboard/dashbase.html')