# Aaron Burns - app.py
# a python flask app which reads input from a webpage and passes it to a trained model

# Adpated from: https://palletsprojects.com/p/flask/

import flask as fl
import base64
import numpy as np
import keras as kr
from PIL import Image, ImageOps
import cv2

app = fl.Flask(__name__)

@app.route('/')
def home():
    #return app.send_static_file('webpage.html')
    return fl.render_template('app/html/webpage.html')

@app.route('/predictDigit', methods=['POST'])
def convertImage():

    # get the image from the request
    encodedImage = fl.request.values[('imgBase64')]
    # decode the dataURL
    # remove the added part of the url start from the 22 index of the image array
    decodedImage = base64.b64decode(encodedImage[22:])
    # save the image
    with open('image.png', 'wb') as f:
        f.write(decodedImage)
        
    # Dimension of the image needed
    size=(28,28)
    # reload the png from the folder
    # bypass this once you get it working!!!
    drawnDigit = Image.open('image.png')
    # Resize the image
    newImage = ImageOps.fit(drawnDigit, size, Image.ANTIALIAS)
    # save the image after its been resized
    newImage.save('resizedImage.png')
    # reopedn the image now that its resized
    resizedImage = cv2.imread('resizedImage.png')
    # Set the image to gray scale
    grayScaleImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
    # pass the image into an ndarray using  numpy and manipulate it the same way the mnist were in the model
    imageArray = np.array(grayScaleImage).reshape(1, 784).astype("Float32") / 255

    # env FLASK_APP=app.py flask run
    # Have to load the model in here or else you get an issue with tensorflow
    model = kr.models.load_model('../model.h5')
    # setting the predicted digit based on the npArray
    setPrediction = model.predict(imageArray)
    # getting the digit value of the npArray above
    getPrediction = np.array(setPrediction[0])
    # using the model to predict the digit when compared to the trained model
    predictedDigit = str(np.argmax(getPrediction))
    # printing the digit for clarification
    print("Prediction: " + predictedDigit)

    return predictedDigit

if __name__ == '__main__':
    app.run(debug=true, threaded = false)