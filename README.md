# CLI Explorer

A web interface for exploring the various OpenStack CLI client tools
Created by Ronald Bradford <me@ronaldbradford.com>

# Pre Requisites

The User Interface can run in any web container (e.g. Apache).

The API that executes the actual CLI commands currently runs in a Flask container.

See INSTALL.md for how to setup a local running copy of CLI Explorer.

# Usage

This tool will run against any running OpenStack installation. It has been tested with:

* devstack - http://devstack.org
* trystack - http://trystack.openstack.org/
* Mirantis Express - https://express.mirantis.com
