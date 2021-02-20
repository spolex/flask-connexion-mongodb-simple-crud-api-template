from flask_injector import inject

from microservice.services.name import ServiceExample


class Example(object):
    @inject
    def get(self, service: ServiceExample) -> dict:
        """
        """
        r = service.method()
        if r<0.1:
            # 409 HTTP Conflict
            return {"conflict":"Conflicted value"}, 409

        if r<0.3:
            return {"error": "Error value"}, 400

        return {"message": "Success value"}, 201


class_instance = Example()