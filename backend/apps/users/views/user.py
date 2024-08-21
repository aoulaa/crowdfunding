from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permission import IsAdminOrOwner
from users.models import User
from users.serializers.user import UserSerializer


class UserDetailView(APIView):

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminOrOwner()]
        return super().get_permissions()

    def get(self, request, key):
        queryset =get_object_or_404(User, id=key)
        serializer = UserSerializer(queryset, context={'request': request})
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, key):
        queryset =get_object_or_404(User, id=key)
        self.check_object_permissions(request, queryset)
        serializer = UserSerializer(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, key):
        queryset =get_object_or_404(User, id=key)
        self.check_object_permissions(request, queryset)
        queryset.is_active = False
        queryset.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

