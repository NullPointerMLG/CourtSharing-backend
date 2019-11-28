import json
import firebase_admin
from firebase_admin import auth
from mongoengine import DoesNotExist
from models.user import User as User_model
import os

class Auth:

    @staticmethod
    def auth_token(args):
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        error_path = os.path.join(dir_path, "errorCodes.json")

        try:
            token = args['token']
            auth.verify_id_token(token)         
            return 'True'
        except (TypeError, KeyError, ValueError):
            with open(error_path, 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['VALUE_ERROR'], 500
        except auth.InvalidIdTokenError:
            with open(error_path, 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['INVALID_IDTOKEN_ERROR'], 500
        except auth.CertificateFetchError:
            with open(error_path, 'r') as errorCodes:
                return json.load(errorCodes)['AUTH_ERROR']['CERTIFICATE_FETCH_ERROR'], 500
