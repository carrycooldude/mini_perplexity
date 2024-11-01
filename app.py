import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Function to query OpenAI API for response generation
def generate_response(query):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an expert in answering questions based on web information."},
            {"role": "user", "content": f"Find the most accurate and up-to-date information to answer this question: {query}"}
        ],
        "max_tokens": 200
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # This will raise an HTTPError if the request returned an unsuccessful status code
    return response.json()["choices"][0]["message"]["content"]

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle queries
@app.route('/query', methods=['POST'])
def query():
    try:
        # Use JSON format for incoming data
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Invalid request: 'query' parameter is required"}), 400
        
        user_query = data['query']
        
        # Generate response from OpenAI
        answer = generate_response(user_query)
        
        # Return the response to the frontend
        return jsonify({"answer": answer})
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return jsonify({"error": "Error with the OpenAI API request"}), 500
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred on the server"}), 500

if __name__ == '__main__':
    app.run(debug=True)

