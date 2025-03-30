import os
import sys
import django

# Agregar la ruta del proyecto para que Sphinx pueda encontrar los módulos
sys.path.insert(0, os.path.abspath('..'))

# Configurar Django para importar modulos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RefugioDigital.settings')
django.setup()

# -- Project information -----------------------------------------------------
project = 'RA6Documentacion'
copyright = '2025, AlejandroPOloBArranco'
author = 'AlejandroPOloBArranco'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Extrae docstrings automáticamente
    'sphinx.ext.napoleon',     # Permite usar docstrings en estilo Google o NumPy
    'sphinx.ext.viewcode',     # Agrega enlaces al código fuente
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Opciones para autodoc ---------------------------------------------------
autodoc_default_options = {
    'members': True,           # Documentar todos los métodos y atributos
    'undoc-members': True,     # Incluir miembros sin docstring
    'private-members': False,  # No documentar miembros privados (con _nombre)
    'show-inheritance': True,  # Mostrar herencia de clases
}

# -- Opciones para HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
