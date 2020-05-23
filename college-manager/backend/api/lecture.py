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


def check_permission(func):
    def wrapper(request: HttpRequest, *args, **kw):
        if not request.user.is_authenticated:
            return response_error('login required', status=403)
        if request.user.is_staff:
            return func(request, *args, **kw)
        if request.method == 'GET':
            params = check_params(request.GET.dict())
        elif request.method == 'POST':
            params = json.loads(request.body.decode())
            params = check_params(params.get('where', {}))
        else:
            return response_error('method denied')
        query = Lecture.objects.filter(**params).values(person_id=F('teacher__person_id'))
        person_id_list = list({item['person_id'] for item in query})
        if len(person_id_list) == 0 or \
                (len(person_id_list) == 1 and person_id_list[0] == request.user.get_username):
            return func(request, *args, **kw)
        return response_error('permission denied', status=403)

    return wrapper


# @check_permission
@check_login
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


# @check_permission
@check_login
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    params = json.loads(request.body.decode())
    params = check_params(params)
    return general_add(Lecture, params)


# @check_permission
@check_login
@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    params = check_params(request.GET.dict())
    return general_del(Lecture, params)


# @check_permission
@check_login
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    where = check_params(params.get('where', {}))
    update = check_params(params.get('update', {}))
    return general_mod(Lecture, where, update)
