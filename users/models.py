from django.db import models


class User(models.Model):
    username = None

    email = models.EmailField(max_length=255, unique=True, verbose_name='Почта', help_text='Укажите почту')

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
