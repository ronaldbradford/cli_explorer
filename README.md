# CLI Explorer

A web interface for exploring the various OpenStack CLI client tools.
A demo runs at http://cli_explorer.ronaldbradford.com

Created by Ronald Bradford <me@ronaldbradford.com>

# Pre Requisites

The User Interface can run in any web container (e.g. Apache).

The API that executes the actual CLI commands currently runs in a Python Flask container.

See the [INSTALL](INSTALL.md) documentation for how to setup a local running copy of CLI Explorer.

# Usage

This tool will run against any running OpenStack installation. It has been tested with:

* devstack - http://devstack.org
* trystack - http://trystack.openstack.org
* Mirantis Express - https://express.mirantis.com
