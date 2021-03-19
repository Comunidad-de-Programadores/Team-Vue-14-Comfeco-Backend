from django.urls import path
from .views import EventAPI, EventRegisterUserAPI, EventUserDeleteAPI


app_name = 'events'

urlpatterns = [
    path('events/', EventAPI.as_view()),
    path('events/add-user/', EventRegisterUserAPI.as_view()),
    path('events/<int:pk>/delete/', EventUserDeleteAPI.as_view())
]