from django.urls import path
from .views import GroupAPI, GroupRegisterUserAPI


app_name = 'groups'

urlpatterns = [
    path('groups/', GroupAPI.as_view()),
    path('groups/add-user/', GroupRegisterUserAPI.as_view()),
]