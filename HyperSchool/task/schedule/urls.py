from django.urls import path
from . import views

urlpatterns = [
    path('schedule/main/', views.main, name='main'),
    path('schedule/course_details/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('schedule/teacher_details/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
]
