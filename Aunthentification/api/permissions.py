from rest_framework.permissions import BasePermissionMetaclass, SAFE_METHODS


class BasePermission(metaclass=BasePermissionMetaclass):
    def has_permission(self, request, view):
        return True
    def has_object_permission(self, request, view, obj):
        return True
class IsAdminOrDeadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user