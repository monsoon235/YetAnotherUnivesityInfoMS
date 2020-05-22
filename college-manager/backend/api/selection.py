import json

import django.views.decorators.csrf
from django.db.models import F
from django.views.decorators.http import require_http_methods

from .general import *
from .models import *

where_params = [
    'lecture_id', 'student_id', 'score'
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
    result = Selection.objects.filter(**params).values(
        *where_params,
        course_name=F('lecture__course__name'),
        teacher_name=F('lecture__teacher__person__name'),
        student_name=F('student__person__name'),
        year=F('lecture__year'),
        term=F('lecture__term')
    )
    return response_success(list(result))


@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    params = json.loads(request.body.decode())
    params = check_params(params)
    return general_add(Selection, params)


@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    params = check_params(request.GET.dict())
    return general_del(Selection, params)


@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    where = check_params(params.get('where', {}))
    update = check_params(params.get('update', {}))
    return general_mod(Selection, where, update)
