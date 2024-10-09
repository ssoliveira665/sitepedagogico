from django import forms
from .models import Candidato
from django.contrib.auth.forms import AuthenticationForm
from .models import Inscricao

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = [
            'nome', 'email', 'cpf', 'data_nascimento', 'maior_de_18', 'nome_responsavel',
            'tipo_responsavel', 'telefone', 'telefone_2', 'endereco', 'bairro', 'ponto_referencia',
            'possui_necessidade_especial', 'necessidade_especial', 'turno_disponivel', 'etapa_pretendida'
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
            'telefone_2': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
        }
#**********************************************************************************************************

class CPFLoginForm(AuthenticationForm):
    username = forms.CharField(label="CPF", max_length=11)

    def __init__(self, *args, **kwargs):
        super(CPFLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Digite seu CPF',
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Digite sua senha',
            'class': 'form-control'
        })


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['prova_todas_disciplinas_sim', 'prova_todas_disciplinas_nao', 'disciplinas']