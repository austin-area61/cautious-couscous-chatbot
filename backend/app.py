# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Define some responses
greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]
default_responses = [
    "I'm not sure how to respond to that.",
    "Can you tell me more?",
    "Interesting, go on.",
    "Let's change the topic.",
]

# Response logic based on user input
def get_response(message):
    message = message.lower()

    # Simple keyword matching
    if "hello" in message or "hi" in message:
        return random.choice(greetings)
    elif "bye" in message or "goodbye" in message:
        return random.choice(farewells)
    elif "how are you" in message:
        return random.choice(["I'm just a bot, but thanks for asking!", "I'm doing great, how about you?"])
    elif "your name" in message:
        return "I'm your friendly chatbot. What's your name?"
    else:
        # Return a random default response
        return random.choice(default_responses)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = get_response(message)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(port=5000)
