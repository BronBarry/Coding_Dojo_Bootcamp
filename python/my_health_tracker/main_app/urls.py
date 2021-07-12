from django.urls import path
from . import views
urlpatterns = [
    # Displays the registration, Login page
    path('', views.index),
    # Adds the registration form into the DB and redirects to the dashboard page
    path('register', views.register),
    # Adds the login form into the session and redirects to the dashboard page
    path('login', views.login),
    # Displays the dashboard page
    path('dashboard', views.dashboard),
    # Destroys the session, logs out, and redirects to the forms page
    path('logout', views.logout),

    # CRUD APPOINTMENTS
    
    #READ the first Appointments page
    path('appointment', views.appointment),
    #READ the Appointments details
    path('appointment/<int:appt_id>', views.appointment_details),
    #CREATE appointment
    path('appointment/new', views.appointment_add),
    #UPDATE appointment
    path('appointment/<int:appt_id>/update', views.appointment_update),
    #DELETE appointment
    path('appointment/<int:appt_id>/delete', views.appointment_delete),

    # CRUD DOCTORS

    #READ the first Doctor page
    path('doctor', views.doctor),
    #READ the Doctor details
    path('doctor/<int:dr_id>', views.doctor_details),
    #CREATE doctor
    path('doctor/new', views.doctor_add),
    #UPDATE doctor
    path('doctor/<int:dr_id>/update', views.doctor_update),
    #DELETE doctor
    path('doctor/<int:dr_id>/delete', views.doctor_delete),
    
    # CRUD PROFILE
    path('profile', views.profile),

    # CRUD HEALTH PAGE

    path('health', views.health),

    # CRUD RESOURCES

    path('resources', views.resources),

]