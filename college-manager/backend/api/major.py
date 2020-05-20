import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest, JsonResponse

from .models import *

where_params = ['id', 'name', 'address', 'campus_id', 'charge_person_id']


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
        result = Major.objects.filter(**params).values(
            *where_params,
            campus_name=F('campus__name'), charge_person_name=F('charge_person__name')
        )
        response['code'] = 1
        response['list'] = list(result)
    except Exception as e:
        print(e)
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
        elif Major.objects.filter(id=params['id']):
            response['code'] = 0
            response['msg'] = 'id exist'
        else:
            params['campus_id_id'] = params['campus_id']
            params.pop('campus_id')
            Major(**params).save()
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
        Major.objects.filter(**params).delete()
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    response = {}
    try:
        params = json.loads(request.body)
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        if 'id' in update:
            response['code'] = 0
            response['msg'] = 'can not modify id'
        Major.objects.filter(**where).update(**update)
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)
