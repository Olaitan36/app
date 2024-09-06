# forms.py

from django import forms
from .models import Resource, Donation, Volunteer, Crisis,User

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['crisis', 'name', 'quantity', 'description']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['crisis', 'donor_name', 'amount', ]

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['crisis', 'name', 'contact_info', 'availability_date']

class CrisisForm(forms.ModelForm):
    class Meta:
        model = Crisis
        fields = ['name', 'description', 'location', 'start_date','end_date']  # Update with actual fields defined in your model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']  