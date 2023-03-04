from .models import *
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
        ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "dept_name",
            "dept_code",
            "cordinator",
        ]

class StudentDataSerializer(serializers.ModelSerializer):
    admin = UserDataSerializer(read_only=True)
    class Meta:
        model = StudentUser
        fields = [
            "id",
            "user",
            "profile_pic",
            "gender",
            "dob",
            "address",
            "phone_number",
            "department",
            "current_level",
        ]