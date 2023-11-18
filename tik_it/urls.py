# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('venue/', views.VenueListCreateView.as_view(), name='venue_list'),
    path('venues/<int:pk>', views.VenueRetrieveUpdateDestroyView.as_view(), name='venue_detail'),
    path('event/', views.EventListCreateView.as_view(), name='event_list'),
    path('events/<int:pk>', views.EventRetrieveUpdateDestroyView.as_view(), name='event_detail'),
]