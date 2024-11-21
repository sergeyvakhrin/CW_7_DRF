from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        max_length=255, unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    tg_chat_id = models.CharField(
        max_length=50,
        help_text="Укажите телеграм chat-id",
        verbose_name="Телеграм chat-id",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
