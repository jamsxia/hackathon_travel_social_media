from django import forms
from .models import VisitedPlace
from datetime import date
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

class VisitedPlaceForm(forms.ModelForm):
    
    class Meta:
        model = VisitedPlace
        fields = ['location_name', 'latitude', 'longitude', 'comment']