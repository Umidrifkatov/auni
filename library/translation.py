from modeltranslation.translator import translator, TranslationOptions
from .models import BookCategory



class CategoryTO(TranslationOptions):
    fields = ('name',)

translator.register(BookCategory, CategoryTO)
