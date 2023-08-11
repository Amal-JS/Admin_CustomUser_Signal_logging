from django.apps import AppConfig


class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_app'

    #we are registering our signal here then only it will work

    def ready(self):
        import admin_app.signal
