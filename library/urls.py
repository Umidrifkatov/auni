from django.urls import path
from .views import AllBooks, SearchBookView, CategoryBookView



urlpatterns = [
    path('', AllBooks.as_view()),
    path('search/', SearchBookView.as_view(), name='search_book'),
    path('category/<str:slug>', CategoryBookView.as_view(), name='category'),
    # path('book/<slug:book_slug>', book_detail, name='book'),

]