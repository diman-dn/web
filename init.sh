#!/bin/bash
sudo rm /etc/gunicorn.d/web
sudo rm /etc/gunicorn.d/ask
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/web
#sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
sudo gunicorn -D -b 0.0.0.0:8080 -c /home/box/web/etc/gunicorn.conf hello:app
cd ask/
sudo gunicorn -D -b 0.0.0.0:8000 -c /home/box/web/etc/gunicorn_ask.conf ask.wsgi:application
#sudo /etc/init.d/gunicorn restart

#sudo /etc/init.d/mysql start
