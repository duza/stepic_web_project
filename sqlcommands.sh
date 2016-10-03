#!/bin/bash
mysql -u root -p -e "CREATE DATABASE django_db;" 
mysql -u root -p -e "CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'mypass';"
mysql -u root -p -e "GRANT ALL PRIVILEGES ON django_db.* TO 'jeffrey'@'localhost';"
mysql -u root -p -e "FLUSH PRIVILEGES;"
