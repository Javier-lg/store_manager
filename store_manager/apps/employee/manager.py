from django.contrib.auth.models import BaseUserManager

class EmployeeManager(BaseUserManager):
    def do_some(self):
        return true    