from django.conf import settings
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Service, Appointment
from store.utils import cookieCart, cartData, guestOrder
# Import User Model From Django
from account.models import Account
from .forms import AppointmentForm, AppointmentFormAdmin
from django.http import HttpResponse
import csv
from django.contrib import messages

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Import Pagination Stuff
from django.core.paginator import Paginator
DEBUG = False

def life_coach_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/life_coach.html", context)

def death_coach_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/death_coach.html", context)

def qi_gong_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/qi_gong.html", context)

def rune_reading_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/rune_reading.html", context)

def hypnotherapy_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/hypnotherapy.html", context)

def grief_work_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/grief_work.html", context)

def end_of_life_care_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "services/end_of_life_care.html", context)


# Show Appointment
def show_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    return render(request, 'services/show_appointment.html', {
            "appointment":appointment
            })



# Create Admin appointment Approval Page
def admin_approval(request):
    # Get Counts
    appointment_count = Appointment.objects.all().count()
    user_count = Account.objects.all().count()

    appointment_list = Appointment.objects.all().order_by('-appointment_date')
    if request.user.is_superuser:
        if request.method == "POST":
            # Get list of checked box id's
            id_list = request.POST.getlist('boxes')

            # Uncheck all appointments
            appointment_list.update(approved=False)

            # Update the database
            for x in id_list:
                Appointment.objects.filter(pk=int(x)).update(approved=True)

            # Show Success Message and Redirect
            messages.success(request, ("Appointment List Approval Has Been Updated!"))
            return redirect('list-appointments')



        else:
            return render(request, 'services/admin_approval.html',
                {"appointment_list": appointment_list,
                "appointment_count":appointment_count,
                "user_count":user_count,})
    else:
        messages.success(request, ("You aren't authorized to view this page!"))
        return redirect('home')


    return render(request, 'services/admin_approval.html')


# Create My Appointments Page
def my_appointments(request):
    if request.user.is_authenticated:
        me = request.user.id
        appointments = Appointment.objects.all()
        return render(request,
            'services/my_appointments.html', {
                "appointments":appointments,

            })


# Cancel an Appointment
def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.user == appointment.client:
        appointment.delete()
        messages.success(request, ("Appointment Canceled!!"))
        return redirect('list-appointments')
    else:
        if request.user.is_superuser:
            appointment.delete()
            messages.success(request, ("Appointment Canceled!!"))
            return redirect('list-appointments')
        else:
            messages.success(request, ("You Aren't Authorized To Delete This Appointment!"))
            return redirect('list-appointments')

def book_appointment(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = AppointmentFormAdmin(request.POST)
            if form.is_valid():
                    form.save()
                    return  HttpResponseRedirect('/book_appointment?submitted=True')
        else:
            form = AppointmentForm(request.POST)
            if form.is_valid():
                #form.save()
                appointment = form.save(commit=False)
                appointment.client = request.user # logged in user
                appointment.save()
                return  HttpResponseRedirect('/book_appointment?submitted=True')
    else:
        # Just Going To The Page, Not Submitting
        if request.user.is_superuser:
            form = AppointmentFormAdmin
        else:
            form = AppointmentForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'services/book_appointment.html', {'form':form, 'submitted':submitted})

def all_appointments(request):
    appointment_list = Appointment.objects.all().order_by('-appointment_date')
    me = request.user.id
    appointments = Appointment.objects.filter(client=me)
    if request.user.is_superuser:
            return render(request, 'services/appointment_list.html',
                {'appointment_list': appointment_list})
    else:
        return render(request,
            'services/my_appointments.html', {
                "appointments":appointments,

            })
