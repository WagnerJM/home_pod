import requests
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_claims, get_jwt_identity, jwt_required
from app.cache import redis_client

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
    def post(self):
        "Record the passed list"
        data = request.get_json()
        return data["recordList"]


class TokenCacheApi(Resource):
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

        


        
