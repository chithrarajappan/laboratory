from django.db import models
from admins.models import PatientRegistartion
from admins.models import TechnicianRegistration
# from admins.models import Logins


# Create your models here.
class AddTestResult(models.Model):
    DateTime = models.DateTimeField()
    Technician_id = models.IntegerField()
    Patient_ID = models.IntegerField()
    Patient_Name = models.CharField(max_length=100)
    Test_Name = models.CharField(max_length=100)
    Result = models.CharField(max_length=100)
    Units = models.CharField(max_length=100)
    Reference_range = models.CharField(max_length=100)
    Doctor_Consulted = models.CharField(max_length=100)



class BloodTest(models.Model):
    Patient_ID = models.IntegerField()
    Test = models.CharField(max_length=100)
    Result = models.CharField(max_length=100)
    Units = models.CharField(max_length=100)
    Reference_range = models.CharField(max_length=100)

class UricAcidTest(models.Model):
    Patient_ID = models.IntegerField()
    Test = models.CharField(max_length=100)
    Result = models.CharField(max_length=100)
    Units = models.CharField(max_length=100)
    Reference_range = models.CharField(max_length=100)

class DiabetesTest(models.Model):
    Patient_ID = models.IntegerField()
    Test = models.CharField(max_length=100)
    Result = models.CharField(max_length=100)
    Units = models.CharField(max_length=100)
    Reference_range = models.CharField(max_length=100)

class CholestrolTest(models.Model):
    Patient_ID = models.IntegerField()
    Test = models.CharField(max_length=100)
    Result = models.CharField(max_length=100)
    Units = models.CharField(max_length=100)
    Reference_range = models.CharField(max_length=100)













