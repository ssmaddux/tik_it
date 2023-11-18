from rest_framework import serializers
from .models import Venue, Event




class EventSerializer(serializers.ModelSerializer):

    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )


    class Meta:
        model = Event
        fields = ('id', 'event_name', 'date','venue', 'venue_id')



class VenueSerializer(serializers.ModelSerializer):
  
    venue_url = serializers.ModelSerializer.serializer_url_field(
    view_name='venue_detail'
   )


    class Meta:
       model = Venue
       fields = ('id', 'name', 'location', 'photo_url', 'description','price','max_occupancy','rating','number_of_rating', 'venue_url')
   