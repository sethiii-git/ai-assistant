# AI Assistant Web Application

This project is a web-based AI Assistant built with Flask and Python, as specified in the "Major Project for Prompt Engineering" document. It allows users to perform tasks like answering questions, summarizing text, and generating creative content by interacting with an AI model.

## Features

* **Three Core Functions**: Question Answering, Text Summarization, and Creative Content Generation.
* **Dynamic Prompt Selection**: For each function, users can choose from three different prompt styles (e.g., Simple, Detailed, ELI5).
* **Web Interface**: A clean, user-friendly interface built with Flask and HTML.
* **Feedback System**: Users can provide feedback on AI responses, which is logged for analysis.

## Setup and Installation

### 1. Prerequisites

* Python 3.7+
* `pip` package installer

### 2. Clone the Repository

Clone or download this project to your local machine.

### 3. Set Up OpenAI API Key

You need an API key from OpenAI to run this project.

1.  Get your key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2.  Open the `app.py` file.
3.  Find the line `openai.api_key = "YOUR_API_KEY_HERE"`
4.  Replace `"YOUR_API_KEY_HERE"` with your actual key.

### 4. Install Dependencies

Navigate to the project directory in your terminal and install the required Python packages.

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Execute the following command in your terminal:

```bash
flask run
```

The application will start, and you can access it by opening your web browser and navigating to `http://127.0.0.1:5000`.
