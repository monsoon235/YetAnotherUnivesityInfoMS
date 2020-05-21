import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest

from .general import *
from .models import *

where_params = ['student_id', 'type', 'date', 'from_class_id', 'to_class_id', 'extra']


def check_params(params: dict) -> dict:
    return {
        k: v for k, v in params.items()
        if k in where_params
    }


@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        result = Adjustment.objects.filter(**params).values(
            *where_params,
            student_name=F('student__name'),
            from_class_name=F('from_class__name'),
            to_class_name=F('to_class__name')
        )
        return response_success(list(result))
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        params = check_params(params)
        return general_add(Adjustment, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        return general_del(Adjustment, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        return general_mod(Adjustment, where, update)
    except Exception as e:
        return response_error(str(e))
