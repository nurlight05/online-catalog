from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Employer

# Serialize with default serializer + Recursive relation representation
# class EmployerSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     position = serializers.ChoiceField(choices=Employer.POSITION_CHOICES)
#     hired = serializers.DateField()
#     salary = serializers.DecimalField(max_digits=10, decimal_places=2)
#     supervisor = serializers.ListField(child=RecursiveField())

# Serialize employers from bottom to top
class EmployerSerializer(serializers.ModelSerializer):
    supervisor = serializers.SerializerMethodField()
    
    class Meta:
        model = Employer
        fields = ('name', 'position', 'hired', 'salary', 'supervisor')
        
    def get_supervisor(self, obj):
        if obj.supervisor is not None:
            # return obj.supervisor.id
            return EmployerSerializer(obj.supervisor).data
        else:
            return None
       
# Serialize 1 level employees 
# class EmployeeSerializer(serializers.ModelSerializer):
#     supervisor = serializers.PrimaryKeyRelatedField(queryset=Employer.objects.all(), source='supervisor.id')
    
#     class Meta:
#         model = Employer
#         fields = ('name', 'position', 'hired', 'salary', 'supervisor')
        
# class EmployerSerializer(serializers.ModelSerializer):
#     employees = EmployeeSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Employer
#         fields = ('name', 'position', 'hired', 'salary', 'employees')
