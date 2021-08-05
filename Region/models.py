from django.db import models


# Create your models here.
class Region(models.Model):
    id = models.IntegerField("编号", primary_key=True)
    name = models.CharField("区域名称", max_length=30)
    parent = models.ForeignKey('self', verbose_name="父级区域", on_delete=models.SET_NULL, null=True, blank=True)

    level = models.CharField("区域等级", max_length=2,null=True)
    longitude = models.FloatField("经度", null=True, blank=True)
    latitude = models.FloatField("纬度", null=True, blank=True)

    is_municipality = models.BooleanField("直辖市", default=False)  # 直辖市
    is_province = models.BooleanField("省会", default=False)  # 省
    is_province_municipality = models.BooleanField("省直辖",default=False)  # 省直辖

    display = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def get_province(self):
        if self.level == '0':
            return self.name
        if self.level == '1':
            return self.parent.name
        if self.level == '2':
            return self.parent.parent.name
        return self.name

    class Meta:
        verbose_name = "区域信息"
        verbose_name_plural = verbose_name
