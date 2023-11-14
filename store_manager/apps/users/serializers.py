from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=('Administrador','Empleado'))
    
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','role')
        
    def create(self,validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        
        if role == 'Administrador':
            user = User.objects.create_admin(password=password, **validated_data)
        else:
            user = user = User.objects.create_user(password=password, **validated_data)
        return user
    