import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest

from .general import *
from .models import *

where_params = [
    'id', 'enroll_date', 'email', 'title',
    'major_id', 'major_name',
    'person_id', 'person_name', 'person_id_type', 'gender', 'birth', 'country',
    'family_address', 'family_zipcode', 'family_tel'
]

teacher_params = [
    'id', 'enroll_date', 'email', 'title',
    'major_id', 'person_id',
]

person_params = [
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
        if k == 'major_name':
            ret['major__name'] = v
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


def check_teacher_params(params: dict) -> dict:
    params = {
        k: v for k, v in params.items()
        if k in teacher_params
    }
    return params


def check_person_params(params: dict) -> dict:
    params = {
        k: v for k, v in params.items()
        if k in person_params
    }
    ret = {}
    for k, v in params.items():
        if k.startswith('person_'):
            ret[k[7:]] = v
        else:
            ret[k] = v
    return ret


@django.views.decorators.csrf.csrf_exempt
def get(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        result = Teacher.objects.filter(**params).values(
            'id', 'enroll_date', 'email', 'title',
            'major_id', 'person_id',
            major_name=F('major__name'),
            person_name=F('person__name'),
            person_id_type=F('person__id_type'),
            gender=F('person__gender'),
            birth=F('person__birth'),
            country=F('person__country'),
            family_address=F('person__family_address'),
            family_zipcode=F('person__family_zipcode'),
            family_tel=F('person__family_tel')
        )
        return response_success(list(result))
    except Exception as e:
        return response_error(str(e))


# 不能用 general

@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    person_added = False
    try:
        params = json.loads(request.body.decode())
        teacher_params = check_teacher_params(params)
        person_params = check_person_params(params)
        if Teacher.objects.filter(id=teacher_params['id']):
            return response_error('teacher id exists')
        if Person.objects.filter(id=person_params['id']):
            return response_error('person id exists')
        Person(**person_params).save()
        person_added = True
        Teacher(**teacher_params).save()
        return response_success()
    except Exception as e:
        if person_added:
            Person.objects.filter(id=person_params['id']).delete()
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        return general_del(Teacher, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        return general_mod(Teacher, where, update)
    except Exception as e:
        return response_error(str(e))
