import os
from flask import Flask, request, render_template, jsonify
from datetime import datetime
from openai import OpenAI

# --- Configuration ---
# 1. Get your Perplexity API key from https://docs.perplexity.ai/
# 2. Set it as an environment variable named 'PERPLEXITY_API_KEY'.
#    - On Windows: set PERPLEXITY_API_KEY=your_key_here
#    - On macOS/Linux: export PERPLEXITY_API_KEY=your_key_here
# If you don't want to set an environment variable, you can paste your key directly.
# api_key = os.getenv("PERPLEXITY_API_KEY", "YOUR_API_KEY_HERE")
api_key="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"
client = OpenAI(api_key=api_key,base_url="https://api.perplexity.ai")

# Initialize the Flask App
app = Flask(__name__)

# --- Prompt Design ---
# This section remains unchanged.
PROMPTS = {
    "question": {
        "Simple": "Answer the following question clearly and concisely: {user_input}",
        "Detailed": "Provide a detailed explanation for the following question, including background context and key facts: {user_input}",
        "ELI5": "Explain the answer to this question as if I were 5 years old: {user_input}"
    },
    "summarize": {
        "Key Points": "Summarize the following text into a few key bullet points: {user_input}",
        "Comprehensive": "Provide a comprehensive summary of the following text, capturing the main arguments and conclusions: {user_input}",
        "Short Paragraph": "Summarize the following text in a single, well-written paragraph: {user_input}"
    },
    "creative": {
        "Short Story": "Write a short story based on the following idea: {user_input}",
        "Poem": "Compose a short poem inspired by this theme: {user_input}",
        "Ad Copy": "Generate a piece of marketing ad copy for a product described as: {user_input}"
    }
}

def get_ai_response(prompt):
    """
    Sends a prompt to the Perplexity API and gets a response.
    """
    if not api_key:
        return "Please configure your Perplexity API key in app.py to use the AI Assistant."
    try:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]
        
        # Use the Perplexity API client
        response = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# The rest of the file (Flask routes for index and feedback) remains exactly the same.
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route for the web interface. Handles form submission and displays results.
    """
    ai_response = ""
    user_input = ""
    selected_function = "question"
    selected_prompt = "Simple"
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        selected_function = request.form['function_select']
        selected_prompt = request.form['prompt_select']
        
        # Construct the final prompt
        prompt_template = PROMPTS[selected_function][selected_prompt]
        final_prompt = prompt_template.format(user_input=user_input)
        
        # Get the AI response
        ai_response = get_ai_response(final_prompt)

    return render_template('index.html',
                           user_input=user_input,
                           ai_response=ai_response,
                           selected_function=selected_function,
                           selected_prompt=selected_prompt,
                           prompts_json=PROMPTS)

@app.route('/feedback', methods=['POST'])
def feedback():
    """
    Feedback route to log user satisfaction.
    """
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (f"Timestamp: {timestamp}\n"
                 f"Function: {data['function']}\n"
                 f"Prompt Style: {data['prompt']}\n"
                 f"User Input: {data['userInput']}\n"
                 f"AI Response: {data['response']}\n"
                 f"Helpful: {data['helpful']}\n"
                 f"--------------------------------\n")
    
    # Append feedback to a log file
    with open("feedback.log", "a") as f:
        f.write(log_entry)
        
    return jsonify({"status": "success", "message": "Feedback received"})

if __name__ == '__main__':
    app.run(debug=True)