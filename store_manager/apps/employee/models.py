from django.db import models
from apps.users.models import User
from .manager import EmployeeManager

# Create your models here.

class Job(models.Model):
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description

class Employee(models.Model):
    '''
    Modelo para Empleados
        -Usa el soft delete heredado de persona
        -Puede ser cambiado de rol (diseñar la manera de manejar este asunto)
    '''
    
    objects = EmployeeManager()
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,related_name='user',verbose_name='Empleado')
    user_made = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True,related_name='employeer',verbose_name='Empleador')
    hire_date = models.DateField(verbose_name='Fecha de contratacion')
    job = models.ForeignKey(Job,on_delete=models.CASCADE,verbose_name="Puesto",null=True,blank=True)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        
    def __str__(self) -> str:
        return f'{self.user}'