import json
import firebase_admin
from firebase_admin import auth
from mongoengine import DoesNotExist
from models.user import User as User_model

class Auth:

    def auth_token(self, token):
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app()

        try:
            auth.verify_id_token(token)         
            return 'True'              
        except ValueError:
            with open('./errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['VALUE_ERROR'], 500
        except auth.InvalidIdTokenError:
            with open('./errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['INVALID_IDTOKEN_ERROR'], 500
        except auth.CertificateFetchError:
            with open('./errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['CERTIFICATE_FETCH_ERROR'], 500
