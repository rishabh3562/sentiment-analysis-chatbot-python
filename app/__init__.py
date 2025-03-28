from flask import Flask

def create_app(): 
    app = Flask(__name__)

    from app.routes import chatbot_bp
    app.register_blueprint(chatbot_bp) #same as app.use(router)
 
    return app
    