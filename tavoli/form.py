from django import forms
from .models import Tavoli

class TavoliForm(forms.ModelForm):

    class Meta:
        model = Tavoli
        fields = ('nome_Tavolo',)