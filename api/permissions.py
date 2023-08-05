from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    If the user is the owner, the user gets the rights to CRUD
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
