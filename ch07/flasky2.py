import os
from app2 import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")
