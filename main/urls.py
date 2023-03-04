from django.urls import path
from .views import *

urlpatterns = [
    path('student_home/', Student_Home.as_view(), name="student_home")
]