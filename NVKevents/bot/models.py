from django.db import models

class Profile(models.Model):
    tg_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")  # telegram user id
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name="username")  # telegram login
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фамилия") 
    photo = models.ImageField(upload_to='bot/profiles/', verbose_name="Фотка")

    def __str__(self):
        return f'Пользователь {self.username}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"