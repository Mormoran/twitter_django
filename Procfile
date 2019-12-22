web: gunicorn twitter_django.wsgi:application --log-file - --log-level debug
worker: celery worker --app=tasks.app -B -l info