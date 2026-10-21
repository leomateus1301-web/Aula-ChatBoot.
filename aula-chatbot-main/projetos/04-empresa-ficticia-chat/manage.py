# Ponto de entrada para os comandos administrativos do Django.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empresa_ficticia_project.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
