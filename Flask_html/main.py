from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
import pandas as pd
import os

app = Flask(__name__)
model = tf.keras.models.load_model('models/WildFireDetector.h5')


def create_df_img(filepath):
    labels = list(map(lambda x: os.path.split(os.path.split(x)[0])[1], filepath))
    filepath = pd.Series(filepath, name='Filepath').astype(str)
    labels = pd.Series(labels, name='Label')
    df = pd.concat([filepath, labels], axis=1)
    return df


@app.route('/')
def html_file():
    return render_template('Main.html')


@app.route('/process_image', methods=['POST'])
def process_image():

    image_upload = request.files['image']
    file_path = 'Imagefile/' + image_upload.filename

    # Create a directory if it doesn't exist
    if not os.path.exists('Imagefile/'):
        os.makedirs('Imagefile/')

    image_upload.save(file_path)

    # Load the image and preprocess it
    process_img = Image.open(file_path)
    process_img = process_img.resize((350, 350))  # Resize the image to match the input size of the model
    process_img = np.array(process_img)  # Convert the image to a numpy array
    process_img = process_img / 255.0  # Normalize the image
    process_img = np.expand_dims(process_img, axis=0)  # Add an extra dimension for batch

    # Make predictions using the Wildfire Model
    predictions = model.predict(process_img)

    os.remove(file_path)

    # Process the predictions
    if predictions[0][1] > 0.90:
        result = f'Wildfire Occurring! Take Preventive Measures (Probability: {predictions[0][1]})'
    elif predictions[0][1] < 0.03:
        result = f'Looks like the place is safe (Probability: {predictions[0][1]})'
    else:
        result = f'Probability: {predictions[0][1]}'

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
