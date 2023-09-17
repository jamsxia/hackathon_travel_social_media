from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from VisitedPlace.models import VisitedPlace
from datetime import datetime
from django.views.generic import ListView

class UserVisitedPlacesView(ListView):
    model = VisitedPlace
    template_name = 'blog/user_visited_places.html'
    context_object_name = 'visited_places_data'

    def get_queryset(self):
        username = self.kwargs['username']  # Get the username from URL parameter
        VisitedPlace = self.model.objects.filter(user__username=username)
        visited_places_data = [{
            'user': place.user.username,
            'location_name': place.location_name,
            'latitude': float(place.latitude),
            'longitude': float(place.longitude),
            'comment': place.comment,
        }
        for place in VisitedPlace
        ]
        return visited_places_data

def home(request):
    visited_places = VisitedPlace.objects.all()
    visited_places_data = [
    {
        'user': place.user.username,
        'location_name': place.location_name,
        'latitude': float(place.latitude),
        'longitude': float(place.longitude),
        'comment': place.comment,
    }
    for place in visited_places
    ]

    return render(request, 'blog/home.html', {'visited_places_data': visited_places_data})
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
