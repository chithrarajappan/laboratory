from django.db import models

# Create your models here.
class PatientRegistartion(models.Model):

    Patient_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Age = models.IntegerField()
    DateofBirth = models.DateField()
    BloodGroup = models.CharField(max_length=100)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=100)
    ResidencyAddress = models.CharField(max_length=100)
    MedicalHistory = models.CharField(max_length=100)


class TechnicianRegistration(models.Model):
    Technician_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    DateofBirth = models.DateField()
    Age = models.IntegerField()
    BloodGroup = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=100)


class Logins(models.Model):
    Email = models.EmailField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)







