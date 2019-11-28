import json
from flask_restful import Resource
from flask import request
import firebase_admin
from firebase_admin import auth
from mongoengine import DoesNotExist
from models.user import User as User_model

class Login(Resource):
    def __init__(self):
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app()

    def post(self):
        args = request.get_json(force=True, silent=True)
        if(args is None):
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['VALUE_ERROR'], 500
        # pylint: disable=E1101
        try:
            decoded_token = auth.verify_id_token(args['data']['token'])
            current_user = auth.get_user(decoded_token['uid'])
            try:             
                user = User_model.objects.get(uuid=current_user.uid)
            except DoesNotExist:
                user = User_model(  
                    uuid=current_user.uid,
                    name=current_user.display_name,
                    photo_url=current_user.photo_url
                )
                user.save()
            return True          
            
        except ValueError:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['VALUE_ERROR'], 500
        except auth.InvalidIdTokenError:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['INVALID_IDTOKEN_ERROR'], 500
        except auth.CertificateFetchError:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['CERTIFICATE_FETCH_ERROR'], 500