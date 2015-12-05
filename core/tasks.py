from __future__ import absolute_import

from time import sleep
from celery import task

@task
def add():
    print('jol')
    sleep(60)

@task
def fasttask():
    print('fasttrask')

def run(x):
    for i in xrange(x):
        add.delay()

def run_fast(x):
    for i in xrange(x):
        fasttask.delay()
