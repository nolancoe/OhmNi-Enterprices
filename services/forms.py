from django import forms
from django.forms import ModelForm
from .models import Appointment, Service
from appointment_time.models import appointment_time

# Admin SuperUser Event Form
class AppointmentFormAdmin(ModelForm):
    class Meta:
        model = Appointment
        fields = ('service', 'appointment_date', 'appointment_time', 'client')
        labels = {
            'service': 'Service',
            'appointment_date': 'YYYY-MM-DD',
            'appointment_time': 'appointment_time',
            'client': 'Client',
        }
        widgets = {
            'service': forms.Select(attrs={'class':'form-select', 'placeholder':'Service'}),
            'appointment_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.Select(attrs={'class':'form-select', 'placeholder':'Appointment Time'}),
            'client': forms.Select(attrs={'class':'form-select', 'placeholder':'Client'}),
        }


# User Event Form
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('service', 'appointment_date', 'appointment_time')
        labels = {
            'service': 'Service',
            'appointment_date': 'Appointment Date',
            'appointment_time': 'Appointment Time',
        }
        widgets = {
            'service': forms.Select(attrs={'class':'form-select', 'placeholder':'Service'}),
            'appointment_date': forms.widgets.DateInput(attrs={'type': 'date', 'placeholder':'Appointment Date'}),
            'appointment_time': forms.Select(attrs={'class':'form-select', 'placeholder':'Appointment Time'}),
        }
