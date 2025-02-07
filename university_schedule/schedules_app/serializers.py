# schedules_app/serializers.py
from rest_framework import serializers
from .models import Faculty, Department, EducationalProgram, Subject, Teacher, Group, Schedule, Classroom


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)

    class Meta:
        model = Department
        fields = "__all__"

class EducationalProgramSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = EducationalProgram
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    program = EducationalProgramSerializer(read_only=True)

    class Meta:
        model = Group
        fields = "__all__"

# schedules_app/serializers.py
from .models import Faculty, Department, EducationalProgram, Subject, Teacher, Group, Schedule, Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    group = GroupSerializer(read_only=True)
    classroom = ClassroomSerializer(read_only=True)

    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source='subject', write_only=True
    )
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True
    )
    group_id = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), source='group', write_only=True
    )
    classroom_id = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), source='classroom', write_only=True
    )

    class Meta:
        model = Schedule
        fields = [
            "id", "subject", "teacher", "group", "classroom",
            "subject_id", "teacher_id", "group_id", "classroom_id",
            "week_type", "day_of_week", "start_time", "end_time"
        ]
