from time import sleep

from celery import shared_task

@shared_task
def notify_customers(message):
    print('sending 10000 emails')
    sleep(10)
    print('emails successfully sent')
    