from django.forms import ModelForm
from contas.models import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao','valor','categoria','observacao']
