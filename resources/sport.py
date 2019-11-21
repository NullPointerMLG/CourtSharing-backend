from flask_restful import Resource, reqparse
from bson.json_util import dumps
<<<<<<< Updated upstream
=======

from flask import request
>>>>>>> Stashed changes
from bson import ObjectId
from flask import request
import datetime



class Sport(Resource):
    resource_id = Unique_sport()

    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):

        query = []
        args = request.args

        sportID = args.get('sport-id')
        if sportID is not None:
            query.append({ "$match" : { "_id" : ObjectId(sportID) } })

        data = self.mongo.db.sport.aggregate(query) 
        
<<<<<<< Updated upstream
        return dumps(data), 200
=======
        json = eval(dumps(data))

        #Esta es una de las formas de hallar el resource_id nos podemos quedar con el 0 pq solo lo vamos a usar cuando busquemos un deporte especific
        # por lo que solo deberia tener un elemento.
        resource_id = json[0]['resource_id']
        print(resource_id)
        print(json[0]['resource_id'])

        return json, 200
>>>>>>> Stashed changes

