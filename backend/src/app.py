from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/crudapp'
mongo = PyMongo(app)

CORS(app) # using API in rest properly

db = mongo.db.users # collection name
@app.route("/") # set page route with html below
def index():
    return '<h1> Hello World'
if __name__ == '__main__':
    app.run(debug=True)
    #run with python3 backend/src/app.py