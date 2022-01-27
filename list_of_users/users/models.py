from django.db import models
from django.urls import reverse


class Users(models.Model):
    """Пользователи"""

    class Status(models.TextChoices):
        """Статус"""

        ACTIVATED = "активирован"
        DEACTIVATED = "не активирован"
        DELETED = "удален"

    first_name = models.CharField(
        verbose_name="Фамилия", max_length=50, blank=True, null=True
    )
    last_name = models.CharField(
        verbose_name="Имя", max_length=50, blank=True, null=True
    )
    patronymic = models.CharField(
        verbose_name="Отчество", max_length=50, blank=True, null=True
    )
    date_of_birth = models.DateField(
        verbose_name="День рождения", null=True, blank=True
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона", max_length=50, blank=True, null=True
    )
    status = models.CharField(
        verbose_name="Статус", max_length=50, choices=Status.choices
    )
    photo = models.ImageField(null=True, blank=True, upload_to="photo/")

    def __str__(self):
        return f"Пользователь {self.first_name} {self.last_name} {self.patronymic}"

    def get_absolute_url(self):
        return reverse("users", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
