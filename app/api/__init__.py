from flask import Blueprint

routes = Blueprint('routes', __name__)

from .api_login import *
from .api_register import *
