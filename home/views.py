from django.shortcuts import render
from department.models import Department
from specialish.models import Specialish
# Create your views here.


def index(request):
    department = Department.objects.all()
    specialish = Specialish.objects.all()
    context = {
        'department':department,
        'specialish':specialish
    }
    return render(request,'home/index.html',context)