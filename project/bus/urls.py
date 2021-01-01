
from django.urls import path
from .api import BusApi,BusUpdateApi,BusRetrieveApi,BusDeleteApi,BusCreateApi

urlpatterns = [
    path('api',BusApi.as_view()),
    path('api/create',BusCreateApi),
    path('api/<int:pk>',BusRetrieveApi.as_view()),
    path('api/<int:pk>/update',BusUpdateApi),
    path('api/<int:pk>/delete',BusDeleteApi.as_view()),
]
