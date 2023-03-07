from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ordering = ('nome', 'descricao', 'preco')
    list_display = ('nome', 'descricao', 'preco')

