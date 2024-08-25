from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import Project, Category
from project.serializers.filter import ProjectFilterSerializer, CategorySerializer


class ProjectCategoryFilterView(APIView):
    def get(self, request, pk):
        queryset = Project.objects.filter(category=pk, is_deleted=False).all()
        serializer = ProjectFilterSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

