import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")  # New search API key
SEARCH_API_URL = "https://api.example.com/search"  # Replace with your chosen search API

app = Flask(__name__)

# Function to query the search API for results
def fetch_search_results(query):
    headers = {
        "Authorization": f"Bearer {SEARCH_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "max_results": 5  # Limit the number of results
    }
    response = requests.post(SEARCH_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()  # Adjust based on the actual response structure

# Function to query OpenAI API for response generation
def generate_response(search_results):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": "You are an expert in answering questions based on web information."},
        {"role": "user", "content": f"Answer this based on the following sources: {search_results}"}
    ]
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 200
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle queries
@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    user_query = data.get('query')
    
    # Fetch search results
    search_results = fetch_search_results(user_query)
    
    # Generate response from OpenAI based on search results
    answer = generate_response(search_results)
    
    # Return the response to the frontend, including sources
    return jsonify({"answer": answer, "sources": search_results.get("sources", [])})

if __name__ == '__main__':
    app.run(debug=True)