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
echo "ServerName "`hostname` > /etc/apache2/conf-enabled/servername.conf
rm /etc/apache2/sites-enabled/000-default.conf
apachectl graceful
curl -s http://localhost | grep title
```

## Install OpenStack Client

In order to run the various CLI commands these must be installed on server running the web container.


### Install from source

```
git clone https://git.openstack.org/openstack/python-openstackclient
cd python-openstackclient
tox -e py27
. .tox/py27/bin/activate
python setup.py build
python setup.py install
pip install flask
```

### Install from Ubuntu packages

This is an example of using the OpenStack Kilo client tools on Ubuntu 14.04 LTS.

```
  sudo apt-get install -y python-pip
  sudo pip install flask
```

```
  sudo apt-get install ubuntu-cloud-keyring
  echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/kilo main"  | sudo tee /etc/apt/sources.list.d/cloudarchive-kilo.list
  sudo apt-get update
  sudo apt-get install python-openstackclient
```

In addition to installing *openstack*, the other OpenStack clients such as *nova* and *glance* are installed with these commands.


## Verifying API Endpoint

After you have a working environment you can verify the API endpoint with

```
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


If you wish to run this on a public webserver rather than localhost
you will need to alter the configuration in /var/www/cli_explorer/etc/cli_explorer.conf
to define the public url and ip address.


TODO:  Ensure the flask process can run in a daemon process.
