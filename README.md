
# 🚀 AI Website Builder
An intelligent, full-stack web development assistant that generates clean, modular code (HTML, CSS, JS, and Backend) using Llama 3.3 70B and Redis for persistent chat memory.

# ✨ Features
- Intelligent Coding: Powered by llama-3.3-70b-versatile via Groq for lightning-fast code generation.

- Persistent Context: Uses Redis to store and retrieve chat history, allowing the AI to remember your project requirements across sessions.

- Modern UI: A dark-themed, responsive dashboard with real-time Markdown rendering and syntax highlighting.

- Security: Sanitized HTML output via DOMPurify to prevent XSS.

# 📂 Project Structure
```
AI_website_builder/
├── app.py              # Flask server & API routes
├── LLM.py              # LangChain logic & Groq/Redis integration
├── static/
│   ├── style.css       # UI Styling
│   └── script.js       # Frontend logic & Markdown parsing
└── templates/
    └── index.html      # Main Dashboard
```
# 🛠️ Setup Instructions
## 1. Prerequisites
Python 3.10+

A Groq Cloud API Key

A Redis Instance (Local or managed like Upstash)

## 2. Installation

Clone the repository and install the dependencies:

```
git clone git@github.com:bunny-ml/AI_website_builder.git
cd AI_website_builder
pip install -r requirements.txt
```
## 3. Environment Configuration
Create a .env file in the root directory and add your credentials:

Code snippet
```
HOST=your_redis_host
PASSWORD=your_redis_password
GROQ_KEY=your_groq_api_key
```
## 4. Running the App
```

python app.py
Open http://localhost:10000 in your browser.
```

# 🖥️ Usage
- Set User ID: Enter a unique ID in the sidebar to keep your chat history separate.

- Describe your Site: Type requirements like "Create a landing page for a coffee shop with a glassmorphism effect."

- Get Code: The AI will provide separate blocks for HTML, CSS, and JS.

- Copy & Build: Use the syntax-highlighted code blocks to build your project.

# 🔧 Technologies Used
- Backend: Python, Flask

- AI Orchestration: LangChain Core

- LLM: Groq (Llama 3.3 70B)

- Memory: Redis (List-based LTRIM history)