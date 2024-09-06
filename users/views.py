# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Resource, Donation, Volunteer, User,Crisis
from .forms import ResourceForm, DonationForm, VolunteerForm
from django.db import models


def base_view(request):
    return render(request, 'base.html')

# CRUD for Resources
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})

def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'templates/resource_form.html', {'form': form})

def resource_update(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'templates/resource_form.html', {'form': form})

def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    return render(request, 'templates/resource_confirm_delete.html', {'resource': resource})


# CRUD for Donations
def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'templates/donation_list.html', {'donations': donations})

def donation_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'templates/donation_form.html', {'form': form})

def donation_update(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm(instance=donation)
    return render(request, 'templates/donation_form.html', {'form': form})

def donation_delete(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        donation.delete()
        return redirect('donation_list')
    return render(request, 'templates/donation_confirm_delete.html', {'donation': donation})


# CRUD for Volunteers
def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})

def volunteer_create(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volunteer_form.html', {'form': form})

def volunteer_update(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'volunteer_form.html', {'form': form})

def volunteer_delete(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteer_list')
    return render(request, 'volunteer_confirm_delete.html', {'volunteer': volunteer})
def crisis_report(request, crisis_id):
    crisis = get_object_or_404(Crisis, pk=crisis_id)
    resources = Resource.objects.filter(crisis=crisis)
    donations = Donation.objects.filter(crisis=crisis)
    volunteers = Volunteer.objects.filter(crisis=crisis)
    
    return render(request, 'crisis_report.html', {
        'crisis': crisis,
        'resources': resources,
        'donations': donations,
        'volunteers': volunteers,
    })
def crisis_list(request):
    crises = Crisis.objects.all()
    return render(request, 'crisis_list.html', {'crises': crises})





