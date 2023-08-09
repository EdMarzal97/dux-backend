"""in this file we are implementing the configuration of sqlalchemy and connecting it to the db"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Configuring a database for the Flask application defined above.
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/dux.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
