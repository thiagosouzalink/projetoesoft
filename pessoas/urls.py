from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('editar_pessoa/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('detalhe_pessoa/<int:id>/', views.detalhe_pessoa, name='detalhe_pessoa')
]