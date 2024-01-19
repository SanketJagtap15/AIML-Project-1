from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
chatbot_context = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = handle_input(user_input)
    return jsonify({'response': response})


def greet():
    return "Hello! I'm your chatbot. How can I help you today?"


def farewell():
    return "Goodbye! If you have more questions, feel free to ask."


def basic_questions():
    questions = [
        "How are you?",
        "What is your name?",
        "Where are you from?",
        "What do you like to do?",
        "Tell me something interesting."
    ]
    return random.choice(questions)


def handle_input(user_input):
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        return farewell()
    elif "hello" in user_input.lower() or "hi" in user_input.lower():
        return greet()
    elif "previous context" in user_input.lower():
        return f"Previous context: {chatbot_context.get('previous_interaction', 'No previous context.')}"
    else:
        response = "I'm not sure how to respond to that. Can you please ask something else?"
        chatbot_context['previous_interaction'] = user_input
        return response


if __name__ == '__main__':
    app.run(debug=True)
