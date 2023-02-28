from django.db import models
from django.urls import reverse





class BookCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория книг'
        verbose_name_plural = 'Категории книг'




class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    year = models.DateField(verbose_name='Год издания', null=True)
    desc = models.CharField(max_length=1000, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name='Категория')
    file = models.FileField(upload_to='books', verbose_name='Файл')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})

    def __unicode__(self):
        return '%name' % {'name': self.name}

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

