from flask import Flask, request, jsonify, render_template
import openai
import os
import json
import markdown
import logging

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)


# ファイルへのハンドラを作成します。
file_handler = logging.FileHandler("app.log")

# ハンドラにフォーマッタを設定します。
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# ハンドラをロガーに追加します。
app.logger.addHandler(file_handler)


@app.route("/")
def hello_world():
    return render_template("client.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_data().decode("utf8")
    data = json.loads(data)
    message = data["message"]

    app.logger.info(message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        messages=[
            {
                "role": "system",
                "content": "あなたは優秀なプログラマで、質問に対してとてもわかりやすい回答ができます。正確な回答を得るため、不明瞭なところは質問者に確認してください。",
            },
            {"role": "user", "content": message},
        ],
    )

    chatbot_response = response["choices"][0]["message"]["content"]
    md = markdown.markdown(chatbot_response)

    app.logger.info(chatbot_response)

    return jsonify({"response": md})


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    os.environ["FLASK_ENV"] = "development"
    app.run(host="0.0.0.0", port=5000, debug=True)
