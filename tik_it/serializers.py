from rest_framework import serializers
from .models import Venue, Event




class VenueSerializer(serializers.ModelSerializer):
  
    venue_url = serializers.ModelSerializer.serializer_url_field(
    view_name='venue_detail'
   )


    class Meta:
       model = Venue
       fields = ('id', 'name', 'location', 'photo_url', 'description','price','max_occupancy','rating','number_of_rating', 'venue_url')




class EventSerializer(serializers.ModelSerializer):
# when using nested serializer the name you are declaring it as has to be the actual attribute name in the model. So for instance venue here is refering to the venue FK in models.py. This is tricky.
    venue = VenueSerializer(

    )
# Here this was a hyper link when venue1 was passed into fields, however now that the above serializer has been put in place it no longer works. This would just create a link in the api to the venu details page of the venue ID that was selected.
    # venue1 = serializers.HyperlinkedRelatedField(
    #     view_name='venue_detail',
    #     read_only=True
    # )


#This gives you the venue ID in the event Ser.
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )


    class Meta:
        model = Event
        fields = ('id', 'event_name', 'date', 'venue_id', 'venue')
   