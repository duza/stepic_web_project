sed 's/goldman\/stepic_web_project/box\/web/g' -i etc/nginx.conf
sed 's/goldman\/stepic_web_project/box\/web/g' -i etc/gunicorn-wsgi.conf
sed 's/goldman\/stepic_web_project/box\/web/g' -i etc/gunicorn-django.conf
sed 's/goldman\/stepic_web_project/box\/web/g' -i ./init.sh
