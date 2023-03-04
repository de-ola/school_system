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