from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CreditEntry
from .models import Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
class CreditEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditEntry
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
