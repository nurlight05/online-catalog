from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployerViewSet)

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index-list'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/employees/', views.EmployeesListView.as_view(), name='employees-list'),
    path('employees/', include(router.urls)),
]

