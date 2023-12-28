from rest_framework import permissions


class UserPermissionsAll(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False
