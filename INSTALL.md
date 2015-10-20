# CLI Explorer

## Installing pre requisites

If you have a virgin Ubuntu server, the following steps will install 
and configure a working environment.


```
  sudo su -
  apt-get install -y apache2 python-dev python-pip git-core
  pip install flask
```

## Install CLI Explorer code

cd /var/www
git clone https://github.com/ronaldbradford/cli_explorer.git
cp cli_explorer/etc/apache2/sites-available/cli_explorer.conf /etc/apache2/sites-available
ln -s /etc/apache2/sites-available/cli_explorer.conf /etc/apache2/sites-enabled
echo "ServerName apache2" > /etc/apache2/conf-enabled/servername.conf
apachectl graceful
