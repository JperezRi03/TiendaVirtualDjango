from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import DireccionEnvio


class DireccionEnvioForm(ModelForm):
     class Meta: 
               model = DireccionEnvio
               fields = [
                    'line1', 'line2' , 'city' , 'state', 'coutry', 'reference', 'postal_code'
               ]  

               labels = {
                      'line1':'calle1',
                      'line2':'calle2',
                      'city':'Ciudad',
                      'state':'Estado',
                      'coutry':'Pais',
                      'reference':'casa',
                      'postal_code':'CodigoP',
                    }


     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

          self.fields['line1'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': 'Calle'
          })

          self.fields['line2'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': '###'
          })

          self.fields['city'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': 'Ciudad'
          })

          self.fields['state'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': 'Estado'
          })

          self.fields['coutry'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': 'Pais'
          })

          self.fields['reference'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': 'Apto, Conjunto ... etc '
          })

          self.fields['postal_code'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': '760'
          })