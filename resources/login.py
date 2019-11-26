from flask_restful import Resource, reqparse
from bson.json_util import dumps
import json
from flask import request
import firebase_admin
from firebase_admin import auth
from models.user import User as User_model
from models.event import Event as Event_model
from models.sport import Sport as Sport_model
from mongoengine import DoesNotExist
import time


class Login(Resource):
    def __init__(self):
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app()

    def post(self):
        jsondata = request.get_json(force=True, silent=True)
        if(jsondata is None):
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['VALUE_ERROR'], 500
        # pylint: disable=E1101
        try:
            decoded_token = auth.verify_id_token(jsondata['token'])
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
            Event_model(
                creation_date=int(time.time()),
                event_date=1554336020,
                title="Evento2",
                description="Lore ipsum. Lore ipsum. Lore ipsum. Lore ipsum.Lore ipsum",
                court_id='Ajedrez',
                creator=user,              
            ).save()
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
