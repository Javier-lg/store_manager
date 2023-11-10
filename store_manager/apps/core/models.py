from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from validators import *

# Create your models here.

class Person(models.Model):
    '''
    Modelo base para personas
    '''
    first_name = models.CharField(max_length=50,validators=[validate_only_letters('invalid_name')])
    last_name = models.CharField(max_length=50,db_index=True,validators=[validate_only_letters('invalid_last_name')])
    phone_number = PhoneNumberField(blank=True)
    dni = models.CharField(max_length=20,validators=[validate_dni])
    birth_date = models.DateField(null=True,blank=True,db_index=True)
    address = models.CharField(max_length=120)
    
    
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    deleted_at = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        abstract = True
        
    def get_full_name(self) -> str:
        return f'{self.last_name}, {self.first_name}'
    
    def __str__(self) -> str:
        return f'{self.get_full_name}' - {self.dni} - {self.address} - {self.phone_number}
    
    
    
    '''
    Funciones para soft y hard delete
    '''
    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()
        
    def hard_delete(self):
        super().delete()
    
    
class BaseAbstractWithUser(models.Model):
    '''
    Modelo para identificar usuario que realiza 
    una accion sobre otros modelos
    '''
    user_made = models.ForeignKey('user.User', on_delete=models.PROTECT,null=True,blank=True)
    
    class Meta:
        abstract = True
        
    def __str__(self) -> str:
        return f'Por: {self.user_made}'