from django.urls import path
from . import views

urlpatterns = [
    path('resources/<int:crisis_id>/', views.resource_list, name='resource_list'),    path('resources/create/', views.resource_create, name='resource_create'),
    path('resources/update/<int:pk>/', views.resource_update, name='resource_update'),
    path('resources/delete/<int:pk>/', views.resource_delete, name='resource_delete'),

    path('donations/', views.donation_list, name='donation_list'),
    path('donations/create/', views.donation_create, name='donation_create'),
    path('donations/update/<int:pk>/', views.donation_update, name='donation_update'),
    path('donations/delete/<int:pk>/', views.donation_delete, name='donation_delete'),

    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('volunteers/create/', views.volunteer_create, name='volunteer_create'),
    path('volunteers/update/<int:pk>/', views.volunteer_update, name='volunteer_update'),
    path('volunteers/delete/<int:pk>/', views.volunteer_delete, name='volunteer_delete'),

    path('crisis/<int:crisis_id>/report/', views.crisis_report, name='crisis_report'),
    path('crisis_list/', views.crisis_list, name='crisis_list'),
]
