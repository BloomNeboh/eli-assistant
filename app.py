from flask import Flask, render_template, request, jsonify
from ai_chat import chat_with_ai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_text = data.get('message')
    
    # Predefined commands
    if "hello" in user_text.lower():
        reply = "Hello, Neboh! How are you today?"
    elif "your name" in user_text.lower():
        reply = "I am Eli, your personal voice assistant!"
    elif "stop" in user_text.lower():
        reply = "Goodbye, Neboh!"
    else:
        # fallback to GPT
        reply = chat_with_ai(user_text)
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)

