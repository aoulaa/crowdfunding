from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import Project
from project.serializers.search import ProjectSearchSerializer


class ProjectSearchView(APIView):

    def get(self, request):
        q = request.GET.get('q')
        if not q:
            return Response([], status=status.HTTP_200_OK)
        projects = Project.objects.filter(
            Q(title__icontains=q) | Q(details__icontains=q), is_deleted=False
        )
        serializer = ProjectSearchSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
