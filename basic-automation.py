import schedule
import os
import sys
import time
from main import main

def job(self, job_func, *args, **kwargs):
    main()
schedule.every(6).hours.do(job)

while True:
    # is pending to run or not
    schedule.run_pending(main)
    time.sleep(1)
