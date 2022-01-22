from django import forms 
from .models import Ware 
class WareCreationForm(forms.ModelForm):
    class Meta:
        model = Ware 
        fields = ["user", "name", "location", "telephone_number", ]