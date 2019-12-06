from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class FormCasa(forms.ModelForm):
    class Meta:
        model = casa
        fields = ('ancho', 'largo', 'precio', 'habitaciones','jardin','disponibilidad')
        widgets = {
            'ancho': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'largo': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'precio': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'habitaciones': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'jardin': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'disponibilidad': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'ancho': _('Ancho de la casa(m.)'),
            'largo': _('Largo de la casa(m.)'),
            'precio': _('Precio'),
            'habitaciones': _('Habitaciones'),
            'jardin': _('Disponibilidad de Jardin'),
            'disponibilidad': _('Disponibilidad'),
        }

class FormDepa(forms.ModelForm):
    class Meta:
        model = departameto
        fields = ('ancho', 'largo', 'precio', 'habitaciones','piso','disponibilidad')
        widgets = {
            'ancho': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'largo': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'precio': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'habitaciones': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'piso': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'disponibilidad': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'ancho': _('Ancho del departamento(m.)'),
            'largo': _('Largo del departamento(m.)'),
            'precio': _('Precio'),
            'habitaciones': _('Habitaciones'),
            'piso': _('Numero de piso en el que se encuentra el departamento'),
            'disponibilidad': _('Disponibilidad'),
        }
