from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework import viewsets

from .serializers import EmployerSerializer
from .models import Employer

def loginUser(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('index-list')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index-list')
        else:
            messages.error(request, 'Username or Password does not exist!') 
            
    context = {
        'page': page
    }
    return render(request, 'employee/login_register.html', context)

def registerUser(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index-list')
        else:
            messages.error(request, 'An error occured during registration!')
    
    context = {
        'form': form
    }
    
    return render(request, 'employee/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index-list')

class IndexListView(ListView):
    template_name = 'employee/index.html'
    model = Employer
    paginate_by = 100
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(name__icontains=query) | 
                                                    Q(position__icontains=query) | 
                                                    Q(hired__contains=query) | 
                                                    Q(salary__contains=query) |
                                                    Q(supervisor__name__icontains=query))
        else:
            object_list = self.model.objects.all()
        return object_list

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