# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Resource, Donation, Volunteer, User,Crisis
from .forms import ResourceForm, DonationForm, VolunteerForm, CrisisForm
from django.db import models


def base_view(request):
    return render(request, 'base.html')
# Resource Views
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return render(request, 'resource_detail.html', {'resource': resource})

def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resource_form.html', {'form': form})

def resource_update(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_detail', resource_id=resource.id)
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'resource_form.html', {'form': form})

def resource_delete(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    return render(request, 'resource_confirm_delete.html', {'resource': resource})

# Donation Views
def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donation_list.html', {'donations': donations})

def donation_detail(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    return render(request, 'donation_detail.html', {'donation': donation})

def donation_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'donation_form.html', {'form': form})

def donation_update(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_detail', donation_id=donation.id)
    else:
        form = DonationForm(instance=donation)
    return render(request, 'donation_form.html', {'form': form})

def donation_delete(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    if request.method == 'POST':
        donation.delete()
        return redirect('donation_list')
    return render(request, 'donation_confirm_delete.html', {'donation': donation})

# Volunteer Views
def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})

def volunteer_detail(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    return render(request, 'volunteer_detail.html', {'volunteer': volunteer})

def volunteer_create(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volunteer_form.html', {'form': form})

def volunteer_update(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_detail', volunteer_id=volunteer.id)
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'volunteer_form.html', {'form': form})

def volunteer_delete(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteer_list')
    return render(request, 'volunteer_confirm_delete.html', {'volunteer': volunteer})

# Crisis Views
def crisis_list(request):
    print("Crisis list view called")
    crises = Crisis.objects.all()
    return render(request, 'users/crisis_list.html', {'crises': crises})


def crisis_detail(request, crisis_id):
    crisis = get_object_or_404(Crisis, id=crisis_id)
    return render(request, 'crisis_detail.html', {'crisis': crisis})

def crisis_create(request):
    if request.method == 'POST':
        form = CrisisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crisis_list')
    else:
        form = CrisisForm()
    return render(request, 'crisis_form.html', {'form': form})

def crisis_update(request, crisis_id):
    crisis = get_object_or_404(Crisis, id=crisis_id)
    if request.method == 'POST':
        form = CrisisForm(request.POST, instance=crisis)
        if form.is_valid():
            form.save()
            return redirect('crisis_detail', crisis_id=crisis.id)
    else:
        form = CrisisForm(instance=crisis)
    return render(request, 'crisis_form.html', {'form': form})

def crisis_delete(request, crisis_id):
    crisis = get_object_or_404(Crisis, id=crisis_id)
    if request.method == 'POST':
        crisis.delete()
        return redirect('crisis_list')
    return render(request, 'crisis_confirm_delete.html', {'crisis': crisis})