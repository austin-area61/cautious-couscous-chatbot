# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from your React frontend

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = f"Hello, {message}!"
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(port=5000)  # Run backend on port 5000
