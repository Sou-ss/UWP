from django import forms
from .models import Klient
class ClientsCreateForm(forms.Form):

    name           = forms.CharField()
    surname        = forms.CharField()



class KlientsCreateForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = [
            'name',
            'surname'
        ]


