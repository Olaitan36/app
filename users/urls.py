from django.urls import path, include
from . import views

urlpatterns = [
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/new/', views.resource_create, name='resource_create'),
    path('resources/<int:pk>/edit/', views.resource_update, name='resource_update'),
    path('resources/<int:pk>/delete/', views.resource_delete, name='resource_delete'),

    path('donations/', views.donation_list, name='donation_list'),
    path('donations/new/', views.donation_create, name='donation_create'),
    path('donations/<int:pk>/edit/', views.donation_update, name='donation_update'),
    path('donations/<int:pk>/delete/', views.donation_delete, name='donation_delete'),

    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('volunteers/new/', views.volunteer_create, name='volunteer_create'),
    path('volunteers/<int:pk>/edit/', views.volunteer_update, name='volunteer_update'),
    path('volunteers/<int:pk>/delete/', views.volunteer_delete, name='volunteer_delete'),

    path('crisis/<int:crisis_id>/report/', views.crisis_report, name='crisis_report'),
    path('crises/', views.crisis_list, name='crisis_list'),  # Added crisis_list
]
