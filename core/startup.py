# coding = utf8
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick,'cron', second='*/5', hour='*')    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() 
