from flask import Flask, request, jsonify, render_template
import openai
import os
import json

openai.api_key = os.environ.get('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('client.html')

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_data().decode('utf8')
    data = json.loads(data)
    message = data["message"]

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        temperature=0.5,
        max_tokens=60
    )

    chatbot_response = response.choices[0].text.strip()

    return jsonify({"response": chatbot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)