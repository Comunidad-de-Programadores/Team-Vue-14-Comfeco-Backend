from django.urls import path
from .views import (UserGroupsAPI, UserRegisterAPI, UserLoginAPI, UserProfileAPI,
                    UserChangePasswordAPI, UserEventAPI, UserGroupsDetailAPI, UserGroupDeleteAPI,
                    UserEventDeleteAPI)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('token/', UserLoginAPI.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/register', UserRegisterAPI.as_view()),
    path('user/me/', UserProfileAPI.as_view(), name='user_profile'),
    path('user/change-password/', UserChangePasswordAPI.as_view(), name='user_change_password'),
    path('user/events/', UserEventAPI.as_view(), name='user_my_events'),
    path('user/groups/', UserGroupsAPI.as_view()),
    path('user/groups/<int:pk>/', UserGroupsDetailAPI.as_view()),
    path('user/groups/<int:pk>/delete/', UserGroupsDetailAPI.as_view()),
    path('user/events/<int:pk>/delete/', UserEventDeleteAPI.as_view())
]