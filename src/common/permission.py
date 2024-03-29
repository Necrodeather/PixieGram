from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "PATCH", "DELETE"):
            return obj.user == request.user
        return True
