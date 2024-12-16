from rest_framework import viewsets, permissions
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, pk=None):
        client = self.get_object()
        projects = client.projects.all()
        serializer = self.get_serializer(client)
        project_data = ProjectSerializer(projects, many=True).data
        return Response({**serializer.data, 'projects': project_data})

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(users=self.request.user)

    def home(request):
        return render(request, 'home.html')
    def client_list(request):
        clients = Client.objects.all()
        return render(request, 'client_list.html', {'clients': clients})

    def project_list(request):
        projects = Project.objects.all()
        return render(request, 'project_list.html', {'projects': projects})