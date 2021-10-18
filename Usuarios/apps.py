from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Usuarios'
    #para cambiar el nombre del administrador de usuario de django
    #verbose_name = 'Restaurante'