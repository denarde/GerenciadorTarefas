from ..models import Tarefa

def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(nome=tarefa.nome,descricao=tarefa.descricao,prioridade=tarefa.prioridade, usuario=tarefa.usuario)

def listar_tarefas(usuario):
    return Tarefa.objects.filter(usuario=usuario).all()

def lista_tarefa_id(id):
    return Tarefa.objects.get(id=id)

def alterar_tarefa(tarefa, tarefa_nova):
    tarefa.nome = tarefa_nova.nome
    tarefa.descricao = tarefa_nova.descricao
    tarefa.prioridade = tarefa_nova.prioridade
    tarefa.save(force_update=True)

def deletar_tarefa(tarefa):
    tarefa.delete()