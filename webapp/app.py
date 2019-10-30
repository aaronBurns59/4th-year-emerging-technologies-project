# Aaron Burns - app.py
# a python flask app which reads input from a webpage and passes it to a trained model

# Adpated from: https://palletsprojects.com/p/flask/

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

app.run()