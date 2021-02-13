from django.urls import path
from .views import UserRegisterAPI

app_name = 'users'

urlpatterns = [
    path('user/register', UserRegisterAPI.as_view())
]