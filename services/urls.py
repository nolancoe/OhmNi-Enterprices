from django.urls import path
from . import views

urlpatterns = [

    path('book_appointment', views.book_appointment, name='book-appointment'),
    path('cancel_appointment/<appointment_id>', views.cancel_appointment, name='cancel-appointment'),
    path('my_appointments', views.my_appointments, name='my_appointments'),
    path('admin_approval', views.admin_approval, name='admin_approval'),
    path('show_appointment/<appointment_id>', views.show_appointment, name='show-appointment'),
    path('appointments', views.all_appointments, name="list-appointments"),
]
