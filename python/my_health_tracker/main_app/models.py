from django.db import models
import bcrypt  # USED FOR PASSWORD INCRYPTION
from datetime import datetime # USED FOR THE DATE ATTRIBUTES
import re   #USED FOR THE EMAIL VALIDATION - REGULAR EXPRESSIONS


class UserManager(models.Manager):   # MANAGES THE VALIDATION METHODS
    # REGISTRATION PAGE VALIDATOR
    def registration_validator(self, post_data):   
        errors = {}

        # VALIDATIONS FOR THE NAME DATA
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        first = str.isalpha(post_data['first_name'])
        if first == False :
            errors['first_name'] = "First name must contain letters only."
        last = str.isalpha(post_data['last_name'])
        if last == False :
            errors['last_name'] = "Last name must contain letters only."
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."

        # VALIDATIONS FOR THE EMAIL FIELD
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):              
            errors['email'] = "Email is invalid format. Please try again."
        else:
            user_list = User.objects.filter(email = post_data['email'])
            if len(user_list) > 0:
                errors['email'] = "Email address is already in use."

        # VALIDATIONS FOR THE PASSWORD FIELD
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords did not match."

        return errors
    
    # LOGIN PAGE VALIDATOR
    def login_validator(self, post_data):
        errors = {}

        user_list = User.objects.filter(email = post_data['email'])  # USES THE EMAIL TO BRING IN THE SPECIFIC USER OBJECT BECAUSE IS NOT YET AVAIABLE
        if len(user_list) > 0:
            user = user_list[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors['password'] = "Invalid Credentials. Please try again."
        else:
            errors['email'] = "Invalid Credentials. Please try again."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #emergency_contacts
    #doctors
    #appointments
    #pharmacies
    #medications
    #immunizations
    #allergies
    #stats
    objects = UserManager()    # LINKS THE MANAGER TO THE USER CLASS


class Emergency_contact(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    relationship = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="emergency_contacts", on_delete = models.CASCADE)


class Doctor(models.Model):
    dr_name = models.CharField(max_length=255)
    hospital_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="doctors", on_delete = models.CASCADE)


class Appointment(models.Model):
    appt_date = models.DateTimeField(auto_now=False)
    ordering = ['-appt_date']
    purpose = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, related_name="appointments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="appointments", on_delete = models.CASCADE)


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="pharmacies", on_delete = models.CASCADE)


class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    refill_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, related_name="medications", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="medications", on_delete = models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, related_name="medications", on_delete = models.CASCADE)
    

class Immunization(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False)
    renew_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, related_name="immunizations", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="immunizations", on_delete = models.CASCADE)


class Allergy(models.Model):
    name = models.CharField(max_length=255)
    symptom = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="allergies", on_delete = models.CASCADE)


class Stats(models.Model):
    weight = models.IntegerField()
    blood_type = models.CharField(max_length=5)
    blood_pressure = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="stats", on_delete = models.CASCADE)