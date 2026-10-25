from flask import Flask, request
import os, requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Davenport Bot is Live!"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return request.args.get("hub.challenge"), 200
    return "OK", 200

if __name__ == "__main__":
    app.run()
