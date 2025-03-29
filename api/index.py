from app import create_app
from asgiref.wsgi import WsgiToAsgi

app = create_app()
asgi_app = WsgiToAsgi(app)  # Convert WSGI to ASGI (required for Vercel)
