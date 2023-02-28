from django.contrib import admin
from .models import BookCategory, Book
from modeltranslation.admin import TranslationAdmin







class BookCategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ('name',)}
admin.site.register(BookCategory, BookCategoryAdmin)




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    prepopulated_fields = {"slug": ('name',)}


