import json

import django.views.decorators.csrf
from django.contrib.auth.models import User
from django.db.models import F
from django.views.decorators.http import require_http_methods

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
    'class_id', 'person_id'
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


def check_auth_params(params: dict) -> dict:
    info = {}
    if 'person_id' in params:
        info['username'] = params['person_id']
    if 'password' in params:
        info['password'] = params['password']
    return info


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
        query = Student.objects.filter(**params).values('person_id')
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
    result = Student.objects.filter(**params).values(
        'id', 'enroll_date', 'email', 'person_id',
        class_id=F('class0_id'),
        class_name=F('class0__name'),
        major_id=F('class0__major_id'),
        major_name=F('class0__major__name'),
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


# exception 需要特殊处理
@check_admin
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def add(request: HttpRequest):
    try:
        params = json.loads(request.body.decode())
        if 'password' not in params:
            return response_error('missing password')
        student_params = check_student_params(params)
        person_params = check_person_params(params)
        if 'id' not in student_params:
            return response_error('missing id')
        if 'id' not in person_params:
            return response_error('missing person_id')
        if Student.objects.filter(id=student_params['id']):
            return response_error('student id exists')
        if Person.objects.filter(id=person_params['id']):
            return response_error('person id exists')
        added = 0
        Person(**person_params).save()
        added = 1
        Student(**student_params).save()
        added = 2
        User.objects.create_user(username=person_params['id'], password=params['password'])
        return response_success()
    except Exception as e:
        if added >= 1:
            Person.objects.filter(**person_params).delete()
        if added >= 2:
            Student.objects.filter(**student_params).delete()
        return response_error(str(e))


@check_admin
@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def delete(request: HttpRequest):
    params = check_params(request.GET.dict())
    # 找出要删的 student 对应的所有 person id,直接删除 person 即可
    person_id_dict_list = Student.objects.filter(**params).values('person_id')
    person_id_list = [item['person_id'] for item in person_id_dict_list]
    for id in person_id_list:
        Person.objects.filter(id=id).delete()
        User.objects.filter(username=id).delete()
    return response_success()


# @check_permission
@check_login
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    where = check_params(params.get('where', {}))
    update = params.get('update', {})
    # 筛选出要更新的 student entry，然后先更新 person,在更新 student
    student_list = Student.objects.filter(**where)
    person_id_dict_list = student_list.values('person_id')
    person_id_list = [item['person_id'] for item in person_id_dict_list]
    for id in person_id_list:
        Person.objects.filter(id=id).update(**check_person_params(update))
        User.objects.filter(username=id).update(**check_auth_params(update))
    student_list.update(**check_student_params(update))
    return response_success()
