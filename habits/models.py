from datetime import timedelta

from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    CHOICES = {
        "DAY": "Day",
        "WEEK": "Week"
    }

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Хозяин привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='Место выполнения привычки', help_text='Укажите место выполнения привычки', **NULLABLE)
    start_time = models.DateTimeField(verbose_name='Время начала', help_text='Во сколько необходимо выполнять привычку', **NULLABLE)
    habit = models.CharField(max_length=255, verbose_name='Привычка', help_text='Опишите привычку')
    sing_habit = models.BooleanField(verbose_name='Признак привычки', help_text='Укажите, если привычка с вознаграждением')
    related_habit = models.OneToOneField('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE, related_name='rel_habit')
    periodicity = models.CharField(max_length=10, choices=CHOICES, verbose_name='Периодичность привычки', default=CHOICES.get('DAY'))
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Вознаграждение за привычку')
    time_to_complete = models.DurationField(default=timedelta(seconds=120), verbose_name='Длительность выполнения привычки')
    sing_publicity = models.BooleanField(default=False, verbose_name='Опубликовано', help_text='Отметьте, если нужно опубликовать')
    date_last_send = models.DateField(verbose_name='Дата последней отправки', help_text='Укажите дату последней отправки', **NULLABLE)

    class Mete:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'Я буду {self.habit} в {self.start_time} в {self.place}'


