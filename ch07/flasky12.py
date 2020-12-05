#
# Example 7-8 : flask.py :  main Application script
#
import os
from app12 import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")