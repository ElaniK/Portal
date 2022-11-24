import django

django.setup()

from django.apps import AppConfig

from . import signals


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals
