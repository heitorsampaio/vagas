from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Owner Permission
    """

    def has_permission(self, request, view, obj):
        """
        Object Permission
        """
        return obj.client == request.user or request.user.is_superuser
