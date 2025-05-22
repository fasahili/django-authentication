from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),

    # Include all URLs from the 'accounts' app
    path('', include('accounts.urls')),
]
