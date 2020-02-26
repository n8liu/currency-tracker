from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .updater import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', minutes=1)
    #scheduler.add_job(update_aroon, 'interval', minutes=15)
    #scheduler.add_job(update_atr, 'interval', minutes=15)
    #scheduler.add_job(update_chaikin, 'interval', minutes=15)
    #scheduler.add_job(update_sma, 'interval', minutes=15)
    #scheduler.add_job(update_ssl, 'interval', minutes=15)
    scheduler.start()

    date = datetime.now()
    if date.isocalendar()[2] == 5 and date.hour >= 13:
        print("closed")
        scheduler.shutdown
    if date.isocalendar()[2] == 7 and date.hour >= 14:
        print("open")
        scheduler.start()