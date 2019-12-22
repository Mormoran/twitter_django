web: gunicorn twitter_django.wsgi:application --log-file - --log-level debug
worker: python manage.py celery worker -B -l info
celery: python manage.py celery worker -c 3 -B -l info