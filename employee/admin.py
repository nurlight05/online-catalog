from django.contrib import admin
from .models import Employer

class EmployerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['supervisor']

admin.site.register(Employer, EmployerAdmin)
