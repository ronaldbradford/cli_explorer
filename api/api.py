#!/usr/bin/env python
from flask import Flask, jsonify, request, abort
from subprocess import Popen, PIPE
import sys
from crossdomain import crossdomain

# Define the web container
api = Flask(__name__)
api.config['SERVER_NAME'] = 'localhost:4242';

# Ensure the API has endpoint discovery
@api.route('/')
@crossdomain(origin='*')
def index():
    return jsonify({'apis' : [ '/api/OSeX' ]})

# Our primary API endpoint
@api.route('/api/OSeX', methods=['POST'])
@crossdomain(origin='*')
def execute():
    # We only accept POST with a JSON data payload
    if not request.json:
      return jsonify({'error': 'Not a valid JSON request'}), 200

    # This request has two required parameters
    required = [ 'command', 'args' ]
    missing=[field for field in required if field not in request.json]
    if missing:
      return jsonify({'error': str(missing)+ ' are required parameters'}), 200
      
    # Obtain the value of passed parameters
    command = request.json['command']
    args = request.json['args']

    # To further hobble this generic execute OS command, we retrict the commands
    valid_commands = [ 'date', 'openstack', 'nova' ]
    if command not in valid_commands:
      return jsonify({'error': 'The supplied command is invalid'}), 200


    # Build the python specific execute command
    execute = [command]
    if (args): 
      args.split(' ')
      execute.append(args)
    api.logger.debug(execute)

    # Execute the command
    p = Popen(execute, stdout=PIPE, stderr=PIPE)

    # Process the commands response
    stdout, stderr = p.communicate()
    rc = p.returncode

    # Return a JSON response
    return jsonify({'execute' : command + " " + args, 'status' : rc, 'stdout' : stdout, 'stderr' : stderr}), 200

if __name__ == '__main__':
    api.run(debug=True)
