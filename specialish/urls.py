from django.urls import path
from . import views



app_name = 'specialish'


urlpatterns = [
    path('',views.SpecialishTemplateView.as_view(),name='index'),

]