from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_claims, get_jwt_identity, jwt_required

class RecorderApi(Resource):
    def get(self):
        "Query the spotify api with the given params"
        pass

    def post(self):
        "Record the passed list"
        pass