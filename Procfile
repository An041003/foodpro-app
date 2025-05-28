web: gunicorn foodpro_backend.wsgi:application
release: python manage.py collectstatic --noinput && npm run --prefix frontend build