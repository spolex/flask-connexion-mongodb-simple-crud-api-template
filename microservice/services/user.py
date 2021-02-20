from microservice.storage.models import User
from microservice.exceptions.exceptions import EmailAlreadyExistError, \
    SchemaValidationError, InternalServerError, UserNotFoundError
from mongoengine.errors import NotUniqueError, ValidationError, DoesNotExist, OperationError
from logging import getLogger


class UsersService(object):

    def __init__(self):
        self.logger = getLogger(__name__)
        self.user = None

    def get(self, email: str):
        try:
            user = User.objects(email=email).get()
            self.logger.debug("Found user: " + user.name)
            return user
        except DoesNotExist:
            self.logger.error("Email {} not found into the database".format(email))
            raise UserNotFoundError()
        except Exception as e:
            self.logger.error(e)
            raise InternalServerError()

    def save(self, user: dict):
        try:
            return User(name=user["name"], email=user["email"]).save(force_insert=True)
        except NotUniqueError as e:
            self.logger.error(e)
            raise EmailAlreadyExistError()
        except ValidationError as e:
            self.logger.error(e)
            raise SchemaValidationError()
        except Exception as e:
            self.logger.error(e)
            raise InternalServerError()

    def delete(self, email):
        try:
            user = User.objects(email=email).get()
            user.delete()
            return user
        except DoesNotExist:
            self.logger.error("Email {} not found into the database".format(email))
            raise UserNotFoundError()
        except Exception as e:
            self.logger.error(e)
            raise InternalServerError()

    def update(self, user):
        try:
            User.objects(email=user["email"]).update(name=user["name"])
            return User.objects(email=user["email"]).get()
        except OperationError:
            self.logger.error("Email {} not found into the database".format(user["email"]))
            raise UserNotFoundError()
        except DoesNotExist:
            self.logger.error("Email {} not found into the database".format(user["email"]))
            raise UserNotFoundError()
        except Exception as e:
            self.logger.error(e)
            raise InternalServerError()
