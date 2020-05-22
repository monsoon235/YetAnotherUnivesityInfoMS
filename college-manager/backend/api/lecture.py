import json

import django.views.decorators.csrf
from django.db.models import F
from django.views.decorators.http import require_http_methods

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


@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    params = check_params(request.GET.dict())
    result = Lecture.objects.filter(**params).values(
        *where_params,
        course_name=F('course__name'),
        teacher_name=F('teacher__person__name'),
        assessment=F('course__assessment'),
        major_name=F('course__major__name')
    )
    return response_success(list(result))


@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    params = json.loads(request.body.decode())
    params = check_params(params)
    return general_add(Lecture, params)


@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    params = check_params(request.GET.dict())
    return general_del(Lecture, params)


@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    where = check_params(params.get('where', {}))
    update = check_params(params.get('update', {}))
    return general_mod(Lecture, where, update)
