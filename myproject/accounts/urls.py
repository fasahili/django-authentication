from django.urls import path
from .views import api_login, refresh_token, HomeView, LoginView, LogoutView

# Maps URL paths to their corresponding view functions.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/login/', api_login),
    path('api/token/refresh/', refresh_token, name='token-refresh'),
]