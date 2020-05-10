from rest_framework import serializers
from .models import Customer, Service


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number', 'vin_number', 'description', 'date_requested')


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('name', 'description', 'avg_time', 'price')