# schedules_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, TeacherViewSet, GroupViewSet, ScheduleViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'schedules', ScheduleViewSet, basename='schedules')

urlpatterns = [
    path('', include(router.urls)),
]
