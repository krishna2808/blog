# Create your tasks here


from celery import shared_task
import time

@shared_task
def add():
    print("************************ ")
    time.sleep(80)
    print("task py ")
    return "this is"
