from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class ExpiringToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created + timedelta(hours=1)

    def __str__(self):
        return f"Token({self.user.username})"
