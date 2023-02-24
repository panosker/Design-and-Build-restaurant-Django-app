from django.shortcuts import render
from rest_framework import generics,viewsets ,permissions
from rest_framework.decorators import api_view , permission_classes
from .models import Menu , Bookings
from .serialiers import MenuSerializer,BookingsSerializer
from django.contrib.auth.models import User , Group


# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [permissions.IsAuthenticated]




