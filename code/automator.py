# -*- coding: utf-8 -*-
"""
@author: taylorthompson

Runs the main function contained in walmartScrape.py at hourly intervals
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from walmartScrape import main
import atexit
import sys

# defining the scheduler and exit handler
sched = BlockingScheduler(daemonic=False)

@sched.scheduled_job('cron', hour='*', misfire_grace_time=60)
def scheduled_job():
    main()

def exit_handler():
    print('Scheduler ended')
    sched.shutdown()

atexit.register(exit_handler)

# running the scheduler
try:
    sched.start()
    
except(KeyboardInterrupt):
    sys.exit(0)
