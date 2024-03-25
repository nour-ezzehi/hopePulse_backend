from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_staff', 'is_active', 'date_joined', 'username', 'biography', 'role', 'first_name', 'last_name', 'profile_complete', 'telephone_number', 'cin']
