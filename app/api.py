# app/api.py
from flask import Flask, request, jsonify
from app.openai_service import generate_text

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    response = generate_text(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
