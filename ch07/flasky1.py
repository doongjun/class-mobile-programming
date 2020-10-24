import os
from app1 import create_app

# Application Script
app = create_app(os.getenv("FLASK_CONFIG") or "default")
