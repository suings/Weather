from django.contrib import admin

# Register your models here.
from WeatherData.models import WeatherData

class AdminWeatherData(admin.ModelAdmin):
    pass

admin.site.register(WeatherData,AdminWeatherData)