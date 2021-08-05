"""Weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WeatherData.views import region_weather, charts, get_json
from Region.views import get_child_by_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('region/<int:region_id>', region_weather),
    path('region/get_child_by_name/<str:name>', get_child_by_name),
    path('charts/', charts),
    path('charts/json', get_json),
    path('', charts)
]
