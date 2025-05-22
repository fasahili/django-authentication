from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExpiringToken
from .utils import generate_token
from django.views import View
from django.utils.decorators import method_decorator


# Handles user authentication logic including login, logout, and token management.

@api_view(['POST'])
def refresh_token(request):
    old_token_key = request.data.get('token')

    try:
        token = ExpiringToken.objects.get(key=old_token_key)
    except ExpiringToken.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=400)

    if token.is_expired():
        return Response({'error': 'Token expired'}, status=403)

    token.delete()
    new_token = generate_token(token.user)

    return Response({'token': new_token.key, 'message': 'Token refreshed successfully'})


@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token = ExpiringToken.objects.filter(user=user).first()
        if token and not token.is_expired():
            return Response({'token': token.key, 'message': 'Existing token valid'})
        else:
            token = generate_token(user)
            return Response({'token': token.key, 'message': 'New token created'})
    return Response({'error': 'Invalid credentials'}, status=400)



# Handles user login
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})


# Handles user logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# Shows the homepage, requires login
@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        return render(request, 'accounts/home.html')






