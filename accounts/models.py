from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя',
        related_name='profile',
    )

    def __str__(self):
        return self. user.username

    class Meta:
        db_table = 'profiles'
        verbose_name='Профиль пользователя'
        verbose_name_plural='Профили пользователя'