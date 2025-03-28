from textblob import TextBlob

def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
