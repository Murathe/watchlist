from flask import Flask
from .config import DevConfig, config_options
from flask_bootstrap import Bootstrap
from app import views
from app import error

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configuration
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extension
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    return app