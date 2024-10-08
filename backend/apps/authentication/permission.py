from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff and request.user.is_superuser:
            return True
        return obj == request.user
