from rest_framework import serializers
from .models import Program, Enrollment

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at']
        read_only_fields = ['created_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(read_only=True)
    program_id = serializers.PrimaryKeyRelatedField(
        queryset=Program.objects.all(), source='program', write_only=True
    )

    class Meta:
        model = Enrollment
        fields = ['id', 'client', 'program', 'program_id', 'enrollment_date', 'status']
        read_only_fields = ['enrollment_date']