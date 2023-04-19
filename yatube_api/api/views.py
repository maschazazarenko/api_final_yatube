from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, filters

from posts.models import Post, Group

from api.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer)
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD для работы с постами.

    Пермишен дает два варианта прав.
    1) Только аутентифицированные пользователи имеют доступ к API.
    2) Полный доступ к объекту поста, изменение, удаление только автору.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        """Создавать новый объект может только автор."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """CRUD для работы с группами."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthorOrReadOnly
    ]


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD для работы с комментариями.

    Пермишен дает два варианта прав.
    1) Только аутентифицированные пользователи имеют доступ к API.
    2) Полный доступ к объекту комментария, изменение, удаление только автору.
    """
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        """Переприоделим queryset, нам нужны комментарии выбранного поста."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """
        Автором коментария является текущий пользователь.
        Комментарии принадлежат определенному посту.
        """
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    """
    CRUD для работы с подписками.

    Только аутентифицированные пользователи имеют доступ к API.
    """
    serializer_class = FollowSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        """Переопределим queryset, используя related_name для подписок."""
        current_user = self.request.user
        return current_user.follower.all()

    def perform_create(self, serializer):
        """Post-запрос может сделать только текущий пользователь."""
        serializer.save(user=self.request.user)
