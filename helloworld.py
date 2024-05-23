from flask import Flask, request
from flask_restful import Resource, Api
from ddtrace import tracer
import requests
import json

import logging
from sys import stdout

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
consoleHandler.setFormatter(FORMAT)

app = Flask(__name__)
api = Api(app)

tracer.configure(
    hostname='host.docker.internal',
    port=8126,
)

class Greeting (Resource):
    @tracer.wrap()
    def get(self):
        log.info('Rota Greeting acessada')
        return 'Hello World!'

class Ping (Resource):
    @tracer.wrap()
    def get(self):
        log.info('Rota ping acessada')
        return 'Pong!'

class HttpRequest (Resource):
    @tracer.wrap()
    def get(self):
        r = requests.get('http://localhost:80/ping')
        # return json.dumps(r.content).encode('utf-8')
        return json.dump(r.content).encode('utf-8')

class Health (Resource):
    @tracer.wrap()
    def get(self):
        return 'Ta tudo bem'

api.add_resource(Greeting, '/home') # Route_1
api.add_resource(Ping, '/ping') # Route_2
api.add_resource(HttpRequest, '/httprequest') # Route_3
api.add_resource(Health, '/health') # Route_4

if __name__ == '__main__':
    app.run('0.0.0.0','80')



