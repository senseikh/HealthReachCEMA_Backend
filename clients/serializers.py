
from rest_framework import serializers
from .models import Client
from programs.serializers import EnrollmentSerializer

class ClientSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 'gender',
            'contact_number', 'email', 'address', 'created_at', 'updated_at',
            'created_by', 'enrollments'
        ]
        read_only_fields = ['created_at', 'updated_at', 'created_by']