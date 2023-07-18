from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News_Portal'

    def ready(self):
        from . import signals
class News_Portal(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News_Portal'

    def ready(self):
        from . import signals  # выполнение модуля -> регистрация сигналов

