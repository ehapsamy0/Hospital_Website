from django.shortcuts import render
from .models import Department
# Create your views here.


def index(request):
    departments = Department.objects.all()
    context = {
        'departments':departments
    }
    return render(request,'department/departments.html',context)