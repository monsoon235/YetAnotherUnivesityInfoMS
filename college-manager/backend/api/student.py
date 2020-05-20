import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest, JsonResponse

from .models import *

where_params = [
    'id', 'enroll_date', 'email',
    'class_id', 'class_name',
    'major_id', 'major_name',
    'person_id', 'person_name', 'person_id_type', 'gender', 'birth', 'country',
    'family_address', 'family_zipcode', 'family_tel'
]


def check_params(params: dict) -> dict:
    params = {
        k: v
        for k, v in params.items()
        if k in where_params
    }
    ret = {}
    for k, v in params.items():
        if k == 'class_id':
            ret['class0_id'] = v
        elif k == 'class_name':
            ret['class0__name'] = v
        elif k == 'major_id':
            ret['class0__major_id'] = v
        elif k == 'major_name':
            ret['class0__major__name'] = v
        elif k == 'person_name':
            ret['person__name'] = v
        elif k == 'person_id_type':
            ret['person__id_type'] = v
        elif k in ['gender', 'birth', 'country',
                   'family_address', 'family_zipcode', 'family_tel']:
            ret['person__' + k] = v
        else:
            ret[k] = v
    return ret


def get(request: HttpRequest):
    response = {}
    try:
        params = check_params(request.GET.dict())
        result = Student.objects.filter(**params).values(
            'id', 'enroll_date', 'email', 'person_id',
            class_id=F('class0_id'),
            class_name=F('class0__name'),
            major_id=F('class0__major_id'),
            major_name=F('class0__major__name'),
            person_id_type=F('person__id_type'),
            gender=F('person__gender'),
            birth=F('person__birth'),
            country=F('person__country'),
            family_address=F('person__family_address'),
            family_zipcode=F('person__family_zipcode'),
            family_tel=F('person__family_tel')
        )
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
        params = check_params(request.POST.dict())
        if 'id' not in params:
            response['code'] = 0
            response['msg'] = 'missing id'
        elif Student.objects.filter(id=params['id']):
            response['code'] = 0
            response['msg'] = 'id exist'
        else:
            Student(**params).save()
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
        Student.objects.filter(**params).delete()
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
        Student.objects.filter(**where).update(update)
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)
