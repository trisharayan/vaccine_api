from flask import Flask
from flask_restful import Api
from resources.update import update,delete
from resources.info import infoClass

from resources.login import loginClass,registerClass
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})

api.add_resource(loginClass, "/login",)
api.add_resource(registerClass, "/register",)

api.add_resource(update, "/update")
api.add_resource(infoClass, "/info")
api.add_resource(delete, "/delete")


if __name__ == "__main__":
  app.run()