from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='Данные авторизации', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.last_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'