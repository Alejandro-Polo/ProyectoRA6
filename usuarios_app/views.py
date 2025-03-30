from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm


def registro(request):
    """
    Maneja el registro de nuevos usuarios.

    Si la solicitud es POST, se procesa el formulario y se registra el usuario.
    Si es GET, se muestra el formulario de registro.

    Parámetros:
        - request (HttpRequest): La solicitud HTTP enviada por el usuario.

    Retorna:
        - HttpResponse: Renderiza la página de registro o redirige al foro.
    """
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("foro")
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})

def login_view(request):
    """
    Maneja el inicio de sesión de los usuarios.

    Si la solicitud es POST, valida los datos y autentica al usuario.
    Si es GET, muestra el formulario de inicio de sesión.

    Parámetros:
        - request (HttpRequest): La solicitud HTTP enviada por el usuario.

    Retorna:
        - HttpResponse: Renderiza la página de login o redirige al foro.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('foro')  
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    """
    Cierra la sesión del usuario y lo redirige a la página de inicio de sesión.

    Parámetros:
        - request (HttpRequest): La solicitud HTTP enviada por el usuario.

    Retorna:
        - HttpResponse: Redirige a la vista de login.
    """
    logout(request)
    return redirect(login_view)


#Provisional
def inicio_view(request):
    return render(request, 'usuarios/inicio.html')

