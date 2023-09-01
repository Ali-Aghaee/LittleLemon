from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Menu,Booking

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
#define Serializer class for Booking model
class Bookingserializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

#define Serializer class for User model



class UserSerializer(ModelSerializer):

    class Meta:
     model = User
     fields = ['url', 'username', 'email', 'groups']