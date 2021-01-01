from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import PassengerSerializer,Passenger1Serializer
from .models import Passenger
from .permissions import IsOwnerOrAdmin
from rest_framework.decorators import api_view, permission_classes


class PassengerApi(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser,]
    queryset = Passenger.objects.all()
    serializer_class = Passenger1Serializer

class PassengerRetrieveApi(generics.RetrieveAPIView):
    permission_classes = [IsOwnerOrAdmin,]
    queryset = Passenger.objects.all()
    serializer_class = Passenger1Serializer

class PassengerUpdateApi(generics.UpdateAPIView):
    permission_classes = [IsOwnerOrAdmin,]
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

@api_view(['DELETE',])
@permission_classes([permissions.IsAuthenticated,])
def PassengerDeleteApi(request, pk):
    passenger=Passenger.objects.get(pk=pk)
    if request.user!=passenger.booking.user and request.user.is_superuser==False:
        return Response({"error":"You are not permitted"})
    booking=passenger.booking
    if booking.no_of_tickets==1:
        booking.delete()
        return Response({"message":"Passenger and booking deleted successfully"})
    else:
        booking.no_of_tickets-=1
        booking.save()
        bus=booking.bus
        bus.available_seats+=1
        bus.save()
        passenger.delete()
        return Response({"message":"Passenger deleted successfully"})
