import requests
import json
import socket
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_claims, get_jwt_identity, jwt_required
from app.cache import redis_client
from app.worker import celery
from app.api.user.models import User
from app.api.system.models import SystemSetting, SystemSettingSchema

class SearchApi(Resource):

    @jwt_required
    def post(self):
        
        "Query the spotify api with the given params"
        
        data = request.get_json()
        trackName = data["trackName"]
        query = "%20".join(trackName.split(" "))
        url = "https://api.spotify.com/v1/search?q={}&type=track&market=DE".format(query)
        spotify_token = redis_client.get("spotify_token").decode("utf-8")
        headers = {"Authorization": "Bearer {}".format(spotify_token)}
        r = requests.get(url, headers=headers)
        return r.json(), 201
       
        

class RecorderApi(Resource):
    @jwt_required
    def post(self):
        tracks = {}
        "Record the passed list"
        data = request.get_json()
        tracks['recordList'] = data['recordList']
        settings = SystemSetting.get_settings()
        schema = SystemSettingSchema()
        
        tracks['settings'] = schema.dump(settings).data
        RECORDER_IP = os.getenv("RECORDER_IP")
        PORT = 65432

        s = socket.Socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((RECORDER_IP, PORT))
        
        json_data = json.dumps(tracks)
        
        s.sendall(json_data)
        
        
        return {
            "message": "Jobs wurden erstellt. Nachricht wird verstand wenn fertig."
        }, 201


class TokenCacheApi(Resource):
    @jwt_required
    def post(self):
        """Put the token into the Cache"""
        data = request.get_json()
        spotify_token = data["spotify_token"]
        if redis_client.exists("spotify_token"):
            redis_client.delete("spotify_token")
            redis_client.set("spotify_token", spotify_token)
            saved_token = redis_client.get("spotify_token").decode("utf-8")
            return {
                "message": "Token wurde gespeichert!",
                "spotify_token": saved_token
                }, 201

        


        
