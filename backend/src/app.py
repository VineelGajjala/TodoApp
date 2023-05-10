from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/crudapp'
mongo = PyMongo(app)

CORS(app) # using API in rest properly

db = mongo.db.users # collection name

# @app.route("/") # set page route with html below
# def index():
#     return '<h1> Hello World'

@app.route('/users', methods=['POST'])
def createUser(): #issue with createUser
    return db.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'contact': request.json['contact'],
        'address': request.json['address']
    }) 
    # request.json is a javascript object of a JSON
@app.route('/testing', methods=['GET']) # get works fine
def attemptTest():
    return 'Hello'
    



if __name__ == '__main__':
    app.run(debug=True)
    #run with python3 backend/src/app.py