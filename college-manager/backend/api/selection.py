import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest

from .general import *
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


@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        result = Selection.objects.filter(**params).values(
            *where_params,
            course_name=F('lecture__course__name'),
            teacher_name=F('lecture__teacher__person__name'),
            student_name=F('student__person__name')
        )
        return response_success(list(result))
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        params = check_params(params)
        return general_add(Selection, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        return general_del(Selection, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        return general_mod(Selection, where, update)
    except Exception as e:
        return response_error(str(e))
