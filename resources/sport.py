from flask_restful import Resource, reqparse
from bson.json_util import dumps
import json

from flask import request
from bson import ObjectId
from flask import request
import datetime



class Sport(Resource):

    def __init__(self, mongo):
        self.mongo = mongo


    def get(self):

        query = []
        args = request.args

        sportID = args.get('sport-id')
        if sportID is not None:
            query.append({ "$match" : { "_id" : ObjectId(sportID) } })

        data = self.mongo.db.sport.aggregate(query) 
        
        jsonAux = eval(dumps(data))

        #Esta es una de las formas de hallar el resource_id nos podemos quedar con el 0 pq solo lo vamos a usar cuando busquemos un deporte especific
        # por lo que solo deberia tener un elemento.
        resource_id = jsonAux[0]['resource_id']
        
        with open('resources/resource.json', "r") as jsonFile:# Open the JSON file for reading
            data = json.load(jsonFile) # Read the JSON into the buffer
            jsonFile.close() # Close the JSON file
            
            data["resource"] = resource_id

        ## Save our changes to JSON file
        with open('resources/resource.json', "w+") as jsonFile:
            jsonFile.write(json.dumps(data))
            jsonFile.close()

        return jsonAux, 200

