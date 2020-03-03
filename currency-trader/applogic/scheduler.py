from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .updater import *

def begin():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', minutes=1)
    scheduler.add_job(update_aroon, 'interval', minutes=1)
    scheduler.add_job(update_atr, 'interval', minutes=1)
    scheduler.add_job(update_chaikin, 'interval', minutes=1)
    scheduler.add_job(update_sma, 'interval', minutes=1)
    scheduler.add_job(update_ssl, 'interval', minutes=1)
    scheduler.start()

    date = datetime.now()
    if date.isocalendar()[2] == 5 and date.hour >= 13:
        print("closed")
        scheduler.pause()
    if date.isocalendar()[2] == 7 and date.hour >= 14:
        print("open")
        scheduler.resume()

