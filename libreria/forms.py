from django import forms
from .models import Citas

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['id','nombre','apellido','correo','documento','fecha','hora','servicio']