from django import forms
from .models import Blog


class PostagemModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'conteudo', 'autor', 'data_publicacao']

