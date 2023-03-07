from django.urls import path
from .views import IndexView, postagem

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('postagem', postagem, name='postagem'),
]
