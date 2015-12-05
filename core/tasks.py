from __future__ import absolute_import

from time import sleep
from celery import task


@task
def slow_task():
    print('slow_task')
    sleep(60)


@task
def fast_task():
    print('fast_task')


def run(x):
    for i in xrange(x):
        slow_task.delay()


def run_fast(x):
    for i in xrange(x):
        fast_task.delay()
