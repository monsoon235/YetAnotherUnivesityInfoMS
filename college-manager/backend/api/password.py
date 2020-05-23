import json

import django.views.decorators.csrf
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from .general import *
from .models import *


@check_login
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    if 'new' not in params:
        return response_error('missing new password')
    request.user.set_password(params['new'])


@check_admin
@hold_exception
@require_http_methods(['POST'])
@django.views.decorators.csrf.csrf_exempt
def admin_mod(request: HttpRequest):
    params = json.loads(request.body.decode())
    if 'id' not in params:
        return response_error('missing id')
    if 'new' not in params:
        return response_error('missing new password')
    id = params['id']
    teacher = Teacher.objects.filter(id=id)
    student = Student.objects.filter(id=id)
    id = None
    if id == 'admin':
        id = 'admin'
    elif teacher.exists():
        id = teacher.values('person_id')[0]['person_id']
    elif student.exists():
        id = student.values('person_id')[0]['person_id']
    if id is None:
        return response_error(f'can not find {id}')
    User.objects.get(username=id).set_password(params['new'])
    return response_success()
