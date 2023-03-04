from .models import *
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
        ]