from django.contrib import admin

from .models import User, Crisis, Resource, Donation, Volunteer

admin.site.register(User)
admin.site.register(Crisis)
admin.site.register(Resource)
admin.site.register(Donation)
admin.site.register(Volunteer)
