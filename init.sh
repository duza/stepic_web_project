sudo ln -fs etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -fs etc/gunicorn-wsgi.conf   /etc/gunicorn.d/test-wsgi
sudo ln -fs etc/gunicorn-django.conf   /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
