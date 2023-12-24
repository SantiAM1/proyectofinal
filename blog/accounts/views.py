from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, CustomUserCreation, UserEdition
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == "POST":
        formulario = CustomUserCreation(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            return redirect("pages:pagelist") 
    else:
        form = CustomUserCreation()
        return render(request, "accounts/signup.html", {"form" : form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('pages:plataforma')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Cierre de sesión exitoso.')
    return redirect('pages:pagelist')

@login_required
def user_edit(request):
    usuario = request.user
    if request.method == "GET":
        
        valores_iniciales = {
            "email" : usuario.email,
            "first_name" : usuario.first_name,
            "last_name" : usuario.last_name,
        }
        form = UserEdition(initial=valores_iniciales)
        return render(request,
        "accounts/editarperfil.html",
        context={"usuario":usuario,"form":form})
    
    else:
        form = UserEdition(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect("pages:plataforma")