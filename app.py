from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://www.tiffinindia.in"}})
  # To allow cross-origin requests from React

# MongoDB Atlas URI
MONGO_URI = os.environ.get("MONGO_STRING")  # Make sure this env variable is set
client = MongoClient(MONGO_URI)  # Connect to MongoDB Atlas
db = client.FeedBacks_and_Requests
collection = db.FeedBacks_and_Requests_collections

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json  # Get the data from the request (as JSON)
    feedback = data.get('feedback')
    rating = data.get('rating')
    email = data.get('email')
    city = data.get('city')

    # Store data in MongoDB
    if feedback and rating and email and city:
        collection.insert_one({'feedback': feedback, 'rating': rating, 'email': email, 'city': city})
        return jsonify({'message': 'Feedback Sent'}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=False)
