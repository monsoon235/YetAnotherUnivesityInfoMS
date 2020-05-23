import json

import django.views.decorators.csrf
from django.contrib import auth
from django.views.decorators.http import require_http_methods

from .general import *
from .models import *


@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def login(request: HttpRequest):
    params = json.loads(request.body.decode())
    if 'id' not in params:
        return response_error('missing id')
    if 'password' not in params:
        return response_error('missing password')
    id = params['id']
    password = params['password']
    # 把 person_id 作为 account
    teacher = Teacher.objects.filter(id=id)
    student = Student.objects.filter(id=id)
    if id == 'admin':
        username = id
        type = 0
    elif teacher.exists():
        username = teacher.values('person_id')[0]['person_id']
        type = 1
    elif student.exists():
        username = student.values('person_id')[0]['person_id']
        type = 2
    else:
        return response_error(f'can not find {id}')
    user = auth.authenticate(username=username, password=password)
    if user is None:  # 验证失败
        return response_error('wrong password')
    auth.login(request, user)
    return JsonResponse({
        'code': 1,
        'type': type,
        'id': id,
        'person_id': username
    })


@hold_exception
@require_http_methods(['GET'])
@django.views.decorators.csrf.csrf_exempt
def logout(request: HttpRequest):
    auth.logout(request)
    return response_success()
