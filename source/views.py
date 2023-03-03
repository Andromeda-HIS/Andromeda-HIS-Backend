from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Admin
from .serializers import AdminSerializer

class AdminApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        admins = Admin.objects.filter(admin_id=request.GET.get('admin_id'))
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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