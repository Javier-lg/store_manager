from django.contrib.auth.models import BaseUserManager
from django.urls import reverse

class UserManager(BaseUserManager):
    '''
    Manager de usuario
    '''
    '''
    Devuelve usuarios no eliminados
    '''
    def all(self):
        users = self.filter(deleted_at=None)
        return users
    
    
    def get_employee(self,pk):
        '''
        Devuelve un empleado
        '''
        employee = self.get(pk=pk, role='Empleado',is_staff=False,is_superuser=False)
        return employe
       
    
    def get_employees(self):
        '''
        Devuelve los empleados
        '''
        employees = self.filter(role='Empleado',is_staff=False,is_superuser=False)
        return employees
    
    def get_admins(self):
        '''
        Devuelve administadores
        '''
        admins = self.filter(role='Administrador',is_staff=False,is_superuser=False)
        return admins
    
    def _create_user(self, first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields):
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            role= role,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, first_name, last_name, username, email, password, **extra_fields): # Para Empleados
        is_staff = False
        is_superuser = False
        role = 'Empleado'
        return self._create_user(first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields)

    def create_superuser(self, first_name, last_name, username, email, password, **extra_fields): # Para Admin desarrollador
        is_staff = True
        is_superuser = True
        role = 'Administrador'
        return self._create_user(first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields)
    
    def create_admin(self, first_name, last_name, username, email, password, **extra_fields): # Para Admin de negocio
        is_staff = True
        is_superuser = False
        role = 'Administrador'
        return self._create_user(first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields)