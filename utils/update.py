import os
import django
from django.db.models import Q
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather.settings')
django.setup()
from Region.models import *

# from django.utils import Q

def update():
    obs = Region.objects.filter(parent__id=0).exclude(id=0).update(level='0')
    print(obs)


def level_update():
    Region.objects.filter(parent__level='0').update(level='1')
    Region.objects.filter(parent__level='1').update(level='2')
    Region.objects.filter(parent__level='2').update(level='3')


# 直辖市
def generate_municipality():
    Region.objects.filter(name__in=['北京市', '上海市', '天津市', '重庆市']).update(is_municipality=True)

# 省会城市
def generate_province_capital():
    print(
        Region.objects.filter(
            id__endswith='0100'
        ).exclude(
            parent__is_municipality=False
        ).update(
            is_province=True
        )
    )

def set_display_region():
    Region.objects.filter(Q(is_municipality=True)|Q(is_province=True)).update(display=True)
    pass

def insert_from_csv():
    with open("中国省市经纬度.csv",'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'province':
                continue
            if row[1] == '':
                r = Region.objects.filter(name=row[0]).first()
            else:
                r = Region.objects.filter(name=row[1]).first()
            if r:
                r.longitude = float(row[2])
                r.latitude = float(row[3])
                r.save()
                print(r.name)

if __name__ == "__main__":
    pass
    # update()
    # level_update()
    # generate_municipality()
    # generate_province_capital()
    set_display_region()
    # insert_from_csv()
