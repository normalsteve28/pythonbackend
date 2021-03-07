'''Here we imported Blueprint from flask, and also Api from flask_restful. 
The imported Api will add some functionality to flask which will help 
us to add routes and simplify some processes.
'''

from flask import Blueprint
from flask_restful import Api
from resources.User import Register
from resources.History import History

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes to access by the application http request
api.add_resource(Register, '/signup')
api.add_resource(History, '/history')
