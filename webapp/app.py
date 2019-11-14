# Aaron Burns - app.py
# a python flask app which reads input from a webpage and passes it to a trained model

# Adpated from: https://palletsprojects.com/p/flask/

import flask as fl
import base64
import numpy as np

from io import StringIO
import PIL.Image

app = fl.Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('webpage.html')

@app.route('/predictDigit', methods=['POST'])
def convertImage():
    # get the image from the request
    image = fl.request.values[('imgBase64')]

    return image


# Recommended to have this
if __name__ == "__main__":
    app.run(debug = True)