Cotton Leaf Disease Detection

A full-stack deep learning web application that detects diseases in cotton leaves using a trained MobileNetV2-based CNN model. Users can upload an image and receive instant disease classification results.

Project Overview

This project helps in early detection of cotton leaf diseases using deep learning, which can assist farmers in reducing crop loss and improving yield.

The system uses:

A trained CNN model (MobileNetV2)
Flask backend for prediction API
HTML/CSS/JavaScript frontend for user interaction

✨ Features
📤 Upload cotton leaf images
🧠 AI-based disease prediction
⚡ Fast real-time results
📊 High accuracy (~93%)
🌐 Simple and user-friendly web interface

🛠️ Technologies Used
Backend
Python
Flask
TensorFlow / Keras
OpenCV
NumPy
Frontend
HTML
CSS
JavaScript
Model
MobileNetV2 (Transfer Learning)
CNN (Convolutional Neural Network)

📂 Dataset Information
Source: Kaggle dataset
Total Images: ~4,800+
Classes: 6 disease categories
Each class divided into:
Early stage
Mid stage
Severe stage

📊 Model Performance
Accuracy: 93%
Trained using:
Data augmentation
Pretrained MobileNetV2
Fine-tuning for better accuracy

🏗️ Project Structure
cotton-leaf-disease-detection/
│
├── backend/
│   ├── app.py
│   ├── CottonPlantDisease.keras
│
├── frontend/
│   ├── index.html
│   ├── predict.html
│   ├── css/
│   ├── js/
│   └── vendor/
│
├── Cotton_Leaf_Disease_Detection.ipynb
├── requirements.txt
└── .gitignore

⚙️ Installation & Setup
1. Clone repository
git clone https://github.com/shivanij002/cotton-leaf-disease-detection.git
cd cotton-leaf-disease-detection
2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run backend server
cd backend
python app.py

▶️ How it works
User uploads cotton leaf image
Image is sent to Flask backend
Model processes image using MobileNetV2
Prediction is returned (disease class + stage)
Result is displayed on UI

📸 Screenshots

🔮 Future Improvements
🌱 Mobile app version
☁️ Cloud deployment (AWS / Azure)
📡 Live camera detection
📊 Disease severity visualization dashboard

👩‍💻 Author

Shivani J

GitHub: https://github.com/shivanij002
Project: Cotton Leaf Disease Detection
⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!