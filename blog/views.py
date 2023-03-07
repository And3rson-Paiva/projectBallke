from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Blog
from .forms import PostagemModelForm
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['postagem'] = Blog.objects.all()

        return context


def postagem(request):
    if str(request.method) == 'POST':
        form = PostagemModelForm(request.POST)
        if form.is_valid():

            form.save()

            messages.success(request, 'Postagem salva com sucesso')
            form = PostagemModelForm()
        else:
            messages.error(request, 'Erro ao salvar a postagem')
    else:
        form = PostagemModelForm()
    context = {
        'form': form
    }
    return render(request, 'postagem.html', context)

