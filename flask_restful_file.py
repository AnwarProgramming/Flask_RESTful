# Flask RESTful is an extension for Flask that adds support for quickly building REST APIs.
# It provides tools for creating resources, handling requests, and formatting responses.
from flask import Flask,make_response, jsonify, request
 # pip install flask_restful
from flask_restful import Api, Resource
app = Flask(__name__)

api = Api(app)

user_details = []

class HelloWorld(Resource):
    def get(self, username=None):
        if username is None:
            if not user_details:
                return make_response(jsonify({"message": "No users found"}), 404)
            return make_response(jsonify(user_details), 200)
        for user in user_details:
            if user['username'] == username:
                return make_response(jsonify(user), 200)
        return make_response(jsonify({"error": "User not found"}), 404)
    
    def post(self):
        credentials = request.get_json()
        if 'username' not in credentials or 'address' not in credentials:
            return make_response(jsonify({"error": "Missing username or address"}), 400)
        user_details.append(credentials)
        result = {
            "message": "User added successfully",
            "user":{
                "username": credentials['username'],
                "address": credentials['address']
            }
        }
        return make_response(jsonify(result), 201)


    def put(self):
        pass
    def delete(self):
        pass

api.add_resource(HelloWorld, '/api', '/api/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)