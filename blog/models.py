from django.db import models


class Blog(models.Model):
    titulo = models.CharField('Título', max_length=200)
    conteudo = models.TextField('Conteudo')
    autor = models.CharField('Autor', max_length=200)
    data_publicacao = models.DateField('Data de Publicação')

    def __str__(self):
        return f'{self.titulo} - {self.autor}'


