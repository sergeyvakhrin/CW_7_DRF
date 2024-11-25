from datetime import timedelta

from rest_framework import serializers
from rest_framework.serializers import ValidationError


def validata_time_complete(value):
    """Валидация вводимого времени выполнения"""
    if value > timedelta(seconds=120):
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class validate_type_habit:
    """Валидация на тип привычки"""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value, *args, **kwargs): # Todo: разобраться с передаваемыми данными. Тут какой-то огород
        sing_habit = value.get(self.field1)
        related_habit = value.get(self.field2)
        reward = value.get(self.field3)

        if sing_habit and related_habit is None and reward is not None:
            raise serializers.ValidationError(
                "Необходимо указать Связанную привычку и убрать вознаграждение. Либо убрать Признак приятной привычки."
            )
        if sing_habit and related_habit is None and reward is None:
            raise serializers.ValidationError("Необходимо указать Связанную привычку.")

        if sing_habit is False and related_habit is not None and reward is not None:
            raise serializers.ValidationError(
                "Необходимо указать Признак приятной привычки и убрать награду. "
                "Любо убрать связанную привычку."
            )
        if sing_habit and related_habit is not None and reward:
            raise serializers.ValidationError(
                "Убери Вознаграждение, у Приятной привычки уже есть Связанная привычка."
            )
        if sing_habit is False and related_habit is None and reward is None:
            raise serializers.ValidationError("Укажите Вознаграждение.")

        if sing_habit is False and related_habit is not None and reward is None:
            raise serializers.ValidationError("Укажите Признак приятной привычки.")


# Валидаторы в целом работаю как нужно, но в коде лучше для каждого типа валидации описывать отдельные функции/классы
# Так ты сможешь написать отдельно тесты на каждый валидатор и проверить "каждый маленький" кусок кода
