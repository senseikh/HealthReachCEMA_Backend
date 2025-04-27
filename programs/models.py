from django.db import models
from clients.models import Client
from django.contrib.auth.models import User

class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('ACTIVE', 'Active'), ('COMPLETED', 'Completed'), ('DROPPED', 'Dropped')],
        default='ACTIVE'
    )

    class Meta:
        unique_together = ['client', 'program']
        ordering = ['enrollment_date']

    def __str__(self):
        return f"{self.client} - {self.program}"
