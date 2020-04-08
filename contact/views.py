from django.shortcuts import render,redirect
from .models import PatientAreSay,HospitalEmail,Contact
from django.http import HttpResponseRedirect
# Create your views here.


def patient_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        message = request.POST.get('message')
        new_patient = PatientAreSay.objects.create(name=name,email=email,date=date,message=message)
        new_patient.save()
    return HttpResponseRedirect('home:index')



def email_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_email = HospitalEmail.objects.create(email=email)
        new_email.save()
    return redirect('home:index')



def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_contact = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        new_contact.save()
        return redirect('contact:index')
    else:
        return render(request,'contact/contact.html')


