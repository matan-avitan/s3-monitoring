from flask import Flask
from flask_restful import Api
from logs_api.app.resource.logs import Logs



def create_app():
    app = Flask(__name__)
    api = Api(app)



    # routes
    api.add_resource(Logs, "/api/log/")
    return app
