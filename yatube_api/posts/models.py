from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """
    Модель для создания постов. В модели описаны поля:
    текст, дата, автор (поле с ссылкой на другую модель 'Users'),
    группы и изображение.
    """
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """
    Модель для добавления комментариев к постам. В модели описаны поля:
    текст, дата, автор поле с ссылкой на другую модель 'Users',
    ссылка на моделль поста.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Group(models.Model):
    """
    Модель для разделения постов по сообществам. В модели описаны поля:
    название группы, адрес, описание сообщества.
    """
    title = models.CharField(
        'Название', max_length=200
    )
    slug = models.SlugField(
        unique=True
    )
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Follow(models.Model):
    """
    Модель-система подписки на авторов.
    """
    user = models.ForeignKey(
        User,
        related_name="follower",
        on_delete=models.CASCADE,
        null=True
    )
    following = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_follow'
            )
        ]
