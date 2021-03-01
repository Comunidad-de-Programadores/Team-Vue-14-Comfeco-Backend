from django.urls import path
from .views import UserRegisterAPI, UserLoginAPI, UserProfileAPI, UserChangePasswordAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('api/token/', UserLoginAPI.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('user/register', UserRegisterAPI.as_view()),
    path('user/me/', UserProfileAPI.as_view(), name='user_profile'),
    path('user/change-password/', UserChangePasswordAPI.as_view(), name='user_change_password'),
]