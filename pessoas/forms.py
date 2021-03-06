from django import forms

from .models import Pessoa


class PessoaForm(forms.ModelForm):
    """Campos do formulário"""
    
    nome = forms.CharField(
        label='Nome'
    )
    sobrenome = forms.CharField(
        label='Sobrenome'
    )
    idade = forms.IntegerField()
    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    email = forms.EmailField()
    apelido=forms.CharField(required=False)
    observacao = forms.CharField(
        label='Observação',
        widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = Pessoa
        fields = '__all__'

    # Salvar dados no BD
    def save(self, commit=True):
        pessoa = super().save(commit=False)
        pessoa.nome = self.cleaned_data['nome']
        pessoa.nome += ' ' + self.cleaned_data['sobrenome']
        pessoa.idade = self.cleaned_data['idade']
        pessoa.data_nascimento = self.cleaned_data['data_nascimento']
        pessoa.email = self.cleaned_data['email']
        pessoa.apelido = self.cleaned_data['apelido']
        pessoa.observacao = self.cleaned_data['observacao']
        if commit:
            pessoa.save()
        return pessoa