
from rest_framework import serializers
from .models import Menu , Bookings

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Bookings
        fields ='__all__'


        