from django.urls import path
from . import views

urlpatterns = [
    path('',views.inmobiliaria, name='inmobiliaria'),
]
