from django import forms
from django.contrib.auth.models import User

class Registro(forms.Form):
    username = forms.CharField(required=True, min_length= 5 , max_length= 10, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : "Usuario"
    }))
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'Email'
    }))
    password  = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Contraseña'
    }))


    def clean_username(self):
        username= self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Usuario Existente')

        return username
    
    def clean_email(self):
        correo = self.cleaned_data.get('correo')
        if User.objects.filter(correo = correo).exists():
            raise forms.ValidationError('Correo Existente')
        return correo