from django.urls import path, include
from . import views

urlpatterns = [
    path('resources/', views.resource_list, name='resource_list'),  # List all resources
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),  # View a specific resource
    path('resource/create/', views.resource_create, name='resource_create'),  # Create a new resource
    path('resource/<int:resource_id>/update/', views.resource_update, name='resource_update'),  # Update a resource
    path('resource/<int:resource_id>/delete/', views.resource_delete, name='resource_delete'),  # Delete a resource

    path('donations/', views.donation_list, name='donation_list'),  # List all donations
    path('donation/<int:donation_id>/', views.donation_detail, name='donation_detail'),  # View a specific donation
    path('donation/create/', views.donation_create, name='donation_create'),  # Create a new donation
    path('donation/<int:donation_id>/update/', views.donation_update, name='donation_update'),  # Update a donation
    path('donation/<int:donation_id>/delete/', views.donation_delete, name='donation_delete'),  # Delete a donation

    path('volunteers/', views.volunteer_list, name='volunteer_list'),  # List all volunteers
    path('volunteer/<int:volunteer_id>/', views.volunteer_detail, name='volunteer_detail'),  # View a specific volunteer
    path('volunteer/create/', views.volunteer_create, name='volunteer_create'),  # Create a new volunteer
    path('volunteer/<int:volunteer_id>/update/', views.volunteer_update, name='volunteer_update'),  # Update a volunteer
    path('volunteer/<int:volunteer_id>/delete/', views.volunteer_delete, name='volunteer_delete'),  # Delete a volunteer

    path('crises/', views.crisis_list, name='crisis_list'),  # List all crises
    path('crisis/<int:crisis_id>/', views.crisis_detail, name='crisis_detail'),  # View a specific crisis
    path('crisis/create/', views.crisis_create, name='crisis_create'),  # Create a new crisis
    path('crisis/<int:crisis_id>/update/', views.crisis_update, name='crisis_update'),  # Update a crisis
    path('crisis/<int:crisis_id>/delete/', views.crisis_delete, name='crisis_delete'),  # Delete a crisis

]
