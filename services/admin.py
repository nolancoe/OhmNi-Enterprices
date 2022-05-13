from django.contrib import admin
from .models import Appointment
from .models import Service


# Register your models here.
admin.site.register(Service)
admin.site.register(Appointment)

