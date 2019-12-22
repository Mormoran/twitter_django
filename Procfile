web: gunicorn twitter_django.wsgi:application --log-file - --log-level debug
worker: celery worker --app=twitter_django -B -l info