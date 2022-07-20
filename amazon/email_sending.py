import schedule
import time
from os import system

def job():
    system("python3 data_Test.py")


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)