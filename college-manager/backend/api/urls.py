from django.urls import path



from . import campus, major, teacher, student, class_, course, lecture, selection,adjustment
from . import views

urlpatterns = [
    path('', views.index),
    path('adjustment/get', adjustment.get),
    path('adjustment/add', adjustment.add),
    path('adjustment/del', adjustment.delete),
    path('adjustment/mod', adjustment.mod),


    path('campus/get', campus.get),
    path('campus/add', campus.add),
    path('campus/del', campus.delete),
    path('campus/mod', campus.mod),

    path('class/get', class_.get),
    path('class/add', class_.add),
    path('class/del', class_.delete),
    path('class/mod', class_.mod),
    #
    path('course/get', course.get),
    path('course/add', course.add),
    path('course/del', course.delete),
    path('course/mod', course.mod),

    path('lecture/get', lecture.get),
    path('lecture/add', lecture.add),
    path('lecture/del', lecture.delete),
    path('lecture/mod', lecture.mod),
    #
    path('major/get', major.get),
    path('major/add', major.add),
    path('major/del', major.delete),
    path('major/mod', major.mod),
    #
    path('selection/get', selection.get),
    path('selection/add', selection.add),
    path('selection/del', selection.delete),
    path('selection/mod', selection.mod),
    #
    path('student/get', student.get),
    path('student/add', student.add),
    path('student/del', student.delete),
    path('student/mod', student.mod),
    #
    path('teacher/get', teacher.get),
    path('teacher/add', teacher.add),
    path('teacher/del', teacher.delete),
    path('teacher/mod', teacher.mod),
]
