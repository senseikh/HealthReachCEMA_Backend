from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Client
from .serializers import ClientSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]  # Change this to IsAuthenticated if needed
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender', 'created_by']
    search_fields = ['first_name', 'last_name', 'email']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            # Only authenticated users can create a client
            serializer.save(created_by=self.request.user)
        else:
            raise PermissionDenied("You must be logged in to create a client.")
