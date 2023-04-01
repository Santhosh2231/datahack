

from flask import Flask
from flask_restful import Api
from routes.routes import recommendations_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)
recommendations_routes(api)

if __name__=="__main__":
    app.run(debug=True)