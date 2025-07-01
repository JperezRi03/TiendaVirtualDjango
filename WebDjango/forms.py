from django import forms
from django.contrib.auth.models import User

class Registro(forms.Form):
    username = forms.CharField(required=True, min_length= 5 , max_length= 10, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : "Usuario"
    }))
    correo= forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'Email'
    }))
    password= forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Contraseña'
    }))

    password2 = forms.CharField(required=True, label='Confirmar Contraseña' , widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Confirmar Contraseña'
    }))

    def clean_username(self):
        username= self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Usuario Existente')
        return username
    
    def clean_correo(self):
        correo= self.cleaned_data.get('correo')
        print(correo)
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('Correo Existente')
        return correo

    def clean(self): # type: ignore
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password') :
            self.add_error('password2' , 'Las contraseñas no coinciden')
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'), # type: ignore
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )
