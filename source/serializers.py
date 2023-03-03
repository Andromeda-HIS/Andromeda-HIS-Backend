from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=['admin_id','admin_username','admin_password']