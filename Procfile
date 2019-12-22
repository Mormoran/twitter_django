web: gunicorn twitter_django.wsgi:application --log-file - --log-level debug
worker: python manage.py celery worker -A twitter_django -B -l info