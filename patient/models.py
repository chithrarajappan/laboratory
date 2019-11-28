from django.db import models
from admins.models import PatientRegistartion
from admins.models import TechnicianRegistration
from admins.models import Logins


# Create your models here.

# class Patient_Report(models.Model):
#     Patient = models.ForeignKey(PatientRegistartion, on_delete=models.CASCADE, )
#     LabName = models.CharField(max_length=100)
#     DateTime = models.DateTimeField()
#     Patient_Name = models.CharField(max_length=100)
#     Age = models.IntegerField()
#     Gender = models.CharField(max_length=100)
#     Specimen_Collected = models.CharField(max_length=100)
#     Doctor_Consulted = models.CharField(max_length=100)
#     Test_Name = models.CharField(max_length=100)
#     Test = models.CharField(max_length=100)
#     Result = models.CharField(max_length=100)
#     Units = models.CharField(max_length=100)
#     Reference_range = models.CharField(max_length=100)
class Appointment(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)

