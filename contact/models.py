from django.db import models

# Create your models here.


class PatientAreSay(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    date    = models.DateField(auto_now=True)
    message = models.TextField()


    def __str__(self):
        return self.name


class HospitalEmail(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email



class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=600)
    message = models.TextField()


    def __str__(self):
        return self.name

