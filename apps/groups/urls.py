from django.urls import path
from .views import GroupAPI


app_name = 'groups'

urlpatterns = [
    path('groups/', GroupAPI.as_view()),
]