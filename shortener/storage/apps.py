from django.apps import AppConfig
from django.conf import settings


class StorageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storage'

    def ready(self):
        print("* initializing *")
        from .url_storage import Storage
        settings.URL_STORAGE = Storage()

