from django.db import models
from django.utils import timezone

class Employer(models.Model):
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
    
    name = models.CharField(max_length=150)
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        default=DEVELOPER,
    )
    hired = models.DateField(default=timezone.now)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    supervisor = models.ForeignKey('self', null=True, related_name='employees', on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    def is_supervisor(self):
        return self.position in {self.CEO, self.DIRECTOR, self.MANAGER, self.TEAMLEAD}
    
    def get_position(self):
        return self.get_position_display()