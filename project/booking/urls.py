
from django.conf.urls import url
from django.urls import path
from .api import BookingCreateApi,BookingApi,BookingRetrieveApi,BookingDeleteApi,MyBookingRetrieveApi

urlpatterns = [
    path('api/create', BookingCreateApi),
    path('api', BookingApi.as_view()),
    path('api/<int:pk>', BookingRetrieveApi.as_view()),
    path('api/mybook/<int:pk>', MyBookingRetrieveApi),
    path('api/<int:pk>/delete', BookingDeleteApi.as_view()),
]
