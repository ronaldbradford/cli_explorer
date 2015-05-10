#!/usr/bin/env python
#
# Copyright 2015 Ronald Bradford http://ronaldbradford.com
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
from flask import Flask, jsonify, request, abort
from subprocess import Popen, PIPE
from crossdomain import crossdomain
import ConfigParser


cnf = os.path.dirname(os.path.realpath(__file__)) + '/../etc/cli_explorer.cnf'
config = ConfigParser.ConfigParser()
if not config.read(cnf):
  print("Config file '%s' not found" % cnf)
  exit()

config.sections()
section='api'
domain = config.get(section,'domain')
ip = config.get(section,'ip')

# Define the web container
api = Flask(__name__)
api.config['SERVER_NAME'] = domain

# Ensure the API has endpoint discovery
@api.route('/')
@crossdomain(origin='*')
def index():
    return jsonify({'apis' : [ '/api/cli' ]})

# Our primary API endpoint
@api.route('/api/cli', methods=['POST'])
@crossdomain(origin='*')
def execute():
    # We only accept POST with a form POST payload
    # This request has two required parameters
    required = [ 'command', 'args' ]
    #missing=[field for field in required if field not in request.form[field]]
    #if missing:
    #    return jsonify({'error': str(missing)+ ' are required parameters'}), 200
      
    # Obtain the value of passed parameters
    command = request.form['command'].strip()
    args = request.form['args'].strip()

    # To further hobble this generic execute OS command, we retrict the commands
    valid_commands = [ 'date', 'openstack', 'nova' ]
    if command not in valid_commands:
        return jsonify({'error': 'The supplied command is invalid'}), 200


    # Build the python specific execute command
    execute = [command]
    if (args): 
        execute += args.split(' ')

    api.logger.info('Executing ' + str(execute))

    # Execute the command
    p = Popen(execute, stdout=PIPE, stderr=PIPE)

    # Process the commands response
    stdout, stderr = p.communicate()
    rc = p.returncode

    # Return a JSON response
    return jsonify({'execute' : command + " " + args, 'status' : rc, 'stdout' : stdout, 'stderr' : stderr}), 200

if __name__ == '__main__':
    api.run(host=ip, debug=True)
