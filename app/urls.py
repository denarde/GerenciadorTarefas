from django.urls import path
from .views.tarefa_views import *
from .views.login_views import *
urlpatterns = [
    path('', login_usuario, name='Login_Usuario'),
    path('listar_tarefas/', listar_tarefas, name='Listar_Tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='Cadastrar_Tarefa'),
    path('alterar_tarefa/<int:id>', alterar_tarefa, name='Alterar_Tarefa'),
    path('deletar_tarefa/<int:id>', deletar_tarefa, name='Deletar_Tarefa'),
    path('cadastrar_usuario/', cadastrar_usuario, name='Cadastrar_Usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='Deslogar_Usuario'),
]
