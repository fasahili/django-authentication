from django.urls import path
from .views import login_view, logout_view, api_login, refresh_token
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/login/', api_login),
    path('api/token/refresh/', refresh_token, name='token-refresh'),
]