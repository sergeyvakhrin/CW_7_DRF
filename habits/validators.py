from datetime import timedelta

from rest_framework.serializers import ValidationError


def validata_time_complete(value):
    """ Валидация вводимого времени выполнения """
    if value > timedelta(seconds=120):
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")
