from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name} ({self.faculty})"


class EducationalProgram(models.Model):
    name = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return f"{self.name} ({self.department})"


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    academic_degree = models.CharField(max_length=255, blank=True)  # учёная степень (например, кандидат наук)
    academic_title = models.CharField(max_length=255, blank=True)   # учёное звание (например, доцент)
    position = models.CharField(max_length=255, blank=True)         # должность (например, профессор)
    departments = models.ManyToManyField(Department, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='groups')
    program = models.ForeignKey(EducationalProgram, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Номер аудитории, например, "101А"
    building = models.CharField(max_length=255, blank=True)  # Корпус, например, "Главный корпус"

    def __str__(self):
        return f"{self.name} ({self.building})"


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    WEEK_TYPE_CHOICES = [
        (0, "Чётная неделя"),
        (1, "Нечётная неделя"),
        (2, "Обе недели")
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='schedules')

    week_type = models.IntegerField(choices=WEEK_TYPE_CHOICES, default=2)
    day_of_week = models.IntegerField()  # 0 - Понедельник, 1 - Вторник и т.д.
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        week_type_str = dict(self.WEEK_TYPE_CHOICES).get(self.week_type, "Обе недели")
        return f"{self.group} | {self.subject} | {week_type_str} | {self.day_of_week} {self.start_time}-{self.end_time}"

