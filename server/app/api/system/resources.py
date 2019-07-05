from flask import request
from flask_restful import Resource

from app.security import admin_required
from app.database import db
from app.api.system.models import SystemSetting, SystemSettingSchema

class SystemSettingApi(Resource):
    def get(self):
        response = {}
        settings = SystemSetting.get_settings()
        schema = SystemSettingSchema()
        response['status'] = "OK"
        reponse['system_settings'] = settings.dump(settings).data

        return response, 200

    def put(self):
        response = {}
        schema = SystemSettingSchema()
        results = schema.load(request.json)

        if not results.errors:
            settings = SystemSetting.query.filter_by(id=1)
            settings.update(request.json)
            db.session.commit()
            response["status"] = "OK"
            settings = SystemSetting.get_settings()
            response["system_settings"] = schema.dump(settings).data
            return response, 200
        else:
            response['status'] = "ERROR"
            return response, 404