from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class UserPermission(permissions.BasePermission):

  def has_permission(self, request, view):
    return bool(request.user and request.user.is_authenticated)

  def has_object_permission(self, request, view, obj):
    # Deny actions on objects if the user is not authenticated
    if not request.user.is_authenticated:
      return False

    return obj.user == request.user
