from django.db import models

# Create your models here.

class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def str(self):
        return f'{self.primeiro_nome} {self.sobrenome}'


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    duracao_minutos = models.IntegerField()
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.titulo


class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    criador = models.CharField(max_length=50)
    data_estreia = models.DateField()
    numero_temporadas = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.titulo