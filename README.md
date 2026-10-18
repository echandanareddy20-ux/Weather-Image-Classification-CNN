# 🌦️ Weather Image Classification using CNN

A deep learning project that classifies weather images into four categories: Cloudy, Rainy, Shine, and Sunrise using a Convolutional Neural Network (CNN).

## 📌 Project Overview

Weather image classification is an application of computer vision that identifies weather conditions from images. This project uses a CNN model built with TensorFlow and Keras to learn visual patterns such as cloud formations, brightness, and sky appearance.

The model takes a weather image as input and predicts its corresponding category. The project demonstrates how deep learning can be applied to image classification.

## ✨ Features

- Classification of weather images into four categories
- Image preprocessing and normalization
- CNN-based deep learning model
- Model training and validation
- Prediction on new weather images

## 📂 Dataset

The project uses a multi-class weather image dataset.

**Categories:**
- ☁️ Cloudy
- 🌧️ Rainy
- ☀️ Shine
- 🌅 Sunrise

The images are organized by category and preprocessed before being provided to the CNN model.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| TensorFlow | Deep learning framework |
| Keras | CNN model development |
| NumPy | Numerical operations |
| Matplotlib | Visualization |
| OpenCV | Image processing |
| Git and GitHub | Version control and project hosting |

## 🧠 Model Architecture

The CNN architecture uses layers designed to learn visual features from images.

1. **Convolutional layers:** Extract features such as edges and patterns.
2. **ReLU activation:** Introduces non-linearity into the network.
3. **MaxPooling layers:** Reduce feature-map dimensions.
4. **Flatten layer:** Converts feature maps into a one-dimensional vector.
5. **Dense layers:** Learn relationships between extracted features.
6. **Output layer:** Produces predictions for the weather categories.

## 🔄 Project Workflow

1. Collect the weather image dataset.
2. Organize images into their respective classes.
3. Preprocess the images.
4. Build the CNN model.
5. Train and validate the model.
6. Evaluate model performance.
7. Predict the class of a new image.

## 📊 Results

The trained model predicts one of the four weather categories for an input image.

Model performance should be reported using the actual results obtained during training and evaluation. Accuracy, loss graphs, and a confusion matrix can be added here after verifying the experimental results.

## 🚀 Future Improvements

- Develop a Streamlit web application.
- Allow users to upload images through a graphical interface.
- Display prediction confidence scores.
- Compare CNN with transfer learning models such as MobileNetV2 and VGG16.
- Add evaluation visualizations and deploy the application online.

## 👩‍💻 Author

**Chandana Reddy**

B.Tech – Electronics and Computer Engineering  
REVA University, Bengaluru

GitHub: [echandanareddy20-ux](https://github.com/echandanareddy20-ux)

