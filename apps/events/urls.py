from django.urls import path
from .views import EventAPI


app_name = 'events'

urlpatterns = [
    path('events/', EventAPI.as_view()),
]