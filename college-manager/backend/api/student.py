import json

import django.views.decorators.csrf
from django.db.models import F
from django.http import HttpRequest

from .general import *
from .models import *

where_params = [
    'id', 'enroll_date', 'email',
    'class_id', 'class_name',
    'major_id', 'major_name',
    'person_id', 'person_name', 'person_id_type', 'gender', 'birth', 'country',
    'family_address', 'family_zipcode', 'family_tel'
]

student_params = [
    'id', 'enroll_date', 'email',
    'class_id', 'major_id', 'person_id'
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
        if k == 'class_id':
            ret['class0_id'] = v
        elif k == 'class_name':
            ret['class0__name'] = v
        elif k == 'major_id':
            ret['class0__major_id'] = v
        elif k == 'major_name':
            ret['class0__major__name'] = v
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


def check_student_params(params: dict) -> dict:
    params = {
        k: v for k, v in params.items()
        if k in student_params
    }
    if 'class_id' in params:
        params['class0_id'] = params['class_id']
        params.pop('class_id')
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
        result = Student.objects.filter(**params).values(
            'id', 'enroll_date', 'email', 'person_id',
            class_id=F('class0_id'),
            class_name=F('class0__name'),
            major_id=F('class0__major_id'),
            major_name=F('class0__major__name'),
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
        student_params = check_student_params(params)
        person_params = check_person_params(params)
        if Student.objects.filter(id=student_params['id']):
            return response_error('student id exists')
        if Person.objects.filter(id=person_params['id']):
            return response_error('person id exists')
        Person(**person_params).save()
        person_added = True
        Student(**student_params).save()
        return response_success()
    except Exception as e:
        if person_added:
            Person.objects.filter(id=person_params['id']).delete()
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    try:
        params = check_params(request.GET.dict())
        return general_del(Student, params)
    except Exception as e:
        return response_error(str(e))


@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        where = check_params(params.get('where', {}))
        update = check_params(params.get('update', {}))
        return general_mod(Student, where, update)
    except Exception as e:
        return response_error(str(e))
