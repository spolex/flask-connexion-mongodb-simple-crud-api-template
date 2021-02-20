from flask import Response
import json


def render_not_unique(exception):
    return Response(response=json.dumps({'EmailAlreadyExist':
                                             "User with specified email already exists in database"}),
                    status=400, mimetype="application/json")


def render_internal(exception):
    return Response(response=json.dumps({'InternalServerError': "Oops something wrong"}),
                    status=500, mimetype="application/json")


def render_schema_validation(exception):
    return Response(response=json.dumps({'SchemaValidationError': "Required fields missing"}),
                    status=400, mimetype="application/json")


def render_user_not_found(exception):
    return Response(response=json.dumps({'UserNotFoundError': "User not found"}),
                    status=409, mimetype="application/json")
