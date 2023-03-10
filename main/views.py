from django.shortcuts import render
from .serializers import *
from user.models import *
from rest_framework import generics, permissions, pagination, status
from rest_framework.views import APIView

# Create your views here.
class Student_Home(generics.ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        user = request.user
        if qs is not None:
            return qs.filter(student_user = user)
        else:
            return StudentUser.objects.none()

class Staff_Home(generics.ListAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        user = request.user
        if qs is not None:
            return qs.filter(staff_user = user)
        else:
            return StudentUser.objects.none()