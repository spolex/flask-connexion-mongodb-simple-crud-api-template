# This file initializes your application and brings together all of the various components.
import connexion
from connexion.resolver import RestyResolver
from json import JSONEncoder
from microservice import config
from microservice.storage import initialize_db
from microservice.exceptions.exceptions import *
from microservice.exceptions.renders import *


def create_app():
    """

    :return:
    """
    app = connexion.FlaskApp(__name__, specification_dir='../')
    # This allows the connexion storage to be serialized to JSON
    app.json_encoder = JSONEncoder
    # The return value is a `connexion.Api`.
    # If needed, the api blueprint is available at `connexion.Api.blueprint`
    app.add_api('swagger.yml', resolver=RestyResolver('api'))
    app.app.config.from_object(config)
    app.app.config.from_pyfile('instance/config.py')
    app.add_error_handler(EmailAlreadyExistError, render_not_unique)
    app.add_error_handler(InternalServerError, render_internal)
    app.add_error_handler(SchemaValidationError, render_schema_validation)

    app.app.register_error_handler(UserNotFoundError, render_user_not_found)

    initialize_db(app)

    return app
