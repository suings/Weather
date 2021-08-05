from django.contrib import admin
from .models import *


# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent','level','longitude','latitude',"is_province",'display','is_municipality']
    # list_editable = ['name', 'parent']


admin.site.register(Region, RegionAdmin)
