# CLI Explorer

A web interface for exploring the various OpenStack CLI client tools
Created by Ronald Bradford <me@ronaldbradford.com>

# Pre Requisites

The User Interface can run in any web container (e.g. Apache).

The API that executes the actual CLI commands currently runs in a Flask container.

# CLI Commands

In order to run the various CLI commands these must be installed on server running the web container.

This is an example of using the OpenStack Kilo client tools on Ubuntu 14.04 LTS.

```
sudo apt-get install ubuntu-cloud-keyring
echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/kilo main"  | sudo tee /etc/apt/sources.list.d/cloudarchive-kilo.list
sudo apt-get update 
sudo apt-get install python-openstackclient
```

In addition to installing *openstack*, the other OpenStack clients such as *nova* and *glance* are installed with these commands.

# Usage

This tool will run against any running OpenStack installation. It has been tested with:

* devstack
* Mirantis Express
