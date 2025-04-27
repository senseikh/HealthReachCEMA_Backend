from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Program, Enrollment
from .serializers import ProgramSerializer, EnrollmentSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


    
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [AllowAny]  

    def perform_create(self, serializer):
        # Just save the enrollment without trying to set client__created_by
        serializer.save()
            
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Enrollment.objects.filter(client__created_by=self.request.user)
        return Enrollment.objects.none()  # Unauthenticated users can only create, not view