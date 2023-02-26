from django.shortcuts import render
from rest_framework import generics,viewsets 
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import Menu , Bookings
from .serializers import MenuSerializer , BookingsSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User 
from rest_framework import status


# Create your views here.
def index(request):
    return render(request,'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def post(self,request):
        searialized_item =MenuSerializer(data=request.data)
        searialized_item.is_valid(raise_exception=True)
        searialized_item.save()
        return Response(searialized_item.validated_data,status.HTTP_201_CREATED)

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def delete(self,request):
        return self.destroy(request)

    


class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAuthenticated]


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]




