from django.db import models

# Create your models here.class Service(models.Model):
class appointment_time(models.Model):
    appointment_time = models.CharField(max_length=15)

    def __str__(self):
        return str(self.appointment_time)

