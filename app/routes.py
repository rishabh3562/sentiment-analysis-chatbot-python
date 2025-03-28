from flask import Blueprint, request, jsonify, render_template
from app.sentiment import analyze_sentiment

# below same as express.Router() so chatbot routes are being created
chatbot_bp = Blueprint("chatbot", __name__, template_folder="../templates")  # Adjust path

@chatbot_bp.route("/")
def home():
    return render_template("index.html")  # Should now find it

@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    sentiment_label = analyze_sentiment(user_message)
    bot_response = "I'm happy to hear that!" if sentiment_label == "Positive" else "Tell me more!"

    return jsonify({"response": bot_response, "sentiment": sentiment_label})
