from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializer import BookingSerializer,Booking1Serializer
from .models import Booking
from .permissions import IsOwnerOrAdmin

class BookingApi(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser,]
    queryset = Booking.objects.all()
    serializer_class = Booking1Serializer

@api_view(['POST',])
@permission_classes([permissions.IsAuthenticated,])
def BookingCreateApi(request):
    serializer=BookingSerializer(data=request.data)
    if serializer.is_valid():
        print(request.user,serializer.validated_data['user'])
        if request.user.is_superuser == False and request.user != serializer.validated_data['user']:
            return Response({"error":"Invalid User"})
        no_of_tickets=serializer.validated_data['no_of_tickets']
        bus=serializer.validated_data['bus']
        passenger_count=len(serializer.validated_data["passenger"])
        if no_of_tickets!=passenger_count:
            return Response({"message":"Invalid Booking"})
        if no_of_tickets>bus.available_seats:
            return Response({"message":"Not much Tickets Available"})
        serializer.save()
        return Response(serializer.data)
    return Response({"message":"Tickets Not Booked"})


class BookingRetrieveApi(generics.RetrieveAPIView):
    permission_classes = [IsOwnerOrAdmin,]
    queryset = Booking.objects.all()
    serializer_class = Booking1Serializer

@api_view(['GET',])
@permission_classes([permissions.IsAuthenticated,])
def MyBookingRetrieveApi(request,pk):
    if request.user.is_superuser or request.user.pk == pk:
        booking=Booking.objects.filter(user=pk)
        serializer=Booking1Serializer(booking,many=True)
        return Response(serializer.data)
    else:
        return Response({"error":"You are not authorized"})


class BookingDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsOwnerOrAdmin,]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

