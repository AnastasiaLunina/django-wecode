from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # adding event listeners to follow deleteing and creating of accounts
    def ready(self):
        import users.signals
