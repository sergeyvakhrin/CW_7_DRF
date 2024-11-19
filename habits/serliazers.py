from rest_framework import serializers

from habits.models import Habit
from habits.validators import validata_time_complete, validate_type_habit


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.DurationField(validators=[validata_time_complete])

    # def validate(self, data):
    #     """ Проверка типа привычки """
    #     if data['sing_habit'] and data['related_habit'] is None and data['reward'] is not None:
    #         raise serializers.ValidationError(
    #             "Необходимо указать Связанную привычку и убрать вознаграждение. Либо убрать Признак приятной привычки.")
    #     if data['sing_habit'] and data['related_habit'] is None and data['reward'] is None:
    #         raise serializers.ValidationError("Необходимо указать Связанную привычку.")
    #     if data['sing_habit'] is False and data['related_habit'] is not None and data['reward'] is not None:
    #         raise serializers.ValidationError("Необходимо указать Признак приятной привычки и убрать награду. "
    #                                           "Любо убрать связанную привычку.")
    #     if data['sing_habit'] and data['related_habit'] is not None and data['reward']:
    #         raise serializers.ValidationError("Убери Вознаграждение, у Приятной привычки уже есть Связанная привычка.")
    #     if data['sing_habit'] is False and data['related_habit'] is None and data['reward'] is None:
    #         raise serializers.ValidationError("Укажите Вознаграждение.")
    #     if data['sing_habit'] is False and data['related_habit'] is not None and data['reward'] is None:
    #         raise serializers.ValidationError("Укажите Признак приятной привычки.")

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            validate_type_habit(
                field1='sing_habit',
                field2='related_habit',
                field3='reward'
            )
        ]
