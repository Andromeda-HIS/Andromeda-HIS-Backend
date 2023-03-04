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
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
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
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
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
                'deo_address':request.data.get('address'),
                'tests_scheduled':request.data.get('tests_scheduled'),
                'treatments_scheduled':request.data.get('treatments_scheduled')
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
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
               
        elif(request.data.get('designation')=='Receptionist'):
            data = { 
                'fdo_username': request.data.get('username'), 
                'fdo_password': request.data.get('password'),
                'fdo_name':request.data.get('name'),
                'fdo_address':request.data.get('address'),
                'registered_num':request.data.get('registered_num'),
                'admitted_num':request.data.get('admitted_num'),
                'discharged_num':request.data.get('discharged_num')
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
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            success=False
            error_message="Other type of user entered"
            response={'success':success,'errorMessage':error_message}
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
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
            return Response(status=status.HTTP_400_BAD_REQUEST)