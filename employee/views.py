from django.http import HttpResponse
from django.shortcuts import render
from .models import Employer

def main(request):
    employee = Employer.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'employee/index.html', context)