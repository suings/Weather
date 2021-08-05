from django.shortcuts import render
from django.http import JsonResponse
from .models import Region
from django.core import serializers
import json


# Create your views here.
def get_child_by_name(request, name='北京市'):
    data = {
        'results': json.loads(
            serializers.serialize('json',
                                  Region.objects.get(name=name).region_set.all()
                                  )
        )
    }

    return JsonResponse(data)
