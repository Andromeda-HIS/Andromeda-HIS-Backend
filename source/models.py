from django.db import models
from datetime import date

class Admin(models.Model):
    admin_username=models.CharField(max_length=100,primary_key=True)
    admin_password=models.TextField()
    class Meta:
        db_table='Admin'

class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    patient_name=models.TextField()
    patient_address=models.TextField()
    admitted=models.BooleanField()
    class Meta:
        db_table='Patient'

class Room(models.Model):
    room_id=models.AutoField(primary_key=True)
    availability=models.BooleanField()
    class Meta:
        db_table='Room'

class Doctor(models.Model):
    doctor_username=models.CharField(max_length=100,primary_key=True)
    doctor_password=models.TextField()
    doctor_name=models.TextField()
    doctor_address=models.TextField()
    department=models.TextField()
    class Meta:
        db_table='Doctor'

class Front_Desk_Operator(models.Model):
    fdo_username=models.CharField(max_length=100,primary_key=True)
    fdo_password=models.TextField()
    fdo_name=models.TextField()
    fdo_address=models.TextField()
    registered_num=models.IntegerField()
    admitted_num=models.IntegerField()
    discharged_num=models.IntegerField()
    class Meta:
        db_table='Front_Desk_Operator'

class Data_Entry_Operator(models.Model):
    deo_username=models.CharField(max_length=100,primary_key=True)
    deo_password=models.TextField()
    deo_name=models.TextField()
    deo_address=models.TextField()
    tests_scheduled=models.IntegerField()
    treatments_scheduled=models.IntegerField()
    class Meta:
        db_table='Data_Entry_Operator'

class Admitted(models.Model):
    admission_id=models.AutoField(primary_key=True)
    patient_id=models.IntegerField()
    room_id=models.IntegerField()
    currently_admitted=models.BooleanField()
    class Meta:
        db_table='Admitted'

class Appointment(models.Model):
    appointment_id=models.AutoField(primary_key=True)
    patient_id=models.IntegerField()
    doctor_id=models.IntegerField()
    date=models.DateField()
    class Meta:
        db_table='Appointment'
        constraints=[
            models.UniqueConstraint(fields=['patient_id','doctor_id','date'],name='appointment_pk')
        ]

class Procedure(models.Model):
    procedure_id=models.AutoField(primary_key=True)
    procedure_name=models.TextField()
    cost=models.IntegerField()
    class Meta:
        db_table='Procedure'

class Treatment(models.Model):
    treatment_id=models.AutoField(primary_key=True)
    patient_id=models.IntegerField()
    doctor_id=models.IntegerField()
    procedure_id=models.IntegerField()
    class Meta:
        db_table='Treatment'


