from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer