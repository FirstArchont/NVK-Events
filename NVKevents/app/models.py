from django.db import models
from django.core.validators import MinValueValidator

class ProfileToEvents(models.Model):
    profile = models.BigIntegerField(unique=True, verbose_name="ID ТГ-профиля")
    username = models.CharField(verbose_name="Username", max_length=255)

    def __str__(self):
        return f'Профиль "{self.username}"'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(ProfileToEvents, on_delete=models.CASCADE, default=None, blank=True)
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    short_description = models.TextField(verbose_name="Краткое описание")
    location = models.CharField(verbose_name="Место", max_length=255)
    datetime = models.DateTimeField(verbose_name="Время")
    participants_requirements = models.CharField(verbose_name="Требования к участникам", max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Количество мест")
    cover = models.ImageField(upload_to='app/covers/', verbose_name="Обложка")
    participants = models.TextField(verbose_name="Участники", blank=True)

    def __str__(self):
        return f'Мероприятие "{self.title}"'

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"