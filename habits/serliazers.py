from rest_framework import serializers

from habits.models import Habit
from habits.validators import validata_time_complete, validate_type_habit


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.DurationField(
        validators=[validata_time_complete], read_only=True
    )

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            validate_type_habit(
                field1="sing_habit", field2="related_habit", field3="reward"
            )
        ]
