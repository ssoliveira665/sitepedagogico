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
#**********************************************************************************************************

class InscricaoSearchForm(forms.Form):
    nome_candidato = forms.CharField(required=False, label='Nome do Candidato', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(required=False, label='CPF', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_inicio = forms.DateField(required=False, label='Data Início', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    data_fim = forms.DateField(required=False, label='Data Fim', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    status = forms.ChoiceField(required=False, choices=[('', 'Todos'), ('Ativo', 'Ativo'), ('Inativo', 'Inativo')], widget=forms.Select(attrs={'class': 'form-control'}))
#**********************************************************************************************************

class InscricaoFilterForm(forms.Form):
    nome_candidato = forms.CharField(required=False, label="Nome do Candidato")
    cpf = forms.CharField(required=False, label="CPF")
    status = forms.ChoiceField(
        required=False,
        choices=[('aprovado', 'Aprovado'), ('pendente', 'Pendente')],
        label="Status da Inscrição"
    )
    data_inicio = forms.DateField(required=False, label="Data de Início", widget=forms.TextInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(required=False, label="Data de Fim", widget=forms.TextInput(attrs={'type': 'date'}))


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['disciplinas_aprovadas', 'status', 'nota_prova', 'prova_realizada']  # Liste todos os campos que você deseja no formulário