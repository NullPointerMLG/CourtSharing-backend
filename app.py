from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import mongoengine
from resources.events import Events
from resources.event import Event
from resources.court import Court
from resources.courts import Courts
from resources.sport import Sport
from resources.login import Login
from resources.transport import Transport
from resources.parking import Parking
from resources.comments import Comments
from resources.comment import Comment
from resources.image import Image
from config import MONGO_URL


mongoengine.connect(alias="default", host=MONGO_URL)

app = Flask(__name__)
CORS(app)
api = Api(app)


# Endpoints
api.add_resource(Events, '/events')
api.add_resource(Event, '/events/<string:id>')
api.add_resource(Login, '/login')
api.add_resource(Courts, '/courts')
api.add_resource(Court, '/courts/<string:id>')
api.add_resource(Sport, '/sports')
api.add_resource(Transport, '/transports')
api.add_resource(Parking, '/parkings')
api.add_resource(Comments, '/comments')
api.add_resource(Comment, '/comments/<string:id>')
api.add_resource(Image, '/image')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
