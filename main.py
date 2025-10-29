from flask import Flask, request
import requests

TOKEN = "7832773312:AAHmLIKTV6dTfwiUxst4TVIDOgmWQJJusaQ"
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

@app.route("/")
def home():
    return "بات فعاله ✅"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    data = request.get_json()
    if not data:
        return "no data"

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if text == "/start":
        requests.post(URL + "sendMessage", json={"chat_id": chat_id, "text": "سلام! ربات فعاله 🎮"})

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
