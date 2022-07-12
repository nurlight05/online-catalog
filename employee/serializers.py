from dataclasses import fields
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Employer

# Serialize employees & employers from bottom to top
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('name', 'position', 'hired', 'salary', 'supervisor', 'employees') # You can remove 'employees' or 'supervisor' field
        depth = 4
        
class EmployerToJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('name', 'position', 'hired', 'salary', 'supervisor')
