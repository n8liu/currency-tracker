from django.contrib import admin
from app.models import Candle, Aroon, Atr, Chaikin, Sma, Ssl 

# Register your models here.
admin.site.register(Candle)
admin.site.register(Aroon)
admin.site.register(Atr)
admin.site.register(Chaikin)
admin.site.register(Sma)
admin.site.register(Ssl)