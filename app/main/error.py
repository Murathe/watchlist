from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_0w_four(error):
   '''
    Function to render custom 404 error view
   '''
   return render_template('four_0w_four'),404