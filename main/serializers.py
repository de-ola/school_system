from user.models import *
from user.serializers import UserDataSerializer, DepartmentSerializer
from rest_framework import serializers

class StudentDataSerializer(serializers.ModelSerializer):
    student_user = UserDataSerializer(read_only=True)
    department = DepartmentSerializer(read_only = True)
    class Meta:
        model = StudentUser
        fields = [
            "id",
            "student_user",
            "profile_pic",
            "gender",
            "dob",
            "address",
            "phone_number",
            "department",
            "current_level",
        ]

class StudentProfileEditSerializer(serializers.ModelSerializer):
    student_user = UserDataSerializer(read_only=True)
    class Meta:
        model = StudentUser
        fields = [
            "id",
            "student_user",
            "profile_pic",
            "gender",
            "dob",
            "address",
            "phone",
            "department",
            "current_level",
        ]