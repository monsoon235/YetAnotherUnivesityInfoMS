from django.db import models


class Campus(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=45)


class Person(models.Model):
    class IDTypeChoice(models.IntegerChoices):
        ID_CARD = 0, 'id_card'
        PASSPORT = 1, 'passport'

    class GenderChoice(models.IntegerChoices):
        MALE = 0, 'male'
        FEMALE = 1, 'female'

    id = models.CharField(max_length=20, primary_key=True)
    id_type = models.IntegerField(choices=IDTypeChoice.choices, default=IDTypeChoice.ID_CARD)
    name = models.CharField(max_length=45)
    gender = models.IntegerField(choices=GenderChoice.choices, default=GenderChoice.MALE)
    birth = models.DateTimeField()
    country = models.CharField(max_length=45)
    family_address = models.CharField(max_length=45, null=True)
    family_zipcode = models.CharField(max_length=10, null=True)
    family_tel = models.CharField(max_length=20, null=True)


class Major(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    charge_person = models.ForeignKey(Person, on_delete=models.PROTECT)


class Teacher(models.Model):
    class TitleChoice(models.IntegerChoices):
        PROFESSOR = 0, 'professor'
        VICE_PROFESSOR = 1, 'vice_professor'

    id = models.CharField(max_length=10, primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    enroll_date = models.DateTimeField()
    email = models.EmailField()
    title = models.IntegerField(choices=TitleChoice.choices, default=TitleChoice.PROFESSOR)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)


class Class(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    found_date = models.DateTimeField()
    grade = models.IntegerField()
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    charge_teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)


class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    enroll_date = models.DateTimeField()
    email = models.EmailField()
    class0 = models.ForeignKey(Class, on_delete=models.PROTECT)


class Course(models.Model):
    class AssessmentChoice(models.IntegerChoices):
        EXAM = 0, 'exam'
        REPLY = 1, 'reply'

    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    assessment = models.IntegerField(choices=AssessmentChoice.choices, default=AssessmentChoice.EXAM)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)


class Lecture(models.Model):
    class TermChoice(models.IntegerChoices):
        SPRING = 0, 'spring'
        AUTUMN = 1, 'autumn'

    id = models.CharField(max_length=10, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    year = models.IntegerField()
    term = models.IntegerField(choices=TermChoice.choices, default=TermChoice.SPRING)
    time = models.IntegerField(default=1)

    # class Meta:
    #     db_constraints = {
    #         'time_choice': 'check(time>=1 and time <=45)',
    #     }


class Selection(models.Model):
    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    score = models.IntegerField(null=True)

    class Meta:
        unique_together = ("lecture", "student")


class Adjustment(models.Model):
    class TypeChoice(models.IntegerChoices):
        CHANGE_MAJOR = 0, 'change_major'
        DOWNGRADE = 1, 'downgrade'

    id = models.CharField(max_length=20, primary_key=True)
    from_class = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='from_class_id')
    to_class = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='to_class_id')
    type = models.IntegerField(choices=TypeChoice.choices, default=TypeChoice.CHANGE_MAJOR)
    date = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT)


class ChangeMajor(models.Model):
    class CCYLChange(models.IntegerChoices):
        YES = 0, 'yes'
        NO = 1, 'no'
        NONE = 2, 'none'

    student = models.OneToOneField(Student, on_delete=models.PROTECT, primary_key=True)
    adjustment = models.OneToOneField(Adjustment, on_delete=models.PROTECT)
    ccyl_change = models.IntegerField(choices=CCYLChange.choices, default=CCYLChange.NONE)


class Downgrade(models.Model):
    class ReasonChoice(models.IntegerChoices):
        SUSPEND = 0, 'suspend'
        SUPPORT_TEACHING = 1, 'support_teaching'

    student = models.OneToOneField(Student, on_delete=models.PROTECT, primary_key=True)
    adjustment = models.OneToOneField(Adjustment, on_delete=models.PROTECT)
    reason = models.IntegerField(choices=ReasonChoice.choices, default=ReasonChoice.SUSPEND)
