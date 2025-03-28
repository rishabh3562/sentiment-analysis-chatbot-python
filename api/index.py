from app import create_app

app = create_app()

# Required for Vercel deployment
def handler(event, context):
    return app(event, context)
