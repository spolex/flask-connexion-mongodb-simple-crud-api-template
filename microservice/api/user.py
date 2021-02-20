from flask_injector import inject
from microservice.services.user import UsersService
import logging


class User(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @inject
    def get(self, service: UsersService, email: str) -> dict:
        """
        """
        self.logger.debug("Searching for user with email {}" + email)
        user = service.get(email)
        return user, 201

    @inject
    def delete(self, service: UsersService, email: str) -> dict:
        """
        """
        self.logger.debug("Deleting user with email {}" + email)
        user = service.delete(email)
        return user, 201

    @inject
    def patch(self, service: UsersService, user: dict) -> dict:
        """
        """
        self.logger.debug("Searching for user with email {}".format(user["email"]))
        user = service.update(user)
        return user, 201

    @inject
    def post(self, service: UsersService, user: dict) -> dict:
        """
        """
        self.logger.debug("Saving user: " + user["name"])
        user = service.save(user)
        return user, 201


class_instance = User()
