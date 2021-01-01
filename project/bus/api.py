from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import BusSerializer
from .models import Bus
from rest_framework.decorators import api_view, permission_classes

class BusApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


@api_view(['POST',])
@permission_classes([permissions.IsAdminUser,])
def BusCreateApi(request):
    serializer=BusSerializer(data=request.data)
    if serializer.is_valid():
        available_seats=serializer.validated_data['available_seats']
        total_seats=serializer.validated_data['total_seats']
        if available_seats>total_seats:
        	return Response({"error":"available seats should be less than total_seats"})
        serializer.save()
        return Response(serializer.data)
    return Response({"error":"Invalid Bus"})

class BusRetrieveApi(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


@api_view(['PUT',])
@permission_classes([permissions.IsAdminUser,])
def BusUpdateApi(request,pk):
	bus=Bus.objects.get(pk=pk)
	serializer=BusSerializer(bus,data=request.data)
	if serializer.is_valid():
		available_seats=serializer.validated_data['available_seats']
		total_seats=serializer.validated_data['total_seats']
		if available_seats>total_seats:
			return Response({"error":"available seats should be less than total_seats"})
		serializer.save()
		return Response(serializer.data)
	else:
		return Response({"error":"Invalid Bus"})

class BusDeleteApi(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser,]
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
