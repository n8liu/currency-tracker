from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group

class CandleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candle
        fields = [
            'complete', 'volume', 'time', 'o', 'h', 'l', 'c'
        ]

class AroonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aroon
        fields = [
            'up', 'down'
        ]

class AtrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atr
        fields = [
           'atr'
        ]
    
class ChaikinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chaikin
        fields = [
           'ad'
        ]

class SmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sma
        fields = [
            'high', 'low', 'close'
        ]

class SslSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ssl
        fields = [
           'ssl'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'username', 'email', 'groups'
        ]
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url', 'name'
        ]