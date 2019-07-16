from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_claims, get_jwt_identity, jwt_required

from app.cache import redis_client

