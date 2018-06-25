# This Python file uses the following encoding: utf-8
from django import forms
from django.forms import TextInput,EmailInput,Select,HiddenInput
from .models import Cliente
choicestxt=(('Madera','Madera'),('Poliestireno','Poliestireno'))
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'direccion', 'email', 'telefono', 'celular', 'empresa', 'ejecutivo','usuario']
        labels = {
            'nombre' : 'Nombre(s)*',
            'apellidos' : 'Apellidos*',
            'direccion' : 'Dirección',
            'email' : 'Correo Electrónico*',
            'telefono' : 'Teléfono*',
            'celular' : 'Celular',
            'sexo' : 'Sexo*',
            'empresa' : 'Empresa*',
            'ejecutivo' : 'Ejecutivo',
            'usuario' : 'Usuario*',
            }
        widgets = {
            'nombre': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'nombre_completo',
                                    'name': 'nombre_completo',
                                    'placeholder':'Nombre(s)'
                                    }),
            'apellidos': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'apellidos',
                                    'name': 'apellidos',
                                    'placeholder':'Apellidos'
                                    }),
            'direccion': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'direccion',
                                    'name': 'direccion',
                                    'placeholder':'Dirección'
                                    }),
            'email': EmailInput(attrs={
                                    'class':'form-control',
                                    'id': 'email',
                                    'name': 'email',
                                    'placeholder':'Correo Electrónico'
                                    }),
            'telefono': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'telefono',
                                    'name': 'telefono',
                                    'placeholder':'(55) 5555-5555'
                                    }),
            'celular': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'celular',
                                    'name': 'celular',
                                    'placeholder':'+ 52 (55) 5555-5555'
                                    }),
            'empresa': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'empresa',
                                    'name': 'empresa',
                                    'placeholder':'Empresa'
                                    }),
            'ejecutivo': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'ejecutivo',
                                    'name': 'ejecutivo',
                                    'placeholder':'Empresa'
                                    }),
            'usuario': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'usuario',
                                    'name': 'usuario',
                                    'style': 'visibility:hidden',

                                    }),
                                    }
