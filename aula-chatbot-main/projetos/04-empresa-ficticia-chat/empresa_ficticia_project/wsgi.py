"""Entrada WSGI para servidores compatíveis."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empresa_ficticia_project.settings")
application = get_wsgi_application()
