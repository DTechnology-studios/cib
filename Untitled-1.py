
from flask import Flask, render_template, request, jsonify
import openai  # if using ChatGPT

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    # example of ChatGPT integration
    openai.api_key = 'YOUR_OPENAI_KEY'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": prompt}]
    )
    return jsonify({"reply": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)