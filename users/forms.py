# forms.py

from django import forms
from .models import Resource, Donation, Volunteer

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['crisis', 'name', 'quantity', 'description']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['crisis', 'donor_name', 'amount']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['crisis', 'name', 'contact_info', 'availability_date']
