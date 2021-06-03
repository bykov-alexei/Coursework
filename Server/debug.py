from app import app

from app.actions import *
app.run("0.0.0.0", 8000, debug=True)