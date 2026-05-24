from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class FeaturedProjectsView(APIView):
    def get(self, request):
        projects = Project.objects.filter(is_featured=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
