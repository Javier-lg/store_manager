from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserCreateSerializer
from rest_framework.permissions import IsAdminUser


# Create your views here.

class UserCreateView(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(f'Usuario creado exitosamente como{user.role}',status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
