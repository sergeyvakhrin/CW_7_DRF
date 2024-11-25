import requests

from config.settings import TELEGRAM_TOKEN


# def send_and_save(habit, today):
#     """Вызывает отправку и сохраняет"""
#     send_telegram_message(habit.owner.tg_chat_id, habit)
#     habit.date_last_send = today
#     habit.save()


# def send_telegram_message(chat_id, message):
#     """Отправляет сообщение в Телеграм"""
#
#     params = {
#         "text": str(message),
#         "chat_id": chat_id,
#     }
#     requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=params)




