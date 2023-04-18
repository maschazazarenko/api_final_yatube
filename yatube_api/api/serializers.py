from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализуем и десериализуем модель Post.
    Переопределим поле автор, чтобы выводилось имя пользователя.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ['id', 'text', 'author', 'image', 'group', 'pub_date']
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализуем и десериализуем модель Comment.
    Переопределим поле автор, чтобы выводилось имя пользователя.
    Поля author и post доступны только для чтения.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ['id', 'author', 'post', 'text', 'created']
        read_only_fields = ['author', 'post']
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализуем и десериализуем модель Group."""
    class Meta:
        fields = ['id', 'title', 'slug', 'description']
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализуем и десериализуем модель Comment.
    Переопределим поля user и following, чтобы выводилось имя пользователя.
    """
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate_following(self, value):
        "Сделаем проверку самоподписки."
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return value
