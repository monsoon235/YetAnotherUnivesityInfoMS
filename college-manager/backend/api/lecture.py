import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest

from .general import *
from .models import *

where_params = [
    'id', 'course_id', 'teacher_id', 'year', 'term', 'time'
]


def check_params(params: dict) -> dict:
    params = {
        k: v
        for k, v in params.items()
        if k in where_params
    }
    return params


@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        result = Lecture.objects.filter(**params).values(
            *where_params,
            course_name=F('course__name'),
            teacher_name=F('teacher__person__name'),
            assessment=F('course__assessment'),
            major_name=F('course__major__name')
        )
        return response_success(list(result))
    except Exception as e:
        return response_error(str(e))


# 没有 id 需要特殊处理
@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        params = check_params(params)
        return general_add(Lecture, params)
    except Exception as e:
        return response_error(str(e))
    # try:
    #     params = json.loads(request.body.decode())
    #     params = check_params(params)
    #     if 'id' not in params:
    #         return response_error('missing id')
    #     if 'class_id' not in params:
    #         return response_error('missing class_id')
    #     if Lecture.objects.filter(
    #             lecture_id=params['lecture_id'],
    #             class_id=params['class_id']):
    #         return response_error('id exists')
    #     Lecture(**params).save()
    #     return response_success()
    # except Exception as e:
    #     return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        return general_del(Lecture, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        return general_mod(Lecture, where, update)
    except Exception as e:
        return response_error(str(e))
