from apscheduler.schedulers.background import BackgroundScheduler
from .updater import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', minutes=1)
    scheduler.add_job(update_aroon, 'interval', minutes=1)
    scheduler.add_job(update_atr, 'interval', minutes=1)
    scheduler.add_job(update_chaikin, 'interval', minutes=1)
    scheduler.add_job(update_sma, 'interval', minutes=1)
    scheduler.add_job(update_ssl, 'interval', minutes=1)
    scheduler.start()