from flask import Flask

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows for the endpoints / URL to be hit.
@app.route('/')
def hello_world():
	return 'Hello World!'