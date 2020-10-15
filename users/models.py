from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    name = models.CharField("Name", max_length=255,
                            help_text="Fullname of the Client",
                            default=None)
    cpf = models.CharField("CPF", unique=True, max_length=14,
                           help_text="Valid CPF of the Client")
    email = models.EmailField("Email", unique=True,
                              help_text="Email of the Client")

    class Meta:
        ordering = ['id']
