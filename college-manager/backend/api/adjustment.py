import json

import django.views.decorators.csrf
from django.db.models import F
from django.views.decorators.http import require_http_methods

from .general import *
from .models import *

where_params = ['student_id', 'type', 'date', 'from_class_id', 'to_class_id', 'extra']


def check_params(params: dict) -> dict:
    return {
        k: v for k, v in params.items()
        if k in where_params
    }


# done

@check_login
@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    params = check_params(request.GET.dict())
    result = Adjustment.objects.filter(**params).values(
        'id', *where_params,
        student_name=F('student__person__name'),
        from_class_name=F('from_class__name'),
        to_class_name=F('to_class__name')
    )
    return response_success(list(result))


@check_admin
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    params = json.loads(request.body.decode())
    params = check_params(params)
    Adjustment(**params).save()
    return response_success()


@check_admin
@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    params = check_params(request.GET.dict())
    return general_del(Adjustment, params)


@check_admin
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    where = check_params(params.get('where', {}))
    update = check_params(params.get('update', {}))
    return general_mod(Adjustment, where, update)
