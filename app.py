from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def ai_javob(text):
    text = text.lower()

    if "headache" in text:
        return "You may have a headache. Drink water and rest."
    elif "fever" in text:
        return "You might have a fever. Check your temperature."
    elif "help" in text:
        return "Call emergency services immediately!"
    else:
        return "I am your AI doctor 🤖. Tell me your symptoms."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = ai_javob(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)