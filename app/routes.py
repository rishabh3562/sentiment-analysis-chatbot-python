from flask import Blueprint, request, jsonify
from app.sentiment import analyze_sentiment

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    sentiment_label = analyze_sentiment(user_message)

    # Simple chatbot logic
    bot_response = "I'm here to help!" if sentiment_label == "Positive" else "Tell me more, I'm listening."

    return jsonify({"response": bot_response, "sentiment": sentiment_label})
