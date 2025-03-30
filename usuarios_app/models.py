from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Usuario(AbstractUser):
    """
    Modelo que representa a un usuario en la plataforma.

    Atributos:
        - rol (str): Define el rol del usuario en el sistema (menor, persona con depresión, psicólogo, admin).
        - anonimo (bool): Indica si el usuario desea permanecer anónimo.
        - groups (ManyToManyField): Relación con los grupos de Django.
        - user_permissions (ManyToManyField): Permisos personalizados del usuario.

    Hereda:
        AbstractUser: Utiliza el modelo de usuario de Django para autenticación.
    """
    ROLES = [
        ('menor', 'Menor afectado por bullying'),
        ('depresion', 'Persona con depresión'),
        ('psicologo', 'Psicólogo / Voluntario'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='menor')
    anonimo = models.BooleanField(default=True)  # Para menores que quieran anonimato

    # Evitar colisión con auth.User
    groups = models.ManyToManyField(Group, related_name="usuarios_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuarios_permissions", blank=True)
