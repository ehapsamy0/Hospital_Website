from django.urls import path
from . import views

app_name = 'contact'


urlpatterns = [
    path('',views.contact_page,name='index'),
    path('patient/',views.patient_form,name='patient_form'),
    path('emails/',views.email_form,name='emails'),


]