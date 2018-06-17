from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from . import views

app_name = 'students'

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', login_required(views.StudentEnrollCourseView.as_view()), name='student_enroll_course'),
    path('courses/', login_required(views.StudentCourseListView.as_view()), name='student_course_list'),
    path('<int:pk>/', cache_page(60*15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('<int:pk>/<int:module_id>/', cache_page(60*15)(views.StudentCourseDetailView.as_view()), name='student_course_detail_module')
]