from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Кастомный пермишен, который разрешит полный доступ к объекту только."""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Автором должен быть текущий пользователь."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
