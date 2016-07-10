#sed 's/goldman\/stepic_web_project/box\/web/g'-i /home/box/web/etc/nginx.conf
sudo ln -fs /home/goldman/stepic_web_project/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
