import json

import django.views.decorators.csrf
from django.core import serializers
from django.http import HttpRequest, JsonResponse

from .models import *


def check_params(params: dict) -> dict:
    return {
        k: v
        for k, v in params.items()
        if k in ['id', 'name', 'address']
    }


def get(request: HttpRequest):
    response = {}
    try:
        params = check_params(request.GET.dict())
        result = Campus.objects.filter(**params)
        result = json.loads(serializers.serialize("json", result))
        data = [{
            'id': item['pk'],
            'name': item['fields']['name'],
            'address': item['fields']['address']
        } for item in result]
        response['code'] = 1
        response['list'] = data
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)


@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    response = {}
    try:
        params = check_params(request.POST.dict())
        if 'id' not in params:
            response['code'] = 0
            response['msg'] = 'missing id'
        elif Campus.objects.filter(id=params['id']):
            response['code'] = 0
            response['msg'] = 'id exist'
        else:
            Campus(**params).save()
            response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)


def delete(request: HttpRequest):
    # todo 存在关联信息则不删除
    response = {}
    try:
        params = check_params(request.GET.dict())
        Campus.objects.filter(**params).delete()
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    response = {}
    try:
        where = check_params(request.POST.get('where', {}))
        update = check_params(request.POST.get('update', {}))
        if 'id' in update:
            response['code'] = 0
            response['msg'] = 'can not modify id'
        Campus.objects.filter(**where).update(update)
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)