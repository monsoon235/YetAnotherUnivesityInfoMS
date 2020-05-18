# from __future__ import unicode_literals
#
# from django.db import models
#
# # Create your models here.
# # -*- coding: utf-8 -*-
#
# from django.db import models
#
#
# # Create your models here.
# class Student(models.Model):
#     student_name = models.CharField(max_length=64)
#     add_time = models.DateTimeField(auto_now_add=True)
#
#     def __unicode__(self):
#         return self.student_name


from django.db import models


class Campus(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=45)


class Major(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    campus_id = models.ForeignKey(Campus, on_delete=models.PROTECT)
    # charge_teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)


class Person(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    id_type = models.TextChoices('id_type', 'id_card passport')
    name = models.CharField(max_length=45)
    gender = models.TextChoices('gender', 'male female')
    birth = models.DateField()
    country = models.CharField(max_length=45)
    family_address = models.CharField(max_length=45, null=True)
    family_zipcode = models.CharField(max_length=10, null=True)
    family_tel = models.CharField(max_length=20, null=True)


class Teacher(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    enroll_date = models.DateField()
    email = models.EmailField()
    title = models.TextChoices('title', 'professor vice_professor')
    major_id = models.ForeignKey(Major, on_delete=models.PROTECT)


Major.charge_teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)


class Class(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    found_date = models.DateField()
    grade = models.IntegerField()
    major_id = models.ForeignKey(Major, on_delete=models.PROTECT)
    charge_teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)


class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    enroll_date = models.DateField()
    email = models.EmailField()
    class_id = models.ForeignKey(Class, on_delete=models.PROTECT)


class Course(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    assessment = models.TextChoices('assessment', 'exam reply')
    major_id = models.ForeignKey(Major, on_delete=models.PROTECT)


class Lecture(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    year = models.IntegerField()
    term = models.Choices('term', 'Spring Autumn')
    time = models.IntegerChoices('time', ' '.join(str(i) for i in range(1, 46)))


class Selection(models.Model):
    id = models.TextField(max_length=20, primary_key=True)
    lecture_id = models.ForeignKey(Lecture, on_delete=models.PROTECT)
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    score = models.IntegerField(null=True)


class Adjustment(models.Model):
    id = models.TextField(max_length=20)
    from_class_id = models.ForeignKey(Class, on_delete=models.PROTECT)
    to_class_id = models.ForeignKey(Class, on_delete=models.PROTECT)
    type = models.Choices('type', 'change_major downgrade')
    date = models.DateField()
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)


class ChangeMajor(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT, primary_key=True)
    adjustment_id = models.ForeignKey(Adjustment, on_delete=models.PROTECT)
    ccyl_change = models.TextChoices('ccyl_change', 'yes no none')


class Downgrade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT, primary_key=True)
    adjustment_id = models.ForeignKey(Adjustment, on_delete=models.PROTECT)
    reason = models.TextChoices('reason', 'suspend support_teaching')
