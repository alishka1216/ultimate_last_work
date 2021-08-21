from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

status_choices = [('phones', 'телефоны'), ('meal', 'еда')]




class Announcement(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, blank=False, related_name='announcement',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    avatar = models.ImageField(
        upload_to='avatars',
        null=True,
        blank=True,
        verbose_name='Картинка объявления'
    )
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    moderate = models.BooleanField(default=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=status_choices, default='other')
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    moderated_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        db_table = 'объявление'
        verbose_name = 'Обълявление'
        verbose_name_plural = 'Объявление'

    def __str__(self):
        return self.title