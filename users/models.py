from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(default=0, null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField(
        upload_to='media/', null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heir', 'heif'])]
    )

    def __str__(self):
        return self.first_name

