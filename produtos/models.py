from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=1000)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome} - {self.descricao} - {self.preco}'


