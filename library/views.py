from .models import Book, BookCategory
from django.views.generic import ListView
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin




class AllBooks(LoginRequiredMixin, ListView):
    paginate_by = 20
    model = Book
    template_name = 'library/lib.html'
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super(AllBooks, self).get_context_data(**kwargs)
        context['categories'] = BookCategory.objects.all()
        return context


class SearchBookView(ListView):
    paginate_by = 20
    model = Book
    template_name = 'library/lib.html'
    context_object_name = "books"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Book.objects.filter(Q(name__icontains=query))
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BookCategory.objects.all()
        return context

class CategoryBookView(ListView):
    paginate_by = 20
    model = Book
    template_name = 'library/lib.html'
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BookCategory.objects.all()
        return context

    def get_queryset(self):  # new
        return Book.objects.filter(category__slug=self.kwargs['slug'])
    
