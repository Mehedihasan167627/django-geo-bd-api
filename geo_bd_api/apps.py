from django.apps import AppConfig


class GeoBdApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geo_bd_api'
    def ready(self):
        import geo_bd_api.signals
