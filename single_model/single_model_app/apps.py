from django.apps import AppConfig


class SingleModelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'single_model_app'
