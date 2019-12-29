from flask import Blueprint
main = Blueprint('min',__name__)
from . import views,errors
