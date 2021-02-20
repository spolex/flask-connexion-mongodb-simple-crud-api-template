# exceptions.py
from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    code = 500
    description = "Internal Server error"


class SchemaValidationError(HTTPException):
    code = 404
    description = "Schema validation error"


class UserNotFoundError(HTTPException):
    code = 404
    description = "User not found"


class EmailAlreadyExistError(HTTPException):
    code = 404
    description = "Email already exist"
