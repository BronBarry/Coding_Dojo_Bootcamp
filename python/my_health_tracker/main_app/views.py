import bcrypt       # IMPORT BCRYPT FOR PASSWORD ENCRYPTION
from django.shortcuts import render, redirect
from .models import *

from django.contrib import messages  # IMPORT MESSAGES FOR THE FORM VALIDATION ERRORS

def index(request):    # DISPLAYS REGISTER LOGIN FORMs with error messages - if user already logged in send to /success
    if "id" in request.session:
        return redirect("/dashboard")
    return render(request, 'index.html') 

def register(request): # ADDS THE REGISTER FORM DATA into the DB and redirects to the dashboard page
    print('THIS IS THE REGISTER METHOD')
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/")
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_pw
        )
        request.session['id'] = new_user.id   # ADDS NEW USER INTO SESSION

    return redirect('/dashboard')

def login(request):  # ADDS THE LOGIN FORM DATA into the session and redirects to the dashboard page
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['id'] = user.id  # ADDS LOGIN USER INTO SESSION

    return redirect('/dashboard')

def dashboard(request): # DISPLAYS THE dashboard PAGE WITH OUR USERNAME 
    if "id" not in request.session:
        return redirect("/")

    context = {
        "logged_in_user" : User.objects.get(id=request.session['id']),   #ADDS USER SESSION OBJECT
    }
    return render(request, "dashboard.html", context)

def logout(request): # DELETES THE SESSION OBJECT, logs out, and redirects to the forms page
    del request.session['id']

    return redirect('/')

########################## APPOINTMENTS SECTION

#Display appt page
def appointment(request):
    context = {
        "logged_in_user" : User.objects.get(id=request.session['id']),
    }
    user = User.objects.get(id=request.session['id'])
    print(user.doctors.all())
    return render(request, 'appointments.html', context)

#Adds new Appt
def appointment_add(request):
    print(request.POST)
    logged_in_user = User.objects.get(id=request.session['id']) 
    doctor_to_add = Doctor.objects.get(id=request.POST['doctor'])
    print(doctor_to_add)
    new_appt = Appointment.objects.create(appt_date=request.POST['appt_date'], purpose = request.POST['purpose'], question = request.POST['question'], doctor = doctor_to_add, user = logged_in_user)

    print(logged_in_user.doctors.all())

    print("PRINTING", request.POST['doctor'])

    return redirect('/appointment')

def appointment_details(request, appt_id):
    context = {
        "logged_in_user" : User.objects.get(id=request.session['id']),
        "appointment" : Appointment.objects.get(id=appt_id),
    }

def appointment_update(request, appt_id):
    pass

def appointment_delete(request, appt_id):
    pass


########################## DOCTOR SECTION

def doctor(request):
    pass

def doctor_details(request, dr_id):
    pass

def doctor_add(request):
    print('Logged in USER ID: ', request.session['id'])
    print(request.POST)    
    logged_in_user = User.objects.get(id=request.session['id']) 

    new_dr = Doctor.objects.create(dr_name = request.POST['dr_name'], hospital_name = request.POST['hospital_name'], address = request.POST['address'], phone = request.POST['phone'], user = logged_in_user)

    # logged_in_user.doctors.add(new_dr)
    print(new_dr)
    return redirect('/appointment')

def doctor_update(request, dr_id):
    pass

def doctor_delete(request, dr_id):
    pass



###################### PROFILE PAGE

def profile(request):
    context = {
        "logged_in_user" : User.objects.get(id=request.session['id']),
    }
    logged_in_user = User.objects.get(id=request.session['id'])
    return render(request, "profile.html", context)

######################## HEALTH PAGE

def health(request):
    context = {
        "logged_in_user" : User.objects.get(id=request.session['id']),
    }
    return render(request, "health.html", context)

####################### RESOURCE

def resources(request):
    context = {
        "logged_in_user" : User.objects.get(id=request.session['id']),
    }
    return render(request, "resources.html", context)
