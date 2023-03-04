from rest_framework import serializers
from .models import *

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=['admin_username','admin_password']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['doctor_username','doctor_password','doctor_name','doctor_address','department']

class Data_Entry_Operator_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Data_Entry_Operator
        fields=['deo_username','deo_password','deo_name','deo_address']

class Front_Desk_Operator_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Front_Desk_Operator
        fields=['fdo_username','fdo_password','fdo_name','fdo_address']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['patient_id','patient_name','patient_address','admitted']
    
class AdmittedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admitted
        fields=['admission_id','patient_id','room_id','currently_admitted']