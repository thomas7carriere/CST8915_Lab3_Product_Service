import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env (local development only)
load_dotenv()

# Fetch PORT from environment, default to 3030
port = int(os.getenv("PORT", "3030"))

# Create Flask app
app = Flask(__name__)

# Enable CORS for all origins (same as allow_any_origin in Warp)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

# Define GET /products route
@app.get("/products")
def get_products():
    return jsonify([
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ])

# Start server (local development only)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)