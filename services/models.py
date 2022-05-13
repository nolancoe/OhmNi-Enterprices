from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date
from django.conf import settings
from appointment_time.models import appointment_time



class Service(models.Model):
    service = models.CharField(max_length=50)

    def __str__(self):
        return str(self.service)


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    appointment_date = models.DateField('Appointment Date')
    appointment_time = models.ForeignKey(appointment_time, on_delete=models.CASCADE, blank=True, null=True)
    #venue = models.CharField(max_length=120)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return str(self.client)+ ', ' + str(self.client.email)+ ', ' + str(self.service)+ ', ' + str(self.appointment_date) + ', ' + str(self.appointment_time)


    @property
    def Days_till(self):
        today = date.today()
        days_till = self.appointment_date - today
        if self.appointment_date == today:
            days_till_stripped = "Today"
        else:
            days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped

    @property
    def Is_Past(self):
        today = date.today()
        if self.appointment_date < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing
