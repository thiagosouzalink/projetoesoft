import requests
from django.shortcuts import render, redirect

from .models import Pessoa
from .forms import PessoaForm


def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/index.html', {'pessoas': pessoas})

def cadastrar_pessoa(request):
    if request.method == "POST":
        form_pessoa = PessoaForm(request.POST)
        if form_pessoa.is_valid():
            form_pessoa.save()
            return redirect('index')
    else:       
        form_pessoa = PessoaForm()
        lista_nome = get_nome()
        form_pessoa.fields['nome'].widget.attrs['value'] = lista_nome[0]
        form_pessoa.fields['sobrenome'].widget.attrs['value'] = lista_nome[1]
    return render(request, 'pessoas/pessoa_form.html', {'form_pessoa': form_pessoa})

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    lista_nome = pessoa.nome.split()
    nome = lista_nome.pop(0)
    sobrenome = ""
    while lista_nome:
        sobrenome +=" " + lista_nome.pop(0)
    pessoa.nome = nome
    pessoa.data_nascimento = pessoa.data_nascimento.strftime('%Y-%m-%d')
    
    if request.method == "POST":
        form_pessoa = PessoaForm(request.POST, instance=pessoa)
        if form_pessoa.is_valid():
            form_pessoa.save()
            return redirect('index')
    else:
        form_pessoa = PessoaForm(instance=pessoa)
        form_pessoa.fields['sobrenome'].widget.attrs['value'] = sobrenome 
    return render(request, 'pessoas/pessoa_form.html', {'form_pessoa': form_pessoa})

def detalhe_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'pessoas/detalhe_pessoa.html', {'pessoa': pessoa})

def get_nome():
    r = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    lista_nome = r.json()
    nome = lista_nome[0]
    sobrenome = f'{lista_nome[1]} {lista_nome[2]}'
    return [nome, sobrenome]

