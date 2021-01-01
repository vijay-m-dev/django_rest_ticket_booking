
from django.urls import path
from .api import PassengerApi,PassengerUpdateApi,PassengerDeleteApi,PassengerRetrieveApi

urlpatterns = [
    path('api',PassengerApi.as_view()),
    path('api/<int:pk>',PassengerRetrieveApi.as_view()),
    path('api/<int:pk>/update',PassengerUpdateApi.as_view()),
    path('api/<int:pk>/delete',PassengerDeleteApi),
]
