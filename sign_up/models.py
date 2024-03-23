from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=9, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    # username =
    gmail = models.EmailField()
    is_teacher = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name + " " + self.username

    class Meta:
        db_table = 'CustomUser'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# Create your models here.
