from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets

from .serializers import EmployerSerializer
from .models import Employer

class IndexListView(ListView):
    template_name = 'employee/index.html'
    model = Employer
    paginate_by = 100

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployeeDetailView(DetailView):
    model = Employer
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employer = self.object
        
        breadcrumb = [employer]
        while employer.supervisor:
            breadcrumb.insert(0, employer.supervisor)
            employer = employer.supervisor
        context['breadcrumb'] = breadcrumb
        
        return context
    
class EmployeesListView(ListView):
    def get_queryset(self):
        self.employer = get_object_or_404(Employer, id=self.kwargs['pk'])
        return Employer.objects.filter(supervisor=self.employer)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supervisor'] = self.employer
        
        employer = self.employer
        breadcrumb = [employer]
        while employer.supervisor:
            breadcrumb.insert(0, employer.supervisor)
            employer = employer.supervisor
        context['breadcrumb'] = breadcrumb
        
        return context