from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'place', 'start_time', 'habit', 'sing_habit', 'related_habit', 'periodicity',
                    'reward', 'time_to_complete', 'sing_publicity', 'date_last_send']
    list_display_links = ['id', 'owner', 'place', 'start_time', 'habit', 'sing_habit', 'related_habit', 'periodicity',
                    'reward', 'time_to_complete', 'sing_publicity', 'date_last_send']

