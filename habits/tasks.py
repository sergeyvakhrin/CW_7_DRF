import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_and_save


@shared_task
def send_telegram():
    """ Проверяет, настало ли время отправки Привычки и если настало, вызывает отправку"""
    today = datetime.datetime.now().date()
    habits = Habit.objects.all()

    for habit in habits:

        if habit.periodicity == "DAY":
            if habit.date_last_send:
                if habit.date_last_send + datetime.timedelta(days=1) < today:
                    send_and_save(habit, today)
                else:
                    continue
            else:
                send_and_save(habit, today)

        elif habit.periodicity == "WEEK":
            if habit.date_last_send:
                if habit.date_last_send + datetime.timedelta(days=7) < today:
                    send_and_save(habit, today)
                else:
                    continue
            else:
                send_and_save(habit, today)
