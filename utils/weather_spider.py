import requests
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather.settings')
django.setup()
from Region.models import Region
from WeatherData.models import WeatherData

url = 'https://wis.qq.com/weather/common'

params = {
    'source': 'pc',
    'weather_type': 'forecast_24h',
    'province': '湖北省',
    'city': "武汉市"
}

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

# 根据区域获取天气数据
def get_region_weather(region: Region):
    params['province'] = region.get_province()
    params['city'] = region.name
    res = requests.get(url, params=params, headers=headers)
    return res.json()['data']['forecast_24h']

# 更新某区域的天气数据
def update_region_weather(region: Region):
    if WeatherData.objects.filter(region=region).count()>0:
        return

    params['province'] = region.get_province()
    params['city'] = region.name
    params['country'] = ""
    res = requests.get(url, params=params, headers=headers)
    data = res.json()['data']['forecast_24h']

    WeatherData.objects.filter(region=region).delete()

    for v in data.values():
        WeatherData.objects.create(region=region, **v)

# 爬取全国重点城市的天气数据，以方便地图显示，需要手动执行
def update_all():
    WeatherData.objects.all().delete()
    region_list = Region.objects.filter(display=True)
    print(region_list)
    for r in region_list:
        data = get_region_weather(r)
        if data:
            for v in data.values():
                WeatherData.objects.create(region=r, **v)

if __name__ =="__main__":
    update_all()
