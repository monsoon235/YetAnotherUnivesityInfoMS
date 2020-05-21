import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest

from .general import *
from .models import *

where_params = ['id', 'name', 'address', 'campus_id', 'charge_person_id']


def check_params(params: dict) -> dict:
    return {
        k: v
        for k, v in params.items()
        if k in where_params
    }


# done

@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        result = Major.objects.filter(**params).values(
            *where_params,
            campus_name=F('campus__name'), charge_person_name=F('charge_person__name')
        )
        return response_success(list(result))
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        params = check_params(params)
        return general_add(Major, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        return general_del(Major, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        return general_mod(Major, where, update)
    except Exception as e:
        return response_error(str(e))
