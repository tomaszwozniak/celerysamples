from time import sleep
from celery import task


@task
def slow_task():
    print('slow_task')
    sleep(60)


def run(x):
    for i in xrange(x):
        slow_task.delay()
