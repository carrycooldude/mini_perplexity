# Mini Perplexity Q&A System

## Project Overview and Objectives

**Mini Perplexity Q&A** is a simplified question-answering system that combines the power of a search engine API and a language model to provide users with concise, accurate answers based on recent web information. The system not only generates answers but also includes source citations, offering users transparency about where the information comes from.

### **Objectives**
1. **Primary Goal:** Develop a functional Q&A system that:
   - Accepts user queries.
   - Performs web searches.
   - Generates concise answers using a language model.
   - Provides accurate source citations.

2. **Secondary Goals:**  
   - Demonstrate proficiency in integrating search APIs and language models.
   - Showcase data handling, processing, and response generation.
   - Emphasize best practices in coding, documentation, and user interface design.
   - Justify design decisions to convey thoughtful problem-solving skills.

## Setup and Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/carrycooldude/mini_perplexity.git
   cd mini_perplexity
   ```

2. **Set Up Virtual Environment (Optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **API Key Configuration**
   - Ensure you have valid API keys for both OpenAI and a search API (e.g., Bing, Google).
   - Create a `.env` file and add the following lines, replacing the placeholders with your keys:

     ```
     OPENAI_API_KEY=your_openai_api_key
     SEARCH_API_KEY=your_search_api_key
     ```

5. **Run the Application**
   ```bash
   flask run
   ```

   Access the application in your browser at `http://127.0.0.1:5000`.

## Deployment Steps and Access Details

1. **Prepare for Deployment**
   - Ensure all API keys and sensitive information are stored securely in environment variables.
   - Confirm that all dependencies are listed in `requirements.txt`.

2. **Deploy to Hosting Platform**
   - Deploy to a platform like Heroku, AWS, or any provider that supports Python and Flask apps.
   - Follow platform-specific instructions to configure environment variables for production.

3. **Deployment Link**
   - After deploying, access the application using the deployment URL provided by your platform.

## Usage Guidelines and Example Interactions

1. **Ask a Question**
   - Go to the application’s main page.
   - Enter a question in the input field (e.g., “What is the latest news on AI?”).
   - Submit the form, and the system will fetch information, generate an answer, and display sources.

2. **View Answer and Sources**
   - The answer will be displayed along with sources for transparency.
   - Example interaction:
     - **User Query:** "What is quantum computing?"
     - **Answer:** "Quantum computing is a type of computing that leverages quantum mechanics..."
     - **Sources:** List of URLs that contributed to the answer.

## Design Decisions, Challenges, and Solutions

1. **Design Decisions**
   - **Frontend Simplicity:** Designed a minimalistic and responsive interface to keep user interaction straightforward.
   - **Source Citations:** Added a source citation feature to increase transparency and build user trust.
   - **Error Handling:** Implemented error handling for API limits and network issues, showing user-friendly messages.

2. **Challenges and Solutions**
   - **Handling Rate Limits:** Managed API rate limits by setting up request throttling and handling errors gracefully.
   - **Ensuring Relevance:** Experimented with prompt engineering to ensure responses are both accurate and relevant.
   - **Cross-Platform Compatibility:** Ensured responsiveness and accessibility so the app works smoothly on various devices.

## Potential Areas for Future Improvement

1. **Enhanced Search Capabilities**
   - Integrate additional APIs or a more advanced search engine for improved query handling.

2. **Improved Answer Accuracy**
   - Incorporate feedback loops to refine answer generation based on user interactions.

3. **User Feedback System**
   - Implement a feature for users to rate answers, helping improve response quality.

4. **Extended Language Model Support**
   - Allow users to select different models for answering queries, enhancing flexibility.

5. **Localization**
   - Expand language support to make the app accessible to non-English speaking users.