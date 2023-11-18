from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_occupancy = models.IntegerField()
    rating = models.IntegerField()
    number_of_rating = models.IntegerField()

    def __str__(self):
        return self.name
    

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    event_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    

    def __str__(self):
        return self.event_name
