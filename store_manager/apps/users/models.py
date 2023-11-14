from django.db import models
from apps.core.models import Person

from django.contrib.auth.models import AbstractUser
from apps.users.manager import UserManager

# Create your models here.

class User(Person,AbstractUser):
    '''
    Clse para usuario del sistema
    '''
    ROLE = [
        ('ADMINISTRADOR','ADMINISTRADOR'),
        ('EMPLEADO','EMPLEADO')
    ]

    objects = UserManager()
    role = models.CharField(max_length=15, choices=ROLE, default='EMPLEADO', null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    
    
    
    def __str__(self):
        return f"{self.get_full_name()} | {self.email or 'Sin email'} | {self.role}"