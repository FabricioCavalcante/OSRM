from django.forms import ModelForm
from app_osrm.models import InserirDados

class ListaForm(ModelForm):
    class Meta:
        model = InserirDados
        fields = ['nome', 'local', 'problema', 'placa_patrimonio']