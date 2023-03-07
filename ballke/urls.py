from django.contrib import admin
from django.urls import path, include
from produtos.views import ProdutoUpdateView, DeleteProdutoView, CreateProdutoView
from rest_framework import routers
from produtos.api.viewsets import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
    path("produtos/", include('produtos.urls')),
    path('cadastro', CreateProdutoView.as_view(), name='add_produto'),
    path('update/<int:pk>/', ProdutoUpdateView.as_view(), name='upd_produto'),
    path('delete/<int:pk>/', DeleteProdutoView.as_view(), name='del_produto'),
]
