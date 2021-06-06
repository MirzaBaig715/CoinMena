import os
from django.apps import AppConfig


class CryptoMetricsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto_metrics'

    def ready(self):
        from crypto_metrics import jobs
        if os.environ.get('RUN_MAIN', None) != 'true':
            # RUN_MAIN check is because python manage.py runs the ready method twice. once in each of two processes
            # https://stackoverflow.com/questions/33814615/how-to-avoid-appconfig-ready-method-running-twice-in-django
            jobs.start_scheduler()
