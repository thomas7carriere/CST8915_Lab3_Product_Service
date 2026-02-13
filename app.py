import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

port = int(os.getenv("PORT", "3030"))

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

@app.get("/products")
def get_products():
    return jsonify([
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
