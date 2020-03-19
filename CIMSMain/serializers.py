from .models import *
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceRoom
        fields = ('name')
        
class MeetingSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name')
    
    class Meta:
        model = Meeting
        # location = LocationSerializer(read_only=True)

        fields = ('name', 'date', 'location_name', 'location_id')
                  #'location', 'channel')

