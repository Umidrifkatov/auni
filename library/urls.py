from django.urls import path
from .views import book_detail, lib



urlpatterns = [
    path('', lib),
    path('book/<slug:book_slug>', book_detail, name='book'),

]