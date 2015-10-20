# CLI Explorer

## Installing pre requisites

If you have a virgin Ubuntu server, the following steps will install 
and configure a working web environment and OpenStack dev environment.


```
  sudo apt-get install -y apache2 git-core
```

## Install CLI Explorer code

```
  sudo su -
  cd /var/www
  git clone https://github.com/ronaldbradford/cli_explorer.git
  cp cli_explorer/etc/cli_explorer.cnf.example cli_explorer/etc/cli_explorer.cnf
  cp cli_explorer/etc/apache2/sites-available/cli_explorer.conf /etc/apache2/sites-available
  ln -s /etc/apache2/sites-available/cli_explorer.conf /etc/apache2/sites-enabled
  echo "ServerName apache2" > /etc/apache2/conf-enabled/servername.conf
  apachectl graceful
```



## Install OpenStack Client

```
  git clone https://git.openstack.org/openstack/python-openstackclient
  cd python-openstackclient
  tox -e py27
  . .tox/py27/bin/activate
  python setup.py build
  python setup.py install
  pip install flask

  python /var/www/cli_explorer/api/api.py 
```

In a different session you can validate the API endpoint is working with:


```
  curl http://localhost:4242/api

{
  "apis": [
    "/api/cli"
  ]
}
```


If you wish to run this on a public webserver rather then localhost
you will need to alter the configuration in /var/www/cli_explorer/etc/cli_explorer.conf
