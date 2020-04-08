from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Specialish
# Create your views here.


class SpecialishTemplateView(TemplateView):
    template_name = 'doctors/doctors.html'

    def get_context_data(self, *args,**kwargs):
        context = super(SpecialishTemplateView,self).get_context_data(*args,**kwargs)
        specialishs = Specialish.objects.all()
        context['specialishs'] = specialishs
        return context


