from rest_framework.permissions import BasePermission, SAFE_METHODS

from main.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or IsAdmin().has_permission(
            request, view)


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or IsStaff().has_permission(
            request, view)
