from django.urls import path, reverse_lazy
from django.views.generic import CreateView

from . import views
from . import models

urlpatterns = [
    path('schedule/main/', views.main, name='main'),
    path('schedule/course_details/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('schedule/teacher_details/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('schedule/add_course/',
        CreateView.as_view(
            model=models.Student,
            fields='__all__',
            success_url=reverse_lazy('enroll'),
            template_name='schedule/enroll.html'
        ),
        name='enroll'),
]
