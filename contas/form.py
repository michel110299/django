from django.forms import ModelForm
from .models import Transacoes , Categoria

class Transacoesform(ModelForm):
    class Meta:
        model = Transacoes
        fields = ['Data','Descricao','Valor','categoria','observacoes']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria

        fields = ['nome']
        