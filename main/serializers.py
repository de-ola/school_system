from user.models import *
from user.serializers import DepartmentSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    change_password = serializers.HyperlinkedIdentityField(view_name='change_password', lookup_field = 'pk')
    update_user_profile = serializers.HyperlinkedIdentityField(view_name='update_profile', lookup_field = 'pk')
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'change_password',
            'update_user_profile',
        ]


class StudentDataSerializer(serializers.ModelSerializer):
    student_user = UserSerializer(read_only=True)
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
    student_user = UserSerializer(read_only=True)
    class Meta:
        model = StudentUser
        fields = [
            'id',
            'student_user',
            'profile_pic',
            'gender',
            'dob',
            'address',
            'phone',
            'department',
            'current_level',
        ]

class StaffDataSerializer(serializers.ModelSerializer):
    staff_user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only = True)
    update_user_profile = serializers.HyperlinkedIdentityField(view_name='update_profile', lookup_field = 'pk')

    class Meta:
        model = StaffUser
        fields = [
            "id",
            "staff_user",
            "profile_pic",
            "title",
            "address",
            "phone_number",
            "department",
        ]

class StaffDataSerializer(serializers.ModelSerializer):
    staff_user = UserSerializer(read_only=True)

    class Meta:
        model = StaffUser
        fields = [
            "id",
            "staff_user",
            "profile_pic",
            "title",
            "address",
            "phone_number",
            "department",
        ]