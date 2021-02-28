from django.urls import path
from .views import UserRegisterAPI, UserLoginAPI, UserProfileAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('api/token/', UserLoginAPI.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('user/register', UserRegisterAPI.as_view()),
    path('user/me/', UserProfileAPI.as_view()),
]