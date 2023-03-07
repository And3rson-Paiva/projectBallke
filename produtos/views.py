from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from django.urls import reverse_lazy


class IndexView(ListView):
    models = Produto
    template_name = 'produtos.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'cadastro.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produtos')


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'cadastro.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produtos')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('produtos')







