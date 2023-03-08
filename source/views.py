from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
from django.db import connection
from .models import *
from .serializers import *

class LoginApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = { 
            'userName':request.GET.get('userName'),
            'password': request.GET.get('password'), 
            'designation': request.GET.get('designation')
        }
        success=False
        error_message=""
        if(data['designation']=='Admin'):
            admins = Admin.objects.raw("SELECT * FROM Admin WHERE admin_username= BINARY %s",[data['userName']])
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
            deos = Data_Entry_Operator.objects.raw("SELECT * FROM Data_Entry_Operator WHERE deo_username= BINARY %s",[data['userName']])
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
            doctors = Doctor.objects.raw("SELECT * FROM Doctor WHERE doctor_username= BINARY %s",[data['userName']])
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
            fdos = Front_Desk_Operator.objects.raw("SELECT * FROM Front_Desk_Operator WHERE fdo_username= BINARY %s",[data['userName']])
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

class ProfileView(APIView):
    def get(self,request,*args,**kwargs):
        success=False
        error_message=""
        if(kwargs['usertype']=='admin'):
            username=request.GET.get('username')
            with connection.cursor() as cursor:
                cursor.execute('SELECT admin_name,admin_address FROM Admin WHERE admin_username= BINARY %s',[username])
                row=cursor.fetchone()
                if row is None:
                    success=False
                    error_message="No such user found"
                    response={'success':success,'errorMessage':error_message}
                    return Response(response,status=status.HTTP_200_OK)
                name=row[0]
                address=row[1]
                success=True
                response={'success':success,'errorMessage':error_message,'username':username,'name':name,'address':address}
                return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['usertype']=='receptionist'):
            username=request.GET.get('username')
            with connection.cursor() as cursor:
                cursor.execute('SELECT fdo_name,fdo_address FROM Front_Desk_Operator WHERE fdo_username= BINARY %s',[username])
                row=cursor.fetchone()
                if row is None:
                    success=False
                    error_message="No such user found"
                    response={'success':success,'errorMessage':error_message}
                    return Response(response,status=status.HTTP_200_OK)
                name=row[0]
                address=row[1]
                success=True
                response={'success':success,'errorMessage':error_message,'username':username,'name':name,'address':address}
                return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['usertype']=='clerk'):
            username=request.GET.get('username')
            with connection.cursor() as cursor:
                cursor.execute('SELECT deo_name,deo_address FROM Data_Entry_Operator WHERE deo_username= BINARY %s',[username])
                row=cursor.fetchone()
                if row is None:
                    success=False
                    error_message="No such user found"
                    response={'success':success,'errorMessage':error_message}
                    return Response(response,status=status.HTTP_200_OK)
                name=row[0]
                address=row[1]
                success=True
                response={'success':success,'errorMessage':error_message,'username':username,'name':name,'address':address}
                return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['usertype']=='doctor'):
            username=request.GET.get('username')
            with connection.cursor() as cursor:
                cursor.execute('SELECT doctor_name,doctor_address,department FROM Doctor WHERE doctor_username= BINARY %s',[username])
                row=cursor.fetchone()
                if row is None:
                    success=False
                    error_message="No such user found"
                    response={'success':success,'errorMessage':error_message}
                    return Response(response,status=status.HTTP_200_OK)
                name=row[0]
                address=row[1]
                department=row[2]
                success=True
                response={'success':success,'errorMessage':error_message,'username':username,'name':name,'address':address,'department':department}
                return Response(response,status=status.HTTP_200_OK)
        
        else:
            success=False
            error_message="Wrong user type sent"
            response={'success':success,'errorMessage':error_message}


class Admin_Functions(APIView):
    def post(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(request.data.get('designation')=='Admin'):
            data = { 
                'admin_username': request.data.get('username'), 
                'admin_password': request.data.get('password'),
                'admin_name':request.data.get('name'),
                'admin_address':request.data.get('address')
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
                if(len(Admin.objects.raw('SELECT * FROM Admin WHERE admin_username= BINARY %s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Admin WHERE admin_username= BINARY %s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
            
        elif(designation=='Doctor'):
            with connection.cursor() as cursor:
                if(len(Doctor.objects.raw('SELECT * FROM Doctor WHERE doctor_username= BINARY %s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Doctor WHERE doctor_username= BINARY %s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
            
        elif(designation=='Clerk'):
            with connection.cursor() as cursor:
                if(len(Data_Entry_Operator.objects.raw('SELECT * FROM Data_Entry_Operator WHERE deo_username= BINARY %s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Data_Entry_Operator WHERE deo_username= BINARY %s", [request.GET.get('username')])
                    success=True
                    error_message="Successfully deleted user"
                else:
                    success=False
                    error_message="No such user found"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
        
        elif(designation=='Receptionist'):
            with connection.cursor() as cursor:
                if(len(Front_Desk_Operator.objects.raw('SELECT * FROM Front_Desk_Operator WHERE fdo_username= BINARY %s',[request.GET.get('username')]))>0):
                    cursor.execute("DELETE FROM Front_Desk_Operator WHERE fdo_username= BINARY %s", [request.GET.get('username')])
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
        
        elif(kwargs['method']=='admittances'):
            admittances=Admitted.objects.raw('SELECT * FROM Admitted WHERE currently_admitted=True')
            data=[]
            for admittance in admittances:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT patient_name FROM Patient WHERE patient_id=%s',[admittance.patient_id])
                    patient_name=cursor.fetchone()[0]
                    data.append([admittance.patient_id,patient_name,admittance.room_id])
            success=True
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['method']=='doctors'):
            doctors=Doctor.objects.raw('SELECT * FROM Doctor')
            data=[(doctor.doctor_username,doctor.doctor_name,doctor.department) for doctor in doctors]
            success=True
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)
        
        else:
            success=False
            error_message="Wrong request sent for Receptionist"
            data=[]
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
            
        
    def post(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(kwargs['method']=='register'):
            data = {
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
        
        elif(kwargs['method']=='scheduleappt'):
            data={
                'patient_id':request.data.get('patient_id'),
                'doctor_username':request.data.get('doctor_username'),
                'date':request.data.get('date'),
                'symptoms':request.data.get('symptoms'),
                'completed':False
            }
            if(len(Patient.objects.raw('SELECT * FROM Patient WHERE patient_id=%s',[data['patient_id']]))==0):
                success=False
                error_message="Patient does not exist"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
            
            current_appts=Appointment.objects.raw('SELECT * FROM Appointment WHERE doctor_username= BINARY %s AND date=%s',[data['doctor_username'],data['date']])
            if(len(current_appts)>=5):
                success=False
                error_message="Doctor is unavailable"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)
            else:
                serializer=AppointmentSerializer(data=data)
                if serializer.is_valid():
                    try:
                        serializer.save()
                    except:
                        success=False
                        error_message="Appointment already exists"
                        response={'success':success,'errorMessage':error_message}  
                        return Response(response, status=status.HTTP_200_OK)
                    success=True
                    response={'success':success,'errorMessage':error_message}  
                    return Response(response, status=status.HTTP_201_CREATED)
                else:
                    success=False
                    error_message="Wrong request sent for Receptionist"
                    response={'success':success,'errorMessage':error_message}  
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        elif(kwargs['method']=='discharge'):
            patients=Patient.objects.raw('SELECT * FROM Patient WHERE patient_id=%s',[request.data.get('patient_id')])
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
                admission=Admitted.objects.raw('SELECT * FROM Admitted WHERE patient_id=%s AND currently_admitted=True',[request.data.get('patient_id')])
                cursor.execute("UPDATE Admitted SET currently_admitted=False WHERE admission_id=%s", [admission[0].admission_id])
                cursor.execute("UPDATE Patient SET admitted=False WHERE patient_id=%s",[request.data.get('patient_id')])
                cursor.execute("UPDATE Room SET availability=True WHERE room_id=%s",[admission[0].room_id])
                success=True
                error_message="Successfully discharged patient"
                response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)

        else:
            success=False
            error_message="Wrong request sent for Receptionist"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)


class Clerk_Functions(APIView):
    def get(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(kwargs['method']=='tests'):
            tests=Test.objects.raw('SELECT * FROM Test WHERE saved_test=False')
            data=[]
            for test in tests:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT patient_name FROM Patient WHERE patient_id=%s',[test.patient_id])
                    patient_name=cursor.fetchone()[0]
                    cursor.execute('SELECT doctor_name FROM Doctor WHERE doctor_username= BINARY %s',[test.doctor_username])
                    doctor_name=cursor.fetchone()[0]
                    data.append([test.test_id,test.patient_id,patient_name,test.doctor_username,doctor_name,test.procedure_name])
            success=True
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['method']=='treatments'):
            treatments=Treatment.objects.raw('SELECT * FROM Treatment WHERE saved_treatment=False')
            data=[]
            for treatment in treatments:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT patient_name FROM Patient WHERE patient_id=%s',[treatment.patient_id])
                    patient_name=cursor.fetchone()[0]
                    cursor.execute('SELECT doctor_name FROM Doctor WHERE doctor_username= BINARY %s',[treatment.doctor_username])
                    doctor_name=cursor.fetchone()[0]
                    data.append([treatment.treatment_id,treatment.patient_id,patient_name,treatment.doctor_username,doctor_name,treatment.prescription])
            success=True
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['method']=='testresults'):
            tests=Test.objects.raw('SELECT * FROM Test WHERE saved_test=True AND saved_test_result=False')
            data=[]
            for test in tests:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT patient_name FROM Patient WHERE patient_id=%s',[test.patient_id])
                    patient_name=cursor.fetchone()[0]
                    cursor.execute('SELECT doctor_name FROM Doctor WHERE doctor_username= BINARY %s',[test.doctor_username])
                    doctor_name=cursor.fetchone()[0]
                    data.append([test.test_id,test.patient_id,patient_name,test.doctor_username,doctor_name,test.procedure_name])
            success=True
            response={'success':success,'errorMessage':error_message,'data':data}  
            return Response(response,status=status.HTTP_200_OK)

        else:
            success=False
            error_message="Wrong request sent for Clerk"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, *args, **kwargs):
        success=False
        error_message=""
        if(kwargs['method']=='savetests'):
            data={
                'date':request.data.get('date'),
                'test_id':request.data.get('test_id')
            }
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Test SET saved_test=True,date=%s WHERE test_id=%s",[data['date'],data['test_id']])
                success=True
                response={'success':success,'errorMessage':error_message}
                return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['method']=='savetreatments'):
            data={
                'date':request.data.get('date'),
                'treatment_id':request.data.get('treatment_id')
            }
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Treatment SET saved_treatment=True,date=%s WHERE treatment_id=%s",[data['date'],data['treatment_id']])
                success=True
                response={'success':success,'errorMessage':error_message}
                return Response(response,status=status.HTTP_200_OK)
        
        elif(kwargs['method']=='savetestresults'):
            data={
                'test_id':request.data.get('test_id'),
                'test_result':request.data.get('test_result'),
                'test_result_image':os.path.join(settings.MEDIA_ROOT,'test_result_images/',request.FILES['test_result_image'].name)
            }
            with open(data['test_result_image'], 'wb+') as destination:
                for chunk in request.FILES['test_result_image'].chunks():
                    destination.write(chunk)

            with connection.cursor() as cursor:
                if(cursor.execute("UPDATE Test SET saved_test_result=True,test_result=%s,test_result_image=%s WHERE test_id=%s",[data['test_result'],data['test_result_image'],data['test_id']])==0):
                    success=False
                    error_message="Unable to upload image"
                else:
                    success=True
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
            
        else:
            success=False
            error_message="Wrong request sent for Clerk"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

class Doctor_Functions(APIView):
    def get(self, request, *args, **kwargs):
        success=False
        error_message=""

        # Sending all patients
        # method = all_patients,
        # "doctor_username" from frontend

        if(kwargs['method']=='all_patients'):
            patients=Patient.objects.raw('SELECT * FROM Patient WHERE (EXISTS (SELECT * FROM Treatment WHERE Treatment.patient_id = Patient.patient_id AND Treatment.doctor_username = BINARY %s)) OR (EXISTS (SELECT * FROM Test WHERE Test.patient_id = Patient.patient_id AND Test.doctor_username = BINARY %s))', [request.GET.get('doctor_username'),request.GET.get('doctor_username')])
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
            
            treatments_data = Treatment.objects.raw('SELECT * FROM Treatment WHERE patient_id=%s AND doctor_username= BINARY %s', [request.GET.get('patient_id'),request.GET.get('doctor_username')])   
            treatments = [(row.treatment_id, row.prescription) for row in treatments_data]
            
            tests_data=Test.objects.raw('SELECT * FROM Test WHERE patient_id=%s AND doctor_username= BINARY %s', [request.GET.get('patient_id'),request.GET.get('doctor_username')])
            tests=[]
            for row in tests_data:
                test_result_image=None
                if(row.test_result_image is not None):
                    with open(row.test_result_image,'rb') as img:
                        test_result_image = img.read()
                    tests.append([row.test_id, row.procedure_name,row.test_result,test_result_image.decode('utf-8')])
                else:
                    tests.append([row.test_id, row.procedure_name,row.test_result,test_result_image])
            response={'success':success,'errorMessage':error_message,'patient_name':patient.patient_name,'patient_address':patient.patient_address,'admitted':patient.admitted,'room':room,'treatments':treatments,'tests':tests}
            return Response(response,status=status.HTTP_200_OK)
        
        # Sending all pending appointments to the doctor
        # method = all_appointments
        # "doctor_username" from frontend

        elif(kwargs['method']=='all_appointments'):
            appointments=Appointment.objects.raw('SELECT * FROM Appointment WHERE doctor_username= BINARY %s AND completed=False ORDER BY date ASC', [request.GET.get('doctor_username')])
            data=[(row.appointment_id,row.patient_id,row.date,row.symptoms) for row in appointments]
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

        if(kwargs['method']=='appointment'):
            dataTreatment = {
                'patient_id': request.data.get('patient_id'), 
                'doctor_username': request.data.get('doctor_username'),
                'prescription': request.data.get('prescription'),
                'appointment_id': request.data.get('appointment_id'),
                'saved_treatment': False
            }

            dataTest = {
                'patient_id': request.data.get('patient_id'), 
                'doctor_username': request.data.get('doctor_username'),
                'procedure_name': request.data.get('procedure_name'),
                'appointment_id': request.data.get('appointment_id'),
                'saved_test': False,
                'saved_test_result':False
            }
            serializerTreatment = TreatmentSerializer(data=dataTreatment)
            if not serializerTreatment.is_valid(): 
                success=False
                error_message="Unable to register treatment"
                response={'success':success,'errorMessage':error_message}
                return Response(response, status=status.HTTP_200_OK)

            serializer = TestSerializer(data=dataTest)
            if serializer.is_valid():
                if not dataTest['procedure_name'] is None:
                    serializer.save()
                if not dataTreatment['prescription'] is None:
                    serializerTreatment.save()
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
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
