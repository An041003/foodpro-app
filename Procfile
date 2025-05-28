web: gunicorn foodpro_backend.wsgi:application
release: cd backend && python manage.py collectstatic --noinput && cd .. && npm run --prefix frontend build