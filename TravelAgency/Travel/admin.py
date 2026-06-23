from django.contrib import admin
from .models import Package, Booking, ContactMessage

admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(ContactMessage)
