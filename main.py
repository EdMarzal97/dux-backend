"""main file for start the app"""
from api import app, db
from models import models

app.app_context().push()
# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    app.run(debug=True)
