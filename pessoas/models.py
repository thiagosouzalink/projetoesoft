from django.db import models


class Pessoa(models.Model):

    nome = models.CharField('Nome', max_length=150)
    idade = models.IntegerField('Idade')
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField('E-mail')
    apelido = models.CharField('Apelido', max_length=50, blank=True)
    observacao = models.TextField('Observação', max_length=150, blank=True)
    
    def __str__(self):
        return self.nome

