from django.db import models


class Teachers(models.Model):
    MALE = 1
    FEMALE = 2
    SEX_TYPES = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    )

    surname = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    middle_name = models.CharField(max_length=1000, blank=True, null=True)
    birthday = models.DateField()
    sex = models.IntegerField(choices=SEX_TYPES, default=FEMALE, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    telephone_number = models.CharField(max_length=1000, blank=True, null=True)
    job_post = models.CharField(max_length=1000, blank=True, null=True)
    date_job = models.DateField()
    subject = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return f"{self.surname} {self.name} {self.middle_name}"


class Groups(models.Model):
    number_group = models.IntegerField(blank=True, default=1, null=True)
    number_1_students = models.IntegerField(blank=True, default=1, null=True)
    date_1_creation = models.DateField(blank=True, null=True)
    date_2_creation = models.DateField(blank=True, null=True)

    TEACHER_CHOICES = [(teachers.id, f"{teachers.surname} {teachers.name} {teachers.middle_name}") for teachers in Teachers.objects.all()]
    data_teacher = models.CharField(choices=TEACHER_CHOICES, max_length=1000, blank=True, null=False)

    class Meta:
        db_table = 'groups'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f"{self.number_group}"


class Works(models.Model):
    number_work = models.IntegerField(blank=True, default=1, null=True)
    date_1 = models.DateField(blank=True, null=True)
    number_groupn = models.IntegerField(blank=True, default=1, null=True)
    number_1_students = models.IntegerField(blank=True, default=1, null=True)
    number_2_students = models.IntegerField(blank=True, default=1, null=True)
    description_work = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'works'
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return f"{self.number_work}"

class Students(models.Model):
    MALE = 1
    FEMALE = 2
    SEX_TYPES = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    )

    surname = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    middle_name = models.CharField(max_length=1000, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.IntegerField(choices=SEX_TYPES, default=FEMALE, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    telephone_number = models.CharField(max_length=1000, blank=True, null=True)
    date_join = models.DateField(blank=True, null=True)
    date_leave = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    GROUP_CHOICES = [(group.id, group.number_group) for group in Groups.objects.all()]
    number_group = models.CharField(choices=GROUP_CHOICES, max_length=1000, blank=True, null=False)

    class Meta:
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.surname