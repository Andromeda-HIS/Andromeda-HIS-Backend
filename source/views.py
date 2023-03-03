from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import AdminSerializer

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
            admins = Admin.objects.filter(admin_username=data['userName'])
            if admins.exists():
                admin=admins.first()
                if(getattr(admin,'admin_password')==data['password']):
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
            deos = Data_Entry_Operator.objects.filter(deo_username=data['userName'])
            if deos.exists():
                deo=deos.first()
                if(getattr(deo,'deo_password')==data['password']):
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
            doctors = Doctor.objects.filter(doctor_username=data['userName'])
            if doctors.exists():
                doctor=doctors.first()
                if(getattr(doctor,'doctor_password')==data['password']):
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
            fdos = Front_Desk_Operator.objects.filter(fdo_username=data['userName'])
            if fdos.exists():
                fdo=fdos.first()
                if(getattr(fdo,'fdo_password')==data['password']):
                    success=True
                else:
                    success=False
                    error_message="Incorrect password"
            else:
                success=False
                error_message="Incorrect username"
            response={'success':success,'errorMessage':error_message}
            return Response(response,status=status.HTTP_200_OK)
    
        return Response("Other type entered", status=status.HTTP_400_BAD_REQUEST)
    # 2. Create
    def post(self, request, *args, **kwargs):
        data = { 
            'admin_username': request.data.get('admin_username'), 
            'admin_password': request.data.get('admin_password')
        }
        serializer = AdminSerializer(data=data)
        if serializer.is_valid():
            if not Admin.objects.filter(admin_username=data['admin_username']).exists():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Username already exists", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)