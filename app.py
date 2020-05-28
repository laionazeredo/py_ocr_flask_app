"""
This module implements a simple server to handle requests from frontend and route to API endpoints.
The standard port is 5000
"""

import os
from flask import Flask, render_template, request

# import our OCR engine
from ocr_engine.ocr_engine import ocr_engine as ocre

# define a folder to store and later serve the images
UPLOAD_FOLDER = './static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# route and function to handle the upload page
@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('index.html', msg='No file selected')
        file = request.files['file']

        # if no file is selected
        if file.filename == '':
            return render_template('index.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR emgine on it
            result= ocre(file)

            # extract the text and display it
            return render_template('index.html',
                                   msg='Successfully processed',
                                   extracted_text=result["text"],
                                   img_src=UPLOAD_FOLDER + file.filename,
                                   average_confidence=result["average_confidence"])
                                   
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run()