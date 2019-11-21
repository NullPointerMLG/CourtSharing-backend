from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import firebase_admin
from firebase_admin import auth
from models.user import User

class Login(Resource):
    def __init__(self, mongo):
        self.mongo = mongo
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app()      

    def post(self):     
        jsondata = request.get_json(force=True)
        if jsondata is None:
            return False
        try:
            decoded_token = auth.verify_id_token(jsondata['token']) 
            current_user = auth.get_user(decoded_token['uid']) 
            user = self.mongo.db.user.find({'UUID':current_user.uid})    
            if user.count() == 0:
                User.uuid = current_user.uid
                User.name = current_user.display_name
                User.photoURL = current_user.photo_url
                self.mongo.db.user.insert({'name':current_user.display_name, 'UUID':current_user.uid, 'photoURL':current_user.photo_url})
            return True
        except ValueError:
            return False
        except auth.InvalidIdTokenError:
            return False
        except auth.CertificateFetchError:
            return False
        
