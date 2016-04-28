from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):
    name = 'imager_profile'

    def ready(self):
        """Let app know about handlers when run."""
        from imager_profile import handlers
