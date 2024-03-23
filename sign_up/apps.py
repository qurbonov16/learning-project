from django.apps import AppConfig


class SignUpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sign_up'

    def ready(self):
        import sign_up.signals