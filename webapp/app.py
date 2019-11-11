# Aaron Burns - app.py
# a python flask app which reads input from a webpage and passes it to a trained model

# Adpated from: https://palletsprojects.com/p/flask/

import flask as fl

app = fl.Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('webpage.html')

app.run()