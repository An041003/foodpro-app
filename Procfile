web: gunicorn foodpro_backend.wsgi:application
release: python manage.py collectstatic --noinput && npx --prefix frontend build