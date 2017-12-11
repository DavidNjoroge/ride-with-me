from rest_framework import serializers
# from .models import MoringaM
from driver.models import LocationDriver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=LocationDriver
        fields=('home_lat','home_lng','dest_lat','dest_lng')