import json

import django.views.decorators.csrf
from django.http import HttpRequest, JsonResponse

from .models import *

where_params = ['id', 'name', 'address']


def check_params(params: dict) -> dict:
    return {
        k: v
        for k, v in params.items()
        if k in where_params
    }


def get(request: HttpRequest):
    response = {}
    try:
        params = check_params(request.GET.dict())
        result = Campus.objects.filter(**params).values()
        response['code'] = 1
        response['list'] = list(result)
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)


@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    response = {}
    try:
        params = json.loads(request.body.decode())
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
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        if 'id' in update:
            response['code'] = 0
            response['msg'] = 'can not modify id'
        Campus.objects.filter(**where).update(**update)
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)
