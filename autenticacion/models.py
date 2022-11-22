
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField("Correo electronico", null=False, unique=True)
    first_name = models.CharField("Nombres", max_length=150, null=False)
    last_name = models.CharField(
        "Apellido Paterno", max_length=150, null=False)
    apellido_materno = models.CharField(
        "Apellido Materno", max_length=100, null=True, blank=True)
    matricula = models.CharField(
        "Matricula", max_length=8, unique=True)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username','password', 'first_name', 'matricula', 'last_name']
