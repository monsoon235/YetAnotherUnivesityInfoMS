import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest, JsonResponse

from .models import *

where_params = [
    'id', 'lecture_id', 'student_id', 'score'
]


def check_params(params: dict) -> dict:
    params = {
        k: v
        for k, v in params.items()
        if k in where_params
    }
    return params


def get(request: HttpRequest):
    response = {}
    try:
        params = check_params(request.GET.dict())
        result = Selection.objects.filter(**params).values(
            *where_params,
            course_name=F('lecture__course__name'),
            teacher_name=F('lecture__teacher__person__name'),
            student_name=F('student__person__name')
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
        params = json.loads(request.body.decode())
        if 'id' not in params:
            response['code'] = 0
            response['msg'] = 'missing id'
        elif Selection.objects.filter(id=params['id']):
            response['code'] = 0
            response['msg'] = 'id exist'
        else:
            Selection(**params).save()
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
        Selection.objects.filter(**params).delete()
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
        Selection.objects.filter(**where).update(update)
        response['code'] = 1
    except Exception as e:
        response['code'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)
