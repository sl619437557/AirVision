from flask import Blueprint

airviz = Blueprint('airviz', __name__)

from . import views
from . import test