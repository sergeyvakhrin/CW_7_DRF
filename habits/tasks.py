from celery import shared_task


@shared_task
def test():
    print(1111111111111111)