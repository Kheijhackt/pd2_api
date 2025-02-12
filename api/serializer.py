from rest_framework import serializers
from .models import Device

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ['created', 'modified']