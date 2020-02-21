#from datetime import datetime
from django.conf import settings
import requests
import numpy as np
from app.models import Candle, Aroon, Atr, Chaikin, Sma, Ssl 
from .indicators import aroon, atr, chaikin, sma, ssl

def update():
    count = 2
    response = requests.get('https://api-fxpractice.oanda.com/v3/instruments/USD_JPY/candles',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': settings.OANDA_PRACTICE_API_KEY,},
                            params=(('count', str(count)),
                                    ('price', 'M'),
                                    ('granularity', 'M1'),))
    candle = response.json()
    c = Candle(complete=str(candle['candles'][0]['complete']),
               volume=str(candle['candles'][0]['volume']),
               time=str(candle['candles'][0]['time']),
               o=str(candle['candles'][0]['mid']['o']),
               h=str(candle['candles'][0]['mid']['h']),
               l=str(candle['candles'][0]['mid']['l']),
               c=str(candle['candles'][0]['mid']['c']))
    c.save()
    return response.status_code

def update_indi(count):
    response = requests.get('https://api-fxpractice.oanda.com/v3/instruments/USD_JPY/candles',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': settings.OANDA_PRACTICE_API_KEY,},
                            params=(('count', str(count)),
                                    ('price', 'M'),
                                    ('granularity', 'M5'),))
    candle = response.json()
    for i in range(count):
            if i == 0:
                main_p_array = np.array([[float(candle['candles'][0]['mid']['o']), 
                                        float(candle['candles'][0]['mid']['h']),
                                        float(candle['candles'][0]['mid']['l']),
                                        float(candle['candles'][0]['mid']['c']),
                                        float(candle['candles'][0]['volume'])]])
            else:
                next_candle = np.array([[float(candle['candles'][i]['mid']['o']), 
                                    float(candle['candles'][i]['mid']['h']),
                                    float(candle['candles'][i]['mid']['l']),
                                    float(candle['candles'][i]['mid']['c']),
                                    float(candle['candles'][i]['volume'])]])
                main_p_array = np.concatenate((main_p_array, next_candle), axis=0)
    return main_p_array    

def update_aroon():
    ar_val = aroon.aroon(update_indi(6))
    data = Aroon(up=ar_val[0], down=ar_val[1])
    data.save()

def update_atr():
    atr_val = atr.atr(update_indi(14))
    data = Atr(atr=atr_val)
    data.save()

def update_chaikin():
    chaikin_val = chaikin.ad(update_indi(4))
    data = Chaikin(ad=chaikin_val)
    data.save()

def update_sma():
    sma_high = sma.sma_high(update_indi(4))
    sma_low = sma.sma_low(update_indi(4))
    sma_close = sma.sma_close(update_indi(4))
    data = Sma(high=sma_high, low=sma_low, close=sma_close)
    data.save()

def update_ssl():
    ssl_val = ssl.ssl(update_indi(10))
    data = Ssl(ssl=ssl_val)
    data.save()