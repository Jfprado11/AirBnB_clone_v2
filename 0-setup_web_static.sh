#!/usr/bin/env bash
# configurates the server to deploy

# installing nginx
if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
# creates folder /data/
if [ ! -d /data/ ]
then
    sudo mkdir /data/
fi


# creates folder /data/web_static/
if [ ! -d /data/web_static/ ]
then
    sudo mkdir /data/web_static/
fi

# creates folder /data/web_static/releases/
if [ ! -d /data/web_static/releases/ ]
then
    sudo mkdir /data/web_static/releases/
fi

# creates folder /data/web_static/shared
if [ ! -d /data/web_static/shared/ ]
then
    sudo mkdir /data/web_static/shared/
fi

# creates folder /data/web_static/releases/test/
if [ ! -d /data/web_static/releases/test/ ]
then
    sudo mkdir /data/web_static/releases/test/
fi



# creating the html file
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Hello world<h1>
  </body>
</html>" > /data/web_static/releases/test/index.html

# creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership to folder data
sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data/

#adding the location
sudo sed -i "/# pass the PHP/i location /hbnb_static {\n\talias /data/web_static/current/;\n}" /etc/nginx/sites-enabled/default

#restarting nginx
sudo service nginx restart
