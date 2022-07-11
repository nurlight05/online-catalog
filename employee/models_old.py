from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomEmployerManager(BaseUserManager):
    def create_user(self, email, username, password, name, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user        

class Employer(AbstractBaseUser):
    CEO = 'CEO'
    DIRECTOR = 'DIR'
    MANAGER = 'MGR'
    TEAMLEAD = 'TML'
    DEVELOPER = 'DVP'
    
    POSITION_CHOICES = [
        (CEO, 'Ceo'),
        (DIRECTOR, 'Director'),
        (MANAGER, 'Manager'),
        (TEAMLEAD, 'Teamlead'),
        (DEVELOPER, 'Developer'),
    ]
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        default=DEVELOPER,
    )
    hired = models.DateField(default=timezone.now)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    supervisor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.name
    
    def is_supervisor(self):
        return self.position in {self.CEO, self.DIRECTOR, self.MANAGER, self.TEAMLEAD}