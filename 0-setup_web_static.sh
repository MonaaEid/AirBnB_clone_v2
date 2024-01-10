#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
if ! [ -x "$(command -v nginx)" ]; then
    apt-get update
    apt-get intall -y ngnix
fi
# mkdir /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html><head></head><body><h4>hello folks</h4></body></html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
