from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def login_usuario(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request,username=username,password=password)

        if usuario is not None:
            login(request,user=usuario)
            return redirect('Listar_Tarefas')
        else :
            messages.error(request, 'Usuario/Senha invalidos. Favor validar')
            print(request.user.is_authenticated)
    elif request.user.is_authenticated:
        return redirect('Listar_Tarefas')

    user_form = AuthenticationForm()
    return render(request, 'login/login.html', {'user_form' : user_form})

def cadastrar_usuario(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('Login_Usuario')
    else:
        user_form = UserCreationForm()

    return render(request, 'login/cadastro_usuario.html', {'user_form' : user_form})

@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('Login_Usuario')