from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db import connection
from .models import *
from .serializers import *

class LoginApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        # admins = Admin.objects.filter(admin_id=request.GET.get('admin_id'))
        data = { 
            'userName':request.GET.get('userName'),
            'password': request.GET.get('password'), 
            'designation': request.GET.get('designation')
        }
        print(data)
        # return Response(status=status.HTTP_200_OK)
        success=False
        error_message=""
        if(data['designation']=='Admin'):
            admins = Admin.objects.raw("SELECT * FROM Admin WHERE admin_username=%s",[data['userName']])
            if len(admins)>0:
                admin=admins[0]
                if(admin.admin_password==data['password']):
                    success=True
                else:
                    success=False
                    error_message="Incorrect password"
            else:
                success=False
                error_message="Incorrect username"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
        
        elif(data['designation']=='Clerk'):
            deos = Data_Entry_Operator.objects.raw("SELECT * FROM Data_Entry_Operator WHERE deo_username=%s",[data['userName']])
            if len(deos)>0:
                deo=deos[0]
                if(deo.deo_password==data['password']):
                    success=True
                else:
                    success=False
                    error_message="Incorrect password"
            else:
                success=False
                error_message="Incorrect username"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)

        elif(data['designation']=='Doctor'):
            doctors = Doctor.objects.raw("SELECT * FROM Doctor WHERE doctor_username=%s",[data['userName']])
            if len(doctors)>0:
                doctor=doctors[0]
                if(doctor.doctor_password==data['password']):
                    success=True
                else:
                    success=False
                    error_message="Incorrect password"
            else:
                success=False
                error_message="Incorrect username"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)

        elif(data['designation']=='Receptionist'):
            fdos = Front_Desk_Operator.objects.raw("SELECT * FROM Front_Desk_Operator WHERE fdo_username=%s",[data['userName']])
            if len(fdos)>0:
                fdo=fdos[0]
                if(fdo.fdo_password==data['password']):
                    success=True
                else:
                    success=False
                    error_message="Incorrect password"
            else:
                success=False
                error_message="Incorrect username"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
        else:
            success=False
            error_message="Other type of user entered"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
    # 2. Create
class Admin_Functions(APIView):
    def post(self, request, *args, **kwargs):
        # print("Request=",request)
        # print("args=",args)
        # print("kwargs=",kwargs)
        # print('method=',kwargs['method'])
        success=False
        error_message=""
        # if(kwargs['method']=='add'):
        if(request.data.get('designation')=='Admin'):
            data = { 
                'admin_username': request.data.get('username'), 
                'admin_password': request.data.get('password')
            }
            serializer = AdminSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                success=True  
                response={'success':success,'errorMessage':error_message}  
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="The username already exists"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
        
        elif(request.data.get('designation')=='Doctor'):
            data = { 
                'doctor_username': request.data.get('username'), 
                'doctor_password': request.data.get('password'),
                'doctor_name':request.data.get('name'),
                'doctor_address':request.data.get('address'),
                'department':request.data.get('department')
            }
            serializer = DoctorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                success=True  
                response={'success':success,'errorMessage':error_message}  
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="The username already exists"
                response={'success':success,'errorMessage':error_message}
        elif(request.data.get('designation')=='Clerk'):
            data = { 
                'deo_username': request.data.get('username'), 
                'deo_password': request.data.get('password'),
                'deo_name':request.data.get('name'),
                'deo_address':request.data.get('address')
            }
            serializer = Data_Entry_Operator_Serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                success=True  
                response={'success':success,'errorMessage':error_message}  
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="The username already exists"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
               
        elif(request.data.get('designation')=='Receptionist'):
            data = { 
                'fdo_username': request.data.get('username'), 
                'fdo_password': request.data.get('password'),
                'fdo_name':request.data.get('name'),
                'fdo_address':request.data.get('address')
            }
            serializer = Front_Desk_Operator_Serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                success=True  
                response={'success':success,'errorMessage':error_message}  
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="The username already exists"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
        else:
            success=False
            error_message="Other type of user entered"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        success=False
        error_message=""
        designation=request.GET.get('designation')
        if(designation=='Admin'):
            with connection.cursor() as cursor:
                print("username=",request.GET.get('username'))
                if(len(Admin.objects.raw('SELECT * FROM Admin WHERE admin_username=%s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Admin WHERE admin_username=%s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
            
        elif(designation=='Doctor'):
            with connection.cursor() as cursor:
                if(len(Doctor.objects.raw('SELECT * FROM Doctor WHERE doctor_username=%s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Doctor WHERE doctor_username=%s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
            
        elif(designation=='Clerk'):
            with connection.cursor() as cursor:
                if(len(Data_Entry_Operator.objects.raw('SELECT * FROM Data_Entry_Operator WHERE deo_username=%s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Data_Entry_Operator WHERE deo_username=%s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
        
        elif(designation=='Receptionist'):
            with connection.cursor() as cursor:
                if(len(Front_Desk_Operator.objects.raw('SELECT * FROM Front_Desk_Operator WHERE fdo_username=%s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Front_Desk_Operator WHERE fdo_username=%s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
        
        else:
            success=False
            error_message="Other type of user entered"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)

class Receptionist_Functions(APIView):
    def get(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(kwargs['method']=='rooms'):
            rooms=Room.objects.raw('SELECT * FROM Room')
            data=[(row.room_id,row.availability) for row in rooms]
            success=True
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)
        else:
            success=False
            error_message="Wrong request sent for Receptionist"
            data=[]
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(kwargs['method']=='register'):
            data = { 
                'patient_id':0,
                'patient_name': request.data.get('name'), 
                'patient_address': request.data.get('address'),
                'admitted':False
            }
            serializer = PatientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                success=True
                response={'success':success,'errorMessage':error_message}  
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="Unable to register patient"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
            
        elif(kwargs['method']=='admit'):
            data={
                'admission_id':0,
                'patient_id':request.data.get('patient_id'),
                'room_id':request.data.get('room_id'),
                'currently_admitted':False
            }
            if(len(Patient.objects.raw('SELECT * FROM Patient WHERE patient_id=%s',[data['patient_id']]))==0):
                success=False
                error_message="No such patient found"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
            
            if(len(Room.objects.raw('SELECT * FROM Room WHERE room_id=%s',[data['room_id']]))==0):
                success=False
                error_message="No such room found"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)

            patients = Patient.objects.raw('SELECT * FROM Patient WHERE patient_id=%s',[data['patient_id']])
            patient=patients[0]
            if(patient.admitted==True):
                success=False
                error_message="Patient already admitted"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
        
            rooms = Room.objects.raw('SELECT * FROM Room WHERE room_id=%s',[data['room_id']])
            room=rooms[0]
            if(room.availability==False):
                success=False
                error_message="Room already occupied"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
    
            data['currently_admitted']=True
            serializer = AdmittedSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE Patient SET admitted=True WHERE patient_id=%s", [data['patient_id']])
                    cursor.execute("UPDATE Room SET availability=False WHERE room_id=%s", [data['room_id']])
                    success=True  
                    response={'success':success,'errorMessage':error_message}  
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="Unable to admit patient"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
        
        else:
            success=False
            error_message="Wrong request sent for Receptionist"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
        
    def delete(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(kwargs['method']=='discharge'):
            patients=Patient.objects.raw('SELECT * FROM Patient WHERE patient_id=%s',[request.GET.get('patient_id')])
            if(len(patients)==0):
                success=False
                error_message="No such patient found"
                response={'success':success,'errorMessage':error_message}
                return Response(response,status=status.HTTP_200_OK)

            patient=patients[0]
            if(patient.admitted==False):
                success=False
                error_message="Patient not admitted"
                response={'success':success,'errorMessage':error_message}
                return Response(response,status=status.HTTP_200_OK)
            
            with connection.cursor() as cursor:
                admission=Admitted.objects.raw('SELECT * FROM Admitted WHERE patient_id=%s AND currently_admitted=True',[request.GET.get('patient_id')])
                cursor.execute("UPDATE Admitted SET currently_admitted=False WHERE admission_id=%s", [admission[0].admission_id])
                cursor.execute("UPDATE Patient SET admitted=False WHERE patient_id=%s",[request.GET.get('patient_id')])
                cursor.execute("UPDATE Room SET availability=True WHERE room_id=%s",[admission[0].room_id])
                success=True
                error_message="Successfully discharged patient"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)

        else:
            success=False
            error_message="Wrong request sent for Receptionist"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)

class Doctor_Functions(APIView):
    def get(self, request, *args, **kwargs):
        success=False
        error_message=""

        # Sending all patients
        # method = all_patients,
        # "doctor_username" from frontend

        if(kwargs['method']=='all_patients'):
            patients=Patient.objects.raw('SELECT * FROM Patient WHERE EXISTS (SELECT * FROM Treatment WHERE Treatment.patient_id = Patient.patient_id AND Treatment.doctor_username = %s)', [request.GET.get('doctor_username')])
            data=[(row.patient_id,row.patient_name) for row in patients]
            success=True
            error_message=""
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)

        # Sending specific patient
        # method = patient
        # "patient_id" and "doctor_username" from frontend

        elif(kwargs['method']=='patient'):
            patients = Patient.objects.raw('SELECT * FROM Patient WHERE patient_id=%s',[request.GET.get('patient_id')])
            if(len(patients) == 0):
                success=False
                error_message="No such patient found"
                response={'success':success,'errorMessage':error_message}
                return Response(response,status=status.HTTP_200_OK)
            success=True
            error_message=""
            patient=patients[0]
            room="NA"
            rooms = Admitted.objects.raw('SELECT * from Admitted WHERE patient_id=%s AND currently_admitted=True',[request.GET.get('patient_id')])
            if(len(rooms) > 0):
                room = rooms[0].room_id
            treatments_data = Treatment.objects.raw('SELECT * FROM Treatment WHERE patient_id=%s AND doctor_username=%s', [request.GET.get('patient_id'),request.GET.get('doctor_username')])   
            treatments = [(row.treatment_id, row.prescription) for row in treatments_data]
            response={'success':success,'errorMessage':error_message,'patient_name':patient.patient_name,'patient_address':patient.patient_address,'admitted':patient.admitted,'room':room,'treatments':treatments}
            return Response(response,status=status.HTTP_200_OK)
        
        # Sending all pending appointments to the doctor
        # method = all_appointments
        # "doctor_username" from frontend

        elif(kwargs['method']=='all_appointments'):
            appointments=Appointment.objects.raw('SELECT * FROM Appointment WHERE doctor_username=%s AND completed=False', [request.GET.get('doctor_username')])
            data=[(row.appointment_id,row.patient_id,row.date) for row in appointments]
            success=True
            error_message=""
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)

        else:
            success=False
            error_message="Wrong request sent for Doctor"
            data=[]
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        success=False
        error_message=""

        # "appointment_id", "patient_id", "doctor_username", "prescription", "procedure_name" from frontend
        # considered procedure_name as string of procedures

        if(kwargs['method']=='appointment'):
            dataTreatment = {
                'treatment_id':0,
                'patient_id': request.data.get('patient_id'), 
                'doctor_username': request.data.get('doctor_username'),
                'prescription': request.data.get('prescription'),
                'appointment_id': request.data.get('appointment_id'),
                'saved_treatment': False
            }

            dataTest = {
                'test_id': 0,
                'patient_id': request.data.get('patient_id'), 
                'doctor_username': request.data.get('doctor_username'),
                'procedure_name': request.data.get('procedure_name'),
                'appointment_id': request.data.get('appointment_id'),
                'saved_test': False
            }

            serializerTreatment = TreatmentSerializer(data=dataTreatment)
            if serializerTreatment.is_valid():
                serializerTreatment.save()
            else:
                success=False
                error_message="Unable to register treatment"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
            
            serializer = TestSerializer(data=dataTest)
            if serializer.is_valid():
                serializer.save()
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE Appointment SET completed=True WHERE appointment_id=%s", [request.data.get('appointment_id')])
                    success=True
                    response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                success=False
                error_message="Unable to register test"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)

        else:
            success=False
            error_message="Wrong request sent for Doctor"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)