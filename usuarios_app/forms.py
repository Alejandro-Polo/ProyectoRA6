from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario de registro para nuevos usuarios.

    Campos:
        - username (str): Nombre de usuario único.
        - email (str): Dirección de correo electrónico.
        - password1 (str): Contraseña del usuario.
        - password2 (str): Confirmación de la contraseña.
        - rol (str): Rol del usuario dentro de la plataforma.

    Hereda:
        UserCreationForm: Proporciona validación y manejo de contraseñas.
    """
    rol = forms.ChoiceField(choices=Usuario.ROLES)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rol']
