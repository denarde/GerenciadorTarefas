from urllib import request

from django.shortcuts import render, redirect
from ..forms import TarefaForm
from ..entidades.tarefa import Tarefa
from ..services import tarefa_db
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def listar_tarefas(request):
    tarefas = tarefa_db.listar_tarefas(request.user)
    return render(request, 'tarefa/lista_tarefas.html', {'tarefas': tarefas})

@login_required()
def cadastrar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            prioridade = form.cleaned_data['prioridade']
            tarefa = Tarefa(nome=nome,descricao=descricao,prioridade=prioridade,usuario=request.user)
            tarefa_db.cadastrar_tarefa(tarefa)
            return redirect('Listar_Tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefa/cadastrar_tarefa.html', {'TarefaForm': form})

@login_required()
def alterar_tarefa(request, id):
    tarefa = tarefa_db.lista_tarefa_id(id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        prioridade = form.cleaned_data['prioridade']
        tarefa_nova = Tarefa(nome=nome, descricao=descricao, prioridade=prioridade,usuario=request.user)
        tarefa_db.alterar_tarefa(tarefa, tarefa_nova)
        return redirect('Listar_Tarefas')

    return render(request, 'tarefa/cadastrar_tarefa.html', {'TarefaForm': form})

@login_required()
def deletar_tarefa(request, id):
    tarefa = tarefa_db.lista_tarefa_id(id)
    tarefa_db.deletar_tarefa(tarefa)
    return redirect('Listar_Tarefas')