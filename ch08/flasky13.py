#
# Example 7-8 : flask.py :  main Application script
#
import os
from app13 import create_app, db
from app13.models import User, Role

app = create_app(os.getenv("FLASK_CONFIG") or "default")

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)