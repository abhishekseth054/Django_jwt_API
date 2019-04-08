from django.shortcuts import render

from .models import Employee
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from employee.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
