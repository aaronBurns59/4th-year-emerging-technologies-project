# Emerging technologies project
## Machine learning neural newtwork

## Introduction
This project involves using the MNIST dataset to train a neural network to recognise digits sent to the network via a web app that allows the user to draw digits. The neural network or model, will be created in python using the **Keras** library. The web app is a standard HTML, Javascript and CSS configuration. And the two are connected via a python **Flask** server file which will connect to two by sending data from the web app to the neural network in the notebook.

## Repository contents & Layout
### model.ipynb
- This is a jupyter notebook.
- In here keras is used to build a neural network that is trained to recognise digits using the **MNIST** dataset. 
- Not only was the model built and saved in this notebook, I also used it to learn about the neural network and how to manipulate the dataset with numpy.

### model.h5
- This is the model that was saved from the notebook, it is loaded into the flask. 

### webapp
- This folder contains the the flask app, the html webpage and the resources for the webpage.

#### app.py
- This is the flask app server. 
- When ran it loads the resources from the static folder. It also loads the model that was created in the in the notebook. It uses the model to predixt the digit sent from the webpage.

#### static
- This folder contains the directories for the JS and CSS resources.

##### css
- This folder contains the CSS file.

###### style.css
- Contains the styles used in the webapp such as organiseing the canvas and decorating the page.

##### js
- This folder contains the javascript file.

###### script.js
- Contains the scripts used in the web app such as resetting the canvas and sending it to the server.

#### templates/app/html
- Folder that contains the webpage html file that is loaded from the flask server.

##### webpage.html
- Loaded by the flask server, uses the CSS and JS resources to organise and send data to the flask server.

## Tools used 
- Anaconda: A distributed system for working with machine learning in python, it has a lot of inbuilt packages needed like keras, tenorflow, numpy and matplotlib(More on these later).

- Jupyter Notebook: A python development enviroment, it works with python 3.7 and can be used with any python library, It is good for visualising the neural network and learning how it works

- Visual Studio Code: A easy to use IDE for making the Flask server and HTML web app.

## Enviroment set up
### Download Python
Download **Python** version 3.7 through ***Anaconda*** (Works with any OS)
[https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)

Check the version of python, open a cmd/terminal and enter
- python --version

make sure its at least version 3.7.

If you have an older version of anaconda you can update it with
- conda update --all

### Anaconda
Comes with the following packages which will be used in the project
- Keras
- Tensorflow
- numpy
- matplotlib

All you need to install manually is jupyter notebook or jupyter lab.
cmd line for installing jupyter lab
- conda install -c conda-forge jupyterlab
or 
- pip install jupyterlab

## How to run
### Run the notebook 
1. Clone the repository to you machine:
git clone https://github.com/aaronBurns59/4th-year-emerging-technologies-project

2. Navigate to this directory in your CMD/Terminal and enter one of the following to run it:
jupyter lab

3. It will open in an Edge browser by default just copy http://localhost:8888/ into the browser of your choice to rectify this

- If you are interested in changing the default browser to say firefox or chrome, I followed this video to do so
[https://youtu.be/8avwgjr3oTw](https://youtu.be/8avwgjr3oTw)  

## Run the Flask server
1. Navigate to the project directories subdirectory "webapp"  
....\4th-year-emerging-technologies-project\webapp  
- env FLASK_APP=app.py flask run

## Research
### - Keras
keras is a ***high level neural networks API***. It is written in Python and can run on top of Tensorflow (Tensorflow is used in the backend). It is good for those who want to experiment quickly with neural networks in a very streamlined implementation, without knowing exactly how machine learning works. It is easy to used and streamlined to make is more user friendlly and less daunting when building neural networks.

### - NumPy
- Numpy is a python package that is used for manipulating arrays. It offers a lot for functions both building and reshaping the arrays that are used to train the model. And it is used for reshaping the image read in by the digit reader. Numpy is used in both the jupyter notebook and the flask app. I had to use numpy to reshape the canvas image the same as was done to the MNIST dataset in the notebook.

### - One Hot Vector
- A **One Hot Vector** is a way of formating data into a very machine readable format. In the case of this project the one hot vector used was a 1d Array with 9 indices. Each indices represents a digit in the MNIST dataset. In the indices are 0s and a 1. The index that contains the 1 is the digit that is recognised.  
                                                    [0,1,2,3,4,5,6,7,8,9]  
                                                    [0,0,0,0,1,0,0,0,0,0] = 4
### - MNIST
- This is a database of handwritten digits and labels. there are 600000 drawn digits and labels for training a neural network and 100000 drawn digits and labels for training the model of the neural network when it is built. It is commonly used for learning to build neural networks.  

### - Flask
- Flask is a python web application framework that is designed to be quick and eeasy to start. It works with a number of python packages such as the ones used in this project, like keras, numpy and PIL. All of these where used in this project inside a flask app "route". Routes are paths that can contain functions that can be called from the webpage.

## References
[https://keras.io/](https://keras.io/)  
[https://numpy.org/devdocs/user/quickstart.html](https://numpy.org/devdocs/user/quickstart.html)  
[https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/)  
[http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)  
[https://www.palletsprojects.com/p/flask/](https://www.palletsprojects.com/p/flask/)  
