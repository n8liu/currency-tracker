from rest_framework import viewsets
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from .serializers import *
import requests
import json

# Create your views here.
def home(request):
    count = 5
    response = requests.get('https://api-fxpractice.oanda.com/v3/instruments/USD_JPY/candles',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': 'Bearer 51c184901981e2067116757c1d5319b4-9fc592249cb81e5246d1a2ce86f72d90',},
                            params=(('count', str(count)),
                                    ('price', 'M'),
                                    ('granularity', 'M5'),))
    candlesticks = response.json()
    status = response.status_code
    
    return render(request, 'app/home.html', {
        'status_code': status,
        'data': candlesticks['candles'],
    })

class CandleViewSet(viewsets.ModelViewSet):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

class AroonViewSet(viewsets.ModelViewSet):
    queryset = Aroon.objects.all()
    serializer_class = AroonSerializer

class AtrViewSet(viewsets.ModelViewSet):
    queryset = Atr.objects.all()
    serializer_class = AtrSerializer

class ChaikinViewSet(viewsets.ModelViewSet):
    queryset = Chaikin.objects.all()
    serializer_class = ChaikinSerializer

class SmaViewSet(viewsets.ModelViewSet):
    queryset = Sma.objects.all()
    serializer_class = SmaSerializer

class SslViewSet(viewsets.ModelViewSet):
    queryset = Ssl.objects.all()
    serializer_class = SslSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer