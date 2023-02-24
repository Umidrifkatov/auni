from django.contrib import admin
from .models import BookCategory, Book






@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ('name',)}




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    prepopulated_fields = {"slug": ('name',)}


