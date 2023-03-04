from django.shortcuts import render
from user.serializers import *
from user.models import *
from rest_framework import generics, permissions, pagination, status
from rest_framework.views import APIView

# Create your views here.
class index(generics.ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentDataSerializer
    permission_classes = [permissions.IsAuthenticated]