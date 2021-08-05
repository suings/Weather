import csv
import os
import django


# 把manage.py的django设置导入
from django.db.models import Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather.settings')

# 启动django
django.setup()

from Region.models import Region
def level_update():
    print(Region.objects.filter(parent__id=0).exclude(id=0).update(level='0'))
    print(Region.objects.filter(parent__level='0').update(level='1'))
    print(Region.objects.filter(parent__level='1').update(level='2'))
    print(Region.objects.filter(parent__level='2').update(level='3'))

# 生成直辖市
def generate_municipality():
    Region.objects.filter(name__in=['北京市', '上海市', '天津市', '重庆市']).update(is_municipality=True)

# 生成省会城市
def generate_province_capital():
    print(Region.objects.filter(id__endswith='0100').exclude(parent__is_municipality=True).update(
        is_province=True))

def set_display_region():
    # Q对象 用于处理 查询条件之间的 AND OR NOT
    Region.objects.filter(Q(is_municipality=True) | Q(is_province=True)).update(display=True)

def insert_latitude_from_csv():
    with open('中国省市经纬度.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)

        for row in reader:
            # 跳过表头
            if row[0] == 'province':
                continue
            if row[1] == '':
                # 直接用get方法查的话 查不到的情况会报异常，所以用filter方法来做
                #  first()获取结果中的第一条,即使前面结果列表为空,也不会报错
                r = Region.objects.filter(name=row[0]).first()
            elif row[1] != '':
                r = Region.objects.filter(name=row[1]).first()
            if r:
                r.longtitude = float(row[2])
                r.latitude = float(row[3])
                r.save()
                print('%s修改成功！' % r.name)

if __name__ == '__main__':
    level_update()
    insert_latitude_from_csv()
    generate_municipality()
    generate_province_capital()
    set_display_region()