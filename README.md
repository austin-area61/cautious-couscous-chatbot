# Chatbot Project

This is a simple chatbot application built using a Flask backend and a React frontend. The chatbot responds to user inputs with random, dynamic responses based on keyword detection. It also has a simple UI where users can interact with the bot.

## Features

- **User Input Handling:** The bot accepts user input from a text box and responds based on keyword detection.
- **Dynamic Responses:** Uses random selection from a list of predefined responses to keep interactions varied.
- **Backend:** Flask is used to handle HTTP requests and serve chatbot responses.
- **Frontend:** React is used to create the UI for interacting with the chatbot.
- **Cross-Origin Resource Sharing (CORS):** Enabled to allow communication between the React frontend and Flask backend.

## Prerequisites

- **Python 3.x** (for the backend)
- **Node.js and npm** (for the frontend)
- **Flask**: Install using `pip install flask flask-cors`
- **React**: Generated using `create-react-app`

Future Improvements
- Integrating a more sophisticated NLP library like spaCy or OpenAI's GPT-3 for advanced chatbot capabilities.
- Add user authentication and persistence (e.g., storing chat history in a database).
- Improve the UI with more interactive elements, such as buttons for frequently used responses.
