from injector import Binder
from flask_injector import FlaskInjector
from microservice.services.name import ServiceExample
from microservice import create_app


def configure(binder: Binder) -> Binder:
    binder.bind(
        ServiceExample,
        ServiceExample()
    )
    return binder


if __name__ == '__main__':
    app = create_app()
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=5000, host='0.0.0.0')