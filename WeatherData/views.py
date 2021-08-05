from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Region.models import Region
from django.http import JsonResponse, HttpResponseRedirect
from WeatherData.models import WeatherData
from utils.weather_spider import update_region_weather
import datetime


def get_json(request):
    key = request.GET.get('key', 'max')

    data = {
        'data': [],
        'geoCoordMap': {}
    }
    for w in WeatherData.objects.filter(time=datetime.datetime.now().strftime('%Y-%m-%d')):
        value = w.max_degree if key == 'max' else w.min_degree
        data['data'].append(
            {'name': w.region.name, 'value': value}
        )
        data['geoCoordMap'][w.region.name] = [w.region.longitude, w.region.latitude]

    return JsonResponse(data)


def region_weather(request, region_id):
    if request.method == "POST":
        region_name = request.POST['region_name']
        rid = Region.objects.get(name=region_name).id
        return HttpResponseRedirect('/region/%d' % rid)
    region = Region.objects.get(id=region_id)
    update_region_weather(region)
    data = WeatherData.objects.filter(region_id=region_id)[:7]
    print(data)
    content = {
        'region': region,
        'data': data,
        'regions': Region.objects.all().first(),
        'province': Region.objects.filter(is_province=True),
        'municipality': Region.objects.filter(is_municipality=True)
    }
    return render(request, 'show.html', content)


def charts(request):
    return render(request, 'echarts.html')
