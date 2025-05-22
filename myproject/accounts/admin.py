from django.contrib import admin
from .models import ExpiringToken

# Registers the ExpiringToken model in the Django admin panel

admin.site.register(ExpiringToken)
