from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permission import IsAdminOrOwner
from project.models import Project
from project.serializers.project import ProjectSerializer




class ProjectListCreateView(APIView):

    def get(self, request):
        queryset = Project.objects.filter(is_deleted=False).all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectDetailView(APIView):
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminOrOwner()]
        return super().get_permissions()

    def get(self, request, pk):
        project = Project.objects.get(pk=pk, is_deleted=False)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):

        project = Project.objects.get(pk=pk, is_deleted=False)
        self.check_object_permissions(request, project.creator)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk, is_deleted=False)
        self.check_object_permissions(request, project.creator)
        project.is_deleted = True
        project.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
