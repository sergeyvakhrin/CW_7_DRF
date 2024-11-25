import datetime
import requests
from datetime import timedelta
from config.settings import TELEGRAM_TOKEN
from celery import shared_task

from habits.models import Habit


@shared_task
def send_telegram():
    """ Проверяет, настало ли время отправки Привычки и если настало, вызывает отправку"""
    today = datetime.datetime.now().date()
    habits = Habit.objects.exclude(periodicity__isnull=True, # исключаются объекты с пустой периодичностью
                                   owner__tg_chat_id__isnull=True) # исключаем пользователей без Телеграм

    # for habit in habits:
    #
    #     if habit.periodicity == "DAY":
    #         if habit.date_last_send:
    #             if habit.date_last_send + datetime.timedelta(days=1) < today:
    #                 send_and_save(habit, today)
    #             else:
    #                 continue
    #         else:
    #             send_and_save(habit, today)
    #
    #     elif habit.periodicity == "WEEK":
    #         if habit.date_last_send:
    #             if habit.date_last_send + datetime.timedelta(days=7) < today:
    #                 send_and_save(habit, today)
    #             else:
    #                 continue
    #         else:
    #             send_and_save(habit, today)


    periods_map = {
            "DAY": timedelta(days=1),
            "WEEK": timedelta(days=7)
        }
    for habit in habits:
        period_delta = periods_map[habit.periodicity]
        if habit.date_last_send:
            if habit.date_last_send + period_delta < today:
                send_and_save.delay(habit.id, today)
            else:
                continue
        else:
            send_and_save.delay(habit.id, today)


@shared_task(autoretry_for=(Exception, ), retry_kwargs={'max_retries':3}) # Проверяем, что сообщение дошло. Три попытки.
def send_and_save(habit_id, today):
    """Вызывает отправку и сохраняет"""

    # Подтягиваем связанные данные одним запросом с помощью select_related,
    # что бы исключить лишние запросы в базу
    habit = Habit.objects.select_related('owner').get(pk=habit_id)

    params = {
        "text": str(habit),
        "chat_id": habit.owner.tg_chat_id,
    }
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=params)

    habit.date_last_send = today
    habit.save()
