from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class IsStaffGroup(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Staff").exists()
        )


class IsAdminGroup(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Admin").exists()
        )


class IsAdminOrStaffGroup(BasePermission):
    def has_permission(self, request, view):
        return IsAdminGroup().has_permission(
            request, view
        ) or IsStaffGroup().has_permission(request, view)


class IsCustomerGroup(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Customer").exists()
        )


class IsOwnerUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user == obj.user)


class IsOwnerUserOrIsAdminOrStaffGroup(BasePermission):
    def has_object_permission(self, request, view, obj):
        return IsOwnerUser().has_object_permission(
            request, view, obj
        ) or IsAdminOrStaffGroup().has_permission(request, view)
