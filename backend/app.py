from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import cv2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model_path = 'CottonPlantDisease.keras'
model = load_model(model_path)

classes = ['Aphids', 'Army worm', 'Bacterial blight', 'Healthy', 'Powdery mildew', 'Target spot']

def process_image(img_path):
    img = image.load_img(img_path, target_size=(160, 160))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    return img_array

def classify_health_status(unhealthy_percentage):
    if unhealthy_percentage >= 71:
        return "Severe"
    elif unhealthy_percentage >= 31:
        return "Mid"
    elif unhealthy_percentage >= 10:
        return "Early"
    else:
        return "Healthy"

def calculate_and_classify_health_status(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    total_pixels = thresholded_image.size
    unhealthy_pixels = np.sum(thresholded_image == 255)
    unhealthy_percentage = (unhealthy_pixels / total_pixels) * 100
    health_status = classify_health_status(unhealthy_percentage)
    return unhealthy_percentage, health_status

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})
    img_file = request.files['image']
    img_path = 'temp.jpg'
    img_file.save(img_path)
    img_array = process_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = classes[np.argmax(predictions)]
    percentage = predictions[0][np.argmax(predictions)]
    leaf_image = cv2.imread(img_path)
    unhealthy_percentage, health_status = calculate_and_classify_health_status(leaf_image)
    os.remove(img_path)
    return jsonify({'prediction': predicted_class, 'percentage': float(percentage), 'health_status': health_status})

if __name__ == '__main__':
    app.run(debug=True)
