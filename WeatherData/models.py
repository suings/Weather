from django.db import models

# Create your models here.
from Region.models import Region


class WeatherData(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    day_weather=models.CharField(max_length=20)
    day_weather_code=models.CharField(max_length=2)
    day_weather_short=models.CharField(max_length=20)
    day_wind_direction=models.CharField(max_length=20)
    day_wind_direction_code=models.CharField(max_length=2)
    day_wind_power=models.SmallIntegerField()
    day_wind_power_code=models.CharField(max_length=2)
    max_degree=models.FloatField()
    min_degree=models.FloatField()
    night_weather=models.CharField(max_length=20)
    night_weather_code=models.CharField(max_length=2)
    night_weather_short=models.CharField(max_length=20)
    night_wind_direction=models.CharField(max_length=20)
    night_wind_direction_code=models.CharField(max_length=2)
    night_wind_power=models.SmallIntegerField()
    night_wind_power_code=models.CharField(max_length=2)
    time=models.DateField()

    # 用于记录天气数据什么时候插入数据库的
    # auto_now_add django自带参数，自动将创建数据的时间插入字段
    # 只读
    created = models.DateTimeField(auto_now_add=True)